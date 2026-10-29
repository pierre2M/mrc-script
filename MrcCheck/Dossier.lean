-- SPDX-License-Identifier: AGPL-3.0-only
import Lean.Data.Json

/-! # Décodage d'un dossier du pilote C (`schema/ecriture_duale.schema.json`)

Lecture seule des champs nécessaires au contrôle. Un champ requis absent ou
mal typé produit `DONNEE_MANQUANTE` (le motif nomme le champ). La conformité
complète au schéma est vérifiée séparément (`tools/check_vectors.py`, CI). -/

namespace MrcCheck
open Lean (Json)

structure AncrageJ where
  traduction  : Option String
  communalite : Option String   -- objet `inscription_communalite_uri_ref`, compressé
  tripletComplet : Bool          -- sans objet si `communalite = none`
  deriving Repr

structure LigneJ where
  id : String
  contrepartie : String
  typage : String
  montant : Nat
  deriving Repr

structure DeclJ where
  titulaire : String
  nature : String
  inclusion : Option String
  concernes : Array String
  ecrivant : String
  interprete : Option String
  mode : String
  reexamen : Option Nat
  deriving Repr

structure MaintienJ where
  porteur : String
  contrepartie : String
  registre : String
  du : Nat
  paye : Nat
  horizon : Nat
  critere : String
  deriving Repr

structure RegistreJ where
  teneur : String
  ancrage : AncrageJ
  lignes : Array LigneJ
  communication : Option String
  milieu : Option (DeclJ × Option MaintienJ)
  deriving Repr

structure DesigJ where
  registre : String
  inst : String
  mode : String
  deriving Repr

structure DossierJ where
  schemaVersion : String
  dossierId : String
  ntarch : String
  arbre : String
  date : Nat
  A : RegistreJ
  B : RegistreJ
  designations : Option (Array DesigJ)
  deriving Repr

abbrev D := Except String

def champ (j : Json) (k : String) (ctx : String) : D Json :=
  match j.getObjVal? k with
  | .ok v => .ok v
  | .error _ => .error s!"{ctx}.{k} absent"

def chaine (j : Json) (k ctx : String) : D String := do
  match (← champ j k ctx).getStr? with
  | .ok s => pure s
  | .error _ => throw s!"{ctx}.{k} : chaîne attendue"

def naturel (j : Json) (k ctx : String) : D Nat := do
  match (← champ j k ctx).getNat? with
  | .ok n => pure n
  | .error _ => throw s!"{ctx}.{k} : entier naturel attendu"

/-- Champ optionnel : absent ou `null` donnent `none`. -/
def optionnel (j : Json) (k : String) : Option Json :=
  match j.getObjVal? k with
  | .ok .null => none
  | .ok v => some v
  | .error _ => none

def tableau (j : Json) (k ctx : String) : D (Array Json) := do
  match (← champ j k ctx).getArr? with
  | .ok a => pure a
  | .error _ => throw s!"{ctx}.{k} : tableau attendu"

def optChaine (j : Json) (k ctx : String) : D (Option String) :=
  match optionnel j k with
  | none => pure none
  | some v => match v.getStr? with
    | .ok s => pure (some s)
    | .error _ => throw s!"{ctx}.{k} : chaîne ou null attendu"

def optNaturel (j : Json) (k ctx : String) : D (Option Nat) :=
  match optionnel j k with
  | none => pure none
  | some v => match v.getNat? with
    | .ok n => pure (some n)
    | .error _ => throw s!"{ctx}.{k} : entier ou null attendu"

def decAncrage (j : Json) (ctx : String) : D AncrageJ := do
  let tr ← optChaine j "traduction_uri_ref" ctx
  match optionnel j "inscription_communalite_uri_ref" with
  | none => pure ⟨tr, none, true⟩
  | some ic =>
    let tp := optionnel ic "triplet_porteur"
    let present (k : String) : Bool :=
      match tp.bind (fun t => optionnel t k) with
      | some (.str s) => !s.isEmpty
      | _ => false
    pure ⟨tr, some ic.compress, present "entite" && present "personne" && present "role"⟩

def decLigne (j : Json) (ctx : String) : D LigneJ := do
  let m ← champ j "montant" ctx
  pure ⟨← chaine j "id" ctx, ← chaine j "contrepartie" ctx, ← chaine j "typage" ctx,
        ← naturel m "valeur" (ctx ++ ".montant")⟩

def decDecl (j : Json) (ctx : String) : D DeclJ := do
  let cs ← (← tableau j "concernes" ctx).mapM fun c => match c.getStr? with
    | .ok s => pure s
    | .error _ => throw s!"{ctx}.concernes : chaînes attendues"
  pure ⟨← chaine j "titulaire" ctx, ← chaine j "nature" ctx, ← optChaine j "inclusion" ctx, cs,
        ← chaine j "ecrivant" ctx, ← optChaine j "interprete" ctx, ← chaine j "mode" ctx,
        ← optNaturel j "reexamen" ctx⟩

def decMaintien (j : Json) (ctx : String) : D MaintienJ := do
  let s ← champ j "situation" ctx
  pure ⟨← chaine j "porteur" ctx, ← chaine j "contrepartie" ctx, ← chaine j "registre" ctx,
        ← naturel s "du" (ctx ++ ".situation"), ← naturel s "paye" (ctx ++ ".situation"),
        ← naturel j "horizon" ctx, ← chaine j "critere" ctx⟩

def decRegistre (j : Json) (ctx : String) : D RegistreJ := do
  let lignes ← (← tableau j "lignes" ctx).mapM (decLigne · (ctx ++ ".lignes"))
  let milieu ← match optionnel j "registre_du_milieu" with
    | none => pure none
    | some m => do
      let d ← decDecl (← champ m "declaration" (ctx ++ ".registre_du_milieu")) (ctx ++ ".registre_du_milieu.declaration")
      let mt ← match optionnel m "maintien" with
        | none => pure none
        | some x => some <$> decMaintien x (ctx ++ ".registre_du_milieu.maintien")
      pure (some (d, mt))
  pure ⟨← chaine j "teneur" ctx, ← decAncrage (← champ j "ancrage" ctx) (ctx ++ ".ancrage"), lignes,
        ← optChaine j "communication" ctx, milieu⟩

def decDossier (j : Json) : D DossierJ := do
  let r ← champ j "reference" "dossier"
  let regs ← champ j "registres" "dossier"
  let ds ← match optionnel j "designations_controle" with
    | none => pure none
    | some _ => some <$> (← tableau j "designations_controle" "dossier").mapM fun x =>
        return ⟨← chaine x "registre" "designation", ← chaine x "instance" "designation",
                ← chaine x "mode" "designation"⟩
  pure ⟨← chaine j "schema_version" "dossier", ← chaine j "dossier_id" "dossier",
        ← chaine r "ntarch_sha256" "reference", ← chaine r "profreg_arbre" "reference",
        ← naturel j "date_controle" "dossier",
        ← decRegistre (← champ regs "A" "registres") "registres.A",
        ← decRegistre (← champ regs "B" "registres") "registres.B", ds⟩

end MrcCheck
