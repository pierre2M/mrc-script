<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->
# Pilote C — écriture duale entre teneurs : table de règles (phase 1.2–1.3)

*État au 07/10/2026. Base : NT-ARCH v5.7 et ProfReg (empreinte et arbre git au manifeste `corpus/_MANIFESTE_v5.7.md`). Porteur du registre pilote : P. M.*

## Objet

Un **dossier** soumet deux registres à teneur, A et B, et leurs lignes réciproques (schéma : `schema/ecriture_duale.schema.json`). L'écriture duale est une **propriété du couple de registres**, non une condition de bonne formation d'une inscription (PR-35, D-ED-3) : un écart ne fait pas échouer le contrôle, il est porté dans l'état de rapprochement.

## Les onze règles

| Fiche | Règle | Statut | Périmètre | Effet du défaut |
| --- | --- | --- | --- | --- |
| C-01 | Ancrage de l'écriture duale : deux teneurs, un ancrage déclaré par côté (D7) | théorème (PR-31) | noyau | E1 refus |
| C-02 | Deux teneurs distincts | théorème (PR-31, D7) + AX-15 | noyau | E1 refus |
| C-03 | Ligne : contrepartie nommée, typage | définition | noyau | E1 (schéma) |
| C-04 | État de rapprochement, écriture duale | théorème (PR-35) | noyau | — calculé |
| C-05 | Garde : deux silences | théorème, nature **G** | hors noyau | E5 `[AUCUNE LIGNE RÉCIPROQUE]` (D9) |
| C-06 | Existence sans valeur | théorème (PR-35) | hors noyau | — information |
| C-07 | Registre du milieu : déclaration des concernés | théorème (PR-37) + AX-7 | noyau | E6 `[REGISTRE DU MILIEU NON OPPOSABLE]` (D8) |
| C-08 | Maintien structuré | **convention** CONV-11 | noyau | E4 `[MAINTIEN NON STRUCTURÉ]` |
| C-09 | Triplet porteur | définition, sans Lean | noyau | E3 |
| C-10 | Instance de contrôle commune | **convention** CONV-16 + AX-16 | NT-ARCH, hors noyau | E4 `[ÉCART SANS INSTANCE DE CONTRÔLE]` |
| C-11 | Statut de l'écart selon la communication | théorème (PR-40) | hors noyau | — information |

« Noyau » : règle adossée à un théorème de `rules/theoremes.yaml`, ou définition de type de ce noyau. Une règle hors noyau ne produit jamais de refus (garde-fou G6).

## Issue du contrôle formel

L'issue suit l'ordre des effets (Annexe méthodologique §A.15.11) ; le premier rang atteint fixe l'issue.

| Rang | Effets | Issue (`formal_control.issue`) | Décisions humaines admises |
| --- | --- | --- | --- |
| 0 | E1 | `refuse` | `rejetee` seulement |
| 1 | E2, E0 | `en_attente` — défaut de référentiel, ou règle non classée par le set : remontée au porteur. Aucune règle du pilote C n'est en E0 depuis D8–D9 | toutes |
| 2 | E3, E4 | `mal_forme` | toutes ; `validee` garde les marqueurs |
| 3 | E5, E6 | `conforme_marque` | toutes |
| — | aucun | `conforme` | toutes |

Les règles s'évaluent après C-01 : un refus d'ancrage arrête le contrôle.

## Garde-fous (phase 1.3)

`python3 tools/check_rules.py --profreg <ProfReg>` vérifie dix garde-fous (en-tête du script). En particulier : une règle de nature G ou L n'est jamais l'appui seul et ne produit ni refus ni mauvaise formation ; une convention ne s'affiche jamais « démontrée » ; le drapeau `noyau` de chaque théorème est confronté à la forme machine du noyau.

## Hors phase 1

| Objet | Module | Motif |
| --- | --- | --- |
| Raccord registre augmenté ↔ écriture duale | PR-36 (`raccord_augmente_duale`, noyau) | Le schéma ne porte pas encore le livre financier et le registre de communalité d'un même teneur |
| Réalisation du maintien | PR-39 | Suit l'inscription : relève du suivi, non du contrôle d'entrée |
| Arbitrage d'un écart par l'instance | PR-41, PR-43 (`arbitrerInstitue`) | Acte de l'instance de contrôle, postérieur au contrôle formel |
| Constat unilatéral, protocole d'attestation (CONV-17) | PR-44, PR-45 | Hors du pilote |

## Constats faits en préparant la phase 1

- `[INCOHÉRENCE INTER-COUCHES]` NT-ARCH v5.7 §8 annonce « AX-1 à AX-14 » et « CONV-1 à CONV-15 » (« quinze conventions ») ; sa propre table liste CONV-16, et §8.5.0 cite AX-15 et AX-16, qui figurent à l'Annexe méthodologique (§A.15.0, fiches). Non lissé ici ; à corriger dans NT-ARCH.
- Le programme (phase 1, candidat C) comptait CONV-16 et AX-16 parmi les nœuds du noyau. Ils n'y sont pas : CONV-16 est mobilisée par NT-ARCH sans théorème cité (« PR-43, non cité ici ») ; AX-16 n'est pas rattaché. La table les classe donc hors noyau.
- `[DÉCOUPLAGE DE RÉGIMES]` levé le 07/10/2026 (D7 (b)) : PR-31 (`ancreeDuale`), NT-ARCH §8.5.0 et PR-35 / AX-15 admettent tous deux teneurs quelconques, chaque côté ancré. Vérification : `tests/lean/D7_Verification_PR31.lean`.
