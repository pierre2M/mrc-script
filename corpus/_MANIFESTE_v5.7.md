# MRC v5.7 — Manifeste de l'état de référence

*État au 29/10/2026. La v5.7 n'est pas stabilisée : elle reste modifiable sans autre numéro de version. Ce manifeste est **régénéré après chaque modification** d'un des fichiers listés ; un fichier dont l'empreinte diffère de celle-ci a été modifié depuis.*

Licence du texte : CC BY-NC-SA 4.0 (`_LICENCE_v5.7.md`). Licence de ProfReg : AGPL-3.0-only.

## 1. Set v5.7 — 17 fichiers

Hors manifeste : `_ETAT_INSCRIPTION_v5.7.md` (journal), `_LICENCE_v5.7.md` et le présent fichier.

```
f3409195bd9b531422ea25ad996887fcf7905695ece250659218be7f3278647d  MRC_v5.7_Annexe_H_Dataroom_augmentee.md
059c8ff3f76e17f348326a7d31b156b09e93f1e85fbb433775f0fecb3eccd580  MRC_v5.7_Annexe_K_Cas_Chiffres.md
7e18c9c291cf43472b2d46ec2e739c5c42317db5c05abb4e25a67349a8fb87bf  MRC_v5.7_Annexe_Methodologique.md
131308b8cb68dfd10b320823490003665177703fcd4df6211e8b8bfb6b668b8c  MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md
f719a49f3794320b24158e43fa5c717a1cc992316085ca089e7bd229871e166e  MRC_v5.7_NT-G10_DemocratieEpistemique.md
b3f41138a09b7c3a1a3fc743cd08551b72a357bc3ff6a0b69a9e76272e73f5e5  MRC_v5.7_NT-G11_Travail.md
cb5323587a9df0fd22d1858e9e1c1545cbc0d08ca1b892f794b6292c5caaa78a  MRC_v5.7_NT-G12_Valuation.md
aa46da573cc4956e8865804ffc401b09aa2575c61b5ec95ab366e17402363a04  MRC_v5.7_NT-G1_Evolutivite.md
73884fc7124c932cf3cf94c3632e141a4e1b32df3f7f6e6b888be8ae097d10df  MRC_v5.7_NT-G2_Responsabilite.md
dc203f6b04dd8aaac9849c59efa956acb2b6b5f0ec3cb1f7752a3e83cb14e701  MRC_v5.7_NT-G3_Soin.md
8cec232104b8da399b90174102166ab1e2d2e71ba65ece2819fafc7707718bbf  MRC_v5.7_NT-G4_Performativite.md
25d5cbb523883680aae8a4cb27671fd195e12e108705247cf68509f3fd38b5ec  MRC_v5.7_NT-G5_Mesologie.md
bf416e94de935fb6f8862a1fd521dfb8e207d9dc40797c02685df8900ff9a28e  MRC_v5.7_NT-G6_Communalite.md
e21138087bac0726ac85f7b12d3f0246bc3de01d610240ba76f4bb5fa5feee96  MRC_v5.7_NT-G7_Justice.md
8f29be2acb6c640d08b2186dbb8b07551db8aa4001690ebfa7377181efa7ea9f  MRC_v5.7_NT-G8_Mimetique.md
363e2cd38e4d18f4bf0d15786cb3d821a926d29d2025f306a20cf88ced6db941  MRC_v5.7_NT-G9_Affectif.md
8a70bd9221e3648e74f37410ca77137cd235ea9737bbfc976a35f13de1188a97  MRC_v5.7_ProfReg_Consolide.md
```

Empreinte globale du set (sha256 de la liste ci-dessus) : `ad3b094a2e4dfc7f2cb501d4faf6a568b6c5e2d82dec2fc003571faf286cbbf8`

## 2. ProfReg

Sur GitHub, **seul l'état courant est publié**, en un commit unique sans historique ; les versions antérieures et leurs tags sont conservés localement. L'identifiant commun à l'état local et à l'état publié est l'**arbre git**.

| | |
| --- | --- |
| Arbre git (local = publié) | `68c98f774af444d541be298224b02e2c3d75c074` |
| Commit local | `a4a9933733f8957f47da97f7f221bd27a0152ffa` (branche `main`, locale) ; commit publié `c17078628bf60b9d66b6f2b1ed7c8b798387f4bd` |
| Licence | AGPL-3.0-only |
| Chaîne | `leanprover/lean4:v4.31.0-rc1` |
| `lake-manifest.json` (sha256) | `e913e2caed2b815520c44aab02119e55ee1fe8b2a735ea899c70b66267e55b6c` |
| Mathlib | `1a59aa5b8603fd850ee2dc6ef9e35a44fe351599` |
| Audit | 604 théorèmes · 0 `sorryAx` · 10 `Classical.choice` · 0 `axiom` (`audit/audit_2026-10-13_PR59.log`, sha256 `a11bfdb536b09fc2204faf90699a50d19df2ecfe85455b112b6fbeb8ba09cc35`) |
| Instantané Lean | `ProfReg/Instantanes_Lean/ProfReg_Lean_2026-10-13_604thm/` — empreinte globale `07e09ab782e4b5275ebf8f7bf554053e6b885f74e82659cfdc380bb39fc24e92` ; archive sha256 `6746c1d1883dd67cf22709267b840c28c27272b87c0d32ec8ef343081588984c` ; sources de l'arbre `3a6c9257`, qui ne diffère de l'arbre ci-dessus que par le README |

## 3. Vérifier

```bash
cd MRC_v5.7 && sed -n "/^\`\`\`$/,/^\`\`\`$/p" _MANIFESTE_v5.7.md | sed "1d;\$d" | head -n 17 | shasum -a 256 -c
git -C ~/Developer/ProfReg rev-parse 'HEAD^{tree}'                  # attendu : arbre ci-dessus
git ls-remote https://github.com/pierre2M/ProfReg main | cut -f1 | xargs -I{} git -C ~/Developer/ProfReg cat-file -p {} | head -1   # « tree » attendu identique (après git fetch)
```

## 4. Régénérer

Après toute modification d'un fichier du set : relancer la génération de ce manifeste, puis `tools/gen_rules.py` dans `mrc-script` (les en-têtes de `rules/` portent l'empreinte de NT-ARCH).
