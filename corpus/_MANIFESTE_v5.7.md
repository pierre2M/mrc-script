# MRC v5.7 — Manifeste de l'état de référence

*État au 07/10/2026. La v5.7 n'est pas stabilisée : elle reste modifiable sans autre numéro de version. Ce manifeste est **régénéré après chaque modification** d'un des fichiers listés ; un fichier dont l'empreinte diffère de celle-ci a été modifié depuis.*

Licence du texte : CC BY-NC-SA 4.0 (`_LICENCE_v5.7.md`). Licence de ProfReg : AGPL-3.0-only.

## 1. Set v5.7 — 17 fichiers

Hors manifeste : `_ETAT_INSCRIPTION_v5.7.md` (journal), `_LICENCE_v5.7.md` et le présent fichier.

```
f3409195bd9b531422ea25ad996887fcf7905695ece250659218be7f3278647d  MRC_v5.7_Annexe_H_Dataroom_augmentee.md
79a1a89de011ffb27ca554e1dbad6ad888d672fe30fc31e3e527dd9479872ae4  MRC_v5.7_Annexe_K_Cas_Chiffres.md
a00df1a336eac9122be69b4cd0e6f890277fc45380f1df49a50961d32f0d791d  MRC_v5.7_Annexe_Methodologique.md
c8f40040667710c6d9f706530d50107de62186ede0a1020039bbe12dc10492ad  MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md
ade2b930546de765099b057c65ee27e012d78c8d6881d1d84858d58a5695e471  MRC_v5.7_NT-G10_DemocratieEpistemique.md
3d011d5fc0d51a7101c2d3bfeb3339deb62c678ae49efdeec5e0f0f8470c43e3  MRC_v5.7_NT-G11_Travail.md
af8d4d82a4cdba422d2500db60caf5a0de133126461269e2b02192806ea91af1  MRC_v5.7_NT-G12_Valuation.md
f9c7fa0e7f520e04a17854b2776f1cb4b1b2c180feb1de15782652daeb7833a8  MRC_v5.7_NT-G1_Evolutivite.md
89a81b11f76180ee881908c92db25cfe74f1d14af9ebdfff5f3a4655941bb138  MRC_v5.7_NT-G2_Responsabilite.md
068a6b38f921ba78cea955113f2d0b9f9255cf919e4e3604ca0071a42f49ad18  MRC_v5.7_NT-G3_Soin.md
0f7bb5773edd7ef1a38999b12053e99aa31bc2201c37f40d73314bb415d29107  MRC_v5.7_NT-G4_Performativite.md
591b320350a30b209392cddf472a2edcd94d42b7a39a19d4d75e7eec5a066260  MRC_v5.7_NT-G5_Mesologie.md
f5fd2e14278efdf039cb4d423e91a6f8e048583991711d9938a5e512196473d8  MRC_v5.7_NT-G6_Communalite.md
476aadaf9ffb41bf86a42ea3b8739333e1cf5544f381ee4d2f0f5203c71e96b1  MRC_v5.7_NT-G7_Justice.md
8c8a0e68510e0099ccffd45f27475096dab0c72336ea6df3be417b62e7f2c755  MRC_v5.7_NT-G8_Mimetique.md
dbd25c14536c0261e3a4a5614a687769b9cb871071b96a1b8016e2f562b46989  MRC_v5.7_NT-G9_Affectif.md
34c63f824d8a9de8dd1d8af488a58329a72707c78e08f150d4a093d8d1dbc069  MRC_v5.7_ProfReg_Consolide.md
```

Empreinte globale du set (sha256 de la liste ci-dessus) : `1d4073146894bb7cbf337341a5a3bb015943d27a193b8e463546f68429e174e6`

## 2. ProfReg

Sur GitHub, **seul l'état courant est publié**, en un commit unique sans historique ; les versions antérieures et leurs tags sont conservés localement. L'identifiant commun à l'état local et à l'état publié est l'**arbre git**.

| | |
| --- | --- |
| Arbre git (local = publié) | `4ef762772e34a412152f4a63f55b674eaac967df` |
| Commit local | `68080d08c47e5757a070feabab0b815896a506e5` (branche `main`, locale) |
| Licence | AGPL-3.0-only |
| Chaîne | `leanprover/lean4:v4.31.0-rc1` |
| `lake-manifest.json` (sha256) | `e913e2caed2b815520c44aab02119e55ee1fe8b2a735ea899c70b66267e55b6c` |
| Mathlib | `1a59aa5b8603fd850ee2dc6ef9e35a44fe351599` |
| Audit | 533 théorèmes · 0 `sorryAx` · 10 `Classical.choice` · 0 `axiom` (`audit/audit_2026-10-07_D7.log`, sha256 `61ebbdac64316f028cfbad2bb279536374e44d7f85b693ad093e059716540ae2`) |
| Instantané Lean | `ProfReg/Instantanes_Lean/ProfReg_Lean_2026-10-07_533thm/` — empreinte globale `44cf9dc6fd193ff2e23372fc6d498be05b2bfec91094f498b6741126d97c22db` ; archive sha256 `d963c150d1912b24d72c067aebdd2aa2f65ad2b4c5d2451ecd6724ba8f3d6a24` |

## 3. Vérifier

```bash
cd MRC_v5.7 && sed -n "/^\`\`\`$/,/^\`\`\`$/p" _MANIFESTE_v5.7.md | sed "1d;\$d" | head -n 17 | shasum -a 256 -c
git -C ~/Developer/ProfReg rev-parse 'HEAD^{tree}'                  # attendu : arbre ci-dessus
git ls-remote https://github.com/pierre2M/ProfReg main | cut -f1 | xargs -I{} git -C ~/Developer/ProfReg cat-file -p {} | head -1   # « tree » attendu identique (après git fetch)
```

## 4. Régénérer

Après toute modification d'un fichier du set : relancer la génération de ce manifeste, puis `tools/gen_rules.py` dans `mrc-script` (les en-têtes de `rules/` portent l'empreinte de NT-ARCH).
