<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->
# Banc d'essai du pilote C — validation explicite

**Méthode (décision du porteur, 09/10/2026).** Le banc ne compare pas la proposition de l'agent à une annotation de référence : personne n'a à produire, sans appui, le dossier « juste ». Il éprouve ce qui compte pour le registre : **les personnes qui ont la responsabilité de valider comprennent-elles les écritures proposées avant de décider ?** Leurs connaissances sont diverses ; le dispositif doit leur permettre de **valider, demander une précision ou refuser** en connaissance de cause.

**Déroulé, pour chaque cas.**
1. *Proposer* : l'agent rédige le dossier à partir de la source du cas (`agent/proposer.py --dossier-id …`). Les champs techniques (empreintes, arbre de ProfReg) sont posés par l'outil, jamais par une personne (`tools/reference.py` pour un proposant humain).
2. *Lire* : `tools/fiche.py` rédige, sans modèle de langage, la **fiche de lecture** du dossier : qui inscrit quoi envers qui, sur quelle pièce ; ce que le contrôle formel a établi, en mots ; ce qu'il ne vérifie pas ; les absences ; les questions à se poser écriture par écriture.
3. *Interroger* : la personne pose ses questions à l'**agent d'explicitation** (`agent/expliquer.py`). Il répond à partir du dossier, de la fiche, du reçu, des règles et des pièces, cite ce sur quoi il s'appuie, dit ce qu'il ne sait pas, et ne recommande aucune décision. Chaque échange est journalisé ; la personne apprécie chaque réponse (utile, insuffisante, erronée).
4. *Décider* : `tools/valider.py` exige **un avis par écriture** — comprise et validée, précision demandée (motif), refusée (motif) — et une décision cohérente : `validee` seulement si toutes les écritures sont comprises et validées ; une précision demandée renvoie le dossier (`retournee`). La fiche et le journal sont joints à la décision, leurs empreintes inscrites, l'ensemble signé.
5. *Suivre* : `tools/banc.py --mrc …` régénère le suivi (questions posées, appréciation des réponses, avis par écriture, décisions et motifs).

**Ce que le banc mesure.** La part des écritures comprises et validées, précisées, refusées ; le nombre et la nature des questions nécessaires ; la qualité des réponses de l'agent d'explicitation, jugée par la personne qui valide. Un agent de proposition est bon si ses écritures sont **validables en connaissance de cause**, non s'il reproduit une référence.

**Cas.** S1 (synthétique) éprouve la chaîne. C1 (RATP ↔ IDFM 2025), C2 (LFDE ↔ salariés), C3 (MEL ↔ CPU, sol du Trichon) sont constitués dans l'espace local du porteur (`banc_pilote_C/`, hors dépôt public). **D6 (09/10/2026) : accès restreint** — pièces et produits du banc versés au dépôt privé `mrc-banc-prive` (`tools/constituer_prive.py`), ouvert en lecture à des vérificateurs désignés, qui refont les contrôles avec `tools/verifier_prive.py`.

*Porteur :* P. M. (seul validateur, D10). *Critère :* au moins un cas historique proposé, examiné et décidé avant la phase 4.
