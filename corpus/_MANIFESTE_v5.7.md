# MRC v5.7 — Manifeste de l'état de référence

*État au 13/10/2026. La v5.7 n'est pas stabilisée : elle reste modifiable sans autre numéro de version. Ce manifeste est **régénéré après chaque modification** d'un des fichiers listés ; un fichier dont l'empreinte diffère de celle-ci a été modifié depuis.*

Licence du texte : CC BY-NC-SA 4.0 (`_LICENCE_v5.7.md`). Licence de ProfReg : AGPL-3.0-only.

## 1. Set v5.7 — 17 fichiers

Hors manifeste : `_ETAT_INSCRIPTION_v5.7.md` (journal), `_LICENCE_v5.7.md` et le présent fichier.

```
f3409195bd9b531422ea25ad996887fcf7905695ece250659218be7f3278647d  MRC_v5.7_Annexe_H_Dataroom_augmentee.md
59d0e34787e06e1b07e0df581555b70c5eae24a6a26e3169e77b092bb9707886  MRC_v5.7_Annexe_K_Cas_Chiffres.md
a555de3dcdfe2e279571e68882c70230e7302082e57c97cfbec105d86cf21ad8  MRC_v5.7_Annexe_Methodologique.md
60bdda938e9cd33fc0b5a5a7f5d641f08c8a1b3597f8349670a1d0e519e14567  MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md
2b5e9326f431bb33d286fce2759fe19a77a667cb806dcb02d41c15b563dd2da8  MRC_v5.7_NT-G10_DemocratieEpistemique.md
e64d64ce5e89c28bf704352656920a42e81fd8beba4d045d1fc06e3aa0189bf4  MRC_v5.7_NT-G11_Travail.md
af8d4d82a4cdba422d2500db60caf5a0de133126461269e2b02192806ea91af1  MRC_v5.7_NT-G12_Valuation.md
f9c7fa0e7f520e04a17854b2776f1cb4b1b2c180feb1de15782652daeb7833a8  MRC_v5.7_NT-G1_Evolutivite.md
cc295cb6b77d0eae66f3759671874b696d2138546061770193f0d88b0b225ed9  MRC_v5.7_NT-G2_Responsabilite.md
9dbd45fae6964e1b184585c14825c7990c5414c2a0383c7457dd015b00d8215e  MRC_v5.7_NT-G3_Soin.md
13dd0ceaea6ebd7ca33dfba4349eb863c930d3cc88239e3cc3b5422fcb01f121  MRC_v5.7_NT-G4_Performativite.md
591b320350a30b209392cddf472a2edcd94d42b7a39a19d4d75e7eec5a066260  MRC_v5.7_NT-G5_Mesologie.md
d2ff24cb6df790e6491ee94fce17de720baf936c0367a6198574a96bb01acc2d  MRC_v5.7_NT-G6_Communalite.md
04db32cf4edcd95828b869107a0c5a4ab3786e391efa6b421dc35f1b3e2324a4  MRC_v5.7_NT-G7_Justice.md
7a022b3e0a0655089856323e25fdc5e003f0221070c44bfecd31a5c74f166c1e  MRC_v5.7_NT-G8_Mimetique.md
b6e7e806bb2bea2d58a90f1c2d43f89246c31f82246fe129f0e79d69b150c547  MRC_v5.7_NT-G9_Affectif.md
0ad212e7f4805017d49fa1082db7c9d1151863c72badf002a2898c9818aab9cb  MRC_v5.7_ProfReg_Consolide.md
```

Empreinte globale du set (sha256 de la liste ci-dessus) : `253596817c44312b5ec390ea0519774fe768d19455dff5dd40a1ccd028bd888d`

## 2. ProfReg

Sur GitHub, **seul l'état courant est publié**, en un commit unique sans historique ; les versions antérieures et leurs tags sont conservés localement. L'identifiant commun à l'état local et à l'état publié est l'**arbre git**.

| | |
| --- | --- |
| Arbre git (local = publié) | `39285595206e664d5b6ab4b23e7d00d2f27b8033` |
| Commit local | `fef75933275cd1b8e787287a43e32826b1212be4` (branche `main`, locale) ; commit publié `fe015fe8eade6485374f67176008a62bb576563f` |
| Licence | AGPL-3.0-only |
| Chaîne | `leanprover/lean4:v4.31.0-rc1` |
| `lake-manifest.json` (sha256) | `e913e2caed2b815520c44aab02119e55ee1fe8b2a735ea899c70b66267e55b6c` |
| Mathlib | `1a59aa5b8603fd850ee2dc6ef9e35a44fe351599` |
| Audit | 596 théorèmes · 0 `sorryAx` · 10 `Classical.choice` · 0 `axiom` (`audit/audit_2026-10-13_PR58.log`, sha256 `b16e13c1bf62ca7db9a1ea2a813b9f5d88afa6facadee4fb960170907d788e23`) |
| Instantané Lean | `ProfReg/Instantanes_Lean/ProfReg_Lean_2026-10-13_596thm/` — empreinte globale `44fd1c225180333cbef0a55a6519157cdf39de3d29996e5ac57578cdaebb8e9b` ; archive sha256 `762d2ff71d326a469c01bfb680823f375b7ad43c6695b492fdf38287519863d3` |

## 3. Vérifier

```bash
cd MRC_v5.7 && sed -n "/^\`\`\`$/,/^\`\`\`$/p" _MANIFESTE_v5.7.md | sed "1d;\$d" | head -n 17 | shasum -a 256 -c
git -C ~/Developer/ProfReg rev-parse 'HEAD^{tree}'                  # attendu : arbre ci-dessus
git ls-remote https://github.com/pierre2M/ProfReg main | cut -f1 | xargs -I{} git -C ~/Developer/ProfReg cat-file -p {} | head -1   # « tree » attendu identique (après git fetch)
```

## 4. Régénérer

Après toute modification d'un fichier du set : relancer la génération de ce manifeste, puis `tools/gen_rules.py` dans `mrc-script` (les en-têtes de `rules/` portent l'empreinte de NT-ARCH).
