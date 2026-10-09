<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->
# Relevé des écarts : prompts v5.5 de `pierre2M/mrc` et table `rules/` (phase 3.2)

*Établi le 07/10/2026 sur `pierre2M/mrc` au commit `8f64b5e` (1er juillet 2026). Fichiers lus : `apps/web/src/lib/prompts/mrc-schema-full.ts` (159 lignes), `mrc-schema-light.ts` (65), `apps/web/src/lib/mrc-definition.ts` (43 ; réexporté par `prompts/mrc-definition.ts`). Relevé mécanique : `tools/releve_prompts.py`, sortie dans `releve_prompts_v55_table.md`.*

## Conclusion

**Les prompts v5.5 ne sont pas réutilisés par l'agent de proposition.** Le gabarit `agent/gabarit_instructions.md` est écrit à partir de `rules/pilote_C` et du schéma seulement. Raison : les prompts v5.5 et l'agent du pilote C n'ont pas le même objet ; aucune de leurs consignes ne porte sur une règle du pilote.

## Constats

| # | Constat | Source vérifiée |
| --- | --- | --- |
| 1 | **Objet différent.** Les prompts v5.5 demandent une **analyse de document** en 9 étapes (acteurs, régimes, modes F1–F4, grammaires, C-DROITS, C-SIGNAL, mémoire des pertes, enquête, performativité), en texte libre. L'agent du pilote C doit produire un **dossier JSON** conforme à un schéma, contrôlable par `mrc-check` | Lecture des trois fichiers |
| 2 | **Aucune notion du pilote C.** `teneur`, `rapprochement`, `ancrage`, `écriture duale`, `instance de contrôle`, `déclaration des concernés`, `triplet porteur`, `contrepartie` : 0 occurrence. `maintien` : 3 occurrences, au sens du régime attentionnel, non de CONV-11 | Relevé, second tableau |
| 3 | **Aucun identifiant des prompts n'est une règle du pilote.** 83 identifiants extraits ; aucun ne figure dans `rules/pilote_C`. Trois figurent dans le texte de la forme machine du noyau (`rules/theoremes.yaml`) : `carre_non_commutatif`, `MILIEU_DÉGRADÉ_PERSISTANT`, `RÉVISION_CONCEPTUELLE` | Relevé, premier tableau |
| 4 | **Quatorze identifiants sont absents du set v5.7** : `C-ENQUÊTE`, `C-MÉMOIRE`, `CHOIX_COLLECTIF`, `LES_DEUX`, `MÉSO_SECTORIEL`, `R-CRISE_MIMETIQUE`, `R-SITUATIONNALITÉ_BLOQUÉE`, `R-VICTIME_EMISSAIRE`, `REFUS_CADRE`, `cycle_performatif_détecté`, `dette_héritée_qualitative`, `identités_légitimes`, `pertes_documentées`, `signal_id`. Certains peuvent être des formes tronquées ou renommées d'identifiants du set ; le relevé ne le tranche pas | Relevé |
| 5 | **Nombre de grammaires incohérent.** 8 grammaires dans `mrc-schema-full` et `mrc-schema-light` ; 10 dans `mrc-definition` ; **12** dans NT-ARCH v5.7 (« Les douze grammaires transversales (NT-G1 → NT-G12) ») | Prompts ; NT-ARCH v5.7 l. 24 |
| 6 | **Échelle d'horizons périmée.** `C-INDEXATION-HORIZON` y finit par `EEA` ; NT-ARCH v5.7 ne contient plus `EEA` (0 occurrence ; 20 dans d'autres fichiers du set). `[PLAUSIBLE, NON VÉRIFIÉ — lien avec l'audit « D-2 suppression eea » du 27/09]` | Relevé ciblé |
| 7 | **Statut formel inexact.** « Existe-t-il une 2-cellule dans ProfReg ? » : en v5.7, la 2-cellule est hors ProfReg (F3 §3.5, horizon v6) ; `carre_non_commutatif` n'est plus un signal à détecter mais une **forme de signal** démontrée (PR-50) | NT-ARCH v5.7 F3 §3.3–3.5 |
| 8 | **Scores numériques demandés au modèle** (`risque_murray` 1–5, `autonomie_subordination` −5 à +5, `asymetrie_DEBIT_CREDIT` −5 à +5). `[À INSTRUIRE]` leur compatibilité avec CONV-14 (« aucun score composite ») n'est pas établie ici : ces scores sont par axe, non composites | Prompts ; CONV-14 |
| 9 | **Point d'accord.** `R-INCAPACITE-LLM-VALIDER` et « écritures validées par des humains, jamais par un LLM » concordent avec le pilote : l'agent ne produit que `PROPOSEE` | `mrc-definition.ts` ; NT-ARCH v5.7 (7 occurrences) |

## Ce que le relevé ne fait pas

Il constate des présences et des absences de chaînes ; il ne compare pas le sens d'un identifiant présent des deux côtés. Il ne propose pas de correction du site `pierre2M/mrc` (hors du programme : D2). `[LACUNE]` Le prompt de démonstration (`demo-prompt.ts`) et les prompts de vérification de cohérence (`verif-coherence-*.ts`) ne sont pas relevés : ils ne sont pas nommés par la tâche 3.2.
