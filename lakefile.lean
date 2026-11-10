-- SPDX-License-Identifier: AGPL-3.0-only
import Lake
open Lake DSL

/-! `mrc-script` — validateur déterministe du pilote C (phase 2).

Aucune dépendance Lake : ProfReg est lu dans `profreg/` (lien vers une copie de
`github.com/pierre2M/ProfReg`), dont l'arbre git est vérifié contre
`corpus/_MANIFESTE_v5.7.md` avant tout contrôle (`tools/mrc-check.sh`).
Seuls les modules du pilote sont compilés : ils ne dépendent pas de Mathlib.
Les définitions exécutées sont celles de ProfReg — aucune n'est réécrite ici. -/

package «mrc-script»

lean_lib ProfReg where
  srcDir := "profreg"
  -- Tous les modules sont connus de Lake ; seuls ceux qu'importe `MrcCheck` sont compilés
  -- (`lake build` construit l'exécutable, non la bibliothèque entière).
  globs := #[.submodules `ProfReg]

lean_lib MrcCheck

@[default_target]
lean_exe «mrc-check» where
  root := `Main
