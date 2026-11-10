#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Pilote C, phase 1.4 — contrôle des vecteurs de test.

Ce script NE CALCULE AUCUNE RÈGLE DU MRC. Il fait trois choses :
  1. valide chaque `dossier.json` contre `schema/ecriture_duale.schema.json` ;
  2. vérifie que chaque `attendu.json` est cohérent avec la table des règles
     (`rules/pilote_C/*.yaml`) : un effet n'est attendu que si le calcul
     attendu correspondant est en défaut, et l'issue suit l'ordre des effets ;
  3. traduit chaque dossier en termes Lean (couture JSON → Lean) et écrit
     `tests/lean/PiloteC_Vecteurs.lean`, où chaque valeur attendue est une
     proposition fermée prouvée par `decide` contre les définitions de
     ProfReg. C'est Lean, non ce script, qui établit les valeurs attendues.

Exception déclarée : la règle C-09 (triplet porteur) n'a aucun prédicat Lean ;
sa présence de champs est vérifiée ici, et seulement ici.

Usage : python3 tools/check_vectors.py [--lean-out tests/lean/PiloteC_Vecteurs.lean]
"""
import argparse, glob, json, os, sys
import jsonschema, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDRE = {"E1": 0, "E2": 1, "E0": 1, "E3": 2, "E4": 2, "E5": 3, "E6": 3}
ISSUE = {0: "refuse", 1: "en_attente", 2: "mal_forme", 3: "conforme_marque", None: "conforme"}
TYP = {"C+": ".Cplus", "D+": ".Dplus", "C-": ".Cmoins", "D-": ".Dmoins"}

class Enc:
    """Encodage des identités par `Nat` (règle des deux portes de PR-31)."""
    def __init__(self): self.t = {}
    def __call__(self, s):
        if s not in self.t: self.t[s] = len(self.t)
        return self.t[s]

def lb(b): return "true" if b else "false"

def ligne(enc, l): return f"⟨{enc(l['contrepartie'])}, {TYP[l['typage']]}, {l['montant']['valeur']}⟩"

def registre(enc, r): return f"⟨{enc(r['teneur'])}, [{', '.join(ligne(enc, l) for l in r['lignes'])}]⟩"

def opt(x): return "none" if x is None else f"some {x}"

def lean_vecteur(name, d, a):
    """Propositions Lean pour un vecteur recevable dont `calculs` est complet."""
    enc = Enc(); codes = Enc()
    A, B = d["registres"]["A"], d["registres"]["B"]
    c = a["calculs"]; t = d["date_controle"]
    out = [f"namespace {name}", "", f"def RA : ProfRegPR35.Registre Nat := {registre(enc, A)}",
           f"def RB : ProfRegPR35.Registre Nat := {registre(enc, B)}"]
    def anc(r):
        an = r.get("ancrage", {})
        tr = opt(codes("tr:" + an["traduction_uri_ref"]) if "traduction_uri_ref" in an else None)
        co = opt(codes("co:" + json.dumps(an["inscription_communalite_uri_ref"], sort_keys=True)) if "inscription_communalite_uri_ref" in an else None)
        return f"⟨{tr}, {co}⟩"
    cA = f"⟨{enc(A['teneur'])}, {anc(A)}⟩"; cB = f"⟨{enc(B['teneur'])}, {anc(B)}⟩"
    ok_anc = c["ancrage"]["A"] and c["ancrage"]["B"] and c["teneurs_distincts"]
    out += ["", "-- C-01 ancrage par côté ; C-01 et C-02 ancrage de l'écriture duale (D7)",
            f"example : ProfRegPR31.ancree {anc(A)} = {lb(c['ancrage']['A'])} := by decide",
            f"example : ProfRegPR31.ancree {anc(B)} = {lb(c['ancrage']['B'])} := by decide",
            f"example : decide (RA.teneur ≠ RB.teneur) = {lb(c['teneurs_distincts'])} := by decide",
            f"example : ProfRegPR31.ancreeDuale {cA} {cB} = {lb(ok_anc)} := by decide"]
    if not ok_anc:
        return out + ["", f"end {name}", ""]
    byid = {l["id"]: l for r in (A, B) for l in r["lignes"]}
    colA = "[" + ", ".join(ligne(enc, byid[i]) for i in c["etat_rapprochement"]["A_vers_B"]) + "]"
    colBids = c["etat_rapprochement"]["B_vers_A"]
    m = B.get("registre_du_milieu")
    if m is None:
        colB = "[" + ", ".join(ligne(enc, byid[i]) for i in colBids) + "]"
        out += ["", "-- C-04 état de rapprochement et écriture duale",
                f"example : ProfRegPR35.etatRapprochement RA RB = ({colA}, {colB}) := by decide",
                f"example : decide (ProfRegPR35.EcritureDuale RA RB) = {lb(c['ecriture_duale'])} := by decide"]
    else:
        dc, mt = m["declaration"], m["maintien"]
        assert dc["titulaire"] == B["teneur"], "phase 1 : le teneur de B est le titulaire"
        nat = ".milieu" if dc["nature"] == "milieu" else ".collectifHumain"
        inc = opt(codes("inc:" + dc["inclusion"]) if dc["inclusion"] is not None else None)
        itp = opt(enc(dc["interprete"]) if dc["interprete"] is not None else None)
        conc = "[" + ", ".join(str(enc(x)) for x in dc["concernes"]) + "]"
        out += ["", f"def decl : ProfRegPR37.DeclarationConcernes := ⟨{enc(dc['titulaire'])}, {nat}, {inc}, {conc}, "
                f"{enc(dc['ecrivant'])}, {itp}, .{dc['mode']}, {opt(dc['reexamen'])}⟩"]
        if mt is None:
            out.append("def mt : Option ProfRegPR37.MaintienMilieu := none")
        else:
            out.append(f"def mt : Option ProfRegPR37.MaintienMilieu := some ⟨{enc(mt['porteur'])}, {enc(mt['contrepartie'])}, "
                       f"{enc(mt['registre'])}, ⟨{mt['situation']['du']}, {mt['situation']['paye']}⟩, {mt['horizon']}, {codes('crit:' + mt['critere'])}⟩")
        out += ["def RBm : ProfRegPR37.RegistreDuMilieu Nat := ⟨decl, RB, rfl, mt⟩",
                "", "-- C-07 déclaration des concernés ; C-08 maintien structuré",
                f"example : ProfRegPR37.declarationValide decl {t} = {lb(c['milieu']['declaration_valide'])} := by decide",
                f"example : (match mt with | some m => m.registre == decl.titulaire | none => false) = {lb(c['milieu']['maintien_structure'])} := by decide",
                f"example : ProfRegPR37.bienForme RBm {t} = {lb(c['milieu']['bien_forme'])} := by decide",
                f"example : mt.map ProfRegPR23.MaintienCONV11.solde = {opt(c['milieu']['solde_maintien'])} := by decide",
                "", "-- C-04 (via PR-37) : colonne A = écart envers le titulaire",
                f"example : ProfRegPR37.ecartEnversMilieu {t} RA {enc(dc['titulaire'])} (some RBm) = {colA} := by decide"]
        if colBids is not None:
            colB = "[" + ", ".join(ligne(enc, byid[i]) for i in colBids) + "]"
            out.append(f"example : ProfRegPR35.ecart RB RA = {colB} := by decide")
        out.append(f"example : decide (ProfRegPR37.ecartEnversMilieu {t} RA {enc(dc['titulaire'])} (some RBm) = [] ∧ "
                   f"ProfRegPR37.bienForme RBm {t} = true ∧ ProfRegPR35.ecart RB RA = []) = {lb(c['ecriture_duale'])} := by decide")
    out += ["", "-- C-05 garde des deux silences",
            f"example : decide (ProfRegPR35.lignesVers RA RB = [] ∧ ProfRegPR35.lignesVers RB RA = []) = "
            f"{lb(not A['lignes'] and not B['lignes'])} := by decide",
            "", "-- C-06 concordance (information)",
            f"example : decide (ProfRegPR35.Concordante RA RB) = {lb(c['concordante'])} := by decide"]
    if c.get("instance_commune") is not None:
        ds = d.get("designations_controle", [])
        dsl = "[" + ", ".join(f"⟨{enc(x['registre'])}, {enc(x['instance'])}, .{x['mode']}⟩" for x in ds) + "]"
        out += ["", "-- C-10 instance de contrôle commune (CONV-16)",
                f"def ds : List ProfRegPR43.DesignationControle := {dsl}",
                f"example : (ds.map (·.instanceCtrl)).any (ProfRegPR43.instanceCommune ds RA.teneur RB.teneur) = "
                f"{lb(c['instance_commune'])} := by decide"]
    if c.get("statut_ecart"):
        com = B["communication"]
        st = "[" + ", ".join("." + c["statut_ecart"][i] for i in c["etat_rapprochement"]["A_vers_B"]) + "]"
        out += ["", "-- C-11 statut de l'écart (PR-40)",
                f"example : (ProfRegPR40.ecartQualifie .{com} RA RB).map (·.2) = {st} := by decide"]
    return out + ["", f"end {name}", ""]

def coherence(path, d, a, regles):
    """L'effet attendu suit la table de règles ; l'issue suit l'ordre des effets."""
    err = []
    eff = {e["regle"]: e for e in a["effets"]}
    for r, e in eff.items():
        code = regles[r].get("defect_effect", {}).get("code")
        if code != e["code"]:
            err.append(f"{r} : effet attendu {e['code']}, table {code}")
        mk = regles[r].get("defect_effect", {}).get("marqueur")
        if mk and e.get("marqueur") != mk:
            err.append(f"{r} : marqueur attendu {e.get('marqueur')}, table {mk}")
    c = a["calculs"]
    if a["schema_valide"] and c and "ancrage" in c:
        A, B = d["registres"]["A"], d["registres"]["B"]
        exp = {}
        if not (c["ancrage"]["A"] and c["ancrage"]["B"]): exp["C-01"] = True
        else:
            if not c["teneurs_distincts"]: exp["C-02"] = True
            if not A["lignes"] and not B["lignes"]: exp["C-05"] = True
            if "milieu" in c:
                if not c["milieu"]["declaration_valide"]: exp["C-07"] = True
                if not c["milieu"]["maintien_structure"]: exp["C-08"] = True
            for r in (A, B):
                ic = r["ancrage"].get("inscription_communalite_uri_ref")
                if ic is not None:
                    tp = ic.get("triplet_porteur", {})
                    if not all(tp.get(k) for k in ("entite", "personne", "role")): exp["C-09"] = True
            com = any("inscription_communalite_uri_ref" in r["ancrage"] for r in (A, B))
            if com and not c.get("instance_commune"): exp["C-10"] = True
        if set(exp) != set(eff):
            err.append(f"effets attendus {sorted(eff)} ; la table et les calculs donnent {sorted(exp)}")
    rang = min((ORDRE[e["code"]] for e in a["effets"]), default=None)
    if ISSUE[rang] != a["issue"]:
        err.append(f"issue {a['issue']} ; l'ordre des effets donne {ISSUE[rang]}")
    return err

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lean-out", default=os.path.join(ROOT, "tests/lean/PiloteC_Vecteurs.lean"))
    args = ap.parse_args()
    schema = json.load(open(os.path.join(ROOT, "schema/ecriture_duale.schema.json"), encoding="utf-8"))
    val = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    regles = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "rules/pilote_C/C-*.yaml"))):
        r = yaml.safe_load(open(f, encoding="utf-8")); regles[r["id"]] = r
    lean = ["-- SPDX-License-Identifier: AGPL-3.0-only",
            "-- GÉNÉRÉ par tools/check_vectors.py — NE PAS ÉDITER À LA MAIN.",
            "-- Chaque `example` fixe une valeur attendue d'un vecteur de tests/ ; `decide` l'établit",
            "-- contre les définitions de ProfReg (arbre de référence : corpus/_MANIFESTE_v5.7.md). Identités encodées en `Nat`.", "",
            "import ProfReg.PR31_BonneFormationDeclarative", "import ProfReg.PR35_EcritureDuale",
            "import ProfReg.PR37_RegistreDuMilieu", "import ProfReg.PR40_StatutDeLEcart",
            "import ProfReg.PR43_InstanceDeControle", ""]
    ok = True
    for att in sorted(glob.glob(os.path.join(ROOT, "tests/*/*/attendu.json"))):
        rep = os.path.dirname(att); rel = os.path.relpath(rep, os.path.join(ROOT, "tests"))
        d = json.load(open(os.path.join(rep, "dossier.json"), encoding="utf-8"))
        a = json.load(open(att, encoding="utf-8"))
        errs = [e.message for e in val.iter_errors(d)]
        if bool(errs) == a["schema_valide"]:
            print(f"ÉCHEC {rel} : schéma {'invalide' if errs else 'valide'}, attendu {'valide' if a['schema_valide'] else 'invalide'} {errs[:2]}"); ok = False; continue
        if a.get("cycle"):
            print(f"ok    {rel} → schéma {'valide' if a['schema_valide'] else 'invalide'} (cycle de vie)"); continue
        ce = coherence(rel, d, a, regles)
        if ce:
            print(f"ÉCHEC {rel} : " + " ; ".join(ce)); ok = False; continue
        if a["schema_valide"] and a["calculs"] and "ancrage" in a["calculs"]:
            lean += lean_vecteur("V_" + rel.replace("/", "_"), d, a)
        print(f"ok    {rel} → {a['issue']}")
    os.makedirs(os.path.dirname(args.lean_out), exist_ok=True)
    open(args.lean_out, "w", encoding="utf-8").write("\n".join(lean))
    print(f"Lean : {os.path.relpath(args.lean_out, ROOT)}")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
