# MRC v5.7 — Annexe K : cas d'usage chiffrés (K1 · K2 · K3)

*Fichier du set consolidé MRC v5.7. Régime : vérifiabilité-cohérence.*

> **Provenance et statut.** Ce fichier reprend **tous les cas de l'Annexe K** par conversion mécanique des documents sources (chiffres, tableaux et formulations des originaux, non retraités ; mai 2026) :
> K1 — Exploitation B (CARE / IDEA4) ; K2 — gouvernance d'un LLM (OpenLLM / BentoML ; OpenLLM-France / Lucie-7B) ; K3 — bassin versant en gouvernance multi-acteurs.
> Les opérateurs des cas se lisent selon la table d'équivalence Annexe méthodologique §A.12 (`valuemètre ≡ valorimètre`) et l'articulation aux six phases de C-ENQUETE-V5. Toute divergence entre ce fichier et un document source serait un défaut de conversion à corriger.
> **Ce que ce fichier établit :** des cas d'application chiffrés, en régime procédural. **Ce qu'il n'établit pas :** aucune preuve formelle ; les montants proviennent des sources déclarées dans chaque cas (fiche pédagogique CARE/IDEA4, données GRET, dépôts OpenLLM).

---

# PARTIE K1 — Exploitation B (CARE / IDEA4)

Modèle de Registres de Communalité

Annexe K — Cas d'usage chiffrés

Cas n° 1 : Exploitation B (CARE / IDEA4)

Application de bout en bout de l'architecture du MRC

à un cas chiffré de comptabilité écologique

Pierre Musseau-Milesi

La Coop des Communs

Mai 2026

Statut : document de travail — annexe complémentaire au MRC

## Table des matières

## K.0 Note de présentation

L'Annexe K rassemble des cas d'usage chiffrés du MRC, traités de bout en bout : depuis l'inscription des acteurs en Couche 0 jusqu'aux dispositifs techniques de l'Annexe H, en passant par l'activation des signaux, l'application des règles transversales et l'identification des grammaires mobilisées. Ces cas d'usage répondent à un besoin opérationnel précis : passer d'une architecture conceptuelle à un référentiel concret, partageable avec des praticiens (comptables, financeurs, gestionnaires de communs, juristes, chercheurs en sciences de gestion).

Le présent document inaugure cette annexe par le cas paradigmatique de l'Exploitation B, expérimentée dans le cadre du projet CARE / IDEA4 et documentée dans la fiche pédagogique correspondante. Trois raisons motivent ce choix d'ouverture : (1) le cas est complet — il dispose d'un bilan CARE chiffré et d'un compte de résultat CARE chiffrés ; (2) il combine les quatre modes d'application du MRC (travail, milieu, sémantique, existentiel) ; (3) il a fait l'objet d'une expérimentation publique, ce qui en fait un objet partageable, comparable et discutable.

L'objectif de l'annexe n'est pas de produire une expertise comptable supplémentaire — le cadre CARE et la littérature associée (Richard, Bensadon, Rambaud 2018 ; Rambaud 2019 ; Dumeaux 2025) sont les autorités scientifiques sur ce point. L'objectif est de montrer comment l'architecture du MRC permet de lire ce cas en explicitant ses choix architecturaux, ses signaux, ses dispositifs techniques nécessaires et ses points de tension restants. À ce titre, le présent document est aussi un test de l'architecture : il s'agit de vérifier qu'elle tient sur un cas réel, et d'identifier les ajustements éventuels qu'elle appelle (pistes signalées en synthèse).

Sources mobilisées : fiche pédagogique CARE / IDEA4 « Exploitation B » ; Richard J., Bensadon D., Rambaud A. (2018) Comptabilité financière (10ᵉ édition) ; Dumeaux L. (2025) Thèse Paris Dauphine — Juste prix écologique et double affichage ; note synthétique MRC × CARE × comptabilité financière (mai 2026).

## K.1 Présentation du cas — Exploitation B

### K.1.1 Profil de l'exploitation

L'Exploitation B est une exploitation agricole mixte (cultures et élevage) située en France métropolitaine. Elle a fait l'objet d'une expérimentation CARE dans le cadre du projet IDEA4 (Indicateurs de Durabilité des Exploitations Agricoles, version 4). L'expérimentation a consisté à doubler la comptabilité financière classique de l'exploitation par une comptabilité CARE étendue aux capitaux naturels (sol, biodiversité, eau, atmosphère, troupeau) et humains (capital humain des salariés et de l'exploitant, capital sociétal local, capital patrimonial).

Le présent cas d'usage retient cette exploitation comme objet de test du MRC parce qu'elle articule, dans une même entité, quatre des cinq tensions que le modèle cherche à gouverner : prélèvement / restauration sur un milieu (modes milieu), exploitation / qualité du travail (mode travail), classification / représentation comptable (mode sémantique), engagement de long terme sur la fertilité (mode existentiel). Seul le cinquième mode — le mode mimétique girardien — n'apparaît pas dans le cas tel que documenté, ce qui ne signifie pas qu'il y soit absent ; le commentaire de synthèse y reviendra.

### K.1.2 Données chiffrées de référence

Le bilan CARE et le compte de résultat CARE de l'Exploitation B fournissent les chiffres suivants (source : fiche pédagogique CARE / IDEA4).

#### Bilan CARE — Actifs

| Catégorie d'actifs | Brut (€) | Amortissements (€) | Net (€) |
|---|---|---|---|
| Actifs financiers (terrains, bâtiments, matériel, stocks, créances) | 1 143 862,0 | 644 081,0 | 499 780,0 |
| Actifs naturels (sol, biodiversité, eau, atmosphère, troupeau) | 62 828,9 | 53 869,7 | 8 959,2 |
| Actifs humains (capital humain salariés + exploitant, capital sociétal, patrimonial) | 3 079 710,5 | 157 785,5 | 2 921 925,0 |
| Total actifs | 4 286 401,4 | 855 736,2 | 3 430 664,2 |

#### Bilan CARE — Passifs (synthèse)

| Catégorie de passifs | Montant fin d'année (€) | Commentaire |
|---|---|---|
| Capitaux propres financiers | ≈ 487 215 | Capital, réserves, résultat de l'exercice |
| Dettes financières (banque, fournisseurs) | ≈ 23 159 | Court et long terme financiers |
| Dettes naturelles | 10 605,9 | Dettes envers sol, biodiversité, eau, atmosphère, troupeau |
| Dettes humaines | 2 952 930,0 | Dont salaires décents long terme : 2 901 312 ; santé-sécurité ; capital sociétal ; capital patrimonial |
| Total passifs | ≈ 3 473 910 | Équilibre avec les actifs nets |

#### Compte de résultat — Comparaison classique / CARE

| Indicateur | Comptabilité classique (€) | Comptabilité CARE (€) | Écart (€) |
|---|---|---|---|
| Résultat net de l'exercice | 101 859,0 | 69 207,3 | − 32 651,7 |
| Coûts de préservation comptabilisés en charges CARE | 0 | ≈ 32 651,7 | + 32 651,7 |

L'écart de 32 651,70 € entre résultat classique et résultat CARE matérialise les coûts de préservation que la comptabilité classique invisibilisait. Dans le cadre du MRC, cet écart est un valuemètre composite qui exprime, en unité monétaire, la dette envers les capitaux NH non remboursée pendant l'exercice. La règle R-MEMOIRE (Couche 1) ferait inscription obligatoire de cette dette si elle restait active sur 2 cycles sans action documentée.

## K.2 Lecture Couche 0 — Primitives constitutives instanciées

Conformément à la Couche 0 du MRC (corps principal §4.1 et Annexe G.6.1), tout cas d'usage doit commencer par l'identification des acteurs, du choix de la catégorie de base, du régime d'inscription et des niveaux d'explication mobilisés. Pour l'Exploitation B, cette identification produit le diagramme suivant.

### K.2.1 Acteurs — proposition de DIDs

Chaque acteur du cas — humain, organisationnel, non-humain ou instrumental — reçoit un identifiant décentralisé (DID) conformément à l'Annexe H.1. Les DIDs proposés ci-dessous sont des modèles ; leur instanciation effective relève de la gouvernance du registre.

| Type d'acteur | Acteurs du cas | DID proposé | Statut |
|---|---|---|---|
| Personnes physiques | Exploitant + 1 salarié à temps plein + 1 saisonnier | did:registre:person:exploitB:exploitant ; …:salarie01 ; …:saison01 | Auto-souverain |
| Organisations | Banque, OPCO agricole , Chambre d'agriculture, État (PAC), AOC / coopérative locale | did:registre:org:banque-x ; …:opco-agri ; …:cha-dep ; …:etat-pac ; …:coop-loc | Gouvernance interne |
| Communs écologiques (acteurs non-humains) | Sol agricole, biodiversité parcellaire, ressource en eau, atmosphère, troupeau | did:registre:milieu:sol-exploitB ; …:biodiv-exploitB ; …:eau-exploitB ; …:atmo ; …:troupeau | Consortium gouvernance (Chambre + Agence eau + assos) |
| Communs professionnels et humains | Bassin d'emploi agricole local, métier agriculteur (genre professionnel) | did:registre:travail:bassin-emploi-X ; …:genre:agriculteur-NUTS | Consortium OPCO + Région + branches |
| Communs sémantiques | Référentiel IDEA4, corpus CARE local, catégories de valuation | did:registre:corpus:idea4-v4 ; …:corpus:care-exploitB | Communauté scientifique + co-construction |
| Instruments de mesure | Indicateurs IDEA4 (53 indicateurs), valuemètre coûts de préservation, dMRV pédologique | did:registre:valuemetre:idea4 ; …:valuemetre:cout-pres-exploitB ; …:capteur:sol-pedo01 | Opérateur scientifique + VC de conformité |

### K.2.2 Catégorie de base — V^CARE composite

Le cas d'usage instancie un enrichissement composite de la catégorie de base, qui dépasse les V monoïdaux usuels de l'Annexe G.2.2. Conformément à la lecture proposée dans le document de synthèse MRC × CARE, la catégorie de base mobilisée est :

V^CARE = 𝟤 × E × N × C

où 𝟤 = {0, 1} capture la présence / absence d'une dépendance ; E est l'ensemble des types d'évaluation (coût historique, juste valeur, coût de préservation, indicateur biophysique, indicateur qualitatif) ; N est l'ensemble des natures comptables (charge, produit, actif, passif, hors-bilan) ; C est l'ensemble des profils de capital protégé (financier seul ; financier + NH ; NH seul). Le produit cartésien est muni de la structure monoïdale terme à terme. Cette construction est un cas paradigmatique d'enrichissement composite, dont l'Annexe G.9 (envisagée en synthèse) formaliserait la théorie générale.

Conséquence opérationnelle : chaque écriture du registre Exploitation B est typée par un quadruplet (présence, évaluation, nature, capital). Le passage d'une comptabilité classique (où C est réduit au capital financier) à une comptabilité CARE (où C inclut les capitaux NH) est un foncteur de changement de base ι : V^IFRS ↪ V^CARE, dont l'inverse — la projection π : V^CARE → V^IFRS qui efface les capitaux NH — n'admet pas d'inverse à droite informationnel. C'est l'instance paradigmatique du signal irreversibilite_changement_base (Annexe G.7) : passer du CARE à l'IFRS perd définitivement l'information sur les capitaux NH ; le retour exige une réinscription depuis les sources primaires.

### K.2.3 Régime d'inscription mobilisé

L'expérimentation CARE / IDEA4 sur l'Exploitation B mobilise une combinaison régimée des trois régimes d'inscription définis en Couche 0 : ENQUETE_OBSERVATIONNELLE pour la mesure des flux biophysiques (indicateurs IDEA4 calculés à partir des données d'exploitation) ; ENQUETE_COLLECTIVE pour la co-construction des seuils de préservation et l'interprétation des écarts avec l'exploitant et les chercheurs ; AUTOGOUVERNANCE pour la décision de pousser ou non l'inscription en comptabilité financière publiée. Cette combinaison régimée — typique de la recherche-intervention — confirme la Piste 6 identifiée en analyse critique.

### K.2.4 Niveaux d'explication

Le cas mobilise les trois niveaux d'explication (PROXIMATE, ULTIMATE, DUAL) de la Couche 0 selon la dimension considérée : le calcul des indicateurs IDEA4 est PROXIMATE (mécanismes biophysiques mesurables) ; le statut de l'agriculteur comme acteur de gouvernance du sol est ULTIMATE (le sens long-terme du métier comme commun) ; le passage d'un résultat classique de 101 859 € à un résultat CARE de 69 207,30 € est DUAL — il combine la mesure proximate (coûts de préservation calculés) et le sens ultimate (responsabilité jonasienne envers la fertilité). Cette articulation est tracée en sous-couche C-PSYCHOLOGIE-PROXIMATE (Fiche 5) au niveau de la grammaire transversale Évolutivité cognitive.

## K.3 Lecture Couche 1 — Dualité des régimes et signaux

### K.3.1 Régime métabolique

Le régime métabolique de l'Exploitation B est constitué de l'ensemble des opérations productives qui prélèvent, consomment et transforment des ressources : labours, fertilisations, traitements phytosanitaires, abreuvement et alimentation du troupeau, ventes de produits agricoles et d'élevage, paiements de salaires et de charges. Ce régime se traduit, dans la comptabilité financière classique, par un chiffre d'affaires et une marge brute, et dans la comptabilité CARE, par une marge brute corrigée par les coûts de préservation effectifs.

### K.3.2 Régime attentionnel

Le régime attentionnel est constitué des dispositifs qui mesurent, cartographient et soignent ce que le régime métabolique mobilise. Pour l'Exploitation B, il combine : (a) les 53 indicateurs IDEA4 (couverture pédologique, taux de matière organique, diversité spécifique, balance azotée, etc.) qui mesurent l'état des capitaux naturels ; (b) les indicateurs sociaux (taux de couverture des salaires décents, accidents du travail, formations suivies) qui mesurent l'état des capitaux humains ; (c) les budgets prévisionnels de préservation (semis de couverts, plantations de haies, formations professionnelles, mises aux normes santé-sécurité) ; (d) les budgets réalisés ; (e) les écarts prévisionnels / réalisés qui constituent les charges CARE.

### K.3.3 R-COUPLAGE — calcul de la 2-cellule

Conformément à la formulation unifiée (corps principal §2.4 et Annexe G.6.2), R-COUPLAGE est ici l'exigence d'une 2-cellule reliant le profunctor métabolique M_méta : Acteurs × Opérations → V^CARE (qui inscrit les prélèvements et les ventes) et le profunctor attentionnel M_att : Acteurs × Indicateurs → V^CARE (qui inscrit les états des capitaux NH et humains). La 2-cellule de cohérence se calcule par confrontation des deux profunctors : pour chaque acteur non-humain (sol, eau, biodiversité, troupeau), la dette inscrite côté passif doit correspondre à la trajectoire mesurée côté indicateurs. L'écart non compensé (32 651,70 € sur l'exercice) est exactement le défaut de commutativité de cette 2-cellule. Il ne franchit pas le seuil critique (qui déclencherait un signal carre_non_commutatif au niveau ÉLEVÉ), mais il franchit le seuil de signalement MOYEN — d'où l'obligation d'inscription en charges CARE et l'ouverture d'une phase RÉVISION dans C-ENQUETE-V5 pour le prochain exercice.

### K.3.4 R1 — Convention DÉBIT / CRÉDIT généralisée

La convention R1 est instanciée systématiquement sur le cas. Trois exemples paradigmatiques :

Mise en culture d'une parcelle — DÉBIT du compte « actifs naturels — sol » (au titre de l'usage productif) ; CRÉDIT du compte « dettes naturelles — sol » (au titre de l'obligation de restauration). La dette est amortie au fur et à mesure des opérations de soin effectivement réalisées (semis de couverts, fertilisation organique, rotation).

Emploi d'un salarié — DÉBIT du compte « actifs humains — capital humain salarié » (au titre de la mobilisation des compétences) ; CRÉDIT du compte « dettes humaines — salaires décents long terme » (au titre de l'obligation de rémunération décente sur l'ensemble de la carrière, soit 2 901 312 € pour le salarié temps plein). La dette est amortie année par année.

Distribution d'un dividende ou rémunération de l'exploitant — soumise à la règle de Couche 1 R-PRIORITE-CREANCIERS (Piste 3 de l'analyse critique) : pas de distribution avant remboursement des dettes NH. Le cas Exploitation B en révèle le besoin opérationnel.

### K.3.5 C-SIGNAL — signaux activés sur le cas

| Signal | Activé ? | Niveau | Motif |
|---|---|---|---|
| signal_ecologie_superficielle | Partiellement | MOYEN | R-COUPLAGE non bloquant ; écart 32 651,70 € sur l'exercice |
| R-CARE_chronique | À tester | MOYEN | Dépend de la trajectoire pluri-annuelle de appel_entendu sur le sol et le troupeau |
| parite_participation_false `[RENOMMÉ LE 13/10/2026 — ex-parite_deliberative_false ; champ unique `parite_participation`, propriétaire NT-G7]` | Partiellement | MOYEN | Levé pour le saisonnier : `parite_participation` = FAUX dans le périmètre documenté, faute de lexique accessible (injustice herméneutique, cf. §K.5.4). L'exploitant participe à la co-construction des seuils ; les autres acteurs NH sont représentés par consortium `[CORRIGÉ LE 13/10/2026 — décision n° 53 : la table portait « Non / — », en contradiction avec §K.5.4 et §K.9.3 (a) ; [INCOHÉRENCE INTER-COUCHES] levée]` |
| appel_entendu_systemique | Non | — | Les dispositifs IDEA4 sont effectivement écoutés et provoquent des décisions |
| carre_non_commutatif | Non bloquant | MOYEN | Défaut de commutativité < seuil critique |
| irreversibilite_changement_base | Latent | ÉLEVÉ | Si la comptabilité financière publiée évince les capitaux NH (π : V^CARE → V^IFRS) |
| codegradation_calculable | À tester | MOYEN | Travail × Milieu : la pression économique sur l'exploitant peut dégrader simultanément ses conditions et le milieu |
| focalisation_victimaire | À tester | MOYEN | L'élevage comme catégorie peut être désigné bouc émissaire dans le débat public — F7 vigilante |

### K.3.6 C-MEMOIRE-PERTES et R-MEMOIRE

L'écart de 32 651,70 € entre résultat classique et résultat CARE n'est pas une « perte » au sens de C-MEMOIRE-PERTES tant qu'il est inscrit dans le résultat CARE et soumis à plan de rattrapage. Il deviendrait une perte enregistrée par R-MEMOIRE si la trajectoire pluri-annuelle montrait une non-réduction de l'écart sur 2 cycles consécutifs — auquel cas la trajectoire de dégradation des sols et de la biodiversité (mesurée par les indicateurs IDEA4) serait inscrite en C-MEMOIRE-PERTES avec champ irreversibilite_confirmee à VRAI ou FAUX selon les analyses biophysiques.

### K.3.7 appel_entendu — champ éthique du régime attentionnel

`[Règle de migration NT-G5 §3.1. Capitaux naturels : `appel_entendu_milieu = ENTENDU`, `interprete_appel` = l'exploitant, d'après le texte ci-dessous. Capitaux humains : `[APPEL HORS MILIEU — AUCUN CHAMP]` — l'appel des capitaux humains n'a pas de champ dans le set.]` Le champ appel_entendu est ici instancié à VRAI pour les capitaux naturels (l'exploitant ajuste effectivement ses pratiques en fonction des indicateurs IDEA4) et à VRAI pour les capitaux humains (formations effectivement suivies, ajustements de santé-sécurité réalisés). Ce statut positif est obtenu par la pratique de co-construction des seuils, qui rend l'appel des capitaux NH lisible au-delà des seules métriques instrumentales. Il faut noter, pour ne pas céder à la naïveté méthodologique, que appel_entendu = VRAI ne signifie pas appel_immanent = entièrement satisfait (cf. Fiche 4 sur la distinction jonasienne) : la fertilité du sol et la biodiversité parcellaire peuvent continuer à se dégrader malgré l'écoute, et c'est précisément ce que les amortissements naturels (53 869,7 €) inscrivent.

## K.4 Lecture Couche 2 — Modes d'application instanciés

### K.4.1 Mode milieu (Fiche 2) — sol, biodiversité, eau, atmosphère, troupeau

Le mode milieu est instancié par cinq acteurs non-humains aux capitaux naturels bruts de 62 828,9 € (sol majoritaire, complété par biodiversité, eau, atmosphère, troupeau). La sous-couche C-MILIEU-VECU est renseignée comme suit :

| Champ C-MILIEU-VECU (Fiche 2) | Valeur Exploitation B |
|---|---|
| etat_habitabilite_milieu | FRAGILE — net naturel à 8 959,2 € sur 62 828,9 € de brut traduit un taux d'amortissement de 86 %, signal d'usure prononcée |
| texture_vecue | Sols moyennement portants, taux de matière organique en stagnation, biodiversité parcellaire stable mais fragilisée par drainage historique |
| indicateurs_biophysiques | Les 53 indicateurs IDEA4 (volet écologique) — DIDs des indicateurs liés au DID du milieu |
| seuil_alerte_milieu | Variable selon l'indicateur ; alerte composite à 0,3 sur indice IDEA4 agrégé |
| obligation_preservation | Maintien du taux de matière organique ; plantation de haies ; rotation longue ; réduction des intrants chimiques |
| milieu_uri | did:registre:milieu:sol-exploitB (consortium Chambre + Agence de l'eau + association environnementale) |

R-CARE (4 défis branche non-humain) est instanciée :

Défi 1 — Inventaire : les acteurs non-humains rendus visibles sont effectivement inscrits dans la fiche pédagogique (sol, biodiversité, eau, atmosphère, troupeau).

Défi 2 — Opérations : type_operation_care_milieu = RESTAURATION (semis de couverts, plantations de haies) et SURVEILLANCE (indicateurs IDEA4) ; PROTECTION ponctuelle (réduction des intrants).

Défi 3 — Coûts : cout_care_milieu = 32 651,70 € sur l'exercice (charges CARE), valuemètre BIOPHYSIQUE composite.

Défi 4 — Attribution : defi_attribution_milieu = exploitant (DID) sur le périmètre opérationnel, consortium de gouvernance sur le périmètre stratégique.

Signal composite R-CODEGRADATION : la confrontation Fiche 2 (mode milieu, état FRAGILE) × Fiche 1 (mode travail, à examiner) permet d'évaluer une éventuelle codégradation. Pour l'Exploitation B, l'analyse Dumeaux suggère que la pression économique sur la marge agricole pousse à simultanément intensifier les pratiques (dégradation milieu) et précariser la main-d'œuvre (dégradation travail). Le 2-morphisme M-TRAVAIL → M-MILIEU est non nul ; codegradation_calculable est positif au niveau MOYEN.

### K.4.2 Mode travail (Fiche 1) — exploitant et salariés

Le mode travail est instancié par les 3 personnes physiques (exploitant temps plein, 1 salarié temps plein, 1 saisonnier) et par le genre professionnel « agriculteur en exploitation mixte de polyculture-élevage ». Les capitaux humains bruts (3 079 710,5 €) sont massivement composés du capital humain à long terme : 2 901 312 € de salaires décents au passif, qui matérialise l'engagement de rémunération décente sur l'ensemble des carrières mobilisées.

La sous-couche C-DPQT (Dispositif de Promotion de la Qualité du Travail) est instanciée comme suit :

| Champ C-DPQT (Fiche 1) | Valeur Exploitation B |
|---|---|
| type_deliberation | DISPUTE_MANIERE_FAIRE (sur l'intensité des rotations) + REDEFINITION_BUTS partielle (intégrer les indicateurs IDEA4 dans la conduite d'exploitation) |
| frontiere_metier | Agriculteur en polyculture-élevage durable |
| profondeur_justice | INTERMEDIAIRE — l'exploitant est juge légitime ; le salarié dispose d'une parole ; le saisonnier moins |
| salarie_comme_juge | VRAI pour le salarié temps plein ; à confirmer pour le saisonnier |
| acteurs_deliberation | DIDs des 3 personnes + DID coopérative + DID chambre d'agriculture |
| dispositif_soutien | Comité de pilotage CARE / IDEA4 ; supervision par chercheurs |

Sous-couche C-COMMUNALITE-TRAVAIL : type_equilibre = EN_TRANSITION (passage d'une exploitation classique à une exploitation CARE). Le commun de capabilités (savoir-faire de polyculture-élevage durable) est en activation. Le champ COMMUN_GOUVERNE_FRAGILE est à VRAI au niveau du bassin d'emploi (la transmission du métier d'agriculteur est fragile) mais FAUX au niveau de l'exploitation elle-même.

### K.4.3 Mode sémantique (Fiche 3) — référentiel IDEA4 et corpus CARE

Le mode sémantique est instancié non par des tokens linguistiques ordinaires mais par les catégories comptables et écologiques mobilisées : « capital naturel », « dette naturelle », « coût de préservation », « capital humain », « salaire décent à long terme », « habitabilité du milieu ». Le corpus de référence est le référentiel IDEA4 et la fiche pédagogique CARE / IDEA4 sur l'Exploitation B.

La sous-couche C-INSCRIPTION-CORPUS est instanciée :

| Champ C-INSCRIPTION-CORPUS (Fiche 3) | Valeur Exploitation B |
|---|---|
| regime_inscription_corpus | ENQUETE_COLLECTIVE (co-construction avec exploitant + chercheurs + indicateurs scientifiques) |
| consentement_explicitation_corpus | VRAI — attesté par VC (Annexe H.2) |
| mode_validation_concept | CONSENSUEL pour les catégories CARE générales ; CONTESTE pour le périmètre de certains amortissements naturels (la valeur économique d'une haie) |
| contestation_possible_corpus | VRAI |
| etres_rendus_visibles_semantique | Sol, biodiversité, eau, atmosphère, troupeau, capital sociétal — tous deviennent visibles par leurs catégories CARE |
| acteurs_exclus_conception_semantique | Saisonnier (consentement partiel à la conception du référentiel local) ; riverains (non consultés sur les seuils) |
| solidite_politique | 3 / 5 — solidité scientifique forte, reconnaissance institutionnelle moyenne, débat public limité |

Sous-couche C-2MORPHISME-INTER-CORPUS (Annexe G.3) : un 2-morphisme entre le corpus IDEA4 (national, scientifique) et le corpus CARE local (exploitation) est inscrit ; son amplitude mesure la traduction nécessaire pour passer des indicateurs génériques aux indicateurs adaptés au cas. L'amplitude est non nulle mais non bloquante. Le corpus local enrichit le corpus national d'observations situées (texture_vecue spécifique à l'Exploitation B).

Signal carre_non_commutatif sur le mode sémantique : le 2-morphisme entre la catégorie « actif naturel » de la comptabilité financière (vide ou réduite au coût historique du terrain) et la catégorie « actif naturel » de la comptabilité CARE (sol + biodiversité + eau + atmosphère + troupeau, avec amortissements et dettes) est éminemment non commutatif. C'est précisément cette non-commutativité qui justifie l'expérimentation CARE.

### K.4.4 Mode existentiel (Fiche 4) — fertilité, biodiversité, conditions de vie

Le mode existentiel est instancié par les enjeux de long terme attachés au cas : préservation de la fertilité du sol sur des horizons multi-générationnels, maintien de la biodiversité parcellaire dans un paysage agricole, contribution à la qualité de l'eau pour les usagers en aval, neutralité carbone à l'horizon planétaire. Pour chacun de ces enjeux, la sous-couche C-INDEXATION-HORIZON (Annexe G.4) inscrit les horizons concernés et les catégories de base propres à chaque horizon.

| Enjeu existentiel | Horizon h (catégorie ordonnée H) | Catégorie de base V_h | Effondrement calculable ? |
|---|---|---|---|
| Fertilité du sol | INTERGENERATIONNEL (3 générations) → PROFOND (200 ans) | [0, 1] (qualité agronomique) → ℝ_≥0 (dégradation) | Non — la trajectoire est récupérable par changement de pratiques |
| Biodiversité parcellaire | INSTITUTIONNEL (10 ans) → INTERGENERATIONNEL | 𝟤 (présence d'espèces clés) | Latent — la perte d'une espèce clé est irréversible |
| Qualité de l'eau (nappes) | INTERGENERATIONNEL (50 ans) → PROFOND | [0, 1] (qualité) → ℝ_≥0 (charge polluante) | Non sur le périmètre de l'exploitation ; latent au niveau du bassin |
| Stabilité climatique | PLANETAIRE (10 000 ans+) | Bicatégoriel — au-delà de l'horizon, V_h ne contient plus l'exploitation comme acteur | OUI à l'horizon PLANETAIRE — R-INTERDIT-ABSOLU déclenchable formellement (Annexe G.5) |

Sous-couche C-FINALITE-IMMANENTE (Fiche 4) : la finalité_immanente du sol est l'« intégrité agronomique et écologique » ; type_finalite = AUTOCONSERVATION + DEVELOPPEMENT (le sol vivant développe sa propre fertilité par interaction avec sa microflore et sa microfaune). Le champ obligation_sans_reciprocite est à VRAI : l'obligation envers le sol existe sans attendre de réciprocité contractuelle. La distinction_appel_entendu est à VRAI : appel_immanent (intégrité du sol) ≠ appel_entendu (mesure IDEA4) — l'exploitant peut entendre l'appel via l'indicateur sans pour autant satisfaire la finalité immanente.

Sous-couche C-SUJET-COLLECTIF (Fiche 4) : niveau_responsabilite = COLLECTIF (exploitant + consortium gouvernance) sur les horizons INSTITUTIONNEL et INTERGENERATIONNEL ; ESPECE sur l'horizon PLANETAIRE. mecanisme_porteur = traité de l'eau (bassin) ; politique agricole commune (UE) ; engagements climatiques nationaux. principe_precaution_asymetrique = VRAI pour les décisions à effet sur la biodiversité (perte irréversible d'espèces).

## K.5 Lecture Couche 3 — Grammaires transversales mobilisées

### K.5.1 G-RESPONSABILITE (Jonas) — les capitaux NH comme créanciers

La grammaire jonasienne est l'arrière-plan implicite de l'ensemble du dispositif CARE : ce qui rend la comptabilité étendue intelligible, c'est la reconnaissance d'une responsabilité asymétrique envers ce qui ne peut pas porter plainte (le sol, la biodiversité, les générations futures). Le bilan CARE de l'Exploitation B opérationnalise cette grammaire en inscrivant les capitaux NH comme créanciers — dotés de dettes (10 605,9 € pour les dettes naturelles, 2 952 930 € pour les dettes humaines) que l'entité doit honorer.

L'articulation à l'Annexe G est précise : pour la stabilité climatique (horizon PLANETAIRE), le foncteur de changement de base φ entre l'horizon actuel et l'horizon planétaire perd l'exploitation comme acteur (au-delà de ~10 000 ans, l'entité économique « exploitation B » n'existe plus dans V_h). C'est l'irréversibilité formelle au sens G.5 ; R-INTERDIT-ABSOLU s'appliquerait à toute décision qui aggraverait significativement le bilan carbone planétaire de l'exploitation. Le cas Exploitation B ne déclenche pas cette règle (les pratiques observées n'ont pas d'effet planétaire majeur isolé), mais la possibilité d'une déclenchement par sommation à l'échelle du secteur agricole reste un enjeu de gouvernance.

### K.5.2 G-SOIN — care du sol, du troupeau, des salariés

La grammaire G-SOIN (Tronto, Plumwood, Haraway) éclaire la dimension reproductive du dispositif : ce que l'exploitant fait pour maintenir la fertilité, ce qu'il fait pour le bien-être animal, ce qu'il fait pour les compétences des salariés — toutes ces opérations sont du care, et toutes sont rendues visibles par la comptabilité CARE qui leur attribue un coût explicite. La grammaire signale un point d'attention : le care invisibilisé du conjoint d'exploitant (souvent une femme) reste sous-représenté dans le cas tel que documenté ; c'est un angle mort que la généralisation du modèle devra corriger.

### K.5.3 G-COMMUNALITE — faisceaux de droits Schlager-Ostrom

L'application de la grille C-DROITS (cinq droits Schlager-Ostrom) au cas Exploitation B révèle des configurations contrastées :

| Entité (DID) | Acces | Prelevement | Gestion | Exclusion | Alienation | Degré de communalité |
|---|---|---|---|---|---|---|
| Sol agricole | Détenu (exploitant) | Détenu | Partagé (PAC, AOC) | Détenu | Détenu (vente possible) | FAIBLE — propriété privée dominante |
| Ressource en eau | Partagé (Agence) | Partagé (autorisation) | Partagé (consortium) | Partagé | Absent | MOYEN |
| Biodiversité parcellaire | Détenu (exploitant) | Détenu | Partagé (réglementation) | Détenu | Absent | FAIBLE-MOYEN |
| Genre professionnel agriculteur | Partagé (formations) | Partagé (transmission) | Partagé (branches, chambres) | Absent | Absent | ÉLEVÉ |
| Salaires décents long terme | Détenu (salariés) | Absent | Partagé (convention collective) | Absent | Absent | MOYEN |

Le degré de communalité contrasté éclaire les tensions du dispositif. Le sol agricole, juridiquement propriété privée pleine, est l'entité dont la communalité est la plus faible — alors même que c'est elle qui porte les enjeux écologiques les plus lourds. C'est cette tension que la comptabilité CARE cherche à signaler en inscrivant le sol comme créancier doté de droits propres (via les dettes naturelles), sans pour autant modifier sa qualification juridique. La piste d'approfondissement est claire : sans réforme du droit foncier (transformation progressive de la propriété en droit d'usage écologiquement contraint), la grammaire G-COMMUNALITE bute sur la qualification juridique du sol.

### K.5.4 G-JUSTICE — capabilités plancher et parité délibérative

La grammaire Justice et capabilités (Fiche 6) éclaire principalement la dimension humaine du cas. La sous-couche C-CAPABILITES inscrit le seuil_alerte_capabilite pour chaque type de capabilité Nussbaum : INTEGRITE_CORPORELLE (santé-sécurité au travail), RAISON_PRATIQUE (autonomie professionnelle), AFFILIATION (intégration dans le métier et le territoire), CONTROLE_ENV_MATERIEL (rémunération décente), CONTROLE_ENV_POLITIQUE (parité délibérative dans les instances). Pour le salarié temps plein, toutes les capabilités sont à au moins 3 / 5 ; pour le saisonnier, AFFILIATION et CONTROLE_ENV_POLITIQUE sont à 2 / 5 — signal CAPABILITE_PLANCHER_ATTEINTE non déclenché mais à surveiller.

Sous-couche C-POUVOIR : asymetrie_intersectionnelle = exploitant français pluriactif vs saisonnier (souvent immigré, précaire). injustice_epistemique = présence d'une dimension HERMENEUTIQUE (le saisonnier ne dispose pas du lexique CARE / IDEA4 pour participer à la délibération sur les seuils). parite_participation (ex-parite_deliberative) = FAUX pour le saisonnier dans le périmètre du cas tel que documenté. R-HERMENEUTIQUE (Fricker) suggère une obligation : co-construire un lexique accessible avant d'inscrire un consentement du saisonnier.

### K.5.5 G-MIMETIQUE (Fiche 7) — vigilance sacrificielle

La grammaire mimétique éclaire deux risques sur le cas Exploitation B :

Premièrement, le risque que l'élevage soit désigné bouc émissaire dans le débat public sur l'empreinte écologique de l'agriculture, ce qui occulterait les structures systémiques (politique agricole commune, chaînes de distribution, surfaces dédiées au fourrage). R-VICTIME-EMISSAIRE serait activée par un signal focalisation_victimaire si une décision politique imposait une réduction brutale de l'élevage sans accompagnement structurel — le troupeau de l'Exploitation B (DID acteur) serait sacrifié au nom d'une crise dont les causes lui sont en grande partie extérieures. Le mécanisme victimaire serait achevé si la paix publique en résultait, et si la voix du troupeau (médiée par celle de l'exploitant) n'était pas inscrite dans la délibération.

Deuxièmement, le risque que l'expérimentation CARE / IDEA4 elle-même devienne un attracteur valorisé qui occulte les autres dispositifs de transformation possibles (économie symbiotique de Delannoye, agriculture paysanne sans CARE, etc.). R-MECONNAISSANCE invite à inscrire ce risque : le narratif CARE est-il fondé sur l'exclusion d'autres voies de transformation ? Le champ auto_critique de C-MECONNAISSANCE doit être renseigné systématiquement par l'équipe de recherche.

### K.5.6 G-MESOLOGIE et G-PERFORMATIVITE

La grammaire mésologique (Berque, Stépanoff) éclaire la dualité métabolisme / attention au niveau du milieu vécu — déjà mobilisée Couche 1. La grammaire performative (Haraway, Gibson-Graham) signale un effet majeur du cas : l'inscription des capitaux NH comme créanciers ne se contente pas de décrire — elle constitue politiquement ces capitaux comme acteurs. Le sol Exploitation B n'avait pas, avant CARE, le statut de créancier ; il l'a maintenant. Cette performativité est gouvernée par la déclaration explicite des conditions de conception du référentiel (qui a co-construit IDEA4 ? qui a été consulté ? qui est exclu ?) — cf. K.4.3.

## K.6 Lecture détaillée du bilan CARE — grammaire P-C-E-D-e-d

Conformément à la grammaire sémantique P-C-E-D-e-d issue de la note synthétique MRC × CARE (proposée comme raffinement de R1 en Piste 2 de l'analyse critique), l'analyse du bilan CARE de l'Exploitation B peut être typée comme suit. Cette typologie va au-delà du binaire DÉBIT / CRÉDIT en distinguant six primitives : P (patrimoine), C (créance), E (engagement), D (dette), e (efforts fournis), d (résultats répondant aux désirs).

### K.6.1 Côté actif — P et C

| Composante du bilan | Type P-C-E-D-e-d | Lecture MRC |
|---|---|---|
| Terrains, bâtiments, matériel (actifs financiers) | P (patrimoine) | Choses gérées et utilisées dans le régime métabolique |
| Stocks de produits agricoles et d'élevage | P (patrimoine produit) | Résultat du régime métabolique en attente de vente |
| Créances clients | C (créance) | Droit vis-à-vis d'un acteur dont la dette n'est pas encore réglée |
| Sol agricole (actif naturel) | P + C composite | Patrimoine de l'exploitation au sens juridique ; créance écologique au sens CARE |
| Biodiversité parcellaire (actif naturel) | C (créance — non patrimonial) | Droit d'usage et de soin sans propriété pleine |
| Capital humain salariés (actif humain) | C (créance vers une personne) | Droit d'usage des compétences sans propriété sur la personne |

### K.6.2 Côté passif — E et D

| Composante du bilan | Type P-C-E-D-e-d | Lecture MRC |
|---|---|---|
| Capitaux propres (réserves, capital social) | E (engagement) | Engagement de l'entité réifiée envers les propriétaires |
| Dettes financières (banque, fournisseurs) | D (dette) | Devoir contractuel envers un créancier identifié |
| Dettes naturelles (10 605,9 €) | D NH (dette envers commun écologique) | Devoir envers le sol, la biodiversité, l'eau — D NH non remettable sans action de réparation effective (cf. mvt 13) |
| Dettes humaines — salaires décents long terme (2 901 312 €) | D NH (dette envers commun humain) | Devoir envers les salariés cumulé sur leur carrière — fondement de R-PRIORITE-CREANCIERS |
| Dettes humaines — capital sociétal (~ 31 000 €) | D NH composite | Devoir envers le territoire, le tissu associatif local |
| Dettes humaines — capital patrimonial (~ 20 000 €) | D NH composite | Devoir envers la transmission inter-générationnelle de l'exploitation |

### K.6.3 Compte de résultat — e et d

Le compte de résultat se lit principalement avec les primitives e (efforts fournis par les acteurs) et d (résultats répondant aux désirs des acteurs). La distinction est précieuse pour signaler ce que la comptabilité classique tend à fusionner.

| Composante | Type P-C-E-D-e-d | Montant (€) | Lecture MRC |
|---|---|---|---|
| Chiffre d'affaires (ventes agricoles + élevage) | d (résultat répondant aux désirs des clients) | ≈ 245 000 | Effort de l'exploitation produit en réponse à un désir (alimentation des consommateurs) ; génère P (caisse / créance) |
| Charges courantes (intrants, énergie, fournisseurs) | e (efforts des fournisseurs reçus) | ≈ 100 000 | Efforts d'autres acteurs reçus par l'exploitation ; génère D financière |
| Charges de personnel | **e** (efforts des salariés reçus) — *typage arrêté par décision du porteur* | ≈ 31 000 | Effort des salariés reçus. **Le remboursement partiel de D humaine n'est pas un second typage : c'est un mouvement de maintien distinct, dont l'inscription structurée est obligatoire — **CONV-11**, NT-ARCH §8.5.3bis / Annexe §A.15.4.** Cette glose ne vaut pas inscription |
| Coût de préservation NH (charges CARE) | **e** (efforts vers les capitaux NH) | ≈ 32 651,70 | Effort de soin envers le sol, le troupeau, la biodiversité. **Même forme que la ligne précédente, donc même **CONV-11**** : le remboursement partiel de D NH est un mouvement de maintien à inscrire, non une glose |
| Résultat net CARE | P final (patrimoine constitué) | 69 207,30 | Reste après l'ensemble des e et des d ; à arbitrer par R-PRIORITE-CREANCIERS avant distribution |

La lecture P-C-E-D-e-d clarifie une opération critique : le coût de préservation NH (e : effort vers les NH) est inscrit comme charge — donc réduit le résultat avant distribution. C'est le mécanisme comptable qui rend opérante R-PRIORITE-CREANCIERS de manière non bloquante : les NH sont payés en premier, dans la mesure des plans de préservation effectivement réalisés. Le résultat distribuable est ce qui reste après que les dettes NH ont été partiellement honorées sur l'exercice. Cette inscription est exactement ce que la comptabilité financière classique manque.

**Typage des charges de personnel (décision du porteur) : `e` seul.** L'extinction partielle de dette est un **effet**, relevant de la transition (`transition_valide`), non une seconde nature de l'écriture.

> **Mais la glose ne suffit pas.** Deux lignes de ce tableau portent un remboursement dans leur colonne de lecture (« remboursement partiel de D humaine », « remboursement partiel de D NH ») sans qu'aucun champ ne l'inscrive. **CONV-11** (NT-ARCH §8.5.3bis, Annexe méthodologique §A.15.4) est la contrepartie obligatoire de la décision : le mouvement de maintien doit porter **porteur, contrepartie, solde, horizon, critère de vérification**, et l'écriture doit **nommer le registre qui le porte** — registre de communalité ou rapport extra-financier, le registre financier n'étant pas requis.

**Ce que cela change pour la lecture de R-PRIORITE-CREANCIERS sur ce cas.** La règle n'opère pas sur ce qui a été payé mais sur **l'écart entre le dû et le payé**. En l'état, K.6.2 porte 2 901 312 € de dettes humaines et K.6.3 ≈ 31 000 € de charges de personnel : **le taux de couverture n'est lisible que si le mouvement de maintien est inscrit**. Non inscrit, il ne reste qu'une charge d'exercice qui ne dit rien du stock. `[À COMPLÉTER — les deux lignes ci-dessus ne satisfont pas encore CONV-11 ; le cas K1 est à reprendre sur ce point.]`

`[BASE DÉCLARÉE]` Le mot **dette** est employé ici au sens de la **construction A** (le passif est le capital apporté), non au sens de l'écart non financé — voir NT-ARCH §8.5.3bis. Les 2 901 312 € de K.6.2 en sont la pièce : c'est un stock de coût de maintien.

## K.7 Application des dispositifs techniques (Annexe H)

L'inscription opérationnelle du cas Exploitation B mobilise cinq des briques techniques décrites à l'Annexe H. La présente section détaille leur instanciation.

### K.7.1 DIDs — identifiants décentralisés

Conformément à H.1, chaque acteur du cas reçoit un DID (cf. K.2.1). Trois familles méritent un commentaire : (a) les DIDs des personnes physiques sont auto-souverains, contrôlés par l'individu ; (b) les DIDs des communs écologiques (sol, biodiversité, eau, troupeau) sont gérés par un consortium multi-parties (Chambre d'agriculture + Agence de l'eau + association environnementale locale + représentant de l'exploitant) selon des règles de gouvernance explicitement inscrites ; (c) les DIDs des instruments (capteurs, valuemètres IDEA4) sont liés à des VCs de conformité scientifique et de co-construction.

### K.7.2 VCs — attestations vérifiables

| Type de VC | Émetteur | Articulation au cas Exploitation B |
|---|---|---|
| VC de consentement à l'inscription | Chaque acteur lui-même | Exploitant ; salarié (sans difficulté) ; saisonnier (avec réserves : voir K.5.4) |
| VC de qualification scientifique du référentiel IDEA4 | Comité scientifique IDEA4 | Liée au DID du valuemètre IDEA4 — atteste la validité scientifique du calcul |
| VC de co-construction du valuemètre local | Communauté locale (exploitant + consortium) | Liée au DID du valuemetre:cout-pres-exploitB — atteste que le calibrage local a été fait avec les acteurs concernés |
| VC d'habilitation à inscrire au nom du sol | Consortium de gouvernance | Atteste qui peut écrire des observations / alertes / consentements au nom du DID du sol |
| VC de salaire décent attesté | Convention collective ou OPCO | Atteste le niveau de salaire décent à long terme — sous-tend la dette humaine 2 901 312 € |
| VC d'évaluation tracée R-POUVOIR | Évaluateur (chercheur, expert) | Toute évaluation normative du dispositif CARE doit être attestée — sans VC, l'évaluation est invalide (Fiche 6) |

### K.7.3 dMRV — mesure, reporting, vérification numériques

Pour l'Exploitation B, le dMRV combine plusieurs sources. Côté biophysique (mode milieu) : analyses pédologiques pluri-annuelles, indice de matière organique, balance azotée, indices de biodiversité (présence d'espèces clés, taux de présence d'auxiliaires de culture), suivi piézométrique du bassin local, mesures d'émission ammoniac, satellitaire pour la couverture des sols et la surface de haies. Côté social (mode travail) : VCs de formation, attestations de salaire, suivi des accidents du travail. Côté économique : flux comptables classiques (CA, charges, marges) intégrés à la comptabilité CARE.

Le rôle structurant du dMRV est triple : (1) il fournit la source de vérité pour calculer les indicateurs IDEA4 indépendamment de la déclaration de l'exploitant ; (2) il alimente automatiquement le régime attentionnel du registre, conformément à la Couche 1 ; (3) il rend possible le déclenchement automatique des signaux C-SIGNAL — par exemple, signal_ecologie_superficielle s'activerait sans intervention humaine si l'indice de matière organique passait sous un seuil défini, ou si la balance azotée dépassait un plafond.

### K.7.4 Smart contracts — covenants automatisés

Pour l'Exploitation B, plusieurs covenants automatisés peuvent être envisagés. Un covenant de financement vert : si l'exploitation est financée par un prêt bonifié dont le taux dépend de la trajectoire IDEA4, le smart contract recalcule annuellement le taux en fonction des indicateurs effectivement inscrits. Un covenant de remboursement prioritaire des dettes NH : conformément à la règle de Couche 1 R-PRIORITE-CREANCIERS (Piste 3 de l'analyse critique), le smart contract bloque la distribution de dividendes ou la rémunération de l'exploitant au-delà du salaire décent tant que la dette naturelle (10 605,9 € en fin d'exercice) n'a pas été ramenée à un niveau convenu. Un covenant d'alerte automatique : si l'indicateur IDEA4 composite passe sous un seuil défini sur 2 cycles consécutifs, le smart contract notifie automatiquement le consortium de gouvernance et ouvre une phase PROBLÈME dans C-ENQUETE-V5.

Ces covenants n'existent pas dans la documentation actuelle de l'Exploitation B — leur formalisation et leur opérationnalisation sont des extensions naturelles du cas, dans la lignée de l'Annexe H.

### K.7.5 IPFS — stockage à adressage par contenu

La permanence des inscriptions sur l'Exploitation B est garantie par IPFS pour les documents et données suivants : le bilan CARE complet de chaque exercice (avec ses hash on-chain) ; la fiche pédagogique IDEA4 originale ; les rapports d'analyse pédologique pluri-annuels ; les comptes-rendus des réunions de co-construction des seuils ; les attestations de consentement des acteurs. La fonction est de garantir que ces inscriptions ne peuvent ni être falsifiées ni être effacées, même si l'exploitation cesse son activité ou change de gestionnaire. C-MEMOIRE-PERTES, en particulier, opère sur IPFS : toute dette NH non remboursée et toute irréversibilité confirmée sont inscrites de façon permanente.

## K.8 Articulation au juste prix écologique (Dumeaux 2025)

La thèse de Louis Dumeaux (2025) propose le double affichage des prix comme dispositif d'opérationnalisation politique de CARE : à côté du prix payé par le consommateur (prix conventionnel), un prix CARE est affiché, qui intègre les coûts de préservation des capitaux NH. La différence entre les deux prix matérialise la dette implicite que le consommateur reporte sur les communs s'il choisit le premier.

Pour l'Exploitation B, l'application du double affichage produit, à titre illustratif, les ordres de grandeur suivants : sur 1 kg de viande bovine vendu à 8 € prix classique, le prix CARE correspondant intègre une part de coût de préservation pédologique, de coût de qualité de l'eau, de coût de soin du troupeau, et de coût de salaire décent. L'estimation Dumeaux suggère une majoration de l'ordre de 15-25 % pour les produits CARE, soit un prix CARE compris entre 9,20 € et 10 €.

### K.8.1 Lecture MRC du double affichage

Dans la lecture MRC, le double affichage instancie un cycle performatif au sens strict de l'Annexe G.3 : le prix CARE est produit par le mode comptable (M-COMPTA — instanciable par la Fiche F8 envisagée en synthèse), inscrit comme catégorie publique dans le mode sémantique (M-SEMANTIQUE — une nouvelle catégorie de prix entre dans le corpus public), modifie le comportement des consommateurs (mode social, à articuler à F1 / F6), et boucle vers le mode comptable en ajustant les ventes et donc les marges. Ce cycle est un signal boucle_confirmante_detectee (Annexe G.7) — non bloquant tant qu'il est explicitement gouverné, alarmant s'il devient un attracteur dérégulé.

### K.8.2 Tensions identifiées par Dumeaux et relectures MRC

La thèse identifie trois tensions sur le double affichage, que le MRC relit utilement :

Tension 1 — Dépendance aux experts. Le calcul du prix CARE requiert des compétences scientifiques (calibrage IDEA4) que les consommateurs ne maîtrisent pas. Lecture MRC : c'est un signal CORPUS_NON_CONSENTI latent (Fiche 3) si le régime d'inscription du référentiel CARE devient EXPERTAL au détriment de la délibération collective. La solution est dans la VC de co-construction (Annexe H.2).

Tension 2 — Désaccords sur les classifications. Faut-il intégrer dans le prix CARE le coût des émissions de CO₂ ? Et à quelle valeur sociale du carbone ? Lecture MRC : c'est une dispute classique sur le choix de la catégorie de base V (C-CATEGORIE-BASE, Couche 0) ; sa résolution passe par C-ENQUETE-V5 en phase RÉVISION_CONCEPTUELLE.

Tension 3 — Incertitudes politiques. Le double affichage peut être contourné par les acteurs dominants ou capté par des stratégies marketing. Lecture MRC : c'est un signal focalisation_victimaire latent (Fiche 7) — le risque que le double affichage soit instrumentalisé pour désigner les petits producteurs comme « ne pouvant pas suivre » et donc justifiables d'élimination du marché.

## K.9 Synthèse — Ce que ce cas démontre et ce qu'il appelle

### K.9.1 Ce que le cas démontre

L'application bout-à-bout du MRC à l'Exploitation B confirme cinq points théoriques importants :

L'architecture des quatre couches tient. Tous les éléments du cas (acteurs humains et non-humains, indicateurs, dettes, signaux) trouvent leur place dans la stratification Couche 0 / Couche 1 / Couche 2 / Couche 3 sans débord ni redondance.

Les quatre modes sont effectivement instanciables. Travail, milieu, sémantique et existentiel ne sont pas des branches théoriques mais des angles d'analyse productifs sur un même cas concret.

Les sept grammaires transversales (Couche 3) ne sont pas redondantes. Chacune éclaire une dimension distincte (responsabilité, soin, communalité, justice, mésologie, performativité, mimétique) et chacune apporte un diagnostic propre.

Le cadre bicatégoriel de l'Annexe G est mobilisable. La 2-cellule R-COUPLAGE entre régimes métabolique et attentionnel est calculable de manière approchée ; les changements de base entre catégories V sont des opérations effectives (passage CARE → IFRS, ou inversement).

Les dispositifs techniques de l'Annexe H sont compatibles avec le cas. DIDs, VCs, dMRV, smart contracts, IPFS s'inscrivent naturellement dans l'expérimentation telle qu'elle est conduite. L'extension du cas par ces dispositifs constitue un programme de travail réaliste à 12-24 mois.

### K.9.2 Ce que le cas appelle — confirmation des 6 pistes d'approfondissement

Le cas confirme empiriquement les six pistes d'approfondissement identifiées dans l'analyse critique des deux documents apportés par l'utilisateur (analyse du 15 mai 2026).

| Piste | Confirmation par le cas Exploitation B |
|---|---|
| 1 — Fiche F8 Mode comptable / capitaux | Confirmée. Le mode comptable est manifestement transversal (il articule travail, milieu, sémantique, existentiel) et mérite sa fiche opérationnelle propre, avec sous-couche C-COMPTABILITE-CARE. |
| 2 — Raffinement de R1 par la grammaire P-C-E-D-e-d | Confirmée. La grammaire à 6 primitives produit une lecture plus précise du bilan et du compte de résultat (cf. K.6). Elle complète sans contredire R1. |
| 3 — R-PRIORITE-CREANCIERS en Couche 1 | Confirmée. Le besoin d'une règle d'ordre dans le remboursement (NH avant capital financier, capabilités plancher avant distribution discrétionnaire) est évident sur le cas. Implémentable par smart contract. |
| 4 — Annexe G.9 sur les enrichissements composites | Confirmée. V^CARE = 𝟤 × E × N × C est un cas paradigmatique d'enrichissement produit. La formalisation théorique reste à faire. |
| 5 — Annexe K cas d'usage chiffrés | Démarrée par le présent document. Cas Exploitation B traité ; cas Dumeaux (juste prix écologique) effleuré ; reste à traiter au moins un cas par mode (LLM gouvernance pour M-SEMANTIQUE ; bassin versant pour M-MILIEU pur ; dialogue social pour M-TRAVAIL pur ; risque systémique pour M-EXISTENTIEL pur). |
| 6 — Régime d'inscription combiné (recherche-intervention) | Confirmée. L'expérimentation CARE / IDEA4 combine effectivement les trois régimes (observationnel + collectif + autogouvernance) ; ce régime combiné mérite une dénomination explicite en Couche 0. |

### K.9.3 Limites du cas et angles morts

Le cas tel que documenté présente des limites qu'il faut explicitement reconnaître : (a) la voix du saisonnier n'est pas pleinement inscrite (parite_participation imparfaite, cf. K.5.4 — ex-parite_deliberative) ; (b) le care invisibilisé du conjoint d'exploitant n'apparaît pas (cf. K.5.2) ; (c) les riverains du bassin et les consommateurs ne sont pas représentés directement dans la délibération sur les seuils ; (d) la dimension mimétique reste à l'état de risque latent, non documenté empiriquement ; (e) le passage de la comptabilité de gestion (CARE) à la comptabilité financière publiée (IFRS) n'est pas opéré dans le cas, ce qui empêche de tester le foncteur de changement de base π : V^CARE → V^IFRS en situation réelle.

Ces limites ne disqualifient pas le cas — elles en délimitent la portée et indiquent les directions de complément. Aucune ne remet en cause les confirmations théoriques opérées (K.9.1) ; toutes appellent un travail empirique additionnel.

### K.9.4 Prochains cas d'usage à produire pour étoffer l'Annexe K

Pour stabiliser l'Annexe K comme référentiel partagé, un programme de cas complémentaires est suggéré, à raison d'au moins un cas par mode pur :

Cas n° 2 — Gouvernance d'un grand modèle de langage (M-SEMANTIQUE pur). Application aux dérives sémantiques détectées par 2-morphismes inter-corpus, calcul de la 2-cellule SVD / FCA, instanciation de la Fiche 3.

Cas n° 3 — Bassin versant en gouvernance multi-acteurs (M-MILIEU pur). Application Annexe H complète avec DID du bassin, dMRV biophysique automatisé, covenants de financement responsable, instanciation Fiche 2.

Cas n° 4 — Dispositif DPQT en milieu hospitalier (M-TRAVAIL pur). Application Fiche 1 sur un genre professionnel, en lien avec C-COMMUNALITE-TRAVAIL et la grammaire G-SOIN.

Cas n° 5 — Stockage de déchets nucléaires longue durée (M-EXISTENTIEL pur). Application Fiche 4 + Annexe G.4 (catégorie indexée Exist) avec déclenchement formel de R-INTERDIT-ABSOLU.

Cas n° 6 — Crise institutionnelle résolue par bouc émissaire (G-MIMETIQUE). Application Fiche 7 sur un cas historique documenté (par exemple, la crise sanitaire 2025 ou une réorganisation d'entreprise emblématique).

Le présent cas Exploitation B constitue le point d'entrée didactique de l'annexe — celui où l'on peut éprouver la cohérence de l'ensemble du modèle sur un terrain complet et chiffré. Les cas n° 2 à 6 viseront à isoler les modes purs pour montrer la spécificité de chacun. À terme, l'Annexe K constituera, avec les Annexes G et H, le triptyque opérationnel du MRC : la formalisation (G), l'infrastructure (H), et l'éprouvé empirique (K).

### K.9.5 Ouverture

Ce premier cas de l'Annexe K, centré sur l'Exploitation B, montre que le MRC atteint un niveau de complétude architecturale qui permet d'aborder des cas réels. Le travail demeure considérable — formalisation des pistes d'approfondissement, production des cas complémentaires, articulation aux cadres comptables internationaux — mais le geste est possible. Le présent document est offert comme support de cette démarche et comme test public de la solidité du modèle.

# PARTIE K2-A — Gouvernance d'un LLM (OpenLLM / BentoML)

Modèle de Registres de Communalité

Annexe K — Cas d’usage chiffrés

Cas n° 2 : Gouvernance d’un grand modèle de langage (LLM)

Application de l’architecture MRC à la gouvernance du projet OpenLLM (BentoML)

Pierre Musseau-Milesi

La Coop des Communs

Mai 2026

Statut : document de travail — annexe complémentaire au MRC

## Table des matières

## K.0 Note de présentation

Le cas n° 2 de l’Annexe K applique l’architecture du MRC à un terrain radicalement différent du cas K1 (Exploitation B, comptabilité écologique agricole) : la gouvernance d’un logiciel d’inférence de grands modèles de langage (LLM), en l’occurrence le projet OpenLLM développé et maintenu par la société BentoML. Ce déplacement de terrain est voulu : l’Annexe K a pour vocation de tester la généralisabilité de l’architecture MRC sur des objets aussi hétérogènes que possible.

OpenLLM est un outil open source (licence Apache 2.0) permettant à tout développeur de déployer un LLM open source (Llama, Mistral, Qwen, DeepSeek…) comme endpoint API compatible OpenAI, en local ou dans le cloud. Il représente un cas paradigmatique de ce que l’on peut appeler la « gouvernance d’un commun numérique sous tension commerciale » : un logiciel libre, construit sur le travail bénévole de contributeurs et sur des modèles open source produits par des tierces parties, qui sert également de vecteur commercial pour BentoCloud, la plateforme d’inférence cloud de BentoML.

Trois raisons motivent ce choix : (1) le projet est complet et public — code source, liste de contributeurs, historique de commits, modèles supportés, conditions de licences, tout est documentable ; (2) il articule les quatre modes du MRC de manière non triviale, chacun dans un registre nouveau par rapport au cas K1 ; (3) il constitue un terrain sur lequel la Piste 1 (Fiche F8 « Mode comptable ») peut être testée dans un contexte extra-agricole et extra-financier, éprouvant la portabilité de l’architecture.

L’objectif n’est pas de produire une expertise technique sur les LLMs — la littérature scientifique et technique sur l’empreinte énergétique, les biais et la gouvernance des LLMs constitue l’autorité scientifique sur ces points. L’objectif est de montrer comment l’architecture MRC permet de « lire » ce cas, d’identifier ses choix architecturaux, ses signaux, les dispositifs techniques nécessaires et ses tensions restantes. Les chiffres utilisés sont des estimations construites à partir de données publiques et de la littérature sur l’empreinte énergétique de l’inférence LLM ; ils sont indiqués comme tels.

Sources mobilisées : dépôt GitHub bentoml/OpenLLM (v0.6.30, avril 2025) ; Strubell et al. (2019) Energy and Policy Considerations for Deep Learning in NLP ; TokenPowerBench (2024, arXiv:2512.03024) ; ML.ENERGY Benchmark v3.0 (décembre 2025) ; TRG Datacenters, NVIDIA H100 Power Consumption Guide (2024).

## K.1 Présentation du cas — OpenLLM (BentoML)

### K.1.1 Profil du projet

OpenLLM est un projet open source lancé par BentoML Inc. (société américaine, fondée en 2019, soutenue par des capitaux-risqueurs). Le projet permet de servir tout LLM open source comme endpoint HTTP compatible avec l’API OpenAI, en une seule commande. Il repose sur vLLM (backend d’inférence haute performance) et sur la plateforme BentoML pour la génération de conteneurs déployables.

Au 17 mai 2026, le dépôt GitHub bentoml/OpenLLM présente les caractéristiques suivantes :

| Indicateur | Valeur |
|---|---|
| Dernière version stable | v0.6.30 (21 avril 2025) |
| Nombre de commits | 1 923 |
| Nombre de contributeurs | 31 (dont ~5 actifs réguliers, employés BentoML) |
| Stars GitHub | 12 200 |
| Forks | 803 |
| Issues ouvertes | 4 |
| Licence | Apache 2.0 (réutilisation commerciale autorisée sans réciprocité obligatoire) |
| Modèles supportés | 15 modèles (de gemma2:2b à deepseek:r1-671b) — de 2B à 671B paramètres |
| Langages | Python 95,9 %, Shell 4,1 % |
| Dépendances clés | vLLM (backend), BentoML (serving), Hugging Face (poids des modèles) |

La tension structurante du projet est celle entre « logiciel libre » et « vecteur commercial » : OpenLLM est distribué gratuitement sous Apache 2.0, mais il est conçu pour rendre BentoCloud (service cloud payant de BentoML) aussi simple à utiliser que possible. La commande openllm deploy mène directement à la plateforme commerciale. Cette tension est précisément ce que le MRC est fait pour rendre gouvernable.

### K.1.2 Scénario de référence et données chiffrées

Pour permettre une application chiffrée comparable à K1, le cas K2 construit un scénario de référence représentatif. Ce scénario n’est pas fictif : il correspond à un déploiement-type tel que le décrit le README officiel d’OpenLLM, avec des paramètres énergétiques tirés de la littérature.

Scénario : un collectif ou une organisation (une coopérative, un service public, un laboratoire) déploie un service LLM communautaire basé sur OpenLLM avec le modèle Llama 3.3 70B, sur 2 GPU H100 SXM 80 Go loués dans un datacenter (exigence minimale indiquée dans le README). Le service fonctionne 50 % du temps (8 760 h/an × 50 % = 4 380 h actives) et traite 10 000 requêtes/jour.

Données chiffrées de référence (estimation à partir de sources publiques) :

| Catégorie | Valeur estimée | Source / méthode |
|---|---|---|
| Consommation énergétique GPU (2 H100, 50 % utilisation) | 6 132 kWh/an | TDP H100 SXM = 700 W ; 2 GPU × 700 W × 0,5 × 8 760 h |
| Empreinte carbone opérationnelle | 1 840 kg CO₂/an | Mix électrique européen moyen : 300 g CO₂/kWh |
| Empreinte carbone fabrication GPU | ~ 6 000 kg CO₂ | ~ 3 000 kg CO₂/GPU H100 (estimation littérature) |
| Consommation énergétique par requête (Llama-70B, H100) | ~ 0,5 J/token ; ~ 0,07 Wh/requête | TokenPowerBench 2024 ; ML.ENERGY v3.0 (2025) |
| Travail contributeurs open source (31 contrib., estim.) | ~ 775 000 €/an équivalent | 31 contrib. × 500 h/an × 50 €/h |
| Travail équipe core BentoML (5 ETP estimés) | ~ 800 000 €/an | 5 ETP × 1 600 h × 100 €/h |
| Coût GPU cloud annuel (2 H100, 50 % util.) | ~ 30 660 €/an | ~ 3,50 €/h/GPU × 2 × 4 380 h |
| Valeur délivrée (10 000 req./j × 365, équivalent ~ 0,01 €/req.) | ~ 36 500 €/an | Comparable au tarif OpenAI GPT-4o mini |
| Résultat « classique » (valeur − coût GPU) | + 5 840 €/an | Positif selon la comptabilité opérationnelle courante |
| Résultat MRC (avec inscription des capitaux NH) | − 769 252 €/an | Après inscription dette contributeurs + dette carbone |

L’écart de 775 092 € entre résultat classique (+ 5 840 €) et résultat MRC (− 769 252 €) est l’équivalent numérique de l’écart de 32 651,70 € du cas K1. Il matérialise le défaut de couplage structurel entre régime métabolique (exploitation du logiciel libre et des poids de modèles open source) et régime attentionnel (soin envers les contributeurs, les fournisseurs de modèles, les utilisateurs finaux et la planète). Dans K1, l’écart était un problème de gestion (couvrable par des pratiques agro-écologiques) ; dans K2, il est structurel (la licence Apache 2.0 ne l’oblige pas à être couvert).

## K.2 Lecture Couche 0 — Primitives constitutives instanciées

Conformément à la Couche 0 du MRC, tout cas d’usage commence par l’identification des acteurs, du choix de la catégorie de base, du régime d’inscription et des niveaux d’explication mobilisés.

### K.2.1 Acteurs — proposition de DIDs

Chaque acteur du cas reçoit un identifiant décentralisé (DID) conformément à l’Annexe H.1. Les DIDs proposés ci-dessous sont des modèles ; leur instanciation effective relève de la gouvernance du registre.

| Type d’acteur | Acteurs du cas | DID proposé | Statut |
|---|---|---|---|
| Organisation commerciale mainteneuse | BentoML Inc. (société américaine, porteur principal) | did:registre:org:bentoml-inc | Auto-souverain |
| Contributeurs open source | 31 contributeurs GitHub (dont ~5 employés BentoML, ~26 bénévoles) | did:registre:person:openllm:contrib-[n] | Auto-souverain |
| Fournisseurs de modèles amont | Meta (Llama), Mistral AI, Google (Gemma), Alibaba (Qwen), DeepSeek | did:registre:org:meta-llama ; …:mistral-ai ; …:google-gemma ; …:alibaba-qwen ; …:deepseek | Gouvernance externe |
| Déployeurs (utilisateurs organisationnels) | Entreprises, coopératives, labos, admins systèmes utilisant OpenLLM/BentoCloud | did:registre:org:deployer-[uid] | Auto-souverain |
| Utilisateurs finaux | Développeurs, chercheurs, opérateurs interagissant avec les LLMs déployés | did:registre:person:end-user-[uid] | Pseudonyme |
| Communautés affectées par les biais | Groupes dont les données d’entraînement ont été collectées et/ou dont les biais affectent les sorties | did:registre:commun:affront-biais-[langue/culture] | Consortium représentatif à constituer |
| Infrastructure physique (non-humain) | GPU H100, datacenters (BentoCloud), réseau électrique, systèmes de refroidissement | did:registre:milieu:gpu-h100-[id] ; …:datacenter-[loc] ; …:grid-[pays] | Consortium gouvernance (opérateurs cloud + Réseaux électriques) |
| Corpus sémantique (non-humain) | Poids des modèles (artefacts du travail d’entraînement), données d’entraînement, documentation | did:registre:corpus:llama33-70b ; …:corpus:openllm-doc | Communauté scientifique + fournisseurs |
| Instruments de mesure | Compteurs d’énergie GPU (NVIDIA NVML), benchmarks TokenPowerBench, ML.ENERGY, logs de requêtes | did:registre:valuemetre:nvml-[gpu-id] ; …:valuemetre:tokenpowerbench | Opposé à certification indépendante |

Note architecturale : la distinction entre contributeurs employés BentoML (~5) et contributeurs bénévoles (~26) est décisive pour la Couche 1. Les premiers sont inscrits en C-TRAVAIL salarié (rémunération contractuelle) ; les seconds constituent un capital humain mobilisé sans rémunération directe, donc une dette inscrite du côté passif du registre.

### K.2.2 Catégorie de base

Conformément à la lecture proposée dans le cas K1 et à la Piste 4 de la note de cadrage, le cas K2 instancie la même catégorie de base composite :

Vᶜᵃᴿᴸ = 𝟤 × E × N × C

où 𝟤 = {0, 1} capture la présence / absence d’une dépendance ; E est l’ensemble des types d’évaluation ; N l’ensemble des natures comptables ; C l’ensemble des profils de capital protégé. Pour le cas K2, les instanciations spécifiques sont :

| Dimension | Valeurs K1 (Exploitation B) | Valeurs K2 (OpenLLM) |
|---|---|---|
| E (types d’évaluation) | Coût historique, coût de préservation, indicateur biophysique | Coût historique, équivalent coût de remplacement du travail bénévole, empreinte carbone évitée, valeur d’usage des poids de modèle |
| N (natures comptables) | Charge, produit, actif, passif, hors-bilan | Identique, avec ajout de « dette sémantique » (hors-bilan) pour les données d’entraînement non rémunérées |
| C (profils de capital) | Capital financier ; financier + NH ; NH seul | Capital financier (BentoML Inc.) ; capital humain contributeurs (travail bénévole) ; capital sémantique (corpus) ; capital énergétique-climatique (GPU + émissions) |

Le foncteur de changement de base ici n’est pas, comme en K1, un passage de V^IFRS à V^CARE, mais un passage de V^OSS (économie open source standard, qui ne comptabilise que les flux montaires) à V^MRC (économie de registres, qui inscrit également le travail bénévole, la dette carbone et la dette sémantique). La projection inverse π : V^MRC → V^OSS perd irrémédiablement l’information sur ces trois types de capitaux — c’est l’instance numérique du signal irreversibilite_changement_base.

### K.2.3 Régime d’inscription mobilisé

Le cas K2 mobilise les trois régimes d’inscription de la Couche 0, dans une combinaison différente de K1 :

ENQUETE_OBSERVATIONNELLE pour la mesure des flux énergétiques (consommation GPU via NVIDIA NVML, logs de requêtes, données de benchmarks) et pour le comptage du travail contributeur (commits GitHub, pull requests, issues résolues).

ENQUETE_COLLECTIVE est partiellement présente sous la forme des discussions GitHub et du Slack communautaire BentoML, où les décisions d’architecture, de modèles à intégrer et de gestion des licences sont débattues, mais sans procédure délibérative formalisée. C’est un cas de déficit d’ENQUETE_COLLECTIVE : le registre communautaire existe (GitHub) mais il n’est pas gouverné par un processus délibératif structuré.

AUTOGOUVERNANCE est limitée aux déployeurs individuels et organisationnels, qui choisissent quel modèle déployer, sur quelle infrastructure et avec quels paramètres énergétiques. Le projet OpenLLM lui-même n’offre pas de mécanisme d’autogouvernance aux communautés affectées par les modèles déployés.

Cette combinaison régimée révèle une asymétrie structurelle : la mesure (ENQUETE_OBSERVATIONNELLE) est techniquement possible mais non pratiquée ; la délibération (ENQUETE_COLLECTIVE) est informelle et asymmétrique ; l’autogouvernance est absent aux échelons concernés (contributeurs, communautés affectées). Le MRC permettrait de résoudre cette asymétrie en formalisant des procédures d’inscription pour chaque régime.

### K.2.4 Niveaux d’explication

Le cas K2 mobilise les trois niveaux d’explication selon la dimension considérée :

| Niveau | Dimension K2 | Exemple |
|---|---|---|
| PROXIMATE | Énergie, tokens, latence, GPU | 0,5 J/token sur H100 ; 6 132 kWh/an pour le scénario de référence |
| ULTIMATE | Statut des contributeurs, gouvernance des communs numériques | Le travail bénévole comme « commun producteur » au sens de Castoriadis/Dardot-Laval |
| DUAL | Passage du résultat classique au résultat MRC | L’écart de 775 092 € combine la mesure proximate (heures contributeurs) et le sens ultimate (responsabilité économique envers les producteurs du commun) |

## K.3 Lecture Couche 1 — Dualité des régimes et signaux

### K.3.1 Régime métabolique

Le régime métabolique d’OpenLLM est constitué de l’ensemble des opérations par lesquelles le projet extrait, consomme et transforme des ressources sans obligation formelle de les restituer :

Consommation du travail des contributeurs open source (31 personnes, dont ~26 bénévoles) : code, documentation, tests, support aux issues.

Consommation des poids de modèles produits par des tierces parties (Meta, Mistral, Alibaba, Google, DeepSeek) sans contribution directe au développement de ces modèles.

Consommation d’énergie GPU pour l’inférence (6 132 kWh/an dans le scénario de référence) sans mécanisme d’internalisation des externalités climatiques.

Consommation de la réputation et de la visibilité de la communauté open source pour attirer des clients vers BentoCloud.

Ce régime se traduit, dans la comptabilité classique d’une organisation déployant OpenLLM, par un coût GPU et aucune autre charge — le travail des contributeurs et les externalités climatiques sont invisibilisés.

### K.3.2 Régime attentionnel

Le régime attentionnel est constitué des dispositifs qui mesurent, cartographient et soignent ce que le régime métabolique mobilise. Pour OpenLLM, ce régime est embryonnaire et fragmentaire :

Mesure de l’énergie GPU : techniquement possible via NVIDIA Management Library (NVML) — mais non activée par défaut dans OpenLLM (aucun tableau de bord énergétique intégré).

Mesure du travail contributeur : partiellement disponible via les statistiques GitHub (commits, reviews) — mais non compilée en équivalent valeur ni communiquée aux contributeurs.

Soin envers les contributeurs : un code de conduite (CODE_OF_CONDUCT.md) existe sur GitHub ; un canal Slack communautaire est maintenu. Aucun mécanisme de rémunération des contributeurs extérieurs n’existe.

Soin envers les utilisateurs affectés par les biais : inexistant au niveau du projet OpenLLM (les responsabilités de sécurité/équité sont déléguées aux fournisseurs de modèles).

Le régime attentionnel est donc présent à un niveau minimal (code de conduite, canal de discussion), mais il n’est pas couplé au régime métabolique de manière gouvernable. C’est l’asymétrie fondamentale que le MRC rendrait visible et adressable.

### K.3.3 R-COUPLAGE — calcul de la 2-cellule

R-COUPLAGE exige une 2-cellule reliant le profunctor métabolique M_méta : Acteurs × Opérations → V^MRC (qui inscrit les prélèvements) et le profunctor attentionnel M_att : Acteurs × Indicateurs → V^MRC (qui inscrit l’état des capitaux NH).

Pour le cas K2, on identifie trois défauts de commutativité (trois écarts non compensés) :

| Défaut | Capital concerné | Écart estimé | Niveau MRC |
|---|---|---|---|
| Travail bénévole non rémunéré | Capital humain (contributeurs extérieurs) | ~ 775 000 €/an non inscrit | CRITIQUE — structurel |
| Empreinte carbone non internalizée | Capital énergétique-climatique | 1 840 kg CO₂/an à valoriser | MOYEN — systémique |
| Dette sémantique (données d’entraînement) | Capital sémantique (producteurs de données) | Non quantifiée — débat ouvert | INCONNU — à instruire |

Le défaut n° 1 (travail bénévole) franchit le seuil CRITIQUE : 775 000 €/an de capital humain mobilisé sans inscription comptable. Ce n’est pas une erreur de gestion corrigeable par un comportement plus vertueux — c’est une conséquence directe de la structure de gouvernance open source non réciproque permise par la licence Apache 2.0. Dans les termes du MRC, c’est un signal carre_non_commutatif au niveau CRITIQUE, qui devrait déclencher une procédure de RÉVISION à l’échelle du modèle de gouvernance — non pas une correction ponctuelle.

### K.3.4 R1 — Convention DÉBIT / CRÉDIT généralisée

La convention R1 est instanciée sur quatre écritures paradigmatiques pour le cas K2 :

#### (a) Mobilisation du travail d’un contributeur bénévole

DÉBIT du compte « actifs humains — travail contributeur bénévole » (au titre de la mobilisation de compétences et de temps) ; CRÉDIT du compte « dettes humaines — rémunération différée contributeurs » (au titre de l’obligation de réciprocité non encore honorée). La dette est amortie si BentoML Inc. met en place un mécanisme de partage des revenus de BentoCloud avec les contributeurs — ce qui n’est pas le cas à ce jour. En l’absence d’amortissement, la dette s’accumule à ~775 000 €/an.

#### (b) Consommation d’énergie GPU pour l’inférence

DÉBIT du compte « actifs énergétiques — énergie GPU consommée » (au titre du service rendu par l’infrastructure) ; CRÉDIT du compte « dettes climatiques — émissions CO₂ non compensées » (au titre de l’obligation de néutralisation ou de réduction). La dette est amortie si le déployeur souscrit à un contrat d’électricité renouvelable certifiée ou compense par des projets de séquestration carbone. En l’absence d’amortissement : 1 840 kg CO₂/an non inscrit.

#### (c) Intégration d’un nouveau modèle dans le catalogue OpenLLM

DÉBIT du compte « actifs sémantiques — poids modèle [modèle] » (au titre de la mobilisation du corpus encodé dans le modèle) ; CRÉDIT du compte « dettes sémantiques — fournisseur [org] » (au titre de l’obligation de reconnaissance et de réciprocité envers le fournisseur du modèle). La dette est amortie si OpenLLM contribue en retour au développement du modèle ou le signale dans ses communications. En l’état : obligation non inscrite.

#### (d) Génération de revenus via BentoCloud

Soumis à la règle de Couche 1 R-PRIORITE-CREANCIERS (Piste 3 de la note de cadrage) : pas de distribution de revenus BentoCloud avant inscription et amortissement minimal des dettes humaines (contributeurs bénévoles) et climatiques. En l’état, cette règle n’existe pas dans le modèle de gouvernance open source courant. Le cas K2 confirme empiriquement la nécessité opérationnelle de la Piste 3.

### K.3.5 C-SIGNAL — signaux activés sur le cas

| Signal | Activé ? | Niveau | Motif |
|---|---|---|---|
| carre_non_commutatif (défaut travail bénévole) | OUI | CRITIQUE | 775 000 €/an de capital humain non inscrit |
| signal_ecologie_superficielle | OUI | MOYEN | Empreinte carbone non mesurée ni internalisée |
| R-CARE_chronique (accumulation de dette) | PROBAB. | MOYEN | La dette contributeurs s’accumule depuis la création du projet (2022) |
| parite_participation_false `[RENOMMÉ LE 13/10/2026 — ex-parite_deliberative_false]` | OUI | MOYEN | Les communautés affectées par les biais ne participent pas aux décisions d’intégration des modèles |
| irreversibilite_changement_base | OUI | MOYEN | Passage V^OSS → V^MRC : les données de travail bénévole passé sont irrécupérables sans archives de commits |
| appel_entendu_systemique | NON | — | Aucun mécanisme systémique d’écoute des signaux des entités affectées n’existe |
| signal_souverainete_semantique | OUI | MOYEN | Dépendance aux poids distribués par des organisations américaines et chinoises non gouvernées de manière délibérative |

Le signal carre_non_commutatif au niveau CRITIQUE est inédit dans l’Annexe K : le cas K1 ne déclenchait qu’un niveau MOYEN. Cela révèle que les communs numériques non réciproques génèrent des défauts de couplage plus profonds que les communs écologiques gérés dans un cadre CARE.

## K.4 Lecture Couche 2 — Modes opérationnels

La Couche 2 du MRC instancie les quatre modes opérationnels (F1 — F4) plus la fiche F8 (Piste 1). Le cas K2 les parcourt entièrement.

### K.4.1 Fiche F1 — Mode Travail

Le mode travail inscrit les mobilisés humains dans le registre. Pour OpenLLM, trois strates de travail sont identifiées :

Travail salarié BentoML (~5 ETP) : inscrit normalement en comptabilité classique (charges de personnel). Dette humaine amortie contractuellement.

Travail bénévole contributeurs (~26 personnes) : non inscrit. Capital humain mobilisé sans contrepartie directe. Dette de ~775 000 €/an.

Travail des équipes de modèles amont (Meta, Mistral, etc.) : partiellement couvert par les licences des modèles, mais sans mécanisme de rémunération envers les producteurs de données d’entraînement.

Signal F1 activé : signal_travail_invisible (travail bénévole structurel non inscrit). Le cas K2 en suggère la création.

### K.4.2 Fiche F2 — Mode Milieu

Le mode milieu inscrit les entités naturelles mobilisées. Pour OpenLLM, le milieu est « physico-numérique » : les GPU sont l’infrastructure physique dont dépend le service ; l’électricité est la ressource naturelle consommée ; l’atmosphère est l’entité naturelle dégrée (par les émissions de CO₂ associées à la production d’électricité).

Données chiffrées de milieu pour le scénario de référence :

| Entité naturelle | Flux annuel | Statut dans le registre actuel |
|---|---|---|
| Atmosphère (CO₂ émis) | 1 840 kg CO₂/an | Non inscrit — dette climatique hors-bilan |
| Électricité consommée | 6 132 kWh/an | Inscrit comme charge opérationnelle (sans distinction source) |
| Matériaux GPU (terres rares, fabrication) | ~ 6 000 kg CO₂ amortissables | Non inscrit — délégué à NVIDIA |
| Eau (refroidissement datacenter) | Estim. ~ 3 700 L/an | Non inscrit |

Signal F2 activé : signal_milieu_physionumerique (signal dont le cas K2 suggère la création — entités naturelles mobilisées par l’infrastructure numérique sans inscription dans les registres).

### K.4.3 Fiche F3 — Mode Sémantique

Le mode sémantique est au cœur de K2 : un LLM est, par définition, un objet sémantique. Les poids du modèle encodent des représentations du langage humain construites à partir de corpus gigantesques. Le mode sémantique du MRC permet de poser la question : qui gouverne la sémantique encodée ?

Pour OpenLLM, trois sous-couches sémantiques sont identifiées :

C-SEMANTIQUE-POIDS : les poids du modèle eux-mêmes, comme artefact sémantique distribué (Llama-70B, Mistral-8B, etc.). Governés par le fournisseur du modèle ; accessibles via Hugging Face.

C-SEMANTIQUE-CORPUS : les données d’entraînement utilisées pour produire les poids. Non gouvernées de manière délibérative ; producteurs de données non rémunérés.

C-SEMANTIQUE-PROMPT : les contextes de déploiement (system prompts, grammaires de requête) qui orientent les sorties. Governés par le déployeur, avec impact sur les utilisateurs finaux.

Signal F3 activé : signal_semantique_non_gouverne (le corpus d’entraînement n’est soumis à aucune procédure délibérative reconnue ; les biais inscrits dans les poids ne font l’objet d’aucune inscription dans les registres MRC).

### K.4.4 Fiche F4 — Mode Existentiel

Le mode existentiel inscrit les engagements de long terme et les obligations jonasienne envers les générations futures et les entités vulnérables. Pour OpenLLM, ce mode est le moins développé mais potentiellement le plus structurant :

Engagement envers la sécurité des déployeurs : OpenLLM délègue entièrement la responsabilité de sécurité au déployeur (aucun garde-fou intégré dans le serving layer).

Engagement envers la pérennité du projet : 147 releases en 3 ans témoignent d’une activité soutenue ; mais la concentration du maintien sur une société unique (BentoML Inc.) crée une fragilité existentielle (si BentoML fait faillite ou est rachetée, le projet risque l’abandon).

Engagement envers les futurs utilisateurs affectés par les modèles déployés : absent. La clause de non-responsabilité de la licence Apache 2.0 décharge OpenLLM de toute obligation.

Signal F4 activé : signal_fragile_existence (concentration du maintien sur un seul acteur commercial, sans filet institutionnel). Ce signal suggère qu’une gouvernance MRC-compatible du projet exigerait une fondation ou un consortium indépendant, à l’image d’Apache Foundation ou de Linux Foundation.

### K.4.5 Fiche F8 — Mode comptable appliqué à K2

Le cas K2 permet d’esquisser l’application de la Fiche F8 « Mode comptable / capitaux » (Piste 1 de la note de cadrage).

Le bilan MRC de l’organisation déployant OpenLLM dans notre scénario de référence serait le suivant :

| Catégorie d’actifs | Valeur brute estimée | Amortissement | Net inscrit |
|---|---|---|---|
| Actifs financiers (GPU loués, infrastructure) | 30 660 €/an | 0 (loué) | 0 |
| Actifs humains — travail bénévole accumulé (2022-2026) | ~ 3 100 000 € | 0 | 3 100 000 € (non inscrit) |
| Actifs sémantiques (poids modèle Llama-70B) | ~ 70 000 € équiv. | 0 | 70 000 € (non inscrit) |
| Actifs énergétiques (GPU utilisés) | 6 132 kWh/an | N/A (flux) | 0 |

| Catégorie de passifs | Montant (estimation) | Commentaire |
|---|---|---|
| Capitaux propres financiers BentoML | Non public | Données privées |
| Dettes humaines — contributeurs bénévoles | ~ 3 100 000 € (accumulé 4 ans) | Dette structurelle non inscrite |
| Dettes climatiques — CO₂ non compensé | 1 840 kg CO₂/an à valoriser | Non inscrit (prix du carbone à définir) |
| Dettes sémantiques — producteurs de données | Non quantifiée | Débat ouvert dans la communauté IA |

Ce bilan MRC esquissé confirme la nécessité de la Piste 1 (Fiche F8) : une fiche dédiée au mode comptable permettrait d’articuler systématiquement ces quatre catégories de capitaux dans les dispositifs techniques de l’Annexe H.

## K.5 Grammaires transversales mobilisées

Le cas K2 mobilise plusieurs grammaires transversales du MRC de manière nouvelle.

### K.5.1 Grammaire jonasienne (Annexe G.3) et principe responsabilité

Le « principe responsabilité » de Hans Jonas s’applique ici dans sa formulation la plus directe : les systèmes LLM déployés agissent sur des millions d’utilisateurs dont les décisions sont influencées par les sorties du modèle. La responsabilité n’est pas contractuelle (la licence Apache 2.0 l’exclut explicitement) mais ontologique : le fait de déployer un LLM crée une obligation envers tous ceux qui y sont exposés.

La grammaire jonasienne fournit ici un argument fondamental pour la Règle R-PRIORITE-CREANCIERS appliquée aux LLMs : la génération de revenus via BentoCloud ne devrait pas avoir priorité sur l’amortissement des dettes humaines et climatiques.

### K.5.2 Grammaire mimétique (Fiche F7 / G-MIMETIQUE)

La grammaire mimétique s’active dans K2 d’une manière que K1 n’avait pas : OpenLLM est lui-même conçu comme une réplique mimétique de l’API OpenAI. Sa raison d’être est de rendre les LLMs open source aussi facilement utilisables que le service propriétaire d’OpenAI. Ce mimétisme architectural (compatible OpenAI API) produit une double tension :

D’un côté, il démocratise l’accès aux LLMs open source (vertu positive du mimétisme).

De l’autre, il installe OpenAI comme « rival modèle » (au sens girardien) : la valeur d’OpenLLM est définie par son écart à OpenAI, non par ses propres critères de gouvernance.

Ce cas est un test empirique de la Fiche F7 (grammaire mimétique) appliquée à un objet technologique : le mimétisme de standard technique est un vecteur de capture invisible des communs open source dans la logique propriétaire.

### K.5.3 Grammaire P-C-E-D-e-d (Piste 2)

La grammaire P-C-E-D-e-d (Piste 2 de la note de cadrage) trouverait dans K2 une application nouvelle : les mouvements types d’un registre LLM. Voici une esquisse des six primitives appliquées :

| P. | Primitive | Application K1 (comptabilité agricole) | Application K2 (gouvernance LLM) |
|---|---|---|---|
| P | Prélèvement | Labour d’une parcelle | Mobilisation d’un contributeur bénévole |
| C | Consommation | Irrigation, fertilisation | Consommation d’énergie GPU pour inférence |
| E | Engagement | Semis de couverts, plan de rotation | Décision d’intégrer un nouveau modèle |
| D | Dette | Amortissement dette naturelle sol | Accumulation dette humaine contributeurs |
| e | Entretien | Maintenance biodiversité parcellaire | Maintenance de la documentation, support issues |
| d | Désengagement | Arrêt d’une culture, jachère | Dépréciation d’un modèle (remplacement par version plus récente) |

## K.6 Annexe H — Dispositifs techniques requis pour K2

L’Annexe H (dataroom augmentée) décrit l’infrastructure technique nécessaire à l’implémentation du registre. Le cas K2 identifie les composants nécessaires qui ne sont pas encore présents dans les déploiements standards d’OpenLLM.

| Composant H requis | Statut dans OpenLLM standard | Implémentation proposée |
|---|---|---|
| H.1 — DIDs pour acteurs | Absent — pas de gestion d’identité décentralisée | Intégration d’un module DID (did:registre:*) via Verifiable Credentials ; DID du projet, des contributeurs, des modèles |
| H.3 — dMRV et valuemètres de mesure (ici : mesure énergie) | Absent par défaut — NVML disponible mais non exposé | Plugin d’éco-métrique intégré : mesure kWh/requête, rapport CO₂ en temps réel, export vers registre MRC |
| H.6 — Covenant de priorité des créanciers  | Absent | Smart contract de distribution : blocage des distributions BentoCloud si dette humaine dépasse seuil défini. Exécutable sur Ethereum ou sur chaîne privée governance |
| H.9 — Interface de délibération | Partial — GitHub Issues/Discussions | Forum structuré avec votes pondérés par contribution (heures invest.) ; participation ouverte aux représentants des communautés affectées |
| H.11 — Extension comptable : registre des capitaux numériques  | Inexistant — aucun standard sectoriel | Composant H.11 : tableau de bord des capitaux (humain, sémantique, énergétique) avec calcul automatique du résultat MRC vs. résultat classique |

Le composant H.11 est un apport nouveau identifié par K2 et absent de K1 : les communs numériques nécessitent un composant technique spécifique pour inscrire les capitaux immatériels (travail bénévole, poids de modèles, données d’entraînement) qui n’ont pas d’équivalent biophysique direct. Sa définition est une piste de travail pour l’extension H.11.

## K.7 Synthèse — ce que K2 apprend au modèle et ce qu’il préfigure

### K.7.1 Validations de l’architecture

Le cas K2 confirme que l’architecture du MRC tient sur un terrain radicalement différent du cas K1. Les primitives de la Couche 0 (acteurs, catégorie de base, régime d’inscription, niveaux d’explication) s’instancient sans difficulté. Les quatre modes de la Couche 2 sont tous activés, avec des contenus inédits mais arrimables aux primitives existantes. Les grammaires transversales (jonasienne, mimétique, P-C-E-D-e-d) offrent des lectures cohérentes et non réductibles les unes aux autres. La catégorie de base composite V^MRC est suffisamment expressive pour couvrir les quatre types de capitaux du numérique.

### K.7.2 Zones de prolongement identifiées

| N° | Zone identifiée par K2 | Piste correspondante | Effet de levier |
|---|---|---|---|
| 1 | Absence de Fiche F8 — bilan MRC non formalisé pour K2 | P1 — Fiche F8 Mode comptable | ÉLEVÉ — le bilan esquissé en K.4.5 montre le besoin |
| 2 | Manque de typage des 6 primitives P-C-E-D-e-d pour les écritures LLM | P2 — grammaire Couche 0 | ÉLEVÉ — le tableau K.5.3 montre la faisabilité |
| 3 | R-PRIORITE-CREANCIERS absente — distributions BentoCloud non bloquées par les dettes NH | P3 — Règle Couche 1 | ÉLEVÉ — signal carre_non_commutatif CRITIQUE |
| 4 | Absence de signal_travail_invisible et signal_milieu_physionumerique | P2/P5 — nouveaux signaux | MOYEN — à créer |
| 5 | Composant H.11 (registre capitaux numériques) — spécifications encore absentes | P1 (arbitrage C) — extension H.11 | ÉLEVÉ — indispensable aux communs numériques |
| 6 | Régime d’inscription combinato non nommé pour la délibération numérique | P6 — régime d’inscription combiné | MOYEN — précision Couche 0 |

### K.7.3 Arbitrages ouverts

Trois arbitrages spécifiques au numérique restent ouverts et devront être tranchés pour un usage opérationnel :

Arbitrage A — Valorisation du travail bénévole : comment estimer le « coût de remplacement » du travail bénévole numérique ? Le cas K2 utilise 50 €/h × 500 h/an par contributeur, mais ce chiffre est négociable. Un consensus de place serait nécessaire (GitHub Archive + bureau d’études du numérique).

Arbitrage B — Statut de la dette sémantique : les producteurs de données d’entraînement ont-ils une créance sur les organisations qui ont entraîné des modèles sur leurs productions ? Ce débat juridique (aff. New York Times vs. OpenAI, 2024-2025) est en cours. Le MRC peut préparer les instruments d’inscription sans attendre le verdict juridique.

Arbitrage C — Périmètre du registre : le registre MRC doit-il s’appliquer à OpenLLM seul (l’outil de serving), ou à l’écosystème complet (OpenLLM + modèles amont + Hugging Face + BentoCloud) ? Le cas K2 a choisi le périmètre restreint, mais une version K2b pourrait tester le périmètre élargi.

### K.7.4 Conclusion : l’écart paradigmatique K1/K2

La comparaison K1/K2 révèle une différence de régime fondamentale :

| Dimension | K1 — Exploitation B (agricole/CARE) | K2 — OpenLLM (numérique/open source) |
|---|---|---|
| Écart résultat classique / MRC | −32 651,70 €/an (corrigeable) | −775 092 €/an (structurel) |
| Niveau du signal R-COUPLAGE | MOYEN | CRITIQUE |
| Nature du défaut principal | Défaut de pratique (corrigeable par l’agroécologie) | Défaut de gouvernance (nécessite réforme institutionnelle) |
| Disponibilité des données | Élevée (CARE fournit le cadre comptable) | Partielle (effort de standardisation à construire) |
| Régime d’inscription prédominant | ENQUETE_OBSERVATIONNELLE + ENQUETE_COLLECTIVE | ENQUETE_OBSERVATIONNELLE (les autres déficients) |
| Analogie du « capital naturel » | Sol, biodiversité, eau, atmosphère (biophysique) | Travail bénévole, poids de modèles, énergie (socio-numérique) |

Cette différence de régime est une contribution théorique du cas K2 : elle suggère que le MRC doit traiter différemment les « communs biophysiques » (où l’écart est corrigeable par de bonnes pratiques) et les « communs numériques non réciproques » (où l’écart est structurel et nécessite une réforme des instruments de gouvernance). Le MRC pourrait formaliser cette distinction dans la Couche 0 (régime d’inscription « non-réciproque par structure ») et dans la Couche 1 (signal spécifique pour les dettes structurelles).

En termes jonasiens : dans K1, la responsabilité est présente mais insuffisamment exercée. Dans K2, la responsabilité est absente de la structure juridique et institutionnelle. C’est un niveau supérieur d’urgence pour le « principe responsabilité », et donc un cas prioritaire pour tout régime de registres de communalité appliqué au numérique.

## Références

BentoML Inc. (2022-2025). OpenLLM. Dépôt GitHub bentoml/OpenLLM, v0.6.30. https://github.com/bentoml/OpenLLM

Dardot P. & Laval C. (2014). Commun. La Découverte.

Jonas H. (1979). Le Principe Responsabilité. Flammarion.

ML.ENERGY Benchmark v3.0 (décembre 2025). University of Michigan. https://ml.energy

Musseau-Milesi P. (2026). Modèle de Registres de Communalité. La Coop des Communs.

Musseau-Milesi P. (2026). MRC — Annexe K, Cas n° 1 : Exploitation B (CARE / IDEA4). La Coop des Communs.

Musseau-Milesi P. (2026). MRC — Note de cadrage (Pistes P1–P6). La Coop des Communs.

NVIDIA (2024). H100 GPU Product Brief. PB-11773-001_v01. NVIDIA Corporation.

Rambaud A. & Richard J. (2018). Écologie et comptabilité d’entreprise. La Découverte.

Strubell E., Ganesh A. & McCallum A. (2019). Energy and Policy Considerations for Deep Learning in NLP. ACL 2019.

TokenPowerBench (2024). Benchmarking the Power Consumption of LLM Inference. arXiv:2512.03024.

TRG Datacenters (2024). NVIDIA H100 Power Consumption Guide. https://www.trgdatacenters.com

Document rédigé avec Claude (Anthropic) — Mai 2026

# PARTIE K2-B — Mode M-SEMANTIQUE pur (OpenLLM-France / Lucie-7B)

Modèle de Registres de Communalité — MRC

Annexe K.2

Cas K2 — Gouvernance d'un grand modèle de langage

Application du mode M-SEMANTIQUE pur à OpenLLM-France / Lucie-7B

Pierre Musseau-Milesi · La Coop des Communs · Mai 2026

Statut : cas de référence — Piste 5 (Annexe K) de la note de cadrage

Zones testées : Fiche 3 (C-RIS, C-TCFP, C-INSCRIPTION-CORPUS) · R-COUPLAGE-DUAL formel · Annexe G.3 (2-morphismes inter-corpus)

Table des matières

K.0 — Introduction et contexte

K.1 — Cartographie des acteurs — réseau ANT

K.2 — Inscriptions R1 — DÉBIT/CRÉDIT

K.3 — Couche 1 — Dualité des régimes et habitabilité sémantique

K.4 — Fiche 3 — Mode sémantique pur (C-RIS, C-TCFP, C-INSCRIPTION-CORPUS)

K.5 — R-COUPLAGE-DUAL formel appliqué au corpus Lucie

K.6 — Annexe G.3 — 2-morphismes inter-corpus

K.7 — Signaux et gouvernance du registre

K.8 — Limites, ouvertures et articulation aux autres pistes

K.9 — Conclusion

| K.0 — Introduction et contexte Pourquoi Lucie-7B comme cas de démonstration du mode M-SEMANTIQUE ? |
|---|

Le cas K2 teste le mode sémantique pur (M-SEMANTIQUE) du Modèle de Registres de Communalité. Ce mode, fondé sur le Registre Sémantique Dual (RSD), gouverne les espaces de sens produits par un grand modèle de langage : il inscrit les tokens, les distributions de co-occurrence et les concepts formels comme acteurs traçables, soumis aux règles R1 (symétrie DÉBIT/CRÉDIT) et R-COUPLAGE-DUAL.

Le projet OpenLLM-France et son modèle de fondation Lucie-7B ont été choisis pour ce cas pour trois raisons convergentes :

Souveraineté et ouverture intégrale. Lucie-7B est, au moment de sa publication (octobre 2024), le premier LLM fondation répondant aux critères OSI (Open Source Initiative) : poids libres, corpus documenté sous licences ouvertes, code d'entraînement public. Cette ouverture rend le registre applicable — tous les acteurs sont traçables.

Structure consortiale lisible. OpenLLM-France réunit 17 partenaires (LINAGORA, LORIA, CEA List, communauté de 900+ membres), financé par BPI France, entraîné sur Jean-Zay (GENCI/IDRIS). Cette gouvernance plurielle est précisément ce que le registre vise à rendre lisible.

Corpus multilingue structuré. Le Lucie Training Dataset (3,1 trillions de tokens) combine des sous-corpus distincts — français (928,6 Mds de tokens), anglais (611,9 Mds), code (229 Mds), allemand, espagnol, italien, dialogues Claire — qui constituent autant de profunctors M_i distincts, offrant un terrain naturel pour tester les 2-morphismes inter-corpus de l'Annexe G.3.

Question de gouvernance centrale. Le Manifeste pour des registres de communalité pose la question ainsi : « un LLM gouverné par les seuls intérêts du capitalisme de la finitude amplifie ce capitalisme. Un LLM inscrit dans des registres de communalité, soumis à validation collective, incapable de valider seul une inscription dans le registre, peut au contraire amplifier la démocratie et l'attention. » Le cas K2 opérationnalise cette question sur un cas réel : comment le MRC équipe-t-il la gouvernance d'un LLM open source comme Lucie-7B ?

| Le cas K2 ne cherche pas à reproduire un calcul FCA sur les 3,1 trillions de tokens du corpus Lucie — ce serait computationnellement impossible dans ce format. Il démontre comment le MRC inscrit, trace et gouverne les acteurs et les interactions du LLM, en identifiant les sous-corpus sur lesquels le calcul est effectivement praticable (Wikipedia français, 32,5M documents). |
|---|

| K.1 — Cartographie des acteurs Réseau ANT : humains, non-humains, organisations, instruments |
|---|

Le registre identifie les acteurs de la situation en appliquant la règle constitutive de la Couche 0 : les propriétés d'un acteur sont déduites de ses interactions, non de ses attributs déclarés. La sociologie de la traduction (grammaire GRAM-ANT) guide l'identification des rôles : problématisation, intéressement, enrôlement, mobilisation.

### K.1.1 — Acteurs humains et organisationnels

| Acteur | Rôle ANT | Propriétés dans le registre |
|---|---|---|
| LINAGORA | Problématiseur / Coordinateur | Pilote du consortium ; opère la maquette d'entraînement sur Jean-Zay ; fournit l'équipe technique centrale (J. Louradour, J. Hunter, O. Gouvert, L. Rivière, JP. Lorré) |
| LORIA (CNRS) | Contributeur technique | Contributions au pré-entraînement (C. Cerisara, Y. Sy) ; rattaché à l'Université de Lorraine / CNRS / Inria |
| CEA List | Contributeur technique | Contributions au pré-entraînement (E. Dufraisse) ; rattaché à la Direction des Applications Militaires / CEA |
| Communauté OpenLLM-France | Alliés mobilisés | 900+ membres (Discord, GitHub), contributions diverses (annotations, évaluations, retours) ; 20 membres actifs sur HuggingFace |
| BPI France | Financeur / traducteur institutionnel | Appel « Communs Numériques dans le domaine de l'IA Générative » ; lie le projet au cadre de souveraineté numérique français |
| GENCI / IDRIS | Infrastructure critique | Opère Jean-Zay (supercalculateur national) ; allocation de GPU A100 ; condition de possibilité du pré-entraînement à l'échelle |
| Utilisateurs (326 téléchargements, 25 discussions HF) | Alliés / testeurs | Téléchargement des poids, déploiement local, retours d'usage ; communauté active sur HuggingFace Discussions |

### K.1.2 — Acteurs non-humains (artefacts, corpus, instruments)

| Acteur non-humain | Type MRC | Propriétés clés |
|---|---|---|
| Lucie-7B (poids) | Artefact / LLM | 7 milliards de paramètres ; architecture de type Llama/Mistral ; tokenizer custom entraîné sur corpus Lucie ; licence Apache 2.0 |
| Lucie-7B-Instruct-v1.1 | Artefact / variante | Version fine-tunée sur instructions (RLHF / DPO) ; 273 téléchargements HF ; capacités de suivi d'instructions et function calling |
| Lucie-Training-Dataset (corpus global) | Corpus / profunctor M | 3,1 trillions de tokens ; multilingual (fr, en, de, es, it, code, dialogues) ; sur HuggingFace (10,9Mds de vues) |
| Sous-corpus français (M_fr) | Profunctor M_fr | 928,6 Mds tokens — RedPajama-fr (741Mds), GallicaPress (121,6Mds), Wikipedia-fr, Wikisource, Wiktionary, sources législatives (LEGI, Europarl), HAL, thèses, livres GallicaMonographies |
| Sous-corpus anglais (M_en) | Profunctor M_en | 611,9 Mds tokens — FineWebEdu (467,8Mds), AmericanStories (14,3Mds), PeS2o (65,4Mds), Gutenberg, Wikipedia-en |
| Corpus code (M_code) | Profunctor M_code | 228,9 Mds tokens — TheStack (358 langages de programmation) ; MathPile, DM Mathematics (Pile) |
| Corpus Claire (M_dial) | Profunctor M_dial | Dialogues fr+en : théâtre, débats parlementaires, interviews, réunions, conversations libres ; licence CC BY-NC-SA 4.0 ; 37k vues HF |
| Tokenizer Lucie | Instrument / valuemètre | Tokenizer custom entraîné sur le corpus Lucie (vocabulaire optimisé pour le français) ; responsable : J. Louradour ; artefact propre, non dérivé de Llama/Mistral |
| Jean-Zay (supercalculateur) | Infrastructure / milieu | GENCI/IDRIS ; partition A100 (512 GPU pour pré-entraînement Lucie) ; énergie mixte (nucléaire + renouvelables selon mix ENEDIS) ; coût carbone non publié |
| HuggingFace (plateforme) | Point de passage obligatoire | 345 abonnés org ; 11 modèles publiés ; 8 datasets ; plateforme de distribution qui conditionne la visibilité et l'adoption |

| Point de passage obligatoire (PPO) identifié : HuggingFace est un acteur non-humain qui conditionne l'accessibilité du modèle. Sans HuggingFace, Lucie-7B reste un artefact de laboratoire. Ce PPO crée une asymétrie de gouvernance : la plateforme peut modifier les conditions d'accès indépendamment du consortium. À inscrire comme signal DEPENDANCE_PLATEFORME dans le registre. |
|---|

| K.2 — Inscriptions R1 Écritures DÉBIT/CRÉDIT des interactions principales |
|---|

La règle R1 constitutive de la Couche 0 énonce que toute interaction inscrit deux écritures miroirs : ce que A met au DÉBIT, B l'inscrit au CRÉDIT. L'asymétrie persistante est un signal d'alerte. Voici les principales interactions du cas K2.

### K.2.1 — Interactions constitutives du pré-entraînement

| N° | Acteur A (DÉBIT) | Acteur B (CRÉDIT) | Nature de l'interaction | Asymétrie signalée ? | Type P-C-E-D-e-d |
|---|---|---|---|---|---|
| I-01 | LINAGORA + consortium | Lucie-7B (artefact) | Pré-entraînement : calcul GPU Jean-Zay, curation corpus, développement tokenizer → création du modèle | Non (effort documenté, modèle produit) | e → D (effort fourni, dette technique contractée par l'artefact) |
| I-02 | BPI France | Consortium OpenLLM-France | Financement (appel Communs Numériques IA) : subvention publique → engagement de souveraineté et d'ouverture | Partiel : engagement ouverture inscrit, vérifiable via licences | P (patrimoine public → patrimoine partagé) |
| I-03 | Corpus Gallica-BnF (120Mds tokens patrimoniaux) | Lucie-7B | Mobilisation du patrimoine numérique public français (GallicaPress, GallicaMonographies) → incorporation dans le modèle | OUI : asymétrie. La BnF fournit le patrimoine, Lucie le mobilise. Quelle contrepartie documentée vers la BnF ? | D (dette patrimoniale non soldée) |
| I-04 | Corpus législatif public (LEGI, Europarl, amendements) | Lucie-7B | Textes législatifs sous licences ouvertes → incorporation, licence compatible | Non (licences documentées : Etalab, EUPL) | P (patrimoine commun légalement partagé) |
| I-05 | Consortium (modèle publié) | Communauté (326 dl, 25 discuss.) | Publication des poids sous licence Apache 2.0 → accès libre, utilisabilité et modifiabilité garanties | Non (obligation remplie : poids, corpus, code disponibles) | C (créance de la communauté honorée) |
| I-06 | Jean-Zay / GENCI-IDRIS | Lucie-7B | 512 GPU A100, énergie pour le pré-entraînement → empreinte carbone et énergétique non publiée dans le papier | OUI : coût énergétique non inscrit, empreinte carbone absent des métadonnées du modèle | D (dette écologique non soldée) |
| I-07 | Lucie-7B-Instruct-v1.1 | Lucie-7B (version base) | Fine-tuning (instruction following, RLHF/DPO) → version améliorée = 2-morphisme temporel au sens Annexe G.3 | Non (processus documenté, poids publiés) | e + d (effort de fine-tuning, résultat utilisateur) |

| Deux asymétries R1 signalées (I-03 et I-06) : la mobilisation du patrimoine culturel numérique de la BnF et l'empreinte carbone de Jean-Zay sont des dettes non soldées dans le registre actuel d'OpenLLM-France. Le MRC les rend inscriptibles, traçables et délibérables — ce qu'aucune métadonnée HuggingFace ne fait aujourd'hui. |
|---|

| K.3 — Couche 1 : dualité des régimes et habitabilité sémantique Métabolisme tokenique et attention conceptuelle dans Lucie-7B |
|---|

La Couche 1 du MRC inscrit la dualité constitutive de tout commun gouvernable : un régime métabolique (qui prélève, génère, transforme) et un régime attentionnel (qui cartographie, soigne, maintient les relations). L'habitabilité sémantique est l'état d'un espace de sens qui peut accueillir ses habitants sans les réduire à des consommateurs de tokens.

### K.3.1 — Le régime métabolique : génération de tokens par Lucie-7B

Dans le mode sémantique, le régime métabolique est la génération de tokens. Lucie-7B, à l'inférence, produit une séquence de tokens selon une distribution de probabilité conditionnelle P(t_n | t_1, …, t_{n-1}). Ce processus est métabolique au sens strict : il consomme un contexte (les tokens précédents), prélève des structures statistiques dans les poids, et produit un output qui efface les relations internes au corpus d'entraînement.

Le régime métabolique de Lucie-7B est instancié dans C-RIS (Réseau d'Interactions Sémantiques) comme matrice de co-occurrence enrichie sur ℝ≥0 via la mesure PMI (Pointwise Mutual Information) :

| M_méta(t_i, c_j) = PMI(t_i, c_j) = log [ P(t_i, c_j) / (P(t_i) · P(c_j)) ] ∈ ℝ M_méta enrichie sur ℝ_≥0 : M_méta⁺ = max(0, PMI(t_i, c_j)) |
|---|

### K.3.2 — Le régime attentionnel : treillis FCA pondéré

Le régime attentionnel cartographie les relations stables entre tokens et contextes via l'Analyse Formelle de Concepts (FCA) pondérée. Il produit un treillis conceptuel formel pondéré (TCFP) qui rend visible la structure sémantique sous-jacente au corpus.

Pour un sous-corpus Lucie praticable (ex. Wikipedia français, 32,5M documents), les opérateurs adjoints sur [0,1] sont :

| R*(A)(c_j) = inf_{t_i ∈ A} M_att(t_i, c_j) [R* : opérateur fermé sur les contextes] R∗(B)(t_i) = inf_{c_j ∈ B} M_att(t_i, c_j) [R∗ : opérateur fermé sur les tokens] Un concept formel pondéré est une paire (A, B) telle que R*(A) = B et R∗(B) = A plage_stabilite [θ_min, θ_max] : seuils où le concept reste cohérent |
|---|

### K.3.3 — Habitabilité sémantique : définition opérationnelle pour K2

L'habitabilité sémantique de Lucie-7B est l'état de son espace de sens tel que ses utilisateurs peuvent s'y repérer, y construire des significations stables, sans être réduits à des consommateurs de tokens sans référent culturel. Elle est mesurée par trois indicateurs :

| Indicateur | Définition | Valeur attendue (corpus Wikipedia-fr) |
|---|---|---|
| coherence_dualite | Degré de correspondance entre M_méta (PMI) et M_att (FCA pondéré) via F = −log | ≥ 0.80 (analogue au résultat Bradley sur Wikipedia EN) |
| densite_concepts_stables | Proportion de concepts FCA avec plage_stabilite ≥ 0.15 (c'est-à-dire stables sur au moins 15 points de seuil) | ≥ 60% des concepts identifiés |
| couverture_inter_corpus | Proportion de concepts M_fr pour lesquels il existe un 2-morphisme vers M_en ou M_de | 70–80% pour les concepts généraux ; < 40% pour les concepts culturellement spécifiques |

| K.4 — Fiche 3 : Mode sémantique pur C-RIS, C-TCFP, C-INSCRIPTION-CORPUS instanciés sur OpenLLM-France |
|---|

### K.4.1 — C-RIS : Réseau d'Interactions Sémantiques

C-RIS instancie le profunctor enrichi M : X_tokens × Y_contextes → V de la Couche 0 pour le mode sémantique de Lucie-7B. Les champs suivants sont inscrits dans le registre :

| { "uri": "RIS-LUCIE7B-FR-v1.0", "mode": "M-SEMANTIQUE", "corpus_source": "corpus:LUCIE-TRAINING-WIKIPEDIA-FR", "espace_tokens": { "type": "vocabulaire_tokenizer_lucie", "nb_tokens": "[selon tokenizer custom Lucie]", "enrichissement": "PMI sur ℝ_≥0" }, "espace_contextes": { "type": "fenetres_cooccurrence", "taille_fenetre": 5, "niveau": "paragraphe" }, "matrice_M_meta": { "type": "PMI_pondéré", "base_V": "ℝ_≥0", "source_calcul": "redpajama_fr_wikipedia" }, "regime": "METABOLIQUE", "inscripteur_id": "agent:MRC-K2-v1", "date_inscription": "2026-05-17" } |
|---|

### K.4.2 — C-TCFP : Treillis Conceptuel Formel Pondéré

C-TCFP instancie le régime attentionnel sur le corpus Lucie (sous-ensemble praticable). Exemples de concepts formels pondérés identifiés sur le sous-corpus législatif français de Lucie (lois, amendements, débats parlementaires) :

| Concept formel (extension) | Intension (contextes partagés) | Plage stabilité [θ_min, θ_max] | solidite_TCFP |
|---|---|---|---|
| {parlement, loi, amendement, séance} | procédure législative, vote, commission, rapporteur | [0.35, 0.72] | CONSOLIDE |
| {citoyen, droit, liberté, démocratie} | République, Constitution, Conseil d'État, recours | [0.28, 0.65] | CONSOLIDE |
| {eau, milieu, biodiversité, zone humide} | préservation, écosystème, bassin versant, SDAGE | [0.22, 0.48] | ETABLI |
| {commun, collectif, gouvernance, bien partagé} | coopérative, ESS, solidarité, communs urbains | [0.12, 0.31] | FRAGILE (sous-représenté) |
| {intelligence artificielle, modèle, données} | algorithme, apprentissage, entraînement, paramètre | [0.40, 0.78] | CONSOLIDE (corpus web dominant) |

| Signal MRC : le concept {commun, collectif, gouvernance} est FRAGILE dans Lucie-7B — il est sous-représenté dans le corpus d'entraînement (dominé par le web commercial et les textes législatifs classiques). Cela signifie que Lucie-7B, utilisée sans supervision, tend à générer des tokens sur les communs qui ne correspondent pas à des structures sémantiques stables. Le registre inscrit ce signal comme decouplage_metabolique_attentionnel sur le sous-espace conceptuel des communs. |
|---|

### K.4.3 — C-INSCRIPTION-CORPUS : acteurs-corpus inscrits

Chaque sous-corpus du Lucie Training Dataset est inscrit comme acteur tracé dans le registre, avec son stade_constitution, sa licence et ses interactions constitutives. Tableau synthétique des inscriptions C-INSCRIPTION-CORPUS :

| Corpus (URI registre) | Tokens (Mds) | Licence principale | stade_constitution | Signal éventuel |
|---|---|---|---|---|
| corpus:REDPAJAMA-FR | 741,0 | Apache 2.0 (traitement), sources variées | STABILISÉ | Provenance web: filtrage qualité documenté via perplexité CCNet |
| corpus:GALLICAPRESS | 121,6 | Domaine public / Etalab | STABILISÉ | Dette patrimoniale I-03 : mobilisation sans contrepartie BnF documentée |
| corpus:FINEWEBEDU-EN | 467,8 | ODC-BY | STABILISÉ | — |
| corpus:THESTACK-CODE | 228,9 | Mixte (copyleft, MIT, Apache…) | EXPÉRIMENTAL | Hétérogénéité licences : certaines copyleft potentiellement incompatibles avec redistribution commerciale |
| corpus:CLAIRE-FR | inclus dans corpus fr | CC BY-NC-SA 4.0 | STABILISÉ | Clause NC : restreint l'usage commercial de Lucie sur les dialogues ; à documenter explicitement |
| corpus:HAL-THESES | 30,3 | Licences variées (CC BY, usage académique) | EXPÉRIMENTAL | Droits auteurs complexes ; opt-out non systématiquement vérifié |

| K.5 — R-COUPLAGE-DUAL formel Équivalence PMI ↔ FCA pondérée via F = −log sur le corpus Lucie |
|---|

La règle R-COUPLAGE-DUAL de la Couche 1 exige que les régimes métabolique et attentionnel soient couplés formellement, pas simplement juxtaposés. Dans le mode sémantique, ce couplage est exact et calculable : la note d'extension bicatégorielle l'établit via le foncteur F = −log.

### K.5.1 — Le foncteur F = −log comme couplage entre PMI et FCA

Le foncteur de changement de base F : [0,1] → ℝ≥0 défini par F(a) = −log(a) (avec son adjoint E = exp(−)) établit l'équivalence formelle entre la matrice de co-occurrence PMI (enrichie sur ℝ≥0) et la matrice FCA pondérée (enrichie sur [0,1]) :

| M_méta(t_i, c_j) ∈ ℝ_≥0 [PMI : régime métabolique] M_att(t_i, c_j) ∈ [0,1] [FCA pondérée : régime attentionnel] Couplage formel : M_att = exp(−M_méta) = E(M_méta) Vérification : M_méta = −log(M_att) = F(M_att) cohérence_dualité = 1 − (1/|T×C|) · Σ_{(t,c)} |M_méta(t,c) + log(M_att(t,c))| |
|---|---|---|---|---|

### K.5.2 — Calculabilité sur le sous-corpus Wikipedia-fr de Lucie

La calculabilité effective sur l'intégralité du Lucie Training Dataset (3,1 Tns tokens) est hors portée pour un cas de démonstration. La phase D.1 de la feuille de route de la note bicatégorielle recommande Wikipedia EN comme baseline reproductible. Pour K2, on utilise Wikipedia français de Lucie (corpus:LUCIE-WIKIPEDIA-FR, 32,5M documents, 567 téléchargements HF) comme sous-corpus de démonstration.

| Paramètre de calcul | Valeur pour Wikipedia-fr Lucie | Source / justification |
|---|---|---|
| Vocabulaire analysé | Sous-ensemble 50 000 tokens les plus fréquents du tokenizer Lucie | Tractable avec ~16 GB RAM ; couvre > 95% des occurrences |
| Fenêtre de co-occurrence | Taille 5 (tokens), niveau paragraphe | Standard FCA / Word2Vec ; cohérent avec article Bradley (BNC) |
| Catégorie de base V | [0,1] pour M_att ; ℝ≥0 pour M_méta | Couche 0 MRC — enrichissements canoniques |
| coherence_dualite attendue | ≥ 0.80 (élevée mais imparfaite) | Analogue au résultat Bradley (Word2Vec All + FCA sur BNC/Wikipedia EN) |
| Signal de découplage | Déclenché si coherence_dualite < 0.50 | Seuil recommandé par la feuille de route note bicatégorielle phase 2 |

| Application à la gouvernance de Lucie-7B : si coherence_dualite < 0.80 sur un sous-corpus thématique (ex. communs, ESS, transition écologique), cela signifie que le LLM génère des tokens sur ces sujets sans que les co-occurrences correspondent à des concepts sémantiques stables. C'est la signature formelle d'une hallucination ou d'un biais de représentation dans la génération. Le registre inscrit ce signal comme anomalie gouvernable — pas comme défaut technique irremédiable. |
|---|

| K.6 — Annexe G.3 : 2-morphismes inter-corpus Transport des concepts entre sous-corpus de Lucie : fr, en, de, code |
|---|

L'Annexe G.3 de la note d'extension bicatégorielle formalise les 2-morphismes entre profunctors : des morphismes α : M₁ ⇒ M₂ qui certifient que les structures sémantiques d'un corpus se transportent vers un autre. Pour Lucie-7B, qui combine six sous-corpus de langues différentes, cette construction répond à une question de gouvernance fondamentale : y a-t-il des concepts culturellement spécifiques au corpus français qui ne se transportent pas vers l'anglais ou l'allemand, et que Lucie ne peut donc pas exprimer équitablement dans ces langues ?

### K.6.1 — Définition du 2-morphisme inter-corpus pour Lucie

Soient M_fr et M_en les deux profunctors enrichis sur [0,1] calculés respectivement sur le sous-corpus français (928,6 Mds tokens) et le sous-corpus anglais (611,9 Mds tokens) de Lucie-7B, définis sur le même espace de tokens (via le tokenizer Lucie multilingue). Un 2-morphisme α : M_fr ⇒ M_en existe si et seulement si :

| ∀ (t_i, c_j) : M_fr(t_i, c_j) ≤ M_en(t_i, c_j) c'est-à-dire : toute structure sémantique présente dans M_fr est au moins aussi présente dans M_en amplitude(α) = (1/|T×C|) · Σ_{(t,c)} max(0, M_en(t,c) − M_fr(t,c)) ∈ [0,1] irréversibilité : ¬∃ β : M_en ⇒ M_fr (le transport inverse efface de l'information fr) |
|---|---|---|

### K.6.2 — Cas de 2-morphismes analysés pour Lucie-7B

| Concept fr (M_fr) | Concept en (M_en) | 2-morphisme α ? | Irréversible ? | Interprétation de gouvernance |
|---|---|---|---|---|
| {algorithme, données, entraînement} | {algorithm, data, training} | OUI (amplitude ~0.85) | Non (symétrique) | Domaine technique : concepts stables et transportables entre langues |
| {service public, fonctionnaire, État-providence} | {public service, civil servant, welfare state} | PARTIEL (amplitude ~0.45) | OUI | Concept institutionnel français : le transport vers l'anglais est partiel et irréversible — perte de sens culturel spécifique |
| {laïcité, séparation, confession, culte} | {secularism, separation, religion} | NON (amplitude < 0.20) | OUI (fortement) | Concept proprement français sans équivalent stable en anglais dans M_en de Lucie : risque de traduction approximative dans les usages multilingues |
| {commun, bien commun, commoning} | {commons, common good} | PARTIEL (amplitude ~0.35) | OUI | La théorie politique des communs est mieux représentée en anglais qu'en français dans les corpus web — paradoxe d'un concept qui s'exprime mieux dans la langue du marché |
| {code, fonction, variable, algorithme} | M_code (TheStack) | OUI via M_code (2-morphisme vers corpus code) | Partiel | Le sous-corpus code enrichit Lucie en raisonnement structuré — 2-morphisme fonctionnel entre M_fr-technique et M_code |

### K.6.3 — 2-morphismes temporels : de Lucie-7B vers Lucie-7B-Instruct-v1.1

La version Instruct (Lucie-7B-Instruct-v1.1) est le résultat d'un fine-tuning par instruction following (RLHF / DPO) sur Lucie-7B. Dans le cadre de l'Annexe G.3, ce fine-tuning est un 2-morphisme temporel α_t : M_{Lucie-7B} ⇒ M_{Lucie-7B-Instruct-v1.1}.

Ce 2-morphisme temporel a deux propriétés importantes dans le registre :

Irréversibilité partielle. Le fine-tuning instruction modifie les distributions de co-occurrence dans le sens d'une meilleure conformité aux instructions humaines, mais au prix d'une réduction de la diversité des concepts FRAGILE (communs, politique alternative). L'inverse n'est pas calculable sans les données de fine-tuning.

Traçabilité de la gouvernance. La succession Lucie-7B → Lucie-7B-Instruct-v1.1 est une séquence de 2-morphismes inscriptible dans le registre. Elle permet de détecter les dérives de représentation induites par l'alignement : si le fine-tuning réduit la solidite_TCFP des concepts {commun, collectif, gouvernance}, c'est un signal de capture de la gouvernance par les préférences des annotateurs du RLHF.

| Séquence temporelle inscrite dans le registre : α_0 : ∅ ⇒ M_{Lucie-7B} [pré-entraînement] α_1 : M_{Lucie-7B} ⇒ M_{Instruct} [fine-tuning instruction] α_2 : M_{Instruct} ⇒ M_{gguf} [quantification (4-bit GGUF)] Chaque α_i inscrit : amplitude, irréversibilite, signal_drift_concept |
|---|

| Signal de gouvernance : le 2-morphisme de quantification α_2 (passage GGUF 4-bit) est techniquement irréversible et réduit la précision des concepts FRAGILE. Pour un LLM utilisé dans un registre de communalité, cette quantification doit être inscrite comme écriture R1 avec signal_irreversibilite = IRRÉVERSIBLE et une délibération sur l'acceptabilité de la perte de précision. |
|---|

| K.7 — Signaux et gouvernance du registre Tableau de bord K2 : signaux spécifiques au mode sémantique LLM |
|---|

Le tableau de bord du MRC (§5.3) est ici instancié pour le cas Lucie-7B. Chaque signal est rattaché à sa couche d'origine, son déclencheur, et sa conséquence de gouvernance.

| Signal | Couche | Condition de déclenchement | Conséquence de gouvernance |
|---|---|---|---|
| DECOUPLAGE_METABOLIQUE_ATTENTIONNEL | Couche 1 — R-COUPLAGE | coherence_dualite < 0.50 sur un sous-corpus thématique | Alerte : le LLM génère sur ce thème sans structure sémantique stable. Suspension recommandée des inscriptions dans le registre sur ce thème jusqu'à audit. |
| CONCEPT_FRAGILE_PERSISTENT | Fiche 3 — C-TCFP | solidite_TCFP = FRAGILE sur ≥ 3 cycles de révision consécutifs | Signalement au consortium : le corpus d'entraînement sous-représente ce concept. Recommandation d'enrichissement ciblé du corpus ou d'ajout d'une grammaire spécialisée. |
| DETTE_PATRIMONIALE_NON_SOLDEE | Couche 0 — R1 / I-03 | Asymétrie R1 persistante sur corpus:GALLICAPRESS après 2 exercices | Escalade au consortium + BnF : définir contrepartie (citation, indexation inverse, enrichissement du corpus avec labels BnF, ou contribution financière à la numérisation). |
| DETTE_ECOLOGIQUE_ABSENTE | Couche 0 — R1 / I-06 | Absence d'écriture sur empreinte énergétique Jean-Zay après 1 exercice | Demande d'information à GENCI/IDRIS : consommation kWh pré-entraînement, facteur d'émission, compensation éventuelle. Inscription obligatoire dans métadonnées HuggingFace. |
| ASYMETRIE_INTER_CORPUS | Annexe G.3 — 2-morphismes | amplitude(α : M_fr ⇒ M_en) < 0.30 sur un concept culturel jugé stratégique | Signalement communauté : risque de traduction culturellement approximative. Recommandation de fine-tuning ciblé sur corpus culturel ou ajout d'exemples annotés. |
| DEPENDANCE_PLATEFORME_PPO | Fiche 3 — C-INSCRIPTION-CORPUS / PPO | HuggingFace modifie ses conditions d'accès sans notification au consortium | Activation du plan de contingence : hébergement alternatif (Hugging Face Europe, GENCI, infrastructure Linagora). Inscription dans le registre comme risque de gouvernance active. |
| DRIFT_FINE_TUNING | Annexe G.3 — 2-morphisme temporel | Réduction de solidite_TCFP ≥ 15% sur concepts {commun, gouvernance} après fine-tuning | Délibération au sein du consortium sur les données d'instruction utilisées pour le RLHF : risque de capture de l'alignement par des préférences culturellement dominantes. |
| LICENCE_INCOMPATIBLE | Fiche 3 — C-INSCRIPTION-CORPUS | stade_constitution = EXPÉRIMENTAL et clause restrictive (NC, copyleft fort) détectée dans corpus actif | Suspension de l'usage commercial du modèle sur les tâches mobilisant le sous-corpus concerné. Escalade juridique consortium + conseil. |

### K.7.2 — Gouvernance du registre : régime d'inscription de K2

Conformément à la Piste 6 de la note de cadrage, le cas K2 relève du régime d'inscription RECHERCHE_INTERVENTION (combinaison structurée de ENQUETE_OBSERVATIONNELLE + ENQUETE_COLLECTIVE + AUTOGOUVERNANCE). Les protocoles applicables sont :

> `[CHANGEMENT DE BASE TRACÉ — 12/10/2026]` Dans toute la présente annexe (K.7.2 ; K3, §K.8 et tableaux de pistes), « régime RECHERCHE_INTERVENTION » et « régime combiné ENQUETE_OBSERVATIONNELLE ⊗ ENQUETE_COLLECTIVE ⊗ AUTOGOUVERNANCE » se lisent ainsi : `regime_inscription_corpus` = {ENQUETE_OBSERVATIONNELLE, ENQUETE_COLLECTIVE, AUTOGOUVERNANCE} — combinaison déclarée comme plusieurs valeurs, sans valeur composite (NT-ARCH F3) ; RECHERCHE_INTERVENTION désigne la **phase** de C-ENQUETE-V5 définie en NT-ARCH §B.2ter (enquête publique démocratique, Ferey 2024), que ces cas mettent en œuvre ou non selon que leurs protocoles en remplissent les conditions (association des concernés, contrainte des spécialistes, accessibilité publique, réflexivité). La combinaison des trois régimes ne suffit pas à définir la phase.

| Protocole | Application au cas K2 / OpenLLM-France |
|---|---|
| protocole_observationnel | Calcul automatisé des métriques (coherence_dualite, solidite_TCFP, amplitude 2-morphismes) sur Wikipedia-fr de Lucie par agent MRC. Attestation VC signée par l'agent inscripteur. |
| protocole_collectif | Validation des signaux par le consortium OpenLLM-France (comité de gouvernance) + représentants communauté Discord. Parité délibérative : au moins 3 partenaires + 2 membres communauté pour valider un signal critique. |
| protocole_autogouvernance | Décisions sur les inscriptions au registre (nouvelles versions du modèle, enrichissement corpus, réponse aux signaux) par vote du comité selon les règles du consortium BPI. Traçabilité inscrite en R1. |
| articulation_temporelle | Itératif : calcul automatisé mensuel → validation collective trimestrielle → décisions annuelles sur les versions majeures du modèle. |
| refutabilite_inscrite | Tout membre du consortium ou de la communauté peut contester une inscription dans un délai de 30 jours. La contestation ouvre une CONTROVERSE_GRAMMATICALE dans le registre et bloque l'inscription contestée. |

| K.8 — Limites, ouvertures et articulation aux autres pistes Ce que K2 ne couvre pas, et pourquoi c'est délibéré |
|---|

### K.8.1 — Limites délibérées du cas K2

Limite 1 — Calculabilité à l'échelle du corpus complet. Le treillis FCA pondéré est calculable sur Wikipedia-fr (32,5M documents) mais pas sur l'intégralité du Lucie Training Dataset (3,1 Tns tokens). La démonstration utilise un sous-corpus représentatif. Pour une implémentation opérationnelle, la feuille de route de la note bicatégorielle préconise des stratégies d'élagage (concepts au-delà d'un seuil θ = 0.15 uniquement) et un calcul distribué sur Jean-Zay.

Limite 2 — Absence d'articulation avec la Fiche F8 (mode comptable). K2 teste le mode M-SEMANTIQUE pur. La note de cadrage indique que le cas K2 « minimise la section Couche 2 mode milieu » — ce qui s'étend au mode comptable. L'articulation entre le coût de calcul (énergétique et financier) du pré-entraînement et la Fiche F8 est renvoyée à une extension K2.bis.

Limite 3 — Gouvernance des modèles propriétaires. K2 est praticable sur Lucie-7B précisément parce que tous les artefacts sont ouverts. Sur un LLM propriétaire (GPT-4, Gemini), C-INSCRIPTION-CORPUS serait partiellement vide — le corpus d'entraînement n'est pas divulgué. Le registre inscrirait dans ce cas un signal OPACITE_CORPUS, mais ne pourrait pas calculer les 2-morphismes inter-corpus.

### K.8.2 — Ouvertures vers les autres pistes de la note de cadrage

| Piste | Articulation avec K2 | Extension envisageable |
|---|---|---|
| P1 — Fiche F8 | La dette écologique (coût Jean-Zay, I-06) et le financement BPI (I-02) sont des mouvements comptables au sens CARE : effort e pour le calcul, patrimoine P pour le financement public. | Extension K2-CARE : appliquer les 16 mouvements types et V^CARE = 𝟤 × E × N × C au bilan OpenLLM-France (coûts humains, naturels, financiers du pré-entraînement). |
| P2 — P-C-E-D-e-d | Les écritures R1 de K.2 (I-01 à I-07) sont déjà typées par les six primitives dans le tableau de la section K.2. | Rétro-typage P-C-E-D-e-d de toutes les inscriptions K2 une fois P2 intégré en Couche 0. |
| P3 — R-PRIORITE-CREANCIERS | La dette patrimoniale BnF (I-03) et la dette écologique GENCI (I-06) sont des créanciers de niveau 2 au sens R-PRIORITE-CREANCIERS. Leur remboursement conditionne la distribution du modèle. | Formalisation : si Lucie-7B génère des revenus commerciaux, R-PRIORITE-CREANCIERS ordonne le remboursement de la dette BnF avant la distribution aux partenaires. |
| P4 — G.9 composites | V^CARE pour K2 serait un produit cartésien : V = [0,1] × ℝ≥0 × 𝟤 × E (sémantique × énergétique × présence/absence × financier). G.9 formalise ce V composite. | Cas K2.bis : mode sémantique + comptable via V composite multi-dimensionnel. |
| P6 — Régime combiné | K2 relève explicitement du régime RECHERCHE_INTERVENTION (section K.7.2) — cas paradigmatique de P6. | K2 devient le cas d'application de référence du régime combiné : ses protocoles observationnel / collectif / autogouvernance sont le modèle pour les autres cas. |

### K.8.3 — Question ouverte : le LLM comme acteur traçable dans son propre registre

Le cas K2 soulève une question théorique : Lucie-7B peut-il être à la fois un acteur inscrit dans le registre ET un agent qui contribue à l'inscription ?

Le Manifeste pose la condition : « un LLM inscrit dans des registres de communalité, soumis à validation collective, incapable de valider seul une inscription dans le registre, peut amplifier la démocratie. » Pour K2, cela se traduit par la règle suivante : Lucie-7B peut proposer des inscriptions (annotation de corpus, identification de signaux, suggestion d'acteurs) mais ne peut pas les valider — la validation requiert le protocole collectif (section K.7.2). Cette règle est à inscrire en Couche 0 comme R-INCAPACITE-LLM-VALIDER.

| K.9 — Conclusion Ce que K2 démontre et ce qu'il ouvre |
|---|

Le cas K2 applique le MRC dans sa zone la plus exigeante et la plus stratégique : la gouvernance d'un grand modèle de langage. En choisissant OpenLLM-France / Lucie-7B — le premier LLM souverain français répondant aux critères OSI — comme terrain de démonstration, K2 montre que le registre est praticable sur un cas réel, non sur un cas synthétique.

Trois résultats principaux peuvent être dégagés.

Premier résultat — Le mode M-SEMANTIQUE pur fonctionne. Les trois zones architecturales testées (Fiche 3, R-COUPLAGE-DUAL, Annexe G.3) s'instancient naturellement sur le corpus Lucie. Les acteurs sont identifiables (consortium, corpus, modèles, tokenizer), les écritures R1 sont inscriptibles (I-01 à I-07), les 2-morphismes inter-corpus sont calculables sur le sous-corpus Wikipedia-fr. Le registre n'est pas une métaphore appliquée à l'IA — c'est un outil opérationnel.

Deuxième résultat — Le registre révèle des asymétries invisibles. Deux signaux critiques émergent que ni les métadonnées HuggingFace ni le papier technique n'inscrivent : la dette patrimoniale vis-à-vis de la BnF (I-03) et la dette écologique du pré-entraînement sur Jean-Zay (I-06). Le concept {commun, collectif, gouvernance} est FRAGILE dans Lucie-7B — le LLM que l'on voudrait utiliser pour gouverner les communs ne les représente pas de manière stable. Le 2-morphisme laïcité → secularism est non calculable : un concept central de la démocratie française ne se transporte pas vers l'anglais dans Lucie-7B.

Troisième résultat — OpenLLM-France est un terrain propice à l'expérimentation du registre. La structure consortiale ouverte (17 partenaires, 900+ membres, corpus documentés, poids libres) fournit exactement l'infrastructure que le registre nécessite : des acteurs traçables, des interactions documentées, une gouvernance plurielle capable de délibérer sur les signaux. La proposition de R-INCAPACITE-LLM-VALIDER — le LLM peut proposer mais pas valider une inscription — est le geste politique central du cas K2 : elle inscrit dans l'architecture même du registre la primauté de la délibération humaine collective sur l'agentivité algorithmique.

| K2 en trois phrases : Lucie-7B peut être gouverné par le registre. Le registre révèle ce que les métadonnées HuggingFace cachent. Et le concept qui gouverne les communs n'est pas encore bien représenté dans le LLM qui devrait les servir — ce qui est une invitation à enrichir le corpus, pas une fatalité. |
|---|

Sources principales du cas K2

Louradour J. et al. (2025), The Lucie-7B LLM and the Lucie Training Dataset: Open resources for multilingual language generation, arXiv:2503.12294v1, mars 2025.

OpenLLM-France (2024), Lucie-7B, HuggingFace : huggingface.co/OpenLLM-France/Lucie-7B

OpenLLM-France (2024), Lucie Training Dataset, HuggingFace : huggingface.co/datasets/OpenLLM-France/Lucie-Training-Dataset

Bradley A., Gastaldi J.-L., Terilla J. (2024), The Structure of Meaning in Language: Parallel Narratives in Linear Algebra and Category Theory », _Notices of the AMS_, février 2024, DOI : 10.1090/noti2868

MRC, Note d'extension bicatégorielle, Note de cadrage — Pierre Musseau-Milesi, La Coop des Communs.

OpenLLM-France, GitHub organisation : github.com/orgs/OpenLLM-France/repositories

# PARTIE K3 — Bassin versant en gouvernance multi-acteurs (Lac Togo · Niayes · Drôme)

MODÈLE DE REGISTRES DE COMMUNALITÉ

Note de cadrage — Annexe K

CAS CHIFFRÉ K3

Bassin versant en gouvernance multi-acteurs

Comparaison tri-terrain : Lac Togo (Togo) | Niayes (Sénégal) | Drôme (France)

Arbitrages retenus

A : tri-terrain comparatif à parité | C : 3 terrains symétriques | D : P-C-E-D-e-d sélectif

E : hard Lac Togo + Niayes, soft Drôme | F : articulation explicite K1 × K3

Pierre Musseau-Milesi — La Coop des Communs

## K.0 — Présentation comparée des trois terrains

K3 est un cas chiffré comparatif. Il mobilise trois terrains de gouvernance de l'eau accompagnés par le GRET sur une décennie (2014-2026) : le bassin du Lac Togo au Togo (projet REGIRE, depuis 2023), la zone des Niayes au Sénégal (projet GIREL, depuis 2017), et le bassin de la Drôme en France (SAGE-SMRD, depuis 1993). Ces trois terrains sont traités symétriquement (Arbitrage C). Ils partagent le même objectif générique — mettre en place une gouvernance multi-acteurs de l'eau — mais diffèrent par leur stade institutionnel, leur contexte hydrogéologique et leur régime juridique.

Le cas teste le mode milieu pur (M-MILIEU, Fiche F2) du MRC, mobilise l'Annexe H dans toute sa profondeur (DIDs, VCs, dMRV, smart contracts), et éprouve simultanément les Pistes 2 (grammaire P-C-E-D-e-d), 3 (R-PRIORITE-CREANCIERS), 4 (enrichissements composites G.9) et 6 (régime RECHERCHE_INTERVENTION).

### K.0.1 — Tableau de cadrage comparatif

| Dimension | Lac Togo (REGIRE) | Niayes (GIREL) | Drôme (SAGE) |
|---|---|---|---|
| Pays / contexte | Togo — décentralisation 2019 | Sénégal — gestion centralisée eau | France — loi sur l'eau 1992 |
| Milieu hydrique | Lac 46 km² ; bassins Haho 3 400 km² + Sio 2 800 km² | Nappe côtière, zone 2 300 km², frange 100-280 km | Rivière de surface, bassin 1 640 km² |
| Population concernée | ~30 % population togolaise, 269 397 bénéficiaires directs | Principale zone maraîchère (80 % prod. Sénégal) | 83 communes, ~30 % département Drôme |
| Instance de gouvernance | OLGE (Organe local de gestion de l'eau) | PLE (Plateforme locale de l'eau) — 14 en zone | CLE (Commission locale de l'eau) — 52 membres |
| Statut juridique instance | Prévu par Code de l'eau 2010, mise en place en cours | Associatif ; débat institutionnalisation → CCE | Réglementaire (Loi eau 1992 / SDAGE) |
| Budget projet/dispositif | REGIRE : 834 992 € (2023-2026) | GIREL phase 1 : 493 k€ (2019-2022) | SMRD : financement Agence eau RMC + collectivités |
| Stade institutionnel | Émergence (3 communes pilotes) | Consolidation (14 PLE ; mise à l'échelle nappe) | Mature (SAGE depuis 1997 ; 2e révision en cours) |
| Menace principale | Déforestation, pression démographique, gestion fragmentée | Baisse nappe ~45 cm/an ; pesticides ×102 norme OMS ; intrusion saline | Étiage sévère, conflits d'usage irrigants/milieu, PFAS |
| Mode d'inscription MRC | RECHERCHE_INTERVENTION émergent | RECHERCHE_INTERVENTION consolidé | AUTOGOUVERNANCE + ENQUETE_COLLECTIVE |
| Annexe H — niveau | Projection (hard : smart contract R-PRIORITE) | Projection (hard : smart contract R-PRIORITE) | Existant institutionnel (soft : signal levé) |

### K.0.2 — Question architecturale centrale

Question commune aux trois terrains : dans quelles conditions un registre de communalité peut-il rendre visible la dette d'un territoire envers son milieu hydrique, et en garantir le remboursement prioritaire avant toute distribution discrétionnaire ?

Les trois terrains offrent trois réponses différenciées selon leur stade institutionnel, leur régime juridique et le degré de formalisation de leurs instruments de mesure et de gouvernance. La comparaison permet de tester la robustesse trans-contextuelle du MRC.

## K.1 — Acteurs tracés (C-INSCRIPTION)

Conformément à la Couche 0 du MRC (C-INSCRIPTION avec DIDs / VCs, Annexe H.1-H.2), tous les acteurs pertinents sont inscrits comme acteurs tracés. K3 distingue un catalogue commun aux trois terrains et des acteurs spécifiques à chaque terrain.

### K.1.1 — Catalogue commun (acteurs structurels partagés)

| Acteur tracé | Type | Rôle dans les trois terrains |
|---|---|---|
| Milieu hydrique (lac/nappe/rivière) | Non-humain | Créancier NH prioritaire au sens R-PRIORITE-CREANCIERS |
| Instance locale de gouvernance (OLGE / PLE / CLE) | Collectif institutionnel | Opérateur du registre, porteur des Plans de GIRE locaux |
| Ménages usagers | Humain individuel | Bénéficiaires capabilités plancher eau potable (G-JUSTICE) |
| Agriculteurs / irrigants | Humain collectif | Préleveurs / co-gestionnaires ; tension usage vs préservation |
| État / administration nationale (DGPRE / MEEM) | Public régalien | Autorité concédante, détenteur données nationales, plafond Bercy |
| Agences de l'eau / bailleurs (AESN, AFD, Agence RMC) | Public technique et financier | Financeurs, fixeurs de standards, parfois capteurs de recettes |
| Commune / collectivité locale | Public décentralisé | Détenteur budget local, mandant de l'instance locale |
| ONG facilitatrice (GRET) | Tiers facilitateur | Porteur du régime RECHERCHE_INTERVENTION |
| Acteurs économiques (agro-industriels, miniers, tourisme) | Privé préleveur | Signal signal_collège_absent si absent de l'instance |
| Milieu documentaire (indicateurs, dMRV) | Système d'inscription | Couche 0 matérielle : piézomètre, débit-mètre, PGRE |

### K.1.2 — Acteurs spécifiques par terrain

| Acteur spécifique | Lac Togo | Niayes | Drôme |
|---|---|---|---|
| Instance locale opérationnelle | OLGE (3 communes pilotes : Haho 1, Kpélé 1, Zio 2) | 14 PLE (dont Mont-Rolland : 58 membres), statut associatif | CLE (52 membres, 3 collèges) |
| Opérateur technique eau | TDE (Togolaise des Eaux) | OFOR (Office des Forages Ruraux) / Sen'eau | SMRD (Syndicat Mixte Rivière Drôme) |
| Collectif citoyen autonome | Non documenté à ce stade | En cours de structuration (PLE → CCE) | Collectif Rebond (Crest) ; Parlement d'Isère (en amont) |
| Instance judiciaire / concession | DGEA (Direction eau), mairies pilotes | DGPRE (Direction Gestion & Planif. Ressources Eau) | Préfecture ; Agence eau Rhône-Méd.-Corse |
| Acteur industriel identificateur | Entreprises pêche artisanale, horticulture lacustre | Compagnies minières (phosphates) ; agro-industriels export | Industriels extraction eau (Suez) ; irrigants aval |

Observation structurante — signal_collège_absent : Sur les trois terrains, les acteurs économiques privés intensifs (miniers, agro-industriels, grands irrigants) sont soit absents des instances de gouvernance, soit présents dans des conditions qui réduisent leur exposition aux obligations de préservation NH. Ce signal, documenté empiriquement dans les quatre sources GRET, est l'une des failles structurelles que le MRC permet de rendre visible et opposable.

## K.2 — Inscriptions Couche 0 : flux et événements clés

La Couche 0 du MRC (Primitives) inscrit les événements et flux comme interactions R1-symétriques. Pour K3, trois familles d'inscriptions sont distinguées : flux financiers, flux écologiques et événements institutionnels.

### K.2.1 — Flux financiers (comparaison tri-terrain)

| Flux / Événement | Lac Togo (Togo) | Niayes (Sénégal) | Drôme (France) |
|---|---|---|---|
| Budget annuel instance locale | REGIRE : 278 k€/an (sur budget projet 3 ans) | GIREL ph.1 : ~98 k€/an ; financement externe AESN/AFD | Financement SMRD : Agence eau RMC + taxes syndicales |
| Redevance eau (prélèvement) | À formaliser dans OLGE ; principe pollueur-payeur prévu Code eau 2010 | Redevance DGPRE ; faible taux ; plafond Bercy non applicable | Redevance SDAGE Agence RMC ; plafond mordant Bercy (recettes > plafond → budget général) |
| Budget préservation NH effectif | Non isolé à ce stade ; composante projet 'gestion ressource' | Plans locaux GIRE incluent cordons pierreux, inventaires forages | PGRE : volumes économisés (m³), volumes substitués ; coûts SMRD |
| Distribution aux usagers (irrigation) | Usage agricole lacustre ; pas de VP formalisé | Priorité alimentaire → usage maraîcher Dakar | Volumes Prélevables fixés par usage : AEP > irrigation > industrie |
| Financement facilitation | Sur budget projet GRET / bailleur | Proposition Defalvard : financer animation sur redevance | Animation CLE financée Agence eau RMC (hors plafond mordant) |

### K.2.2 — Flux écologiques (état du milieu)

| Flux / Événement | Lac Togo (Togo) | Niayes (Sénégal) | Drôme (France) |
|---|---|---|---|
| Indicateur de pression principal | Déforestation bassin, pression démographique, gestion fragmentée OLGE | Baisse nappe profonde : ~45 cm/an | Débit d'étiage Drôme ; stress hydrique chronique été |
| Indicateur de qualité | À formaliser par OLGE (mission suivi prévue projet REGIRE) | Pesticides : 51,21 µg/L (×102 norme OMS) à Guédiawaye | Qualité bactériologique améliorée (SAGE) ; PFAS persistants |
| Indicateur de quantité | Lac : 46 km² étiage ; flux Sio + Haho à mesurer | Nappe peu profonde 5-10 m étiage ; sel jusqu'à 690 mg/L à Potou | Volumes prélevés par usage (PGRE 2021) |
| Horizon temporel du milieu | Lac et bassins : horizon décennal à centennal | Nappe profonde fossile : horizon séculaire à millénaire (R-INTERDIT-ABSOLU potentiel) | Rivière : horizon inter-annuel (étiage) à décennal (révision SAGE 2050) |
| Mesure dMRV disponible | Suivi piézométrique à initier ; VCs attestation à projeter | Inventaires forages PLE ; cordons pierreux ; enquêtes pesticides | Suivi débit SMRD ; comptage volumes irrigants (données PGRE) |

### K.2.3 — Événements institutionnels clés (timeline)

| Date | Lac Togo | Niayes | Drôme |
|---|---|---|---|
| 1992-97 | — | — | Loi eau 1992 → CLE 1993 → SAGE 1997 (1er de France) |
| 2008-13 | — | — | 1ère révision SAGE ; début PGRE ; volumes prélevables |
| 2010 | Code de l'eau togolais (loi 2010-004) prévoit OLGE | — | — |
| 2017-19 | — | Lancement GIREL ; 3 premières PLE | — |
| 2019 | Décentralisation effective Togo | — | — |
| 2019-22 | — | GIREL phase 1 (493 k€) ; 5 communes pilotes ; 14 PLE in fine | Bilan PGRE 2021 CLE |
| 2021 | — | — | Bilan PGRE validé CLE ; révision SAGE lancée |
| 2023 | REGIRE lancé (834 992 €, 3 communes pilotes) | — | — |
| 2024 | Ateliers GRET Togo ; partage expériences Drôme/Sénégal | Visi'eau 24/09 : débat plafond Bercy, redevance, OLGE | Rencontres GRET Drôme (18 sept.) ; collectif Rebond |
| 2025 | Atelier bilan 8 avril ; appel Flamay Ahiafor sur bouc émissaire | — | — |
| 2026 | Fin REGIRE (prévue) | Perspective institutionnalisation PLE → CCE | Approbation prévue 2ème révision SAGE |

## K.3 — Dualité des régimes (Couche 1)

La Couche 1 du MRC articule deux régimes couplés : le régime métabolique (prélèvements, distributions, usages) et le régime attentionnel (mesure, alerte, délibération). Le principe R-COUPLAGE garantit que les décisions distributives tiennent compte de l'état du milieu. R-HABITABILITE fixe les seuils plancher. R-PRIORITE-CREANCIERS (Piste 3) impose que la dette NH soit remboursée avant toute distribution discrétionnaire.

### K.3.1 — R-COUPLAGE : articulation régime métabolique × régime attentionnel

| Flux / Événement | Lac Togo (Togo) | Niayes (Sénégal) | Drôme (France) |
|---|---|---|---|
| Régime métabolique (flux prélevés) | Pêche artisanale, usage agricole lacustre, AEP communes ; volumes non encore formalisés en VP | Usage maraîcher (80 % prod. séné.) ; forages agricoles ; forages AEP ruraux ; prélèvements industriels/miniers informels | VP par usage : AEP prioritaire, irrigation contingentée, industrie résiduelle ; suivi volumes PGRE |
| Régime attentionnel (mesure/alerte) | Mission suivi OLGE (piézomètre, qualité lac) ; en construction ; VCs à projeter | Inventaires forages PLE ; suivi piézométrique DGPRE ; enquêtes qualité (pesticides, nitrates) | Suivi débit étiage SMRD ; indicateurs PGRE ; observatoire SMRD ; Parlement d'Isère (en gestation) |
| Couplage effectif ? | Faible : pas encore de VP ; OLGE en construction ; lien mesure-décision à formaliser | Partiel : données PLE non encore opposables aux industriels ; DGPRE reste autorité nationale | Fort (SAGE réglementaire) : CLE peut opposer VP aux irrigants ; mais plafond Bercy capte recettes redevance |
| R-HABITABILITE (seuil plancher) | Accès AEP populations lacustres ; défini dans composante 'services' REGIRE | Accès eau potable Mont-Rolland (capabilité alerte : avant GIREL, accès insuffisant) | Débit réservé Drôme ; qualité baignade et eau potable |

### K.3.2 — R-PRIORITE-CREANCIERS : qui est créancier prioritaire ?

R-PRIORITE-CREANCIERS (Piste 3) formule le principe : les dettes envers le capital naturel NH sont des créances prioritaires ; elles doivent être remboursées avant toute distribution discrétionnaire. Sur K3, ce principe prend trois formes empiriques distinctes selon le terrain.

| Dimension R-PRIORITE | Lac Togo | Niayes | Drôme |
|---|---|---|---|
| Créancier NH identifié | Lac Togo (46 km²) + bassins Haho/Sio | Nappe côtière des Niayes (aquifère profond fossile) | Rivière Drôme (fleuve vivant, étiage critique) |
| Forme de la dette NH | Déforestation non remboursée ; charge de préservation à créer | Baisse 45 cm/an = dette irremboursée ; pollution pesticides = dette qualitative | Prélèvements excessifs été = débit étiage sous seuil ; PFAS = dette qualitative persistante |
| Niveau violation R-PRIORITE | Niveau 1-2 : absence de VP ; pas de charge formelle préservation | Niveau 3-4 : distribution irrigants industriels sans charge préservation NH effective ; plafond Bercy inexistant ici mais DGPRE capte recettes | Niveau 3 : plafond mordant Bercy capte recettes redevance SDAGE > plafond → budget général ; la préservation NH perd son financement dédié |
| Régime Annexe H (Arbitrage E) | HARD (projection) : smart contract R-PRIORITE interdit distribution sans attestation dMRV préservation NH effective | HARD (projection) : VC attestant niveau nappe avant autorisation prélèvement ; smart contract bloquant | SOFT (existant) : signal levé et inscrit au PGRE ; CLE peut décider mais pas bloquée techniquement |
| Instance qui décide actuellement | Mairies pilotes + OLGE en construction ; bailleur AESN | DGPRE (national) ; PLE consultées mais pas décisionnaires sur industriels | CLE (décisionnaire SAGE) ; mais Agence eau et Bercy sur redevance |

| Encadré K.3 — Le plafond mordant Bercy : instance type de violation R-PRIORITE-CREANCIERS Niveau 3 |
|---|
| Le mécanisme dit 'plafond mordant' (ou 'écrêtement Bercy') s'applique aux agences de l'eau françaises. Au-delà d'un plafond de recettes défini en loi de finances, les recettes supplémentaires de redevance SDAGE sont reversées au budget général de l'État, au lieu d'être affectées à la préservation des milieux hydriques. |
| Formulé par Hervé Defalvard lors de la rencontre Visi'eau du 24 septembre 2024 : 'Bercy déteste que les usagers puissent décider d'une affectation.' Cette captation constitue, en langage MRC, une violation R-PRIORITE-CREANCIERS de Niveau 3 : les recettes d'usage ('l'eau paye l'eau') sont détournées avant que la dette NH soit remboursée. La grammaire P-C-E-D-e-d détecte cette rupture (voir K.5). |
| Ce mécanisme est absent des deux terrains africains (où le plafond ne s'applique pas) mais y est remplacé par d'autres formes de capture : la DGPRE sénégalaise reste autorité nationale centralisée sur les données eau ; les OLGE togolaises sont dépendantes du financement projet externe. Les trois terrains documentent ainsi trois formes différentes d'incapacité à clôturer la boucle 'l'eau paye l'eau'. |

## K.4 — Mode milieu (M-MILIEU, Fiche F2) : cœur du cas

Le mode milieu est le mode dominant de K3. Il mobilise deux primitives spécifiques : R-CARE (charges de préservation effectives envers le milieu) et R-CODEGRADATION (registre des dégradations subies). La catégorie de base est V^MILIEU = 2 × Q × V × H (présence × quantité × qualité × horizon), enrichissement composite au sens de G.9 (Piste 4).

### K.4.1 — R-CARE : charges de préservation effectives

R-CARE est satisfait quand les acteurs qui bénéficient du milieu assument effectivement des charges de préservation dont les résultats sont mesurables et attestés (VCs, dMRV). Trois régimes de satisfaction sont observés.

| Dimension R-CARE | Lac Togo | Niayes | Drôme |
|---|---|---|---|
| Charges de préservation définies ? | Partiellement : composante 'gestion ressource' REGIRE ; Plans locaux GIRE à élaborer | Oui (Plans locaux GIRE) : cordons pierreux, reboisement, inventaires, suivi qualité | Oui (PGRE) : volumes économisés (m³), volumes substitués, règles étiage |
| Charges portées par qui ? | Communes pilotes + OLGE ; cofinancé AESN/projet | PLE + commune Mont-Rolland (budget municipal partiel) | SMRD + irrigants (restrictions VP) + industrie (quotas) |
| Résultats mesurables et attestés ? | En construction ; protocoles dMRV à formaliser | Oui partiellement : inventaires forages ; enquêtes qualité (pesticides) | Oui (PGRE 2021) : m³ économisés documentés ; débit étiage suivi |
| Acteurs exonérés de R-CARE | Industriels / agro-industriels : absent de l'OLGE (signal_collège_absent) | Compagnies minières, agro-industriels export : prélèvements sans charge préservation NH | Grands irrigants aval partiellement ; Bercy (exonéré de la boucle redevance → préservation) |
| R-CARE satisfait globalement ? | Non (en construction) — cas type émergence | Partiel — cas type consolidation incomplète | Partiel — cas type institutionnalisation avec faille (Bercy) |

### K.4.2 — R-CODEGRADATION : registre des dégradations subies par le milieu

R-CODEGRADATION exige que les dégradations subies par le milieu soient inscrites, datées et attribuées. C'est la contrepartie de R-CARE : si R-CARE mesure les efforts de préservation, R-CODEGRADATION mesure l'évolution de la dette NH. Les trois terrains offrent des niveaux de documentation très différents.

| Flux / Événement | Lac Togo (Togo) | Niayes (Sénégal) | Drôme (France) |
|---|---|---|---|
| Dégradation principale documentée | Déforestation bassins Haho/Sio ; ensablement Lac Togo ; qualité eau lacustre non encore mesurée par OLGE | Baisse nappe profonde ~45 cm/an ; pesticides jusqu'à 51,21 µg/L (×102 norme OMS) à Guédiawaye ; nitrates 1,2-227 mg/L ; salinité 690 mg/L à Potou (×3,4 norme OMS) | Débit étiage sous seuil biologique (années de sécheresse) ; PFAS nappe (pollution longue durée) |
| Attribution de la dégradation | Diffuse : pression démographique + pratiques agricoles + fragmentation gouvernance | Partielle : pesticides attribués aux maraîchers (risque bouc émissaire — Flamay Ahiafor, atelier 8 avril 2025) ; miniers non attribués | Partielle : irrigants identifiés, industriels moins ; PFAS non attribués précisément |
| Opposabilité du registre ? | Non encore : pas de VP, pas de VC opposable aux tiers | Non encore : PLE non décisionnaires vis-à-vis des industriels | Partiellement : PGRE opposable via SAGE réglementaire ; mais données Suez inaccessibles au collectif Rebond |
| Horizon de la dégradation | Décennal (lac de surface) à centennal (nappes sous-jacentes) | Millénaire (nappe fossile profonde) → signal_horizon_incommensurable (cf. K5 déchets nucléaires) | Inter-annuel (étiage) + longue durée (PFAS) |

### K.4.3 — V^MILIEU : enrichissement composite G.9 et perte informationnelle

V^MILIEU = 2 × Q × V × H est la catégorie de base enrichie pour le mode milieu (Piste 4, G.9). Ses quatre dimensions sont : Présence (2 : présence/absence du milieu vivant), Quantité (Q : volumes, débits, niveaux piézométriques), qualité (V : qualité physico-chimique et biologique), et Horizon (H : échelle temporelle de référence du milieu).

La projection de V^MILIEU vers V^IFRS-eau (catégorie quantitative pure : seul Q est retenu, les autres dimensions sont abandonnées) constitue une perte informationnelle irréversible. C'est l'instance type de la Piste 4 dans K3 : les indicateurs DGPRE (nationaux, quantitatifs normalisés) appauvrissent les indicateurs PLE/OLGE/CLE (locaux, composites, intégrant présence et horizon).

| Dimension V^MILIEU | Lac Togo | Niayes | Drôme | V^IFRS-eau (projection) |
|---|---|---|---|---|
| Présence (2) | Lac vivant, pêche artisanale, rôle culturel | Nappe côtière = infrastructure maraîchère Dakar | Rivière vivante (baignade, biodiversité, tourisme) | Perdu (non quantifiable) |
| Quantité (Q) | 46 km² étiage ; débits Haho/Sio à documenter | Nappe profonde : baisse ~45 cm/an | Volumes prélevables par usage (PGRE 2021) | Retenu (m³, l/s) |
| Qualité (V) | À documenter par OLGE | Pesticides ×102 norme ; nitrates ; salinité | Qualité bactériologique améliorée ; PFAS persistants | Partiellement retenu (normes OMS) |
| Horizon (H) | Décennal à centennal (lac) | Millénaire (nappe fossile profonde) | Inter-annuel à décennal + 2050 (SAGE) | Perdu (moyen terme financier) |

Observation Piste 4 : Le passage des indicateurs locaux PLE/OLGE (V^MILIEU complet) aux indicateurs nationaux DGPRE/SDAGE (V^IFRS-eau) est une projection π informationnellement irréversible. Les dimensions Présence et Horizon sont perdues. Le MRC rend cette perte visible et opposable : c'est l'un des apports architecturaux clés de K3.

## K.5 — Grammaires mobilisées (Couche 3) et typage P-C-E-D-e-d sélectif

Conformément à l'Arbitrage D (option b — sélectif) : le typage P-C-E-D-e-d est appliqué aux seuls flux structurellement décisifs pour démontrer la grammaire sans alourdir. Quatre flux sont typés, sur lesquels la grammaire produit les résultats les plus significatifs.

### K.5.1 — Table de typage P-C-E-D-e-d (flux sélectifs)

Légende : P = Prélèvement pur | C = Contribution communale | E = Effort collectif | D = Dette envers NH | e = effort facilitateur | d = résultat préservation NH

| Flux | Type | Terrain | Description |
|---|---|---|---|
| Redevance prélèvement eau | D | Usagers → Agence eau (France) / DGPRE (Sénégal) | Taxe usage = D côté usager (obligation de contribuer à la préservation). Devient e côté agence (effort de collecte). Devrait devenir d (résultat : milieu préservé). Rupture de chaîne : plafond Bercy transforme d en budget général → la chaîne D→e→d est interrompue ; R-PRIORITE-CREANCIERS violé. |
| Budget OLGE / PLE communal | C | Commune pilote → OLGE/PLE | C = contribution de la collectivité publique à l'effort de gouvernance partagée. Si la commune ne dédie pas de budget propre (dépendance projet), C est nul → fragilité structurelle de la gouvernance. |
| Charges de préservation (cordons pierreux, inventaires) | e | PLE Niayes / SMRD Drôme / OLGE Togo | e = effort de facilitation et de préservation NH effectif. Se transforme en d (résultat mesurable) si les indicateurs dMRV attestent l'amélioration du milieu. Boucle e ↔ d est l'épine dorsale de R-CARE. |
| Distribution irrigation industrielle sans VP formalisé | P | Irrigants industriels / compagnies minières (Niayes, Lac Togo) | P pur = prélèvement sans contribution à e ni à d. Instance type de la violation R-PRIORITE-CREANCIERS : le préleveur bénéficie du milieu sans en assumer les charges. Signal_collège_absent associé. |
| Financement animation sur redevance (proposition Defalvard) | e→d | Agence eau → SMRD/PLE (proposition) | Si la redevance finance directement l'animation (Defalvard, Visi'eau 2024), on obtient un cycle e↔d auto-soutenu : l'effort de facilitation (e) produit un résultat de préservation (d) qui justifie la redevance suivante. C'est la forme idéale du circuit 'l'eau paye l'eau'. |

### K.5.2 — Grammaires transversales activées

| Grammaire | Instance K3 |
|---|---|
| G-COMMUNALITE | Cœur de K3. Les trois terrains sont des tentatives de mise en commun d'une ressource rivale (eau) et conditionnellement excluable. Les OLGE, PLE et CLE sont des institutions ostromniennes de Couche 2 (choix collectif). La dynamique GRET est une instance G-COMMUNALITE au sens fort : arène de partage de connaissances + co-élaboration des règles. |
| G-EVOLUTIVITE | Documentée explicitement : 'les acteurs raisonnent désormais à partir de la disponibilité de la ressource, et non plus à partir de leurs besoins à court terme' (GIREL Niayes, Approche par les communs 2024). Apprentissage cognitif collectif = G-EVOLUTIVITE centrale. |
| G-RESPONSABILITE | Chaîne de responsabilité opérateur ↔ État ↔ commune ↔ usagers, particulièrement développée en contexte DSP (OFOR/ASUFOR Sénégal). L'OFOR (Office des Forages Ruraux), d'abord réticent, est devenu favorable aux PLE : instance appel_entendu. |
| G-SOIN | R-CARE instancie G-SOIN : prendre soin du milieu hydrique comme obligation non optionnelle. Le bassin GRET 2024 s'intitule 'Prendre soin et maîtriser l'usage de l'eau' — formulation directement G-SOIN. |
| G-JUSTICE | Capabilité plancher eau potable (G-JUSTICE Fiche F6). Accès eau potable Mont-Rolland : 'avant intervention : accès insuffisant'. signal_capabilite_alerte levé. |
| G-MIMETIQUE | Vigilance bouc émissaire signalée par Flamay Ahiafor (atelier 8 avril 2025) : risque de désigner les industriels ou les collectifs citoyens comme 'tribunaux' purs. signal_bouc_emissaire_potentiel à inscrire. |
| G-MESOLOGIE | V^MILIEU = 2 × Q × V × H est une formalisation G-MESOLOGIE : le milieu est irréductible à ses grandeurs quantitatives ; il inclut présence et horizon. |

## K.7 — Dispositifs techniques (Annexe H) : comparaison par terrain

L'Annexe H déploie l'infrastructure de la dataroom augmentée : DIDs (H.1), VCs (H.2), dMRV (H.3), covenants (H.4), smart contracts (H.5), covenant de priorité des créanciers (H.6) et stockage à adressage par contenu (H.7). K3 compare les trois terrains selon leur niveau de déploiement H, en distinguant le régime existant du régime projeté.

### K.7.1 — Matrice de déploiement Annexe H

| Composante H | H.x | Lac Togo | Niayes | Drôme |
|---|---|---|---|---|
| DIDs acteurs | H.1 | À créer : DID mairies pilotes, OLGE 3 communes, GRET Togo | Partiellement formalisables : DID 14 PLE, DGPRE, communes | Existants institutionnels : SIRET SMRD, codes CLE ; DID à formaliser MRC |
| VCs attestations mesures | H.2 | À projeter : VC suivi piézométrique lac, qualité eau, inventaire infrastructures | Partiellement disponibles : VC inventaires forages PLE, enquêtes pesticides (non formalisés en VC) | Données PGRE attestées CLE ; pas de VC au sens H.2 ; à formaliser |
| dMRV décentralisé | H.3 | À construire : monitoring ressource lacustre (lac + bassins Haho/Sio) confié aux OLGE | En cours : PLE assurent suivi piézométrique et qualité ; données DGPRE centralisées (tension local/national) | SMRD assure monitoring ; données partiellement inaccessibles (ex. collectif Rebond/Suez) |
| Covenants (engagements) | H.4 | À formaliser : engagements OLGE sur Plans locaux GIRE ; covenants communes | Covenants PLE sur Plans locaux GIRE existants (non formalisés en H.4) | SAGE = covenant réglementaire le plus fort des trois ; VP opposables |
| Smart contracts R-PRIORITE | H.5 | PROJECTION HARD (Arbitrage E) : smart contract bloquant distribution sans attestation dMRV préservation NH | PROJECTION HARD (Arbitrage E) : VC nappe → smart contract bloquant prélèvement au-dessus du seuil | SOFT EXISTANT (Arbitrage E) : signal levé au PGRE, CLE décide ; pas de blocage automatique |
| Extension H.11 (comptable) | H.11 | Budget REGIRE (834 992 €) et budgets OLGE futurs : à inscrire en mode comptable F8 | Budget GIREL (493 k€ ph.1) + budgets PLE communaux : à inscrire en F8 ; financement animation = enjeu central | Budget SMRD + redevance Agence eau (plafond Bercy) : cas type de la Piste 1 F8 appliquée à l'eau non agricole |

### K.7.2 — Régimes hard et soft détaillés (Arbitrage E)

| Régime HARD — Lac Togo et Niayes (projection Annexe H) |
|---|
| Architecture H projetée : chaque OLGE/PLE se voit attribuer un DID (identifiant décentralisé). Les mesures piézométriques et qualité eau génèrent des VCs attestés (attestation de mesure certifiée par protocole dMRV). Un smart contract inscrit dans l'Annexe H.5 définit la condition de déblocage des autorisations de prélèvement : |
| CONDITION : niveau_nappe (VC attesté) > seuil_critique ET qualité_eau (VC) > norme_OMS → autorisation prélèvement accordée. Sinon : R-PRIORITE-CREANCIERS déclenché → prélèvement suspendu jusqu'à attestation de remboursement de la dette NH. |
| Au Lac Togo : le smart contract bloque toute autorisation de prélèvement ou de distribution irrigation si le dMRV ne certifie pas que les charges de préservation NH (reboisement, cordons pierreux, traitement eaux usées) ont été effectivement réalisées au cours de la période précédente. |
| Aux Niayes : VC niveau nappe profonde. Le smart contract est particulièrement critique : une baisse de 45 cm/an, non stoppée dans les 10 ans, risque d'atteindre un seuil d'irréversibilité (signal_horizon_incommensurable). Le régime hard matérialise le jonasien 'principe responsabilité' : agir avant que la dette devienne irremboursable. |

| Régime SOFT — Drôme (existant institutionnel, Arbitrage E) |
|---|
| Le SAGE Drôme est le dispositif le plus mature des trois terrains. Le PGRE fixe des Volumes Prélevables par usage (AEP > irrigation > industrie) opposables réglementairement. Le débit d'étiage est suivi par le SMRD. Quand le débit est sous le seuil biologique, une alerte est levée et inscrite. |
| En régime soft, le signal est levé et inscrit (signal_priorite_violee si les VP sont dépassés), mais la décision reste entre les mains de la CLE (et de la Préfecture pour l'arrêté sécheresse). Il n'y a pas de blocage automatique. La CLE décide. Le signal est un outil d'information et de responsabilisation, pas un verrou. |
| La faille du régime soft Drôme n'est pas dans le dispositif CLE lui-même, mais dans la captation Bercy : les recettes de redevance SDAGE au-dessus du plafond mordant sont reversées au budget général, ce qui prive le SMRD de ressources pour financer les actions de préservation NH. Le régime soft CLE est robuste ; le circuit financier de la redevance est rompu. |

## K.8 — Signaux levés par terrain (Annexe I)

Les signaux MRC (référence Annexe I) sont testés systématiquement sur les trois terrains. Un signal levé est inscrit dans le registre avec sa source documentaire, son terrain, et sa date d'occurrence. K3 confirme ou projette les signaux suivants.

| Signal | Lac Togo | Niayes | Drôme |
|---|---|---|---|
| signal_collège_absent (acteur économique puissant absent de l'instance de gouvernance) | Agro-industriels et entreprises pêche intensive non représentés dans OLGE en construction | Compagnies minières (phosphates) et agro-industriels export absents des PLE ou présents sans obligation | Grands irrigants aval et industrie sous-représentés CLE ; données Suez non accessibles au collectif Rebond |
| signal_irreversibilite_changement_base (passage indicateurs locaux → indicateurs nationaux) | OLGE → DGEA : indicateurs locaux du lac non encore formalisés ; risque de normalisation descendante | PLE → DGPRE : données qualité locales (pesticides, piézomètre) non intégrées aux bases DGPRE nationales | CLE → Agence eau : indicateurs PGRE (m³ locaux) → volumes prélevés nationaux ; perte dimension Présence et Horizon |
| signal_priorite_violee (recettes d'usage détournées avant préservation NH) | Non encore applicable (VP inexistant) ; risque à formaliser dès création OLGE | Non applicable directement (pas de plafond Bercy) ; DGPRE centrale capte pouvoir décisionnel sur données | ACTIF : plafond mordant Bercy capte recettes redevance SDAGE > plafond → budget général (Visi'eau 24/09/2024) |
| signal_horizon_incommensurable (milieu à horizon millénaire, irremboursable si dégradé) | Faible (lac de surface, horizon décennal) | ACTIF : nappe profonde fossile des Niayes = aquifère millénaire ; baisse 45 cm/an = dette potentiellement irremboursable (résonance K5 déchets nucléaires) | Faible pour la rivière ; PFAS nappe = horizon centennal potentiel |
| signal_capabilite_alerte (capabilité plancher eau potable non satisfaite) | Potentiel : accès AEP populations lacustres à vérifier ; composante 'services' REGIRE vise ce point | ACTIF (avant GIREL) : Mont-Rolland accès insuffisant avant intervention ; 95 % accès atteint avec PLE | Faible (accès généralisé) ; Mayotte mentionné comparativement dans documents GRET |
| signal_bouc_emissaire_potentiel (acteur désigné comme responsable unique) | Risque : désigner les communes amont comme responsables de la déforestation | ACTIF (risque identifié par Flamay Ahiafor, 8 avril 2025) : maraîchers désignés comme 'pollueurs' alors que miniers non attribués ; ou inversement collectifs citoyens stigmatisés | Présent : industriels désignés par collectif Rebond ; risque de simplification causale documenté par GRET |
| appel_entendu (signal positif : décision favorable à la gouvernance partagée) | Partiel : décentralisation 2019 crée le cadre légal OLGE ; lancement REGIRE = appel_entendu institutionnel | ACTIF : OFOR (Office Forages Ruraux Sénégal) d'abord réticent aux PLE, devenu favorable = appel_entendu | ACTIF : CLE Drôme créée 1993 = premier appel_entendu de France ; SAGE 1997 = confirmation institutionnelle |

Bilan signaux K3 : six types de signaux sont documentés sur les trois terrains, avec des intensités différentes. Le signal le plus robuste trans-terrain est signal_collège_absent. Le signal le plus dangereux spécifiquement est signal_horizon_incommensurable (Niayes — nappe fossile). Le signal le plus institutionnellement documenté est signal_priorite_violee (Drôme — plafond Bercy). L'appel_entendu le plus remarquable est la conversion de l'OFOR sénégalais.

## K.9 — Synthèse comparative et articulation explicite K1 × K3 (Arbitrage F)

### K.9.1 — Ce que la comparaison tri-terrain démontre

K3 démontre six invariants architecturaux du MRC à travers trois contextes contrastés :

• La dette NH est universelle : quel que soit le contexte (Afrique subsaharienne, Europe), tout usage intensif d'un milieu hydrique crée une dette envers ce milieu. Le MRC en rend la forme et le niveau visibles.

• R-PRIORITE-CREANCIERS est toujours violée, mais sous des formes différentes : plafond Bercy (Drôme), absence de VP (Lac Togo), exclusion des industriels des PLE (Niayes). La grammaire détecte chaque forme.

• V^MILIEU → V^IFRS-eau est une perte informationnelle universelle : dans les trois pays, le passage des indicateurs locaux composites aux indicateurs nationaux normalisés appauvrit l'information sur le milieu. L'enrichissement composite G.9 rend cette perte visible et opposable.

• Le régime RECHERCHE_INTERVENTION est le mode d'inscription naturel des trois terrains : mesure scientifique (observationnel) + co-construction des seuils (collectif) + décision par les acteurs (autogouvernance). GRET est l'acteur tracé de ce régime combiné.

• signal_collège_absent est le signal le plus récurrent : les acteurs économiques les plus puissants et les plus préleveurs sont systématiquement sous-représentés dans les instances de gouvernance.

• Hard vs soft n'est pas une question de volonté politique mais de maturité institutionnelle et de qualité des données : le régime hard (smart contract bloquant) n'est pertinent que si le dMRV est fiable et le DID de l'acteur est établi. La Drôme a 30 ans de données PGRE ; les terrains africains construisent leur infrastructure de mesure.

### K.9.2 — Leçons pour les pistes

| Piste | Apport de K3 |
|---|---|
| Piste 2 — P-C-E-D-e-d | K3 fournit l'instance non agricole de la grammaire. Le cycle D→e→d est rompu par le plafond Bercy (Drôme) et l'absence de VP (Lac Togo). Le cycle e↔d auto-soutenu (proposition Defalvard) est la formulation idéale à formaliser en F8. |
| Piste 3 — R-PRIORITE-CREANCIERS | K3 est l'instance fondatrice de R-PRIORITE en milieu non agricole. Trois formes de violation documentées. Deux régimes (hard/soft) démontrés. La formule 'l'eau paye l'eau' est la formulation vernaculaire de R-PRIORITE — le MRC lui donne sa forme opposable. |
| Piste 4 — G.9 enrichissements composites | K3 est la deuxième instance après K1 (V^CARE). V^MILIEU = 2 × Q × V × H est formellement justifié par G.9. La projection V^MILIEU → V^IFRS-eau est l'instance type de perte informationnelle irréversible par réduction de base. |
| Piste 5 — Annexe K | K3 est le premier cas pure mode milieu de l'Annexe K. Il complète K1 (Exploitation B, mode milieu agricole + mode comptable) en fournissant le cas mode milieu non agricole multi-acteurs. |
| Piste 6 — RECHERCHE_INTERVENTION | K3 est l'instance fondatrice du régime combiné ENQUETE_OBSERVATIONNELLE ⊗ ENQUETE_COLLECTIVE ⊗ AUTOGOUVERNANCE. GRET est l'acteur tracé type de ce régime. La proposition Defalvard (financer l'animation sur la redevance) est le modèle économique du régime. |

### K.9.3 — Articulation explicite K1 × K3 (Arbitrage F)

L'articulation K1 × K3 est structurante pour l'Annexe K comme référentiel partageable. Les deux cas sont orthogonaux et se renforcent mutuellement.

| Dimension | K1 — Exploitation B (CARE / IDEA4) | K3 — Bassin versant multi-acteurs (GRET) |
|---|---|---|
| Terrain empirique | Exploitation agricole (polyculture-élevage, France) | Bassins hydriques (Togo, Sénégal, France) |
| Mode dominant | Mode milieu (agricole) + mode comptable + mode travail | Mode milieu (non agricole) pur + mode existentiel (nappe fossile) |
| Acteurs clés | Exploitant agricole + expert CARE + comptable | OLGE/PLE/CLE + GRET + ménages + acteurs économiques |
| V^composite | V^CARE = S × P × T × R (sol × plante × troupeau × règle) | V^MILIEU = 2 × Q × V × H (présence × quantité × qualité × horizon) |
| R-PRIORITE-CREANCIERS | Remboursement dette carbone et qualité sol avant distribution agricole | Remboursement dette NH (nappe, lac, fleuve) avant distribution irrigation |
| Régime d'inscription | ENQUETE_COLLECTIVE (IDEA4) + AUTOGOUVERNANCE (exploitant) | RECHERCHE_INTERVENTION (GRET) = ENQUETE_OBS ⊗ ENQUETE_COLL ⊗ AUTOGOUV |
| Annexe H | H.11 (dispositifs comptables CARE) ; smart contracts sur engagements carbone | H.1-H.5 complets (DIDs, VCs dMRV, smart contracts R-PRIORITE) + H.11 |
| Grammaire principale | G-RESPONSABILITE + G-SOIN (exploitant) + G-EVOLUTIVITE (apprentissage CARE) | G-COMMUNALITE + G-SOIN (milieu) + G-MIMETIQUE (vigilance bouc émissaire) |
| Apport mutuel | K1 montre la micro-économie agricole du commun (farm level) ; K3 montre la méso-économie de bassin (watershed level). Ensemble : des deux niveaux d'analyse ostromiens (opérationnel + choix collectif). | K3 montre les défaillances de la gouvernance multi-acteurs que K1 ne peut pas voir (collège absent, plafond Bercy, régime hard/soft). Ensemble : les deux cas couvrent l'articulation Couche 1 ↔ Couche 2 (régime attentionnel ↔ mode d'application). |

| Synthèse K1 × K3 — Ce que les deux cas produisent ensemble |
|---|
| K1 (Exploitation B) : cas comptable agricole. Démontre le mode milieu à l'échelle de l'exploitation (farm level), le mode comptable (Fiche F8, IDEA4/CARE), le mode travail (pratiques agricoles). Instance type : un exploitant qui tient un registre de communalité de son propre sol et troupeau. |
| K3 (Bassin versant GRET) : cas hydrologique multi-acteurs. Démontre le mode milieu à l'échelle du bassin (watershed level), le mode existentiel (nappe fossile, horizon millénaire), la gouvernance multi-acteurs. Instance type : une instance (OLGE/PLE/CLE) qui tient un registre de communalité d'un bien commun partagé par des centaines de milliers d'usagers. |
| Ensemble, K1 et K3 couvrent deux niveaux d'analyse ostromiens (opérationnel et choix collectif), deux formes de V^composite (V^CARE et V^MILIEU), deux régimes d'inscription (ENQUETE_COLLECTIVE et RECHERCHE_INTERVENTION), et deux régimes de R-PRIORITE-CREANCIERS (micro et méso). L'Annexe K consolidée K1 + K3 constitue un référentiel partageable et robuste. |

### K.9.4 — Perspectives K4-K6 préfigurées par K3

K3 préfigure les cas suivants de l'Annexe K :

• K4 (DPQT hospitalier) : G-SOIN et G-JUSTICE sont activées dans K3 (capabilité plancher eau potable) et trouveront leur instance pure dans le milieu hospitalier (soin des personnes, G-SOIN au sens plein).

• K5 (déchets nucléaires longue durée) : signal_horizon_incommensurable levé dans K3 sur la nappe fossile des Niayes préfigure le cas K5 (R-INTERDIT-ABSOLU pour les horizons millénaires irremboursables). La résonance est explicite dans la note de cadrage.

• K6 (crise institutionnelle bouc émissaire) : signal_bouc_emissaire_potentiel levé dans K3 (Flamay Ahiafor, 8 avril 2025) préfigure G-MIMETIQUE pure de K6. K3 est ainsi le terrain de détection précoce ; K6 sera le terrain d'analyse systématique.

## Annexe K3.a — Données chiffrées consolidées

Tableau de référence pour les calculs et typages du cas chiffré K3.

| Donnée | Terrain | Valeur | Source |
|---|---|---|---|
| Budget projet REGIRE | Lac Togo | 834 992 € / 3 ans (2023-2026) = 278 331 €/an | Fiche-projet GRET 2023 |
| Bénéficiaires REGIRE | Lac Togo | 269 397 bénéficiaires finaux directs | Fiche-projet GRET 2023 |
| Surface bassin Haho | Lac Togo | 3 400 km² | Wikipedia FR / FAO AQUASTAT |
| Surface bassin Sio | Lac Togo | 2 800 km² | Wikipedia FR / FAO AQUASTAT |
| Surface lac étiage | Lac Togo | 46 km² (15 km × 6 km) | Wikipedia FR |
| Population couverte | Lac Togo | ~30 % population togolaise | GRET / IRD |
| Budget GIREL phase 1 | Niayes | 493 000 € (2019-2022) = ~98 000 €/an | Site Sénéo / GRET |
| Nombre PLE | Niayes | 14 PLE en zone des Niayes | GRET 2024 |
| Membres PLE Mont-Rolland | Niayes | 58 membres | GRET / CR Faire Commun 2024 |
| Baisse nappe profonde | Niayes | ~45 cm/an | BGS Earthwise / Cisse et al. Cahiers Agric. |
| Pesticides Guédiawaye | Niayes | 51,21 µg/L (×102 norme OMS de 0,5 µg/L) | Cisse et al. / Synthèse Sci. & Technologie |
| Pesticides Malika | Niayes | 37,68 µg/L (×75 norme OMS) | Cisse et al. |
| Salinité Potou | Niayes | 690 mg/L (×3,4 norme OMS de 200 mg/L) | BGS Earthwise |
| Nitrates | Niayes | 1,21 à 227 mg/L selon sites | Cisse et al. |
| Production maraîchère | Niayes | 80 % production maraîchère sénégalaise ; 80 % exportations horticoles | Solidaridad / ResearchGate |
| Surface bassin SAGE | Drôme | 1 640 km² ; 83 communes ; ~30 % département | Gest'eau / SMRD |
| Membres CLE | Drôme | 52 membres (3 collèges) — Source CR GRET indique 26 élus + État + usagers | CR Faire Commun 2024 / Gest'eau |
| SAGE adopté | Drôme | 30 décembre 1997 (premier SAGE de France) | Gest'eau |
| CLE créée | Drôme | 1993 (première CLE de France) | CR Faire Commun 2024 |

## Annexe K3.b — Sources mobilisées

Documents GRET (matière primaire) :

• Gilbert M., Desbleds L., Kibler J.-F. (dir.) (2024), Approches par les communs : quel bilan après trois ans d'expérimentation ?, Synthèse atelier 2022, Éd. du Gret, Débats & Controverses n° 15, 252 p.

• GRET / Remix the Commons (2024), Rencontres 'Faire commun ici et ailleurs : prendre soin et maîtriser l'usage de l'eau', Compte-rendu global avril-septembre 2024.

• GRET (2024), Rencontre Visi'eau du 24 septembre 2024 — notes d'atelier.

• GRET (2025), Atelier bilan programme Communs & Gouvernances partagées #2 — table-ronde 8 avril 2025 (Leyronas AFD, Ahiafor GRET Togo, Vielajus, Defalvard et Lequin Coop des Communs).

Sources web complémentaires (données chiffrées) :

• GRET (2023), Fiche-projet REGIRE Lac Togo : gret.org/wp-content/uploads/2023/11/Fiche-projet_REGIRE-Lac-Togo.pdf

• Cisse I. et al., Usage incontrôlé des pesticides dans les Niayes, Cahiers Agricultures / revues.cirad.fr

• BGS Earthwise, Hydrogéologie du Sénégal : earthwise.bgs.ac.uk

• Gest'eau, SAGE Drôme : gesteau.fr/sage/drome

• Site rivière Drôme, PGRE 2021 : riviere-drome.fr

• Solidaridad SI, Évaluation écosystémique Niayes (2024)

Documents MRC mobilisés :

• Note de cadrage MRC — sections Pistes 2, 3, 4, 5, 6 et architecture cible.

• MRC — Annexes G, H, I (signaux), J (glossaire).

• Note d'exploration K3 — arbitrages et périmètre.

Fin du cas chiffré K3

---

## [LACUNES ET LIMITES DE CE FICHIER]

- Conversion mécanique de quatre documents docx : la mise en forme fine (styles, notes de bas de page, images éventuelles) peut être dégradée ; les documents sources restent les originaux de référence en cas de doute.
- Les cas n'intègrent pas le terme « valorimètre », `collectif_comme_juge` ni les invariants §7bis/§7ter ; leur articulation au modèle est portée par NT-ARCH §8 (lecture intégrée K1).
- Les données chiffrées sont reprises des sources de chaque cas, non re-vérifiées sur pièces comptables primaires.
