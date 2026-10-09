# mrc-script

Dispositif d'application du **Modèle de Registres de Communalité (MRC) v5.7**, adossé au noyau démontré par ProfReg.

> **Statut.** Prototype en construction (programme de travail : phase 0 achevée ; phase 1 établie sur papier pour le pilote C, le 03/10/2026). **Aucune sortie de ce dépôt n'est opposable.** Il produit au mieux des propositions techniquement formées et des reçus de contrôle ; l'admission, l'opposabilité et toute attribution d'obligation relèvent de la gouvernance du registre concerné.

## Contenu (phase 0)

- `corpus/_MANIFESTE_v5.7.md` — état de référence : empreintes SHA-256 des 17 fichiers du set v5.7 ; commit et tag de ProfReg. La v5.7 n'est pas stabilisée : elle reste modifiable sans autre numéro de version, et le manifeste est régénéré après chaque modification.
- `corpus/_LICENCE_v5.7.md` — licence du texte du set.
- `docs/` — noyau démontré et éléments non repris, régénérés sur l'état de référence.
- `rules/` — forme machine du noyau (théorèmes, conventions, axiomes), générée par `tools/gen_rules.py`.

## Contenu (phase 1 — pilote C : écriture duale entre teneurs)

Porteur du registre pilote : P. M.

- `schema/ecriture_duale.schema.json` — le dossier : deux registres à teneur, leurs lignes, ancrages, registre d'un milieu, désignations de contrôle ; `evidence` et `rule_trace` distincts ; quatre statuts de cycle de vie séparés.
- `rules/pilote_C/` — onze fiches de règle (C-01 à C-11) : statut, nature, périmètre (noyau ou non), appuis Lean, effet du défaut, condition de réfutation, porteur, horizon. Lire `rules/pilote_C/README.md`.
- `tests/ok`, `tests/ko` — seize vecteurs tirés des témoins Lean ; `tests/cycle` — six cas de cycle de vie (validée, retournée, rejetée ; trois combinaisons interdites).
- `tests/lean/PiloteC_Vecteurs.lean` — généré : chaque valeur attendue des vecteurs est prouvée par `decide` contre les définitions de ProfReg.
- `governance/registre_pilote.md` — rôles, statuts, voie de contestation, décisions ouvertes.

Contrôles :
```bash
python3 tools/check_rules.py --profreg <ProfReg>     # garde-fous de la table (1.3)
python3 tools/check_vectors.py                       # schéma, cohérence, génération Lean (1.4)
LEAN_PATH=<oleans ProfReg> lean tests/lean/PiloteC_Vecteurs.lean   # silencieux = valeurs attendues prouvées
```

## Contenu (phase 2 — validateur déterministe)

- `MrcCheck/`, `Main.lean`, `lakefile.lean` — l'exécutable Lean `mrc-check`. Il décode le dossier JSON et évalue les **définitions de ProfReg** (`ancree`, `ancreeDuale`, `etatRapprochement`, `EcritureDuale`, `declarationValide`, `bienForme`, `ecartEnversMilieu`, `instanceCommune`, `ecartQualifie`…) : aucune n'est réécrite. ProfReg est lu dans `profreg/` (lien local vers le dépôt ProfReg, ou copie en CI) ; seuls les modules du pilote sont compilés, sans Mathlib.
- `tools/mrc-check.sh <dossier.json> [reçu.json]` — calcule le contexte de version et produit le reçu.
- `tools/test_recus.py` — vecteurs de la phase 1 contre les reçus, rejeu (même entrée, même version → même sha256), cas de bord.
- `tools/verifier_audit.sh` — seuils figés de l'audit ProfReg (533 théorèmes, 0 `sorryAx`, ≤ 10 `Classical.choice`).
- `.github/workflows/ci.yml` — CI : arbre de ProfReg publié = manifeste ; build complet de ProfReg et audit ; règles, vecteurs, preuves Lean, reçus.

**Le reçu.** Statut parmi six, et seulement six :

| Statut | Quand |
| --- | --- |
| `FORMELLEMENT_BIEN_FORMEE` | aucun effet, ou seulement des marqueurs E5 / E6 |
| `FORMELLEMENT_INCOMPLETE` | effet E3 (délibération) ou E4 (marqueur de mauvaise formation) |
| `CONTROLE_ECHOUE` | effet E1 (refus) |
| `CONTROLE_NON_APPLICABLE` | type de dossier non contrôlé ; effet E2 / E0 (attente) |
| `DONNEE_MANQUANTE` | JSON illisible, champ requis absent ou mal typé |
| `ECART_DE_VERSION` | référence du dossier, ou ProfReg compilé, différents de l'état de référence |

Le reçu porte les effets MRC (règle, code, nature : refus, délibération, marqueur, attente), les calculs, et le contexte : empreinte du set et de NT-ARCH, arbre de ProfReg, sha256 du schéma et de `rules/`, toolchain. **Il ne porte jamais `VALIDE` ni `OPPOSABLE`** : le type des statuts ne les contient pas.

Lancer en local :
```bash
ln -s ~/Developer/ProfReg profreg     # une fois
lake build
tools/mrc-check.sh tests/ok/03_riviere_arretee/dossier.json
python3 tools/test_recus.py
```

## Contenu (phase 3 — agent de proposition sous surveillance)

- `agent/` — l'agent : ne produit que des dossiers `PROPOSEE`, avec provenance complète, signés par sa clé ; aucun accès en écriture au registre (`agent/README.md`).
- `tools/valider.py` — décision humaine et inscription au registre (seul écrivain de `registre/`), signée par la clé du validateur ; `tools/check_registre.py` — invariants du registre (CI).
- `docs/releve_prompts_v55.md` — relevé des écarts des prompts v5.5 du site avec `rules/` : ils ne sont pas réutilisés.
- `banc/` — banc d'essai : corpus (cas historiques à constituer), annotations, tableau de suivi `banc/SUIVI.md` (`tools/banc.py`).
- `tests/agent/test_chaine.py` — essai de bout en bout (8 essais, dont 5 négatifs).

**Validation explicite (09/10/2026).** `tools/fiche.py` (fiche de lecture d'un dossier, sans modèle de langage), `agent/expliquer.py` (agent d'explicitation : questions et réponses journalisées, appréciées), `tools/valider.py` (un avis par écriture, fiche et journal joints à la décision), `tools/reference.py` (champs techniques posés par l'outil). Le banc d'essai mesure la validabilité des écritures, non l'accord avec une annotation (`banc/README.md`).

À venir (phase 4) : publication et canonisation limitée.

## Dépendance

ProfReg — programme de preuve Lean 4 (`github.com/pierre2M/ProfReg`), identifié par son **arbre git** (`corpus/_MANIFESTE_v5.7.md`) ; 533 théorèmes ; licence AGPL-3.0-only.

## Publication

Ce dépôt public ne porte que **l'état courant**, en un seul commit sans historique ; les versions antérieures sont conservées par le porteur, hors ligne. Publication : `tools/publier.sh` ; garde locale contre un push direct : `tools/pre-push`.

## Licence

| Composant | Licence | Texte |
| --- | --- | --- |
| Code et tests (`tools/`, `tests/`, futurs validateur et agent) | AGPL-3.0-only | `LICENSE` |
| `docs/`, `rules/`, `corpus/`, `schema/`, `governance/` (dérivés du texte du set MRC v5.7) | CC BY-NC-SA 4.0 | `LICENSES/CC-BY-NC-SA-4.0.txt` |
| ProfReg (dépendance) | AGPL-3.0-only | dépôt ProfReg |

Raison du choix pour le code : il dérive de ProfReg (AGPL) et exécutera ses vérifications ; l'AGPL garantit que les versions modifiées offertes comme service réseau restent ouvertes. Les fichiers portent un en-tête `SPDX-License-Identifier`.

© 2026 Pierre Musseau-Milesi · La Coop des Communs.
