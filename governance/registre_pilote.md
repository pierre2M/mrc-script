<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->
# Registre pilote — gouvernance (phase 1.5)

*État au 07/10/2026. Pilote C : écriture duale entre teneurs (NT-ARCH v5.7 §8.5.0 ; PR-31, PR-35, PR-37).*

## 1. Rôles

| Rôle | Titulaire | Statut |
| --- | --- | --- |
| **Porteur du registre pilote** | Pierre Musseau-Milesi (P. M.) | **Déclaré** (décision du porteur, 03/10/2026) |
| **Validateur humain** (`lifecycle.human_validation`) | P. M., **seul validateur** | **Déclaré** (décision du porteur D10, 07/10/2026) — voir la règle de validation ci-dessous |
| **Instance de gouvernance** (adopte les règles, décide de toute opposabilité) | Aucune à ce jour | Tant qu'aucune n'existe, `opposability.statut` reste `non_ouverte` pour tout dossier (le schéma l'impose) |
| **Tiers de contestation** | Aucun à ce jour | Voir §3 |

**Règle de validation (D10).** Le MRC n'est validé que par son porteur, **tant qu'une gouvernance alternative ne modifie pas les règles de validation**. Un nouveau validateur n'est institué que pour un **registre de communalité disposant d'une gouvernance associée** : cette gouvernance désigne alors le validateur des dossiers de ce registre, selon ses propres règles, inscrites au journal du registre pilote.

- *Porteur :* P. M. *Horizon :* jusqu'à l'institution d'une gouvernance alternative, ou d'un registre de communalité doté d'une gouvernance associée. *Critère de vérification :* chaque `human_validation` porte `validateur : P. M.`, sauf pour un registre dont la gouvernance associée est inscrite au journal.
- *Contrepartie réfutable :* la règle cesse dès qu'une gouvernance alternative modifie les règles de validation, ou, pour un registre donné, dès qu'une gouvernance associée y est inscrite.
- `[ENGAGEMENT SANS SYMÉTRIE — déclaré, assumé par le porteur]` Le porteur valide des dossiers contrôlés par des règles qu'il a lui-même arrêtées. La règle ci-dessus en fixe la sortie ; elle ne lève pas l'asymétrie tant que la sortie n'est pas atteinte.

## 2. Ce que chaque statut engage

| Statut | Qui le pose | Ce qu'il dit | Ce qu'il ne dit pas |
| --- | --- | --- | --- |
| `proposal` | Le proposant (humain ou agent) | Un dossier est soumis | Rien sur sa forme |
| `formal_control` | L'outil (`mrc-check`, phase 2 ; sur papier en phase 1) | L'issue des règles C-01 à C-11 | Rien sur le fond : une écriture bien formée peut être fausse ou contestée (NT-ARCH §8.5.3bis, patron R0-bis) |
| `human_validation` | Le validateur | `validee` (inscrite, avec ses marqueurs), `retournee`, `rejetee` | La validation n'efface aucun marqueur. Un contrôle `refuse` n'admet que `rejetee` |
| `opposability` | L'instance de gouvernance | Phase pilote : `non_ouverte` | — |

**Critère de la phase 1** (programme, phase 1) : une proposition simulée peut être validée, retournée et rejetée sans ambiguïté de statut. Démonstration sur papier : `tests/cycle/01_validee`, `02_retournee`, `03_rejetee` ; les combinaisons interdites (`04`, `05`, `06`) sont refusées par le schéma.

## 3. Voie de contestation

1. Toute personne peut contester une décision (`validee`, `retournee`, `rejetee`) ou une fiche de règle, en ouvrant une *issue* « Contestation » sur `github.com/pierre2M/mrc-script` (gabarit : `.github/ISSUE_TEMPLATE/contestation.md`).
2. La contestation désigne : le dossier ou la règle visés ; la décision contestée ; le motif ; les pièces. Une contestation d'une règle cite la **condition de réfutation** de la fiche, quand elle existe.
3. Le porteur répond par écrit dans l'*issue*. La réponse est inscrite au journal du registre pilote. `[PLAUSIBLE, NON VÉRIFIÉ — délai à fixer par le porteur : 30 jours proposé]`
4. **Limite déclarée.** Aucun tiers de contestation n'est désigné : le porteur, seul validateur (D10), répond aux contestations portant sur ses propres décisions. La voie existe, elle n'est pas indépendante ; elle le devient pour un registre dont la gouvernance associée institue un tiers. `[RAISONNEMENT AUTORÉFÉRENTIEL — risque déclaré, non levé]`

## 4. Décisions de porteur de la phase 1 (D7–D10 tranchées le 07/10/2026, D6 le 09/10/2026)

| # | Décision | Fiche |
| --- | --- | --- |
| D6 | **Tranchée le 09/10/2026 : accès restreint.** Les pièces du banc d'essai et ses produits (sources de cas, propositions, journaux, réponses brutes, décisions) ne sont pas publiés : le dépôt public n'en donne que les empreintes (`banc/corpus.yaml`) et des comptes (`banc/SUIVI.md`). Ils sont versés dans un **dépôt privé** (`pierre2M/mrc-banc-prive`, historique conservé), constitué par `tools/constituer_prive.py` et ouvert **en lecture seule** à des vérificateurs désignés par le porteur ; les accès sont inscrits dans `ACCES.md` de ce dépôt (qui, quand, pour quels cas, engagement de ne rien recopier). Un vérificateur refait les contrôles avec `tools/verifier_prive.py` (empreintes contre le corpus public, manifeste, signatures des décisions). **Condition proposée, à confirmer :** l'accès à une pièce interne (C2 : LFDE ; C3 : synthèse MEL) n'est ouvert à un tiers qu'avec l'accord écrit de l'organisation qui l'a émise ; à défaut, le vérificateur n'a accès qu'aux autres pièces. **Réfutation :** une empreinte du dépôt privé qui diffère du corpus public, ou une décision qui ne passe pas `check_registre`, est un écart signalé au journal. `[ENGAGEMENT À HORIZON IRRÉVERSIBLE]` : un accès retiré n'efface pas ce qui a été lu ou copié | banc |
| D7 | **Tranchée le 07/10/2026 : (b).** L'ancrage de l'écriture duale est élargi à deux registres tenus par des teneurs identifiés, chaque côté portant son ancrage déclaré ; le registre de communalité est une modalité d'ancrage pour les entités ou concernés sans comptabilité admise. PR-31 corrigé (`CoteDuale`, `ancreeDuale`, quatre théorèmes) ; NT-ARCH §8.5.0 modifié. L'homologie bancaire n'assimile pas l'engagement écologique à une dette financière et ne confère aucun pouvoir d'émission monétaire ; les exigences propres au financement écologique restent distinctes du contrôle d'ancrage | C-01, C-02 |
| D8 | **Tranchée : E6.** Une déclaration des concernés défaillante (non arrêtée, sans concernés, sans critère d'inclusion, sans interprète, écrivant inadmissible, ou échue) rend le registre du milieu non opposable : la qualification « en écriture duale avec le milieu » est refusée ; les lignes restent inscrites, bien formées ; l'écart envers le titulaire est porté dans l'état de rapprochement. Marqueur `[REGISTRE DU MILIEU NON OPPOSABLE]`. Inscrit à l'Annexe méthodologique §A.15.11 | C-07 |
| D9 | **Tranchée : effets déduits du critère §A.15.11, inscrits au set.** C-02 — écriture duale à un seul teneur : **E1** (branche 1, classe « écriture T sans ancrage », PR-31 `un_seul_teneur_pas_de_duale`). C-05 — aucune ligne réciproque : **E5** (branche 5, bien formée et marquée `[AUCUNE LIGNE RÉCIPROQUE]` : deux silences ne sont pas un accord). Conséquence : plus aucune règle du pilote n'est en E0 ; l'issue `en_attente` n'est plus atteinte par le pilote C | C-02, C-05 |
| D10 | **Tranchée.** P. M. seul validateur ; nouveau validateur seulement pour un registre de communalité disposant d'une gouvernance associée ; règle valable tant qu'une gouvernance alternative ne la modifie pas (§1). Pas de tiers de contestation (§3.4) | §1, §3 |

## 5. Agent de proposition et inscription (phase 3)

- Un dossier entre au registre pilote par trois actes distincts : **proposition** (humain, ou agent : `agent/proposer.py`, signée par la clé de l'agent), **contrôle formel** (`mrc-check`, reçu), **décision humaine** (`tools/valider.py`, signée par la clé du validateur). Seul le troisième écrit dans `registre/`.
- Les deux clés sont distinctes et déclarées dans `governance/signataires_autorises` ; une clé partagée, une décision signée par l'agent, une proposition modifiée après signature sont détectées (`tools/check_registre.py`, CI).
- Une décision inscrite n'est pas réécrite : une révision passe par un nouveau dossier.

## 6. Validation explicite (décision du porteur, 09/10/2026)

Valider, c'est se prononcer **en connaissance de cause** sur chaque écriture. Avant de décider, la personne qui valide dispose de la **fiche de lecture** du dossier (rédigée sans modèle de langage) et peut interroger l'**agent d'explicitation** ; elle donne **un avis par écriture** : comprise et validée, précision demandée, refusée. La fiche et le journal des questions sont joints à la décision et signés avec elle. Les champs techniques (empreintes, références) ne lui sont jamais demandés : les outils les posent. L'agent d'explicitation explique ; il ne recommande pas de décision ; ses réponses sont appréciées et conservées.
