#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Phase 2c — tests du validateur `mrc-check` contre les vecteurs de la phase 1.4.

Pour chaque vecteur `tests/{ok,ko}/*/` :
  1. rejeu : deux exécutions de `tools/mrc-check.sh` donnent le même reçu (même sha256) ;
  2. le statut du reçu correspond à l'issue attendue (`attendu.json`) ;
  3. les effets (règle, code, marqueur) sont ceux attendus ;
  4. les calculs (ancrage, teneurs, état de rapprochement, écriture duale, concordance,
     registre du milieu, instance commune, statut de l'écart) sont ceux attendus.
Puis trois cas de bord produits à la volée : DONNEE_MANQUANTE, CONTROLE_NON_APPLICABLE,
ECART_DE_VERSION. Enfin, aucun reçu ne porte « VALIDE » ni « OPPOSABLE ».
Ce script compare ; il ne calcule aucune règle.
"""
import glob, hashlib, json, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECK = os.path.join(ROOT, "tools", "mrc-check.sh")
STATUT = {"conforme": "FORMELLEMENT_BIEN_FORMEE", "conforme_marque": "FORMELLEMENT_BIEN_FORMEE",
          "mal_forme": "FORMELLEMENT_INCOMPLETE", "refuse": "CONTROLE_ECHOUE",
          "en_attente": "CONTROLE_NON_APPLICABLE"}
INTERDIT = re.compile(r'"(VALIDE|OPPOSABLE)"')

def run(path):
    return subprocess.run([CHECK, path], capture_output=True, check=True).stdout

def triple(l):
    return {"contrepartie": l["contrepartie"], "typage": l["typage"], "montant": l["montant"]["valeur"]}

def comparer(d, a, r):
    err = []
    exp = STATUT[a["issue"]]
    if r["statut"] != exp: err.append(f"statut {r['statut']} ≠ {exp}")
    got = sorted((e["regle"], e["code"], e.get("marqueur")) for e in r["effets"])
    want = sorted((e["regle"], e["code"], e.get("marqueur")) for e in a["effets"])
    if got != want: err.append(f"effets {got} ≠ {want}")
    c, k = a.get("calculs"), r.get("calculs") or {}
    if c and "ancrage" in c:
        if k.get("ancrage") != c["ancrage"]: err.append("ancrage")
        if k.get("teneurs_distincts") != c["teneurs_distincts"]: err.append("teneurs_distincts")
        if c["ancrage"]["A"] and c["ancrage"]["B"] and c["teneurs_distincts"]:
            byid = {l["id"]: l for g in ("A", "B") for l in d["registres"][g]["lignes"]}
            er = c["etat_rapprochement"]
            if k.get("ecriture_duale") != c["ecriture_duale"]: err.append("ecriture_duale")
            if k["etat_rapprochement"]["A_vers_B"] != [triple(byid[i]) for i in er["A_vers_B"]]: err.append("colonne A")
            wb = None if er["B_vers_A"] is None else [triple(byid[i]) for i in er["B_vers_A"]]
            if k["etat_rapprochement"]["B_vers_A"] != wb: err.append("colonne B")
            if k.get("concordante") != c["concordante"]: err.append("concordante")
            if k.get("instance_commune") != c.get("instance_commune"): err.append("instance_commune")
            if "milieu" in c and k.get("milieu") != c["milieu"]: err.append(f"milieu {k.get('milieu')}")
            if c.get("statut_ecart"):
                st = [x["statut"] for x in k.get("statut_ecart") or []]
                if st != [c["statut_ecart"][i] for i in er["A_vers_B"]]: err.append("statut_ecart")
    return err

def main():
    ok = True; n = 0; recus = []
    for att in sorted(glob.glob(os.path.join(ROOT, "tests/o[k]/*/attendu.json")) + sorted(glob.glob(os.path.join(ROOT, "tests/ko/*/attendu.json")))):
        rep = os.path.dirname(att); rel = os.path.relpath(rep, os.path.join(ROOT, "tests"))
        dp = os.path.join(rep, "dossier.json")
        r1, r2 = run(dp), run(dp)
        h = hashlib.sha256(r1).hexdigest()
        errs = [] if r1 == r2 else ["rejeu : deux reçus différents"]
        r = json.loads(r1); recus.append(r1)
        errs += comparer(json.load(open(dp, encoding="utf-8")), json.load(open(att, encoding="utf-8")), r)
        n += 1
        print(("ÉCHEC " if errs else "ok    ") + f"{rel:34s} {r['statut']:26s} {h[:16]}" + (" — " + " ; ".join(errs) if errs else ""))
        ok &= not errs
    base = json.load(open(os.path.join(ROOT, "tests/ok/01_pret_bancaire/dossier.json"), encoding="utf-8"))
    bords = {"DONNEE_MANQUANTE": lambda d: d.pop("registres"),
             "CONTROLE_NON_APPLICABLE": lambda d: d.update(schema_version="pilote-X/9"),
             "ECART_DE_VERSION": lambda d: d["reference"].update(ntarch_sha256="0" * 64)}
    with tempfile.TemporaryDirectory() as t:
        for attendu, mut in bords.items():
            d = json.loads(json.dumps(base)); mut(d)
            p = os.path.join(t, "d.json"); json.dump(d, open(p, "w"))
            r1 = run(p); r = json.loads(r1); recus.append(r1)
            good = r["statut"] == attendu and run(p) == r1
            print(("ok    " if good else "ÉCHEC ") + f"bord/{attendu:29s} {r['statut']:26s} motif : {r['motif']}")
            ok &= good
    if any(INTERDIT.search(x.decode("utf-8")) for x in recus):
        print("ÉCHEC un reçu porte VALIDE ou OPPOSABLE"); ok = False
    print(f"{n} vecteurs + 3 cas de bord ; {'tout passe' if ok else 'échecs'}")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
