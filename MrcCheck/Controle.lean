-- SPDX-License-Identifier: AGPL-3.0-only
import MrcCheck.Dossier
import ProfReg.PR31_BonneFormationDeclarative
import ProfReg.PR35_EcritureDuale
import ProfReg.PR37_RegistreDuMilieu
import ProfReg.PR40_StatutDeLEcart
import ProfReg.PR43_InstanceDeControle

/-! # Contrôle formel du pilote C et reçu

Chaque calcul appelle une définition de ProfReg (`ancree`, `ancreeDuale`,
`etatRapprochement`, `EcritureDuale`, `lignesVers`, `Concordante`,
`declarationValide`, `bienForme`, `ecartEnversMilieu`, `instanceCommune`,
`ecartQualifie`, `MaintienCONV11.solde`). Ce module n'en redéfinit aucune : il
encode le dossier (identités en `Nat`, règle des deux portes de PR-31), applique
l'ordre des effets (Annexe §A.15.11, table `rules/pilote_C`) et rédige le reçu.

Exception déclarée : C-09 (triplet porteur) n'a pas de prédicat dans ProfReg ;
c'est une vérification de présence de champs, faite au décodage.

Le reçu ne porte jamais `VALIDE` ni `OPPOSABLE` : le type `Statut` ne les a pas. -/

namespace MrcCheck
open Lean (Json)
open ProfRegPR35 (Registre Ligne)

/-- Les seuls statuts que le reçu peut porter (programme, phase 2b). -/
inductive Statut where
  | formellementBienFormee | formellementIncomplete | controleNonApplicable
  | controleEchoue | donneeManquante | ecartDeVersion
  deriving DecidableEq, Repr, Inhabited

def Statut.texte : Statut → String
  | .formellementBienFormee => "FORMELLEMENT_BIEN_FORMEE"
  | .formellementIncomplete => "FORMELLEMENT_INCOMPLETE"
  | .controleNonApplicable  => "CONTROLE_NON_APPLICABLE"
  | .controleEchoue         => "CONTROLE_ECHOUE"
  | .donneeManquante        => "DONNEE_MANQUANTE"
  | .ecartDeVersion         => "ECART_DE_VERSION"

structure Effet where
  regle : String
  code : String
  marqueur : Option String
  deriving Repr

/-- Effet MRC du défaut (Annexe §A.15.11) : refus, délibération, marqueur, attente. -/
def nature : String → String
  | "E1" => "refus" | "E3" => "deliberation" | "E0" | "E2" => "attente" | _ => "marqueur"

/-- Rang d'un code dans l'ordre des effets ; le premier rang atteint fixe le statut. -/
def rang : String → Nat
  | "E1" => 0 | "E0" | "E2" => 1 | "E3" | "E4" => 2 | _ => 3

def statutDe (es : List Effet) : Statut :=
  match (es.map (rang ·.code)).min? with
  | some 0 => .controleEchoue
  | some 1 => .controleNonApplicable
  | some 2 => .formellementIncomplete
  | _      => .formellementBienFormee

/-! ## Encodage -/

/-- Table d'identités : ordre de première apparition dans un parcours fixe. -/
def table (xs : List String) : Array String :=
  xs.foldl (fun t s => if t.contains s then t else t.push s) #[]

def idx (t : Array String) (s : String) : Nat := (t.findIdx? (· == s)).getD t.size

def entites (d : DossierJ) : List String :=
  let reg (r : RegistreJ) : List String :=
    [r.teneur] ++ (r.lignes.toList.map (·.contrepartie)) ++
    (match r.milieu with
     | none => []
     | some (dc, mt) => [dc.titulaire] ++ dc.concernes.toList ++ [dc.ecrivant] ++ dc.interprete.toList ++
         (match mt with | none => [] | some m => [m.porteur, m.contrepartie, m.registre]))
  reg d.A ++ reg d.B ++ ((d.designations.getD #[]).toList.flatMap fun x => [x.registre, x.inst])

def codes (d : DossierJ) : List String :=
  let reg (r : RegistreJ) : List String :=
    (r.ancrage.traduction.toList.map ("tr:" ++ ·)) ++ (r.ancrage.communalite.toList.map ("co:" ++ ·)) ++
    (match r.milieu with
     | none => []
     | some (dc, mt) => (dc.inclusion.toList.map ("inc:" ++ ·)) ++ (mt.toList.map ("crit:" ++ ·.critere)))
  reg d.A ++ reg d.B

def typage : String → Option ProfRegPR20.TypageIA
  | "C+" => some .Cplus | "D+" => some .Dplus | "C-" => some .Cmoins | "D-" => some .Dmoins | _ => none

def typageTexte : ProfRegPR20.TypageIA → String
  | .Cplus => "C+" | .Dplus => "D+" | .Cmoins => "C-" | .Dmoins => "D-"

/-! ## Reçu -/

structure Recu where
  statut : Statut
  effets : List Effet
  calculs : Json
  motif : Option String

instance : Inhabited Recu := ⟨⟨.donneeManquante, [], Json.null, none⟩⟩

def ligneJson (te : Array String) (l : Ligne Nat) : Json :=
  Json.mkObj [("contrepartie", Json.str (te.getD l.contrepartie "?")), ("typage", Json.str (typageTexte l.typage)),
              ("montant", Json.num (l.montant : Nat))]

def colonne (te : Array String) (ls : List (Ligne Nat)) : Json :=
  Json.arr (ls.map (ligneJson te)).toArray

def effetJson (e : Effet) : Json :=
  Json.mkObj ([("regle", Json.str e.regle), ("code", Json.str e.code), ("effet", Json.str (nature e.code))] ++
    (match e.marqueur with | some m => [("marqueur", Json.str m)] | none => []))

def statutEcartTexte : ProfRegPR40.StatutEcart → String
  | .constate => "constate" | .nonVerifiable => "nonVerifiable" | .refuse => "refuse" | .conteste => "conteste"

/-! ## Contrôle -/

def controler (d : DossierJ) : Except Recu Recu := do
  let echec (st : Statut) (m : String) : Recu := ⟨st, [], Json.null, some m⟩
  if d.schemaVersion != "pilote-C/0.1" then
    throw (echec .controleNonApplicable s!"schema_version {d.schemaVersion} : seul pilote-C/0.1 est contrôlé")
  if d.A.milieu.isSome then
    throw (echec .controleNonApplicable "registre du milieu côté A : hors du pilote C (côté B seulement)")
  let te := table (entites d)
  let tc := table (codes d)
  let E := idx te
  let K := idx tc
  let lignes (r : RegistreJ) : Except Recu (List (Ligne Nat)) :=
    r.lignes.toList.mapM fun l => match typage l.typage with
      | some t => pure ⟨E l.contrepartie, t, l.montant⟩
      | none => throw ⟨.controleEchoue, [⟨"C-03", "E1", none⟩], Json.null,
                       some s!"ligne {l.id} : typage {l.typage} hors de C+, D+, C-, D-"⟩
  let RA : Registre Nat := ⟨E d.A.teneur, ← lignes d.A⟩
  let RB : Registre Nat := ⟨E d.B.teneur, ← lignes d.B⟩
  let anc (r : RegistreJ) : ProfRegPR31.EcritureT :=
    ⟨r.ancrage.traduction.map (K ∘ ("tr:" ++ ·)), r.ancrage.communalite.map (K ∘ ("co:" ++ ·))⟩
  -- C-01, C-02 : ancrage de l'écriture duale (PR-31, D7)
  let ancA := ProfRegPR31.ancree (anc d.A)
  let ancB := ProfRegPR31.ancree (anc d.B)
  let distincts := decide (RA.teneur ≠ RB.teneur)
  let ancDuale := ProfRegPR31.ancreeDuale ⟨RA.teneur, anc d.A⟩ ⟨RB.teneur, anc d.B⟩
  let base : List (String × Json) :=
    [("ancrage", Json.mkObj [("A", Json.bool ancA), ("B", Json.bool ancB)]), ("teneurs_distincts", Json.bool distincts),
     ("ancrage_duale", Json.bool ancDuale)]
  if !ancDuale then
    let e : Effet := if ancA && ancB then ⟨"C-02", "E1", none⟩ else ⟨"C-01", "E1", none⟩
    return ⟨.controleEchoue, [e], Json.mkObj base, none⟩
  let mut effets : List Effet := []
  let mut champs := base
  -- C-04 (via PR-37 si B est le registre d'un milieu), C-07, C-08
  match d.B.milieu with
  | none =>
    let (ca, cb) := ProfRegPR35.etatRapprochement RA RB
    champs := champs ++ [("etat_rapprochement", Json.mkObj [("A_vers_B", colonne te ca), ("B_vers_A", colonne te cb)]),
                         ("ecriture_duale", Json.bool (decide (ProfRegPR35.EcritureDuale RA RB))), ("milieu", Json.null)]
  | some (dc, mt) =>
    if h : RB.teneur = E dc.titulaire then
      let nat : ProfRegPR37.NatureTitulaire := if dc.nature == "milieu" then .milieu else .collectifHumain
      let mode : ProfRegPR37.ModeDeclaration :=
        if dc.mode == "arretee" then .arretee else if dc.mode == "ratifiee" then .ratifiee else .nonDeclare
      let decl : ProfRegPR37.DeclarationConcernes :=
        ⟨E dc.titulaire, nat, dc.inclusion.map (K ∘ ("inc:" ++ ·)), dc.concernes.toList.map E, E dc.ecrivant,
         dc.interprete.map E, mode, dc.reexamen⟩
      let m : Option ProfRegPR37.MaintienMilieu :=
        mt.map fun x => ⟨E x.porteur, E x.contrepartie, E x.registre, ⟨x.du, x.paye⟩, x.horizon, K ("crit:" ++ x.critere)⟩
      let R : ProfRegPR37.RegistreDuMilieu Nat := ⟨decl, RB, h, m⟩
      let t := d.date
      let dv := ProfRegPR37.declarationValide decl t
      let ms := match m with | some x => x.registre == decl.titulaire | none => false
      let bf := ProfRegPR37.bienForme R t
      let ca := ProfRegPR37.ecartEnversMilieu t RA decl.titulaire (some R)
      let cb := ProfRegPR35.ecart RB RA
      champs := champs ++ [("etat_rapprochement", Json.mkObj [("A_vers_B", colonne te ca),
                              ("B_vers_A", if bf then colonne te cb else Json.null)]),
                           ("ecriture_duale", Json.bool (decide (ca = [] ∧ bf = true ∧ cb = []))),
                           ("milieu", Json.mkObj [("declaration_valide", Json.bool dv), ("maintien_structure", Json.bool ms), ("bien_forme", Json.bool bf),
                              ("solde_maintien", match m with | some x => Json.num (x.solde : Nat) | none => Json.null)])]
      if !dv then effets := effets ++ [⟨"C-07", "E6", some "[REGISTRE DU MILIEU NON OPPOSABLE]"⟩]
      if !ms then effets := effets ++ [⟨"C-08", "E4", some "[MAINTIEN NON STRUCTURÉ]"⟩]
    else
      return ⟨.controleNonApplicable, [], Json.mkObj champs, some "registre du milieu : le titulaire n'est pas le teneur de B (phase 1)"⟩
  -- C-05 : garde des deux silences
  let silence := decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = [])
  if silence then effets := effets ++ [⟨"C-05", "E5", some "[AUCUNE LIGNE RÉCIPROQUE]"⟩]
  -- C-06 : concordance, information
  champs := champs ++ [("aucune_ligne_reciproque", Json.bool silence), ("concordante", Json.bool (decide (ProfRegPR35.Concordante RA RB)))]
  -- C-09 : triplet porteur (présence de champs ; sans prédicat ProfReg)
  if (d.A.ancrage.communalite.isSome && !d.A.ancrage.tripletComplet) ||
     (d.B.ancrage.communalite.isSome && !d.B.ancrage.tripletComplet) then
    effets := effets ++ [⟨"C-09", "E3", some "[TRIPLET PORTEUR INCOMPLET]"⟩]
  -- C-10 : instance de contrôle commune (CONV-16, PR-43)
  if d.A.ancrage.communalite.isSome || d.B.ancrage.communalite.isSome then
    let mode (s : String) : ProfRegPR37.ModeDeclaration :=
      if s == "arretee" then .arretee else if s == "ratifiee" then .ratifiee else .nonDeclare
    let ds : List ProfRegPR43.DesignationControle :=
      (d.designations.getD #[]).toList.map fun x => ⟨E x.registre, E x.inst, mode x.mode⟩
    let ic := (ds.map (·.instanceCtrl)).any (ProfRegPR43.instanceCommune ds RA.teneur RB.teneur)
    champs := champs ++ [("instance_commune", Json.bool ic)]
    if !ic then effets := effets ++ [⟨"C-10", "E4", some "[ÉCART SANS INSTANCE DE CONTRÔLE]"⟩]
  else
    champs := champs ++ [("instance_commune", Json.null)]
  -- C-11 : statut de l'écart (PR-40), information
  match d.B.communication with
  | none => champs := champs ++ [("statut_ecart", Json.null)]
  | some c =>
    let com : ProfRegPR40.Communication :=
      if c == "extraitCommunique" then .extraitCommunique else if c == "nonCommunique" then .nonCommunique else .refuse
    let q := ProfRegPR40.ecartQualifie com RA RB
    champs := champs ++ [("statut_ecart", Json.arr (q.map fun (l, s) =>
      Json.mkObj [("ligne", ligneJson te l), ("statut", Json.str (statutEcartTexte s))]).toArray)]
  return ⟨statutDe effets, effets, Json.mkObj champs, none⟩

/-! ## Contexte de version et reçu complet -/

structure Contexte where
  setEmpreinte : String
  ntarch : String
  arbreManifeste : String
  arbreProfReg : String
  schema : String
  rules : String
  toolchain : String

def decContexte (j : Json) : D Contexte := do
  let c := "contexte"
  pure ⟨← chaine j "set_empreinte" c, ← chaine j "ntarch_sha256" c, ← chaine j "profreg_arbre_manifeste" c,
        ← chaine j "profreg_arbre" c, ← chaine j "schema_sha256" c, ← chaine j "rules_sha256" c,
        ← chaine j "toolchain" c⟩

def contexteJson (c : Contexte) : Json :=
  Json.mkObj [("set_empreinte", Json.str c.setEmpreinte), ("ntarch_sha256", Json.str c.ntarch),
    ("profreg_arbre", Json.str c.arbreProfReg), ("schema_sha256", Json.str c.schema),
    ("rules_sha256", Json.str c.rules), ("toolchain", Json.str c.toolchain)]

def recuJson (id : String) (c : Contexte) (r : Recu) : Json :=
  Json.mkObj [("recu_version", Json.str "mrc-check/0.1"), ("dossier_id", Json.str id),
    ("statut", Json.str r.statut.texte), ("effets", Json.arr (r.effets.map effetJson).toArray),
    ("calculs", r.calculs), ("motif", match r.motif with | some m => Json.str m | none => Json.null),
    ("contexte", contexteJson c),
    ("portee", Json.str "Reçu de contrôle formel : il ne vaut ni validation humaine ni opposabilité.")]

/-- Point d'entrée pur : texte du dossier, contexte → reçu. -/
def recu (dossier : String) (c : Contexte) : Json :=
  match Json.parse dossier with
  | .error e => recuJson "?" c ⟨.donneeManquante, [], Json.null, some s!"JSON illisible : {e}"⟩
  | .ok j =>
    let id := (j.getObjValAs? String "dossier_id").toOption.getD "?"
    match decDossier j with
    | .error e => recuJson id c ⟨.donneeManquante, [], Json.null, some e⟩
    | .ok d =>
      if c.arbreManifeste != c.arbreProfReg then
        recuJson id c ⟨.ecartDeVersion, [], Json.null, some "l'arbre de ProfReg compilé diffère de celui du manifeste"⟩
      else if d.ntarch != c.ntarch || d.arbre != c.arbreProfReg then
        recuJson id c ⟨.ecartDeVersion, [], Json.null, some "la référence du dossier (NT-ARCH, ProfReg) diffère de l'état de référence"⟩
      else
        match controler d with
        | .ok r | .error r => recuJson id c r

end MrcCheck
