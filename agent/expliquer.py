#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Agent d'explicitation (validation explicite).

La personne qui valide pose une question sur un dossier proposé ; l'agent répond à partir du dossier,
de sa fiche de lecture (`tools/fiche.py`), du reçu de `mrc-check`, des règles du pilote et des pièces
sources fournies. Il explique ; il ne recommande aucune décision et ne modifie rien.

Chaque échange est ajouté au **journal** du dossier (une ligne JSON par question) : question, réponse,
fournisseur, modèle, sha256 du gabarit, du contexte et de la réponse, appréciation de la personne
(à poser ensuite). Le sha256 du journal est inscrit dans la décision (`tools/valider.py --journal`).
L'agent n'écrit que dans ce journal ; il n'a aucun accès au registre.

Usage :
  agent/expliquer.py --proposition P.json --question "…" [--source S.md …] --fournisseur anthropic --modele <id>
  agent/expliquer.py --proposition P.json --question "…" --fournisseur rejeu --reponse R.txt
  agent/expliquer.py --proposition P.json --apprecier 1 utile|insuffisante|erronee [--note "…"]
  agent/expliquer.py --proposition P.json --lire          (affiche le journal)
Journal par défaut : <P sans .json>.journal.jsonl
"""
import argparse, datetime, glob, hashlib, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRE = os.path.realpath(os.path.join(ROOT, "registre"))
sys.path.insert(0, os.path.join(ROOT, "agent"))
from proposer import appeler_anthropic, regles  # même appel API, même résumé des règles

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proposition", required=True)
    ap.add_argument("--journal")
    ap.add_argument("--question")
    ap.add_argument("--source", action="append", default=[])
    ap.add_argument("--fournisseur", choices=["anthropic", "rejeu"])
    ap.add_argument("--modele")
    ap.add_argument("--reponse", help="rejeu : réponse enregistrée")
    ap.add_argument("--apprecier", nargs=2, metavar=("N", "VALEUR"))
    ap.add_argument("--note", default="")
    ap.add_argument("--lire", action="store_true")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    if not a.proposition or not os.path.isfile(a.proposition):
        sys.exit(f"proposition introuvable : « {a.proposition} » (chemin vide ? définir P=… avant la commande)")
    journal = a.journal or os.path.splitext(a.proposition)[0] + ".journal.jsonl"
    jr = os.path.realpath(journal)
    if jr == REGISTRE or jr.startswith(REGISTRE + os.sep):
        sys.exit("refusé : l'agent d'explicitation n'écrit pas dans registre/")
    entrees = [json.loads(l) for l in open(journal, encoding="utf-8")] if os.path.exists(journal) else []

    if a.lire:
        for e in entrees:
            print(f"--- n° {e['n']} ({e['date']}, {e['fournisseur']} / {e['modele']}) — appréciation : {e.get('appreciation') or 'à poser'}")
            print(f"Q : {e['question']}\nR : {e['reponse']}\n")
        return
    if a.apprecier:
        n, v = int(a.apprecier[0]), a.apprecier[1]
        if v not in ("utile", "insuffisante", "erronee"): sys.exit("appréciation : utile, insuffisante ou erronee")
        for e in entrees:
            if e["n"] == n: e["appreciation"], e["note"] = v, a.note
        open(journal, "w", encoding="utf-8").write("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in entrees))
        print(f"n° {n} : {v}"); return
    if not a.question or not a.fournisseur: sys.exit("--question et --fournisseur requis")

    dossier = open(a.proposition, encoding="utf-8").read()
    recu = subprocess.run([os.path.join(ROOT, "tools", "mrc-check.sh"), a.proposition], capture_output=True, check=True).stdout.decode()
    fiche = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "fiche.py"), a.proposition], capture_output=True, check=True).stdout.decode()
    sources = "\n\n".join(f"=== {os.path.basename(s)} ===\n" + open(s, encoding="utf-8").read() for s in a.source) or "(aucune pièce source fournie)"
    gab_p = os.path.join(ROOT, "agent", "gabarit_explicitation.md")
    contexte = dossier + fiche + recu + sources
    prompt = (open(gab_p, encoding="utf-8").read().replace("{{DOSSIER}}", dossier).replace("{{FICHE}}", fiche)
              .replace("{{RECU}}", recu).replace("{{REGLES}}", regles()).replace("{{SOURCES}}", sources)
              .replace("{{QUESTION}}", a.question))
    if a.fournisseur == "rejeu":
        if not a.reponse: sys.exit("--reponse requise pour le rejeu")
        texte, modele = open(a.reponse, encoding="utf-8").read().strip(), a.modele or "rejeu"
    else:
        if not a.modele: sys.exit("--modele requis (aucune valeur par défaut)")
        texte, modele = appeler_anthropic(a.modele, prompt).strip(), a.modele
    e = {"n": len(entrees) + 1, "date": a.date, "question": a.question, "reponse": texte,
         "fournisseur": a.fournisseur, "modele": modele, "gabarit_sha256": sha(open(gab_p, "rb").read()),
         "contexte_sha256": sha(contexte.encode()), "reponse_sha256": sha(texte.encode()),
         "appreciation": None, "note": ""}
    with open(journal, "a", encoding="utf-8") as f: f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(f"n° {e['n']}\n{texte}\n\n(journal : {journal} ; appréciez la réponse : --apprecier {e['n']} utile|insuffisante|erronee)")

if __name__ == "__main__":
    main()
