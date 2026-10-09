# NT-ARCH v5.7 — Noyau démontré : théorèmes ProfReg, axiomes et conventions associés

*Note condensée dérivée de l'**état de référence MRC v5.7** (`MRC_v5.7/_MANIFESTE_v5.7.md`, qui porte les empreintes courantes ; la v5.7 n'est pas stabilisée et reste modifiable sans autre numéro de version) : `MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md` ; ProfReg à l'état local `68080d0` (arbre git `4ef76277`, identique à celui du commit publié ; 533 théorèmes, 0 `sorryAx`, 10 `Classical.choice`, audit du 07/10/2026). Régénérée le 02/10/2026 ; mise à jour le 07/10/2026 (décision D7, §10.2). Licence : CC BY-NC-SA 4.0. Forme machine : `~/Developer/mrc-script/rules/`. Complément : `NT-ARCH_v5.7_Elements_non_repris_2026-10-02.md`.*

**Critère d'inclusion.** Un énoncé est repris si et seulement si (i) NT-ARCH l'adosse à ProfReg, par un théorème nommé ou par un résultat attribué à un module PR, et (ii) une déclaration `theorem` de ce nom existe dans `~/Developer/ProfReg` et est importée par `ProfReg.lean`. Ce qui n'est que déclaré (définitions, invariants posés, conventions) n'est repris que pour rendre les énoncés lisibles (§0) ou parce qu'il est rattaché à un théorème repris (§11, §12).

**Base de vérification.** `lake build` du porteur (07/10/2026) et `audit/audit_2026-10-07_D7.log` : 533 déclarations, 0 `sorryAx`, 10 `Classical.choice`, 0 erreur. Les sources ne contiennent aucune déclaration `axiom`. NT-ARCH v5.7 §8 et §11 portent cet état d'audit. L'audit d'axiomes établit que les preuves sont complètes. Il n'établit pas qu'elles démontrent ce que leurs noms annoncent (NT-ARCH §8).

**Forme des énoncés.** Chaque ligne paraphrase la **signature Lean**. Quand la prose de NT-ARCH dit autre chose, c'est la signature qui est suivie, et l'écart est consigné dans la note complémentaire, section 3.

**Légende.**
- **Ax.** (axiomes Lean dont dépend la preuve) : ∅ aucun · p `propext` · p,Q `+Quot.sound` · p,C,Q `+Classical.choice` (passage par ℝ ou `ENNReal`).
- **Nat.** (nature, telle que NT-ARCH la déclare) : A architecture · T porte sur un texte (la table §8.5) · G garde de non-régression (vraie par construction, jamais citée comme appui) · L lecture (dépliage d'une définition ; jamais un appui seul, R-3 et R-7 de §8ter-bis).
- ⊕ : NT-ARCH attribue le résultat au module sans nommer le théorème ; le nom est relevé dans le source Lean.
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
| Toute fraction actorielle est de la forme `declaree s v`, donc porte un champ source | `fraction_exhibe_sa_source` (LotL2_PR2_PR14) | ∅ | A · CONV-1 |
| Ce champ peut être vide : `declaree "" v` existe | `fraction_exhibe_une_source_eventuellement_vide` (PR-27) | ∅ | A · borne CONV-1 |

## 2. Couche 1 — R1 et régime systémique (§2, §7)

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Une interaction systémique sans créancier ne satisfait pas R1 standard | `systemique_requires_R1_extension` (P2Synthesis) | p,C,Q | A |
| Si p₁ (à valeurs réelles) est une extension compatible de p₀ (p₁ a b = 1 ⇔ p₀ a b) et si p₀ satisfait R1 (symétrie), alors p₁ a b = 1 → p₁ b a = 1. **L'équivalence « fraction = 1 ⇔ ACTORIEL » est une hypothèse du théorème, pas sa conclusion** | `B1_coherence_condition` (P2Synthesis ; alias déclaré de `R1_preserved_under_CB1`) | p,C,Q | A |

## 3. Couche 1 — machine d'états et inventaire (§4, §5.1)

| Énoncé démontré | Théorème (module) | Ax. | Nat. |
|---|---|---|---|
| Depuis nonAttribuee, le seul niveau valide est deliberation | `nonattribuee_force_deliberation` (V4) | ∅ | A |
| Depuis nonAttribuee, critique n'est jamais valide | `cascade_deliberation_before_critique` (V4) | ∅ | A |
| Avec statut_avant = enDeliberation et statut_apres = attribuee : critique est fermé avant, ouvert après, et l'inventaire est non vide. **La transition elle-même est une hypothèse** | `critique_released_by_porteur` (V4) | p | A |
| Un `InventaireNonVide` n'est pas vide | `inventaire_nonempty_required` (V4) | ∅ | L |
| Témoin : le type est habité et la liste vide en est exclue | `inventaire_nonempty_discrimine` (V4) | ∅ | A |
| MILIEU_DEGRADE_PERSISTANT exige l'inventaire sans régime déclencheur ni déclarant | `le_milieu_declenche_sans_qu_aucun_acteur_ait_declare` (PR-4) | p | A |

## 4. Couche 1 — invariant ACT-ARCH-001 (§7bis, §7bis-a) — PR-3

| Énoncé démontré | Théorème | Ax. |
|---|---|---|
| ACT_ARCH_001, statut attribuee et seuil nonDeclare : contradiction | `attribuee_seuil_declare_required` | ∅ |
| Seuil nonDeclare ⇒ statut ≠ attribuee | `seuil_non_declare_interdit_attribution` | ∅ |
| Statut attribuee ⇒ seuil ∈ {sentience, finaliteImmanente} | `attribution_exige_un_seuil_declare` | ∅ |
| Seuil nonDeclare ⇒ critique n'est pas valide. Conséquence : contester le seuil protège de l'attribution | `seuil_non_declare_bloque_critique` | p |
| Avec une mobilisation seuil-valuatif `BienFormee`, l'attribution exige le seuil déclaré **et** un statut du seuil (quadruplet), par composition avec PR-10 | `attribution_exige_seuil_et_quadruplet` | p |
| Le régime strict équivaut au repli dont l'échéance est l'instant d'attribution (les deux sens) | `stricte_est_instance_du_repli`, `repli_a_l_instant_d_attribution_est_strict` | ∅ |
| Sous échéance non nommée, une dette attribuee dont le seuil n'a jamais été déclaré satisfait l'invariant : le repli sans date dégénère | `repli_sans_echeance_degenere` | ∅ |
| Témoin mal formé : dette attribuee déclarée « dans les temps » qui viole l'invariant strict | `PR3_clauseSeuil_temoin_mal_forme` | ∅ |
| Il existe une dette conforme au repli daté et non conforme au strict : PR-3 ne choisit pas le régime | `PR3_ne_choisit_pas_le_regime` | ∅ |
| Les deux seuils déclarés sont admis : PR-3 ne les départage pas | `PR3_ne_departage_pas_les_seuils` | ∅ |

*Nature : A pour tous. Module : PR3_AttributionSeuil.*

## 5. Couche 1 — extinction, second axe (§4bis) — PR-26 et PR-11

| Énoncé démontré | Théorème | Ax. | Nat. · rattachement |
|---|---|---|---|
| NONDECLARE est bien formé et ne compte pas comme éteint : le silence ne solde rien | `le_silence_ne_solde_rien` ⊕ | p | A · RSO-8 (hors note) |
| Un lemme 4 portant deux prises renseignées, sans lemme 3 antérieur, est mal formé : la lecture paresseuse est refusée | `deux_regimes_divergents_ne_suffisent_pas` ⊕ | ∅ | A |
| Un lemme 4 précédé d'un lemme 3 attesté est bien formé (dépendance 4 → 3) | `le_tiers_atteste_leve_le_refus` ⊕ | ∅ | A |
| Un lemme 3 avec interprète mais sans critère de résolution est mal formé | `tiers_lemme_sans_critere_mal_forme` ⊕ | ∅ | A |
| Orthogonalité : une obligation non attribuée peut être éteinte, une attribuée non éteinte, et les deux sont bien formées | `l_extinction_ne_depend_pas_de_l_attribution` ⊕ | ∅ | A |
| nonAttribuee ⇒ critique n'est pas valide, quel que soit l'état d'extinction | `la_machine_d_attribution_ignore_l_extinction` | ∅ | **G** |
| Une extinction bien formée peut être une remise | `une_extinction_bien_formee_peut_etre_une_remise` ⊕ | ∅ | A |
| Une dette de régime A2 inscrite ETEINTE est mal formée | `une_dette_A2_ne_s_eteint_jamais` | p | A · **AX-2** |
| Une dette A2 au lemme 4 est bien formée (après un lemme 3) | `le_quart_lemme_est_le_regime_de_A2` | ∅ | A · **AX-2** |
| Une extinction déclarée par le seul débiteur est bien formée, marquée, et comptée éteinte | `seul_debiteur_bien_forme_mais_marque` | ∅ | A · AX-7 (appui doctrinal, non garantie) |
| Si les concernés tiennent le miroir, le marqueur est levé | `le_miroir_des_concernes_leve_le_marqueur` | p | A |
| Si un événement fait passer l'obligation à « réalisée », c'est une réalisation vérifiée. Le modèle ignore la remise et la prescription : portée bornée à l'extinction par exécution | `seule_la_realisation_eteint` (PR-11) | p | A |
| Un transfert ne produit aucune obligation : l'obligation n'est pas cessible | `obligation_non_cessible` ⊕ (PR-11) | ∅ | A |

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
| V3 (B1 ↔ B2), régime systémique : le chemin direct aboutit à deliberation | `V3_aboutit_deliberation` (V3) | p | A |
| Régime actoriel : la phase est inchangée par les deux chemins | `V3_actoriel_inchange` (V3) | p | A |
| Chemin direct = chemin via inventaire (vrai par construction, forme 1) | `V3_commutatif` (V3) | p | **L** · CONV-2 étendue |
| VJE (E ↔ J) : le trajet J→E puis E→J laisse l'état inchangé | `VJE_carre_ne_commute_pas_sans_revision` (VJE) | p | A |
| Le sens J→E ne produit pas la révision | `sensJE_ne_produit_pas_la_revision` (VJE) | ∅ | A |
| Si la révision est donnée en prémisse, la précondition vaut `true` ssi la persistance est épisodique | `VJE_ferme_apres_revision_externe` (VJE) | p | A |
| PR-5 (M ↔ R) : il existe un état où sensRM∘sensMR ≠ sensMR∘sensRM | `le_carre_MR_ne_commute_pas` (PR-5) | p | A |
| Avec la voix de la victime inscrite et la traçabilité de la genèse complète, l'acte `lever` désactive la précaution asymétrique | `le_carre_ferme_apres_l_acte` (PR-5) | p | A |

## 8. Contrôle des énoncés et des champs (§8)

| Énoncé démontré | Théorème (module) | Ax. | Nat. · rattachement |
|---|---|---|---|
| Il existe une mobilisation seuil-valuatif `BienFormee` sans cinquième terme déclaré | `BienFormee_ne_borne_pas_le_quintuplet` (PR-10) | p | A · motive **CONV-9** |
| Pour tout contrôle calculable et toute donnée, il existe deux fiches de même donnée, l'une cohérente, l'autre non : le champ déclaré ajoute un degré de liberté | `le_champ_ajoute_un_degre_de_liberte` (PR-21) | p | A |
| Le désaccord entre champ et contrôle existe dans les deux sens | `les_deux_mensonges_existent` ⊕ (PR-21) | ∅ | A |
| Une inscription bien formée dont les seuls réfutants admis sont ses porteurs est contradictoire : l'autoréfutation n'est pas une réfutation | `autorefutation_n_est_pas_refutation` (PR-16) | ∅ | A |
| Si les réfutants ne sont pas énumérables, toute liste close en exclut au moins un | `liste_close_exclut_toujours` (PR-16) | ∅ | A |
| Sans porteur nommé de la charge de preuve, aucun renversement n'est déclaré (renommé D-13-4 ; énoncé repris de la source Lean) | `sans_porteur_nomme_pas_de_renversement` (PR-15) | ∅ | A |
| La qualification d'avarie du code coïncide avec la fiche | `PR12_coincide_avec_la_fiche` (PR-27) | ∅ | **G** |
| Pour tout seuil > 0, il existe une série d'écritures toutes triviales sous le seuil dont l'agrégat **par somme** n'est pas conforme. Coûts entiers : le résultat ne porte pas sur V₂ (§2ter.5) | `serie_bien_formee_agregat_non_conforme` ⊕ (PR-19) | p,Q | A |

## 9. Couche 2 transversale — hôte, porteur représentant, répartiteur (§B.2bis ; F4 §4.2bis–4.2ter)

| Énoncé démontré | Théorème (module) | Ax. | Rattachement |
|---|---|---|---|
| INSTRUMENTATION avec un hôte non renseigné ou AUCUN : effet E3 (délibération) | `hote_non_declare_delibere` (PR-34) | p | |
| Hôte déclaré mais triplet incomplet : un effet est toujours assigné | `la_voie_intermediaire_ne_dispense_pas_du_triplet` (PR-34) | p | |
| Triplet incomplet déclarant « aucune gouvernance imposée » : effet E4 (marqueur). Si cette déclaration est réfutée, ou si une gouvernance est imposée : E3 | `sans_gouvernance_declaree_le_marqueur_suffit` (PR-34) | p | |
| Témoin : un triplet complet n'a pas d'effet ; un hôte non renseigné a l'effet E3 | `P5_temoin_discriminant` (PR-34) | p | |
| Les effets suivent le classement du critère de l'Annexe §A.15.11 (principe et exception) | `P5_suit_le_critere` (PR-34) | p | |
| Porteur représentant des membres sans dimension de pouvoir : attribution mal formée | `representant_sans_dimension_mal_forme` (PR-31) | p | AX-4 (réfutation) |
| Témoin P7 : avec la dimension [AVEC], bien formée ; avec une liste vide, mal formée | `P7_temoin_discriminant` (PR-31) | ∅ | |
| Il existe une attribution bien formée portant [AVEC, SUR] qu'aucune valeur unique ne porte : la lecture exclusive est réfutée | `la_lecture_exclusive_ne_porte_pas_deux_dimensions` (PR-31) | ∅ | |
| Dette de régime A3 dont le mandat du décideur n'est pas borné : le traitement « répartir » ne produit rien | `sans_mandat_borne_aucune_repartition` (PR-12) | p | **AX-3, AX-9** |
| Il existe une répartition dont l'avarie est qualifiée et qui reste mal formée | `l_avarie_qualifiee_ne_suffit_pas` (PR-27) | p | **AX-3** |
| Un répartiteur non nommé rend la répartition mal formée | `le_repartiteur_non_nomme_ne_decouple_pas` (PR-27) | p | **AX-3** |

*Nature : A pour tous.*

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

## 10. F8 — mode comptable

**10.1 Régimes déclarés (§8.4bis, §8.4ter) — PR-22, PR-32**

| Énoncé démontré | Théorème | Ax. | Rattachement |
|---|---|---|---|
| Instance du sol : une même chose, deux natures, deux régimes, deux porteurs | `une_chose_deux_natures` (PR-22) | ∅ | patron de CONV-12 (§8octies) |
| Population non énumérable : une énumération close de régimes exclut un collectif | `enumeration_close_exclut_un_collectif` (PR-22) | ∅ | |
| Instance sur `Nat` : une liste close exclut quelqu'un (ex-`la_decision_1_exige_l_ouverture`) | `une_liste_close_de_collectifs_Nat_exclut_quelqu_un` (PR-22) ↻ | p,Q | |
| Garde : le régime foncier reste porté par le normalisateur IFRS | `PR22_ne_supprime_pas_les_regimes_etablis` (PR-22) | ∅ | |
| Garde : les natures et les noms de régimes diffèrent ; aucun n'est départagé | `PR22_ne_departage_pas_les_regimes` (PR-22) | ∅ | |
| Un régime sans condition de réfutation n'est pas admis et n'autorise aucune écriture | `regime_sans_refutation_n_autorise_aucune_ecriture` (PR-32) | p | **CONV-7** |
| Collectif et date présents, sans réfutation : CANDIDAT_NON_INSTANCIABLE ⇔ critère de sortie ∧ caducité | `candidat_ssi_critere_de_sortie_et_caducite` (PR-32) | p | **CONV-7** |
| Témoins : admis, candidat, non inscrit | `regime_temoin_discriminant` (PR-32) | ∅ | |

**10.2 Ancrage de la sous-couche T (§8.5) — PR-31 ; écriture duale élargie à deux teneurs quelconques (décision D7, 07/10/2026)**

| Énoncé démontré | Théorème | Ax. |
|---|---|---|
| Une écriture T sans traduction ni inscription de communalité n'est pas ancrée : elle est refusée | `sans_ancrage_refusee` | p |
| Un registre de communalité suffit comme ancrage | `le_registre_de_communalite_suffit` | ∅ |
| Un seul ancrage suffit à un côté ; il ne suffit pas à une écriture duale dont l'autre côté n'est pas ancré (un ancrage par côté ; restaté sur `ancreeDuale`, D7 du 07/10/2026) | `la_duale_exige_un_ancrage_par_cote` | ∅ |
| Une écriture duale est ancrée si et seulement si ses deux teneurs sont distincts et chaque côté porte un ancrage déclaré (lecture de `ancreeDuale`, discriminée par les trois suivants) | `ancree_duale_ssi` | ∅ |
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
| La relation d'écriture duale entre deux registres à teneur est symétrique | `ecriture_duale_symetrique` ⊕ (PR-35) | ∅ | **AX-15** |
| Témoin : le prêt bancaire est en écriture duale ; après un remboursement inscrit par la banque seule, il ne l'est plus | `ecriture_duale_temoin_discriminant` ⊕ (PR-35) | ∅ | **AX-15** |
| L'état de rapprochement nomme l'écart (ici, la ligne C⁻ de 100 manquante) | `l_etat_de_rapprochement_nomme_l_ecart` ⊕ (PR-35) | ∅ | **AX-15** |
| Registre augmenté tenu et cohérent, en écriture duale avec un registre B : toute ligne financière dont la contrepartie est le teneur de B entraîne une ligne de communalité vers B et, chez B, une ligne miroir vers A de rôle opposé. Double tenue et écriture duale se composent | `raccord_augmente_duale` (PR-36) | p,Q | |
| Un registre de milieu bien formé n'est pas écrit par le milieu : l'écrivant diffère du titulaire | `le_milieu_n_ecrit_pas_son_registre` ⊕ (PR-37) | p | |
| Une déclaration seulement ratifiée (non arrêtée par les concernés) ne fonde pas un registre opposable | `la_ratification_ne_fonde_pas_le_registre` ⊕ (PR-37) | p | **AX-7** |
| Sans maintien, le registre du milieu n'a pas d'appui ; un maintien porté par un autre registre que celui du titulaire non plus | `sans_maintien_pas_d_appui`, `maintien_d_un_autre_registre_pas_d_appui` ⊕ (PR-37) | p | **CONV-11** |

**10.3ter Ancrages de conventions (§8, rubrique « Conventions d'architecture rattachées ») — PR-28.** *Ils établissent la forme de l'obligation conventionnelle, non sa justesse.*

| Énoncé démontré | Théorème | Ax. | Convention |
|---|---|---|---|
| Sous la règle déclarée, un seuil `NONDECLARE` ne rend accessible que la délibération | `nondeclare_force_deliberation` | ∅ | **CONV-8** |
| Il existe une écriture bien formée (PR-8), engageant au-delà de l'exercice, qui ne satisfait pas CONV-6 : le trou | `BienFormee_ne_borne_pas_la_prospective` | ∅ | **CONV-6** |
| CONV-6 est satisfiable | `CONV6_est_satisfiable` | ∅ | **CONV-6** |
| Deux profils peuvent être ordonnés en sens inverse sur un axe et sur le score composite | `la_comparaison_sur_un_axe_n_est_pas_le_classement` | ∅ | **CONV-14** |

**10.4 Mouvement de maintien (§8.5.3bis) — PR-23 ; motive et borne CONV-11 sans la démontrer**

| Énoncé démontré | Théorème | Ax. |
|---|---|---|
| Il existe une écriture `e` bien formée au sens actuel qui ne satisfait pas CONV-11 | `BienFormee_ne_borne_pas_le_maintien` | ∅ |
| Sans maintien inscrit, deux situations d'écarts différents donnent la même écriture | `deux_dettes_distinctes_meme_ecriture` | ∅ |
| Sans maintien inscrit, R-PRIORITE-CREANCIERS ne rend aucun verdict | `priorite_sans_assiette` | ∅ |
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
| Une écriture à trois livres sans tiers est mal formée (A) | `trois_livres_sans_tiers_mal_formee` (PR-29) | p |
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
| Répartissabilité NON_DETERMINABLE : le résultat est INDETERMINE | `non_determinable_rend_indetermine` | p | |
| Répartissabilité NONDECLARE : l'engagement ne qualifie pas et l'écriture est marquée | `le_non_declare_ne_qualifie_pas_et_marque` | p | **CONV-9** (patron) |
| Témoins : l'asymétrie existentielle qualifie sans marqueur ; FAUX qualifie | `qualifiant_temoin_discriminant` | ∅ | |
| Règle A : une seule classe non répartissable suffit | `une_classe_non_repartissable_suffit` | p,Q | |
| La qualification par classe diffère de la qualification agrégée | `la_qualification_agregee_n_est_pas_la_qualification_par_classe` | ∅ | |
| Règle B (fiducie) : une classe manquante rend le résultat INDETERMINE et marqué | `classe_manquante_rend_indetermine` | p | |
| La complétude prime sur la classe qualifiante | `la_completude_prime_sur_la_classe_qualifiante` | ∅ | |
| Un D⁺ fondé sur les règles propres d'un collectif n'engage pas les tiers | `citer_ses_regles_n_engage_pas_les_tiers` | p | |
| Un D⁺ sans source d'engagement (pratique seule) n'est pas un D⁺ de commun et porte un marqueur | `la_pratique_seule_marque_et_ne_qualifie_pas` | p | |
| Témoin PLE Niayes : le droit d'écrire n'est pas le pouvoir d'engager | `droit_d_ecrire_n_est_pas_pouvoir_d_engager` | p | |

---

## 11. Axiomes du modèle associés (AX)

*Les axiomes AX sont des constats sur le monde (Annexe §A.15.0). Aucun n'est formalisé dans ProfReg, qui ne déclare aucun `axiom`. Ne sont retenus que les axiomes que NT-ARCH relie à un théorème repris ci-dessus. Énoncés condensés à partir des fiches citées par l'Annexe §A.15.0, porteur P. Musseau.*

| # | Énoncé (condensé) | Condition de réfutation | Théorèmes liés |
|---|---|---|---|
| **AX-2** — Dette non soldable | Les obligations nées de la dépendance à des processus non créés et non maîtrisés sont héritées collectivement, se renouvellent à chaque cycle et ne se soldent par aucun transfert, faute de créancier apte à donner quittance | Un dispositif ne connaissant que des créances exigibles qui porte durablement une telle obligation sans la convertir ni la déclarer acquittée ; ou un solde par transfert avec quittance d'un créancier apte | `une_dette_A2_ne_s_eteint_jamais`, `le_quart_lemme_est_le_regime_de_A2` (§5) |
| **AX-3** — Découplage du sauvetage et de la répartition | Face à un péril commun, la décision de l'action et la règle de répartition de sa charge peuvent être confiées à deux acteurs distincts, la seconde posée a priori. Sans cette séparation, l'action se bloque sur l'arbitrage entre efficacité et équité | La séparation ne produit aucune différence observable sur les décisions, les contributions ou l'acceptabilité | `sans_mandat_borne_aucune_repartition`, `l_avarie_qualifiee_ne_suffit_pas`, `le_repartiteur_non_nomme_ne_decouple_pas` (§9) |
| **AX-9** — Conflit et permanence | Une institution dure en instituant le conflit et en revenant à son principe. Une autorité d'exception n'est compatible avec la durée que bornée dans le temps par un porteur autre que son bénéficiaire | Des institutions durables ayant supprimé le conflit, ou une durée sans corrélation avec le retour au principe. Condition empirique, non testée par le corpus | `sans_mandat_borne_aucune_repartition` (§9) |
| **AX-7** — Seuil arrêté par les concernés | Il existe des dispositifs (TZCLD ; SSA/Roubaix) où les critères du seuil sont arrêtés par une instance ouverte aux concernés et composée d'eux | Péremption si les dispositifs cessent ; réfutation sur pièces. **Posé ; constat documenté** : dossier de preuve constitué (axiome de référence : `Fiche_Axiome_A7_Seuil_Arrete_Par_Les_Concernes_2026-09-11` ; examen Roubaix, pièces `TZCLD/`, `RADIS/`), qui ne vaut pas preuve Lean. **Appui doctrinal, non garantie** ; en tension déclarée avec RSO-6 | `seul_debiteur_bien_forme_mais_marque` (§5) ; `la_ratification_ne_fonde_pas_le_registre` (§10.3bis) |
| **AX-15** — Rapprochement banque / client | Au titre de l'inventaire (C. com. L.123-12 ; PCG art. 1021-3), l'entreprise et sa banque tiennent chacune le compte de l'autre : mêmes opérations, sens opposé ; l'écart est normal ; à la clôture, un état de rapprochement nomme les opérations manquantes de chaque côté | Péremption si l'obligation d'inventaire disparaît, ou si le compte de l'entreprise n'est qu'une copie du relevé. Tombe comme ancrage de N2 si les deux registres ne sont pas tenus indépendamment | §10.3bis (PR-35) |
| **AX-4** — Mobilisabilité | Visible, convocable, opposable et reprenable sont quatre états qui ne s'impliquent pas l'un l'autre | Un dispositif où la visibilité suffit à l'opposabilité et à la reprise | Rattaché aux **conditions de réfutation** des champs P5 et P7, non aux théorèmes eux-mêmes (§9) |

**Homonymies déclarées par NT-ARCH, à ne pas confondre avec les AX.** « A1 / A1-ter », « A7 » et « A8 » désignent aussi des arbitrages du chantier de corrections (X-9, 28/09). « A2 / A3 » désignent aussi des amendements de NT-G2 (CONV-15).

## 12. Conventions associées (CONV)

*Une convention est opposable et non démontrable (Annexe §A.15). Les théorèmes cités la motivent, la bornent ou en exhibent le patron. Ils ne la démontrent pas. Énoncés repris de l'Annexe §A.15.1.*

| # | Énoncé (condensé) | Rapport aux théorèmes repris |
|---|---|---|
| **CONV-1** | La fraction actorielle est déclarée, jamais calculée : aucun foncteur de calcul n'est mobilisable dans ProfReg | Appui de typage : `fraction_exhibe_sa_source`, borné par `…_eventuellement_vide`. Le seul candidat de calcul est réfuté comme oplax (`CB3_…`). L'inexistence générale d'un foncteur V₁→V₃ reste une lacune |
| **CONV-2** (étendue) | La commutativité du triangle NT-G7 ↔ NT-G2 ↔ NT-ARCH et celle du carré B1↔B2 sont procédurales, et ne dispensent jamais de l'inventaire | `V3_commutatif` en est une lecture (forme 1), jamais un appui. Le contenu calculable est porté par `V3_aboutit_deliberation` et `V3_actoriel_inchange` |
| **CONV-3** | `regimeobligation` est obligatoire : aucun côté d'écriture n'est inscriptible sans lui. Le défaut entraîne le refus | Type de toutes les quantifications sur `RegimeObligation` (§2, §7) |
| **CONV-6** | La représentation prospective est exigée de toute écriture qui engage au-delà de l'exercice (effet du défaut : E3). Appliquée au cas planétaire (§5.2) | Ancrages PR-28 (§10.3ter). Homologue de `V10a_planetaire_force_deliberation` |
| **CONV-7** | Une condition de réfutation obligatoire et absente produit un marqueur, non un refus ; ce marqueur a un horizon (critère de sortie ou caducité). Appliquée au cas planétaire (§5.2) | `regime_sans_refutation_n_autorise_aucune_ecriture`, `candidat_ssi_critere_de_sortie_et_caducite` (au niveau des régimes) |
| **CONV-8** | Un seuil NONDECLARE appelle la délibération. Cela se déclare : l'exhaustivité du type ne l'établit pas | `nondeclare_force_deliberation` (PR-28, moitié positive), sur le patron de `V10a_planetaire_force_deliberation` |
| **CONV-9** | Toute mobilisation seuil-valuatif déclare au cinquième terme ce que l'agrégat sert à établir. « Non déclaré » ne vaut pas déclaration | Motivée par `BienFormee_ne_borne_pas_le_quintuplet`. Patron repris par `le_non_declare_ne_qualifie_pas_et_marque` |
| **CONV-10** | Dans l'écriture duale, `plein` signifie que le registre reconnaît le lien, jamais qu'il le valorise | `registre_augmente_coherent`, `registre_augmente_non_equivalence`, `accord_sur_l_existence_pas_sur_la_valeur` |
| **CONV-11** | Une écriture `e` dont l'apporteur figure comme créancier n'est bien formée que si le mouvement de maintien est inscrit de façon structurée et si le registre qui le porte est nommé. Depuis D-ED-16 (30/09), six éléments : porteur, contrepartie, registre, situation (solde **calculé**), horizon, critère (`MaintienCONV11`, PR-23 §6) | PR-23 (§10.4) la motive et la borne ; PR-37 l'applique au registre d'un milieu (§10.3bis). Seule la contrepartie est acquise par ailleurs (`registre_augmente_coherent`) |
| **CONV-14** | L'échelle de communalité ne s'agrège pas : axes déclarés séparément, aucun score composite | `la_comparaison_sur_un_axe_n_est_pas_le_classement` (PR-28) |
| **CONV-12** | Une obligation à deux niveaux déclare le niveau de chacune ; la non-équivalence est calculée, non déclarée | Patron cité pour la scission des champs de NT-G7, avec la décision 1 de 12ter (`une_chose_deux_natures`) |

---

`[LACUNES ET LIMITES DE CETTE NOTE]`
- **Complétude des preuves.** Elle repose sur le build et l'audit du porteur du 02/10/2026 (`audit_2026-10-02_PR50.log`). Une recompilation postérieure prime.
- **Sens des théorèmes.** Que chaque théorème démontre ce que son nom annonce n'est pas établi par l'audit (formes 3 à 6 de §8). Les paraphrases suivent les signatures, que j'ai lues. Les définitions sous-jacentes (`BienFormee`, `effetP5`, `qualifiant`, etc.) n'ont pas été relues ligne à ligne. `[PLAUSIBLE, NON VÉRIFIÉ — fidélité des définitions aux règles de NT-ARCH]`
- **Théorèmes marqués ⊕.** L'attribution au passage de NT-ARCH est mon inférence, à partir de la concordance entre la prose et la signature. `[INFÉRENCE DÉCLARÉE]`
- **Périmètre.** Ne sont retenus que les théorèmes que NT-ARCH cite ou décrit. Les autres théorèmes ProfReg (533 au total), cités ailleurs dans le set ou nulle part, sont hors périmètre.
