#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Constitue (ou met à jour) la copie de travail du dépôt PRIVÉ du banc d'essai (décision D6 : accès restreint).

Le dépôt public ne publie que des empreintes. Le dépôt privé contient ce qu'un vérificateur désigné doit pouvoir
lire pour refaire les contrôles :
  · pieces/<chemin>        — les pièces d'origine citées par `banc/corpus.yaml` (empreinte vérifiée à la copie) ;
  · banc_pilote_C/         — sources de cas, consignes, déclarations, propositions, journaux, réponses brutes,
                             registre (décisions signées), suivi complet ;
  · MANIFESTE.sha256       — empreinte de chaque fichier copié (format `sha256sum`) ;
  · README.md              — créé s'il manque ; ACCES.md n'est jamais écrit par ce script (registre des accès,
                             tenu à la main par le porteur).
Rien n'est poussé : le porteur relit, committe et pousse lui-même.
Usage : tools/constituer_prive.py --mrc ~/Documents/Claude/Projects/MRC --sortie ~/Developer/mrc-banc-prive
"""
import argparse, hashlib, os, shutil, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORER = {".DS_Store", ".gitkeep"}

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()

README = """# mrc-banc-prive — pièces du banc d'essai du pilote C (accès restreint)

Dépôt **privé** (décision D6 du registre pilote, `mrc-script/governance/registre_pilote.md`). Il contient les pièces
d'origine et les produits du banc que le dépôt public `mrc-script` ne cite que par empreinte.

- Accès en lecture seule, accordé par le porteur du registre pilote à des vérificateurs désignés ; registre des accès : `ACCES.md`.
- Ne rien recopier hors de ce dépôt : les pièces internes restent soumises à l'accord de l'organisation qui les a émises.
- Vérifier : depuis `mrc-script`, `tools/verifier_prive.py --prive <ce dépôt>` (empreintes contre `banc/corpus.yaml`,
  manifeste, signatures des décisions).
- Mise à jour : `tools/constituer_prive.py` depuis `mrc-script`, puis commit par le porteur. L'historique est conservé.
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mrc", required=True); ap.add_argument("--sortie", required=True)
    a = ap.parse_args()
    mrc, out = os.path.expanduser(a.mrc), os.path.expanduser(a.sortie)
    corpus = yaml.safe_load(open(os.path.join(ROOT, "banc", "corpus.yaml"), encoding="utf-8"))["cas"]
    os.makedirs(out, exist_ok=True)
    copies, erreurs = {}, []
    for c in corpus:
        if c.get("espace") != "local": continue
        for p in c.get("pieces", []):
            src = os.path.join(mrc, p["chemin"])
            if not os.path.exists(src): erreurs.append(f"{c['id']} : pièce absente {p['chemin']}"); continue
            if sha(src) != p["sha256"]: erreurs.append(f"{c['id']} : pièce modifiée {p['chemin']}"); continue
            copies[os.path.join("pieces", p["chemin"])] = src
    banc = os.path.join(mrc, "banc_pilote_C")
    for d, _, fs in os.walk(banc):
        for f in fs:
            if f in IGNORER: continue
            src = os.path.join(d, f)
            copies[os.path.join("banc_pilote_C", os.path.relpath(src, banc))] = src
    if erreurs: sys.exit("rien n'est copié :\n  " + "\n  ".join(erreurs))
    for rel, src in sorted(copies.items()):
        dst = os.path.join(out, rel); os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(src, dst)
    open(os.path.join(out, "MANIFESTE.sha256"), "w", encoding="utf-8").write(
        "".join(f"{sha(os.path.join(out, r))}  {r}\n" for r in sorted(copies)))
    if not os.path.exists(os.path.join(out, "README.md")):
        open(os.path.join(out, "README.md"), "w", encoding="utf-8").write(README)
    print(f"{len(copies)} fichiers copiés dans {out} ; manifeste écrit. Relire, puis : cd {out} && git add -A && git commit")

if __name__ == "__main__":
    main()
