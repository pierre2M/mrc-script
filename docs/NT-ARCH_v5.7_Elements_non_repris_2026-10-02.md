# NT-ARCH v5.7 — Éléments non repris dans le noyau démontré

*Complément de `NT-ARCH_v5.7_Noyau_demontre_ProfReg_2026-10-02.md`. Régénéré le 02/10/2026, mis à jour le 03/10 et le 07/10/2026 sur l'**état de référence MRC v5.7** (`MRC_v5.7/_MANIFESTE_v5.7.md` ; la v5.7 reste modifiable sans autre numéro de version) : `MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md` (2 837 lignes ; empreinte courante dans le manifeste) ; ProfReg à l'état local `68080d0` (arbre git `4ef76277`, identique à celui du commit publié ; 533 théorèmes, 0 `sorryAx`, 10 `Classical.choice`, audit du 07/10/2026). Les numéros « L » renvoient aux lignes de ce fichier.*

**Règle d'exclusion.** Est exclu tout ce qui n'est pas soit (a) un théorème ProfReg cité ou décrit par NT-ARCH et présent dans l'état de référence de ProfReg, soit (b) un axiome AX ou une convention CONV que NT-ARCH rattache à un tel théorème. L'exclusion ne juge pas la valeur d'un contenu : elle constate qu'il n'est pas démontré dans ProfReg.

**Contrôle mécanique de l'instantané.** 124 identifiants de NT-ARCH sont des noms de théorèmes de ProfReg. Tous figurent au noyau, sauf deux, cités sans énoncé (section 1). Le noyau compte en outre 16 théorèmes identifiés dans les modules auxquels NT-ARCH attribue un résultat sans les nommer (marqués ⊕), et nomme l'alias `R1_preserved_under_CB1`.

---

## 1. Noms cités dans NT-ARCH qui ne sont pas des théorèmes repris

| Nom | Où | Statut | Raison |
|---|---|---|---|
| `les_deux_registres_augmentes_ont_le_meme_socle`, `lien_inter_acteurs_porte_par_un_registre_augmente` | L3 (note de terminologie) | Théorèmes existants | Cités comme noms Lean, sans énoncé |
| `V10b_seuil_nondeclare_force_deliberation` | §8 L431, §8bis L442 | **Retiré** de ProfReg ; cité comme tel | Converti en CONV-8 |
| `porteurDeLaDeclaration` (PR-18) | §8.4bis L1417, §8.4ter L1438 | Définition | NT-ARCH le déclare lui-même : « c'est la définition, non un théorème » |
| `transition_valide`, `ACT_ARCH_001`, `InventaireNonVide` | §4, §7bis, §5.1 | Définitions | Reprises au vocabulaire du noyau (§0) |
| `Regime.A2` (PR-12), « patron calculé de PR-12 » | §4bis.3 L240 | Constructeur et patron, sans théorème nommé | Le résultat est porté au noyau par PR-26 |

## 2. Résultats présentés comme établis, sans théorème ProfReg

| Énoncé | Où | Statut |
|---|---|---|
| PR-4 « porte » APPEL_IMMANENT_NON_ENTENDU comme projection booléenne, `false` sur INDECIDABLE_ATTESTE (« appui compilé ») | §5.1 L329, F4 L1195 | **Définition** dans `PR4_InventaireTriggerMilieu.lean` ; aucun théorème |
| CB₂ transporte `min` en `max` ; le candidat identité est *lax* monoïdal | §2ter.4, §2ter.5 | Calculs à la main, déclarés non compilés |
| R1 profunctor « commute par excès » (totalité, suffisance, non-saturation) | §2ter.1 L89 | Aucun théorème |
| « Seulement deux » asymétries autorisées | §3bis L170-179 | Déclaré « éprouvé, non démontré » |
| `obligationpreservation_derivable` | §7ter L372 | Preuve hors Mathlib, horizon v6.x (déclaré) |
| Sous-couche M « démontrée complète » : 16 mouvements | §8.3bis L1350, §8.5.5 L1936 | Dénombrement en prose ; aucun ancrage ProfReg |
| Objets catégoriels des fiches : 2-morphismes, bicatégorie des modes, catégorie Exist, horizons H, projection π, 2-cellule | F3 §3.5 (et renvois de F1, F2, F4, F8, §8, §11) | **Hors ProfReg**, déclaré par F3 §3.5 ; seule la forme du signal `carre_non_commutatif` est démontrée (PR-50, au noyau) |
| Modules cités sans énoncé : PR-1, PR-2, PR-6, PR-8, PR-9, PR-14, PR-24, PR-25, PR-38 à PR-49 (hors PR-43 cité comme ancrage de CONV-16) | §8 L427, §8octies-bis L576, F5 L2473, §8.5 L1474 | Théorèmes existants, sans énoncé dans NT-ARCH à condenser |

## 3. Écarts entre NT-ARCH et ProfReg

**Levés** (corrections du porteur du 02/10/2026) : B1 (§2) ; conventions du cas planétaire (§5.2) ; liste des théorèmes rattachés et rubrique « Conventions d'architecture rattachées » (§8) ; PR-22 / patron PR-16 (§8.4ter) ; vulgarisation (§11) ; décomptes ProfReg (seul l'état d'audit courant subsiste) ; AX-7 (axiome de référence `Fiche_Axiome_A7_Seuil_Arrete_Par_Les_Concernes_2026-09-11`) ; fichier unique de référence ; `carre_non_commutatif` (PR-50, F3 §3.3–3.5).

**Levés le 03/10/2026** (dans la v5.7, sans autre numéro de version) : « Programme de preuve : PR-1 → PR-50 » (§8 L427) ; obligation du Consolidé §1.2 (instantané `ProfReg_Lean_2026-10-02_529thm` déposé).

**Restant ouverts dans la v5.7** :

| Écart | Où | Correction proposée |
|---|---|---|
| Annexe G §I.2 et §III.2 citées (§2ter) : sections de l'annexe jonasienne, **hors set** | §2ter L77-137 | Déclarer l'annexe comme source hors set, ou verser les définitions en Couche 0 |
| Le Consolidé §2.2 signale deux réserves de ventilation (8 universels longs non relus ; deux « gardes » sans la formule R-5) | Consolidé §2.2 | Relecture ; décision sur les deux gardes |

## 4. Contenus non repris, partie par partie

**Ensemble du fichier** : note de terminologie « écriture duale » (vocabulaire repris au noyau §0).

**Partie A — Couches 0 et 1**
- §0–§1 : objet, périmètre, table des quatre couches, règle de circulation, renvois.
- §2 : champs `collectifhybridedeclare`, sémantique de la fraction, réfutabilité de B1, renvoi NT-G4.
- §2bis : attribut `charge_valuative`, clause de suspension, orthogonalité, réfutation.
- §2ter.1–5 : R1 profunctor, asymétrie jonasienne de F_y, orientation de la tour V₀–V₂ (réduite au vocabulaire), portée de CB₃, lacune du produit monoïdal de V₂ et proposition P9.
- §3–§3bis : C-STATUT-DETTE (au vocabulaire), R1 constitutive, typage, deux asymétries autorisées, instruction du don, exigence de réfutabilité épistémique.
- §4 : table des quatre flèches et correspondance avec le code (au vocabulaire).
- §4bis : décision « l'obligation s'éteint ; la trace demeure », justification (Yamauchi, Berque), table des exigences par lemme, ternarité S/P/I, homologues mondains, partie procédurale de la règle du seul débiteur, trace, table `C-MEMOIRE-PERTES`, portée et réfutation.
- §5.1–§5.2 : déclencheurs et contenu de l'inventaire, décision sur INDECIDABLE_ATTESTE ; REPRESENTATION-PROSPECTIVE et ses champs (conventions CONV-6, CONV-7 reprises au noyau §12).
- §6 : taxinomie intergénérationnelle.
- §7–§7ter : couplages en prose ; énoncé et contrepartie réfutable d'ACT-ARCH-001 ; §7ter entier.
- §8 : quatre classes de nœuds, alignement des couches, critère de décompte, §8bis–§8octies-bis (formes de sur-revendication, règles R-1 à R-7, deux portes du `Classical.choice`, cribles, motifs transversaux).
- §9, §9bis (T0), §9ter (T1), §10, §11 (vulgarisation).

**Partie B — Couche 2**
- §B.1, §B.2 (invariants 1 et 3, bornage de la source déclarée et vérifiable), §B.2bis (hors théorèmes PR-34).
- Fiches F1, F2 ; F3 hors tables 3.3–3.5 (signal PR-50, statut formel) ; F4 hors conditions PR-31, PR-12, PR-27 ; F5, F6, F7, F9/F10.
- F8 : §8.1–8.3bis, couche R, lignes du registre des régimes, champs de §8.5, §8.5.0–8.5.1ter, la table §8.5.2 elle-même, §8.5.2bis–ter, §8.5.3, partie procédurale de §8.5.3bis, points ouverts de §8.5.4, table §8.5.5, prose et cas de §8.5.6, §8.6–§8.14 en entier.
- §B.4 (vulgarisation).

**Partie C** : système des grammaires, `statut_grammaire`, plafond de 12, matrice (sauf cases VJE et M↔R). **Partie D** : index, règles, traçage, lacunes.

## 5. Nœuds non repris des autres classes

- **Axiomes non rattachés à un théorème repris** : AX-1, AX-5, AX-6, AX-8, AX-10 à AX-14, AX-16 (cité sans théorème), AX-17 (absent de NT-ARCH).
- **Conventions non rattachées** : CONV-4, CONV-5, CONV-17, CONV-18 (absentes de NT-ARCH) ; CONV-13, CONV-15, CONV-16 (citées, sans ancrage démontré).
- **Règles de second ordre** RSO-1 à RSO-8 : classe distincte ; RSO-8 sous-tend `le_silence_ne_solde_rien` et `le_non_declare_ne_qualifie_pas_et_marque`.
- **Sources bibliographiques, décisions du porteur, propositions, arbitrages, cas et obligations ouvertes**, sauf lorsqu'un théorème repris en est l'ancrage.

`[LACUNES ET LIMITES]` Le relevé des sections 1 et 2 est mécanique pour les identifiants (croisement avec les 533 déclarations de l'état de référence) et par mots-clés pour les résultats sans identifiant. L'inventaire de la section 4 est établi au niveau des sections.
