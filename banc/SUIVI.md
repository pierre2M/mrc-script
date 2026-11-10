<!-- Généré par tools/banc.py — NE PAS ÉDITER À LA MAIN -->
# Banc d'essai du pilote C — suivi de la validation explicite

*Ce que mesure le banc : si les écritures proposées peuvent être comprises puis validées, précisées ou refusées par la personne qui en a la responsabilité, avec l'aide d'une fiche de lecture et d'un agent d'explicitation. Cas locaux : comptes seulement ; pièces et produits au dépôt privé, ouvert à des vérificateurs désignés (décision D6).*

| Cas | Titre | Instruction | Espace | Proposant | Contrôle formel | Questions posées | Avis par écriture | Décision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S1 *(synthétique)* | Rivière et entreprise — essai de chaîne | synthetique | dépôt | — | — | 0 | — | sans_proposition |
| C1 | RATP ↔ IDFM, exercice 2025 | constitue | local | — | — | 0 | — | sans_proposition |
| C2 | La Fabrique de l'Emploi ↔ salariés, capitaux humains 2025 | constitue | local | anthropic / claude-opus-5-5 | refuse | 1 (utile 1) | comprise_validee 4 | rejetee |
| C2b | La Fabrique de l'Emploi ↔ salariés, ancrage de LFDE fictif, sans registre des salariés | fictif | local | anthropic / claude-sonnet-5-5 | CONTROLE_ECHOUE | 1 (utile 1) | — | en_examen |
| C2c | La Fabrique de l'Emploi ↔ registre d'attente des salariés | constitue | local | anthropic / claude-sonnet-5-5 | mal_forme | 3 (utile 3) | comprise_validee 8 | validee |
| C3a | MEL ↔ registre du sol de la friche Nollet (Trichon) | constitue | local | anthropic / claude-opus-5-5 | refuse | 2 (non_appreciee 1, utile 1) | — | rejetee |
| C3b | CPU ↔ registre du sol de la friche Nollet (Trichon) | constitue | local | — | — | 0 | — | sans_proposition |
| C3c | MEL ↔ CPU, financement de la reconstitution du sol (Trichon) | constitue | local | — | — | 0 | — | sans_proposition |

**Totaux (hors cas synthétiques)** — dossiers : en examen 1 · rejetee 2 · sans proposition 3 · validee 1 ; écritures : comprise validee 12 ; réponses de l'agent d'explicitation : non appreciee 1 · utile 6
