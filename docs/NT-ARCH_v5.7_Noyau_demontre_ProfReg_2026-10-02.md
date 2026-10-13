# NT-ARCH v5.7 — Noyau démontré : théorèmes ProfReg, axiomes et conventions associés

*Note condensée dérivée de l'**état de référence MRC v5.7** (`MRC_v5.7/_MANIFESTE_v5.7.md`, qui porte les empreintes courantes ; la v5.7 n'est pas stabilisée et reste modifiable sans autre numéro de version) : `MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md` ; ProfReg à l'état local `fef7593` (arbre git `39285595`, identique à celui du commit publié ; 596 théorèmes, 0 `sorryAx`, 10 `Classical.choice`, audit du 13/10/2026, `audit_2026-10-13_PR58.log` ; noms courts uniques). Régénérée le 02/10/2026 ; régénérée le 12/10/2026 sur le journal à 577 (PR-56, §9octies) ; régénérée le 12/10/2026 sur le journal à 587 (PR-57, §9novies) ; régénérée le 13/10/2026 sur le journal à 596 (PR-58, §9decies) ; régénérée le 12/10/2026 sur le journal à 570 (PR-54, §9sexies ; PR-55, §9septies ; témoin de PR-55 renommé `corpus_signal_temoin_discriminant`, le nom court `signal_temoin_discriminant` étant déjà pris par PR-50) ; régénérée le 12/10/2026 (NT-G9 : CONV-19, CONV-20, PR-52 et trois théorèmes de PR-9 nommés par NT-ARCH, §9quater et §12 ; sur le journal du porteur à 555, `audit_2026-10-12_PR53.log` ; canal G-JUSTICE → G-AFFECTIF, §9quinquies), régénérée le 12/10/2026 sur l'audit à 536 (trois doublons d'énoncé hors noyau retirés de ProfReg ; aucun théorème du noyau touché) ; mise à jour le 07/10/2026 (décision D7, §10.2), le 11/10/2026 (PR-51, carré B1↔B2, §7 et §12 CONV-2), le 11/10/2026 (les seize théorèmes ⊕ désormais nommés par NT-ARCH ; sept d'entre eux en nature L, cités avec leurs témoins ; quatre témoins ajoutés : §5, §10.3bis) le 11/10/2026 (CONV-5 versée à NT-ARCH §8 avec ses deux ancrages PR-10, §8 et §12), le 11/10/2026 (`R1_preserved_under_CB1` nommé par NT-ARCH §2 à côté de son alias `B1_coherence_condition` : plus aucun théorème du noyau n'est hors des noms de NT-ARCH), le 11/10/2026 (témoin d'AX-9, `PR12_ne_qualifie_aucune_dette`) et le 10/10/2026 (versements dans NT-ARCH : nature de l'éponyme de PR-15 en §8 ; §8bis, §9ter, §10.3ter, §10.7, §11 AX-14, §12 CONV-4, CONV-16 à CONV-18). Licence : CC BY-NC-SA 4.0. Forme machine : `~/Developer/mrc-script/rules/`. Complément : `NT-ARCH_v5.7_Elements_non_repris_2026-10-02.md`.*

**Critère d'inclusion.** Un énoncé est repris si et seulement si (i) NT-ARCH l'adosse à ProfReg, par un théorème nommé ou par un résultat attribué à un module PR, et (ii) une déclaration `theorem` de ce nom existe dans `~/Developer/ProfReg` et est importée par `ProfReg.lean`. Ce qui n'est que déclaré (définitions, invariants posés, conventions) n'est repris que pour rendre les énoncés lisibles (§0) ou parce qu'il est rattaché à un théorème repris (§11, §12).

**Base de vérification.** `lake build` du porteur (12/10/2026) et `audit/audit_2026-10-13_PR58.log` : 596 déclarations, 0 `sorryAx`, 10 `Classical.choice`, 0 erreur. Les sources ne contiennent aucune déclaration `axiom`. NT-ARCH v5.7 §8 et §11 portent cet état d'audit. L'audit d'axiomes établit que les preuves sont complètes. Il n'établit pas qu'elles démontrent ce que leurs noms annoncent (NT-ARCH §8).

**Forme des énoncés.** Chaque ligne paraphrase la **signature Lean**. Quand la prose de NT-ARCH dit autre chose, c'est la signature qui est suivie, et l'écart est consigné dans la note complémentaire, section 3.

**Légende.**
- **Ax.** (axiomes Lean dont dépend la preuve) : ∅ aucun · p `propext` · p,Q `+Quot.sound` · p,C,Q `+Classical.choice` (passage par ℝ ou `ENNReal`).
- **Nat.** (nature ; depuis le 11/10/2026, alignée sur le classement du Consolidé §2.2 — A : témoin, délimitation, résultat ou lemme de construction ; L : lecture R-3, lecture de fonction R-7, ou déclaré jamais appui seul ; G : garde R-5 ; T : colonne texte. Onze lectures de PR-3 et PR-17, et celle de `suspension_ne_declenche_aucune_regle` (PR-10), que le Consolidé dénombre sans les nommer, sont attribuées d'après les sources Lean `[INFÉRENCE DÉCLARÉE]`) : A architecture · T porte sur un texte (la table §8.5) · G garde de non-régression (vraie par construction, jamais citée comme appui) · L lecture (dépliage d'une définition ; jamais un appui seul, R-3 et R-7 de §8ter-bis).
- ⊕ : NT-ARCH attribue le résultat au module sans nommer le théorème ; le nom est relevé dans le source Lean. *Depuis le 11/10/2026, aucun théorème ne porte plus ce marqueur : tous sont nommés par NT-ARCH.*
- ↻ : NT-ARCH cite un ancien nom ; c'est le nom en vigueur qui est donné.

---

## 0. Vocabulaire minimal (définitions déclarées, non démontrées)

| Terme | Définition (source Lean / NT-ARCH) |
|---|---|
| `RegimeObligation` | {actoriel, systemique, hybride}. Primitive de Couche 0, constitutive d'un côté d'écriture (CONV-3) |
| `StatutDette` × `NiveauRIA` | {nonAttribuee, enDeliberation, attribuee} × {deliberation, critique} |
| `transition_valide` | `StatutDette → NiveauRIA → Prop` (`Primitives.lean`), soit 6 cas. La transition enDeliberation → attribuee n'existe que dans V4c, qui est procédural |
| `InventaireNonVide` | `{ l : List DID // l ≠ [] }` |
| `SeuilCommunauteMorale` | {sentience, finaliteImmanente, nonDeclare} |
| `ACT_ARCH_001 e d` | Invariant §7bis : pas de statut ATTRIBUEE avec un seuil NONDECLARE, paramétré par l'échéance `e` ∈ {aLAttribution, aDate T, nonNommee} |
| `EtatExtinction` | Second axe (§4bis), orthogonal à `transition_valide` : eteinte (1) · nonEteinte (2) · indecidableAtteste (3) · eteinteEtNonEteinte (4) · nonDeclare (hors tétralemme ; refuse) |
| Typage T | P, C, E, D (signes + / −), e, d (signe neutre °). Arités : intra-écriture, inter-acteurs à deux livres, à trois livres |
| Écriture duale / registre augmenté | « Écriture duale » (N2) désigne la seule écriture miroir entre **deux teneurs** (PR-35) ; l'objet de L2 est le **registre comptable augmenté** : un même fait dans deux registres, sans teneur |
| `BienFormee` (PR-10) | Bonne formation R0-bis d'une mobilisation ; `QuintupletDeclare` désigne son cinquième terme (CONV-9) |
| Changements de base | CB₁ : Bool → [0,1] ; CB₂ = −log : [0,1] → [0,∞]. Orientations : V₁ en `≤`, V₂ en `≥` (§2ter.3) |

---

## 1. Couche 0 — changement de base et fraction actorielle (§2, §2ter)

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| CB₂(1) = 0 et CB₂(0) = ⊤ | `CB2_one`, `CB2_zero` (ChangeOfBase) | p,C,Q | A |
| Sur [0,1], il est faux que min(a,b) ≤ a·b pour tous a, b : le candidat identité n'est pas *oplax* monoïdal | `CB3_candidate_not_oplax_monoidal` (CB3Attempt) | p,C,Q | A · CONV-1 |
| Toute fraction actorielle est de la forme `declaree s v`, donc porte un champ source | `fraction_exhibe_sa_source` (LotL2_PR2_PR14) | ∅ | L · CONV-1 |
| Ce champ peut être vide : `declaree "" v` existe | `fraction_exhibe_une_source_eventuellement_vide` (PR-27) | ∅ | A · borne CONV-1 |

## 2. Couche 1 — R1 et régime systémique (§2, §7)

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Une interaction systémique sans créancier ne satisfait pas R1 standard | `systemique_requires_R1_extension` (P2Synthesis) | p,C,Q | L |
| Si p₁ (à valeurs réelles) est une extension compatible de p₀ (p₁ a b = 1 ⇔ p₀ a b) et si p₀ satisfait R1 (symétrie), alors p₁ a b = 1 → p₁ b a = 1. **L'équivalence « fraction = 1 ⇔ ACTORIEL » est une hypothèse du théorème, pas sa conclusion** | `R1_preserved_under_CB1` (V2Verification) | p,C,Q | A |
| Alias déclaré de la précédente (jamais appui seul) | `B1_coherence_condition` (P2Synthesis) | p,C,Q | L |

## 3. Couche 1 — machine d'états et inventaire (§4, §5.1)

| Énoncé démontré | Théorème (module) | Ax. | Nat. |
|---|---|---|---|
| Depuis nonAttribuee, le seul niveau valide est deliberation | `nonattribuee_force_deliberation` (V4) | ∅ | A |
| Depuis nonAttribuee, critique n'est jamais valide | `cascade_deliberation_before_critique` (V4) | ∅ | L |
| Avec statut_avant = enDeliberation et statut_apres = attribuee : critique est fermé avant, ouvert après, et l'inventaire est non vide. **La transition elle-même est une hypothèse** | `critique_released_by_porteur` (V4) | p | L |
| Un `InventaireNonVide` n'est pas vide | `inventaire_nonempty_required` (V4) | ∅ | L |
| Témoin : le type est habité et la liste vide en est exclue | `inventaire_nonempty_discrimine` (V4) | ∅ | A |
| MILIEU_DEGRADE_PERSISTANT exige l'inventaire sans régime déclencheur ni déclarant | `le_milieu_declenche_sans_qu_aucun_acteur_ait_declare` (PR-4) | p | A |

## 4. Couche 1 — invariant ACT-ARCH-001 (§7bis, §7bis-a) — PR-3

| Énoncé démontré | Théorème | Ax. |
|---|---|---|
| ACT_ARCH_001, statut attribuee et seuil nonDeclare : contradiction | `attribuee_seuil_declare_required` | ∅ (L) |
| Seuil nonDeclare ⇒ statut ≠ attribuee | `seuil_non_declare_interdit_attribution` | ∅ (L) |
| Statut attribuee ⇒ seuil ∈ {sentience, finaliteImmanente} | `attribution_exige_un_seuil_declare` | ∅ (L) |
| Seuil nonDeclare ⇒ critique n'est pas valide. Conséquence : contester le seuil protège de l'attribution | `seuil_non_declare_bloque_critique` | p (L) |
| Avec une mobilisation seuil-valuatif `BienFormee`, l'attribution exige le seuil déclaré **et** un statut du seuil (quadruplet), par composition avec PR-10 | `attribution_exige_seuil_et_quadruplet` | p (L) |
| Le régime strict équivaut au repli dont l'échéance est l'instant d'attribution (les deux sens) | `stricte_est_instance_du_repli`, `repli_a_l_instant_d_attribution_est_strict` | ∅ (L) |
| Sous échéance non nommée, une dette attribuee dont le seuil n'a jamais été déclaré satisfait l'invariant : le repli sans date dégénère | `repli_sans_echeance_degenere` | ∅ (L) |
| Témoin mal formé : dette attribuee déclarée « dans les temps » qui viole l'invariant strict | `PR3_clauseSeuil_temoin_mal_forme` | ∅ |
| Il existe une dette conforme au repli daté et non conforme au strict : PR-3 ne choisit pas le régime | `PR3_ne_choisit_pas_le_regime` | ∅ |
| Les deux seuils déclarés sont admis : PR-3 ne les départage pas | `PR3_ne_departage_pas_les_seuils` | ∅ |

*Nature : L (dépliages d'`ACT_ARCH_001`, R-3) sauf les témoins, marqués A. Module : PR3_AttributionSeuil.*

## 5. Couche 1 — extinction, second axe (§4bis) — PR-26 et PR-11

| Énoncé démontré | Théorème | Ax. | Nat. · rattachement |
|---|---|---|---|
| NONDECLARE est bien formé et ne compte pas comme éteint : le silence ne solde rien | `le_silence_ne_solde_rien` | p | L · RSO-8 (hors note) · témoins : `seul_debiteur_bien_forme_mais_marque`, `deux_regimes_divergents_ne_suffisent_pas` |
| Un lemme 4 portant deux prises renseignées, sans lemme 3 antérieur, est mal formé : la lecture paresseuse est refusée | `deux_regimes_divergents_ne_suffisent_pas` | ∅ | A |
| Un lemme 4 précédé d'un lemme 3 attesté est bien formé (dépendance 4 → 3) | `le_tiers_atteste_leve_le_refus` | ∅ | A |
| Un lemme 3 avec interprète mais sans critère de résolution est mal formé | `tiers_lemme_sans_critere_mal_forme` | ∅ | A |
| Orthogonalité : une obligation non attribuée peut être éteinte, une attribuée non éteinte, et les deux sont bien formées | `l_extinction_ne_depend_pas_de_l_attribution` | ∅ | A |
| nonAttribuee ⇒ critique n'est pas valide, quel que soit l'état d'extinction | `la_machine_d_attribution_ignore_l_extinction` | ∅ | **G** |
| Une extinction bien formée peut être une remise | `une_extinction_bien_formee_peut_etre_une_remise` | ∅ | A |
| Une dette de régime A2 inscrite ETEINTE est mal formée | `une_dette_A2_ne_s_eteint_jamais` | p | A · **AX-2** |
| Une dette A2 au lemme 4 est bien formée (après un lemme 3) | `le_quart_lemme_est_le_regime_de_A2` | ∅ | A · **AX-2** |
| Une extinction déclarée par le seul débiteur est bien formée, marquée, et comptée éteinte | `seul_debiteur_bien_forme_mais_marque` | ∅ | A · AX-7 (appui doctrinal, non garantie) |
| Si les concernés tiennent le miroir, le marqueur est levé | `le_miroir_des_concernes_leve_le_marqueur` | p | L |
| Si un événement fait passer l'obligation à « réalisée », c'est une réalisation vérifiée. Le modèle ignore la remise et la prescription : portée bornée à l'extinction par exécution | `seule_la_realisation_eteint` (PR-11) | p | A |
| Un transfert ne produit aucune obligation : l'obligation n'est pas cessible | `obligation_non_cessible` (PR-11) | ∅ | L · témoin : `PR11_ne_verifie_pas_la_realisation` |
| Une réalisation vérifiée fait passer l'obligation à « réalisée » ; le théorème ne vérifie pas que la réalisation a eu lieu (témoin discriminant de la précédente) | `PR11_ne_verifie_pas_la_realisation` (PR-11) | ∅ | L |

*Module : PR26_ExtinctionSecondAxe, sauf mention PR-11 (PR11_ObligationNonCessible).*

## 6. Couche 1 — représentation prospective planétaire (§5.2, §8bis)

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Sous la règle `ReglePlanetaire`, un contexte planétaire sans porteur n'a qu'un niveau valide : deliberation | `V10a_planetaire_force_deliberation` (V10) | ∅ | A · patron de CONV-8, homologue de CONV-6 |
| Synthèse : tout niveau valide est deliberation, et critique n'est pas valide | `V10a_synthese` (V10) | ∅ | A |

## 7. Couplages inter-couches et inter-grammaires (§7, §B.2, §C.3)

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| V1 (F4 ↔ F6), pour un même acteur : R-HABITABILITE-CAPABILITE = R-PUISSANCEAFFIRMATIVE ⇔ (score de l'appel > 0 ⇔ score de puissance < seuil critique) | `V1_commute_ssi_coherence` (V1) | ∅ | A |
| Lecture de la précédente sur `ActeurF4Coherent` | `V1_commutatif` (V1) | p | L |
| Témoin : sans cohérence, les deux règles divergent | `V1_coherence_discrimine` (V1) | ∅ | A |
| V3 (B1 ↔ B2), régime systémique : le chemin direct aboutit à deliberation | `V3_aboutit_deliberation` (V3) | p | L |
| Régime actoriel : la phase est inchangée par les deux chemins | `V3_actoriel_inchange` (V3) | p | L |
| Chemin direct = chemin via inventaire (vrai par construction, forme 1) | `V3_commutatif` (V3) | p | **L** · CONV-2 étendue |
| Carré B1↔B2, règle des pas déclarée : sous phase d'inventaire requise, le chemin direct n'est pas admissible | `le_chemin_direct_n_est_pas_admissible` (PR-51) | p | L · CONV-2 étendue |
| On n'entre en délibération, sous phase d'inventaire requise, que depuis l'inventaire et sur une écriture clôturable | `entrer_en_deliberation_exige_l_inventaire` (PR-51) | p | L · CONV-2 étendue |
| Sous phase d'inventaire requise, tout chemin admissible qui atteint la délibération passe par l'inventaire, et l'écriture est clôturable (induction sur le chemin) | `aucune_deliberation_sans_inventaire` (PR-51) | p | A · CONV-2 étendue |
| Deux chemins admissibles partis de l'inscription qui atteignent la délibération passent tous deux par l'inventaire, et l'écriture porte un inventaire non vide : la commutation n'est jamais une dispense d'inventaire | `carre_B1B2_commute_sur_les_chemins_admissibles` (PR-51) | p | A · CONV-2 étendue |
| Témoins : la règle trie (chemin par l'inventaire admissible avec inventaire, non sans ; chemin direct exclu sous déclencheur, admis sans) ; l'hypothèse du résultat est satisfiable | `carre_temoin_discriminant`, `le_carre_a_un_chemin_admissible` (PR-51) | p | A · CONV-2 étendue |
| VJE (E ↔ J) : le trajet J→E puis E→J laisse l'état inchangé | `VJE_carre_ne_commute_pas_sans_revision` (VJE) | p | A |
| Le sens J→E ne produit pas la révision | `sensJE_ne_produit_pas_la_revision` (VJE) | ∅ | G |
| Si la révision est donnée en prémisse, la précondition vaut `true` ssi la persistance est épisodique | `VJE_ferme_apres_revision_externe` (VJE) | p | L |
| PR-5 (M ↔ R) : il existe un état où sensRM∘sensMR ≠ sensMR∘sensRM | `le_carre_MR_ne_commute_pas` (PR-5) | p | A |
| Avec la voix de la victime inscrite et la traçabilité de la genèse complète, l'acte `lever` désactive la précaution asymétrique | `le_carre_ferme_apres_l_acte` (PR-5) | p | L |

## 8. Contrôle des énoncés et des champs (§8)

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Il existe une mobilisation seuil-valuatif `BienFormee` sans cinquième terme déclaré | `BienFormee_ne_borne_pas_le_quintuplet` (PR-10) | p | A · motive **CONV-9** |
| Une mobilisation dont la suspension est bien déclarée (statut au régime descriptif-suspendu, marqueur `[VALUATION SUSPENDUE]` levé) ne déclenche aucune règle. `DeclencheRegle` est **défini** comme le régime d'usage normatif : la définition encode CONV-5 | `suspension_ne_declenche_aucune_regle` (PR-10) | ∅ | L · lecture de **CONV-5**, citée avec son témoin |
| Il existe une mobilisation au marqueur `[VALUATION SUSPENDUE]` levé dont la suspension n'est pas bien déclarée (statut absent) | `PR10_suspension_temoin_mal_forme` (PR-10) | ∅ | A · témoin de CONV-5 |
| Pour tout contrôle calculable et toute donnée, il existe deux fiches de même donnée, l'une cohérente, l'autre non : le champ déclaré ajoute un degré de liberté | `le_champ_ajoute_un_degre_de_liberte` (PR-21) | p | A |
| Le désaccord entre champ et contrôle existe dans les deux sens | `les_deux_mensonges_existent` (PR-21) | ∅ | A |
| Une inscription bien formée dont les seuls réfutants admis sont ses porteurs est contradictoire : l'autoréfutation n'est pas une réfutation | `autorefutation_n_est_pas_refutation` (PR-16) | ∅ | L |
| Si les réfutants ne sont pas énumérables, toute liste close en exclut au moins un | `liste_close_exclut_toujours` (PR-16) | ∅ | L |
| Sans porteur nommé de la charge de preuve, aucun renversement n'est déclaré (renommé D-13-4 ; énoncé repris de la source Lean) | `sans_porteur_nomme_pas_de_renversement` (PR-15) | ∅ | L · témoins en §8bis |
| La qualification d'avarie du code coïncide avec la fiche | `PR12_coincide_avec_la_fiche` (PR-27) | ∅ | **G** |
| Pour tout seuil > 0, il existe une série d'écritures toutes triviales sous le seuil dont l'agrégat **par somme** n'est pas conforme. Coûts entiers : le résultat ne porte pas sur V₂ (§2ter.5) | `serie_bien_formee_agregat_non_conforme` (PR-19) | p,Q | A |

## 8bis. Réfutation, charge de la preuve, effet du défaut, inscription de milieu (§8, §8ter-bis, §8octies-bis) — PR-15, PR-16, PR-31, PR-33

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Il existe une obligation d'instruction dont la charge est satisfaite (preuve reconstructible) et le renversement déclaré ; PR-15 ne juge pas la preuve, seulement sa reconstructibilité | `charge_satisfaite_et_renversement_declare_coexistent` (PR-15) | p | A · témoin bien formé de l'éponyme |
| Les trois prédicats de PR-15 discriminent : obligation sans renversement déclaré, sans charge satisfaite, bien formée avec porteur, mal formée | `PR15_discrimine` (PR-15) | p | A |
| Toute inscription bien formée portant une condition de réfutation exhibe un réfutant possible qui n'est pas l'un de ses porteurs | `refutation_exige_un_tiers` (PR-16) | ∅ | L · AX-14 |
| La condition de réfutation d'une inscription bien formée a un lieu de dépôt | `refutation_exige_un_lieu` (PR-16) | ∅ | L · AX-14 |
| La condition de réfutation d'une inscription bien formée inscrit la reprise de l'objection | `refutation_exige_une_reprise` (PR-16) | ∅ | L · AX-14 |
| Témoins : une inscription échoue sur la seule altérité (réfutants admis = porteurs), une sur le seul lieu de dépôt, une sur la seule reprise | `PR16_alterite_temoin_discriminant`, `PR16_moyens_temoin_discriminant`, `PR16_reprise_temoin_discriminant` (PR-16) | ∅ | A · AX-14 |
| Il existe une inscription qui porte une condition de réfutation sans être bien formée au sens de L3 : l'inscription de la condition (PR-8) ne suffit pas | `PR8_ne_suffit_pas` (PR-16) | p | A · borne CONV-7 |
| Une condition de réfutation non restreinte est exerçable par tous : l'ouverture n'exclut personne | `ouverture_n_exclut_personne` (PR-16) | ∅ | L |
| Le marqueur `[INSCRIPTION DE MILIEU SANS INTERPRÈTE]` se lève si et seulement si S et P sont renseignés et I manque | `le_marqueur_de_milieu_se_leve_exactement_sur_l_interprete_manquant` (PR-31) | p | A |
| Témoin : mêmes S et P ; avec I, bien formée ; sans I, mal formée et marquée | `trois_termes_temoin_discriminant` (PR-31) | ∅ | A |
| Il existe une inscription de milieu bien formée dont l'interprète n'est pas le déclarant : le champ I n'est pas redondant par construction | `l_interprete_ne_se_deduit_pas_du_declarant` (PR-31) | ∅ | A |
| Classement de référence de onze règles : CONV-3 → E1, CONV-7 → E4, CONV-8 → E3, CONV-15 → E5, « sans objet » non motivé → E1, régime sans horizon → E1, régime candidat → E4, CONV-20 → E1 (branche 1bis), P5 en principe → E3, P5 exception → E4, clôture non déclarée → E4 | `classement_de_reference` (PR-33) | ∅ | A |
| L'ordre des branches compte : CONV-3 est classé E1 ; privé de sa branche 1, le même défaut serait E3 | `l_ordre_fait_prevaloir_l_objet` (PR-33) | ∅ | A |
| Branche 1bis : CONV-20 est classé E1 ; privé de la branche 1bis (l'inscription est elle-même le dommage), le même défaut serait E4 | `l_inscription_dommageable_est_refusee_avant_tout_marqueur` (PR-33) | ∅ | A · CONV-20 |
| Il existe un défaut portant sur une condition de bonne formation qui n'est pas classé refus | `mal_formee_n_implique_pas_refusee` (PR-33) | ∅ | A |
| Un refus (E1) ne vient que des branches 1 à 3 (1bis comprise) | `les_refus_ne_viennent_que_des_branches_un_a_trois` (PR-33) | ∅ | A |
| Un marqueur d'écriture mal formée (E4) ne vient que de l'appréciation sur une condition de bonne formation, ou du statut candidat à horizon | `le_marqueur_ne_vient_que_de_l_appreciation_ou_du_candidat` (PR-33) | ∅ | A |
| Un défaut qui ne relève d'aucune branche est classé E0 | `sans_branche_pas_de_classement` (PR-33) | p | L |

*PR-33 établit la forme du critère §A.15.11, non sa justesse ni le classement d'une règle réelle (lecture déclarée).*

## 9. Couche 2 transversale — hôte, porteur représentant, répartiteur (§B.2bis ; F4 §4.2bis–4.2ter)

| Énoncé démontré | Théorème (module) | Ax. | Rattachement |
|---|---|---|---|
| INSTRUMENTATION avec un hôte non renseigné ou AUCUN : effet E3 (délibération) | `hote_non_declare_delibere` (PR-34) | p | L |
| Hôte déclaré mais triplet incomplet : un effet est toujours assigné | `la_voie_intermediaire_ne_dispense_pas_du_triplet` (PR-34) | p | L |
| Triplet incomplet déclarant « aucune gouvernance imposée » : effet E4 (marqueur). Si cette déclaration est réfutée, ou si une gouvernance est imposée : E3 | `sans_gouvernance_declaree_le_marqueur_suffit` (PR-34) | p | |
| Témoin : un triplet complet n'a pas d'effet ; un hôte non renseigné a l'effet E3 | `P5_temoin_discriminant` (PR-34) | p | |
| Les effets suivent le classement du critère de l'Annexe §A.15.11 (principe et exception) | `P5_suit_le_critere` (PR-34) | p | |
| Porteur représentant des membres sans dimension de pouvoir : attribution mal formée | `representant_sans_dimension_mal_forme` (PR-31) | p | AX-4 (réfutation) · L |
| Témoin P7 : avec la dimension [AVEC], bien formée ; avec une liste vide, mal formée | `P7_temoin_discriminant` (PR-31) | ∅ | |
| Il existe une attribution bien formée portant [AVEC, SUR] qu'aucune valeur unique ne porte : la lecture exclusive est réfutée | `la_lecture_exclusive_ne_porte_pas_deux_dimensions` (PR-31) | ∅ | |
| Dette de régime A3 dont le mandat du décideur n'est pas borné : le traitement « répartir » ne produit rien | `sans_mandat_borne_aucune_repartition` (PR-12) | p | **AX-3, AX-9** · L |
| Témoin : dettes A2 et A3 à avarie qualifiée et mandat borné — « renouveler » et « répartir » produisent chacun un effet ; PR-12 sépare les régimes sans qualifier les dettes | `PR12_ne_qualifie_aucune_dette` (PR-12) | p | **AX-3, AX-9** |
| Il existe une répartition dont l'avarie est qualifiée et qui reste mal formée | `l_avarie_qualifiee_ne_suffit_pas` (PR-27) | p | **AX-3** |
| Un répartiteur non nommé rend la répartition mal formée | `le_repartiteur_non_nomme_ne_decouple_pas` (PR-27) | p | **AX-3** · L |

*Nature : A sauf mention (L) dans la colonne Ax.*

## 9bis. F3 — signal `carre_non_commutatif` (§B.3, table 3.3–3.4) — PR-50

*Versé le 02/10/2026 (`ProfReg/ProfReg/PR50_CarreNonCommutatif.lean`), audité dans le build du porteur. Forme du signal seulement : SVD, FCA pondérée, 2-morphismes et 2-cellule restent hors ProfReg (NT-ARCH F3 §3.5).*

| Énoncé démontré | Théorème | Ax. |
|---|---|---|
| Un signal levé atteste une non-commutation en ce point | `signal_implique_non_commutation` | p |
| Un carré qui commute ne signale jamais | `commutatif_ne_signale_pas` | p |
| Sans seuil déclaré : pas de signal, marqueur levé | `seuil_non_declare_ne_signale_pas` | ∅ (L) |
| Le signal n'est pas la non-commutativité : sous le seuil, un carré qui ne commute pas ne signale rien | `non_commutation_sous_le_seuil_ne_signale_pas` | p |
| Même carré, même écart : le verdict dépend du seuil déclaré | `signal_temoin_discriminant` | p |
| Même carré, même seuil : le verdict dépend de l'écart déclaré | `le_signal_depend_de_l_ecart_declare` | p |
| L'action REVISION_CONCEPTUELLE suit le signal | `action_temoin_discriminant` | p |

## 9ter. F6 — régime du dispositif (F6.2) — PR-17

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Un critère d'accès aux droits bien formé conclut que le dispositif est en régime `infrastructure` | `regime_du_dispositif_declare` (PR-17) | p | L |
| Un dispositif dont le régime n'est pas déclaré ne supporte pas le critère : le silence ne vaut pas permission | `nonDeclare_ne_vaut_pas_permission` (PR-17) | p | L · CONV-8 (moitié négative, patron) |

## 9quater. F1 et F5 — régime affectif (C-GENRE-METIER) et couplage G-EVOLUTIVITE ↔ G-AFFECTIF — PR-52, PR-9

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Une qualification du régime affectif sans source déclarée n'est pas légitime | `sans_source_rien_n_est_legitime` (PR-52) | ∅ | L · **CONV-20** ; témoin `inscriptible_temoin_discriminant` |
| Il existe une qualification de source déclarée qui n'est pas légitime (sans consentement collectif) : la source est nécessaire, non suffisante | `la_source_ne_suffit_pas` (PR-52) | p | A · CONV-20 |
| Une qualification au statut `NONCOLLECTE` n'est jamais légitime | `noncollecte_n_est_jamais_legitime` (PR-52) | ∅ | L · CONV-20 ; témoin `inscriptible_temoin_discriminant` |
| Sur support distribué, aucune qualification n'est inscriptible : la règle du support exige `NONCOLLECTE`, la règle d'inscription l'exclut | `sur_support_distribue_rien_n_est_inscriptible` (PR-52) | ∅ | A · CONV-20 |
| Il existe une qualification inscriptible et une qui ne l'est pas | `inscriptible_temoin_discriminant` (PR-52) | p | A · témoin |
| Des appuis qui ne sont que des signaux de souffrance ne qualifient aucune créance (`QualifieCreance` encode CONV-19) | `la_souffrance_seule_ne_qualifie_aucune_creance` (PR-52) | ∅ | L · **CONV-19** ; témoin `la_souffrance_n_empeche_pas_la_qualification` |
| Un signal de souffrance joint à un appui de G-JUSTICE n'empêche pas la qualification | `la_souffrance_n_empeche_pas_la_qualification` (PR-52) | p | A · témoin de CONV-19 |
| Il existe un canal et un état sur lesquels les deux ordres de propagation entre G-EVOLUTIVITE et G-AFFECTIF diffèrent : le couplage est un cycle non commutatif | `les_deux_ordres_different` (PR-9) | p | A |
| Un canal qui ne relit pas le seuil qu'il écrit termine | `un_canal_qui_ne_relit_pas_le_seuil_termine` (PR-9) | ∅ | L · témoin `un_canal_qui_relit_le_seuil_ne_termine_pas` |
| Un canal qui relit le seuil qu'il écrit ne termine pas | `un_canal_qui_relit_le_seuil_ne_termine_pas` (PR-9) | p | A · témoin |

*PR-52 établit la forme des deux règles de NT-G9 §10.1 et de la non-confusion de §4.2, non leur justesse. PR-9 nomme « E→A » le canal que NT-G9 appelle A→E (correspondance déclarée en NT-G9 §10.2).*

## 9quinquies. F6 → F1 — canal G-JUSTICE → G-AFFECTIF — PR-53

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Une injustice de type admis, documentée par un documentant désigné et indépendamment de la souffrance, qui ne passe pas, est déclarée locale et épisodique : le filtre n'écarte que le déclaré incident | `le_filtre_n_ecarte_que_le_declare_incident` (PR-53) | p | A |
| Une injustice testimoniale locale mais structurelle passe | `local_mais_structurel_passe` (PR-53) | ∅ | A |
| Une injustice herméneutique dont la portée et la persistance ne sont pas déclarées passe, marquée `[PORTÉE NON DÉCLARÉE]` | `non_declare_passe_avec_marqueur` (PR-53) | ∅ | A |
| Une injustice dont la seule documentation est la souffrance ne passe pas | `documentee_par_la_souffrance_ne_passe_pas` (PR-53) | p | A · CONV-19 |
| La même injustice locale passe si elle est structurelle, non si elle est épisodique | `filtre_temoin_discriminant` (PR-53) | ∅ | A · témoin |
| Une qualification dont la seule source serait l'hypothèse venue de F6 n'est pas légitime | `l_hypothese_seule_ne_qualifie_pas_le_regime` (PR-53) | ∅ | A · CONV-20 |
| Un second passage A→J→A ne change rien : le cycle termine | `le_cycle_AJ_termine` (PR-53) | p | A |
| Sans documentant, une souffrance déclarée ne fait passer aucune hypothèse | `la_souffrance_ne_se_confirme_pas_elle_meme` (PR-53) | p | A · CONV-19 |
| Le déni du réel déclaré et le déni présumé ne se recouvrent pas | `declare_et_presume_s_excluent` (PR-53) | p | A |
| Il existe un déni présumé sans atteinte déclarée (seule l'hypothèse herméneutique pendante), et sans signal il n'y en a pas | `deni_presume_temoin` (PR-53) | ∅ | A · témoin |
| Règle d'ordre : la qualification inscrite sans examen est E4 ; mobilisée dans une décision, E3 | `ordre_non_respecte_deux_effets` (PR-53) | ∅ | A |

*PR-53 établit la forme du canal et de la règle d'ordre, non leur justesse.*

## 9sexies. F3 — `boucle_confirmante_detectee` et contre-performativité (table 3.3–3.5 ; §B.2bis.6) — PR-54

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Un signal de boucle confirmante atteste une boucle et un effet aligné sur l'intention | `boucle_confirmante_atteste_l_alignement` (PR-54) | p | L · témoin `boucle_temoin_discriminant` |
| Une boucle contre-performative (effet contraire à l'intention) ne lève jamais le signal de boucle | `la_contre_performativite_ne_leve_pas_la_boucle` (PR-54) | p | A |
| La même écriture, à l'alignement près, lève ou non le signal | `boucle_temoin_discriminant` (PR-54) | ∅ | A · témoin |
| Il existe une écriture contre-performative, logée dans un hôte, sous `INSTRUMENTATION` sans hôte renseigné, dont le défaut P5 se lève | `l_effet_d_hote_voit_un_cas_contraire` (PR-54) | p | A · PR-34 |
| Si l'écriture ne déclare ni `INSTRUMENTATION` ni hôte, une boucle contre-performative n'est vue par aucun signal | `hors_hote_la_contre_performativite_est_invisible` (PR-54) | p | A |
| Il existe un désalignement sans hôte qui reste invisible | `desalignement_sans_hote_temoin` (PR-54) | p | A · témoin |
| Ce que le registre voit ne dépend pas de l'existence réelle d'un hôte | `le_registre_ne_lit_pas_l_hote_reel` (PR-54) | p | L · témoin `un_hote_reel_declare_aucun_echappe` |
| Il existe un hôte réel, déclaré `AUCUN` sous une opération déclarée `AUCUNE`, qui échappe à tout signal | `un_hote_reel_declare_aucun_echappe` (PR-54) | p | A · témoin |

*PR-54 établit la forme du signal et de sa lacune, non la fréquence des cas ; la boucle est réduite à un booléen.*

## 9septies. F3 → F6, F10 — CORPUS\_NON\_CONSENTI : signal, blocage, sortie (table 3.3–3.4) — PR-55

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Le signal se lève si et seulement si le corpus n'est pas consenti et que le mode de validation est EXPERTAL | `corpus_non_consenti_lit_le_mode_de_validation` (PR-55) | p | L · témoin `corpus_signal_temoin_discriminant` |
| Le même corpus non consenti signale sous validation experte, non sous validation majoritaire | `corpus_signal_temoin_discriminant` (PR-55) | ∅ | A · témoin |
| Un acteur joignable qui n'a pas consenti n'est couvert par aucune représentation | `la_representation_ne_couvre_pas_un_joignable` (PR-55) | p | A |
| Si chaque acteur a consenti ou est absent, désigner un porteur et un mécanisme pour les absents lève le blocage | `l_absence_n_est_jamais_un_verrou` (PR-55) | p,Q | A |
| Un corpus concernant un joignable consentant et un absent représenté est levé ; ni le consentement seul ni la représentation seule ne couvrent les deux | `les_deux_cles_sont_necessaires` (PR-55) | ∅ | A · témoin |
| Un changement du mode de validation ne change pas le blocage | `le_changement_de_mode_ne_leve_pas` (PR-55) | ∅ | L · témoin `bloque_temoin_discriminant` |
| Le même absent, sans porteur, bloque ; avec porteur et mécanisme, ne bloque plus | `bloque_temoin_discriminant` (PR-55) | ∅ | A · témoin |

*PR-55 établit la forme du signal et de sa sortie, non la justesse des déclarations d'absence.*

## 9octies. F3 — consentement par personne et absence opposable (C-INSCRIPTION-CORPUS ; table 3.3–3.4) — PR-56

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Le consentement du corpus est vrai si et seulement si chaque personne du périmètre a consenti | `le_consentement_du_corpus_est_derive` (PR-56) | p,Q | L · témoin `consentement_derive_temoin` |
| Un seul consentement manquant rend faux le consentement du corpus | `consentement_derive_temoin` (PR-56) | ∅ | A · témoin |
| Une personne déclarée en recherche infructueuse, sans trace ni attestation, n'est pas représentée, quels que soient porteur et mécanisme | `sans_trace_ni_attestation_pas_d_absence` (PR-56) | p | A |
| Une contestation retenue par l'instance fait tomber la représentation, même avec trace et attestation | `une_contestation_retenue_fait_tomber_la_representation` (PR-56) | p | A |
| La trace seule, ou l'attestation seule, suffit ; ni l'une ni l'autre, non | `trace_ou_attestation_temoin` (PR-56) | ∅ | A · témoin |
| Toute représentation admise par PR-56 l'est par PR-55 | `pr56_restreint_pr55` (PR-56) | p | A |
| Si chaque personne a consenti ou est absente à titre admis, désigner porteur et mécanisme pour les absents lève le blocage | `l_absence_opposable_n_est_jamais_un_verrou` (PR-56) | p,Q | A |

*PR-56 établit la forme du consentement par personne et de l'absence opposable ; il ne dit pas qu'une trace est sincère, seulement qu'elle existe et qu'elle est contestable.*

## 9novies. §B.2ter — phase RECHERCHE\_INTERVENTION, constat d'effet et contre-performativité attestée — PR-57

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Un constat NON INSTRUIT n'atteste pas l'alignement, ne lève pas le signal et ne relance pas l'enquête | `non_instruit_ne_vaut_pas_aligne` (PR-57) | p | A |
| Un constat attesté par le porteur de l'instrument n'est pas recevable | `le_porteur_ne_s_atteste_pas` (PR-57) | p,Q | A |
| Un constat d'une instance qui n'associe pas les personnes concernées n'est pas recevable | `sans_les_concernes_pas_de_constat` (PR-57) | p | A |
| Un constat dont l'hypothèse est déclarée après lui, ou jamais, n'est pas recevable | `hypothese_apres_coup_non_admise` (PR-57) | p,Q | A |
| Le même constat CONTRAIRE lève le signal s'il est attesté par un tiers associant les concernés, non s'il l'est par le porteur | `constat_temoin_discriminant` (PR-57) | ∅ | A · témoin |
| Un constat À QUALIFIER recevable relance l'enquête sans lever le signal | `a_qualifier_relance_sans_signal` (PR-57) | p | A |
| Le nombre de relances ne dépasse pas le nombre de constats | `pas_de_relance_sans_constat` (PR-57) | p | A |
| Une écriture contre-performative hors effet d'hôte, invisible aux signaux (PR-54), devient visible dès qu'un constat CONTRAIRE recevable existe | `l_enquete_rend_visible_la_contre_performativite` (PR-57) | p | A · PR-54 |
| Sans constat, ce que voit le registre est inchangé | `sans_constat_la_lacune_demeure` (PR-57) | p | L · témoin `constat_temoin_discriminant` |
| Une échéance sans les personnes concernées n'ouvre pas la phase ; les quatre autres déclencheurs l'ouvrent | `echeance_sans_concernes_n_ouvre_pas` (PR-57) | p | A |

*PR-57 établit la forme du constat et de son effet, non la justesse d'un constat ni la qualité de l'enquête (NT-G10).*

## 9decies. §8.5.6.4 — un commun suppose ses instances (C-DROITS, F6) — PR-58

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Une chose inscrite comme commun porte l'un des trois patrons de communalité | `le_typage_est_necessaire` (PR-58) | p | A |
| Une propriété collective avec utilités distribuées mais sans instance délibérative ni de contrôle n'est pas inscrite comme commun | `une_indivision_n_est_pas_un_commun` (PR-58) | p | A |
| Sans instance délibérative déclarée, aucune chose n'est inscrite comme commun | `sans_instance_deliberative_pas_de_commun` (PR-58) | p | A |
| Sans instance de contrôle déclarée, aucune chose n'est inscrite comme commun | `sans_instance_de_controle_pas_de_commun` (PR-58) | p | A |
| Une forme admise (ORE) qui satisfait la condition T sans instance délibérative n'est pas inscrite comme commun | `une_forme_admise_sans_deliberation_n_est_pas_un_commun` (PR-58) | p | A |
| Une chose typée `P+` seul n'est jamais inscrite comme commun, quelles que soient ses instances | `la_propriete_seule_n_est_jamais_un_commun` (PR-58) | p | A |
| Une chose d'intérêt diffus sans attributaire identifié est inscrite comme commun si ses instances délibérative et de contrôle sont tenues | `l_interet_diffus_se_passe_d_attributaire` (PR-58) | p | A |
| La même propriété collective est un commun avec ses trois instances, non sans instance de contrôle | `commun_temoin_discriminant` (PR-58) | p | A · témoin |

*PR-58 établit la forme de la règle, jamais qu'une chose est un commun. Son neuvième théorème (`l_interet_commun_ne_determine_pas_l_inclusivite`) porte sur NT-G6 et n'est pas cité par NT-ARCH : il est hors du périmètre de cette note.*

## 10. F8 — mode comptable

**10.1 Régimes déclarés (§8.4bis, §8.4ter) — PR-22, PR-32**

| Énoncé démontré | Théorème | Ax. | Rattachement |
|---|---|---|---|
| Instance du sol : une même chose, deux natures, deux régimes, deux porteurs | `une_chose_deux_natures` (PR-22) | ∅ | patron de CONV-12 (§8octies) |
| Population non énumérable : une énumération close de régimes exclut un collectif | `enumeration_close_exclut_un_collectif` (PR-22) | ∅ | L |
| Instance sur `Nat` : une liste close exclut quelqu'un (ex-`la_decision_1_exige_l_ouverture`) | `une_liste_close_de_collectifs_Nat_exclut_quelqu_un` (PR-22) ↻ | p,Q | |
| Garde : le régime foncier reste porté par le normalisateur IFRS | `PR22_ne_supprime_pas_les_regimes_etablis` (PR-22) | ∅ | |
| Garde : les natures et les noms de régimes diffèrent ; aucun n'est départagé | `PR22_ne_departage_pas_les_regimes` (PR-22) | ∅ | |
| Un régime sans condition de réfutation n'est pas admis et n'autorise aucune écriture | `regime_sans_refutation_n_autorise_aucune_ecriture` (PR-32) | p | **CONV-7** · L |
| Collectif et date présents, sans réfutation : CANDIDAT_NON_INSTANCIABLE ⇔ critère de sortie ∧ caducité | `candidat_ssi_critere_de_sortie_et_caducite` (PR-32) | p | **CONV-7** |
| Témoins : admis, candidat, non inscrit | `regime_temoin_discriminant` (PR-32) | ∅ | |

**10.2 Ancrage de la sous-couche T (§8.5) — PR-31 ; écriture duale élargie à deux teneurs quelconques (décision D7, 07/10/2026)**

| Énoncé démontré | Théorème | Ax. |
|---|---|---|
| Une écriture T sans traduction ni inscription de communalité n'est pas ancrée : elle est refusée | `sans_ancrage_refusee` | p (L) |
| Un registre de communalité suffit comme ancrage | `le_registre_de_communalite_suffit` | ∅ |
| Un seul ancrage suffit à un côté ; il ne suffit pas à une écriture duale dont l'autre côté n'est pas ancré (un ancrage par côté ; restaté sur `ancreeDuale`, D7 du 07/10/2026) | `la_duale_exige_un_ancrage_par_cote` | ∅ |
| Une écriture duale est ancrée si et seulement si ses deux teneurs sont distincts et chaque côté porte un ancrage déclaré (lecture de `ancreeDuale`, discriminée par les trois suivants) | `ancree_duale_ssi` | ∅ (L) |
| Deux comptabilités tenues ancrent une écriture duale (couple banque / emprunteur de PR-35) | `deux_comptabilites_tenues_ancrent_une_duale` | ∅ |
| Le registre de communalité ancre un côté, face à une comptabilité tenue comme face à un autre registre de communalité | `le_registre_de_communalite_ancre_un_cote` | ∅ |
| Un seul teneur ne fait pas d'écriture duale, même ancré des deux côtés | `un_seul_teneur_pas_de_duale` | ∅ |

**10.3 Registre comptable augmenté (L2) et lien inter-acteurs (§8.5.3bis, §8.5.4, §8septies) — CONV-10**

| Énoncé démontré | Théorème | Ax. |
|---|---|---|
| Dans un registre comptable augmenté : `pFin a b = plein` ⇔ `pCom a b = plein` | `registre_augmente_coherent` ↻ (ex-`ecriture_duale_coherente`, LotL2_PR2_PR14) | ∅ |
| Il existe une instance où un lien du socle est plein des deux côtés et où un lien hors socle ne l'est d'aucun | `registre_augmente_non_equivalence` ↻ (ex-`ecriture_duale_non_equivalence`) | p |
| Il existe deux registres augmentés, chacun cohérent, qui diffèrent sur un couple. Le témoin a un socle vide : il n'y a pas d'accord sur la valeur parce qu'il n'y a pas de lien | `accord_sur_l_existence_pas_sur_la_valeur` (PR-20) | p |

**10.3bis Écriture duale entre teneurs (N2), raccord, registre d'un milieu (§8.5, terminologie « écriture duale ») — PR-35, PR-36, PR-37**

| Énoncé démontré | Théorème (module) | Ax. | Rattachement |
|---|---|---|---|
| La relation d'écriture duale entre deux registres à teneur est symétrique | `ecriture_duale_symetrique` (PR-35) | ∅ | **AX-15** · L (déclarée, jamais appui seul) |
| Témoin : le prêt bancaire est en écriture duale ; après un remboursement inscrit par la banque seule, il ne l'est plus | `ecriture_duale_temoin_discriminant` (PR-35) | ∅ | **AX-15** |
| L'état de rapprochement nomme l'écart (ici, la ligne C⁻ de 100 manquante) | `l_etat_de_rapprochement_nomme_l_ecart` (PR-35) | ∅ | **AX-15** |
| Registre augmenté tenu et cohérent, en écriture duale avec un registre B : toute ligne financière dont la contrepartie est le teneur de B entraîne une ligne de communalité vers B et, chez B, une ligne miroir vers A de rôle opposé. Double tenue et écriture duale se composent | `raccord_augmente_duale` (PR-36) | p,Q | |
| Un registre de milieu bien formé n'est pas écrit par le milieu : l'écrivant diffère du titulaire | `le_milieu_n_ecrit_pas_son_registre` (PR-37) | p | L |
| Une déclaration seulement ratifiée (non arrêtée par les concernés) ne fonde pas un registre opposable | `la_ratification_ne_fonde_pas_le_registre` (PR-37) | p | **AX-7** · L |
| Sans maintien, le registre du milieu n'a pas d'appui ; un maintien porté par un autre registre que celui du titulaire non plus | `sans_maintien_pas_d_appui`, `maintien_d_un_autre_registre_pas_d_appui` (PR-37) | p | **CONV-11** · L |
| Témoin : déclaration arrêtée, registre de milieu bien formé, écriture duale avec l'entreprise, écart vide | `ecriture_duale_avec_un_milieu` (PR-37) | ∅ | **AX-7** |
| Témoin : déclaration arrêtée, l'écart est vide ; ratifiée, il reste | `registre_de_milieu_temoin_discriminant` (PR-37) | ∅ | **AX-7** |
| Témoin : si le maintien nomme un autre registre que celui du titulaire, l'écart revient | `registre_mal_nomme_l_ecart_revient` (PR-37) | ∅ | **CONV-11** |

**10.3ter Ancrages de conventions (§8, rubrique « Conventions d'architecture rattachées ») — PR-28.** *Ils établissent la forme de l'obligation conventionnelle, non sa justesse.*

| Énoncé démontré | Théorème | Ax. | Convention |
|---|---|---|---|
| Sous la règle déclarée, un seuil `NONDECLARE` ne rend accessible que la délibération | `nondeclare_force_deliberation` | ∅ | **CONV-8** |
| Il existe une écriture bien formée (PR-8), engageant au-delà de l'exercice, qui ne satisfait pas CONV-6 : le trou | `BienFormee_ne_borne_pas_la_prospective` | ∅ | **CONV-6** |
| CONV-6 est satisfiable | `CONV6_est_satisfiable` | ∅ | **CONV-6** |
| Deux profils peuvent être ordonnés en sens inverse sur un axe et sur le score composite | `la_comparaison_sur_un_axe_n_est_pas_le_classement` | ∅ | **CONV-14** |
| Témoins : la règle de CONV-8 exclut un contexte (seuil NONDECLARE, statut attribuée) ; un seuil déclaré laisse le niveau critique accessible | `CONV8_temoin_discriminant` | ∅ | **CONV-8** |
| Une écriture à horizon institutionnel satisfait toujours CONV-6 : garde de portée (témoin : `BienFormee_ne_borne_pas_la_prospective`) | `CONV6_ne_vaut_pas_dans_l_exercice` | ∅ | **CONV-6** · L |
| Il existe une source déclarée qui satisfait CONV-4 sans être un DID | `CONV4_satisfaite_sans_DID` | ∅ | **CONV-4** |
| Il existe une source dont désignation, résolution et intégrité sont renseignées et qui ne satisfait pas CONV-4 : la clause du porteur mord | `source_sans_porteur_mal_formee` | ∅ | **CONV-4** |
| Pour toute forme de désignation, il existe une source qui satisfait CONV-4 sous cette forme | `CONV4_ne_prescrit_aucune_forme` | ∅ | **CONV-4** |

**10.4 Mouvement de maintien (§8.5.3bis) — PR-23 ; motive et borne CONV-11 sans la démontrer**

| Énoncé démontré | Théorème | Ax. |
|---|---|---|
| Il existe une écriture `e` bien formée au sens actuel qui ne satisfait pas CONV-11 | `BienFormee_ne_borne_pas_le_maintien` | ∅ |
| Sans maintien inscrit, deux situations d'écarts différents donnent la même écriture | `deux_dettes_distinctes_meme_ecriture` | ∅ |
| Sans maintien inscrit, R-PRIORITE-CREANCIERS ne rend aucun verdict | `priorite_sans_assiette` | ∅ (L) |
| Pour tout registre, une écriture satisfait CONV-11 avec un maintien porté par ce registre : le registre financier n'est pas requis | `CONV11_satisfaite_sans_registre_financier` | ∅ |
| Deux écritures conformes à CONV-11, nommant deux registres différents, ont le même écart lisible : PR-23 ne certifie pas le nommage | `PR23_ne_certifie_pas_le_nommage` | ∅ |

**10.5 Table des miroirs §8.5.2 — Sonde P-C-E-D-e-d et PR-29**

*Nature T sauf mention. Antériorité : la sonde type deux lectures retirées depuis de la couche T (`P⁺+C⁺`, `e°+D⁻`). Ses énoncés restent exacts, mais ils ne certifient aucun typage en vigueur.*

| Énoncé démontré | Théorème (module) | Ax. |
|---|---|---|
| Le typage à six primitives se formalise : C⁺→D⁺ et E⁺→∅ sont admis | `la_sonde_ne_condamne_pas_le_typage` (Sonde) | p |
| Table du 08/09 : aucun typage simple autre que E⁺ n'admet le vide | `seul_E_plus_admet_le_vide` (Sonde) | p |
| Table du 18/09 : E⁺ admet le vide, les neuf autres (E⁻ compris) ne l'admettent pas | `seul_E_plus_admet_le_vide_table_1809` (Sonde) | p |
| E ≠ D ; E⁺→∅ est admis, D⁺→∅ ne l'est pas : un engagement sans miroir n'est pas une dette sans créancier | `engagement_sans_miroir_n_est_pas_dette_sans_creancier` (Sonde) | p |
| C⁺/D⁺ sont réciproques, alors que P⁺→e° est admis et e°→P⁺ ne l'est pas : la table mêle deux relations | `la_table_melange_deux_relations` (Sonde) | p |
| P⁻→C⁺ est admis, C⁺→P⁻ ne l'est pas | `second_couple_asymetrique` (Sonde) | p |
| Ces résultats tiennent sur la table du 18/09 | `les_resultats_de_la_sonde_tiennent_table_1809` (Sonde) | p |
| Un `respect_R1` déclaré peut contredire le contrôle, dans un sens comme dans l'autre | `respect_R1_declare_peut_mentir`, `respect_R1_declare_peut_se_sous_estimer` (Sonde) | p |
| Il existe un typage de longueur 2 qui n'est pas simple : le miroir n'est pas défini sur les composites | `miroir_non_defini_sur_les_composites` (Sonde) | ∅ |
| P⁻→∅ est une violation ; C⁻→E⁻ est une lacune, puisque E⁻ n'est pas dans le miroir de C⁻ (A) | `absent_n_implique_pas_violation` (PR-29) | p |
| Un même couple peut avoir deux statuts : le statut ne se lit pas sur la table (A) | `le_statut_ne_se_lit_pas_sur_la_table` (PR-29) | p |
| Une écriture à trois livres sans tiers est mal formée (L, lecture de fonction R-7) | `trois_livres_sans_tiers_mal_formee` (PR-29) | p (L) |
| Témoin trois livres : avec tiers, bien formée ; sans tiers, mal formée (A) | `trois_livres_temoin_discriminant` (PR-29) | ∅ |
| Une écriture bien formée à deux livres, relue à trois, ne l'est plus (A) | `la_troisieme_arite_n_est_pas_la_deuxieme` (PR-29) | ∅ |
| Colonne d'origine : 15 branches inter-acteurs ou mixtes, dont 8 échouent au contrôle (liste nommée) | `la_colonne_d_origine_ne_satisfait_pas_B7` (PR-29) | p |
| 10 échecs en lecture littérale du « + », 8 en lecture composite | `le_decompte_depend_de_la_lecture_du_plus` (PR-29) | p |
| Le dédoublement de la colonne ne perd aucune contrepartie | `le_dedoublement_conserve_la_contrepartie` (PR-29) | ∅ |
| La transcription compte 27 branches, fidèles à la table | `branches_fideles_a_la_table` (PR-29) | p |
| Restent 4 lacunes : E⁺→D⁺, E⁺→C⁺, E⁻→C⁻, d→C⁻ | `sous_la_colonne_dedoublee_restent_quatre_lacunes` (PR-29) | p |

**10.6 Inscription d'une chose comme commun (§8.5.6) — PR-30. La forme des règles est démontrée, non leur justesse**

| Énoncé démontré | Théorème | Ax. | Rattachement |
|---|---|---|---|
| La condition du 21/09 laissait passer le capital d'apporteur ; la branche B (répartissable = VRAI) l'exclut | `la_branche_B_exclut_le_capital_d_apporteur` | ∅ | |
| Répartissabilité NON_DETERMINABLE : le résultat est INDETERMINE | `non_determinable_rend_indetermine` | p | L |
| Répartissabilité NONDECLARE : l'engagement ne qualifie pas et l'écriture est marquée | `le_non_declare_ne_qualifie_pas_et_marque` | p | **CONV-9** (patron) · L |
| Témoins : l'asymétrie existentielle qualifie sans marqueur ; FAUX qualifie | `qualifiant_temoin_discriminant` | ∅ | |
| Règle A : une seule classe non répartissable suffit | `une_classe_non_repartissable_suffit` | p,Q | L |
| La qualification par classe diffère de la qualification agrégée | `la_qualification_agregee_n_est_pas_la_qualification_par_classe` | ∅ | |
| Règle B (fiducie) : une classe manquante rend le résultat INDETERMINE et marqué | `classe_manquante_rend_indetermine` | p | L |
| La complétude prime sur la classe qualifiante | `la_completude_prime_sur_la_classe_qualifiante` | ∅ | |
| Un D⁺ fondé sur les règles propres d'un collectif n'engage pas les tiers | `citer_ses_regles_n_engage_pas_les_tiers` | p | L |
| Un D⁺ sans source d'engagement (pratique seule) n'est pas un D⁺ de commun et porte un marqueur | `la_pratique_seule_marque_et_ne_qualifie_pas` | p | L |
| Témoin PLE Niayes : le droit d'écrire n'est pas le pouvoir d'engager | `droit_d_ecrire_n_est_pas_pouvoir_d_engager` | p | |

**10.7 Instance de contrôle, constat attesté, annotation de destination (§8.5, conventions rattachées) — PR-43, PR-45, PR-47.** *Ils établissent la forme de l'obligation conventionnelle, non sa justesse.*

| Énoncé démontré | Théorème (module) | Ax. | Convention |
|---|---|---|---|
| Si le tiers n'est pas l'instance commune des deux registres, l'écart reste non arbitré, quel que soit le tiers | `sans_instance_commune_rien_n_est_arbitre` (PR-43) | p | **CONV-16** · L |
| Une instance déclarée liée n'arbitre pas, même désignée par les deux registres | `l_instance_liee_n_arbitre_pas` (PR-43) | p | **CONV-16** · L |
| Une investigation de l'instance commune, déclarée non liée, qui confirme, donne `confirmeParTiers` | `l_instance_commune_tranche_toujours` (PR-43) | p | **CONV-16** |
| Instance : l'instance commune tranche ; un autre tiers non lié, non désigné, ne tranche pas | `seule_l_instance_commune_tranche` (PR-43) | ∅ | **CONV-16** |
| Une désignation unilatérale ou seulement ratifiée ne suffit pas : l'écart reste non arbitré | `la_designation_doit_etre_commune_et_arretee` (PR-43) | ∅ | **CONV-16** |
| Une partie désignée par les deux registres n'est pas instance commune | `l_instance_ne_peut_etre_partie` (PR-43) | ∅ | **CONV-16** |
| Le constat de réalisation par l'instance commune vaut ; celui d'un tiers non désigné ou d'une partie reste attendu | `l_instance_de_controle_peut_constater` (PR-43) | ∅ | **CONV-16** |
| Témoin : `instanceCommune` vrai sous désignation commune, faux sous désignation unilatérale | `instance_commune_temoin_discriminant` (PR-43) | ∅ | **CONV-16** |
| Sans protocole conforme, une saisine au nom du registre est hors protocole | `conv17_sans_protocole_hors_protocole` (PR-45) | p | **CONV-17** · L |
| Un membre qui saisit en son nom fait un signalement individuel : CONV-17 ne l'interdit pas | `conv17_n_interdit_pas_de_signaler` (PR-45) | ∅ | **CONV-17** · L |
| Avec protocole conforme, la saisine est portée au nom du registre et retrouve le statut de constat de PR-44 | `conv17_avec_protocole_retrouve_PR44` (PR-45) | p | **CONV-17** · L |
| Le protocole conforme porte ; sans demande de communication, avec qualification juridique ou sans méthode, la saisine tombe hors protocole | `chaque_rubrique_compte` (PR-45) | ∅ | **CONV-17** |
| Une déclaration détenue par la contrepartie elle-même ne reconstitue pas le miroir : confrontation non obtenue | `la_reconstitution_suppose_un_detenteur_tiers` (PR-45) | ∅ | **CONV-17** · L |
| Instance : 120 constatés, 80 déclarés par la contrepartie : sous-déclaration chiffrée de 40 | `la_sous_declaration_est_chiffree` (PR-45) | ∅ | **CONV-17** |
| Témoins : les quatre issues de la confrontation (concordant, sous-déclaré, sur-déclaré, non obtenu) ; un protocole conforme et un protocole non conforme | `confronter_temoin_discriminant`, `conforme_temoin_discriminant` (PR-45) | ∅ | **CONV-17** |
| Un engagement annoté sans site est en état « destination non déclarée » | `sans_site_destination_non_declaree` (PR-47) | p,Q | **CONV-18** · L |
| Annotation complète, vérification par l'instance commune qui confirme le site : l'engagement est qualifié sur le lien retenu par l'instance | `le_lien_retenu_prime` (PR-47) | p | **CONV-18** · L |
| Instance : déclaré « directement lié », l'engagement n'est pas une dette (lien non qualifié) ; requalifié « contribue » par l'instance, il en devient une | `l_instance_requalifie_le_lien` (PR-47) | ∅ | **CONV-18** |
| Une vérification par un tiers non désigné laisse le lien non qualifié | `un_verificateur_non_designe_ne_vaut_pas` (PR-47) | ∅ | **CONV-18** |
| Site non confirmé : destination infirmée ; objet hors des objets déclarés du registre : destination non déclarée | `destination_infirmee_et_objet_hors_registre` (PR-47) | ∅ | **CONV-18** |
| Témoin : les quatre états de `etat18` | `etat18_temoin_discriminant` (PR-47) | ∅ | **CONV-18** |

---

## 11. Axiomes du modèle associés (AX)

*Les axiomes AX sont des constats sur le monde (Annexe §A.15.0). Aucun n'est formalisé dans ProfReg, qui ne déclare aucun `axiom`. Ne sont retenus que les axiomes que NT-ARCH relie à un théorème repris ci-dessus. Énoncés condensés à partir des fiches citées par l'Annexe §A.15.0, porteur P. Musseau.*

| # | Énoncé (condensé) | Condition de réfutation | Théorèmes liés |
|---|---|---|---|
| **AX-2** — Dette non soldable | Les obligations nées de la dépendance à des processus non créés et non maîtrisés sont héritées collectivement, se renouvellent à chaque cycle et ne se soldent par aucun transfert, faute de créancier apte à donner quittance | Un dispositif ne connaissant que des créances exigibles qui porte durablement une telle obligation sans la convertir ni la déclarer acquittée ; ou un solde par transfert avec quittance d'un créancier apte | `une_dette_A2_ne_s_eteint_jamais`, `le_quart_lemme_est_le_regime_de_A2` (§5) |
| **AX-3** — Découplage du sauvetage et de la répartition | Face à un péril commun, la décision de l'action et la règle de répartition de sa charge peuvent être confiées à deux acteurs distincts, la seconde posée a priori. Sans cette séparation, l'action se bloque sur l'arbitrage entre efficacité et équité | La séparation ne produit aucune différence observable sur les décisions, les contributions ou l'acceptabilité | `sans_mandat_borne_aucune_repartition`, `l_avarie_qualifiee_ne_suffit_pas`, `le_repartiteur_non_nomme_ne_decouple_pas` (§9) |
| **AX-9** — Conflit et permanence | Une institution dure en instituant le conflit et en revenant à son principe. Une autorité d'exception n'est compatible avec la durée que bornée dans le temps par un porteur autre que son bénéficiaire | Des institutions durables ayant supprimé le conflit, ou une durée sans corrélation avec le retour au principe. Condition empirique, non testée par le corpus | `sans_mandat_borne_aucune_repartition` (§9) (lecture) ; témoin `PR12_ne_qualifie_aucune_dette` |
| **AX-7** — Seuil arrêté par les concernés | Il existe des dispositifs (TZCLD ; SSA/Roubaix) où les critères du seuil sont arrêtés par une instance ouverte aux concernés et composée d'eux | Péremption si les dispositifs cessent ; réfutation sur pièces. **Posé ; constat documenté** : dossier de preuve constitué (axiome de référence : `Fiche_Axiome_A7_Seuil_Arrete_Par_Les_Concernes_2026-09-11` ; examen Roubaix, pièces `TZCLD/`, `RADIS/`), qui ne vaut pas preuve Lean. **Appui doctrinal, non garantie** ; en tension déclarée avec RSO-6 | `seul_debiteur_bien_forme_mais_marque` (§5) ; `la_ratification_ne_fonde_pas_le_registre` (§10.3bis) |
| **AX-15** — Rapprochement banque / client | Au titre de l'inventaire (C. com. L.123-12 ; PCG art. 1021-3), l'entreprise et sa banque tiennent chacune le compte de l'autre : mêmes opérations, sens opposé ; l'écart est normal ; à la clôture, un état de rapprochement nomme les opérations manquantes de chaque côté | Péremption si l'obligation d'inventaire disparaît, ou si le compte de l'entreprise n'est qu'une copie du relevé. Tombe comme ancrage de N2 si les deux registres ne sont pas tenus indépendamment | §10.3bis (PR-35) |
| **AX-4** — Mobilisabilité | Visible, convocable, opposable et reprenable sont quatre états qui ne s'impliquent pas l'un l'autre | Un dispositif où la visibilité suffit à l'opposabilité et à la reprise | Rattaché aux **conditions de réfutation** des champs P5 et P7, non aux théorèmes eux-mêmes (§9) |
| **AX-14** — L'objectivité tient à la critique transformatrice (Longino 1990) | L'objectivité d'une connaissance tient au degré auquel la communauté qui la produit permet la critique transformatrice de ses données, méthodes et présupposés ; quatre conditions : voies reconnues de critique, standards partagés, réponse de la communauté, égalité de l'autorité intellectuelle | Tombe, pour l'usage du MRC, si l'on documente un dispositif dont les inscriptions sont durablement contestées et effectivement corrigées sans qu'aucun tiers non partie n'ait accès à la contestation ni à ses règles. **Valable sous conditions déclarées ; transposition déclarée** | `refutation_exige_un_tiers`, `refutation_exige_un_lieu`, `refutation_exige_une_reprise` (§8bis ; conditions 4, 1 et 3 de Longino ; lectures) ; témoins `PR16_alterite_temoin_discriminant`, `PR16_moyens_temoin_discriminant`, `PR16_reprise_temoin_discriminant` |

**Homonymies déclarées par NT-ARCH, à ne pas confondre avec les AX.** « A1 / A1-ter », « A7 » et « A8 » désignent aussi des arbitrages du chantier de corrections (X-9, 28/09). « A2 / A3 » désignent aussi des amendements de NT-G2 (CONV-15).

## 12. Conventions associées (CONV)

*Une convention est opposable et non démontrable (Annexe §A.15). Les théorèmes cités la motivent, la bornent ou en exhibent le patron. Ils ne la démontrent pas. Énoncés repris de l'Annexe §A.15.1.*

| # | Énoncé (condensé) | Rapport aux théorèmes repris |
|---|---|---|
| **CONV-1** | La fraction actorielle est déclarée, jamais calculée : aucun foncteur de calcul n'est mobilisable dans ProfReg | Appui de typage : `fraction_exhibe_sa_source`, borné par `fraction_exhibe_une_source_eventuellement_vide`. Le seul candidat de calcul est réfuté comme oplax (`CB3_candidate_not_oplax_monoidal`). L'inexistence générale d'un foncteur V₁→V₃ reste une lacune |
| **CONV-2** (étendue) | La commutativité du triangle NT-G7 ↔ NT-G2 ↔ NT-ARCH et celle du carré B1↔B2 sont procédurales, et ne dispensent jamais de l'inventaire | `V3_commutatif` en est une lecture (forme 1), jamais un appui. Lectures à témoins croisés : `V3_aboutit_deliberation`, `V3_actoriel_inchange`. **Carré B1↔B2 appuyé par PR-51** (§7) : `aucune_deliberation_sans_inventaire`, `carre_B1B2_commute_sur_les_chemins_admissibles` (A), `le_chemin_direct_n_est_pas_admissible`, `entrer_en_deliberation_exige_l_inventaire` (L), `carre_temoin_discriminant`, `le_carre_a_un_chemin_admissible`. Le triangle reste sans ancrage |
| **CONV-3** | `regimeobligation` est obligatoire : aucun côté d'écriture n'est inscriptible sans lui. Le défaut entraîne le refus | Type de toutes les quantifications sur `RegimeObligation` (§2, §7) |
| **CONV-4** | Le valorimètre déclare sa source : tout valorimètre ou seuil de F8 porte `source_valuemetre`, source déclarée et vérifiable (désignation, résolution, intégrité, porteur nommé) ; le DID en est une forme possible, non la forme obligatoire. Codes de l'effet du défaut proposés : E1 / E4 | `source_sans_porteur_mal_formee` (la clause du porteur mord), `CONV4_satisfaite_sans_DID`, `CONV4_ne_prescrit_aucune_forme` (PR-28, §10.3ter) |
| **CONV-5** | Dans le périmètre où PR-10 opère, « déclencher une règle R-\* » vaut « régime d'usage normatif », et réciproquement ; une mobilisation sous `[VALUATION SUSPENDUE]` ne déclenche aucune règle R-\* (convention de traduction ; effet du défaut proposé : E6) | `suspension_ne_declenche_aucune_regle` en est une lecture (la définition de `DeclencheRegle` encode la convention), avec le témoin `PR10_suspension_temoin_mal_forme`. Risque déclaré (Annexe §A.15.2) : si le set définit le déclenchement autrement, le théorème change de sens sans cesser d'être vrai |
| **CONV-6** | La représentation prospective est exigée de toute écriture qui engage au-delà de l'exercice (effet du défaut : E3). Appliquée au cas planétaire (§5.2) | Ancrages PR-28 (§10.3ter), dont la garde de portée `CONV6_ne_vaut_pas_dans_l_exercice`. Homologue de `V10a_planetaire_force_deliberation` |
| **CONV-7** | Une condition de réfutation obligatoire et absente produit un marqueur, non un refus ; ce marqueur a un horizon (critère de sortie ou caducité). Appliquée au cas planétaire (§5.2) | `regime_sans_refutation_n_autorise_aucune_ecriture`, `candidat_ssi_critere_de_sortie_et_caducite` (au niveau des régimes) ; bornée par `PR8_ne_suffit_pas` (PR-16) : une condition inscrite n'est pas pour autant exerçable |
| **CONV-8** | Un seuil NONDECLARE appelle la délibération. Cela se déclare : l'exhaustivité du type ne l'établit pas | `nondeclare_force_deliberation` (PR-28, moitié positive ; témoins `CONV8_temoin_discriminant`), sur le patron de `V10a_planetaire_force_deliberation` ; moitié négative, patron établi sur le régime du dispositif : `nonDeclare_ne_vaut_pas_permission` (PR-17) |
| **CONV-9** | Toute mobilisation seuil-valuatif déclare au cinquième terme ce que l'agrégat sert à établir. « Non déclaré » ne vaut pas déclaration | Motivée par `BienFormee_ne_borne_pas_le_quintuplet`. Patron repris par `le_non_declare_ne_qualifie_pas_et_marque` |
| **CONV-10** | Dans l'écriture duale, `plein` signifie que le registre reconnaît le lien, jamais qu'il le valorise | `registre_augmente_coherent`, `registre_augmente_non_equivalence`, `accord_sur_l_existence_pas_sur_la_valeur` |
| **CONV-11** | Une écriture `e` dont l'apporteur figure comme créancier n'est bien formée que si le mouvement de maintien est inscrit de façon structurée et si le registre qui le porte est nommé. Depuis D-ED-16 (30/09), six éléments : porteur, contrepartie, registre, situation (solde **calculé**), horizon, critère (`MaintienCONV11`, PR-23 §6) | PR-23 (§10.4) la motive et la borne ; PR-37 l'applique au registre d'un milieu (§10.3bis). Seule la contrepartie est acquise par ailleurs (`registre_augmente_coherent`) |
| **CONV-14** | L'échelle de communalité ne s'agrège pas : axes déclarés séparément, aucun score composite | `la_comparaison_sur_un_axe_n_est_pas_le_classement` (PR-28) |
| **CONV-12** | Une obligation à deux niveaux déclare le niveau de chacune ; la non-équivalence est calculée, non déclarée | Patron cité pour la scission des champs de NT-G7, avec la décision 1 de 12ter (`une_chose_deux_natures`) |
| **CONV-16** | Le tiers d'une écriture duale est l'instance de contrôle commune, désignée par les deux registres par une désignation arrêtée, ni A ni B, non liée ; seule elle arbitre l'écart et peut constater la réalisation du maintien (effet du défaut : E4 `[ÉCART SANS INSTANCE DE CONTRÔLE]`) | PR-43 (§10.7) : `seule_l_instance_commune_tranche`, `l_instance_commune_tranche_toujours`, `sans_instance_commune_rien_n_est_arbitre`, `l_instance_liee_n_arbitre_pas`, `la_designation_doit_etre_commune_et_arretee`, `l_instance_ne_peut_etre_partie`, `l_instance_de_controle_peut_constater`, `instance_commune_temoin_discriminant` |
| **CONV-17** | Seul un constat attesté selon le protocole (sept rubriques) est porté au nom du registre devant un tiers extérieur ; à défaut, la saisine est inscrite `[SAISINE HORS PROTOCOLE]` (E6) ; nul n'est empêché de signaler en son nom | PR-45 (§10.7) : `conv17_sans_protocole_hors_protocole`, `conv17_n_interdit_pas_de_signaler`, `conv17_avec_protocole_retrouve_PR44`, `chaque_rubrique_compte`, `la_reconstitution_suppose_un_detenteur_tiers`, `la_sous_declaration_est_chiffree`, `confronter_temoin_discriminant`, `conforme_temoin_discriminant` |
| **CONV-18** | Tout engagement porté à un registre de chaîne est annoté (site, objet, lien déclaré) ; l'instance commune vérifie la destination et qualifie le lien, le lien retenu primant ; à défaut d'annotation `[DESTINATION NON DÉCLARÉE]` (E4), à défaut de qualification `[LIEN NON QUALIFIÉ PAR L'INSTANCE]` (E5) | PR-47 (§10.7) : `sans_site_destination_non_declaree`, `le_lien_retenu_prime`, `l_instance_requalifie_le_lien`, `un_verificateur_non_designe_ne_vaut_pas`, `destination_infirmee_et_objet_hors_registre`, `etat18_temoin_discriminant` |
| **CONV-19** | Le signal de souffrance est un indice explicatif, jamais l'appui d'une créance ; il n'y fait pas non plus obstacle (effet du défaut proposé : E6) | `la_souffrance_seule_ne_qualifie_aucune_creance` en est une lecture (la définition de `QualifieCreance` encode la convention), avec le témoin `la_souffrance_n_empeche_pas_la_qualification` |
| **CONV-20** | Une qualification du régime affectif n'est inscriptible qu'avec une source déclarée, le consentement collectif et un statut de protection ; sur support distribué, seul NONCOLLECTE est admis (effet du défaut : E1, branche 1bis) | Lectures `sans_source_rien_n_est_legitime`, `noncollecte_n_est_jamais_legitime` ; `la_source_ne_suffit_pas` ; composition `sur_support_distribue_rien_n_est_inscriptible` ; témoin `inscriptible_temoin_discriminant`. NONCOLLECTE désigne l'absence de toute qualification inscrite (décision du porteur, 12/10/2026) |

---

`[LACUNES ET LIMITES DE CETTE NOTE]`
- **Complétude des preuves.** Elle repose sur le build et l'audit du porteur du 12/10/2026 (`audit_2026-10-13_PR58.log`). Une recompilation postérieure prime.
- **Sens des théorèmes.** Que chaque théorème démontre ce que son nom annonce n'est pas établi par l'audit (formes 3 à 6 de §8). Les paraphrases suivent les signatures, que j'ai lues. Les définitions sous-jacentes (`BienFormee`, `effetP5`, `qualifiant`, etc.) n'ont pas été relues ligne à ligne. `[PLAUSIBLE, NON VÉRIFIÉ — fidélité des définitions aux règles de NT-ARCH]`
- **Anciens théorèmes ⊕.** L'attribution au passage de NT-ARCH était mon inférence ; elle est désormais écrite dans NT-ARCH (11/10/2026), qui les nomme à ces passages. `[INFÉRENCE DÉCLARÉE]`
- **Versements du 10/10/2026.** Les énoncés de §8bis, §9ter, §10.3ter (lignes ajoutées) et §10.7 paraphrasent les signatures et docstrings lues ce jour ; les axiomes Lean viennent du journal `audit_2026-10-07_D7.log`. Les deux noms PR-20 que NT-ARCH cite sans énoncé (note complémentaire, section 1) restent hors noyau.
- **Périmètre.** Ne sont retenus que les théorèmes que NT-ARCH cite ou décrit. Les autres théorèmes ProfReg (596 au total), cités ailleurs dans le set ou nulle part, sont hors périmètre.
