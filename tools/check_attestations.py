#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Phase 4.2 — contrôle des attestations de vérificateurs tiers (`governance/attestations/`).

Pour chaque `attestation_*.md` :
  A1. une signature `.sig` existe et vérifie (espace de noms `mrc-attestation`) pour un principal déclaré dans
      `governance/signataires_autorises` avec cet espace de noms ;
  A2. la clé du vérificateur n'est ni celle de l'agent ni celle du validateur (personne distincte du porteur) ;
  A3. l'arbre de ProfReg attesté est celui du manifeste ; la conclusion est « tous les contrôles sont réussis ».
Affiche aussi l'arbre de mrc-script attesté (à rapprocher de l'état publié). Sortie non nulle en cas d'écart.
Usage : tools/check_attestations.py
"""
import glob, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIG = os.path.join(ROOT, "governance", "signataires_autorises")
MAN = open(os.path.join(ROOT, "corpus", "_MANIFESTE_v5.7.md"), encoding="utf-8").read()
ARBRE_MAN = re.search(r"Arbre git \(local = publié\) \| `([0-9a-f]{40})`", MAN).group(1)

def main():
    lignes = [l.split() for l in open(SIG, encoding="utf-8") if l.strip() and not l.startswith("#")]
    cles = {l[0]: (l[1], " ".join(l[2:4])) for l in lignes}
    interdites = {v[1] for k, v in cles.items() if "mrc-proposition" in v[0] or "mrc-validation" in v[0]}
    verifs = {k: v for k, v in cles.items() if "mrc-attestation" in v[0]}
    ecarts, n = [], 0
    for a in sorted(glob.glob(os.path.join(ROOT, "governance", "attestations", "attestation_*.md"))):
        n += 1; nom = os.path.basename(a); txt = open(a, encoding="utf-8").read()
        signe = None
        if os.path.exists(a + ".sig"):
            for p in verifs:
                with open(a, "rb") as f:
                    if subprocess.run(["ssh-keygen", "-Y", "verify", "-f", SIG, "-I", p, "-n", "mrc-attestation", "-s", a + ".sig"],
                                      stdin=f, capture_output=True).returncode == 0: signe = p; break
        if not signe: ecarts.append(f"A1 {nom} : signature absente ou d'un principal non déclaré (mrc-attestation)"); continue
        if verifs[signe][1] in interdites: ecarts.append(f"A2 {nom} : la clé de {signe} est celle de l'agent ou du validateur")
        m = re.search(r"Arbre de ProfReg vérifié \| `([0-9a-f]{40})`", txt)
        if not m or m.group(1) != ARBRE_MAN: ecarts.append(f"A3 {nom} : arbre de ProfReg attesté ≠ manifeste")
        if "tous les contrôles sont réussis" not in txt: ecarts.append(f"A3 {nom} : conclusion non réussie")
        mm = re.search(r"Arbre de mrc-script vérifié \| `([0-9a-f]{40})`", txt)
        print(f"{nom} : signée par {signe} ; mrc-script {mm.group(1) if mm else '?'}")
    print(f"attestations : {n} ; {len(ecarts)} écart(s)"); print("\n".join(ecarts))
    sys.exit(1 if ecarts else 0)

if __name__ == "__main__":
    main()
