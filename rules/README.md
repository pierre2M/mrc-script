# rules/ — forme machine du noyau démontré MRC v5.7

Fichiers **générés** par `tools/gen_rules.py` à partir de `docs/NT-ARCH_v5.7_Noyau_demontre_ProfReg_2026-10-02.md`, de NT-ARCH v5.7 (empreinte courante : `corpus/_MANIFESTE_v5.7.md`), des sources ProfReg (état identifié par son arbre git) et du journal d'audit. Ne pas les éditer à la main : corriger la source, puis régénérer. L'en-tête de chaque fichier porte les empreintes de ses entrées.

| Fichier | Contenu | Champs |
| --- | --- | --- |
| `theoremes.yaml` | 143 théorèmes du noyau | `id`, `status: theorem`, `nature` (A architecture · T texte · G garde · L lecture), `lean_ref` (module, nom, axiomes Lean), `enonce` (paraphrase de la signature), `noyau_section`, `ntarch_sections`, `nomme_par_ntarch`, `rattachements` (CONV, AX) |
| `conventions.yaml` | 11 conventions rattachées | `id`, `status: convention`, `enonce`, `ancrages_profreg`, `rapport_aux_theoremes` |
| `axiomes.yaml` | 6 axiomes rattachés | `id`, `status: axiom`, `intitule`, `enonce`, `refutation`, `theoremes_lies` |

**Règles de lecture codées dans les champs.** Une entrée de nature `G` ou `L` n'est jamais un appui seul (NT-ARCH §8ter-bis, R-3, R-5). Une entrée de nature `T` ne qualifie que la table §8.5.2. Une convention ou un axiome n'est jamais présenté comme démontré ; `ancrages_profreg` en établit la forme, non la justesse.

Régénérer :
```bash
python3 tools/gen_rules.py --noyau docs/NT-ARCH_v5.7_Noyau_demontre_ProfReg_2026-10-02.md \
  --ntarch <set>/MRC_v5.7/MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md \
  --profreg <ProfReg> --audit <ProfReg>/audit/audit_2026-10-07_D7.log --out rules
```

**Licence.** Ces fichiers dérivent du texte du set : CC BY-NC-SA 4.0 (`../LICENSES/CC-BY-NC-SA-4.0.txt`).
