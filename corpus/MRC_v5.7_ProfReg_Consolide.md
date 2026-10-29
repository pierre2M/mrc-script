# MRC v5.7 — ProfReg consolidé : état formel de référence

> **Vocabulaire.** « Écriture duale » désigne la seule écriture miroir entre deux teneurs (N2, formalisée par PR-35) ; l'objet de L2 est le **registre comptable augmenté** (`RegistreComptableAugmente`, `registre_augmente_{coherent, preserve_R1, non_equivalence}`).

*Fichier du set MRC v5.7. Régime : vérifiabilité-cohérence.*

> **Ce document est le point de renvoi unique du set pour toute mention de ProfReg.** Il est adossé à une **compilation vérifiée**. Les fichiers `.lean` restent les livrables de référence.
>
> **Séparation des régimes (à ne jamais lisser).** ProfReg est le mode **formel calculable** (Lean 4 / Mathlib) ; le set opère en mode **procédural**. Le set peut *invoquer* les théorèmes compilés comme ancrage ; il ne *recalcule* pas leur valeur et ne présente jamais une résolution procédurale comme une complétude formelle — sinon `[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ]`.

---

## §0. Portée de `fraction_exhibe_sa_source`

`fraction_exhibe_sa_source` établit **l'obligation de déclarer une source, jamais sa forme**. CONV-4 étant bornée (source déclarée et vérifiable ; le DID en est une forme possible, non la forme obligatoire), écrire que ProfReg « exige un DID » serait une sur-revendication de forme 8.

> **Analogie, non appui.** `fraction_exhibe_une_source_eventuellement_vide` (PR-27) montre que le théorème **admet la source vide** : il établit l'existence du champ source, non l'obligation de le renseigner. L'obligation est portée par **CONV-4** (et CONV-1 pour la fraction) ; la formule « portée par `fraction_exhibe_sa_source` » est une **analogie**.

---

## §1. Décompte de référence — **604 théorèmes = 584 d'architecture + 20 de texte**

| | |
| --- | --- |
| Théorèmes dans les sources | **604 = 584 d'architecture + 20 de texte** ; `lake build` du porteur confirmé le 13 octobre 2026 (PR-59, après PR-54 à PR-58) ; audit : 604 lignes, 0 `sorryAx`, 10 `Classical.choice`, 0 erreur (`~/Developer/ProfReg/audit/audit_2026-10-13_PR59.log`, sha256 `a11bfdb536b09fc2204faf90699a50d19df2ecfe85455b112b6fbeb8ba09cc35`). Répartition : 295 sans axiome · 269 `propext` · 30 `propext` + `Quot.sound` · 10 avec `Classical.choice` |
| `sorry` dans les sources | **0** |
| `sorryAx` dans l'audit | **0** — *seul contrôle rigoureux ; un `grep sorry` n'en est pas un* |
| Erreurs de compilation | **0** |
| Déclarations dépendant de `Classical.choice` | **10** — voir §3 |
| Fichiers sources / lignes d'`import` | **73 / 73**, correspondance exacte |

**Le critère de décompte.** Est comptée toute déclaration `theorem` ou `lemma` **atteignable depuis `ProfReg.lean`** et auditée par une ligne `#print axioms` dans `Audit.lean`.

> **Pourquoi ce critère.** Le `lakefile.lean` déclare `lean_lib «ProfReg»` **sans `globs`** : Lake ne construit que ce qui est atteignable depuis la racine. **Un fichier non importé est un fichier non prouvé.** `[LACUNE STRUCTURELLE DÉCLARÉE — le contrôle fichiers / imports est la parade, et il est manuel.]`

### §1.2 Empreinte et localisation de la compilation de référence

| | |
| --- | --- |
| Chaîne Lean | `leanprover/lean4:v4.31.0-rc1` |
| Révision Mathlib | `1a59aa5b` ; aesop, Qq, batteries, Cli en `v4.31.0-rc1` |
| Source de l'empreinte |  **`lakefile.lean` épinglé sur `1a59aa5b`** et `lake-manifest.json` (`inputRev` = révision) ; chaîne lue dans `lean-toolchain` |
| Emplacement des sources | **Projet de travail** : `~/Developer/ProfReg` (73 modules sous `ProfReg/` et quatre fichiers racine : `ProfReg.lean`, `Audit.lean`, `R7_Controle.lean`, `Main.lean` ; ≈ 0,5 Mo hors `.lake/`, qui pèse 7,2 Go), **hors du dossier projet**. **Dans le set** : un **instantané daté** par gel de version — `ProfReg/Instantanes_Lean/ProfReg_Lean_<date>_<N>thm/` : archive des sources, `SHA256SUMS.txt`, journal d'audit, `REJOUER.md` |

> Le projet de travail reste hors du set ; **à chaque état de référence** (tag ProfReg), un instantané est déposé par `instantane_lean.sh` (archive sans `.lake/`, sommes sha256 fichier par fichier, empreinte globale, journal d'audit, procédure de rejeu). **La v5.7 est reproductible depuis le set seul une fois son instantané déposé** ; entre deux instantanés, le décompte courant est **attesté** par les journaux d'audit datés et **référencé** par le chemin ci-dessus. `[RÉSERVE]` Une dépendance transitive (`plausible`) a `inputRev = main` dans le manifeste : elle est figée par sa révision tant qu'on ne lance pas `lake update`.
>
> **Instantané déposé** : `ProfReg/Instantanes_Lean/ProfReg_Lean_2026-10-13_604thm/` — archive (81 fichiers, sha256 `6746c1d1883dd67cf22709267b840c28c27272b87c0d32ec8ef343081588984c`), `SHA256SUMS.txt`, journal d'audit, `REJOUER.md` ; 604 théorèmes, 0 `sorryAx`, 10 `Classical.choice` ; empreinte globale `07e09ab782e4b5275ebf8f7bf554053e6b885f74e82659cfdc380bb39fc24e92`. Dépôt git de ProfReg : branche locale `main`, commit `a4a9933` ; **arbre git `68c98f774af444d541be298224b02e2c3d75c074`**, identique à celui de l'unique commit publié sur GitHub (`c1707862`) ; l'instantané porte les sources Lean de cet arbre, avec le README de l'arbre `3a6c9257` (seule différence : le README) (seul l'état courant est public ; les états antérieurs, dont les instantanés du 2, du 7, du 11, du 12 et du 13 octobre, sont conservés localement). Licence AGPL-3.0-only. Le décompte est **reproductible depuis le set**.

---

## §2. Inventaire par fichier

*Soixante-sept modules, dont cinq sans théorème (`Basic`, `Primitives`, `BaseCategories`, `Actors` : types et primitives ; `V10bVerification` : résolu procédural). Les comptes par fichier sont recomptés mécaniquement sur les sources (12/10/2026).*

### Socle catégoriel

| Fichier | N | Contenu |
| --- | --- | --- |
| `BaseCategories.lean` | 0 | V₀ (Bool), V₁ (ℝ), V₂ (ENNReal) |
| `Actors.lean` | 0 | `Actor := String` |
| `Basic.lean`, `Primitives.lean` | 0 | types du registre |
| `Interactions.lean` |  3 | R1 par régime, `SystemicInteraction` ; `R1_systemique` = **indicateur** de satisfaisabilité, caractérisé par `R1_systemique_ssi_creancier` |
| `ChangeOfBase.lean` | 4 | CB1 (Bool→ℝ), CB2 (ℝ→ENNReal via −log) |
| `V2Verification.lean` | 1 | `R1_preserved_under_CB1` |
| `CB3Attempt.lean` | 1 | `CB3_candidate_not_oplax_monoidal` |
| `P2Synthesis.lean` | 2 | synthèse P2 ; `B1_coherence_condition` = **alias déclaré** de `R1_preserved_under_CB1` |
| `V1Verification.lean` |   3 | `V1_commutatif` — carré F4–F6 ; **lecture** du champ `coherence`, témoin `V1_coherence_discrimine` ; **caractérisation** `V1_commute_ssi_coherence` ; la cohérence relève de **CONV-15** (co-obligation, marqueur `[PAIRE F4 NON COHÉRENTE]`, jamais refus) |
| `V3Verification.lean` | 3 |  phase INVENTAIRE ; `V3_commutatif` = **lecture** des deux définitions (forme 1) — la commutativité B1↔B2 est **procédurale** |

### Vérifications de grammaire

| Fichier | N | Contenu |
| --- | --- | --- |
| `V4Verification.lean` |  6 | cascade R-INTERDIT-ABSOLU ; `transition_valide` ; `inventaire_nonempty_required` = lecture du type, témoin `inventaire_nonempty_discrimine` |
| `V4cVerification.lean` | 3 | préservation ACTORIEL (ACT-G2-010) — **procédural** ; deux formes 1 déclarées, `V4c_actoriel_preserved` et son alias `V4c_actoriel_preserved_alias` |
| `V10Verification.lean` | 3 | cohérence planétaire V10a |
| `V10bVerification.lean` |  0 | carré triangulaire NT-G7↔NT-G2↔NT-ARCH — **procédural** ; aucun théorème : la commutation relève de **CONV-2** |
| `VJEVerification.lean` |  11 | carré J↔E (AM-G7-04) + **PR-6** ; `sensJE_ne_produit_pas_la_revision` = **garde R-5** |

### Programme de preuve PR-1 à PR-25

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `LotL2_PR2_PR14.lean` |  13 |  **registre comptable augmenté**  ; **PR-2** régime par écriture ; **PR-14** opposabilité ; **CONV-4** source exhibée (l'obligation, non la forme — §0) |
| `PR3_AttributionSeuil.lean` |  15 | **PR-3** — attribution exige un seuil déclaré ; régimes strict / repli |
| `PR4_InventaireTriggerMilieu.lean` |   9 | témoin `PR4_temoin_discriminant` ; **le type ne produit aucun inventaire** ; le milieu déclenche sans déclarant ; `appelImmanentNonEntendu` = **projection booléenne déclarée** de `appel_entendu_milieu` |
| `PR5_CarreMR.lean` |  8 | **le carré M↔R NE COMMUTE PAS** ; ce qui le ferme est un acte |
| `PR7_PrioriteF6F10.lean` | 8 | priorité F6/F10 ; **garde-fou anti-épistocratique démontré** |
| `PR8_RefutationPratique.lean` |   11 | **CONV-7 au marqueur** : `le_marqueur_se_leve_exactement_sur_le_defaut`, `bien_formee_sans_refutation_n_est_pas_obligee` ; représentation pratique et planétaire exigent une réfutation ; **exactement ces deux** (`exactement_deux_regimes_obliges`, caractérisation) |
| `PR9_CanalEA.lean` |  9 | témoin `PR9_canalAE_temoin_discriminant` ; **le couplage E↔A EST un cycle, et les deux ordres diffèrent** (`les_deux_ordres_different` ; l'éponyme `le_couplage_est_un_cycle` est une forme 1, déclarée) ; la terminaison se vérifie sur le canal ; *étiquettes* : `canalEA` est le sens que NT-G9 appelle A→E — correspondance déclarée en tête du fichier, identifiants conservés |
| `PR10_StatutSeuil.lean` |  16 | quintuplet du statut du seuil ; **CONV-9** usage de l'agrégat ; **CONV-5** : `suspension_ne_declenche_aucune_regle`, lecture (`DeclencheRegle` est défini comme le régime d'usage normatif), témoin `PR10_suspension_temoin_mal_forme` (NT-ARCH §8, table des conventions) |
| `PR11_ObligationNonCessible.lean` | 14 | obligation non cessible ; **CONV-13** successeur déclaré |
| `PR12_NonConfusionDettes.lean` |   17 | témoin `confusion_temoin_discriminant` ; non-confusion AX-2 / AX-3 ; contrôle calculé ; **quatre conditions d'avarie + mandat borné** |
| `PR13_NonEquivalenceDeclaree.lean` | 16 | `la_fusion_au_meme_niveau_somme_les_charges` ; **CONV-12** — déclarer les niveaux, calculer la non-équivalence |
| `PR15_ChargeDePreuve.lean` |  5 | la charge de preuve ne retombe pas sur les affectés ; trois **lectures** témoignées ; `sans_porteur_nomme_pas_de_renversement` |
| `PR16_RefutationTiers.lean` |  14 | la réfutation exige un tiers, un lieu, une reprise |
| `PR17_RegimeDispositif.lean` |  7 | régime du dispositif déclaré ; NONDECLARE ≠ permission |
| `PR18_PorteurDuSeuil.lean` |   8 | **la relation porteur / population se décide sur la seule inscription** (une procédure booléenne la tranche) ; déclarant seul réfutant est mal formé |
| `PR19_SerieAgregat.lean` | 8 | série bien formée, agrégat non conforme — pour tout seuil positif (`serie_bien_formee_agregat_non_conforme`) |
| `PR20_MiroirInterActeurs.lean` |  18 |  lien inter-acteurs **porté par un registre augmenté** (relation globale, sans teneur)  ; témoin `lien_temoin_discriminant` (R-7) ; `les_deux_registres_augmentes_ont_le_meme_socle` |
| `PR21_ChampDouble.lean` |  8 | **tout champ déclaré doublant un contrôle calculable peut mentir** |
| `PR22_RegimeDeclare.lean` |  7 | une chose, deux régimes ; les collectifs ne sont pas énumérables — hypothèse de modélisation, satisfaite sur `Nat` par `nat_non_enumerable` (PR-16), qu'appelle `une_liste_close_de_collectifs_Nat_exclut_quelqu_un` ; instances de PR-16 déclarées |
| `PR23_MouvementDeMaintien.lean` |   **19**  | témoin `ecart_lisible_temoin_discriminant` ; **CONV-11** — le mouvement de maintien inscrit ; la glose ne suffit pas ; **§6** : `MaintienCONV11` à six éléments, solde calculé, projection vers `InscriptionMaintien`, `CONV11_complet_retrouve_PR23`, `la_projection_perd_la_contrepartie`, `la_dette_de_preservation_est_calculee` |
| `PR24_PorteeFinie.lean` |   9 | maillon **L1** — ce que la présence perd, l'inscription le garde ; la non-énumérabilité des relations est une hypothèse de modélisation, satisfaite sur `Nat` par `nat_non_enumerable` (PR-16) |
| `PR25_VerificationSansDivulgation.lean` | 9 | témoin `la_lecture_com_temoin_discriminant` (R-7) ; appui de **PAL-5** — vérifier sans divulguer ; témoins **sur un lien existant** ; ce qui n'est pas divulgué est l'inscription du lien par le registre financier, non un montant (CONV-10) |

### Second axe d'extinction, candidats, ancrages de conventions (PR-26 à PR-28)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR26_ExtinctionSecondAxe.lean` | 11 | **second axe d'extinction** (NT-ARCH §4bis) : bonne formation des quatre lemmes et du hors-tétralemme ; dépendance 4 → 3 effective ; orthogonalité à l'attribution ; seul débiteur marqué ; remise admise (cohérent avec NC bornée) ; **une dette AX-2 ne s'inscrit jamais en `ETEINTE`**, le quart lemme est son régime **Une garde de non-régression déclarée** (NT-ARCH §8ter-bis R-5) : `la_machine_d_attribution_ignore_l_extinction` ; `le_miroir_des_concernes_leve_le_marqueur` est une **lecture** licite, non une garde |
| `PR27_Candidats_Septembre.lean` |  6 | AX-3 : **répartiteur ≠ décideur** (NT-ARCH §4.2ter) ; CONV-4 : **la source compilée peut être vide** ; CONV-14 : **le score ne détermine pas les axes** ; `PR12_coincide_avec_la_fiche` : garde de non-régression vraie par construction, **déclarée** |
| `PR28_AncragesConventions.lean` | 9 | **ancrages de conventions** : CONV-8 moitié positive, CONV-6 (trou, satisfiabilité, garde), CONV-4 bornée (satisfiable sans DID, porteur mordant, aucune forme prescrite), garde CONV-14 — Annexe §A.15.10 |

### Table des arités, communalité, bonne formation déclarative, effet du défaut (PR-29 à PR-34)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR29_TableArites.lean` | 10 (5 texte + 5) | **table §8.5.2** : fidélité de la transcription ; **la colonne d'origine ne satisfait pas B7** (8 / 15) ; le décompte dépend de la lecture du « + » (10 / 8) ; sous la colonne dédoublée,  **quatre lacunes** ; aucune contrepartie perdue *(texte)* — **absent ⇏ violation** ; le statut ne se lit pas sur la table seule — **trois livres sans tiers mal formée**, la troisième arité n'est pas la deuxième |
| `PR30_Communalite.lean` | 11 | **§8.5.6, premier ancrage** : garde de la branche B (capital d'apporteur) ; `NON_DETERMINABLE` → `INDETERMINE` ; `NONDECLARE` ne qualifie pas et marque — règle A, par classe — règle B, complétude ; **droit d'écrire ⇏ pouvoir d'engager** |
| `PR31_BonneFormationDeclarative.lean` | 16 | S-P-I de `C-MILIEU-VECU`, **marqueur** ; ancrage T, **refus** ; ancrage de l'écriture duale élargi à deux teneurs quelconques (`ancreeDuale`, D7 du 07/10) ; « sans objet » non motivé ≡ `NONDECLARE`, **refus** ; P7 : `dimension_pouvoir` liste non exclusive, **mal formée** |
| `PR32_HorizonDuMarqueur.lean` | 5 | **admission d'un régime** : sans condition de réfutation, aucune écriture autorisée ; candidat **ssi** critère de sortie et caducité — **horizon du marqueur CONV-7** : il atteint toujours un état caduc |
| `PR33_EffetDuDefaut.lean` | 7 | **codes E0-E7 et critère ordonné** (Annexe §A.15.11) : classement de référence (CONV-20 compris) ; **branche 1bis** — l'inscription dommageable est refusée avant tout marqueur ; l'ordre fait prévaloir l'objet (CONV-3) ; mal formée ⇏ refusée ; un refus ne vient que des branches 1-3 ; un marqueur E4 ne vient que de l'appréciation ou du candidat — *théorèmes de forme* |
| `PR34_InstrumentHote.lean` | 5 | **instrument-hôte** : hôte non déclaré → E3 ; triplet incomplet reste un défaut ; exception E4 si aucune gouvernance déclarée, réfutable ; **P5 suit le critère** |

### Écriture duale entre teneurs et registres de chaîne (PR-35 à PR-49)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR35_EcritureDuale.lean` *(PAL-2c)*  | 16 | **écriture duale entre teneurs** (N2) : `Registre` à **teneur**, `ecart`, `etatRapprochement`, `EcritureDuale` (rapprochement vide, décidable), `completer` ; instance banque / emprunteur (Richard et al. 2018, ch. 40 §4) ; peut échouer ; miroir de rôle opposé ; rapprochement résorbe un sens et un seul ; existence sans valeur ; 2 lemmes de liste constructifs. **0 `Classical.choice`** |
| `PR36_RaccordAugmenteDuale.lean` *(PAL-2c)*  | 12 | **raccord N3 ↔ N2** : `RegistreAugmenteTenu`, `Coherent` ; passerelle vers L2 (`versL2`, `le_registre_tenu_satisfait_L2`) ; `raccord_augmente_duale` ; gardes : sans cohérence / sans écriture duale pas de raccord, pas de valeur ; témoin discriminant. **0 `Classical.choice`** |
| `PR37_RegistreDuMilieu.lean` *(PAL-2c)*  |   **16**  | **registre d'un milieu** : `DeclarationConcernes` (arrêtée / ratifiée / non déclarée — AX-7),  `MaintienCONV11` de PR-23 (six éléments, registre nommé vérifié, solde calculé), `RegistreDuMilieu` (titulaire = milieu, écrivant désigné) ; l'écart reste inscrit sans registre ; ratification, absence de déclaration, maintien absent ou nommant un autre registre : pas d'appui ; instance entreprise / rivière. **0 `Classical.choice`** ; `DeclarationConcernes` (titulaire, nature, critère d'inclusion, concernés, écrivant, interprète, mode, réexamen) ; `versInscriptionMilieu` (raccord PR-31) ; date d'évaluation |
| `PR38_ReciproquesIntragroupe.lean` *(PAL-2c)*  |  **7**   | **comptes réciproques intragroupe** : `signe`, `solde`, `soldeConsolide` ; une paire concordante s'annule ; le prêt mère / filiale a la forme de AX-15 ; la consolidation efface ce que l'écriture duale conserve ; sans concordance, écart de conciliation ; l'addition de deux teneurs est possible mais non prescrite. **0 `Classical.choice`** |
| `PR39_RealisationDuMaintien.lean` *(PAL-2c)*  | 7 | **réalisation du maintien** : `EtatResultat`, `Constat`, `LigneRealisation`, `etat` (lu depuis l'autre teneur), `resteOuvert`, `etatExercice` ; sans constat rien n'est déchargé ; auto-constat sans valeur ; contestation inscrite ; reconduction. **0 `Classical.choice`** |
| `PR40_StatutDeLEcart.lean` *(PAL-2c)*  | 6 | **statut de l'écart** : `Communication`, `StatutEcart`, `denegation`, `statut`, `ecartQualifie` ; le statut ne change pas l'écart ; rien à qualifier en écriture duale ; non vérifiable ≠ constaté ; refus ≠ silence ; dénégation → contesté. **0 `Classical.choice`** |
| `PR41_ArbitrageParUnTiers.lean` *(PAL-2c)*  | 6 | **arbitrage de l'écart par un tiers** (ISA 505) : `Investigation`, `tiersRecevable`, `StatutArbitre`, `arbitrer`, `ecartArbitre` ; aucun teneur ne tranche ; un tiers lié ne tranche pas ; l'arbitrage n'efface rien. **0 `Classical.choice`** |
| `PR42_TeneursIndependants.lean` *(PAL-2c)*  | 7 | **teneurs indépendants** (ISA 505 §2, ISA 550 §10) : `Relation`, `Probante` ; entre liés sans tiers, rien ne prouve ; mère / filiale, témoin du groupe, subordination. **0 `Classical.choice`** |
| `PR43_InstanceDeControle.lean` *(PAL-2c, CONV-16)*  |  **8**   | **instance de contrôle commune** : `DesignationControle`, `designe`, `instanceCommune`, `arbitrerInstitue` (PR-41 restreint), `etatInstitue` (PR-39 étendu) ; sans instance commune rien n'est arbitré ; l'instance liée n'arbitre pas ; désignation commune et arrêtée ; l'instance ne peut être partie ; elle peut constater. **0 `Classical.choice`** |
| `PR44_ConstatUnilateralEtTiersExterieur.lean` *(PAL-2c)*  |  **14**  | **constat unilatéral** : `Attestation`, `attestationValide`, `Piece`, `Force` (renseignement / libre appréciation / foi jusqu'à preuve contraire), `Voie` (négociation, transaction, juge judiciaire, autorité administrative, parquet, arbitrage, autorité de supervision, injonction de vigilance), `saisineRecevable`, `StatutConstat` (unilatéral → attesté → porté → tranché) ; l'attestation interne ne tranche pas envers X ; sans pièce extérieure pas de foi (art. 1363) ; au pénal, renseignement ; voies privées fermées sans X, voies publiques indifférentes à son refus ; le juge du préjudice écologique exige la qualité (art. 1248) ; rien n'est effacé. **0 `Classical.choice`** |
| `PR45_ProtocoleAttestationEtMiroirReconstitue.lean` *(PAL-2c, CONV-17)*  | 9 | **protocole d'attestation** (`Protocole`, `PieceTracee`, `conforme` : sept rubriques), **CONV-17** (`Emetteur`, `StatutSaisine`, `statut17` : hors protocole, signalement individuel, retour à PR-44), **miroir reconstitué** (`DeclarationAdministrative`, `Confrontation`, `confronter` : détenteur tiers requis ; sous-déclaration chiffrée). **0 `Classical.choice`** |
| `PR46_RegistreDeChaine.lean` *(PAL-2c, S3)*  |   **13**   | **registre de chaîne** : `Lien` (cause / contribue / directement lié, OCDE 2023), `Objet`, `NatureEngagement`, `qualifier`, `EngagementVigilance`, `registreChaine`, `registreEntreprise`, `recenserSiFondee`, `consentPour` ; l'étoile porte la chaîne ; la projection perd le fournisseur ; directement lié, pas de dette de réparation ; objets déclarés ; pas de consolidation ; teneur ≠ instance ; plainte   reconnue par la société, ou retenue par l'instance / l'autorité (PR-48) = miroir inscrit ou forcé ; consentement ex ante. **0 `Classical.choice`** ; `la_signature_n_ouvre_pas_la_transaction` (la signature ouvre l'arbitrage, non la transaction) |
| `PR47_AnnotationDeDestination.lean` *(PAL-2c, CONV-18)*  | 6 | **annotation de destination** : `Annotation`, `Verification`, `EngagementAnnote`, `annotationComplete`, `etat18` (destination non déclarée / lien non qualifié / vérifié / destination infirmée) ; sans site pas de destination ; le lien retenu par l'instance prime ; requalification « directement lié » → « contribue » : la réparation devient dette ; vérificateur non désigné sans effet. **0 `Classical.choice`** |
| `PR48_QualificationDesPlaintes.lean` *(PAL-2c)*  | 7 | **qualification des plaintes** (CS3D art. 14) : `AvisSociete` (fondée / non fondée / sans réponse), `statutApresAvis` (non fondée → `conteste`, silence → `nonVerifiable`), `IssuePlainte`, `issuePlainte` (instance commune, puis autorité de supervision), `retenue`, `miroirApres` ; « non fondée » est une contestation ; plainte retenue = miroir forcé ; la société ne s'arbitre pas ; sans instance, l'autorité. **0 `Classical.choice`** — *PR-44 porte la voie `autoriteSupervision`.* |
| `PR49_InjonctionEtGardeDeForme.lean` *(PAL-2c)*  | 7 | **garde de forme** (`la_conformite_ne_vaut_pas_realisation`, indépendance conformité / réalisation) ; **injonction de vigilance** : `ExigenceGriefs` (stricte / souple), `MiseEnDemeure`, `injonctionRecevable` ; sans mise en demeure ou avant trois mois, irrecevable ; la lecture stricte ferme ce que la souple ouvre ; intérêt à agir requis. **0 `Classical.choice`** — *PR-44 : voie `injonctionVigilance`, qualité `interetAAgir`.* |

### Forme du signal `carre_non_commutatif` (PR-50)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR50_CarreNonCommutatif.lean` *(F3)* | 7 | **forme du signal** de la Fiche F3 : `Carre` (deux chemins), `EcartDeclare` (nul sur l'égalité), `signal` (seuil déclaré, strictement positif, atteint), `marqueurSeuilNonDeclare`, `action` ; un signal atteste une non-commutation ; un carré qui commute ne signale pas ; le signal n'est pas la non-commutativité (sous le seuil) ; dépendance au seuil et à l'écart déclarés ; sans seuil, marqueur. **Sans Mathlib, 0 `Classical.choice`**. Hors ProfReg : écart SVD / FCA pondérée, 2-morphismes, 2-cellule (NT-ARCH F3 §3.5) |

### Carré B1↔B2 (PR-51)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR51_CarreB1B2.lean` *(CONV-2 étendue)* | 6 | **règle des pas déclarée** (`pas`, `admissible`), puis commutation conclue sur les chemins admissibles : le chemin direct n'est pas admissible dès que l'inventaire est requis ; aucun chemin admissible n'atteint la délibération sans inventaire (induction) ; deux chemins admissibles qui l'atteignent passent tous deux par l'inventaire, sur une écriture qui porte un inventaire non vide ; témoins. Lean pur, importe PR-4 ; 6 `propext`. Ne porte pas sur le carré triangulaire |

### Qualification du régime affectif (PR-52)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR52_QualificationAffective.lean` *(CONV-19, CONV-20 ; NT-G9)* | 7 | **règle d'inscription** (`Legitime` : source déclarée, consentement collectif, statut protecteur) et **règle du support** (`SupportAdmis` : sur support distribué, `NONCOLLECTE`) ; sans source rien n'est légitime ; la source est nécessaire, non suffisante ; `NONCOLLECTE` — l'absence de qualification inscrite, par décision du porteur — n'est jamais une qualification légitime ; **composées, les deux règles ferment toute inscription sur support distribué** ; témoin discriminant ; **non-confusion** (`QualifieCreance`) : la souffrance seule ne qualifie aucune créance, et n'y fait pas obstacle. **0 `Classical.choice`** ; 4 sans axiome, 3 `propext` |

### Canal G-JUSTICE → G-AFFECTIF (PR-53)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR53_CanalJusticeAffectif.lean` *(NT-G7 §4.3 ; NT-G9 §4.2, §10.2 ; importe PR-52, PR-33)* | 11 | **filtre** (`passe` : type testimonial ou herméneutique, non déclaré local et épisodique, documentant désigné, documentation indépendante de la souffrance) : n'écarte que le déclaré incident ; local mais structurel passe ; non déclaré passe, marqué ; issue de la seule souffrance ne passe pas ; témoin discriminant ; **l'hypothèse seule ne qualifie pas le régime** (PR-52) ; **cycle A→J→A qui termine**, la souffrance ne se confirme pas elle-même ; **déni du réel** déclaré et présumé disjoints (le présumé lit aussi le départ des porteurs, C-MEMOIRE-PERTES), témoin ; **règle d'ordre** : deux défauts, E4 et E3 (PR-33). **0 `Classical.choice`** ; 6 sans axiome, 5 `propext` |

### Boucle confirmante et contre-performativité (PR-54)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR54_BoucleEtContrePerformativite.lean` *(NT-G4 §2.1, §7, §8 ; NT-ARCH F3, §B.2bis ; importe PR-34)* | 8 | **forme du signal `boucle_confirmante_détectée`** : il atteste un point fixe aligné ; témoin discriminant ; **une boucle contre-performative ne le lève jamais** (Unal et al. 2025, p. 20) ; **levée partielle par l'effet d'hôte** : un cas contraire vu (défaut P5), et hors effet d'hôte la contre-performativité n'est vue par aucun signal ; témoin ; **les signaux lisent des déclarations** : l'hôte réel n'est pas lu, un hôte réel déclaré `AUCUN` échappe. **0 `Classical.choice`** |

### CORPUS_NON_CONSENTI : signal, blocage, sortie (PR-55)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR55_CorpusNonConsenti.lean` *(NT-G4 §3.2, §6, §6bis ; NT-ARCH F3, F10 ; décisions n° 42, 43, 58, 59)* | 7 | le signal lit `mode_validation_concept = EXPERTAL` ; témoin discriminant ; **la représentation ne couvre pas un acteur joignable** ; **l'absence n'est jamais un verrou** ; **les deux clés sont nécessaires** ; un changement de mode ne lève pas le blocage ; témoin discriminant du blocage. **0 `Classical.choice`**. `[PÉREMPTION PARTIELLE — §2.1]` (décisions n° 58 et 59) |

### Consentement par personne, absence opposable (PR-56)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR56_ConsentementEtAbsenceOpposable.lean` *(NT-G4 §6bis ; NT-ARCH F3 ; décisions n° 45, 46 ; importe PR-55)* | 7 | **consentement du corpus dérivé** des consentements par personne ; témoin ; **une recherche sans trace ni attestation n'est pas une absence** ; une contestation retenue fait tomber la représentation ; témoin discriminant (trace seule, attestation seule, ni l'une ni l'autre) ; **PR-56 restreint PR-55** ; **l'absence opposable n'est jamais un verrou**. **0 `Classical.choice`** |

### Phase RECHERCHE_INTERVENTION et contre-performativité attestée (PR-57)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR57_EnqueteEtContrePerformativite.lean` *(NT-ARCH §B.2ter ; NT-G4 §7 ; décisions n° 47 à 50 ; importe PR-54)* | 10 | **recevabilité du constat** : NON INSTRUIT ne vaut pas ALIGNÉ ; le porteur ne s'atteste pas ; sans les concernés, pas de constat ; hypothèse après coup non admise ; témoin discriminant ; **À QUALIFIER relance sans signal** ; **pas de relance sans constat** ; **l'enquête rend visible la contre-performativité que PR-54 montre invisible** ; sans constat, la lacune demeure ; **une échéance sans les concernés n'ouvre pas la phase**. **0 `Classical.choice`** |

### Un commun suppose ses instances ; axes séparables (PR-58)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR58_CommunTroisInstances.lean` *(NT-ARCH §8.5.6.3, §8.5.6.4, §8.5.6.2bis ; NT-G6 §2.1, §7 ; décision n° 52)* | 9 | **le typage T est nécessaire, non suffisant** ; une indivision n'est pas un commun ; **sans instance délibérative ou de contrôle, pas de commun** ; une forme admise sans délibération n'est pas un commun (marais des Lagneux) ; `P+` seul n'est jamais un commun ; l'intérêt diffus se passe d'attributaire ; témoin discriminant ; **l'intérêt commun ne détermine pas l'inclusivité** (communauté fermée, chose commune de l'art. 714 ; un seul sens). **0 `Classical.choice`** |

### Écart par droit ; inclusivité par instance (PR-59)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `PR59_EcartParDroitEtInclusiviteParInstance.lean` *(NT-G6 §2.1, §3.1, §3.2 ; NT-ARCH F6 ; décisions n° 54 et 55 ; importe PR-58)* | 8 | **écart droit par droit** : pas d'alerte sans seuil déclaré pour ce droit ; **non instruit ≠ nul** ; un cycle ne suffit pas ; **même écart total, droits différents** (gestion : pouvoir ; accès : usage) ; sans faisceau, pas d'alerte ; **second sens sur l'instance de contrôle** : l'inclusivité du contrôle ne détermine pas l'intérêt commun (action populaire, p. 411 / recours pour excès de pouvoir, p. 332-333) ; témoin (recours pour excès de pouvoir / action de groupe) ; le premier sens porte sur l'instance attributaire. Instance délibérative sans témoin. 4 `propext`, 4 sans axiome ; **0 `Classical.choice`** |

### Sonde — colonne « texte » (20)

| Fichier | N | Ce qu'il établit |
| --- | --- | --- |
| `Sonde_PCEDed.lean` |  15 | formalise **le texte** de NT-ARCH §8.5 — table §8.5.2 **d'origine** (13 théorèmes) **et table en vigueur** (2) — voir l'avertissement ci-dessous |
| `PR29_TableArites.lean` §1-§2 | 5 | formalise **le texte** de la table §8.5.2 en vigueur et de ses colonnes : fidélité, constat B7, lecture du « + », quatre lacunes, contrepartie conservée |

> **⚠️ Statut particulier de la sonde.** Ses quinze théorèmes portent sur **un texte du set**, non sur l'architecture, et **aucun n'établit une thèse du MRC.** Deux d'entre eux portent sur des typages composites qui ne figurent plus dans la couche T — **cas de péremption d'objet** (forme 7). `[BASE DÉCLARÉE]`
>
> **Le décompte de 604 agrège donc deux natures** : **584** d'architecture, **20** de texte. **Les deux colonnes sont le décompte de référence** : toute citation d'un total ProfReg donne les deux nombres.

### §2.1 Péremption d'objet dans un fichier compilé — `PR10_ne_vaut_pas_pour_les_relationnelles`

Un théorème compilé peut prendre pour **témoin** une chaîne qui nomme un champ du set : Lean n'en connaît que la chaîne. Si le champ est scindé ou retiré dans le set, **le théorème reste vrai et sa preuve tient**, mais son témoin est périmé — forme 7 (péremption d'objet), début de forme 6 (témoin dégénéré).

> **Ce que cela change pour le décompte : rien.** `Audit.lean` valide un théorème dont le témoin nommerait un champ qui n'existe plus — **sans que cela invalide quoi que ce soit**, ce qui est exactement ce qui rend la forme 7 difficile à voir. Les témoins de `PR10_ne_vaut_pas_pour_les_relationnelles` et d'`orthogonalite_charge_valuative_usage` nomment des champs en vigueur (`"capabilite_individuelle"`, `"seuil_franchi"`). **Aucun crible de péremption d'objet n'existe** (Lacunes).

**Second cas — PR-55 et la règle d'inscription de CORPUS\_NON\_CONSENTI** (décisions n° 58 et 59). PR-55 modélise un **signal inscrit** (`signale`) qui **bloque** la délibération (`bloque`) jusqu'à la levée par les deux clés (`leve`). La règle en vigueur **refuse l'inscription** du corpus tant qu'un acteur n'est pas couvert (E1, NT-G4 §6bis). Les théorèmes restent vrais et le décompte ne change pas ; leur lecture se répartit ainsi :

| Théorème | Lecture sous la règle en vigueur |
| --- | --- |
| `corpus_non_consenti_lit_le_mode_de_validation`, `corpus_signal_temoin_discriminant` | inchangée : condition de la règle |
| `la_representation_ne_couvre_pas_un_joignable`, `les_deux_cles_sont_necessaires` | inchangée : `couvert` et `leve` sont la condition d'**inscriptibilité** |
| `l_absence_n_est_jamais_un_verrou` | contenu valide (la preuve établit `leve`), **énoncé périmé** : il conclut sur `bloque` |
| `le_changement_de_mode_ne_leve_pas`, `bloque_temoin_discriminant` | ne valent que pour la **perte de couverture après inscription** (E6) |
| — | **sans théorème** : la trace du refus (`refus_inscription_corpus`), le changement de mode motivé (`motif_changement_mode`), le refus du corpus entier |

PR-56, énoncé sur `leveOpp`, n'est pas touché. `[À L'HORIZON]` Un module d'inscriptibilité (refus, trace, mode motivé) remplacerait la lecture ci-dessus ; il changerait le décompte et n'est pas écrit avant le gel.

---

### §2.2 Ventilation par catégorie ; table nominative R-7

*Règles : NT-ARCH §8ter-bis, R-1 à R-7.*

| Catégorie | N | Contenu |
| --- | --- | --- |
| **Lectures** — dépliages de définitions de bonne formation et du type (R-1 à R-3) | 56 | 55 dépliages témoignés (PR-57 1 : `sans_constat_la_lacune_demeure` ; PR-56 1 : `le_consentement_du_corpus_est_derive` ; PR-55 2 : `corpus_non_consenti_lit_le_mode_de_validation`, `le_changement_de_mode_ne_leve_pas` ; PR-54 (2) : `boucle_confirmante_atteste_l_alignement`, `le_registre_ne_lit_pas_l_hote_reel` ; PR-52 3 : `sans_source_rien_n_est_legitime`, `noncollecte_n_est_jamais_legitime`, témoin `inscriptible_temoin_discriminant` ; `la_souffrance_seule_ne_qualifie_aucune_creance`, lecture de CONV-19, témoin `la_souffrance_n_empeche_pas_la_qualification` · LotL2 4 · PR-10 5, dont `suspension_ne_declenche_aucune_regle`, lecture de CONV-5, témoin `PR10_suspension_temoin_mal_forme` · PR-3 8 · PR-8 5 · PR-15 3 · PR-16 5 · PR-17 3 · PR-18 1 · PR-24 3 · PR-26 2 · PR-27 1 · V1 1 · PR-23 1 `CONV11_complet_satisfait_CONV11` · PR-35 1 `ecriture_duale_ssi_rapprochement_vide` · PR-37 1 `le_milieu_n_ecrit_pas_son_registre` · PR-42 2 `probante_suppose_la_duale`, `entre_lies_sans_tiers_rien_ne_prouve`) ; `inventaire_nonempty_required` (lecture du type) |
| **Lectures de fonctions licites** (R-7) | 125 | table nominative ci-dessous (n° 1 à 125) |
| **Gardes de non-régression déclarées** (R-5) | 3 | `PR12_coincide_avec_la_fiche` (PR-27), `la_machine_d_attribution_ignore_l_extinction` (PR-26) ; `sensJE_ne_produit_pas_la_revision` (sortie constante) |
| **Témoins** de non-vacuité et discriminants (R-2, R-7) | 74 | PR-59 (1) : `controle_temoin` ; PR-58 (1) : `commun_temoin_discriminant` ; PR-57 (1) : `constat_temoin_discriminant` ; PR-56 (2) : `consentement_derive_temoin`, `trace_ou_attestation_temoin` ; PR-55 (2) : `corpus_signal_temoin_discriminant`, `bloque_temoin_discriminant` ; PR-54 (1) : `boucle_temoin_discriminant` ; PR-53 (2) : `filtre_temoin_discriminant`, `deni_presume_temoin` ; PR-52 (2) : `inscriptible_temoin_discriminant`, `la_souffrance_n_empeche_pas_la_qualification` ; 14 témoins de non-vacuité (NT-ARCH §8ter-bis) ; `inventaire_nonempty_discrimine` ; `R1_systemique_ssi_creancier` ; `PR4_temoin_discriminant`, `lien_temoin_discriminant`, `la_lecture_com_temoin_discriminant` (R-7) ;  `confusion_temoin_discriminant`, `ecart_lisible_temoin_discriminant`, `PR9_canalAE_temoin_discriminant` ; PR-23 §6 à PR-50 (25) : `la_dette_de_preservation_est_calculee` ; `ecriture_duale_temoin_discriminant` ; `raccord_temoin`, `coherent_temoin_discriminant` ; `registre_de_milieu_temoin_discriminant`, `un_collectif_peut_tenir_son_propre_registre` ; `etat_temoin_discriminant` ; `statut_temoin_discriminant` ; `arbitrer_temoin_discriminant` ; `probante_temoin_discriminant` ; `instance_commune_temoin_discriminant` ; `l_arbitrage_exige_une_convention`, `au_penal_le_constat_renseigne`, `statut_constat_temoin_discriminant` ; `confronter_temoin_discriminant`, `conforme_temoin_discriminant` ; `la_signature_n_ouvre_pas_la_transaction`, `qualifier_temoin_discriminant` ; `etat18_temoin_discriminant` ; `issue_plainte_temoin_discriminant` ; `conformite_et_realisation_independantes`, `injonction_temoin_discriminant` ; `signal_temoin_discriminant`, `le_signal_depend_de_l_ecart_declare`, `action_temoin_discriminant` ; PR-51 (2) : `carre_temoin_discriminant`, `le_carre_a_un_chemin_admissible` |
| **Témoins et délimitations** (existentiels ; universels à paramètres) | 221 | PR-59 (5) : `pas_d_alerte_sans_seuil_declare`, `non_instruit_n_est_pas_nul`, `un_cycle_ne_suffit_pas`, `meme_ecart_total_droits_differents`, `sans_faisceau_pas_d_alerte` ; PR-58 (6) : `sans_instance_deliberative_pas_de_commun`, `sans_instance_de_controle_pas_de_commun`, `une_indivision_n_est_pas_un_commun`, `une_forme_admise_sans_deliberation_n_est_pas_un_commun`, `la_propriete_seule_n_est_jamais_un_commun`, `l_interet_diffus_se_passe_d_attributaire` ; PR-57 (6) : `non_instruit_ne_vaut_pas_aligne`, `le_porteur_ne_s_atteste_pas`, `sans_les_concernes_pas_de_constat`, `a_qualifier_relance_sans_signal`, `pas_de_relance_sans_constat`, `echeance_sans_concernes_n_ouvre_pas` ; PR-56 (3) : `sans_trace_ni_attestation_pas_d_absence`, `une_contestation_retenue_fait_tomber_la_representation`, `pr56_restreint_pr55` ; PR-55 (2) : `la_representation_ne_couvre_pas_un_joignable`, `les_deux_cles_sont_necessaires` ; PR-54 (3) : `l_effet_d_hote_voit_un_cas_contraire`, `desalignement_sans_hote_temoin`, `un_hote_reel_declare_aucun_echappe` ; PR-53 (5) : `local_mais_structurel_passe`, `non_declare_passe_avec_marqueur`, `documentee_par_la_souffrance_ne_passe_pas`, `la_souffrance_ne_se_confirme_pas_elle_meme`, `ordre_non_respecte_deux_effets` ; PR-52 (1) : `la_source_ne_suffit_pas` ; PR-33, branche 1bis (1) : `l_inscription_dommageable_est_refusee_avant_tout_marqueur` ; PR-31, D7 du 07/10 (3) : `deux_comptabilites_tenues_ancrent_une_duale`, `le_registre_de_communalite_ancre_un_cote`, `un_seul_teneur_pas_de_duale` ; 127 antérieurs, dont 9 existentiels à paramètres parmi les 45 universels longs relus ; 59 instances concrètes de PR-23 §6 et PR-35 à PR-50 (PR-23 1 · PR-35 7 · PR-36 3 · PR-37 5 · PR-38 4 · PR-39 4 · PR-40 3 · PR-41 2 · PR-42 4 · PR-43 4 · PR-44 5 · PR-45 3 · PR-46 5 · PR-47 3 · PR-48 3 · PR-49 2 · PR-50 1), toutes prouvées par `decide` ou `rfl` sur des registres nommés |
| **Résultats** (universels à preuve longue ; résultats courts) | 76 | PR-59 (2, courts) : `l_inclusivite_du_controle_ne_determine_pas_l_interet_commun`, `le_premier_sens_porte_sur_l_attributaire` ; PR-58 (2, courts) : `le_typage_est_necessaire`, `l_interet_commun_ne_determine_pas_l_inclusivite` ; PR-57 (2) : `hypothese_apres_coup_non_admise`, `l_enquete_rend_visible_la_contre_performativite` ; PR-56 (1, long) : `l_absence_opposable_n_est_jamais_un_verrou` ; PR-55 (1, long) : `l_absence_n_est_jamais_un_verrou` ; PR-54 (2) : `hors_hote_la_contre_performativite_est_invisible` (long), `la_contre_performativite_ne_leve_pas_la_boucle` (court) ; PR-53 (4) : `le_filtre_n_ecarte_que_le_declare_incident`, `le_cycle_AJ_termine` (longs), `l_hypothese_seule_ne_qualifie_pas_le_regime`, `declare_et_presume_s_excluent` (courts) ; PR-52 (1, court) : `sur_support_distribue_rien_n_est_inscriptible` ; 44 antérieurs (relecture des 45 universels longs ci-dessous) ; 15 de PR-35 à PR-50 — **8 longs** : `le_rapprochement_resorbe_l_ecart`, `concordante_implique_duale` (PR-35), `coherent_vers_acteur`, `raccord_augmente_duale` (PR-36), `la_consolidation_efface_toujours_la_paire` (PR-38), `l_instance_commune_tranche_toujours` (PR-43), `sans_piece_exterieure_pas_de_foi` (PR-44), `l_etoile_est_toujours_duale` (PR-46) ; **7 courts** : `le_miroir_change_de_role`, `la_ligne_miroir_est_de_role_oppose` (PR-35), `role_miroir`, `une_paire_concordante_s_annule` (PR-38), `plainte_retenue_miroir_force` (PR-48), `signal_implique_non_commutation`, `commutatif_ne_signale_pas` (PR-50) ; PR-51 (2) : `aucune_deliberation_sans_inventaire` (long, induction), `carre_B1B2_commute_sur_les_chemins_admissibles` (court) |
| **Lemmes de construction** | 13 | `compat_financier`, `compat_communalite`, `compat_financier_bis`, `les_deux_temoins_sont_coherents` ;  `le_foldr_max`, `agreger_serieTriviale`, `serieTriviale_est_triviale` ; `filtre_vide_de_tous_faux`, `tous_faux_de_filtre_vide` (PR-35) ; `nat_beq_refl`, `nat_eq_of_beq`, `versActeur_de_ligne`, `aUneLigneVers_iff` (PR-36) |
| **Déclarés, jamais appui seul** (formes 1, alias, instances) | 16 | `V3_commutatif` ; `retiqueter_regime_unchanged`, `V4c_regime_unchanged`, `V4c_actoriel_preserved_alias` ; `fraction_exhibe_sa_source` ; `B1_coherence_condition`, `enumeration_close_exclut_un_collectif`, `seule_l_ouverture_admet_tout_collectif` ; `PR25_n_etablit_aucune_confidentialite` ; `le_couplage_est_un_cycle` ;  `V4c_actoriel_preserved` (forme 1, par cohérence avec son alias) ; `CONV11_complet_retrouve_PR23` (PR-23, compatibilité par construction) ; `ecriture_duale_symetrique` (PR-35, symétrie par construction, déclarée) ; `le_registre_tenu_satisfait_L2` (PR-36, instance de `registre_augmente_coherent`) ; `la_projection_perd_le_fournisseur` (PR-46, invariance d'un champ non touché, forme 1) ; `plainte_fondee_ecart_resorbe` (PR-46, instance de `le_rapprochement_resorbe_l_ecart`) |
| **Architecture** | **584** | = 56 + 125 + 3 + 74 + 221 + 76 + 13 + 16 |
| **Colonne texte** — sonde et PR-29  |  20 | table §8.5.2 d'origine (13) et table en vigueur (2) ; **PR-29 §1-§2 (5)** : fidélité, constat B7, lecture du « + », lacunes, contrepartie conservée |
| **Total ventilé** | **604** = 584 + 20 | égal au décompte de §1. Les trois doublons d'énoncé que les sources de PR-19, PR-22 et PR-24 ne portent plus (fichier d'état, §5) relevaient des témoins et délimitations — celui de PR-19 nommément dans l'instruction du crible R-7, les deux autres `[INFÉRENCE DÉCLARÉE]`. Le témoin de satisfiabilité de `liste_close_exclut_toujours` (PR-16) est `nat_non_enumerable` |

> **Ventilation de PR-23 §6 et PR-35 à PR-50 (152 théorèmes), 2 octobre 2026.** Les lignes n° 86 à 122 de la table R-7 ont leur `example` dans `R7_Controle.lean` (vérifiés le 02/10 par compilation isolée des modules PR-35 à PR-50, qui ne dépendent pas de Mathlib ; rejeu complet : `lake env lean R7_Controle.lean`). Classement par relecture de l'énoncé, de la longueur et de la forme de la preuve, et des docstrings, selon R-1 à R-7. `[À CONTRÔLER]` (1) les 8 nouveaux universels longs ne sont pas entrés dans la relecture « un à un » ci-dessous ; (2) `deux_silences_sont_en_ecriture_duale` (PR-35) et `l_addition_est_possible_mais_non_prescrite` (PR-38), annoncés « garde » dans leur docstring sans la formule de R-5, sont rangés en témoins et délimitations.

**Table nominative R-7.** Pour chaque lecture de fonction licite, le témoin discriminant — une autre entrée pour laquelle la fonction rend une autre valeur. *Nature* : **direct** = le témoin exhibe l'autre valeur de la même fonction ; **indirect** = le témoin l'exhibe par une fonction calculée sur celle-ci, ou par une caractérisation ; **invariance témoignée** = cas (iii) de R-7, le témoin montre que la fonction modifie autre chose. Tous les noms sont contrôlés mécaniquement contre l'audit compilé. **Contrôle mécanique des valeurs** : `R7_Controle.lean` (racine du projet ; `lake env lean R7_Controle.lean`, silence = contrôle passé) établit, pour chacune des lignes et **à partir de la lecture et de son témoin nommés**, que la fonction rend une autre valeur sur l'entrée du témoin — ou, pour une invariance témoignée, qu'elle dépend d'un autre argument ou modifie un autre champ. Les `example` de `R7_Controle.lean` sont hors décompte ; `lake env lean R7_Controle.lean` est silencieux sur la machine du porteur.

| # | Module | Lecture | Fonction lue | Témoin discriminant | Nature |
|---|---|---|---|---|---|
| 1 | PR-11 | `obligation_non_cessible` | appliquer (transfert → none) | `PR11_ne_verifie_pas_la_realisation` | direct |
| 2 | PR-11 | `l_etat_efface_son_origine` | appliquer (disparition, régime libre) | `le_resultat_depend_du_regime` |   invariance témoignée (dépend du régime) |
| 3 | PR-11 | `regime_strict_bloque_a_la_disparition` | appliquer (stricte → none) | `devolution_libre_reconstitue_la_cession` | direct |
| 4 | PR-11 | `PR11_ne_choisit_pas_le_regime` | appliquer (transfert → none, deux régimes) | `PR11_ne_verifie_pas_la_realisation` | direct |
| 5 | PR-11 | `PR11_ne_verifie_pas_la_realisation` | appliquer (réalisation → some) | `obligation_non_cessible` | direct |
| 6 | PR-11 | `PR11_ne_juge_pas_l_obligation` | appliquer (stricte, indépendant de l'obligation) | `PR11_ne_verifie_pas_la_realisation` |   invariance témoignée (dépend de l'événement) |
| 7 | PR-12 | `l_obligation_A2_ne_se_repartit_pas` | appliquer (A2, répartir → none) | `PR12_ne_qualifie_aucune_dette` | direct |
| 8 | PR-12 | `la_charge_A3_ne_se_renouvelle_pas` | appliquer (A3, renouveler → none) | `PR12_ne_qualifie_aucune_dette` | direct |
| 9 | PR-12 | `les_deux_erreurs_sont_symetriques` | appliquer (les deux confusions → none) | `PR12_ne_qualifie_aucune_dette` | direct |
| 10 | PR-12 | `regime_non_declare_ne_vaut_pas_permission` | appliquer (nonDeclare → none) | `PR12_ne_qualifie_aucune_dette` | direct |
| 11 | PR-12 | `sans_resultat_utile_aucune_repartition` | appliquer (A3 sans résultat utile → none) | `PR12_ne_qualifie_aucune_dette` | direct |
| 12 | PR-12 | `sans_mandat_borne_aucune_repartition` | appliquer (A3 sans mandat borné → none) | `PR12_ne_qualifie_aucune_dette` | direct |
| 13 | PR-12 | `le_silence_n_est_pas_une_confusion` | confusionDesDeuxDettes, appliquer (nonDeclare) |   `PR12_ne_qualifie_aucune_dette` ; **`confusion_temoin_discriminant`** |  direct |
| 14 | PR-12 | `PR12_ne_qualifie_aucune_dette` | appliquer (≠ none) | `l_obligation_A2_ne_se_repartit_pas` | direct |
| 15 | PR-12 | `PR12_ne_juge_pas_le_montant` | appliquer (isSome indépendant du montant) | `l_obligation_A2_ne_se_repartit_pas` ; `PR12_ne_qualifie_aucune_dette` |   invariance témoignée (dépend du traitement) |
| 16 | PR-12 | `PR12_ne_hierarchise_pas` | appliquer (A2 répartir = A3 renouveler) | `PR12_ne_qualifie_aucune_dette` | direct |
| 17 | PR-13 | `la_non_equivalence_est_calculee` | nonEquivalentes (niveaux déclarés → some) | `sans_niveau_declare_aucun_verdict` | direct |
| 18 | PR-13 | `sans_niveau_declare_aucun_verdict` | nonEquivalentes (niveau absent → none) | `la_non_equivalence_est_calculee` | direct |
| 19 | PR-13 | `aucune_fusion_entre_niveaux_distincts` | fusionner (niveaux distincts → none) | `PR13_n_interdit_pas_le_meme_niveau` | direct |
| 20 | PR-13 | `niveau_non_declare_ne_vaut_pas_permission` | fusionner (niveau absent à gauche → none) | `PR13_n_interdit_pas_le_meme_niveau` | direct |
| 21 | PR-13 | `niveau_non_declare_a_droite_ne_vaut_pas_permission` | fusionner (niveau absent à droite → none) | `PR13_n_interdit_pas_le_meme_niveau` | direct |
| 22 | PR-13 | `PR13_n_interdit_pas_le_meme_niveau` | fusionner (même niveau → ≠ none) | `aucune_fusion_entre_niveaux_distincts` | direct |
| 23 | PR-13 | `entite_et_territoire_ne_fusionnent_pas` | fusionner (entité / territoire → none) | `la_fusion_au_meme_niveau_somme_les_charges` | direct |
| 24 | PR-13 | `la_fusion_au_meme_niveau_somme_les_charges` | fusionner (même niveau → somme) | `aucune_fusion_entre_niveaux_distincts` | direct |
| 25 | PR-19 | `PR19_ne_touche_pas_l_ecriture_isolee` | conformeSous (écriture isolée triviale → conforme) | `serie_bien_formee_agregat_non_conforme` | direct |
| 26 | PR-20 | `sans_creance_aucun_lien` | lien (sans créance → false) | **`lien_temoin_discriminant`** | direct |
| 27 | PR-20 | `absence_n_est_pas_lien_nul` | registreCommunalite (sans créance → absent) | **`lien_temoin_discriminant`** | direct |
| 28 | PR-20 | `sans_creance_sur_soi_pas_de_lien_a_soi` | lien (a, a sans créance → false) | **`lien_temoin_discriminant`** | direct |
| 29 | PR-20 | `les_deux_registres_augmentes_ont_le_meme_socle` | socle des deux  registres augmentés (égal) | `accord_sur_l_existence_pas_sur_la_valeur` (les registres financiers diffèrent) | invariance témoignée (R-7, 3ᵉ distinction) |
| 30 | PR-23 | `la_glose_ne_rend_rien_lisible` | ecartLisible (ne dépend que du maintien) |   **`ecart_lisible_temoin_discriminant`** |  direct |
| 31 | PR-23 | `priorite_sans_assiette` | prioriteMord (sans maintien → none) | `priorite_mord_si_inscrite` | direct |
| 32 | PR-25 | `la_lecture_com_decide_le_lien` | lectureCom (projection de `compatCom`) | **`la_lecture_com_temoin_discriminant`** | direct |
| 33 | PR-26 | `le_silence_ne_solde_rien` | BienFormee, compteEteinte (nonDeclare) | `seul_debiteur_bien_forme_mais_marque` ; `deux_regimes_divergents_ne_suffisent_pas` | direct |
| 34 | PR-4 | `milieu_degrade_persistant_declenche` | phaseInventaireRequise (→ true) | **`PR4_temoin_discriminant`** (1) | direct |
| 35 | PR-4 | `cloture_interdite_sans_inventaire` | cloturable (→ false) | **`PR4_temoin_discriminant`** (2) | direct |
| 36 | PR-4 | `PR4_les_trois_declencheurs_suffisent_chacun` | phaseInventaireRequise (→ true) | **`PR4_temoin_discriminant`** (1) | direct |
| 37 | PR-4 | `PR4_ne_juge_pas_le_contenu` | cloturable (indépendant du contenu) | `cloture_interdite_sans_inventaire` ; **`PR4_temoin_discriminant`** (2) |   invariance témoignée (dépend de l'inventaire) |
| 38 | PR-5 | `aucun_sens_ne_produit_la_voix` | sensMR, sensRM (champ non touché) | `l_ordre_RM_puis_MR_inscrit_seul` | invariance témoignée (R-7, 3ᵉ distinction) |
| 39 | PR-5 | `aucun_sens_ne_produit_l_audit` | sensMR, sensRM (champ non touché) | `l_ordre_RM_puis_MR_inscrit_seul` | invariance témoignée (R-7, 3ᵉ distinction) |
| 40 | PR-5 | `le_carre_ferme_apres_l_acte` | lever (→ false) | `un_seul_des_deux_actes_ne_ferme_pas` | direct |
| 41 | PR-7 | `F10_ne_certifie_pas_sous_F6_actif` | traiter (certifier sous F6 actif → none) | `F10_reprend_apres_traitement` | direct |
| 42 | PR-7 | `traiter_F6_est_toujours_admis` | traiter (traiter F6 → some) | `F10_ne_certifie_pas_sous_F6_actif` | direct |
| 43 | PR-7 | `F10_reprend_apres_traitement` | traiter (certifier après traitement → some) | `F10_ne_certifie_pas_sous_F6_actif` | direct |
| 44 | PR-7 | `PR7_ne_juge_pas_l_injustice` | traiter (isSome indépendant du contenu) | `F10_ne_certifie_pas_sous_F6_actif` ; `F10_reprend_apres_traitement` |   invariance témoignée (dépend des drapeaux) |
| 45 | PR-7 | `PR7_ne_contraint_pas_hors_coactivation` | traiter (F6 inactif → some) | `F10_ne_certifie_pas_sous_F6_actif` | direct |
| 46 | PR-9 | `un_canal_qui_ne_relit_pas_le_seuil_termine` | Termine (canal sans relecture) | `un_canal_qui_relit_le_seuil_ne_termine_pas` | direct |
| 47 | V3 | `V3_aboutit_deliberation` | chemin_direct (systémique → deliberation) | `V3_actoriel_inchange` (actoriel → i.phase) | direct |
| 48 | V3 | `V3_actoriel_inchange` | chemin_direct, chemin_via_inventaire (actoriel → i.phase) | `V3_aboutit_deliberation` | direct |
| 49 | V4 | `cascade_deliberation_before_critique` | transition_valide (nonAttribuee → critique interdit) | `critique_released_by_porteur` (attribuee → critique valide) | direct |
| 50 | V4 | `critique_released_by_porteur` | transition_valide (enDeliberation / attribuee) | `V4_cascade_coherente` ; l'énoncé porte lui-même les deux valeurs | direct |
| 51 | VJE | `VJE_sensJE_declenche` | appliquerSensJE (→ métalucidité true) | `VJE_sansResistance` | direct |
| 52 | VJE | `VJE_sensEJ_episodique` | appliquerSensEJ (épisodique → true) | `VJE_sensEJ_structurel_bloque` | direct |
| 53 | VJE | `VJE_sensEJ_structurel_bloque` | appliquerSensEJ (structurelle → false) | `VJE_sensEJ_episodique` | direct |
| 54 | VJE | `VJE_ferme_apres_revision_externe` | appliquerSensEJ (après révision) | VJE_sensEJ_structurel_bloque / VJE_sensEJ_episodique ; l'énoncé porte les deux valeurs | direct |
| 55 | VJE | `VJE_sansResistance` | appliquerSensJE (→ métalucidité false) | `VJE_sensJE_declenche` | direct |
| 56 | VJE | `VJE_sansResistance_sourceDID` | appliquerSensJE (→ source none) | `VJE_sensJE_declenche` (source `some did`) | direct |
| 57 | VJE | `VJE_metalucidite_ssi` | appliquerSensJE (caractérisation) | `VJE_sensJE_declenche` ; `VJE_sansResistance` | direct |
| 58 | Interactions | `systemique_sans_creancier_viole_R1` | R1_systemique (sans créancier → False) | **`R1_systemique_ssi_creancier`** | direct |
| 59 | Interactions | `systemique_requires_R1_extension` | R1_systemique (instance sans créancier) | `R1_systemique_ssi_creancier` | direct — spécialisation de n° 58 |
| 60 | PR-11 | `la_devolution_ne_solde_pas` | appliquer (disparition : statut conservé) | `devolution_libre_reconstitue_la_cession` (porteur modifié) | invariance témoignée |
| 61 | PR-16 | `ouverture_n_exclut_personne` | ExercablePar (ouverture → tous) | `liste_close_exclut_toujours` | direct |
| 62 | PR-23 | `priorite_mord_si_inscrite` | prioriteMord (→ some true) | `priorite_sans_assiette` ; `PR23_n_affirme_aucune_dette` (some false) | direct |
| 63 | PR-5 | `PR5_ne_refute_pas_le_couplage` | sensMR (→ précaution true) | `PR5_ne_juge_pas_la_meconnaissance` | direct |
| 64 | PR-5 | `PR5_ne_juge_pas_la_meconnaissance` | sensMR (méconnaissance absente → inchangé) | `PR5_ne_refute_pas_le_couplage` | invariance témoignée |
| 65 | PR-7 | `PR7_ne_touche_pas_au_contenu` | traiter (contenu conservé) | `traiter_F6_est_toujours_admis` (f6Traite modifié) | invariance témoignée |
| 66 | V4 | `V4_cascade_coherente` | transition_valide (nonAttribuee) | `critique_released_by_porteur` | direct |
| 67 | VJE | `VJE_pasDeJE_horsHermeneutique` | appliquerSensJE (hors herméneutique → false) | `VJE_sensJE_declenche` | direct |
| 68 | PR-9 | `PR9_ne_supprime_pas_le_canal_AE` | canalAE (modificateur → résistance true) | **`PR9_canalAE_temoin_discriminant`** | direct |
| 69 | PR-8 | `exactement_deux_regimes_obliges` | RefutationObligatoire (caractérisation sur les quatre légitimités) | `representation_pratique_refutation` (vraie) ; `PR8_ne_vaut_pas_pour_les_legitimites_procedurales` (fausse) | direct |
| 70 | PR-28 | `CONV6_ne_vaut_pas_dans_l_exercice` | SatisfaitCONV6 (horizon institutionnel → satisfaite) | `BienFormee_ne_borne_pas_la_prospective` (non satisfaite) | direct |
| 71 | PR-29 | `trois_livres_sans_tiers_mal_formee` | bienFormeeArite (trois livres, sans tiers → false) | `trois_livres_temoin_discriminant` | direct |
| 72 | PR-30 | `non_determinable_rend_indetermine` | qualifiant (→ indetermine) | `la_branche_B_exclut_le_capital_d_apporteur` (nonQualifie) | direct |
| 73 | PR-30 | `le_non_declare_ne_qualifie_pas_et_marque` | qualifiant, marqueurSansQualification | `qualifiant_temoin_discriminant` | direct |
| 74 | PR-30 | `une_classe_non_repartissable_suffit` | qualifieParClasse (→ true) | `la_qualification_agregee_n_est_pas_la_qualification_par_classe` (false) | direct |
| 75 | PR-30 | `classe_manquante_rend_indetermine` | statutFiducie (→ indetermine) | `la_completude_prime_sur_la_classe_qualifiante` (qualifie) | direct |
| 76 | PR-30 | `citer_ses_regles_n_engage_pas_les_tiers` | engage (non-membre → some false) | `droit_d_ecrire_n_est_pas_pouvoir_d_engager` (membre → some true) | direct |
| 77 | PR-30 | `la_pratique_seule_marque_et_ne_qualifie_pas` | estDPlusDeCommun (→ false) | `droit_d_ecrire_n_est_pas_pouvoir_d_engager` (true) | direct |
| 78 | PR-31 | `sans_ancrage_refusee` | ancree (→ false) | `le_registre_de_communalite_suffit` (true) | direct |
| 79 | PR-31 | `sans_objet_sans_motif_est_un_nondeclare_renomme` | effet (→ refusee) | `G4_n_admet_pas_le_titulaire_non_humain` (G1 → admise) | direct |
| 80 | PR-31 | `le_motif_refute_requalifie` | requalifier | l'énoncé porte lui-même les deux valeurs | direct |
| 81 | PR-31 | `representant_sans_dimension_mal_forme` | bienFormeeP7 (→ false) | `P7_temoin_discriminant` (true) | direct |
| 82 | PR-32 | `regime_sans_refutation_n_autorise_aucune_ecriture` | autoriseEcriture (sans condition de réfutation → false) | `regime_temoin_discriminant` (admis → true) | direct |
| 83 | PR-33 | `sans_branche_pas_de_classement` *(critère)* | classer (aucune branche → E0) | `classement_de_reference` (CONV-8 → E3) | direct |
| 84 | PR-34 | `hote_non_declare_delibere` *(P5)* | effetP5 (hôte non renseigné → E3) | `P5_temoin_discriminant` (triplet complet → none) | direct |
| 85 | PR-34 | `la_voie_intermediaire_ne_dispense_pas_du_triplet` *(P5)* | effetP5 (triplet incomplet → isSome) | `P5_temoin_discriminant` (triplet complet → none) | direct |
| 86 | PR-50 | `seuil_non_declare_ne_signale_pas` *(F3)* | signal (seuil absent → false) ; marqueurSeuilNonDeclare (→ true) | `signal_temoin_discriminant` (seuil 1 → true) | direct |
| 87 | PR-37 | `sans_registre_l_ecart_reste_inscrit` | ecartEnversMilieu (sans registre → lignes vers le milieu) | `registre_de_milieu_temoin_discriminant` (registre arrêté → []) | direct |
| 88 | PR-37 | `la_ratification_ne_fonde_pas_le_registre` | registreOpposable (ratifiée → none) | `ecriture_duale_avec_un_milieu` (arrêtée, bien formée) | indirect |
| 89 | PR-37 | `sans_declaration_pas_de_registre` | registreOpposable (non déclarée → none) | `ecriture_duale_avec_un_milieu` | indirect |
| 90 | PR-37 | `sans_critere_d_inclusion_pas_de_registre` | registreOpposable (inclusion absente → none) | `ecriture_duale_avec_un_milieu` | indirect |
| 91 | PR-37 | `sans_interprete_pas_de_registre` | registreOpposable (interprète absent → none) | `ecriture_duale_avec_un_milieu` | indirect |
| 92 | PR-37 | `sans_interprete_le_marqueur_PR31_se_leve` | marqueurSansInterprete ∘ versInscriptionMilieu (interprète absent → true) | `le_marqueur_de_milieu_se_leve_exactement_sur_l_interprete_manquant` (PR-31 ; interprète renseigné → false) | indirect (caractérisation) |
| 93 | PR-37 | `sans_maintien_pas_d_appui` | registreOpposable (maintien absent → none) | `ecriture_duale_avec_un_milieu` | indirect |
| 94 | PR-37 | `maintien_d_un_autre_registre_pas_d_appui` | registreOpposable (maintien d'un autre registre → none) | `registre_mal_nomme_l_ecart_revient` / `ecriture_duale_avec_un_milieu` | indirect |
| 95 | PR-39 | `sans_constat_rien_n_est_decharge` | resteOuvert (non constaté → dû) | `attendu_n_est_pas_constate` (100 / 40) | direct |
| 96 | PR-39 | `le_constat_ramene_a_la_dette_de_preservation` | resteOuvert (constaté → solde) | `attendu_n_est_pas_constate` (100 / 40) | direct |
| 97 | PR-40 | `la_communication_ne_change_pas_l_ecart` | ecartQualifie (projection sur les lignes = écart) | `statut_temoin_discriminant` (le statut varie) | invariance témoignée |
| 98 | PR-40 | `en_ecriture_duale_rien_a_qualifier` | ecartQualifie (écriture duale → []) | `non_verifiable_n_est_pas_constate` (écart non vide) | direct |
| 99 | PR-41 | `aucun_teneur_ne_tranche` | arbitrer (investigation d'un teneur → nonArbitre) | `arbitrer_temoin_discriminant` | direct |
| 100 | PR-41 | `un_tiers_lie_ne_tranche_pas` | arbitrer (tiers lié → nonArbitre) | `arbitrer_temoin_discriminant` | direct |
| 101 | PR-41 | `l_arbitrage_n_efface_rien` | ecartArbitre (projection sur les lignes = écart) | `le_tiers_tranche_la_contestation` (le statut varie) | invariance témoignée |
| 102 | PR-43 | `sans_instance_commune_rien_n_est_arbitre` | arbitrerInstitue (pas d'instance commune → nonArbitre) | `seule_l_instance_commune_tranche` | direct |
| 103 | PR-43 | `l_instance_liee_n_arbitre_pas` | arbitrerInstitue (tiers lié → nonArbitre) | `seule_l_instance_commune_tranche` | direct |
| 104 | PR-44 | `le_parcours_n_efface_rien` | suivre (champ ligne inchangé) | `statut_constat_temoin_discriminant` (le statut varie) | invariance témoignée |
| 105 | PR-44 | `sans_attestation_rien_n_est_porte` | statutConstat (sans attestation → unilateral) | `statut_constat_temoin_discriminant` | direct |
| 106 | PR-44 | `sans_consentement_la_voie_privee_est_fermee` | saisineRecevable (voie privée sans consentement → false) | `l_arbitrage_exige_une_convention` (avec consentement → true) | direct |
| 107 | PR-44 | `la_voie_publique_ignore_le_refus` | saisineRecevable (voie publique, indépendant du consentement) | `l_arbitrage_exige_une_convention` (voie privée : dépend du consentement) | invariance témoignée |
| 108 | PR-44 | `l_autorite_de_supervision_ne_depend_pas_de_la_societe` | saisineRecevable (autorité de supervision → true) | `sans_consentement_la_voie_privee_est_fermee` (→ false) | direct |
| 109 | PR-45 | `conv17_sans_protocole_hors_protocole` | statut17 (non conforme → horsProtocole) | `chaque_rubrique_compte` (conforme → auNomDuRegistre) | direct |
| 110 | PR-45 | `conv17_n_interdit_pas_de_signaler` | statut17 (membre → signalementIndividuel) | `chaque_rubrique_compte` (registre → auNomDuRegistre) | direct |
| 111 | PR-45 | `conv17_avec_protocole_retrouve_PR44` | statut17 (conforme → auNomDuRegistre (statutConstat …)) | `conforme_temoin_discriminant` / `chaque_rubrique_compte` | direct |
| 112 | PR-45 | `la_reconstitution_suppose_un_detenteur_tiers` | confronter (détenteur = X → nonObtenue) | `confronter_temoin_discriminant` | direct |
| 113 | PR-46 | `directement_lie_pas_de_dette_de_reparation` | qualifier (directement lié, réparation → participationVolontaire) | `qualifier_temoin_discriminant` (cause → dette) | direct |
| 114 | PR-46 | `exiger_n_endette_pas` | qualifier (correction exigée → exigenceDInfluence) | `qualifier_temoin_discriminant` | direct |
| 115 | PR-46 | `la_signature_vaut_consentement_ex_ante` | saisineRecevable ∘ consentPour (arbitrage signé → true) | `la_signature_n_ouvre_pas_la_transaction` (transaction → false) | direct |
| 116 | PR-47 | `sans_site_destination_non_declaree` | etat18 (site absent → destinationNonDeclaree) | `etat18_temoin_discriminant` | direct |
| 117 | PR-47 | `le_lien_retenu_prime` | etat18 (vérification de l'instance → verifie) | `etat18_temoin_discriminant` | direct |
| 118 | PR-48 | `non_fondee_est_une_contestation` | issuePlainte (non fondée, sans tiers → nonArbitree conteste) | `issue_plainte_temoin_discriminant` | direct |
| 119 | PR-48 | `plainte_non_retenue_rien_ne_change` | miroirApres (non retenue → registre inchangé) | `le_miroir_force_sur_l_instance` (retenue → écart résorbé) | direct |
| 120 | PR-49 | `la_conformite_ne_vaut_pas_realisation` | etat (sans constat → attendu, quelle que soit la conformité) | `conformite_et_realisation_independantes` | direct |
| 121 | PR-49 | `sans_mise_en_demeure_irrecevable` | injonctionRecevable (sans mise en demeure → false) | `injonction_temoin_discriminant` | direct |
| 122 | PR-49 | `avant_trois_mois_irrecevable` | injonctionRecevable (2 mois → false) | `injonction_temoin_discriminant` | direct |
| 123 | PR-31 | `ancree_duale_ssi` | ancreeDuale (deux comptabilités → true ; un côté sans ancrage, ou un seul teneur → false) | `deux_comptabilites_tenues_ancrent_une_duale` ; `la_duale_exige_un_ancrage_par_cote` ; `un_seul_teneur_pas_de_duale` | direct |
| 124 | PR-51 | `le_chemin_direct_n_est_pas_admissible` | admissible (chemin direct, inventaire requis → false) | `carre_temoin_discriminant` (sans déclencheur → true) | direct |
| 125 | PR-51 | `entrer_en_deliberation_exige_l_inventaire` | pas (vers la délibération, inventaire requis → seulement depuis l'inventaire) | `carre_temoin_discriminant` | direct |

**Relecture des 45 universels à preuve longue.** Chaque énoncé relu avec sa preuve, contre les formes 1 et 3 et contre R-7.

| Classe | N | Théorèmes |
| --- | --- | --- |
| Résultats confirmés | 21 | `CB3_candidate_not_oplax_monoidal`, `registre_augmente_coherent`, `typage_binaire_apres_prudence`, `porteur_stable_hors_devolution`, `seule_la_realisation_eteint`, `regime_strict_fige_le_porteur`, `traitement_admis_suppose_son_regime`, `le_signal_se_leve_exactement_sur_la_confusion`, `traitement_admis_laisse_la_dette_inchangee`, `fusion_admise_seulement_au_meme_niveau`, `serie_bien_formee_agregat_non_conforme`, `serie_nulle_reste_conforme`, `lien_est_symetrique`, `critique_exige_attribution`, `cloture_declenchee_exhibe_un_inventaire_non_vide`, `la_coactivation_a_un_ordre_unique`, `la_terminaison_se_verifie_sur_le_canal_seul`, `V10a_synthese`, `V1_commute_ssi_coherence`, `nonattribuee_force_deliberation`, `VJE_source_ssi_metalucidite` |
| Témoins et délimitations (existentiels à paramètres) | 9 | `PR10_ne_prouve_pas_la_separabilite`, `champ_declare_peut_mentir`, `le_champ_ajoute_un_degre_de_liberte`, `BienFormee_ne_borne_pas_le_maintien`, `CONV11_est_satisfiable`, `la_glose_varie_librement`, `CONV11_satisfaite_sans_registre_financier`, `PR23_ne_juge_aucun_montant`, `PR23_ne_certifie_pas_le_nommage` |
| Lemmes de construction | 3 | `le_foldr_max`, `agreger_serieTriviale`, `serieTriviale_est_triviale` |
| Lectures de fonctions licites (R-7) | 10 | table, n° 59 à 68 |
| Forme 1 déclarée | 1 | `V4c_actoriel_preserved` — invariance d'un champ non touché, sans témoin, déclarée comme son alias |
| Caractérisation (lecture R-7, n° 69) | 1 | `exactement_deux_regimes_obliges` |

`[LACUNES ET LIMITES]` (1) le contrôle établit l'autre valeur sur **une** entrée de la classe lue, non sur chacune — ce qu'exige R-7, pas davantage ; (2) la classe « résultat » reste un jugement de relecture ; (3) trois lectures relèvent de l'**invariance témoignée** (n° 29, 38, 39).

## §3. Les dix `Classical.choice` — contrôle de référence

**Exactement dix déclarations dépendent de `Classical.choice`, et ce sont exactement celles qui passent par les réels.** Ce nombre est un **contrôle** : toute déclaration nouvelle qui le porterait à onze signale qu'un axiome fort est entré par une porte non voulue.

> **`R1_systemique_ssi_creancier` porte `Classical.choice`, par une porte voulue et identifiée** : le type `SystemicInteraction` en dépend lui-même (champ `amount : ENNReal`, construit sur les réels), si bien que **tout énoncé portant sur ce type en hérite, quelle que soit sa preuve** (`theorem t (d : SystemicInteraction) : d = d := rfl` porte l'axiome). Le critère du contrôle — *exactement celles qui passent par les réels* — tient.

```
systemique_sans_creancier_viole_R1 CB1_in_unit CB1_lax_monoidal
CB2_one CB2_zero R1_preserved_under_CB1
CB3_candidate_not_oplax_monoidal systemique_requires_R1_extension
B1_coherence_condition R1_systemique_ssi_creancier
```

 **Localisation exacte des dix** : `Interactions` (2 — `systemique_sans_creancier_viole_R1`, `R1_systemique_ssi_creancier`), `ChangeOfBase` (4), `V2Verification` (1 — `R1_preserved_under_CB1`), `CB3Attempt` (1), `P2Synthesis` (2 — `systemique_requires_R1_extension`, `B1_coherence_condition`). `BaseCategories` ne contient aucun théorème.

> **Règle des deux portes** — NT-ARCH §8quinquies-ter : `Classical.choice` n'entre que (1) par `simp` sur une égalité propositionnelle de `String`, à éviter, ou (2) par un type construit sur les réels, porte voulue et déclarée ici. Les dix déclarations ci-dessus passent **toutes** par la porte (2). La porte (1) est la cause type d'une alerte du contrôle ; une modification qui remplace une chaîne de caractères dans un témoin est de cette famille et appelle une relecture du contrôle après recompilation.

---

## §4. Ce qui est démontré, et ce qui ne l'est pas

**C'est la section que le set doit citer.**

**Ce qui est démontré au sens formel** — un énoncé, une preuve, un `#print axioms` :

- les **conditions de bonne formation** d'une inscription : ce qu'une écriture doit porter pour qu'une règle ait prise sur elle ;
- les **non-implications** : ce qu'un type, un champ ou une déclaration **ne produit pas** — la classe la plus nombreuse ;
- les **réfutations d'énoncés du set lui-même** : le carré M↔R ne commute pas (PR-5), le couplage E↔A est un cycle **dont les deux ordres diffèrent** (PR-9, `les_deux_ordres_different` ; `le_couplage_est_un_cycle` est une forme 1), le carré J↔E ne se ferme que sur révision inscrite (VJE), la chaîne de PR-4 ne se clôt pas par son type.

**Ce qui n'est pas démontré, et ne doit jamais être écrit comme tel** :

| Énoncé | Statut réel |
| --- | --- |
| Les **obligations** du modèle | **Déclarées** — conventions CONV-1 à CONV-20 (Annexe §A.15). *Une obligation ne se démontre pas, elle se déclare.* CONV-14 est la seule dont **la source** interdit le calcul qu'elle interdit |
| L'**opposabilité** des conventions | **Conférée par une règle de second ordre** — RSO-1 (Annexe §A.16) —, **ni démontrée ni démontrable**, et autofondée `[RAISONNEMENT AUTORÉFÉRENTIEL — déclaré en §A.16.6, non résolu]`. Écrire qu'une convention est « opposable au même titre qu'un théorème » cite RSO-1, non ProfReg |
| Les **axiomes** AX-1 à **AX-17** | **Posés**, six familles (Annexe §A.15.0). AX-1 s'entend au sens de la fiche v2 (liens multifibres / étalés), non « attention finie » ; PAL-1 et PR-24 sont rattachés à AX-1 v2 + AX-10 ; condition de réfutation d'AX-1 v2 en Annexe §A.15.1. AX-11 : *valable sous forme affaiblie* ; AX-12 : *valable sous conditions déclarées* ; AX-7 : *posé — constat daté ; dossier de preuve constitué (pièces détenues), lecture partielle* ; AX-6 : analyse contradictoire non passée (Annexe §A.15.1) |
| Les **six paliers** PAL-1 à PAL-6′ | **Chaînes d'arguments en régime procédural** — aucun n'est un théorème. PR-24 et PR-25 en sont des **appuis**, non des preuves |
| Le **second axe d'extinction** (NT-ARCH §4bis) | **Procédural.** Hors programme de preuve. Il ne casse aucun théorème compilé (**vérifié par recompilation pour V4, PR-3 et PR-11**, NC étant bornée à l'exécution) ; une dette AX-2 ne s'inscrit jamais en `ETEINTE`. **Ses conditions de bonne formation sont formalisées par PR-26** ; la trace et la qualité des interprètes restent procédurales ; la règle « prise contraire d'un concerné → lemme 4 » reste **procédurale, déclarée** |
| La **2-cellule G.9.3** (framed bicategories) | **Hors Mathlib actuel** — horizon v6.x. Écrire « la commutativité de base est prouvée » serait un `[DÉCOUPLAGE DE RÉGIMES]` |
| L'**inexistence d'un foncteur de calcul** V₁→V₃ | **Lacune déclarée.** Ce qui est prouvé est la réfutation d'**un candidat** (`CB3_candidate_not_oplax_monoidal`) |
| V4c (ACT-G2-010) et V10b | **RÉSOLUS PROCÉDURAUX** — invariants vérifiés sur structures d'états ; **V10b ne porte aucun théorème** (la commutation relève de CONV-2) |

> **Le set compte 604 théorèmes (584 d'architecture, 20 de texte) et zéro thèse démontrée.** Les théorèmes établissent **la forme des inscriptions** ; les thèses relèvent des paliers, et les paliers sont procéduraux. **Le set compte en outre une classe de nœuds — les RSO — dont la fonction est précisément de conférer au déclaratif une force que le formel ne lui donne pas.** C'est cohérent avec le régime ; c'est aussi l'endroit où il est le plus exposé.

---

## §5. Correspondance amendements ↔ vérifications

A2+A3 (couplage `appelimmanent`/`puissanceaffirmative`) → **V1**. B1 (`regimeobligation` + `fractionactorielle`) → **V2**, l'obligation de déclaration étant portée par **CONV-1** et `fraction_exhibe_sa_source`. B2 (phase INVENTAIRE-ASSETS-ACTIFS) → **V3** *(commutativité procédurale ; CONV-2 étendue)*. Tension T3 (cascade R-INTERDIT-ABSOLU) → **V4**. AM-G7-08 + AM-ARCH-01 (cohérence planétaire) → **V10a**, l'obligation de représentation prospective étant portée par **PR-8**. ACT-G2-010 → **V4c** *(procédural)*. Carré triangulaire → **V10b** *(procédural)*. AM-G7-04 (carré J↔E) → **VJE**, **conditionné à une révision inscrite**. Amendement A5 des grammaires (découplage M→R, NT-G8 §10.1) → **PR-5** — *à ne pas confondre avec l'axiome AX-5*.

> « A2 », « A3 », « A5 » désignent dans ce paragraphe des **amendements de grammaires**, non les axiomes AX-2, AX-3, AX-5. **L'axiome AX-3** (découplage du sauvetage et de la répartition, règle des avaries communes) a sa fiche au set (Annexe §A.18) et **fonde le retrait du nœud D** (§7), tandis que **l'amendement A3** désigne `puissanceaffirmative`. PR-12 (« non-confusion AX-2 / AX-3 ») porte sur les **dettes** AX-2/AX-3 : lire la déclaration du fichier avant de citer.

---

## §6. Définitions formelles clés

- `R1_actoriel (p) : ∀ a b, p a b = true → p b a = true` ; `R1_systemique (d) : d.creditor ≠ none`.
- `RegimeObligation ::= actoriel | systemique | hybride` ; `PhaseEnquete ::= inscription | obligationSansPorteur | inventaireAssetsActifs | deliberation`.
- `StatutDette ::= attribuee | nonAttribuee | enDeliberation` ; `NiveauRIA ::= deliberation | critique` ; `transition_valide : StatutDette → NiveauRIA → Prop` (interdictions encodées comme `False` littéral) ; `InventaireNonVide := { l : List String // l ≠ [] }`.
 - **L'extinction n'est pas un constructeur de `StatutDette`** et n'en deviendra pas un : c'est un second axe, procédural (NT-ARCH §4bis.2). Un énoncé du set qui la présenterait comme un « cinquième état » de la machine compilée serait un `[CHANGEMENT DE BASE NON TRACÉ]`.
- `HorizonTemporel ::= institutionnel | intergenerationnel | profond | planetaire` ; `LegitimiteRepresentant ::= pratique | deliberative | juridique | planetaireNonDesignee`.
 - **`planetaire` est l'horizon maximal** : un horizon géologique équivaut au planétaire et ne peut le dépasser ; l'EEA des sources de NT-G1 est un agrégat de conditions de sélection passées, non un horizon (Boyer & Petersen 2018, §4.1).
- `ActeurG7G2` porte `seuilEntre : Fin 3` (0 = SENTIENCE, 1 = FINALITEIMMANENTE, 2 = NONDECLARE).
- `RegistreComptableAugmente` : la contrepartie existe dans un registre **si et seulement si** elle existe dans l'autre — et, sur une même écriture, là où le lien existe les deux registres sont pleins, et là où il n'existe pas aucun ne l'est (`registre_augmente_non_equivalence`, témoin avec un lien) ; **la cohérence ne contraint rien d'autre**, et L2 n'a pas de quoi exprimer davantage (CONV-10).
- Convention de nommage : les identifiants conservent la graphie compilée (`valuemetre`…) — table d'équivalence en Annexe méthodologique §A.12.

---

## §7. Le programme de preuve PR-1 → PR-25 — **clos**

| PR | État | Où |
| --- | --- | --- |
| PR-1 | **Instruit et redistribué** — obligation de source : **CONV-4** / `fraction_exhibe_sa_source` ; sanction d'opposabilité : **PR-14** | `LotL2_PR2_PR14.lean` |
| PR-2 | ✓ | `LotL2_PR2_PR14.lean` |
| PR-3 | ✓ | `PR3_AttributionSeuil.lean` |
| PR-4 · PR-5 · PR-6 · PR-7 · PR-9 | ✓ | fichiers propres, sauf **PR-6** versé dans `VJEVerification.lean` |
| PR-8 · PR-10 | ✓ | `PR8_RefutationPratique.lean`, `PR10_StatutSeuil.lean` |
| PR-11 · PR-12 · PR-13 | ✓ | fichiers propres |
| PR-14 · PR-15 · PR-16 · PR-17 · PR-18 · PR-19 | ✓ | fichiers propres |
| PR-20 · PR-21 · PR-22 · PR-23 | ✓ | fichiers propres |
| PR-24 · PR-25 | ✓ | **hors programme** — appuis de paliers (L1, PAL-5) |

**PR-26 à PR-59** formalisent des règles et conventions du set (second axe d'extinction, candidats, ancrages de conventions, table des arités, communalité, effet du défaut, écriture duale entre teneurs et registres de chaîne, signal `carre_non_commutatif`, carré B1↔B2, qualification du régime affectif, canal G-JUSTICE → G-AFFECTIF, boucle confirmante et contre-performativité, CORPUS\_NON\_CONSENTI, consentement par personne et absence opposable, phase RECHERCHE\_INTERVENTION, instances d'un commun et axes séparables, écart par droit et inclusivité par instance — §2) ; ils sont hors du programme PR-1 → PR-25.

**Trois énoncés du programme sont réfutés par leur propre formalisation** — PR-5, PR-9, PR-4 : le set les annonçait dans l'autre sens.

Aucun candidat n'est versé au programme sur le seul motif qu'il serait faisable : *« le dire faisable serait le dire fait »* (décision du porteur sur l'opération instituante). Le lot A-TÉTRA et le second axe d'extinction sont déclarés **hors programme**.

**Hors programme, horizon v6.x** : inexistence complète de CB₃, 2-cellule G.9.3, dérivabilité `obligationpreservation` (nœud D). **Hors programme de preuve** : la tension T4 est une question politique, domiciliée en NT-G12 et NT-G4.

> **Nœud D.** Le retrait du nœud D repose sur l'**axiome AX-3** : fermer le carré rendrait la répartition dérivable de l'agrégation, et c'est le recouplage que AX-3 défait. La fiche d'AX-3 est au set (Annexe §A.18) : **le retrait est contestable sur pièces, sans être validé pour autant.** Ce qui pourra être *prouvé* au nœud D reste commandé par une décision d'horizon v6 : le **produit monoïdal de V₂** (`max` ou `+`, NT-ARCH §2ter.5), versé **comme motif, jamais comme arbitrage**.

---

## §8. Obligations ouvertes qui touchent ProfReg

| Objet | Engage une recompilation ? | Où | Statut |
| --- | --- | --- | --- |
| Produit monoïdal de V₂ (`max` / `+`) | Horizon v6 | NT-ARCH §2ter.5 | OUVERTE — horizon v6 ; trois éléments d'instruction en NT-ARCH §2ter.5 |
| Lacunes de table `E−→C−`, `d→C−` (NT-ARCH §8.5.2) | Selon le cas | NT-ARCH §8.5.2 ; PR-29 | OUVERTES — traitées cas par cas |
| Contrôle des deux points `[À CONTRÔLER]` de la ventilation de PR-23 §6 et PR-35 à PR-50 | Non | §2.2 | OUVERT |

> Le suivi des décisions est tenu au fichier d'état (`_ETAT_INSCRIPTION_v5.7.md`).

---

## [LACUNES ET LIMITES DE CE DOCUMENT]

- **Adossement.** Les décomptes par fichier du §2 sont recomptés mécaniquement sur les sources (29/10/2026, arbre `3a6c9257`, dont les modules sont ceux de l'arbre `68c98f77` ; 73 modules) : ils coïncident tous avec les déclarations `theorem` des modules. Le recompte ne vérifie pas le classement de §2.2, qui reste une lecture.
- **Reproductibilité** : reproductible depuis le set **au gel de version**, par l'instantané daté ; entre deux gels, attestée par journaux d'audit datés. Instantané de l'état de référence déposé le 13/10/2026 (§1.2).
- **Crible de la forme 3 (variante 3b)** passé selon NT-ARCH §8ter-bis R-6 : 41 dépliages, 0 retrait, 14 témoins. **Limites** : crible procédural (extraction scriptée + relecture), non un métaprogramme ; les lectures de fonctions (hors motif ii) ne sont pas criblées.
- **Formes 4 à 7** (NT-ARCH §8ter à §8septies) : sans outil. **Quatre fois sur quatre, les formes non outillées ont été trouvées par accident** (NT-ARCH §8septies) (§2.1). **Aucun crible de péremption d'objet n'existe** : chaque retrait ou scission de champ dans le set peut en produire un nouveau cas dans un témoin compilé. Parade minimale proposée, `[PLAUSIBLE, NON VÉRIFIÉ]` : à chaque retrait ou renommage de champ, rechercher la chaîne dans les `.lean` — ce qui suppose, encore, l'accès aux sources.
- **La forme 8** (engagement sur-revendiqué) porte sur les notes de grammaire ; elle est citée ici parce qu'elle s'applique aussi à **ce que le set écrit de ProfReg** — cf. §0 sur `fraction_exhibe_sa_source`.
- **Responsable ProfReg : Pierre Musseau**, qui **cumule** les fonctions de porteur MRC, de rédacteur et de vérificateur de la compilation. **Horizon** : jusqu'à la production propre d'une **v5.7 publiable (GitHub) et transmissible à des tiers**. **Critère** : chaque passe Lean est compilée sur la machine du responsable et son journal d'audit daté est versé (décompte, `sorryAx`, `Classical.choice`). **Ce que le cumul ne fournit pas** : une vérification par un tiers — PR-16 et PR-18 refusent ailleurs que le déclarant soit seul réfutant. `[À L'HORIZON]` désigner un vérificateur tiers qui rejoue l'instantané de la v5.7.
