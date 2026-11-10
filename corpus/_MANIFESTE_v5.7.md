# MRC v5.7 — Manifeste de l'état de référence

*État au 10/11/2026 (décisions n° 62 et 63). La v5.7 n'est pas stabilisée : elle reste modifiable sans autre numéro de version. Ce manifeste est **régénéré après chaque modification** d'un des fichiers listés ; un fichier dont l'empreinte diffère de celle-ci a été modifié depuis.*

Licence du texte : CC BY-NC-SA 4.0 (`_LICENCE_v5.7.md`). Licence de ProfReg : AGPL-3.0-only.

## 1. Set v5.7 — 17 fichiers

Hors manifeste : `_ETAT_INSCRIPTION_v5.7.md` (journal), `_LICENCE_v5.7.md` et le présent fichier.

```
f3409195bd9b531422ea25ad996887fcf7905695ece250659218be7f3278647d  MRC_v5.7_Annexe_H_Dataroom_augmentee.md
059c8ff3f76e17f348326a7d31b156b09e93f1e85fbb433775f0fecb3eccd580  MRC_v5.7_Annexe_K_Cas_Chiffres.md
734e57c102618f6653edf7a6fa413dab72e53e79d9b9454689a256c08952d211  MRC_v5.7_Annexe_Methodologique.md
1f365c94c83f5bc70d8eac8c1aa7c7bd77efcf564c26d55c1cbac383d54f839f  MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md
f719a49f3794320b24158e43fa5c717a1cc992316085ca089e7bd229871e166e  MRC_v5.7_NT-G10_DemocratieEpistemique.md
3fe67a62784d7c62b058e4a5b26d3e2e5444deb0cb55e03fa1a4fc3cbd8dcdc8  MRC_v5.7_NT-G11_Travail.md
cb5323587a9df0fd22d1858e9e1c1545cbc0d08ca1b892f794b6292c5caaa78a  MRC_v5.7_NT-G12_Valuation.md
aa46da573cc4956e8865804ffc401b09aa2575c61b5ec95ab366e17402363a04  MRC_v5.7_NT-G1_Evolutivite.md
73884fc7124c932cf3cf94c3632e141a4e1b32df3f7f6e6b888be8ae097d10df  MRC_v5.7_NT-G2_Responsabilite.md
dc203f6b04dd8aaac9849c59efa956acb2b6b5f0ec3cb1f7752a3e83cb14e701  MRC_v5.7_NT-G3_Soin.md
65682180968ecbd6c4faeb240e9f87203ab6b67445d1a60fe7ffafcacbe8cf7d  MRC_v5.7_NT-G4_Performativite.md
25d5cbb523883680aae8a4cb27671fd195e12e108705247cf68509f3fd38b5ec  MRC_v5.7_NT-G5_Mesologie.md
ba8acba181b84ae0f1c1fb7d3f0e11f474f91d82a735f7bb52304589ddacc34a  MRC_v5.7_NT-G6_Communalite.md
e21138087bac0726ac85f7b12d3f0246bc3de01d610240ba76f4bb5fa5feee96  MRC_v5.7_NT-G7_Justice.md
8f29be2acb6c640d08b2186dbb8b07551db8aa4001690ebfa7377181efa7ea9f  MRC_v5.7_NT-G8_Mimetique.md
363e2cd38e4d18f4bf0d15786cb3d821a926d29d2025f306a20cf88ced6db941  MRC_v5.7_NT-G9_Affectif.md
823442df39a4923a0d35ff8ae3f6813a3cecddf9324773d62bc4db310e3a6386  MRC_v5.7_ProfReg_Consolide.md
```

Empreinte globale du set (sha256 de la liste ci-dessus) : `53cf46738edf1db3375e8091b5f9d327be9bb12ed493ed40b0634a627e29b9d2`

## 2. ProfReg

> **État du 10/11/2026 (décisions n° 62 et 63)** : PR-60 versé, compilé, commité, instantané déposé, **publié sur GitHub** (commit unique `10f6676d`, arbre identique à l'état local).

Sur GitHub, **seul l'état courant est publié**, en un commit unique sans historique ; les versions antérieures et leurs tags sont conservés localement. L'identifiant commun à l'état local et à l'état publié est l'**arbre git**.

| | |
| --- | --- |
| Arbre git (local = publié) | `48ab6c29f011048c12c1558f9413a3a064345a22` |
| Commit local | `c1f288fa691437a81a7a33092d40f3ce17b7ca45` (branche `main`, locale) ; commit publié `10f6676dc6c0f8003a688536fb00665dd3b3539c` (10/11/2026 ; précédent : `c17078628bf60b9d66b6f2b1ed7c8b798387f4bd`, arbre `68c98f77`) |
| Licence | AGPL-3.0-only |
| Chaîne | `leanprover/lean4:v4.31.0-rc1` |
| `lake-manifest.json` (sha256) | `e913e2caed2b815520c44aab02119e55ee1fe8b2a735ea899c70b66267e55b6c` |
| Mathlib | `1a59aa5b8603fd850ee2dc6ef9e35a44fe351599` |
| Audit | 614 théorèmes · 0 `sorryAx` · 10 `Classical.choice` · 0 `axiom` (`audit/audit_2026-11-10_PR60.log`, sha256 `1547267f7833704f7a9972652c642b4121a819a55c3752bde5a7730d7976016c`) |
| Instantané Lean | `ProfReg/Instantanes_Lean/ProfReg_Lean_2026-11-10_614thm/` — empreinte globale `91b41df5419936df7f26be18809f4e6b1992bd74a6a582ad0b69fd1ca0135808` ; archive sha256 `8a6dfbd00192208f23399d460c45d01d790f1853663b68c61fa1305dcb415180` ; sources de l'arbre `48ab6c29` (contenu commité) |

## 3. Vérifier

```bash
cd MRC_v5.7 && sed -n "/^\`\`\`$/,/^\`\`\`$/p" _MANIFESTE_v5.7.md | sed "1d;\$d" | head -n 17 | shasum -a 256 -c
git -C ~/Developer/ProfReg rev-parse 'HEAD^{tree}'                  # attendu : arbre ci-dessus
git ls-remote https://github.com/pierre2M/ProfReg main | cut -f1 | xargs -I{} git -C ~/Developer/ProfReg cat-file -p {} | head -1   # « tree » attendu identique (après git fetch)
```

## 4. Régénérer

Après toute modification d'un fichier du set : relancer la génération de ce manifeste, puis `tools/gen_rules.py` dans `mrc-script` (les en-têtes de `rules/` portent l'empreinte de NT-ARCH).
