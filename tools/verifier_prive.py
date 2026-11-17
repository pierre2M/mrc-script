#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Vérification par un tiers ayant accès au dépôt privé du banc (décision D6 : accès restreint).

Contrôle, sans rien modifier :
  1. que chaque pièce, source de cas et consigne citée par `banc/corpus.yaml` (dépôt public) est présente dans le
     dépôt privé avec la même empreinte ;
  2. que chaque fichier du dépôt privé correspond à son `MANIFESTE.sha256` ;
  3. que les décisions de `banc_pilote_C/registre/` passent `tools/check_registre.py` (signatures, examen explicite).
Usage : tools/verifier_prive.py --prive ~/Developer/mrc-banc-prive
"""
import argparse, hashlib, os, subprocess, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--prive", required=True); a = ap.parse_args()
    pv = os.path.expanduser(a.prive); ecarts = []
    corpus = yaml.safe_load(open(os.path.join(ROOT, "banc", "corpus.yaml"), encoding="utf-8"))["cas"]
    for c in corpus:
        if c.get("espace") != "local": continue
        refs = [(os.path.join("pieces", p["chemin"]), p["sha256"]) for p in c.get("pieces", [])]
        for k in ("source_cas", "consigne"):
            if c.get(k): refs.append((c[k]["chemin"], c[k]["sha256"]))
        for rel, h in refs:
            f = os.path.join(pv, rel)
            if not os.path.exists(f): ecarts.append(f"{c['id']} : absent du dépôt privé : {rel}")
            elif sha(f) != h: ecarts.append(f"{c['id']} : empreinte différente : {rel}")
    man = os.path.join(pv, "MANIFESTE.sha256")
    if not os.path.exists(man): ecarts.append("MANIFESTE.sha256 absent")
    else:
        for l in open(man, encoding="utf-8"):
            h, rel = l.rstrip("\n").split("  ", 1)
            f = os.path.join(pv, rel)
            if not os.path.exists(f) or sha(f) != h: ecarts.append(f"manifeste : {rel}")
    reg = os.path.join(pv, "banc_pilote_C", "registre")
    if os.path.isdir(reg):
        r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "check_registre.py"), "--registre", reg,
                            "--propositions", os.path.join(pv, "banc_pilote_C", "propositions")], capture_output=True, text=True)
        print(r.stdout.strip())
        if r.returncode != 0: ecarts.append("check_registre : écart(s) ci-dessus")
    print("\n".join(ecarts) if ecarts else "dépôt privé conforme au corpus public, au manifeste et au registre")
    sys.exit(1 if ecarts else 0)

if __name__ == "__main__":
    main()
