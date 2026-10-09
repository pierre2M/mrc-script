#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
# Contrôle formel d'un dossier du pilote C (phase 2).
#   tools/mrc-check.sh <dossier.json> [reçu.json]
# 2e : calcule les empreintes de l'état de référence et les inscrit dans le reçu :
# empreinte globale du set et de NT-ARCH (corpus/_MANIFESTE_v5.7.md), arbre git de ProfReg
# (attendu au manifeste, et réellement compilé dans profreg/), schéma, rules/, toolchain.
# Le reçu est écrit sur la sortie standard (ou dans le fichier donné) ; son sha256 sur stderr.
set -euo pipefail
RACINE=$(cd "$(dirname "$0")/.." && pwd)
DOSSIER=$1; SORTIE=${2:-}
H() { if command -v sha256sum >/dev/null; then sha256sum "$@"; else shasum -a 256 "$@"; fi; }
MAN="$RACINE/corpus/_MANIFESTE_v5.7.md"
SET=$(grep -o 'Empreinte globale du set (sha256 de la liste ci-dessus) : `[0-9a-f]*`' "$MAN" | grep -o '[0-9a-f]\{64\}')
NTARCH=$(grep -m1 'MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md$' "$MAN" | cut -c1-64)
ARBRE_MAN=$(grep -o 'Arbre git (local = publié) | `[0-9a-f]*`' "$MAN" | grep -o '[0-9a-f]\{40\}')
if [ -z "$(git -C "$RACINE/profreg" status --porcelain 2>/dev/null)" ]; then
  ARBRE=$(git -C "$RACINE/profreg" rev-parse 'HEAD^{tree}')
else
  ARBRE="$(git -C "$RACINE/profreg" rev-parse 'HEAD^{tree}' 2>/dev/null || echo inconnu)+modifie"
fi
SCHEMA=$(H "$RACINE/schema/ecriture_duale.schema.json" | cut -c1-64)
RULES=$(cd "$RACINE" && find rules -name '*.yaml' | LC_ALL=C sort | xargs cat | H | cut -c1-64)
TOOLCHAIN=$(tr -d '\n' < "$RACINE/lean-toolchain")
CTX=$(mktemp)
trap 'rm -f "$CTX"' EXIT
printf '{"set_empreinte":"%s","ntarch_sha256":"%s","profreg_arbre_manifeste":"%s","profreg_arbre":"%s","schema_sha256":"%s","rules_sha256":"%s","toolchain":"%s"}\n' \
  "$SET" "$NTARCH" "$ARBRE_MAN" "$ARBRE" "$SCHEMA" "$RULES" "$TOOLCHAIN" > "$CTX"
if [ -n "$SORTIE" ]; then
  "$RACINE/.lake/build/bin/mrc-check" "$DOSSIER" "$CTX" > "$SORTIE"
  echo "$(H "$SORTIE" | cut -c1-64)  $SORTIE" >&2
else
  "$RACINE/.lake/build/bin/mrc-check" "$DOSSIER" "$CTX"
fi
