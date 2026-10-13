#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Pilote C, phase 1.3 — garde-fous de lecture du noyau, appliqués à la table de règles.

Vérifie `rules/pilote_C/*.yaml` :
  G1  champs requis présents ; `status` dans la liste fermée ; `nt_arch_ref.sha256` = empreinte
      de NT-ARCH au manifeste (`corpus/_MANIFESTE_v5.7.md`).
  G2  une règle `status: theorem` de nature A s'appuie sur au moins un théorème de nature A :
      un théorème de nature G ou L n'est jamais l'appui seul (NT-ARCH §8ter-bis, R-3, R-5).
  G3  une règle dont tous les appuis Lean sont de nature G ou L ne produit ni refus (E1) ni
      mauvaise formation (E3, E4).
  G4  une règle de nature T ne produit aucun effet sur le dossier (elle ne qualifie que la table).
  G5  une convention ou un axiome ne s'affiche jamais « démontré(e) ».
  G6  une règle hors noyau ne produit pas de refus (E1).
  G7  `noyau: true` ⇔ le théorème figure dans `rules/theoremes.yaml` (forme machine du noyau).
  G8  une règle `perimetre: noyau` et `status: theorem` cite au moins un théorème du noyau.
  G9  chaque théorème cité existe dans le module ProfReg nommé (si --profreg est donné).
  G10 chaque témoin cité existe dans `tests/`.
  G11 (si --profreg) chaque théorème cité par `rules/pilote_C` ou par `rules/theoremes.yaml` est audité
      par une ligne `#print axioms` de `Audit.lean` : un théorème retiré de l'audit est détecté.
Usage : python3 tools/check_rules.py [--profreg CHEMIN_PROFREG]
"""
import argparse, glob, os, re, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATUS = {"theorem", "convention", "axiom", "RSO", "procedure", "definition"}
PERIM = {"noyau", "nt_arch_hors_noyau", "hors_noyau"}
REQ = ["id", "titre", "status", "perimetre", "application", "enonce", "nt_arch_ref", "owner",
       "horizon", "critere_verification", "affichage", "temoins"]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--profreg"); a = ap.parse_args()
    man = open(os.path.join(ROOT, "corpus/_MANIFESTE_v5.7.md"), encoding="utf-8").read()
    ntsha = re.search(r"([0-9a-f]{64})  MRC_v5\.7_NT-ARCH_Architecture_Couches0-3\.md", man).group(1)
    noyau = set(re.findall(r'^  - id: "([^"]+)"', open(os.path.join(ROOT, "rules/theoremes.yaml"), encoding="utf-8").read(), re.M))
    err = []
    files = sorted(glob.glob(os.path.join(ROOT, "rules/pilote_C/C-*.yaml")))
    for f in files:
        r = yaml.safe_load(open(f, encoding="utf-8")); i = r.get("id", os.path.basename(f))
        e = lambda g, m: err.append(f"{i} {g} : {m}")
        for k in REQ:
            if k not in r: e("G1", f"champ `{k}` absent")
        if r.get("status") not in STATUS: e("G1", f"status {r.get('status')}")
        if r.get("perimetre") not in PERIM: e("G1", f"perimetre {r.get('perimetre')}")
        if r.get("nt_arch_ref", {}).get("sha256") != ntsha: e("G1", "empreinte NT-ARCH ≠ manifeste")
        refs = r.get("lean_ref", []); code = (r.get("defect_effect") or {}).get("code")
        natures = {x.get("nature") for x in refs}
        if r.get("status") == "theorem" and r.get("nature") == "A" and "A" not in natures:
            e("G2", "aucun appui de nature A")
        if refs and natures <= {"G", "L"} and code in {"E1", "E3", "E4"}:
            e("G3", f"appuis G/L seulement, effet {code}")
        if r.get("nature") == "T" and code: e("G4", f"règle T avec effet {code}")
        if r.get("status") in {"convention", "axiom"}:
            for m in re.finditer(r"démontr\w*", r.get("affichage", "")):
                if "jamais" not in r["affichage"][max(0, m.start() - 12):m.start()]:
                    e("G5", "affichage « démontré »")
        if r.get("perimetre") != "noyau" and code == "E1": e("G6", "refus hors noyau")
        for x in refs:
            if bool(x.get("noyau")) != (x["nom"] in noyau):
                e("G7", f"{x['nom']} : noyau={x.get('noyau')}, forme machine={'oui' if x['nom'] in noyau else 'non'}")
            if a.profreg:
                src = os.path.join(a.profreg, "ProfReg", x["module"] + ".lean")
                if not os.path.exists(src) or not re.search(rf"^theorem {re.escape(x['nom'])}\b", open(src, encoding="utf-8").read(), re.M):
                    e("G9", f"{x['module']}.{x['nom']} introuvable")
        if r.get("perimetre") == "noyau" and r.get("status") == "theorem" and not any(x.get("noyau") for x in refs):
            e("G8", "règle du noyau sans théorème du noyau")
        for t in r.get("temoins", {}).get("ok", []) + r.get("temoins", {}).get("ko", []):
            if not os.path.exists(os.path.join(ROOT, "tests", t, "dossier.json")): e("G10", f"témoin {t} absent")
    if a.profreg:
        audit = open(os.path.join(a.profreg, "Audit.lean"), encoding="utf-8").read()
        audites = {x.split(".")[-1] for x in re.findall(r"^#print axioms (\S+)", audit, re.M)}
        cites = {x["nom"] for f in files for x in (yaml.safe_load(open(f, encoding="utf-8")).get("lean_ref") or [])} | noyau
        for nom in sorted(cites - audites):
            err.append(f"G11 : {nom} cité mais absent de Audit.lean (retiré ou non audité)")
    for m in err: print("ÉCHEC", m)
    print(f"{len(files)} règles ; {len(err)} écart(s)")
    sys.exit(1 if err else 0)

if __name__ == "__main__":
    main()
