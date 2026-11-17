# MRC v5.7 — Manifeste de l'état de référence

*État au 17/11/2026 (décisions n° 64 à 69). La v5.7 n'est pas stabilisée : elle reste modifiable sans autre numéro de version. Ce manifeste est **régénéré après chaque modification** d'un des fichiers listés ; un fichier dont l'empreinte diffère de celle-ci a été modifié depuis.*

Licence du texte : CC BY-NC-SA 4.0 (`_LICENCE_v5.7.md`). Licence de ProfReg : AGPL-3.0-only.

## 1. Set v5.7 — 17 fichiers

Hors manifeste : `_ETAT_INSCRIPTION_v5.7.md` (journal), `_LICENCE_v5.7.md` et le présent fichier.

```
f3409195bd9b531422ea25ad996887fcf7905695ece250659218be7f3278647d  MRC_v5.7_Annexe_H_Dataroom_augmentee.md
059c8ff3f76e17f348326a7d31b156b09e93f1e85fbb433775f0fecb3eccd580  MRC_v5.7_Annexe_K_Cas_Chiffres.md
80f04c38e885ecb6f20b6d96b83b5b83809f68e5ff8e7e258f8edb52c9bf266c  MRC_v5.7_Annexe_Methodologique.md
ad672eab8549dbf3ced72db95e54d58887d3eb688549873f8ac7433c83637308  MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md
f195be4503392f0561e479edd2817eaecfaf873f1f8427bf1cabb418e0c286b2  MRC_v5.7_NT-G10_DemocratieEpistemique.md
3fe67a62784d7c62b058e4a5b26d3e2e5444deb0cb55e03fa1a4fc3cbd8dcdc8  MRC_v5.7_NT-G11_Travail.md
cb5323587a9df0fd22d1858e9e1c1545cbc0d08ca1b892f794b6292c5caaa78a  MRC_v5.7_NT-G12_Valuation.md
aa46da573cc4956e8865804ffc401b09aa2575c61b5ec95ab366e17402363a04  MRC_v5.7_NT-G1_Evolutivite.md
73884fc7124c932cf3cf94c3632e141a4e1b32df3f7f6e6b888be8ae097d10df  MRC_v5.7_NT-G2_Responsabilite.md
dc203f6b04dd8aaac9849c59efa956acb2b6b5f0ec3cb1f7752a3e83cb14e701  MRC_v5.7_NT-G3_Soin.md
383b7127366197be0a84cb1442c9ebb699f9c12b18b1c20c6ecc414dfb405031  MRC_v5.7_NT-G4_Performativite.md
25d5cbb523883680aae8a4cb27671fd195e12e108705247cf68509f3fd38b5ec  MRC_v5.7_NT-G5_Mesologie.md
ba8acba181b84ae0f1c1fb7d3f0e11f474f91d82a735f7bb52304589ddacc34a  MRC_v5.7_NT-G6_Communalite.md
e21138087bac0726ac85f7b12d3f0246bc3de01d610240ba76f4bb5fa5feee96  MRC_v5.7_NT-G7_Justice.md
8f29be2acb6c640d08b2186dbb8b07551db8aa4001690ebfa7377181efa7ea9f  MRC_v5.7_NT-G8_Mimetique.md
363e2cd38e4d18f4bf0d15786cb3d821a926d29d2025f306a20cf88ced6db941  MRC_v5.7_NT-G9_Affectif.md
9e2212f017c0bdb45d5c58fc87b5015456a8ce5264a34c75b124cbc467cf9471  MRC_v5.7_ProfReg_Consolide.md
```

Empreinte globale du set (sha256 de la liste ci-dessus) : `eee11f00b94e4c1f1aec5b92a921efb2909b36a9e25cc2264ce138a60e3a21a9`

## 2. ProfReg

> **État du 17/11/2026 (décision n° 69)** : PR-61 modifié (date de déclaration du périmètre), compilé, commité, instantané déposé, **publié sur GitHub** (commit unique `b6d585b6`, arbre identique à l'état local ; `refs/publie/main` vérifié).

Sur GitHub, **seul l'état courant est publié**, en un commit unique sans historique ; les versions antérieures et leurs tags sont conservés localement. L'identifiant commun à l'état local et à l'état publié est l'**arbre git**.

| | |
| --- | --- |
| Arbre git (local = publié) | `d573858531fe6149158ae80bb6aacebfcb64cce5` |
| Commit local | `319e2cdba0f25d93aaf0a71b8e877e0f4d435062` (branche `main`, locale) ; commit publié `b6d585b6b94e618488281ddfef57c1f6b0983a28` (17/11/2026 ; précédent : `2096f0f3d7c87b87ba0553e39789cf520da20a9d`, arbre `f82380a7`) |
| Licence | AGPL-3.0-only |
| Chaîne | `leanprover/lean4:v4.31.0-rc1` |
| `lake-manifest.json` (sha256) | `e913e2caed2b815520c44aab02119e55ee1fe8b2a735ea899c70b66267e55b6c` |
| Mathlib | `1a59aa5b8603fd850ee2dc6ef9e35a44fe351599` |
| Audit | 625 théorèmes · 0 `sorryAx` · 10 `Classical.choice` · 0 `axiom` (`audit/audit_2026-11-17_PR61-n69.log`, sha256 `dda6354ca952550657de03d14c9e76018e475a33e0cb8f7aac59377e0ce27c12`) |
| Instantané Lean | `ProfReg/Instantanes_Lean/ProfReg_Lean_2026-11-17_625thm/` — empreinte globale `6c304f561f14d4a6089d068c83a762835ecba60ff02d59e9a810c5b39e0c4b24` ; archive sha256 `bf157dea4f83c37afeb4a9784bf8e361080fa85699bbc436a0ba48e9cda17d8b` ; sources de l'arbre `d5738585` (contenu commité) |

## 3. Vérifier

```bash
cd MRC_v5.7 && sed -n "/^\`\`\`$/,/^\`\`\`$/p" _MANIFESTE_v5.7.md | sed "1d;\$d" | head -n 17 | shasum -a 256 -c
git -C ~/Developer/ProfReg rev-parse 'HEAD^{tree}'                  # attendu : arbre ci-dessus
git ls-remote https://github.com/pierre2M/ProfReg main | cut -f1 | xargs -I{} git -C ~/Developer/ProfReg cat-file -p {} | head -1   # « tree » attendu identique (après git fetch)
```

## 4. Régénérer

Après toute modification d'un fichier du set : relancer la génération de ce manifeste, puis `tools/gen_rules.py` dans `mrc-script` (les en-têtes de `rules/` portent l'empreinte de NT-ARCH).
