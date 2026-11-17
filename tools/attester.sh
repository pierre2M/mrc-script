#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
# Phase 4.2 — trousse du VÉRIFICATEUR TIERS (personne distincte du porteur et du rédacteur).
# À lancer dans un clone FRAIS des dépôts publiés : github.com/pierre2M/mrc-script et github.com/pierre2M/ProfReg
# (lien ou copie dans mrc-script/profreg). Rejoue le build et l'audit, puis tous les contrôles de la CI, et
# rédige une attestation à signer par le vérificateur avec SA clé (espace de noms `mrc-attestation`).
# Rien n'est envoyé ni modifié dans les dépôts : seule l'attestation est écrite (dans --sortie).
#   tools/attester.sh --verificateur "Prénom Nom" [--prive ~/mrc-banc-prive] [--sortie DIR] [--sans-audit]
# --sans-audit : essai à blanc sans le build Mathlib de ProfReg ; l'attestation est alors marquée PARTIELLE
# et refusée par tools/check_attestations.py.
# Prérequis : elan (toolchain de lean-toolchain), python3 avec jsonschema et pyyaml, ssh-keygen, git.
set -uo pipefail
RACINE=$(cd "$(dirname "$0")/.." && pwd); cd "$RACINE"
SANS_AUDIT=0; VERIF=""; PRIVE=""; SORTIE="$RACINE/governance/attestations"
while [ $# -gt 0 ]; do case $1 in
  --verificateur) VERIF=$2; shift 2;; --prive) PRIVE=$2; shift 2;; --sortie) SORTIE=$2; shift 2;; --sans-audit) SANS_AUDIT=1; shift;;
  *) echo "option inconnue : $1" >&2; exit 2;; esac; done
[ -n "$VERIF" ] || { echo "--verificateur requis" >&2; exit 2; }
DATE=$(date +%F); J=$(mktemp -d); RES=(); OK=1
etape() { local nom=$1; shift; echo "== $nom"; if "$@" >"$J/$(echo "$nom" | tr ' /' '__').log" 2>&1; then RES+=("| $nom | réussi |"); else RES+=("| $nom | **ÉCHEC** (journal joint) |"); OK=0; fi; }
H() { if command -v sha256sum >/dev/null; then sha256sum "$@"; else shasum -a 256 "$@"; fi; }
MAN=corpus/_MANIFESTE_v5.7.md
ARBRE_MRC=$(git rev-parse 'HEAD^{tree}'); ARBRE_PR=$(git -C profreg rev-parse 'HEAD^{tree}')
ARBRE_MAN=$(grep -o 'Arbre git (local = publié) | `[0-9a-f]*`' "$MAN" | grep -o '[0-9a-f]\{40\}')
SET=$(grep -o 'Empreinte globale du set (sha256 de la liste ci-dessus) : `[0-9a-f]*`' "$MAN" | grep -o '[0-9a-f]\{64\}')
etape "ProfReg compilé = manifeste" test "$ARBRE_PR" = "$ARBRE_MAN"
etape "Arbres propres" sh -c '[ -z "$(git status --porcelain)" ] && [ -z "$(git -C profreg status --porcelain)" ]'
if [ $SANS_AUDIT -eq 0 ]; then
etape "ProfReg : cache Mathlib" sh -c 'cd profreg && lake exe cache get'
etape "ProfReg : build" sh -c 'cd profreg && lake build'
etape "ProfReg : audit" sh -c 'cd profreg && lake env lean Audit.lean > "$0/audit.log" 2>&1; tools_dir="$1"; "$tools_dir/verifier_audit.sh" "$0/audit.log"' "$J" "$RACINE/tools"
etape "ProfReg : R-7" sh -c 'cd profreg && lake env lean R7_Controle.lean'
else RES+=("| ProfReg : build, audit, R-7 | **non rejoués** (--sans-audit) |"); OK=0; fi
etape "mrc-check : build" lake build
etape "Règles" python3 tools/check_rules.py --profreg profreg
etape "Vecteurs" sh -c 'python3 tools/check_vectors.py && git diff --exit-code tests/lean/PiloteC_Vecteurs.lean'
etape "Vecteurs prouvés en Lean" sh -c 'lake env lean tests/lean/PiloteC_Vecteurs.lean && lake env lean tests/lean/D7_Verification_PR31.lean'
etape "Reçus et rejeu" python3 tools/test_recus.py
etape "Chaîne agent / validation / registre" sh -c 'python3 tests/agent/test_chaine.py && python3 tools/check_registre.py'
[ -n "$PRIVE" ] && etape "Dépôt privé du banc (D6)" python3 tools/verifier_prive.py --prive "$PRIVE"
AUDIT=$(grep -h "^audit :" "$J"/ProfReg_:_audit.log 2>/dev/null | head -1)
mkdir -p "$SORTIE"; A="$SORTIE/attestation_${DATE}_$(echo "$VERIF" | tr -cs 'A-Za-z0-9' '-' | sed 's/-$//').md"
{
echo "# Attestation de vérification — phase 4.2"; echo
echo "Je soussigné·e, **$VERIF**, déclare n'être ni le porteur du registre pilote ni le rédacteur des dépôts vérifiés,"
echo "et avoir rejoué le $DATE, sur ma machine, les contrôles ci-dessous à partir des dépôts publiés."; echo
echo "| Objet | Valeur |"; echo "| --- | --- |"
echo "| Arbre de mrc-script vérifié | \`$ARBRE_MRC\` |"; echo "| Arbre de ProfReg vérifié | \`$ARBRE_PR\` |"
echo "| Arbre de ProfReg au manifeste | \`$ARBRE_MAN\` |"; echo "| Empreinte du set v5.7 | \`$SET\` |"
echo "| Toolchain | \`$(tr -d '\n' < lean-toolchain)\` |"; echo "| Machine | \`$(uname -srm)\` |"
echo "| Audit ProfReg | $AUDIT |"; echo
echo "| Contrôle | Résultat |"; echo "| --- | --- |"; printf '%s\n' "${RES[@]}"; echo
if [ $OK -eq 1 ]; then echo "**Conclusion : tous les contrôles sont réussis.**"; elif [ $SANS_AUDIT -eq 1 ]; then echo "**Conclusion : attestation PARTIELLE (audit de ProfReg non rejoué) ; elle ne vaut pas attestation de phase 4.2.**"; else echo "**Conclusion : au moins un contrôle a échoué ; voir les journaux.**"; fi
echo; echo "Cette attestation porte sur la reproductibilité technique. Elle ne valide aucune écriture, ne rend rien opposable et ne canonise rien."
} > "$A"
tar -czf "${A%.md}.journaux.tar.gz" -C "$J" .
echo; echo "Attestation : $A"; echo "Signer avec VOTRE clé :  ssh-keygen -Y sign -f ~/.ssh/<votre_cle> -n mrc-attestation \"$A\""
echo "Puis transmettre au porteur l'attestation, sa signature (.sig), les journaux et votre clé publique."
[ $OK -eq 1 ]
