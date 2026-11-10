#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Renseigne la `reference` d'un dossier (empreinte de NT-ARCH, arbre de ProfReg) depuis le manifeste.

Ces valeurs sont techniques : aucune personne n'a à les connaître ni à les recopier. Le proposant
humain lance ce script sur son dossier ; l'agent de proposition fait de même automatiquement.
Usage : tools/reference.py <dossier.json>      (modifie le fichier en place)
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
man = open(os.path.join(ROOT, "corpus", "_MANIFESTE_v5.7.md"), encoding="utf-8").read()
ref = {"mrc_release": "v5.7",
       "ntarch_sha256": re.search(r"([0-9a-f]{64})  MRC_v5\.7_NT-ARCH_Architecture_Couches0-3\.md", man).group(1),
       "profreg_arbre": re.search(r"Arbre git \(local = publié\) \| `([0-9a-f]{40})`", man).group(1)}
p = sys.argv[1]; d = json.load(open(p, encoding="utf-8")); d["reference"] = ref
open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(ref, ensure_ascii=False))
