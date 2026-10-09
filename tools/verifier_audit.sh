#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
# Phase 2d — seuils figés de l'audit ProfReg. Échec si :
#   · une ligne d'audit porte `sorryAx` ;
#   · le nombre de théorèmes dépendant de `Classical.choice` dépasse la valeur figée ;
#   · le nombre de déclarations auditées diffère de la valeur figée (un théorème ajouté ou
#     retiré doit être une décision tracée : on modifie alors les valeurs ci-dessous) ;
#   · le journal contient une erreur de compilation.
# Usage : tools/verifier_audit.sh <journal d'audit>
set -euo pipefail
THEOREMES_FIGES=533        # Consolidé §1 (07/10/2026)
CLASSICAL_MAX=10           # Consolidé §3
LOG=$1
N=$(grep -c "axioms" "$LOG" || true)
S=$(grep -c "sorryAx" "$LOG" || true)
C=$(grep -c "Classical.choice" "$LOG" || true)
E=$(grep -ci "error" "$LOG" || true)
echo "audit : $N théorèmes · $S sorryAx · $C Classical.choice · $E erreur(s)"
ok=1
[ "$S" -eq 0 ] || { echo "ÉCHEC : sorryAx présent"; ok=0; }
[ "$C" -le "$CLASSICAL_MAX" ] || { echo "ÉCHEC : Classical.choice $C > $CLASSICAL_MAX (valeur figée)"; ok=0; }
[ "$N" -eq "$THEOREMES_FIGES" ] || { echo "ÉCHEC : $N théorèmes ≠ $THEOREMES_FIGES (valeur figée)"; ok=0; }
[ "$E" -eq 0 ] || { echo "ÉCHEC : erreur dans le journal"; ok=0; }
[ "$ok" -eq 1 ]
