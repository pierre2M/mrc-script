<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->
# Agent de proposition (phase 3.1)

L'agent **propose** ; il ne contrôle, ne valide ni n'inscrit rien.

| Garantie | Comment elle est tenue | Vérifiée par |
| --- | --- | --- |
| Statut `PROPOSEE` seulement | le squelette du cycle de vie est imposé après la réponse du modèle (`formal_control`, `human_validation` vides ; opposabilité `non_ouverte`) ; le schéma n'admet que `PROPOSEE` | schéma ; `tools/check_registre.py` (R2) |
| Provenance complète | fournisseur, modèle, sha256 du gabarit, de l'entrée, de la réponse, du schéma et de `rules/`, version de l'agent | schéma (exigée si `origine = agent`) |
| Aucun accès en écriture au registre | l'agent refuse toute sortie dans `registre/` ; il n'importe aucun code du validateur ; seul `tools/valider.py` écrit dans `registre/` | `tests/agent/test_chaine.py` (essai 4) |
| Clés distinctes | l'agent signe dans l'espace de noms `mrc-proposition`, le validateur dans `mrc-validation`, avec deux clés déclarées dans `governance/signataires_autorises` | `check_registre.py` (R1, R3) ; essais 5, 6, 8 |

**Gabarit.** `agent/gabarit_instructions.md`, écrit à partir de `rules/pilote_C` et du schéma ; les prompts v5.5 du site ne sont pas repris (`docs/releve_prompts_v55.md`).

**Fournisseurs.** `anthropic` : API Messages, clé dans `ANTHROPIC_API_KEY`, modèle **obligatoire** (`--modele`, sans valeur par défaut) ; aucune température n'est imposée (paramètre refusé par les modèles récents) : la reproductibilité tient au rejeu, pas à l'appel ; `--enregistrer-reponse` garde la réponse brute pour la rejouer. `rejeu` : réponse enregistrée, rejouable à l'identique.

```bash
# clés (une fois)
ssh-keygen -t ed25519 -f ~/.ssh/mrc_agent -C agent-proposition
# proposer
agent/proposer.py --source <pièce> --fournisseur anthropic --modele <identifiant> \
  --enregistrer-reponse banc/reponses/<cas>.txt --cle ~/.ssh/mrc_agent
# valider (validateur seulement, sa propre clé)
tools/valider.py --proposition propositions/<id>.json --decision validee|retournee|rejetee \
  --motif "…" --cle ~/.ssh/mrc_validateur
```

## Agent d'explicitation (validation explicite)

`agent/expliquer.py` répond aux questions de la personne qui valide, sur un dossier proposé : il s'appuie sur le dossier, sa fiche de lecture (`tools/fiche.py`), le reçu de `mrc-check`, les règles du pilote et les pièces fournies (`--source`), cite ses appuis, signale ce qui relève d'une connaissance générale non vérifiée, et **ne recommande aucune décision**. Chaque échange est ajouté au journal du dossier (`<dossier>.journal.jsonl`) avec la provenance (modèle, sha256 du gabarit, du contexte, de la réponse) ; la personne apprécie chaque réponse (`--apprecier N utile|insuffisante|erronee`). Le journal est joint à la décision (`tools/valider.py --journal`). Il n'écrit nulle part ailleurs.

```bash
agent/expliquer.py --proposition <P.json> --source <source du cas> --fournisseur anthropic --modele <id> \
  --question "Pourquoi cette écriture est-elle une créance et non un actif ?"
agent/expliquer.py --proposition <P.json> --lire
agent/expliquer.py --proposition <P.json> --apprecier 1 utile
```
