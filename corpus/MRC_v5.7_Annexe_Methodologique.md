# MRC v5.7 — Annexe méthodologique (étendue)

> **« Écriture duale »** (décision du porteur ; `Note_Desambiguisation_Ecriture_Duale_2026-09-29.md`). **« Écriture duale » désigne la seule écriture miroir entre deux teneurs** (N2, formalisée par PR-35) ; l'objet de L2 est le **registre comptable augmenté** (identifiants Lean : `RegistreComptableAugmente`, `registre_augmente_{coherent, preserve_R1, non_equivalence}`, `registreAugmenteDe/Bis`, `lien_inter_acteurs_porte_par_un_registre_augmente`, `les_deux_registres_augmentes_ont_le_meme_socle`).

*Méthodes formelles non normatives · mécanisme de renvoi des sources · questions méthodologiques et programme de preuve ProfReg · journal d'avancement, verrous bibliographiques et chantiers ouverts*

Pierre Musseau-Milesi · La Coop des Communs · MRC v5.7 · Régime : vérifiabilité-cohérence

> **État d'inscription.** Le suivi des inscriptions, des décisions prises et des décisions en attente est tenu **exclusivement** dans `MRC_v5.7/_ETAT_INSCRIPTION_v5.7.md` (source unique).

> **Set MRC v5.7.** Architecture à **quatre couches**, alignée sur la nomenclature ProfReg : Couche 0 = primitives ; Couche 1 = régimes et invariants ; Couche 2 = modes d'application (fiches F1–F10) ; **Couche 3 = grammaires transversales**. Architecture : → `MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md` (renvois « NT-ARCH §n » : Partie A). Méthodes, programme de preuve (→ également `MRC_v5.7_ProfReg_Consolide.md`), verrous bibliographiques et chantiers : la présente annexe.

**Objet et périmètre étendu.** Cette annexe consolide en un seul fichier tout ce qui, dans le set, est *méthodologique et non normatif* : (§A) les méthodes formelles mobilisées par les fiches et les grammaires ; (§B) le mécanisme de renvoi des sources (solution de rattachement) ; (§C) les questions méthodologiques ouvertes et le programme de preuve ProfReg ; (§D) le journal d'avancement — amendements, théorèmes, verrous bibliographiques, chantiers et Vagues de travail. Une grammaire (Couche 3) qualifie normativement une interaction ; une méthode fournit un instrument de calcul ou de représentation sans engagement normatif réfutable propre. Les confondre serait un \[CHANGEMENT DE BASE NON TRACÉ\].

---

# §A — Méthodes formelles non normatives

## §A.1 Objet

Cette annexe accueille les sources académiques qui outillent le MRC sans porter d'engagement éthico-politique réfutable — c'est-à-dire les méthodes formelles et techniques. À la différence d'une grammaire (Couche 3), une méthode ne qualifie pas normativement une interaction : elle fournit un instrument de calcul ou de représentation. Les rattacher à une NT-G serait un \[CHANGEMENT DE BASE NON TRACÉ\] (confusion méthode / grammaire). L'annexe maintient la distinction et reste extensible : d'autres sources méthodologiques pourront y être ajoutées.

Règle de tri (Couche 0). Une source entre dans l'annexe méthodologique si et seulement si : (a) elle fournit un formalisme ou un outil ; (b) elle ne pose aucun engagement normatif réfutable propre ; (c) son usage est transversal à plusieurs modes/grammaires. Sinon, elle relève d'une grammaire (NT-G1 à G12).

## §A.2 Sources méthodologiques inscrites

### §A.2.1 Analyse Formelle de Concepts — Ganter & Wille

Mobilisée par : Fiche F3 (Mode sémantique), sous-couche C-TCFP (Treillis de Concepts Formels Pondérés) et C-2MORPHISME-INTER-CORPUS. Rôle : fournir la structure mathématique (treillis de Galois) qui organise les concepts d'un corpus. L'AFC est une méthode de représentation, sans engagement normatif : elle ne dit pas ce qui est juste, elle structure ce qui est dit. Référence : Ganter, B. & Wille, R., Formal Concept Analysis: Mathematical Foundations, Springer, 1999 \[PLAUSIBLE, NON VÉRIFIÉ — édition à confirmer\].

## §A.3 Réserve d'extension

Peuvent ultérieurement rejoindre cette annexe (sous réserve de la règle de tri du §1) : les outils de calcul d'irréversibilité (catégorie Exist, Annexe G.5), la double catégorie ProfReg (Lean 4 / Mathlib) en tant qu'instrument de vérification formelle, et tout dispositif cryptographique (DIDs / Verifiable Credentials) en tant que méthode de traçabilité. Ces éléments sont aujourd'hui décrits dans les Annexes G et H du MRC ; leur regroupement méthodologique est une option d'organisation, non une obligation. \[LACUNE : périmètre exact de l'annexe à arbitrer par le porteur.\]

## §A.4 Articulation avec le compte des 12 grammaires

L'existence de cette annexe est ce qui permet de tenir le plafond de 12 grammaires : les sources méthodologiques n'y comptent pas. Le MRC compte donc exactement 12 grammaires (NT-G1 à NT-G12) plus une annexe méthodologique, et non 13 grammaires. Statut du « plafond » : discipline de gouvernance révisable, non invariant d'architecture — voir Architecture §C.2 (deux tests de Couche 0 : règle de tri §A.1, non-réductibilité).

> **§A.4bis — Cadrage : le set compte 12 grammaires.** Le set compte 12 grammaires : aucune 13ᵉ grammaire n'est créée. **Engagement §0.3** (production par révision/intégration sans grammaire nouvelle) : **CLOS**. Les candidats réfutateurs sont **résolus « non »** : la futurité (→ §A.5), l'autohistoire du dispositif (→ NT-G4) et **DARN** (articulation MRC × DARN comme méthode, « même structure » : contrepartie réfutable **reportée v6**, non effacée). **Ce n'est pas une clôture définitive du questionnement :** chacune des contreparties réfutables — dont la réserve « la futurité instituée oriente-t-elle ou oblige-t-elle ? » (→ §A.5) — est **reportée à la v6** avec son statut `[ENGAGEMENT À HORIZON IRRÉVERSIBLE — délibération v6]`, non effacée. Renoncer à la 13ᵉ grammaire *dans le set actuel* n'équivaut pas à trancher *définitivement* que ces gestes sont réductibles : le second énoncé engagerait un horizon irréversible et reste ouvert. Le statut du « plafond » demeure : discipline de gouvernance révisable, non invariant d'architecture.
>
> **§A.4ter — Mode de révision de la clôture (décision du porteur).** `[CHANGEMENT DE BASE TRACÉ — niveaux 0/1]` La clôture « 12 grammaires » de §A.4bis relève d'une **décision de cadrage**, tandis que la règle de tri (§A.9, primitive « §0.2 » du programme) pose que la question de la 13ᵉ grammaire se tranche **par test de réfutabilité, non par quota**. Pour lever l'`[INCOHÉRENCE INTER-COUCHES — niveaux 0/1]` entre la règle de tri et le mode de clôture effectif, la clôture est une **discipline de gouvernance révisable**, dont la **modification ou la réouverture procède par vote** de la communauté de gestion du MRC (une fois instituée). Deux plans, tenus distincts et non conflatés (`[DÉCOUPLAGE DE RÉGIMES déclaré]`) : (a) **rouvrir/modifier la clôture** est un acte de **cadrage → par vote** ; (b) **admettre effectivement une 13ᵉ grammaire** reste soumis, après réouverture, au **test de réfutabilité de §A.9** — un vote peut lever le palier, il **ne dispense pas** du test. La règle §A.9 demeure donc l'arbitre du *contenu* ; le vote arbitre le *statut du palier*. Réserve : tant que la communauté de gestion n'est pas instituée, le porteur du vote n'est pas encore constitué → `[INCOHÉRENCE INTER-COUCHES — niveau 2 : porteur du vote non encore institué]`, signalée, non lissée.

## §A.5 Futurité-Commons comme lecture méso de niveau méthode

`[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ — déclaré, non lissé]` Le découplage est entre la futurité *descriptive* (Commons 1931, *« Institutional Economics »*, *AER* 21(4), p. 648-657 — axiologiquement neutre, y compris « futurité de domination ») et le régime *normatif* (G-RESPONSABILITE, horizon irréversible). **Inscription (source primaire `Lamarche et al. 2021` lue \[VÉRIFIÉ\]) :** la futurité est inscrite comme **lecture méso de niveau méthode** (non comme grammaire), couplée à G-PERFORMATIVITE (projection) et **ne déclenchant** G-RESPONSABILITE **qu'**à l'horizon irréversible. Chez Lamarche et al. 2021, la futurité « **oriente** » les dispositifs, elle n'« **oblige** » pas → **pas d'engagement réfutable propre en l'état → pas de 13ᵉ grammaire**. **Réserve (reportée v6, cf. §A.4bis) :** si l'instruction « orientation vs obligation » établissait qu'une futurité *instituée* crée une obligation de cohérence projection↔dispositif **non** réductible à G-PERFORMATIVITE × G-VALUATION, l'option « 13ᵉ grammaire » serait rouvrable — mais **en v6**. *Articulation :* le cadre de lecture méso complet est inscrit au §A.7 ; la présente section en porte l'usage futurité. La futurité reçoit une **forme d'inscription** — cadre diagnostique et cadre pronostique — au **§A.5bis**. Ce complément ne touche pas le motif du refus de la 13ᵉ grammaire ci-dessus : il fournit une forme, non une obligation, et la réserve « orientation vs obligation » reste reportée v6.

## §A.5bis Structure de cadrage de la futurité — diagnostique / pronostique

 Origine : `Lecture_Numero74_Meso-ESS_x_MRC_2026-09-14.md`, proposition P4. Source : Lanciano E. & Saleilles S. (2026), « Pour une approche processuelle de la futurité dans les espaces méso-critiques », *Revue Interventions économiques* 74, DOI 10.4000/15naf, reprenant Snow D. A., Rochford E. B., Worden S. K. & Benford R. D. (1986) et Goffman.

### §A.5bis.1 Ce que cette structure ne fait pas — à lire avant le reste

**Il ne rouvre pas la question de la 13ᵉ grammaire, et ne la préempte pas.** Le §A.5 refuse la grammaire au motif que, chez Lamarche et al. (2021), la futurité « oriente » et n'« oblige » pas — donc pas d'engagement réfutable propre. **Ce motif est intact.** La présente structure ne crée **aucune obligation** : elle fournit une **forme d'inscription** à ce que le §A.5 tenait déjà pour une lecture de méthode.

La réserve « orientation vs obligation » reste ouverte et reportée v6 (→ §A.4bis), avec son statut `[ENGAGEMENT À HORIZON IRRÉVERSIBLE — délibération v6]`. La présente structure **n'en constitue pas l'instruction**, et la clôture « 12 grammaires » n'est pas touchée — sa révision procède par vote de la communauté de gestion (→ §A.4ter), non par versement de méthode.

### §A.5bis.2 Deux champs, non une alternative

Les deux cadres **ne s'excluent pas** : ils coexistent dans une même futurité — l'un convertit un phénomène en problème, l'autre propose des voies de résolution. Deux champs sont donc posés, non une alternative :

| Champ | Valeurs | Ce qu'il qualifie |
| :-- | :-- | :-- |
| `cadre_diagnostique_nature` | **COHERENT / AMBIGU / NON_INSTRUIT** *(défaut)* | La façon dont le problème est posé : renvoie-t-elle à des cadres de référence explicites, ou reste-t-elle ouverte à des interprétations divergentes ? |
| `cadre_pronostique_nature` | **COHERENT / AMBIGU / NON_INSTRUIT** *(défaut)* | La façon dont les voies de résolution sont posées : une seule, explicite — ou plusieurs, laissées ouvertes ? |

`NON_INSTRUIT` est **la valeur par défaut**, pour la même raison qu'au §A.17.3 et qu'au §8.2bis de NT-ARCH : sans elle, le silence se lirait comme une déclaration, et l'instrument produirait le défaut qu'il vise.

### §A.5bis.3 Ce qui est formel et ce qui est empirique — la distinction décisive

Un marqueur `[FUTURITÉ MAL FORMÉE]` déclenché par `diagnostique = AMBIGU` transformerait un résultat empirique monographique en défaut de forme, ce qui est précisément le `[DÉCOUPLAGE DE RÉGIMES]` que le set interdit. Deux marqueurs distincts sont donc posés.

**(a) `[FUTURITÉ MAL FORMÉE]` — marqueur formel.** Se déclenche lorsqu'une écriture **prétend inscrire une futurité** sans déclarer ses deux cadres. C'est une exigence de complétude, sans contenu empirique : elle ne dit rien de la valeur de la futurité, seulement qu'elle n'est pas inscrite entièrement. Homologue de forme du triplet exigé par `cloture_declaree` (→ NT-ARCH §8.2bis).

**(b) `[ALTERNATIVITÉ FRAGILE — hypothèse de lecture]` — marqueur empirique, non bloquant.** Se pose lorsque `cadre_diagnostique_nature = AMBIGU`. Il **n'est pas** une condition de bonne formation : il signale qu'une hypothèse de lecture, datée et monographique, est en jeu. Il ne bloque aucune inscription.

L'hypothèse en question, énoncée par ses autrices : *« La cohérence du diagnostic fonde l'alternativité, tandis que l'ambiguïté du pronostique ouvre des futurs possibles »*, et *« La pluralité est donc souhaitable au niveau des solutions, mais non au niveau de l'appréhension du problème. »* `[PLAUSIBLE, NON VÉRIFIÉ]`.

### §A.5bis.4 Homonymie déclarée — « pronostic » a déjà un sens dans le set

`[CHANGEMENT DE BASE TRACÉ]` Le mot **pronostic** est déjà employé dans NT-G10 au sens jonasien — *« priorité au pronostic catastrophique »*, critère de précaution issu de G-RESPONSABILITE. Le **cadre pronostique** de Snow et al. n'a aucun rapport : il désigne la façon dont un collectif formule les voies de résolution d'un problème qu'il a posé.

**Règle d'usage, obligatoire :** ne jamais employer « pronostic » seul dans le set. Écrire soit « pronostic catastrophique (Jonas, → NT-G10) », soit « cadre pronostique (Snow et al., → §A.5bis) ». Laisser l'homonymie implicite serait un `[CHANGEMENT DE BASE NON TRACÉ]`.

### §A.5bis.5 Non-réductibilité

Recherche sur les dix-sept fichiers du set des chaînes `cadrage`, `cadre diagnostique`, `pronostic`, `diagnostique`, `Goffman`, `Snow et al`. **Aucune structure existante.** Les occurrences relevées sont : le pronostic catastrophique de NT-G10 (sens jonasien, *supra*), un verbe dans une table théorique de NT-G9, un adjectif dans une condition de réfutation de NT-G5, et des emplois de « cadrage » au sens ordinaire de « note de cadrage ». La structure ne recouvre rien.

**Elle ne crée pas non plus de grammaire** : elle ne porte pas d'engagement réfutable propre, et son contenu empirique est explicitement tenu hors du formel (§A.5bis.3). Règle de tri §A.9 : non franchie, et il n'est pas proposé de la franchir.

### §A.5bis.6 Conditions de réfutation

**De l'hypothèse de lecture (b).** Elle tombe si un espace méso-critique maintient durablement son alternativité avec un cadre diagnostique ambigu. **Condition d'usage normatif : deux terrains supplémentaires au moins.** Le résultat de Lanciano & Saleilles est monographique — une métropole, dix-sept ans — et les autrices le présentent comme une *proposition de recherche*, non comme une loi. L'employer aujourd'hui pour qualifier un espace serait une sur-généralisation.

**De la structure elle-même (a).** Elle est mal posée si le codage diagnostique / pronostique ne sépare rien sur les corpus du MRC — c'est-à-dire si toutes les écritures y reçoivent les mêmes valeurs. La structure serait alors un formalisme sans pouvoir discriminant et devrait être retirée.

*Porteur :* porteur MRC. *Horizon :* institutionnel, révisable. *Critère de vérification :* application à deux corpus existants — registre de soin, cas agro-environnemental — et constat que le codage sépare effectivement les écritures.

### §A.5bis.7 `[LACUNES ET LIMITES DE CETTE SECTION]`

- **Aucun corpus n'est codé.** La structure existe, elle n'a pas servi ; son critère de vérification n'est pas satisfait. C'est l'un des **trois instruments posés sans être éprouvés**, avec C-CLOTURE-ACCES (→ NT-ARCH §8.2bis) et `statut_grammaire` (→ §A.17).
- **La source est lue une fois, dans un PDF à encodage défectueux** — texte reconstitué par décodage des identifiants de glyphes, fiable sur les mots, sans pagination. Les citations du §A.5bis.3 sont à recontrôler sur l'original avant tout usage en publication.
- **Snow et al. (1986) et Goffman ne sont pas lus.** Ils sont connus par la reprise qu'en font Lanciano & Saleilles. `[À CONTRÔLER SUR SOURCE PRIMAIRE]`.
- **Le cadre motivationnel, troisième type chez Snow et al., n'est pas versé** — les autrices l'écartent de leur analyse, et rien n'a été instruit à son sujet. Son absence est un choix hérité, non un arbitrage du MRC.
- **La frontière COHERENT / AMBIGU n'est pas outillée** et relève du jugement de l'analyste, comme la frontière STRUCTURANT / SECONDAIRE du §A.17.

---

## §A.6 Verrou 03 (commutativité micro-macro CARE→CENP) : voie 3 « double comptabilité déclarée »

Pour articuler la comptabilité **micro** (CARE, niveau entité) et **macro** (CENP, niveau territorial/planétaire), le MRC retient la **voie 3 — double comptabilité déclarée** : **maintenir deux dettes distinctes** (CARE / CENP) et **déclarer explicitement leur non-équivalence**, plutôt que de les harmoniser. C'est un choix de **méthode** conforme au régime : le `[DÉCOUPLAGE DE RÉGIMES]` micro-macro est **déclaré et assumé**, non résorbé par une synthèse non fondée. *À lire avec* l'invariant `obligationpreservation_derivable` (NT-ARCH §7ter). **Voies non retenues :** voie 1 (harmonisation descendante) et voie 2 (réconciliation itérative) exigent un **porteur normatif** (autorité publique — note 05 De Schutter, A/HRC/56/61 ; position adverse de la voie 1 documentée note BEE p. 36) ; elles restent **rouvrables en v6**. *Statut de preuve :* la commutativité micro-macro (nœud D, PR analogue à PR-5) est **reportée v6.x, hors Mathlib** : `[PLAUSIBLE, NON VÉRIFIÉ]`. La forme atteignable en l'état est la **gouvernance calculable de la non-clôture** (déclaration obligatoire des deux dettes et de leur non-équivalence). *Porteur :* porteur MRC / architecte. *Horizon :* institutionnel (voie 3) ; voie 1 engagerait un horizon irréversible (autorité publique).

> ### (proposition P9) — et ce qu'elle ne fait pas
>
> **Ce qui est versé.** Le n° 74 d'*Interventions économiques* (« L'approche méso de l'ESS : vers un nouveau paradigme ? », 2026) fournit **dix études empiriques indépendantes** dans lesquelles le bouclage méso → macro **ne se fait pas en pratique**. Celle, Ballon & Lévesque, en conclusion de leur lecture transversale : *« la difficulté d'une majorité d'articles à aborder l'articulation et le bouclage avec le macro »*, et : *« Ce constat interroge à la fois la capacité de l'approche méso à pouvoir saisir ces potentielles dynamiques de transformation sociale et écologique, ou bien la capacité même de l'ESS et ses composantes à pouvoir l'engager. »*
>
> **Ce que cela déplace, et c'est borné à la voie 1.** La voie 1 — harmonisation descendante — suppose qu'un **porteur normatif** puisse faire tenir l'articulation de haut en bas. Dix monographies où l'articulation ne tient pas **augmentent le coût de cette hypothèse** : la soutenir demande d'expliquer pourquoi elle échoue là où elle est observée. C'est à ce titre, et à ce seul titre, que le versement se fait.
>
> **Ces dix études ne confortent pas la voie 3.** Lire ces études comme faisant de la non-clôture micro-macro « un fait attesté du champ, ce qui conforte la voie 3 », ce serait **prendre l'absence d'un résultat pour un résultat — exactement la sur-revendication que le set traque** : que dix enquêtes ne parviennent pas à boucler n'établit pas que le bouclage est impossible, ni que la déclaration de non-équivalence est la bonne réponse. La voie 3 reste retenue **pour ses raisons propres** — elle ne requiert aucun porteur normatif —, non parce que d'autres ont échoué.
>
> `[RÉSERVE D'HOMOLOGIE, HÉRITÉE ET MAINTENUE]` L'assimilation « verrou 03 / nœud D ↔ bouclage méso → macro » est une **construction de la note de lecture**, qui la déclare telle : l'une est l'absence d'une **preuve formelle**, l'autre l'absence d'un **résultat empirique**. Les traiter comme un seul problème serait une erreur. `[PLAUSIBLE, NON VÉRIFIÉ]` Instruction : `Decision_P9_Verrou_Macro_x_Avaries_Communes_2026-09-14.md`.

## §A.7 Lecture méso — grille des canaux comme cadre d'agrégation (méthode, non grammaire)

Un espace méso (filière, territoire, profession) n'est pas une primitive du MRC : c'est un **périmètre d'agrégation** que l'analyste construit en regroupant des écritures (F1–F8) partageant une logique de différenciation. La grille des canaux — Travail, Produits-Concurrence, Nature, Gouvernance, Futurité (→ §A.5) — sert de **cadre de lecture** pour (a) identifier par quel(s) canal/canaux un espace se différencie, (b) tester la cohérence interne du périmètre, (c) examiner son articulation au macro. Cette lecture est **descriptive** : elle mobilise les grammaires existantes sans en être une.

> **Version de la grille retenue — datation obligatoire.** `[CHANGEMENT DE BASE TRACÉ]` La grille des canaux **n'est pas stabilisée chez ses auteurs**. Le présent §A.7 en fixe **une** version, datée ; il ne fixe pas « la » grille méso. Toute citation du §A.7 doit reprendre cette datation — présenter la grille comme un acquis du champ serait un `[CHANGEMENT DE BASE NON TRACÉ]`, le set gagnant une stabilité que son ancrage n'a pas.
>
> | Version | Source | Canaux |
> |---|---|---|
> | 3 canaux | Lamarche, Grouiez, Nieddu, Chanteau, Labrousse, Michel, Vercueil (2021) | Travail · Produits-Concurrence · Futurité |
> | 4 canaux | Lamarche & Bastien (2025), ch. 5 §3.3 | + Relation à la nature |
> | 5 canaux | Ballon & Celle (2023) | + Gouvernance **et** Environnement |
> | **Retenue au §A.7** | composite des trois ci-dessus, fixée le 2 juillet 2026 | Travail · Produits-Concurrence · Nature · Gouvernance · Futurité (+ Monnaie, hors grille source) |
>
> **Trois écarts à déclarer, faute de quoi ils passent pour des évidences.**
>
> 1. **La grille retenue est composite : elle n'existe telle quelle chez aucun auteur.** Ne pas l'attribuer à Lamarche & Bastien ni à Ballon & Celle.
> 2. **Le canal « Environnement » de Ballon & Celle est identifié ici au canal « Nature » de Lamarche & Bastien.** Cette identification est une **décision du MRC**, non un résultat des sources. *Condition de réfutation :* si les deux canaux recouvraient des objets distincts — par exemple un canal Environnement portant le rapport aux dispositifs environnementaux (labels, REP, taxonomie) et un canal Nature portant le rapport au vivant —, la fusion tomberait et la table serait à scinder.
> 3. **Le canal « Monnaie / circuits financiers » est propre au MRC.** Il n'a **aucune source dans la littérature méso** et ne doit jamais être cité comme un canal de la grille des canaux.
>
> *Motif de la datation.* L'instabilité est déclarée par le collectif lui-même. Celle, Ballon et Lévesque (2026) : « la notion de canaux n'est pas stabilisée », et ce numéro « permet de constater une appropriation hétérogène, selon les articles, des canaux (trois ou quatre canaux, avec un usage plus ou moins central pour apprécier l'ÉSS et ses composantes) ». La localisation de la gouvernance y est explicitement laissée ouverte : « il serait intéressant de clarifier où se situe la gouvernance dans les canaux, car elle apparaît souvent étudiée via le canal travail ». Marie-Claire Malo, dans l'entretien du même numéro, demande où loger « la gestion des avoirs […], la question du surplus (où va-t-il ?), la concentration du capital » — « dans le canal travail ? Le canal gouvernance ? Dans un canal manquant ? ».
>
> *Condition de réfutation de la datation elle-même.* Si une publication ultérieure du collectif **fixe** la grille, la mention de version devient superflue et doit être **retirée**, non maintenue par inertie.
>
> *Porteur :* porteur MRC. *Horizon :* institutionnel. *Critère de vérification :* présence, au §A.7, de la date de fixation, de la table des versions concurrentes, et des trois écarts déclarés ci-dessus.

**Table de cartographie canal → grammaire(s) (rapports de périmètre déclarés, non identités).**

| Canal | Grammaire(s) recouvrante(s) | Statut | Reste déclaré |
|---|---|---|---|
| Travail | NT-G11 (C-MURRAY, `collectif_comme_juge`), NT-G3, NT-G7 | Couvert (mode d'application) | — |
| Nature | NT-G5 (`mode_metabolique_actif`, `état_habitabilité_milieu`), NT-G2 (`seuil_degredation_irréversible`), NT-G3 (branche non-humain) | Couvert | métabolisme-méso (ci-dessous) |
| Gouvernance | NT-G6 (faisceaux Schlager-Ostrom, `parite_participation` lu de NT-G7 — ex-`parite_deliberative`, nom aligné le 13/10/2026) × NT-G10 | Couvert — Couche 2, intersection F6×F10×F1 ; échoue au test de non-réductibilité | — |
| Produits-Concurrence | NT-G12 × NT-G4 (qualité/label/prix) ; **clôture et éligibilité → F8 §8.2bis (C-CLOTURE-ACCES)** | Couvert pour la qualité ; **clôture couverte par C-CLOTURE-ACCES** | — *(reste levé, cf. ci-dessous)* |
| Futurité | NT-G4 (projection) × NT-G12 (écart valorimètre/convention) × NT-G2 (au seul horizon irréversible) | Lecture de méthode (→ §A.5) | réserve « orientation vs obligation » (→ §A.4bis) |
| Monnaie / circuits financiers | NT-G12 (`C-MOUVEMENT-TYPE.R`) × `marquagemonetaire` (candidat C2, **niveau méso déclaré**, → §A.11) | Lecture de méthode (descriptif) | usage écologique « monnaie post-croissance » reporté v6 (F4, horizon irréversible) |

Deux composantes descriptives relèvent de cette lecture (elles décrivent des régularités de régime, non des obligations). **L'une des deux a un domicile de Couche 2** :

— **métabolisme-méso** (un régime métabolique d'espace : flux matière/eau/énergie/carbone à l'échelle d'un périmètre méso) — couplé à G-MESOLOGIE quand il devient milieu vécu, à G-RESPONSABILITE quand un seuil devient irréversible ;
— la composante **clôture** (oligopole, stratégie de retrait, alliance hégémonique) **a un domicile de Couche 2** : la sous-couche **C-CLOTURE-ACCES** de la fiche F8 (→ NT-ARCH Partie B, §8.2bis), avec deux champs déclarés — `cloture_declaree` (triplet : qui est exclu, par quel dispositif, qui l'a posé) et `enjeu_acces` (MARCHE / FINANCEMENT / COMMANDE-PUBLIQUE / AGREMENT / GISEMENT-MATIERE / RECONNAISSANCE / AUCUN / NON_DETERMINABLE).

> **Le mode d'inscription, à ne pas perdre.** La clôture n'est **pas** inscrite comme propriété d'un espace — le MRC n'a pas d'espace méso pour primitive et lui en donner une serait un `[CHANGEMENT DE BASE NON TRACÉ]`. Elle est inscrite comme **condition d'une écriture**, et **l'espace se lit par agrégation** de ces conditions sur un périmètre construit par l'analyste, conformément au présent §A.7. La lecture méso reste donc une méthode ; avec C-CLOTURE-ACCES, elle a quelque chose à agréger.
>
> *Contrepartie réfutable, portée au §8.2bis.* Si `enjeu_acces` vaut `AUCUN` sur la quasi-totalité d'un corpus instruit, le canal Produits-Concurrence est **inopérant pour ce corpus** et doit être déclaré tel — un canal inopérant est un résultat, non un échec de codage. Si le constat se répétait sur tous les corpus du MRC, c'est la sous-couche qui serait à retirer.

**Reste sans domicile : le métabolisme-méso.** Il n'en réclame pas — il décrit une régularité de régime, non une obligation — et sa condition de réfutation est celle du garde-fou ci-dessous.

*Garde-fou.* Ces composantes sont des **dimensions de lecture**, jamais des engagements réfutables propres ; les présenter comme des grammaires serait un `[CHANGEMENT DE BASE NON TRACÉ]`. *Condition de réfutation.* L'échelon méso est mal posé si l'une de ses composantes se révélait porter un engagement réfutable propre non réductible aux grammaires de couplage indiquées — elle rejoindrait alors le statut de candidat (règle de tri, §A.9).

**Corpus de contrôle — *Interventions économiques* n° 74 | 2026.** Le numéro spécial « L'approche méso de l'économie sociale et solidaire : vers un nouveau paradigme ? » (douze textes, répertoire `méso/`) sert de corpus de contrôle de la table ci-dessus. Trois constats, portés ici sans conséquence sur la table — les conséquences éventuelles sont instruites hors §A.7 :

— **Gouvernance.** Le numéro **pose** la question de la localisation du canal et ne la tranche pas. Le §A.7 y répond : Gouvernance = NT-G6 × NT-G10, *échoue au test de non-réductibilité*. Cette réponse est **plus avancée que le champ**, et à ce titre exportable — elle est réfutable au même titre que le reste.
— **Produits-Concurrence.** Trois articles du numéro en font le canal **structurant** (Magne & Vallade 2026 sur les SCIC ; Cordrie, Grassart & Bayard 2026 sur l'accès aux gisements et aux fonds réemploi ; Grassart & Sébert 2026 sur les conditions concurrentielles d'émergence des AMEP).
— **Nature.** Le canal n'est instruit dans **aucun** des articles empiriques du numéro, ce que l'introduction constate elle-même (« le canal du rapport à la nature […] n'a toutefois pas été étudié dans les articles de ce numéro »). Le couplage « Nature → NT-G5 × NT-G2 × NT-G3 » de la table reste donc **non éprouvé par le champ** : il est vérifié verbalement contre les textes de cadrage, jamais contre une application empirique. À ne pas citer comme corroboré.

*Sources.* Lamarche et al. (2021), « Saisir les processus méso : une approche régulationniste », *Économie appliquée* 2021/1, p. 13-49 (HAL hal-02998010) — VÉRIFIÉ (PDF lu, source fondatrice des trois premiers canaux). Lamarche & Bastien, *Mésoéconomie*, Dunod, 2025 — corpus partiel (ch. 3 §1.2, ch. 5) `[réserve déclarée]`. Ballon & Celle (2023), *Revue Interventions économiques* 69 — VÉRIFIÉ (canaux Gouvernance **et Environnement**). Celle S., Ballon J. & Lévesque B. (2026), « L'approche méso de l'économie sociale et solidaire : vers un nouveau paradigme ? », *Revue Interventions économiques* 74, DOI 10.4000/15na6 — LU (introduction du numéro ; source de la déclaration d'instabilité de la grille). Bodet C., Lamarche T. & Richez-Battesti N. (2026), « Rethinking the Social and Solidarity Economy and Its Potential for Socio-Ecological Transitions: A Mesoeconomic Approach », *ibid.*, DOI 10.4000/15na7 — LU (cadrage à quatre canaux, en anglais). `[RÉSERVE DE LECTURE]` Les PDF du répertoire `méso/` portent une anomalie d'encodage (polices sans table ToUnicode) ; le texte a été reconstitué par décodage des identifiants de glyphes. **Les citations sont fiables sur les mots, la ponctuation fine ne l'est pas, et les numéros de page ne sont pas disponibles.** Toute citation destinée à publication est à recontrôler sur l'original. Les commutativités canal↔grammaire sont vérifiées **verbalement** (procédural) — les affirmer prouvées serait un `[DÉCOUPLAGE DE RÉGIMES]`.

## §A.8 Protocole d'expérimentation pilote accompagnée (méthode)

Spécifie comment une expérimentation accompagnée — encore pilotée par le chercheur qui accompagne un collectif — **produit des écritures décidables** qui instruisent les lacunes L1 (lecture située du concepteur) et L2 (passage au collectif) de l'usage descriptif, et nourrissent la délibération de bascule Usage 2 → Usage 3. Les règles mobilisées par les indicateurs — **R0-bis** (suspension de valuation) et **R0-ter** (déclaration de situation) — sont définies au **§A.14**.

**Règle de portage (décision du porteur).** Le portage du MRC reste unique (régime mono-porteur, §D.12) ; mais **chaque expérimentation accompagnée désigne à son ouverture un porteur d'expérimentation nommé** — le chercheur-pilote de la campagne, distinct du porteur MRC — qui porte, pour cette campagne : la déclaration de situation R0-ter, le journal des reprises, et le renseignement des indicateurs I-1→I-6. Sans cette désignation, aucune écriture de campagne n'est inscriptible — un protocole sans porteur nommé est un `[ENGAGEMENT SANS SYMÉTRIE]` (homologue de l'exigence porteur/horizon/critère des lots). La désignation, son horizon et sa révocation sont tracés au journal de campagne. Le protocole transforme ces lacunes en **questions empiriques** plutôt qu'en présomptions. Aucune grammaire, aucun invariant de Couche 1 (méthode).

**Indicateurs (déclarés, non calculés par valorimètre — régime procédural).** Aucun seuil chiffré posé a priori : la délibération fixe le seuil d'acceptabilité ; l'expérimentation fournit la mesure et sa traçabilité, pas le verdict.

| # | Question | Mesure dans le pilote | Inscription MRC |
|---|---|---|---|
| I-1 Traçabilité du cadrage | Le cadrage situé du pilote est-il déclaré et reprenable ? | Part des catégories appliquées portant déclaration R0-ter + marqueur `[CADRAGE REPRENABLE]` | Déclaration de situation (R0-ter) |
| I-2 Contestabilité effective | Le collectif conteste-t-il, et est-ce inscrit et suivi d'effet ? | Reprises/retraits exercés par le collectif / éléments de cadrage ; part inscrite | Journal des reprises |
| I-3 Co-construction du valorimètre | Le référentiel est-il co-construit ou imposé par le pilote ? | Origine déclarée de chaque valorimètre (importé / co-construit) | `source_valuemetre` (DID) + co-porteur |
| I-4 Suspension de valuation tenue | Les primitives `seuil-valuatif` restent-elles `[VALUATION SUSPENDUE]` sans garantie du pilote ? | Part des usages descriptifs portant le quadruplet « statut du seuil » (R0-bis) | Marqueur R0-bis |
| I-5 Variance inter-lecteurs | La sélection des points dépend-elle du lecteur ? | ≥2 lecteurs appliquent la même grille au même matériau ; divergence **attribuée et inscrite** | Écritures parallèles tracées |
| I-6 Appropriabilité | Un membre du collectif produit-il une écriture défendable sans le pilote ? | Après N sessions, écriture en autonomie ; défendabilité évaluée contradictoirement | Écriture + revue contradictoire |

*Note sur I-5.* L'objectif n'est pas d'annuler la variance inter-lecteurs (constitutive de l'analyse qualitative), mais de la rendre **attribuable et inscrite** : une divergence déclarée et rattachée à un lecteur situé est compatible avec le régime ; une divergence masquée derrière une prétention descriptive ne l'est pas.

**Règle de décision (déclarée, non calculée).** La délibération de bascule Usage 2 → 3 est **éligible** quand, sur le commun pilote : (1) I-1, I-3, I-4 sont renseignés sur au moins une campagne complète ; (2) I-2 montre des reprises réellement exercées et inscrites ; (3) I-6 est positif sur au moins quelques membres ; (4) I-5 est inscrite et attribuée. Ces conditions rendent la délibération *informée*, elles ne la *remplacent pas*.

*Critère de vérification.* Chaque session produit : (a) écritures MRC datées ; (b) déclaration de situation R0-ter ; (c) journal des reprises ; (d) indicateurs I-1→I-6 renseignés. *Condition de réfutation.* Le protocole est invalide si une session produit des écritures sans journal de reprise exploitable, ou si les indicateurs ne sont pas renseignables à partir des traces — l'expérimentation reste alors illustrative, non probante.

> `[ENGAGEMENT À HORIZON IRRÉVERSIBLE]` Ce protocole **n'autorise pas** la bascule : il **documente** ce que la délibération collective devra trancher. Présenter de « bons » indicateurs comme une autorisation serait un `[DÉCOUPLAGE DE RÉGIMES]` (cadre mesuré ≠ système incarné délibéré).

## §A.9 Règle de tri des candidats grammaires

**Règle de tri (générale).** Un candidat n'entre comme 13ᵉ grammaire que s'il exhibe un **engagement réfutable propre** (i) non porté par une grammaire/un opérateur existant **et** (ii) non réductible à une combinaison existante ni à la méthode. La question se tranche par ce test, non par un quota (→ §A.4, Architecture §C.2).

## §A.10 Marketcraft (Vogel 2018) : grille descriptive de la fabrication des marchés (méthode, non grammaire)

*Inscription par décision du porteur. Vogel entre comme **méthode + ancrages descriptifs** versés à des grammaires existantes — **pas de 13ᵉ grammaire** (conforme §A.4bis). Provenance tracée au fichier d'état (`_ETAT_INSCRIPTION_v5.7.md`).*

**Grille d'entrée descriptive.** Steven K. Vogel, *Marketcraft: How Governments Make Markets Work*, Oxford University Press, 2018 — **VÉRIFIÉ sur source primaire (PDF déposé en biblio)** : capture élargie *pro-market / anti-regulation* (lignée Stigler 1971) au rendu PDF p. 140-141 [pagination imprimée ~128 à confirmer] ; « freedom… empirical question » / « no natural or default position » p. 147-148 rendu. **Ch. 2-4 VÉRIFIÉS** : structure des *elements* (ch. 2, TOC p. 8) ; « freest… most governed » (ch. 3, p. 43) ; « liberalization does not mean liberation… construction of market infrastructure » (ch. 4, p. 78) ; « policy change without more competition in [Japan] » (p. 130) ; antitrust Japon 1953 / recession cartels (ch. 4). La matrice de travail USA/Japon (matériau hors set, provenance tracée au fichier d'état) est ainsi adossée à des claims vérifiés au mot près (Tables 3.1-4.2 non ré-extraites cellule à cellule). Vogel pose les marchés comme **institutions** — « complex combinations of laws, practices, and norms » (p. 2). La grille **laws / practices / norms** sert d'inventaire descriptif **avant** qualification normative : elle relève de la **règle de tri §A.9** (formalisme transversal sans engagement réfutable propre → méthode). Vogel le déclare lui-même : la liberté est « an empirical question » et « analysts should not begin with any preconceived notion of a natural or default position » (p. 134) — formulation politiste de la **suspension de valuation** (usage descriptif W-10).

**Ancrages descriptifs versés (sans obligation propre) :** frames de *policy* → NT-G4 (en complément du versant STS/DARN) ; couplage micro↔macro (« macro politics shapes micro governance », Gourevitch cité p. 130) → appui descriptif au verrou 03 (§A.6) ; clivages/coalitions réels (*incumbents/challengers* ; contest à trois *shareholders/managers/workers*, p. 129-130) → lectures F6/F10 et G-COMMUNALITE ; « liberté = question empirique » (p. 134) → W-10.

### §A.10bis Discriminant de source du signal « capture » — `capture_Vogel` ≠ `capture_Pistor`

`[CHANGEMENT DE BASE TRACÉ — homonymie déclarée]` Le signal transversal **« capture »** (W-1a, hors Couche 0) reçoit **deux ancrages disciplinaires indépendants**, ce qui **réduit le risque `[CORPUS AUTORÉFÉRENTIEL]`** d'un signal adossé à une seule source. Mais les deux « capture » sont **homonymes, non co-référents** : les fusionner serait un `[CHANGEMENT DE BASE NON TRACÉ]`. Un **discriminant de source obligatoire** est déclaré (homologue de `source_asymetrie_pouvoir`, W-14b) :

| Discriminant | `capture_Vogel` | `capture_Pistor` |
|---|---|---|
| **Discipline** | Science politique de la régulation | Droit (codage juridique) |
| **Définition (vérifiée sur source)** | Capture réglementaire, lignée Stigler 1971, **élargie** par Vogel : *pro-regulation capture*, ***pro-market capture***, ***anti-regulation capture*** (Vogel 2018, **p. 128**, verbatim vérifié) | **Convention opérante du MRC** (note ContreCapture, §0) : déplacement, par des acteurs à ressources juridiques supérieures, du contrôle effectif des **cinq droits du faisceau Schlager-Ostrom** hors de la communauté déclarée, **sans modification formelle** du registre |
| **Mécanisme** | Agence ↔ groupe d'intérêt, gouvernance de marché (méso/politique) | Droit privé ordinaire — contrat, propriété, procédure, choix de loi (micro-juridique) |
| **Source primaire** | Vogel 2018, *Marketcraft*, OUP — VÉRIFIÉ (ch. 1, 5) | Pistor 2025, *The Law of Capitalism and How to Transform It*, Yale UP (ISBN 978-0-300-28280-1) — VÉRIFIÉ (verbatim ch. 3/5/6/7 ; pagination non conservée) |

**Comment les deux définitions s'articulent.** Contrôle procédural sur les sources primaires telles que lues dans les notes de lecture internes (Vogel, PDF lu ; Pistor 2025 lu au mot près, note ContreCapture) :

1. **Convergence de forme.** Les deux décrivent qu'un **acteur doté de ressources supérieures déplace le contrôle effectif de règles** au détriment d'un intérêt collectif — d'où la pertinence d'un signal commun « capture ».
2. **Divergence de référent.** Vogel = capture d'une **agence/gouvernance de marché** (le *qui régule* est retourné) ; Pistor = capture du **code juridique / des droits** (le *droit lui-même* code l'asymétrie, sans capture délibérée d'aucune agence — cf. Pistor 2025, ch. 6, Luhmann : les tribunaux « are programmed to enforce these interests as long as they are presented in the appropriate legal form »).
3. **Couplage asymétrique (déclaré).** `[DÉCOUPLAGE DE RÉGIMES PARTIEL — assumé]` : la capture juridique de Pistor est **un vecteur** de la fabrication politique des marchés de Vogel (sens Pistor→Vogel : compatible) ; mais toute fabrication politique de marché **ne passe pas** par un codage juridique à la Pistor — Vogel inclut *practices* et *norms* irréductibles au droit (sens Vogel→Pistor : non nécessaire). Complémentarité, non identité : Vogel **élargit** le périmètre au-delà du droit.

> `[SOURCE À DISTINGUER]` Les quatre attributs du codage du capital (*priority, durability, universality, convertibility*) relèvent de **Pistor 2019, *The Code of Capital*, Princeton UP** — ouvrage **distinct** de la source d'ancrage du MRC (**Pistor 2025**, *The Law of Capitalism…*). Les deux sont cohérents (même autrice, même thèse du droit comme code du capital) mais **ne doivent pas être confondus** : l'ancrage opérant du set est **2025** (faisceau Schlager-Ostrom + droit privé ordinaire) ; la référence à *The Code of Capital* (2019) reste `[À VÉRIFIER SUR SOURCE PRIMAIRE 2019]` si un usage explicite des quatre attributs est inscrit. Distinction tracée pour éviter un `[CORPUS AUTORÉFÉRENTIEL]` (deux livres traités comme un seul).

*Condition de réfutation du discriminant.* Le discriminant est mal posé si, sur cas instancié, distinguer `capture_Vogel` de `capture_Pistor` ne changeait **jamais** la prescription (routage de révision) — il serait alors un raffinement sans effet, à retirer.

## §A.11 Marquage monétaire (Zelizer 2005a ; Carruthers & Ariovich 2010) — candidat de Couche 2, niveau méso déclaré

*Inscription par décision du porteur. Statut : **candidat de Couche 2, descriptif** (homologue de W-14) — **pas de 13ᵉ grammaire** (§A.4bis). Provenance tracée au fichier d'état (`_ETAT_INSCRIPTION_v5.7.md`).*

**Champ candidat `marquagemonetaire`.** Le marquage = opération sociale qui rend l'argent **non fongible** en le fléchant vers des usages selon la relation qui le porte. Zelizer : « il n'y a pas d'argent unique, uniforme et généralisé, mais des monnaies multiples : les êtres humains marquent les diverses devises en les rapportant à de nombreux types d'interactions sociales » (Zelizer, *La signification sociale de l'argent*, Le Seuil « Liber », 2005 [= 2005a], p. 52 ; marquage p. 27) — **VÉRIFIÉ sur source secondaire déposée** (Chiapello & Violle, *Sociologie des circuits financiers*, 2025, §« Marquage »). Deux appuis Carruthers, **distincts**  : (i) **Carruthers 2017**, « The social meaning of credit, value and finance » (in *Money Talks*, Princeton UP, pp. 73-88), **p. 75-77** = source du marquage **du crédit** (« si l'argent liquide n'est pas marqué, le crédit, lui, l'est toujours, car il implique un prêteur et un emprunteur particuliers ») ; (ii) **Carruthers & Ariovich 2010**, *Money and Credit: A Sociological Approach* (Polity), chap. 2 = synthèse large de la fabrique des monnaies.

**Réductibilité vérifiée : non.** Aucun champ F8 existant ne capte le marquage — `C-MOUVEMENT-TYPE.R` code le *régime comptable*, `P-C-E-D-e-d` l'*ontologie de l'écriture*, `regimeobligation` le *régime d'obligation* ; aucun ne dit « cet argent est fléché pour tel usage, par telle relation, avec tel cloisonnement ». D'où le statut de **candidat de Couche 2**. Zelizer/Carruthers étant **descriptifs** (sans engagement réfutable propre), le candidat **n'ouvre pas de grammaire** (§A.9).

> **⚠️ Réserve de niveau — OBLIGATOIRE à chaque usage.** `[CHANGEMENT DE BASE NON TRACÉ évité]` Le marquage opère à l'échelle du **circuit financier (méso)**, **pas** de l'écriture comptable individuelle (micro). **VÉRIFIÉ sur source primaire déposée** (Chiapello & Violle 2025) : « **les circuits financiers reposent donc sur des marquages** » ; le chap. 5 (Rivière & Ducastel), « Marquages de l'argent : la dynamique d'écologisation de l'industrie électrique en Guadeloupe », instancie le marquage **au niveau du circuit** — lecture **méso**. En conséquence : `marquagemonetaire` est routé **d'abord vers l'échelon méso (§A.7 / canal, W-2b)**, **et** vers F8 (NT-ARCH §8 / NT-G12) **avec le niveau — méso (circuit) ou micro (écriture) — explicitement déclaré à chaque emploi**. Router le marquage vers F8 (micro) sans déclarer le niveau serait un `[CHANGEMENT DE BASE NON TRACÉ — niveau micro/méso confondu]`. Le niveau par défaut est **méso** ; l'usage micro (écriture qui *enregistre* un marquage décidé en amont au niveau du circuit) doit être signalé comme tel.

**Report table §A.7 (canal).** Une ligne descriptive figure dans la grille des canaux méso : *Monnaie/circuits financiers → NT-G12 (`C-MOUVEMENT-TYPE.R`) × `marquagemonetaire` (candidat C2, niveau méso déclaré)*, reste déclaré = usage écologique « monnaie post-croissance » reporté v6 (F4, horizon irréversible).

*Condition de réfutation.* Le champ est réfuté si, sur cas instancié, un usage de `marquagemonetaire` se révèle **entièrement réductible** à `C-MOUVEMENT-TYPE.R` + `regimeobligation` sans reste — il serait alors redondant, à retirer. L'usage écologique (« monnaie post-croissance dédiée à la restauration d'un milieu ») touche des seuils irréversibles → `[ENGAGEMENT À HORIZON IRRÉVERSIBLE — délibération v6, F4/W-12d]`, hors clôture du set.

## §A.12 « Valorimètre » — table d'équivalence texte / identifiants formels

*Décision du porteur.* Le **texte** emploie **« valorimètre »** ; les **identifiants formels ProfReg et les DID** gardent la graphie `valuemetre` (sans accent) pour ne pas rompre la correspondance avec les fichiers `.lean` et les identifiants décentralisés. `[CHANGEMENT DE BASE évité — table d'équivalence déclarée]` :

| Texte | Identifiant formel / DID | Registre |
|---|---|---|
| valorimètre | `source_valuemetre` | champ obligatoire (B4) — **source déclarée et vérifiable ; DID = forme possible, non obligatoire**  |
| valorimètre | **`fraction_exhibe_sa_source`** (CONV-4) | L'obligation de source est portée par CONV-4 et son appui compilé ; l'opposabilité est sanctionnée par **PR-14** `opposabilite_exige_statut_declare` |
| valorimètre (URI) | `valuemetre_uri`, `did:registre:valuemetre:…`, `did:valuemetre:…` | identifiants décentralisés (Annexe H) |

Règle de rédaction : en prose, écrire **valorimètre** ; entre backticks ou dans un DID, conserver **valuemetre**. Toute future recompilation `.lean` qui renommerait les identifiants devra tracer un `[CHANGEMENT DE BASE]` et mettre à jour cette table.

### §A.12bis Préfixes des étiquettes

Le préfixe « A + chiffre » nu désigne plusieurs familles d'objets (axiomes, amendements de grammaires, arbitrages, conceptions BEE). **Règle** : un axiome s'écrit **`AX-n`** (ex. `AX-7`) ; une convention s'écrit **`CONV-n`** ; un palier s'écrit **`PAL-n`** (`PAL-6′`, `PAL-2c`). Un intervalle s'écrit « AX-1 à AX-10 », « PAL-1 à PAL-6′ ». Dans le graphe Mermaid, l'identifiant de nœud est `AX_n`, `CONV_n` (le tiret casserait la syntaxe) et l'étiquette affichée `AX-n`, `CONV-n`. L'axiome de Campo s'écrit `AX-10` ; « votre A1 … A4 » (prémisses de la note de Campo) est cité tel quel.

Les **amendements** de grammaires, les **arbitrages** et les **décisions P1-P9** ne reçoivent pas de préfixe propre : ils gardent leur étiquette, **qualifiée** à la première occurrence (« amendement A5 », « arbitrage A8 », « décision P5 »). Gardent aussi leur étiquette les autres « C + chiffre » et « P + chiffre », qui ne désignent ni une convention ni un palier (conditions C1, C2 de NT-G2 et NT-G7 ; amendements Hache P1-P4, NT-G2, §D.2 ; pistes P1-P6 de l'Annexe K ; principe P2 d'Ostrom). Les **identifiants Lean** (`Regime.A2`, `l_obligation_A2_ne_se_repartit_pas`, `AxiomesMRC.A2`…, `P5_…`, `bienFormeeP7`) et les **noms de fichiers** (`Fiche_Axiome_A8_…`) gardent leur graphie : les renommer toucherait la compilation et les renvois.

**AX-8** désigne l'axiome *Attention de soin : réception et indifférence organisée*. Un « A8 » nu désigne l'**arbitrage A8** (une lacune de table met l'écriture en attente), actif en NT-ARCH §3bis et §8.5.2, Annexe §A.15.11, Annexe H §H.5.2 et PR-29.

## §A.13 Gardes empiriques sur `appel_entendu_milieu` (attachement au lieu — méthode, W-ATT-1)

*Décision du porteur. L'attachement au lieu n'est **ni** un champ dédié, **ni** un matériau inerte : c'est un **matériau de lecture qui donne de la méthode**. Provenance tracée au fichier d'état (`_ETAT_INSCRIPTION_v5.7.md`).*

**Refus d'un champ `attachement` autonome de Couche 2.** Un tel champ **échoue au test de non-réductibilité** (§A.9) : il **duplique** ce que captent déjà `appel_entendu_milieu` (NT-G5, perception du signal du milieu, y compris « attachement rompu »), `signalversaffectif` (NT-G9, cause structurelle affective) et la contre-écriture **R1** (l'attachement mobilisé comme justification qui masque un coût = CRÉDIT sans son DÉBIT). Inscrire un champ dédié serait du **double comptage** — **même motif de rejet que la condition de réfutation de W-14b** (un discriminant entièrement réductible à des opérateurs existants est retiré). Donc : **pas de champ de Couche 2, pas de 13ᵉ grammaire** (conforme §A.4bis).

**Versement de la part opératoire comme méthode (échelon méso).** Trois **gardes empiriques** sont versées comme **dimensions de lecture** du prédicat existant `appel_entendu_milieu` (NT-G5) — elles précisent *à quelles conditions* le passage milieu → responsabilité s'active, sans porter d'obligation propre (donc **méthode**, §A.9, non grammaire) :

| Garde (sur `appel_entendu_milieu`) | Ce qu'elle règle | Source | Condition de réfutation |
|---|---|---|---|
| **Garde d'échelle** (local ↔ global) | Un attachement/appel **local** ne vaut pas obligation **globale** ; leur articulation est l'objet même de l'**échelon méso** (§A.7, W-2b) | Scannell & Gifford 2010 ; Devine-Wright 2009/2013 `[NON VÉRIFIÉ — W-6]` | Si l'attachement local **prédit** l'action globale, la garde est superflue (retrait) |
| **Garde de menace** (distante/cachée vs locale/visible) | Une menace **distante ou cachée** mobilise mal la perception ; en MRC = **dette systémique non attribuée** dont le porteur local ne perçoit pas le signal | Brown, Altman & Werner 2011/2012 **[VÉRIFIÉ]** | Si la perception ne dépend pas de la distance/visibilité de la menace, la garde est superflue |
| **Garde d'effort** (fort/faible) | L'effet attachement → comportement pro-environnemental est **modéré, conditionnel**, et peut être **négatif** pour les comportements à **fort effort** (place social bonding) ; à articuler avec le coût d'action (NT-G12) | Revue *Sustainability* 13(23) 2021 ; méta-analyse *J. Retailing & Consumer Services* 2020 `[NON VÉRIFIÉ — W-6]` | Si l'effet est indépendant du coût d'action, la garde est superflue |

*Garde-fou.* Ces gardes sont des **dimensions de lecture** sur un prédicat existant, jamais des engagements réfutables propres ; les présenter comme des champs ou des grammaires serait un `[CHANGEMENT DE BASE NON TRACÉ]`.

> **Un usage fautif a été constaté, et il n'est pas imputable aux gardes.** L'analyse de l'entretien John-C (`Protocole/John-C/Note_analyse_MRC_John-C_2026-09-18.md` §4.1 a) conclut qu'« au niveau de la grammaire, la garde *effort investi dans le lieu* prendrait ici une valeur négative motivée par l'enquêté lui-même ». Or le verbatim visé — « **je crois qu'il faudrait qu'il soit détruit pour que je sache si j'y étais attaché ou non** » [032] — n'est **pas** une négation : c'est l'attestation explicite que la question n'est pas décidable en l'état, **assortie du critère qui la rendrait décidable**. Le coder en valeur négative d'une garde, c'est **écraser une attestation en une absence**.
>
> **Règle.** Une garde **discipline la lecture d'une valeur ; elle n'en produit jamais**. Le lieu d'inscription d'une indécidabilité attestée est la valeur `INDECIDABLE_ATTESTE` de `appel_entendu_milieu` (NT-G5 §3.1, lemme 3), qui **exige un critère de résolution déclaré** — ici : la destruction du lieu.
>
> `[CORRECTION D'UN USAGE, NON D'UNE GARDE.]` La condition suspensive des trois gardes, W-ATT-4 → W-6 ci-dessous, reste entière. *Réfutation du lot (W-ATT-1) :* si une garde s'avère **non transversale** (propre à un seul mode d'application), elle reste locale, non méthode.

**Condition suspensive (W-ATT-4 → W-6).** Les sources secondaires des gardes d'échelle et d'effort — **Devine-Wright, Scannell & Gifford, revue *Sustainability* 2021, méta-analyse 2020** — sont `[NON VÉRIFIÉ]` **au-delà de la revue jointe** (aucune n'est déposée en biblio). **Aucun durcissement** de ces gardes (passage de dimension de lecture à règle opposable) n'est admis **avant vérification W-6** (lot **W-ATT-4**). Seul **Brown, Altman & Werner** (garde de menace) est **VÉRIFIÉ** sur source primaire. Tant que W-6 n'est pas fait, les trois gardes restent des **candidates de méthode déclarées**, non durcies.

## §A.14 Usage non-normatif et clause de suspension de valuation (méthode, W-10)

*Décision du porteur : rattachement à la présente Annexe (et non à NT-ARCH §C), conformément à la règle de tri §A.9 — la clause est un protocole d'inscription transversal, sans engagement normatif réfutable propre ; elle ne compte pas dans le plafond des 12 grammaires. Provenance tracée au fichier d'état (`_ETAT_INSCRIPTION_v5.7.md`).*

Cette section rend opérationnelle l'affirmation suivante, en évitant qu'elle soit une neutralisation tacite du normatif : *mobiliser le MRC en lecture analytique (sociologie descriptive/constructiviste) est possible à condition de cibler le niveau méthode, non le niveau grammaire-obligation*. La méta-règle « ne pas confondre les deux régimes » est nécessaire mais non suffisante : on peut tenir les régimes distincts *de nom* tout en important un seuil *de fait*. La règle complète est : **« ne pas importer un seuil — ni un cadrage — sans déclarer son statut »**.

### §A.14.1 Définitions (conventions de méthode, Couche 0 non modifiée)

- **Usage non-normatif (lecture analytique)** : mobilisation d'une catégorie du MRC comme *descripteur* d'un état de fait, sans activer la règle de couplage ni l'obligation associée (pas de DÉBIT, aucune règle R-\* déclenchée).
- **Charge valuative d'une primitive** : propriété d'une primitive de Couche 0 selon que ses *conditions d'application* peuvent (ou non) être énoncées sans prédicat évaluatif. Attribut `charge_valuative ∈ {relationnelle, seuil-valuatif}`, déclaré au schéma de Couche 0 (→ Architecture §2bis) et instruit primitive par primitive au §A.14.7.
- **Suspension de valuation** : acte d'inscription par lequel l'analyste, mobilisant une primitive à seuil en usage descriptif, déclare que **le seuil est importé du modèle et non endossé** dans le contexte d'analyse. Ce n'est ni l'endossement ni l'absence de valuation : c'est sa mise entre parenthèses **tracée**.
- **Statut d'un seuil** : **quintuplet** déclaré **{ source du seuil ; convention de mesure ; régime d'usage (normatif / descriptif-suspendu) ; porteur de la déclaration ; usage de l'agrégat }**. Généralise la règle B4 (`source_valuemetre`, §C-II.2 PR-1) hors de F8. *Le cinquième terme est posé par CONV-9 (§A.14.9).*
- **Usage de l'agrégat** *(cinquième terme)* : ce qu'une somme ou une moyenne sert à établir dans la mobilisation du seuil. Quatre valeurs : **`constatation`** (l'agrégat sert à établir que le seuil est franchi) ; **`au-delà`** (le franchissement est établi cas par cas, l'agrégat n'opère qu'au-dessus du seuil — répartir, budgéter, comparer) ; **`sans agrégat`** (contrôle unité par unité) ; **`non déclaré`** (défaut : **refuse, n'autorise pas**). *Axe orthogonal au régime d'usage : celui-ci dit si le seuil déclenche une règle, celui-là dit si une somme établit son franchissement. Les quatre croisements sont réalisables — `orthogonalite_usage_agregat_regime_usage`, compilé.*
- **Population visée** *(terme facultatif du statut du seuil)* : à qui le seuil s'applique. Il est distinct du **porteur de la déclaration**, qui dit qui le déclare ; leur relation est décidable sur la seule inscription (`porteur_du_seuil_exhibe_sa_population`, PR-18). Trois effets, et seulement trois :
  - terme **absent** : l'écriture est bien formée et marquée `[POPULATION VISÉE NON DÉCLARÉE]` — **E5** ;
  - terme déclaré, **porteur hors de la population visée** : signal `[SEUIL DÉCLARÉ PAR UN TIERS]`, l'écriture reste bien formée — **E5**. Le signal n'interdit pas qu'un tiers déclare (`PR18_n_impose_pas_qui_declare`) et ne juge pas le contenu du seuil (`PR18_ne_juge_pas_le_contenu`) ;
  - terme déclaré, **réfutants admis limités à la population visée** : mal formée, `[RÉFUTATION RÉSERVÉE AUX DÉCLARANTS]` — **E4** (`declarant_seul_refutant_est_mal_formee` ; témoins `PR18_temoin_mal_forme`, `declarer_par_les_concernes_reste_admissible`), transposition de `autorefutation_n_est_pas_refutation` (PR-16). *Horizon du marqueur :* critère de sortie — l'ouverture de la condition de réfutation à au moins un réfutant hors de la population visée, déclarée par le porteur de la déclaration.
  *Ce que le terme ne fait pas.* Il ne prescrit pas que le seuil soit déclaré par les concernés : AX-7 n'établit qu'une possibilité, en tension déclarée avec RSO-6. `[LACUNE]` Il ne dit pas qui délimite la population visée : un porteur peut la délimiter de façon à s'y inclure. `[CONDITION DE RÉFUTATION]` Le terme est mal posé si, sur les cas du corpus où le porteur de la déclaration est documenté (TZCLD, SSA), le signal ne sépare jamais deux inscriptions. *Portée :* les trois effets valent pour les mobilisations inscrites après le 10 octobre 2026 ; ils ne requalifient aucune fiche existante (patron de la portée de CONV-9, §A.14.9).

### §A.14.9 CONV-9 — obligation de déclarer l'usage de l'agrégat

> **CONV-9.** Toute mobilisation d'une primitive `seuil-valuatif` déclare, au cinquième terme du statut du seuil, **ce que l'agrégat sert à établir**. La valeur `non déclaré` ne vaut pas déclaration : elle refuse, elle n'autorise pas.

**C'est une convention, non un théorème**, pour la raison qui fonde CONV-1 à CONV-4 : *un champ obligatoire vrai par construction du typage ne se prouve pas, il se déclare.* Ce que la formalisation apporte n'est pas l'obligation mais ce qui la **motive** et ce qui la **borne** — six théorèmes compilés dans `ProfReg/PR10_StatutSeuil.lean` §7.

**Le trou est démontré, non postulé.** `BienFormee_ne_borne_pas_le_quintuplet` exhibe une mobilisation `seuil-valuatif` **parfaitement bien formée** au sens de R0-bis — statut présent, quatre termes renseignés — dont le cinquième n'est pas déclaré. CONV-9 ferme ce trou, et son existence est un résultat, non une intuition. *(Même figure que `PR14_ne_borne_pas_l_attribution` pour ACT-ARCH-001.)*

**L'ancrage.** André, M. et Gosseries, A., *La Justice climatique*, PUF, coll. « Que sais-je ? », 2024, ch. I §II : l'approche par les droits humains fondamentaux « rejette l'agrégation des intérêts qui prévaut dans l'analyse coût-bénéfice », **et** « n'empêche pas, une fois le seuil de dignité atteint pour tous, de chercher ensuite à maximiser le bien-être agrégé ou à égaliser les conditions au-delà de ce seuil (Gosseries, 2011) ». \[VÉRIFIÉ sur source primaire\] **L'agrégation est exclue pour constater le franchissement, permise au-dessus.**

**CONV-9 déclare, elle n'interdit pas.** Le MRC n'arbitre pas entre les théories de la justice : il oblige à déclarer laquelle s'applique (NT-G2 §7). La source ne couvre que le cas suffisantiste ; étendre l'**interdiction** à tout principe intergénérationnel serait un `[ENGAGEMENT SANS SYMÉTRIE]` — emprunter l'autorité d'une source pour un énoncé plus large qu'elle. Étendre la **déclaration** est un choix de forme, assumé comme tel. `constatation_reste_licite` (compilé) inscrit cette limite : une mobilisation qui déclare établir le franchissement par agrégat est bien formée.

**Ce que CONV-9 ne fait pas.** Elle ne dit pas si le seuil est bon — elle dit comment on établit qu'il est franchi (`le_cinquieme_terme_ne_touche_pas_au_seuil`). Elle ne classe pas : deux mobilisations différant sur le seul cinquième terme sont l'une et l'autre bien formées (`PR10_ne_juge_pas_l_usage_de_l_agregat`).

**À ne pas confondre avec PR-19.** PR-19 (`serie_bien_formee_agregat_non_conforme`, compilé) porte sur l'addition d'**écritures dans une série** : chacune conforme, la série non conforme. Le cinquième terme porte sur l'agrégation de **dimensions à un instant** — un stock contre un autre, une personne contre une autre. **Aucun des deux ne couvre l'autre**, et les confondre serait un `[CHANGEMENT DE BASE NON TRACÉ]`.

`[CONDITION DE RÉFUTATION]` CONV-9 tombe si l'on montre que la question « par agrégat ou cas par cas ? » ne se pose pas hors du cas suffisantiste — c'est-à-dire si les cas non suffisantistes qui la motivent (soutenabilité forte, exhaustivité territoriale, seuil de température) se ramènent tous à un principe déclaré. **Ils n'y sont pas ramenés à ce jour, et c'est ce qui justifie la forme universelle de la déclaration.**

`[PORTÉE DÉCLARÉE — Couche 2]` CONV-9 s'applique aux inscriptions **postérieures au 8 septembre 2026**. Elle **n'invalide aucune fiche existante** : le registre opérationnel (`Registre_Soin_Ecologisation`, 1 069 fiches) ne porte pas ce champ, et le lui appliquer rétroactivement reviendrait à faire acquérir silencieusement une déclaration que personne n'a faite — exactement ce que le refus d'une valeur par défaut évite du côté formel. **La reprise du registre est une décision distincte, non prise ici** (voir §D des lacunes).

### §A.14.10 CONV-10 — ce que `plein` désigne dans un registre comptable augmenté

> **CONV-10.** Dans toute instance du registre comptable augmenté L2 (`RegistreComptableAugmente`), la valeur désignée `plein` d'un registre signifie **que le registre reconnaît le lien**, et **jamais qu'il le valorise**. Un registre qui reconnaît une obligation sans savoir la chiffrer est à son point plein.

**Pourquoi c'est une convention et non un théorème.** Même raison que CONV-1 à CONV-4 : *un énoncé sur l'interprétation d'un paramètre ne se prouve pas, il se déclare.* `pleinFin` et `pleinCom` sont des **champs de l'instance**, pas de la théorie ; rien dans les types n'impose que deux instances les lisent pareillement.

**Ce que la formalisation apporte, et qui rend la convention non arbitraire.** Trois faits établis sur `LotL2_PR2_PR14.lean` :

1. `CompatibleExtension {V : Type} (plein : V) … : ∀ a b, p1 a b = plein ↔ p0 a b = true` — `V` est un **type quelconque**, `plein` un **élément désigné**. Rien n'y est un montant.
2. **Aucune arithmétique n'apparaît dans L2** : pas d'addition, pas d'ordre, pas de zéro. **Un registre ne peut pas valoriser dans le vocabulaire de L2.**
3. Le témoin de `registre_augmente_non_equivalence` est une `RegistreComptableAugmente Bool Nat` : le registre **financier** y porte des booléens, celui de communalité des entiers. **Le set a lui-même écrit un témoin qui échange les rôles intuitifs.**

**Contrôle des instances.** Trois instanciations de `RegistreComptableAugmente` dans le set, **toutes en lecture « drapeau de présence »** : `registreAugmenteDe` et `registreAugmenteBis` (PR-20, `pleinFin := 1`) et le témoin interne de `registre_augmente_non_equivalence`. **PR-2 et PR-14 n'instancient pas la structure.** Le risque est donc **prospectif, non actuel** — et c'est la raison de le déclarer. *(Contrôle par recherche textuelle sur `RegistreComptableAugmente`, `pleinFin`, `CompatibleExtension` ; une instanciation construite par une voie indirecte y échapperait.)* PR-36 (`versL2`) instancie aussi `RegistreComptableAugmente`.

**Ce que CONV-10 rend possible.** La condition de bonne formation v2 (NT-ARCH §8.5.3bis) pose que **le registre financier n'est pas requis** pour porter un chiffre. Sans CONV-10, cette clause serait suspecte de contredire `registre_augmente_coherent` ; avec elle, la compatibilité est déclarée et vérifiable.

**Ce que CONV-10 ne fait pas.** Elle n'exige aucune harmonisation des évaluations — `les_deux_registres_augmentes_ont_le_meme_socle` (lecture qui n'appuie pas seule), `accord_sur_l_existence_pas_sur_la_valeur`. Elle ne dit pas non plus **quel** registre porte quoi : la clause de nommage de la v2 reste **non certifiable en l'état**, `RegistreComptableAugmente` ayant deux registres câblés et **aucun nom de registre**. `[LACUNE DE COUVERTURE]` Deux issues, non tranchées : (a) lire `pCom` comme « le registre non financier, quel que soit le document qui le porte », et le déclarer ; (b) indexer L2 par une **liste déclarée de registres**, ce qui refond L2 et tout ce qui en dépend. **(a) est recommandé ; (b) est la forme que L2 devra prendre si le nommage doit être opposable.** PR-36 (`RegistreAugmenteTenu`) indexe le registre augmenté par son **teneur** : l'issue (b) est engagée pour le teneur, non pour le nom de registre.

`[CONDITION DE RÉFUTATION]` CONV-10 tombe si une instance légitime de L2 exige que `plein` porte une valorisation — c'est-à-dire si l'on exhibe un usage où la reconnaissance du lien sans chiffre doit être traitée comme absence de lien.

`[PORTÉE DÉCLARÉE — Couche 1]` CONV-10 porte sur l'interprétation d'un paramètre existant. **Elle ne modifie aucun théorème et n'invalide aucune preuve** : les trois instances actuelles la satisfaient déjà.

---

### §A.14.2 Critère de séparabilité

Un descripteur D est **séparable** (usage non-normatif possible) si et seulement si ses conditions d'application peuvent être énoncées **sans prédicat évaluatif**, la valuation entrant alors comme *référence déclarable* et non comme *direction de mal intrinsèque*. Sinon, D est un **concept épais** : description et évaluation non décollables. [Cadrage philosophique : Bernard Williams, *Ethics and the Limits of Philosophy*, 1985 ; Hilary Putnam, *The Collapse of the Fact/Value Dichotomy*, 2002 — thèse **débattue**, déclarée comme telle ; la clause R0-bis n'exige pas de la trancher : elle impose une inscription, pas une métaphysique. Pagination non contrôlée dans cette inscription — `[À VÉRIFIER SUR SOURCE avant diffusion externe]`.]

### §A.14.3 Règle R0-bis — clause de suspension de valuation

> **R0-bis.** Toute mobilisation **descriptive** (non-normative) d'une primitive `seuil-valuatif` exige l'inscription d'une **déclaration de suspension de valuation** : l'analyste déclare que le seuil est *importé du modèle, non endossé* dans le contexte d'analyse, renseigne le **quintuplet** « statut du seuil » (§A.14.1), **cinquième terme compris** et appose le marqueur `[VALUATION SUSPENDUE]`. Aucune règle R-\* n'est alors déclenchée. À défaut : `[CHANGEMENT DE BASE NON TRACÉ — valuation importée sans déclaration de statut]`.

En grammaire DÉBIT/CRÉDIT (lecture de Couche 1, par analogie déclarée — cf. Architecture §3bis, ne pas assimiler à la symétrie comptable R1) : la valuation importée est un **débit** ; la déclaration de non-endossement est le **crédit** qui l'équilibre. R0-bis n'est pas une obligation morale nouvelle : c'est l'extension hors-F8 de la discipline « tout seuil déclare sa source » (B4/PR-1), le statut incluant la valeur *suspendu*. Les primitives `relationnelle` restent d'usage descriptif libre **à condition de déclarer la référence** (déjà exigé par les grammaires).

### §A.14.4 Règle R0-ter — déclaration de situation du concepteur/accompagnateur

> **R0-ter (contre-écriture de cadrage).** Toute mobilisation **accompagnée** du MRC par un chercheur-pilote exige l'inscription d'une **déclaration de situation** : (i) **qui** cadre l'analyse (acteur nommé) ; (ii) **depuis quel corpus/horizon** (déclaré, non neutre) ; (iii) **quels points ont été retenus et lesquels écartés** ; (iv) un marqueur `[CADRAGE REPRENABLE PAR LE COLLECTIF]` sur chaque élément de cadrage. À défaut : `[CHANGEMENT DE BASE NON TRACÉ — cadrage situé importé sans déclaration]`.

Là où R0-bis traite la valuation importée *du modèle*, R0-ter traite la valuation importée *du concepteur* — troisième source de valuation, distincte aussi de la valeur émique de l'acteur enquêté. Le **portage** de la déclaration suit l'axe des trois régimes d'usage (orthogonalité, §A.14.6) : Usage 1, le chercheur seul (R0-ter suffit) ; Usage 2, chercheur-pilote + collectif co-enquêteur (R0-ter **+** procédure de reprise inscrite — protocole §A.8) ; Usage 3, le collectif lui-même (précondition de la bascule v6, hors périmètre du set actuel). `[ENGAGEMENT SANS SYMÉTRIE — déclaré, contrepartie opérationnelle]` : le droit de reprise (iv) n'a de portée que si une procédure effective de contestation existe et est inscrite ; cette contrepartie est le protocole d'expérimentation pilote (§A.8, indicateurs I-1/I-2). R0-ter est **non testée empiriquement** à ce jour : sa séparabilité (le cadrage situé est-il toujours déclarable sans vider l'analyse ?) est une question ouverte instruite par le pilote — `[PLAUSIBLE, NON VÉRIFIÉ]`.

### §A.14.5 Ce que cette clause prolonge — et ne préempte pas

Elle articule deux dispositifs préexistants qui traitaient partiellement le problème : les clauses « diagnostic partiel » des 12 grammaires (elles autorisent l'usage non-doctrinal mais ne disent rien du seuil logé dans la primitive) et la règle B4/PR-1 (elle impose la source d'un seuil, mais en F8 seulement, sans la valeur *suspendu*). Elle fournit le patron de résolution de la réserve « orientation vs obligation » de la futurité (§A.5) **sans la trancher** : la futurité descriptive est admissible sous suspension déclarée ; décider si la futurité *instituée* porte un engagement réfutable propre reste une décision v6 — `[ENGAGEMENT À HORIZON IRRÉVERSIBLE — délibération nécessaire, non préemptée]`. Un candidat de preuve **PR-10 `seuil_valuatif_must_declare_status`** (analogue de PR-1, quantifié sur les primitives `seuil-valuatif`) est versé au programme de preuve reporté v6 (§C-II.2) — `[PLAUSIBLE, NON VÉRIFIÉ — faisabilité Lean non tentée]`.

### §A.14.6 Orthogonalité aux trois régimes d'usage

L'axe *descriptif / normatif* introduit ici porte sur la **charge d'obligation** d'une catégorie ; l'axe Usages 1/2/3 (Architecture §8.1.1) porte sur l'**opposabilité/fiabilité** d'une inscription. Les deux axes se croisent (on peut faire un usage descriptif-suspendu en Usage 2) ; les confondre (« descriptif = Usage 1 ») est un `[CHANGEMENT DE BASE NON TRACÉ]`.

### §A.14.7 Table de typage `charge_valuative` des primitives et champs déclencheurs

Typage **déclaré, non calculé**, établi par examen de la définition d'origine de chaque primitive (jamais de son nom). Les cas mixtes sont marqués et traités, par prudence, comme `seuil-valuatif`. Périmètre : primitives de Couche 0 déclarées + champs déclencheurs des 12 grammaires (extension de périmètre déclarée : c'est dans ces champs que loge la charge valuative).

| Fichier | Primitive / champ | Charge | Justification (procédurale) |
|---|---|---|---|
| Architecture §2 | `regimeobligation`, `fractionactorielle`, `collectifhybridedeclare` | relationnelle | Classification structurelle et score délibéré-déclaré ; aucune direction de mal |
| Architecture §3bis | `asymetrie_existentielle` | relationnelle | Décrit une structure d'écriture (E sans miroir) ; la règle déclenchée (R-INTERDIT-ABSOLU) est normative, pas l'identification |
| Architecture §5.1 | `seuilentreecommunautemorale` | **seuil-valuatif** | Fixe l'entrée dans la communauté morale (SENTIENCE/FINALITEIMMANENTE) : l'appliquer décide de la considérabilité — valuation non décollable |
| NT-G1 | `attracteur_culturel`, `système_cognitif_implique`, `niveau_explication`, `résistance_cognitive_révision`, `praticabilite_cognitive`, `modificateur_affectif` | relationnelle | Typologies descriptives à référentiel déclaré (Tinbergen, Boyer, Henrich) — aucune primitive `seuil-valuatif` dans G1 |
| NT-G2 | primitive Interaction (porteur, horizon, obligation) | relationnelle | Structure de relation, sans prédicat évaluatif |
| NT-G2 | `puissanceaffirmative` (score 0-5) | relationnelle | Mesure graduée à référence déclarée |
| NT-G2 | `seuilpuissanceaffirmative` | **seuil-valuatif** | Pose « en-deçà = perte à protéger » — direction de mal au seuil |
| NT-G2 | `appelimmanent` | `[CHARGE VALUATIVE MIXTE]` → seuil-valuatif | Résistance observable de l'entité **et** finalité jonasienne importée — séparabilité à trancher |
| NT-G2 §6 | taxinomie A4 (RECIPROCITE / SUFFICIENCY / NON_AGGRAVATION) | relationnelle (taxinomie) / **seuil-valuatif** (seuils d'application, not. SUFFICIENCY) | La taxinomie classe ; le seuil de suffisance pose une direction de mal |
| NT-G3 | `defi_caring_about`…`defi_care_receiving`, `type_operation_care`, `charge_emotionnelle_distribuee`, `reconnaissance_charge_emotionnelle`, `soin_avec_milieu` | relationnelle | Rôles (Tronto) et faits d'inscription attestables — aucune primitive `seuil-valuatif` dans G3 |
| NT-G4 | `boucle_confirmante_détectée`, `consentement_explicitation_corpus`, `contestation_possible_corpus`, `légitimité_corpus_tracee`, `solidite_politique` | relationnelle | Structures de boucle et faits procéduraux ; forme du signal de boucle : PR-54 ; `consentement_explicitation_corpus` est **dérivé** des consentements attestés par personne (PR-56, `le_consentement_du_corpus_est_derive`) |
| NT-G4 | `exclusion_performative_détectée` (ex-`exclusion_productive_détectée`, renommé le 12/10/2026 — NT-G4 §3.1bis) | `[CHARGE VALUATIVE MIXTE]` → seuil-valuatif | L'écart périmètre déclaré / êtres rendus visibles est attestable (valeur dérivée, NT-ARCH F3) ; qualifier la part écartée d'« accessoire » importe une critique |
| NT-G5 | `type_milieu_vecu` (versants **topos** et **chôra**), `appel_entendu_milieu` (**énumération à quatre lemmes** ; gardes §A.13, qui ne codent aucune valeur), **`interprete_appel`** (obligatoire), `mode_metabolique_actif`, `soin_avec_milieu` | relationnelle | Fait perceptif rapporté à son interprète, et flux tracés |
| NT-G5 | `seuil_degredation_irréversible` | **seuil-valuatif** | Direction de mal jonasienne posée au seuil |
| NT-G5 | `obligation_preservation` | relationnelle | Citer une obligation inscrite (porteur DID) n'est pas l'endosser — référence déclarable |
| NT-G6 | faisceau des 5 droits (Schlager-Ostrom), **les cinq champs d'axes non agrégés** (`communalite_interet_commun`, `communalite_inclusivite`, `communalite_instance`, `prescription_etat`, `nature_prerogative`), `congruence_règles_local` | relationnelle | Attributions et axes à référentiel déclaré, **non agrégés** |
| NT-G6 | `ecart_formel_réel` (mesure) | relationnelle | Le terme de comparaison (droit formel, C-DROITS) est une référence conventionnelle déclarable — lecture *law in books / law in action* ; un écart et un seuil déclaré par droit, sans alerte hors seuil déclaré (PR-59, `pas_d_alerte_sans_seuil_declare`, `non_instruit_n_est_pas_nul`) |
| NT-G6 §5 | seuil de déclenchement de l'écart (deux cycles) | **seuil-valuatif** | « Dépasser le seuil » importe une direction de mal ; décomposition mesure/seuil recommandée (identifiant distinct : décision porteur en attente) |
| NT-G6 / NT-G7 | `parite_participation` (un seul champ, propriétaire NT-G7, lu par NT-G6 ; ex-`parite_deliberative`) | `[CHARGE VALUATIVE MIXTE]` → seuil-valuatif | Convention de mesure déclarable, mais « parité effective » (Fraser) porte la direction de mal |
| NT-G7 | `capabilité_plancher_menacée` | **seuil-valuatif** | Plancher (liste Nussbaum 2000) + « menacé » = en-deçà-mauvais, non décollable ; test de séparabilité **réussi sous suspension** : suspendue, la primitive décrit encore un état relatif au référentiel nommé |
| NT-G7 | `capabilite_individuelle` | relationnelle | Liste de référence déclarée (Nussbaum) |
| NT-G7 | `habitabilite_systemique` |  | **HABITABILITE\_PRODUCTIVE et INTEGRITE\_ECOSYSTEMIQUE qualifient l'état d'un écosystème : ce sont des candidats `seuil-valuatif`, non des valeurs relationnelles.** Par la règle de prudence de §A.14, un cas mixte est **traité comme `seuil-valuatif`** — ce qui **fait entrer ce champ dans le périmètre de R0-bis**. |
| NT-G7 | `niveau_injustice_épistémique`, `type_injustice` | **seuil-valuatif** | « Injustice » est un concept épais (Fricker, Fraser) : l'identification importe la valuation |
| NT-G7 | `précondition_herméneutique_satisfaite`, `asymétries_intersectionnelles`, `source_asymetrie_pouvoir` | relationnelle | Faits attestables ; discriminant de routage (défaut INDETERMINEE) |
| NT-G7 | `violence_symbolique` | **seuil-valuatif** | Identification bourdieusienne (adhésion intériorisée = violence) — la garde anti-paternalisme de G7 en est déjà la contre-écriture |
| NT-G8 | `médiation_type`, `intensite_rivalite`, `distance_catégorielle`, `voix_victime_inscrite`, `narratif_legitimateur`, `autocritique` | relationnelle | Typologies et faits d'inscription |
| NT-G8 | `focalisation_victimaire`, `meconnaissance_fondatrice` | `[CHARGE VALUATIVE MIXTE]` → seuil-valuatif | Bascule attentionnelle observable, mais « victime » et « méconnaissance » girardiennes présupposent l'arbitraire du sacrifice |
| NT-G9 | `regimeaffectif`, `sourcequalification`, `vitalitediscussionprofessionnelle`, `seuildisposition`, `evenementmesentente` | relationnelle | Régimes qualifiés par source déclarée ; seuils de disposition = descriptifs (pas de direction de mal) |
| NT-G9 | `signalsouffrance` | relationnelle | **Antécédent interne de R0-bis** : G9 déclare déjà « indicateur explicatif, non preuve de légitimité d'une créance » — suspension partielle inscrite |
| NT-G9 | `sphereviolee`, `ideologiedefensivedetectee` | `[CHARGE VALUATIVE MIXTE]` → seuil-valuatif | « Violée », « défensive » (Dejours) : concepts épais de clinique du travail |
| NT-G10 | `risqueepistocratie` (score) et champs de substitution (`absencestructurelle`, `mecanismesubstitution`, `porteurrepresentationabsents`, `reversibilitedecision`, `revuesubstitution`) | relationnelle | Score déclaré et dispositifs procéduraux |
| NT-G10 | seuil de déclenchement (risque ≥ 4, R-EPISTOCRATIE) ; `qualiteenquete` ; `contraintejonasienne` | **seuil-valuatif** (`qualiteenquete` : `[MIXTE]`) | Le déclenchement et la précaution asymétrique portent la direction de mal ; « insuffisante » est évaluatif |
| NT-G11 | **`travail_bien_fait`** | relationnelle **(valuation émique déclarée)** | Cas wébérien : la valuation est portée par le collectif enquêté, intrinsèquement disputable (Clot et al. 2021), **non fixée par le modèle** — l'usage descriptif commute sans clause, à condition de déclarer que le juge est le collectif |
| NT-G11 | `collectif_comme_juge`, `type_fragilite`, `profondeur_justice` | relationnelle | Désignation du juge et typologies |
| NT-G12 / F8 | valorimètres et seuils comptables | **seuil-valuatif par construction, déjà gouverné** | B4/PR-1 impose la source déclarée ; R0-bis ajoute la valeur *suspendu* au statut — « un prix est une décision tracée » |
| §A.11 | `marquagemonetaire` (candidat) | relationnelle | Descriptif de circuit (niveau méso déclaré obligatoire) |

**Lecture d'ensemble.** Environ un cinquième des primitives/champs porte une charge `seuil-valuatif` avérée ; sept cas sont (traités `seuil-valuatif` par prudence) ; le reste est `relationnelle` sous condition de déclaration de référence. Deux enseignements : G9 contenait déjà une suspension partielle (`signalsouffrance`), et `travail_bien_fait` exhibe un **troisième cas de figure** (valuation émique portée par l'enquêté) qui ne relève ni de la suspension ni de l'endossement — le typage binaire est donc **suffisant mais à surveiller** : si d'autres primitives émiques apparaissent, une troisième valeur (`émique-déclarée`) devra être délibérée.

### §A.14.8 Conditions de réfutation

(1) **De la clause** : R0-bis tombe si l'on exhibe une primitive `seuil-valuatif` dont la suspension la vide de tout contenu descriptif (le descripteur disparaît avec la norme) — cette primitive ne serait alors employable qu'en régime normatif. Test conduit sur `capabilité_plancher_menacée` : **réussi** (§A.14.7) ; à conduire sur chaque `[MIXTE]` au moment de trancher. (2) **Du typage** : chaque ligne du §A.14.7 est révisable par examen contradictoire de la définition d'origine ; un typage contesté se tranche par délibération du porteur, non par le nom de la primitive. (3) **Critère de vérification d'usage** : tout usage descriptif d'une primitive `seuil-valuatif` dans le corpus doit porter `[VALUATION SUSPENDUE]` + quadruplet ; contrôle par la part renseignée (indicateur I-4, §A.8).

\[LACUNES ET LIMITES — §A.14\] (1) Typage instruit sur les tables de champs des notes techniques, non sur une relecture intégrale des définitions longues : les sept `[MIXTE]` et tout champ absent des tables restent à instruire. (2) La frontière relationnelle/seuil-valuatif repose sur la thèse (débattue) des concepts épais ; le typage d'une primitive litigieuse peut être contesté sans invalider la clause. (3) R0-ter non testée empiriquement (→ protocole §A.8). (4) PR-10 est une conjecture de faisabilité, non une preuve. (5) La tenue de la suspension **sans garantie du pilote** (Usage 3) est une question v6, documentée — non tranchée — par le pilote.

---

## §A.15 Table canonique des conventions inscrites

> **Décision du porteur : le set est le lieu canonique de la série des conventions.** Cette table fait foi. Les notes de travail (`ProfReg/Conventions_et_sanctions_2026-09-07.md`, le graphe de dépendances §2sexies/§2septies, les rapports d'audit) sont le **dossier d'instruction** de chaque convention, non le lieu de son inscription.

> **Ce qui rend une convention opposable n'est pas une convention.** L'énoncé « déclarer confère l'opposabilité » gouverne **toutes les conventions de §A.15.1** ; il est inscrit comme **RSO-1**, première des **règles de second ordre** — quatrième classe de nœuds du set, **§A.16**. La circularité que cela expose (RSO-1 se fonde elle-même) y est déclarée plutôt que résolue : voir §A.16.6.

**Ce qu'est une convention dans le set.** Un énoncé **opposable et non démontrable** : soit vrai par construction du typage (et donc creux comme théorème), soit portant sur l'**interprétation** d'un paramètre ou d'une architecture, que le calcul ne décide pas. La règle qui les gouverne est celle de §8sexies de NT-ARCH : *déclarer ce qui ne se calcule pas, calculer ce qui se calcule.* Les conventions entrent au graphe de dépendances comme **classe de nœuds distincte** — ni prouvées, ni à prouver, **opposables au même titre** que les théorèmes.

**Statut « Institution »** : une convention qui **désigne un tiers** ou **règle ce qui sort du registre** vers un tiers (CONV-16, 17, 18). Elle n'est ni vraie par construction du typage, ni une interprétation ; elle **organise une relation entre registres, ou entre un registre et l'extérieur**. Elle reste une convention, parce qu'elle oblige des inscriptions (désignation arrêtée, attestation, annotation) ; elle ne confère pas de statut à un acte du modèle, ce qui la distingue d'une RSO (§A.16.2). `[CHANGEMENT DE BASE TRACÉ — la définition d'une convention ci-dessus (typage ou interprétation) ne couvre pas ce statut, défini ici]`

### §A.15.0 Table canonique des axiomes — AX-1 à AX-17

*Placée en tête de §A.15 parce que les axiomes précèdent les conventions. Chaque énoncé est **repris verbatim de sa fiche** (référence et ligne), **non réécrit** ; les cas non tranchés portent leur marqueur. Elle fait foi pour l'identité des axiomes.*

**Familles** *(1 et 2 dans l'ordre de `Fiches_Axiomes_A11_A12_A13_2026-09-11.md` l.14)* : **1** anthropologique · **2** institutionnelle · **3** constat historique daté · **4** constat sur l'état d'un corpus théorique · **5** cadre importé · **6** postulat de structure.

**Doctrine de la famille 3** : un constat daté porte **une condition de péremption** — il cesse d'être vrai — **et peut porter une condition de réfutation** — il n'était pas vrai à sa date. AX-7 porte les deux. **AX-15, AX-16 et AX-17 portent les deux** : énoncés datés, péremption et réfutation séparées.

**Porteur / horizon / critère** : porteur **P. Musseau** pour les dix-sept, tous au graphe ; horizons déclarés : AX-7 (dates et péremption), AX-14 (v6). **Triplets de tous les axiomes : table ci-dessous.**

**Triplets porteur / horizon / critère** *Base : la proposition par famille (`ProfReg/Instruction_Suites_Audit_Axiomes_Conventions_RSO_2026-09-28.md` §1.4), précisée axiome par axiome à partir de la condition de chaque fiche. **Porteur : P. Musseau, porteur MRC, pour les dix-sept, tous au graphe.***

**Deux règles communes.**
- **Règle de provenance.** Le cas qui éprouve une condition n'est **ni celui dont l'axiome est tiré, ni celui qui a servi à calibrer la condition**. Un cas de calibrage confirme la rédaction, il n'éprouve pas l'axiome. `[RAISONNEMENT AUTORÉFÉRENTIEL évité]`
- **Critère satisfait** quand l'issue de la confrontation est **inscrite** (au registre `_ETAT` et dans la fiche) : *tombe*, *ne tombe pas*, ou *non décidable sur ce cas* avec la raison. Un critère satisfait ne dit pas que l'axiome est vrai.

| # | Famille | Horizon | Critère de vérification | Cas | État |
|---|---|---|---|---|---|
| **AX-1** | 1 | **v6** | la condition est confrontée à un cas de provenance distincte de Stepanoff **et** de Pruvost 2024 | à désigner | Pruvost 2024 a servi à **calibrer** la condition : il ne compte pas comme épreuve |
| **AX-2** | 2 | **v6** | la condition est confrontée à un dispositif d'inscription **ne connaissant que des créances exigibles**, du corpus | **proposé : registre RATP 2025 (IFRS, jalons J1)** — chercher une obligation envers un processus non maîtrisé portée durablement sans conversion ni déclaration d'acquittement | non engagé |
| **AX-3** | 2 | **v6** | la condition est confrontée à **deux cas comparés** : un où décideur et répartiteur sont séparés, un où ils ne le sont pas — pour établir ou non une différence observable | **proposé : avarie commune** (`ProfReg/Avarie_commune_A2_P6prime_2026-09-07.md`) pour le premier ; le second à désigner | non engagé ; l'avarie commune est la **source** d'AX-3 : elle ne suffit pas seule (règle de provenance) |
| **AX-4** | 2 | **v6** | la condition (« il suffirait d'un cas ») est confrontée à un dispositif nommé où la **visibilité** d'une atteinte est établie : sont-elles aussi opposables et reprenables par les affectés ? | **proposé : un terrain K3** (Annexe K ; CLE Drôme, PLE Niayes ou OLGE Lac Togo) | non engagé |
| **AX-5** | 2 | **v6** | la condition (« un seul cas suffirait ») est confrontée à un dispositif nommé : l'inscription d'une atteinte y produit-elle, **sans montage**, débiteur, ressource, action et vérification ? | **proposé : le même terrain K3** qu'AX-4 — les deux conditions s'éprouvent sur un même relevé | non engagé — « la condition la plus facile à tester du set » |
| **AX-6** | 4 | **clôture de l'étape 2 du protocole** | la recherche d'une **dérivation** de la métrique chez un suffisantiste est conduite sur les objecteurs hors corpus | **Casal 2007** d'abord (fiche l.135), puis Crisp, Arneson | non engagé ; étape 2 non close |
| **AX-9** | 1 | **v6** | la condition empirique est confrontée à **une institution durable** hors du corpus romain et florentin (Machiavel) | à désigner | non engagé — « le corpus déposé ne la teste pas » |
| **AX-10** | 1 | **v6** | *préalable* : la pièce `L1_repris_Campo` est convertie en **fiche au gabarit** ; puis la condition est confrontée à une infrastructure de mesure nommée *(pour un même collectif, sous deux dispositifs ; provenance : hors économie numérique de l'attention)* | à désigner |  **préalable rempli sous réserve** : fiche `ProfReg/Fiche_Axiome_A10_Selectivite_Situee_Attention_2026-09-30.md`  |
| **AX-11** | 6 | **v6** | *(i)* la requalification « isomorphe » / « homologue de forme » est **tranchée** : **« homologue de forme » (T1-T3)** ; *(ii)* le **tableau des traits** T1-T3 est soumis à au moins un lecteur, qui confirme ou réfute chaque case ; l'issue est inscrite | lecteur à désigner | *(i)* **satisfait** ; *(ii)* non engagé |
| **AX-12** | 5 | **v6** | la condition est confrontée à un dispositif collectif nommé où une règle délibérée **contraire à un attracteur identifié** a été adoptée | à désigner | non engagé |
| **AX-13** | 5 | **v6** | *préalable* : la fiche est **reprise** sur la forme requalifiée (NT-G8 §2.1) ; puis la **condition de pertinence** est confrontée à un corpus d'au moins **deux crises nommées**, dont une documentée par des intérêts divergents, lu par **deux lecteurs indépendants** ; corpus hors Girard (provenance)  | à désigner |  **préalable rempli** ; épreuve non engagée |
| AX-7 | 3 | *déjà déclaré* : péremption (les deux dispositifs cessent) et réfutation (pièces) | examen des pièces détenues (`TZCLD/`, `RADIS/`) | TZCLD ; Comité citoyen de Roubaix |   **Roubaix : condition confrontée — ne tombe pas à sa date, sous réserves** ;  **épreuve indépendante** (porteur non rédacteur ; charte signée le 18/06/2026) ; TZCLD non relu |
| **AX-8**  | 5 | **v6** | chaque clause est confrontée à un cas nommé ; issue inscrite | **(2)** proposé : LFDE (TZCLD), registre CARE « capitaux humains » 2025 `[CHOIX DE L'INSTRUCTEUR]` ; **(1)** à désigner — **LFDE exclu** (calibrage de PR-39, qui formalise la clause 1 : règle de provenance) | non engagé |
| AX-14 | 5 | *déjà déclaré* : **v6** | condition confrontée à un cas nommé ; gabarit contradictoire complété par au moins un objecteur lu | — | fiche établie |
| AX-15  | 3 | **v6** | *(i)* le fondement réglementaire de l'obligation de rapprochement est lu (PCG, normes d'exercice professionnel) ; *(ii)* la cohérence avec la réconciliation des comptes réciproques intragroupe est vérifiée — **fait** : `ProfReg/Verification_D-ED-10_A15_x_Reciproques_Intragroupe_2026-09-30.md` (non réfuté ; finalité inverse ; PR-38) | réconciliation intragroupe — IFRS 10 §B86(c), ANC 2020-01 art. 221-2, ISA 505 §6 et §14 (lus ; art. 251-1 non lu) | *(ii)* **engagé et satisfait** ; *(i)* **satisfait**  : fondement **indirect** — obligation d'inventaire et de justification des postes du bilan (C. com. L.123-12 ; PCG art. 1021-3, 1ᵉʳ janvier 2026) ; aucun texte ne nomme l'état de rapprochement ; le manuel (2018, ch. 40 §4) ne cite aucun texte ; **épreuve de N2 désignée : LFDE (TZCLD), registre CARE capitaux humains 2025, miroir tenu par le collectif des salariés**  |
| AX-16  | 3 | **v6** | *(i)* la norme d'exercice professionnel française (NEP 505) est lue ; *(ii)* au moins un objecteur (fiabilité des confirmations, indépendance de l'auditeur) est lu ; *(iii)* une instance de contrôle commune (CONV-16) est éprouvée sur un cas nommé |  **désigné pour (iii) : LFDE (TZCLD), registre CARE capitaux humains 2025, instance commune LFDE / collectif des salariés**  `[CHOIX DE L'INSTRUCTEUR — révisable]` | non engagé |
| AX-17  | 3 | **v6** | *(i)* les Principes directeurs des Nations unies (2011) et le Guide OCDE sur le devoir de diligence (2018) sont lus ; *(ii)* au moins un objecteur (la tripartition comme échappatoire ; pratiques d'achat comme contribution) est lu ; *(iii)* une qualification du lien par une instance commune (CONV-18) est éprouvée sur un cas nommé | registre de chaîne (modèle : Accord Bangladesh 2013) — à désigner | non engagé |

`[CAS PROPOSÉS PAR L'INSTRUCTEUR]` Les cas marqués « proposé » (AX-2, AX-3, AX-4, AX-5) sont des **choix d'instruction**, révisables par le porteur ; ils sont pris dans le corpus existant. Les cas « à désigner » sont une **obligation ouverte** : *porteur* P. Musseau ; *horizon* v6 ; *critère* le cas est nommé dans la présente table.

`[ENGAGEMENT À HORIZON — non irréversible]` L'horizon v6 est une échéance de version : il n'engage rien d'irréversible ; un axiome dont le critère n'est pas satisfait à v6 garde son statut, **marqué `[CRITÈRE NON SATISFAIT À L'HORIZON]`** — marqueur, non retrait (patron des marqueurs E4, horizon caduc : l'axiome reste, il ne peut plus être présenté comme éprouvé).

| # | Intitulé | Famille | Statut | Condition | Fiche |
| --- | --- | --- | --- | --- | --- |
| **AX-1** | Liens multifibres / étalés (v2) | 1 — anthropologique | `valable sous conditions déclarées`, daté, réversible | réfutation | `ProfReg/Fiche_Axiome_A1_v2_Stepanoff_2026-09-07.md` |
| **AX-2** | Dette non soldable | 2 — institutionnelle | `valable sous conditions déclarées` | réfutation | `ProfReg/Fiche_Axiome_A2_Dette_2026-09-07.md` |
| **AX-3** | Découplage du sauvetage et de la répartition | 2 — institutionnelle | `valable sous conditions déclarées` — quatre conditions | réfutation |  `ProfReg/Fiche_Axiome_A3_Decouplage_2026-09-07.md` *(versée au set : §A.18)*  |
| **AX-4** | Mobilisabilité | 2 — institutionnelle | `valable sous conditions déclarées` — corpus Partie I | réfutation | `ProfReg/Fiche_Axiome_A4_Mobilisabilite_2026-09-08.md` |
| **AX-5** | Non-fermeture des chaînes | 2 — institutionnelle | `valable sous conditions déclarées` | réfutation | `ProfReg/Fiche_Axiome_A5_Non_Fermeture_2026-09-08.md` |
| **AX-6** | La doctrine du seuil ne fixe pas sa métrique | 4 — constat sur l'état d'un corpus théorique | `historiquement situé`, corpus nommé (1987-2024) | réfutation | `Fiche_Axiome_A6_Metrique_2026-09-08.md` |
| **AX-7** | Seuil arrêté par les concernés | 3 — constat historique daté | `posé — constat daté`, dossier de preuve **constitué** (pièces détenues), lecture partielle | péremption + réfutation | `ProfReg/Fiche_Axiome_A7_Seuil_Arrete_Par_Les_Concernes_2026-09-11.md` |
| **AX-8**  | **Attention de soin : réception et indifférence organisée** (Garrau 2014 ; Tronto, Molinier via Garrau) | 5 — cadre importé (éthiques du care) | `valable sous conditions déclarées` — transposition aux milieux déclarée (réception par un interprète) | réfutation (deux clauses) | `ProfReg/Fiche_Axiome_A8_Attention_de_Soin_Indifference_Organisee_2026-09-30.md` |
| **AX-9** | Conflit et permanence | 1 — anthropologique | `historiquement situé, avec transposition déclarée` | réfutation | `ProfReg/Fiche_Axiome_A9_Conflit_et_Permanence_2026-09-08.md` |
| **AX-10** | Sélectivité située de l'attention (Campo  **2020, 2026**)  | 1 — anthropologique *(famille à relire : fiche AX-10)* | `valable sous conditions déclarées` (transposition aux infrastructures déclarée) | réfutation |  `ProfReg/Fiche_Axiome_A10_Selectivite_Situee_Attention_2026-09-30.md`  *(pièce d'origine : `L1_repris_Campo_2026-09-07.md` §7)* |
| **AX-11** |  **Homologie de forme de trois obligations**  | 6 — postulat de structure |  `valable comme homologie de forme déclarée (T1-T3)` ; T3 absent de la forme comptable ordinaire | réfutation | `Fiches_Axiomes_A11_A12_A13_2026-09-11.md` |
| **AX-12** | Attracteurs cognitifs | 5 — cadre importé | `valable sous conditions déclarées` | réfutation | `Fiches_Axiomes_A11_A12_A13_2026-09-11.md` |
| **AX-13** | Lecture mimétique | 5 — cadre importé | `valable comme grille d'interprétation ; non établi comme cadre causal` — condition de pertinence  |  **pertinence** (tient lieu de réfutation pour une grille) | `Fiches_Axiomes_A11_A12_A13_2026-09-11.md` |
| **AX-14** | L'objectivité tient à la critique transformatrice (Longino 1990) | 5 — cadre importé | `valable sous conditions déclarées` — transposition déclarée | réfutation | `ProfReg/Fiche_Axiome_A14_Longino_Objectivite_Sociale_2026-09-28.md` |
| **AX-15**  | Rapprochement banque / client | 3 — constat historique daté | `valable sous conditions déclarées` — la forme est attestée ; sa transposition hors de la relation monétaire exigible est conditionnée |  péremption + réfutation  | `ProfReg/Fiche_Axiome_A15_Rapprochement_Bancaire_2026-09-29.md` |
| **AX-16**  | L'écart est investigué par un tiers (ISA 505) | 3 — constat historique daté | `valable sous conditions déclarées` — transposition aux registres de communalité conditionnée à l'institution d'un tiers (CONV-16) |  péremption + réfutation  | `ProfReg/Fiche_Axiome_A16_Confirmation_Externe_ISA505_2026-09-30.md` |
| **AX-17**  | La responsabilité n'est pas transférée par la relation d'affaires (OCDE 2023 ; CS3D art. 10 §1) | 3 — constat historique daté | `valable sous conditions déclarées` — usage conditionné à la qualification du lien par une instance (CONV-18) |  péremption + réfutation  | `ProfReg/Fiche_Axiome_A17_Responsabilite_Non_Transferee_OCDE_2026-09-30.md` |

**Énoncés (colonne A, verbatim) et conditions.**

**AX-1 — Liens multifibres / étalés (v2)** *(`ProfReg/Fiche_Axiome_A1_v2_Stepanoff_2026-09-07.md`, l.80)*

> **AX-1.** Les collectifs humains entretiennent avec leur milieu nourricier des liens qui peuvent être **multifibres** — métaboliques, techniques, cognitifs, affectifs et rituels tenus ensemble sur un même territoire — ou **étalés** — l'approvisionnement métabolique provenant de territoires distants que le collectif ne fréquente pas, tandis que les liens affectifs et cognitifs subsistants portent sur un milieu immédiat dont il ne dépend pas matériellement.
>
> Le passage des premiers aux seconds **n'est pas un effet d'échelle ni d'une limite cognitive** : il résulte d'opérations de spécialisation et de monopolisation des liens, historiquement documentées. Il produit une situation où **les dépendances matérielles d'un collectif échappent à ses liens de connaissance et de soin** — et où les dettes envers le milieu se convertissent en dettes envers des institutions humaines, ou sont déclarées acquittées.

*Condition* *(`ProfReg/Fiche_Axiome_A1_v2_Stepanoff_2026-09-07.md`, l.86)* :

> **Condition de réfutation** : AX-1 tombe si l'on documente un collectif dont une part significative des dépendances matérielles provient de territoires qu'il ne fréquente pas, et qui exerce sur ces dépendances-là non seulement une connaissance, mais un soin — une action effective sur leurs conditions de renouvellement — comparable à celui qu'il exerce sur ses dépendances locales. **Ne le réfutent pas** : (i) la re-densification d'un réseau, qui confirme la réversibilité déclarée ; (ii) la seule connaissance, même chiffrée, de dépendances lointaines ; (iii) l'existence d'inscriptions, qui relève de L1. *Examen sur Pruvost, La Subsistance au quotidien, 2024, p. 424-484 : `Instruction_D-11_…_2026-09-28.md`, annexe.* `[LACUNE DÉCLARÉE — ni « part significative » ni « comparable » n'ont de métrique]`

**AX-2 — Dette non soldable** *(`ProfReg/Fiche_Axiome_A2_Dette_2026-09-07.md`, l.170)*

> **AX-2.** Les collectifs humains dépendent de processus qu'ils n'ont pas créés et qu'ils ne maîtrisent pas. Cette dépendance engendre des obligations qui présentent trois traits : elles sont **héritées collectivement** et non contractées par les individus présents ; elles se **renouvellent à chaque cycle** au lieu de s'amortir ; et elles ne peuvent être **soldées par aucun transfert**, faute d'un créancier apte à en donner quittance.
>
> Toute société les traite d'une manière ou d'une autre. Les dispositifs d'inscription qui ne savent écrire que des créances exigibles ne peuvent pas les porter : ils les convertissent en dettes envers des institutions humaines — donc soldables — ou les déclarent acquittées. **Dans les deux cas l'obligation n'est pas éteinte : elle sort du registre.**

*Condition de réfutation* *(annexe C de l'audit §3.2)* :

> AX-2 tombe si l'on documente un dispositif d'inscription ne connaissant que des créances exigibles qui porte durablement une obligation envers un processus non maîtrisé, sans la convertir en dette envers une institution humaine ni la déclarer acquittée ; ou une telle obligation effectivement soldée par transfert avec quittance d'un créancier apte.

**AX-3 — Découplage du sauvetage et de la répartition** *(`MRC_v5.7/MRC_v5.7_Annexe_Methodologique.md`, §A.18.1 — **fait foi** ; identique à la colonne A de `ProfReg/Fiche_Axiome_A3_Decouplage_2026-09-07.md`)*

> **AX-3 — Découplage du sauvetage et de la répartition.** Lorsqu'un collectif fait face à un péril qui menace l'ensemble de ce qu'il a à préserver, la décision de l'action de sauvetage et la règle de répartition de sa charge **peuvent être séparées** : confiées à deux acteurs distincts, la seconde posée *a priori* et indépendamment de la première.
>
> Là où cette séparation n'est pas opérée, l'instrument qui détermine l'effort détermine simultanément sa répartition, et l'action collective se bloque sur l'arbitrage entre efficacité et équité.

*Condition* *(`MRC_v5.7/MRC_v5.7_Annexe_Methodologique.md`, §A.18)* :

> **AX-3 tombe si**, sur les cas étudiés, la séparation du décideur et du répartiteur ne produit **aucune différence observable** sur les décisions prises, les contributions versées ou l'acceptabilité de l'action. Elle serait alors une distinction sans effet.

**AX-4 — Mobilisabilité** *(`ProfReg/Fiche_Axiome_A4_Mobilisabilite_2026-09-08.md`, l.31)*

> **AX-4.** Dans les dispositifs étudiés, **rendre une atteinte visible ne suffit pas à la rendre mobilisable**. Une information inscrite peut être seulement *visible*, ou *effectivement convocable*, ou *opposable à un porteur*, ou *reprise par une procédure permettant de contester* — et ces quatre états ne s'impliquent pas l'un l'autre. La distribution de l'action entre acteurs, instruments et milieux **n'implique pas** une distribution symétrique des capacités de définir, paramétrer, interpréter, contester ou réviser le dispositif.

*Condition* *(`ProfReg/Fiche_Axiome_A4_Mobilisabilite_2026-09-08.md`, l.94)* :

> **AX-4 tombe si l'on documente un dispositif où la visibilité d'une atteinte suffit, par elle-même, à la rendre opposable et reprenable par les affectés** — c'est-à-dire où les quatre états coïncident. Il suffirait d'un cas.

**AX-5 — Non-fermeture des chaînes** *(`ProfReg/Fiche_Axiome_A5_Non_Fermeture_2026-09-08.md`, l.24)*

> **AX-5.** Les chaînes reliant une **atteinte**, son **inscription**, l'**obligation** correspondante, les **ressources** disponibles, l'**action de soin** et sa **vérification** demeurent **disjointes** tant qu'un montage spécifique ne les relie pas. Une représentation de la dégradation ne produit pas mécaniquement une obligation ; une obligation déclarée ne produit pas mécaniquement les moyens de l'exécuter ; un financement ne produit pas mécaniquement une action vérifiée.

*Condition* *(`ProfReg/Fiche_Axiome_A5_Non_Fermeture_2026-09-08.md`, l.87)* :

> **AX-5 tombe si l'on documente un dispositif où l'inscription d'une atteinte produit, sans montage supplémentaire, la désignation d'un débiteur, l'affectation d'une ressource, l'action et sa vérification.** Un seul cas suffirait. **C'est la condition la plus facile à tester du set** — et personne ne l'a testée.

**AX-6 — La doctrine du seuil ne fixe pas sa métrique** *(`Fiche_Axiome_A6_Metrique_2026-09-08.md`, l.28)*

> **AX-6.** Le suffisantisme pose un **seuil absolu** — la satisfaction d'un niveau minimum — et **laisse sa métrique indéterminée**. Chez ses défenseurs comme chez ses critiques, la métrique (bien-être, besoins de base, capabilités, ressources) est traitée comme une **variable libre de la famille**, non comme une conséquence de la doctrine. Le choix de métrique change ce que le seuil exige ; aucun argument de la doctrine ne le fait.

*Condition* *(`Fiche_Axiome_A6_Metrique_2026-09-08.md`, l.135)* :

> **AX-6 tombe si l'on exhibe, chez un suffisantiste, une *dérivation* de la métrique** — un argument établissant *quelle* métrique le seuil doit prendre, et non un choix déclaré parmi plusieurs.

**AX-7 — Seuil arrêté par les concernés** *(`ProfReg/Fiche_Axiome_A7_Seuil_Arrete_Par_Les_Concernes_2026-09-11.md`, l.40)*

> **AX-7.** Il existe des dispositifs — français, contemporains, portant chacun sur une dimension de la suffisance — où **les critères qui qualifient le seuil ** **sont arrêtés par une instance ouverte aux concernés et composée d'eux** — les personnes auxquelles ce seuil s'applique —, et non par une administration extérieure. *La charte de Roubaix montre que « révocable » ne convient pas à une instance de participation directe.*
>
> Deux cas : **TZCLD** (droit à l'emploi ; critères de qualité du travail) et les **caisses communes de l'alimentation / SSA** (droit à l'alimentation ; sept critères de qualité arrêtés par le Comité Citoyen de Roubaix).

*Condition* *(`ProfReg/Fiche_Axiome_A7_Seuil_Arrete_Par_Les_Concernes_2026-09-11.md`, l.105)* :

> **AX-7 tombe le jour où les deux dispositifs cessent de fonctionner ainsi**, c'est-à-dire où les critères y sont arrêtés ailleurs que par les concernés. **Le processus est documenté comme déjà engagé sur TZCLD** (objection *a*).

**Réfutation.** AX-7 tombe si l'examen des pièces montre, **pour chacun des deux dispositifs**, que les critères n'y étaient pas arrêtés par les concernés : **(i)** qu'ils étaient arrêtés — et non seulement proposés — par une instance où les concernés ne décident pas, ou que la décision des concernés était soumise à la validation d'une telle instance ; **ou (ii)**, lorsque l'instance est **représentative**, que son mandat n'était pas révocable par les concernés. Une **instance de participation directe**, ouverte aux concernés et composée d'eux, satisfait AX-7 : la révocabilité n'y a pas d'objet. Si un seul des deux dispositifs échoue, AX-7 ne tombe pas ; il perd un cas, et cela se déclare. **Péremption, précisée pour Roubaix** : AX-7 périme pour ce cas si, dans l'organisation annoncée, la Commission produits ou le Comité de gouvernance viennent à arrêter ou valider les critères que le Comité citoyen définit, ou si le conventionnement s'écarte des critères sans que le Comité en décide ; horizon d'observation : fin de validité de la charte (un an après signature).

**Épreuve sur Roubaix** (`ProfReg/Examen_A7_Charte_Roubaix_2026-09-28.md`) : une condition formulée en termes de mandat est **mal posée** pour ce cas — le Comité citoyen n'a pas de mandat parce qu'il n'est pas représentatif. **AX-7 ne tombe pas sur ce cas, à la date de la pièce** (charte en projet, juin 2026) : sept critères et tarifs définis par le Comité citoyen, composé d'habitant·e·s, ouvert, sans instance de validation. **Réserves** : pièce non signée ; concernés = participants (les exclus sont déplacés vers l'essaimage) ; l'objection de délégation devient une objection d'**auto-sélection** ; cadrage du parcours en amont ; péremption annoncée par l'organisation « Demain ». **Réfutation alignée sur l'énoncé** : AX-7 tombe si, pour chacun des deux dispositifs, les critères y étaient arrêtés — ou validés — par une instance **qui n'était pas ouverte aux concernés, ou pas composée d'eux**. La branche (ii) (mandat révocable) **perd son objet** : une instance représentative fermée ne satisfait pas l'énoncé, qu'elle soit révocable ou non. `[CONSÉQUENCE TIRÉE PAR L'INSTRUCTEUR — révisable]` **Provenance** : le porteur déclare n'avoir pas pris part à la rédaction de la charte ; l'examen de Roubaix vaut **épreuve indépendante**. **Signature** : la charte a été signée le 18 juin 2026 (déclaration du porteur ; la pièce lue est la version projet, la version signée n'est pas au dossier).

**AX-8 — Attention de soin : réception et indifférence organisée** *(`ProfReg/Fiche_Axiome_A8_Attention_de_Soin_Indifference_Organisee_2026-09-30.md`, l.22)*

> **AX-8 — Attention de soin : réception et indifférence organisée.** Le soin commence par une attention au particulier, qui se laisse affecter par la situation et la perçoit dans son détail.
>
> **(1) Réception.** Un soin n'est pas achevé quand il est donné : il comprend un moment de **réception**, où ceux qui le reçoivent peuvent faire entendre si la réponse convient. Sans ce moment, la justesse du soin n'est pas établie.
>
> **(2) Indifférence organisée.** Cette attention n'est pas également répartie : elle est **assignée** à certains. Ce transfert **permet** à ceux qui en bénéficient de ne voir ni leur propre dépendance, ni ceux qui la prennent en charge.

*Conditions* *(`ProfReg/Fiche_Axiome_A8_Attention_de_Soin_Indifference_Organisee_2026-09-30.md`, l.84)* :

> **(1) AX-8 tombe, pour la réception,** si l'on documente un dispositif où la justesse d'un soin est **durablement établie**, et tenue pour telle par ses bénéficiaires une fois interrogés, **sans qu'aucun moment de réception** n'ait été prévu ni exercé.
>
> **(2) AX-8 tombe, pour l'indifférence organisée,** si l'on documente un **transfert durable** du soin d'une dépendance vers un groupe tiers, à l'issue duquel les bénéficiaires **continuent** de connaître cette dépendance **et** de reconnaître, matériellement et symboliquement, ceux qui la prennent en charge.
>
> **Ne la font pas tomber** : *(i)* un soin technique sans réception (objection c : sa justesse n'est pas établie, il existe) ; *(ii)* des cas individuels de reconnaissance ; la clause (2) porte sur un transfert **organisé et durable**.

*Formalisation de la clause (1) : PR-39 (`AX-8 -. formalisé par .-> PR39`) ; appui de CONV-11 ; tension avec RSO-6. Clause (2) sans formalisation `[LACUNE FORMELLE DÉCLARÉE]`.*

**AX-9 — Conflit et permanence** *(`ProfReg/Fiche_Axiome_A9_Conflit_et_Permanence_2026-09-08.md`, l.22)*

> **AX-9.** Une institution durable ne tire pas sa durée de l'absence de conflit, mais de deux choses : elle **institue** le conflit — elle en fait la source de ses règles plutôt que la menace à supprimer — et elle se **ramène périodiquement à son principe**, faute de quoi elle s'altère et cesse de durer. Corollairement, une autorité d'exception n'est compatible avec la durée que si elle est **bornée dans le temps** par un porteur autre que son bénéficiaire.

*Condition* *(`ProfReg/Fiche_Axiome_A9_Conflit_et_Permanence_2026-09-08.md`, l.82)* :

> **AX-9 tombe si l'on documente des institutions durables ayant supprimé le conflit plutôt que l'ayant institué**, ou si l'on montre que la durée des institutions ne corrèle pas avec leur capacité de retour au principe. C'est une **condition empirique**, et le corpus déposé ne la teste pas.

**AX-10 — Sélectivité située de l'attention (Campo 2020, 2026)** *(`ProfReg/L1_repris_Campo_2026-09-07.md`, l.195 ; repris verbatim, étiquette AX-10, dans `ProfReg/Fiche_Axiome_A10_Selectivite_Situee_Attention_2026-09-30.md`, colonne A)*

> **AX-10.** L'attention n'est pas une quantité fixe dont un sujet souverain disposerait. Elle est une pratique **située, sélective et relationnelle** : elle ouvre un champ de pertinence et laisse nécessairement d'autres relations à l'arrière-plan. Cette sélectivité n'est pas seulement une limite individuelle — elle est **organisée** par des systèmes de pertinence, des cadres d'interaction et des dispositifs matériels et techniques.
>
> En particulier, les infrastructures de mesure ne se bornent pas à enregistrer ce à quoi on prête attention : elles participent à décider ce qui mérite attention, et tendent à devenir invisibles à mesure qu'elles deviennent infrastructurelles.

*Condition* *( `ProfReg/Fiche_Axiome_A10_Selectivite_Situee_Attention_2026-09-30.md`, §4)* :

> **AX-10 tomberait si l'on établissait que le champ de pertinence d'un collectif est invariant aux dispositifs de mesure et de pertinence qui l'organisent.**

*Étiqueté « A4 » dans la pièce d'origine (`L1_repris_Campo_2026-09-07.md` §7). Fiche au gabarit : `ProfReg/Fiche_Axiome_A10_Selectivite_Situee_Attention_2026-09-30.md` (ancrage clause par clause sur Campo 2026 lu intégralement et Campo 2020 ch. VI lu en partie ; gabarit contradictoire, dont Adams & Aizawa 2010 ; colonne B **proposée, non appliquée** ; condition portant sur le « champ de pertinence », décision du porteur).*

**AX-11 — Homologie de forme de trois obligations** *(`Fiches_Axiomes_A11_A12_A13_2026-09-11.md`, l.49)*

> **AX-11 — Homologie de forme de trois obligations.** L'exigence `M_att(x,y) ≥ F_y(M_met(x,y))`, l'obligation de responsabilité envers une entité vulnérable, et l'écriture qui inscrit une dette et sa couverture sont **homologues de forme** : elles partagent des traits de forme déclarés, et **ceux-là seulement**. Ce ne sont pas trois figures d'une même structure : aucune valeur ne se transporte de l'une à l'autre (CONV-1), et aucun foncteur n'est revendiqué.
>
> | Trait | Exigence MRC (NT-ARCH §2ter) | Obligation de responsabilité (Jonas) | Écriture comptable |
> |---|---|---|---|
> | **T1. Domination ordonnée** : ce qui est fourni domine ce qui est exigé, sans l'égaler | `≥` de V_att | la responsabilité est « une fonction du pouvoir et du savoir » (p. 171) | couverture ≥ dette `[PLAUSIBLE : principe de prudence — à sourcer, PCG / IAS 37]` |
> | **T2. Asymétrie** : l'exigence ne décroît pas quand la menace croît | F_y à trois régimes | « priorité du mauvais pronostic sur le bon » (p. 54-55) | provision croissante avec la probabilité de sortie `[PLAUSIBLE — à sourcer]` |
> | **T3. Élément absorbant** : un état où aucune couverture ne suffit, et où l'acte qui l'exige est interdit | ⊤ → R-INTERDIT-ABSOLU | « l'enjeu ne doit jamais être l'intégralité des intérêts des autres concernés, surtout pas leur vie » (p. 60-61) | **absent** : la comptabilité ordinaire n'interdit pas, elle constate l'insuffisance |
>
> **T3 n'est pas porté par la forme comptable ordinaire : le MRC le lui impose.** L'homologie est **complète entre l'exigence MRC et l'obligation jonasienne**, **partielle (T1, T2) avec l'écriture comptable**.

*Condition* *(`Fiches_Axiomes_A11_A12_A13_2026-09-11.md`, l.104 et l.108)* :

> **AX-11 tombe si l'on exhibe une obligation de soin bien formée au sens du MRC dont la forme comptable ne soit pas construisible** — c'est-à-dire une exigence de maintien réelle, avec porteur, horizon et vérification, qu'aucune écriture typée ne peut porter sans la déformer.
>
> **AX-11 tombe également si l'un des trois domaines ne porte pas un trait que l'énoncé lui attribue** — par exemple une obligation de responsabilité, au sens de Jonas, dont l'exigence **décroît** quand la menace croît (T2). Aucun foncteur n'étant revendiqué, la condition « un lecteur exige le foncteur » est **sans objet** ; elle est remplacée par : **le tableau des traits est soumis à un lecteur, qui confirme ou réfute chaque case**.

**AX-12 — Attracteurs cognitifs** *(`Fiches_Axiomes_A11_A12_A13_2026-09-11.md`, l.138)*

> **AX-12.** Des dispositions cognitives durables — héritées, ou stabilisées par transmission culturelle cumulative — produisent des **attracteurs** : des points vers lesquels les représentations collectives tendent spontanément, indépendamment de leur justification délibérée. Le décalage entre un attracteur et une règle délibérée du registre est **repérable et inscriptible**.

*Condition* *(`Fiches_Axiomes_A11_A12_A13_2026-09-11.md`, l.186)* :

> **AX-12 tombe si l'on documente un dispositif collectif où une règle délibérée, contraire à un attracteur identifié, est adoptée et tenue durablement sans dispositif de maintien** — c'est-à-dire où la résistance à la révision, supposée durable, ne se manifeste pas.

**AX-13 — Lecture mimétique** *(`Fiches_Axiomes_A11_A12_A13_2026-09-11.md`, l.223)*

> **AX-13 — Lecture mimétique.** La théorie mimétique fournit une **grille d'interprétation** des crises collectives : elle donne à lire une montée de la rivalité vers l'indifférenciation, sa résolution par focalisation sur une victime unique, et la méconnaissance que conservent les institutions issues d'une telle résolution. Le MRC l'emploie **comme grille, non comme cadre causal** : elle qualifie une inscription, elle ne l'explique pas et ne prédit rien. Son auteur la donne pour une hypothèse dont « la valeur […] se vérifie à l'abondance des matériaux […] qu'elle sera capable d'interpréter » (Girard, *La Violence et le sacré*, Grasset, 1972, p. 228).

*Condition de pertinence* *(`Fiches_Axiomes_A11_A12_A13_2026-09-11.md`, l.279)* :

> **Condition de pertinence** *(tient lieu de condition de réfutation pour une grille, famille 5 ; option (α))*. **AX-13 tombe comme grille si l'un des deux cas se produit :**
> **(a) Non-discrimination.** Appliquée à un corpus d'au moins deux crises collectives nommées, dont **au moins une est documentée par des intérêts divergents, sans imitation du désir** (objection c), la grille ne rend sur **aucune** une lecture négative (`médiation_type` ∉ {RIVALITE_ACTIVE, INDIFFERENCIATION} ou `focalisation_victimaire` = FAUX). Une grille qui lit toute crise de la même façon ne discrimine rien.
> **(b) Non-reproductibilité.** Deux lecteurs indépendants, appliquant la grille à la même crise sur les mêmes pièces, divergent sur `focalisation_victimaire` ou `médiation_type`, sans que l'écart soit imputable aux pièces.
>
> **Ne la font pas tomber** : l'existence de lectures concurrentes (une grille n'est pas exclusive) ; l'absence de prédiction (elle n'en revendique pas).
>
> **Règle de provenance** : le corpus d'épreuve ne peut pas être celui de Girard (mythes, rites, tragédies) ; il est tiré des terrains du set ou d'un corpus hors set.

**AX-14 — L'objectivité tient à la critique transformatrice (Longino 1990)** *(`ProfReg/Fiche_Axiome_A14_Longino_Objectivite_Sociale_2026-09-28.md`, l.13)*

> **AX-14.** L'objectivité d'une connaissance n'est une propriété ni de l'individu qui l'énonce, ni des seules données qui l'appuient : elle tient au **degré** auquel la communauté qui la produit permet la **critique transformatrice** de ses données, de ses méthodes et de ses **présupposés d'arrière-plan**. Ce degré dépend de quatre conditions : des **voies reconnues** de critique ; des **standards partagés** que les critiques peuvent invoquer ; la **réponse** de la communauté à la critique ; l'**égalité de l'autorité intellectuelle** entre praticiens qualifiés.

*Condition* *(`ProfReg/Fiche_Axiome_A14_Longino_Objectivite_Sociale_2026-09-28.md`, l.62)* :

> **AX-14 tombe, pour l'usage qu'en fait le MRC, si l'on documente un dispositif d'inscription dont les inscriptions sont durablement contestées et effectivement corrigées sans qu'aucun tiers non partie n'ait accès ni à la contestation ni aux règles qui la gouvernent** — c'est-à-dire une réfutabilité effective sans inspectabilité. Il suffirait d'un cas.

*Fiche établie sur lecture de Longino 1990, ch. 4, p. 72-79.*

**AX-15 — Rapprochement banque / client** *(`ProfReg/Fiche_Axiome_A15_Rapprochement_Bancaire_2026-09-29.md`, colonne A)*

> **AX-15.** Au titre de l'obligation d'inventaire — le commerçant contrôle au moins une fois tous les douze mois l'existence et la valeur des éléments d'actif et de passif (C. com., art. L.123-12) et organise les données d'inventaire « de manière à justifier le contenu de chacun des postes du bilan » (PCG, règlement ANC n° 2014-03, art. 1021-3, version consolidée au 1ᵉʳ janvier 2026) —, la pratique décrite par le manuel de référence (Richard, Bensadon & Rambaud, *Comptabilité financière*, 2018, ch. 40 §4) est la suivante. Une entreprise tient son compte Banque ; la banque tient, de son côté, le compte de cette entreprise. Les deux comptes enregistrent les **mêmes opérations**, en **sens opposé** : une rentrée de fonds pour l'entreprise est une sortie pour la banque. À un instant donné, ils **concordent rarement** ; l'écart est **normal**, il n'est pas une faute. À la clôture, l'entreprise établit un **état de rapprochement** qui nomme les opérations manquantes de chaque côté, et **complète son propre compte** des opérations qui figurent sur le relevé de la banque.

 *Énoncé daté ; énoncé du 29/09 dans la fiche.*

*Condition* *(même fiche, gabarit §4)* :

> **AX-15 cesse** (péremption) si l'obligation de justifier les postes du bilan par inventaire disparaît, ou si la banque cesse de communiquer son registre au client (relevé), ou si le rapprochement devient une opération sans inscription propre de l'entreprise (compte 512 alimenté par copie du relevé).

> **AX-15 tombe comme ancrage de N2** si l'on établit que le rapprochement banque / client **ne porte pas sur deux registres tenus indépendamment** — par exemple si le compte de l'entreprise n'était qu'une copie du relevé, sans inscription propre. Dans ce cas, il n'y aurait qu'un teneur, et la forme de N2 ne serait pas attestée par cette pratique.

*Fiche établie sur lecture de Richard, Bensadon & Rambaud 2018, ch. 40 §4, p. 639-640. Ancrage de l'écriture duale entre teneurs (PR-35) ; appuie PAL-2c.*

**AX-16 — L'écart est investigué par un tiers (ISA 505)** *(`ProfReg/Fiche_Axiome_A16_Confirmation_Externe_ISA505_2026-09-30.md`, colonne A)*

> **AX-16.** Selon ISA 505, *External Confirmations* (IAASB), dans le texte anglais publié par l'Institut des Réviseurs d'Entreprises et lu le 30 septembre 2026, l'audit légal organise la vérification d'une information inscrite par une entité en la faisant **confirmer directement par un tiers**, sous le **contrôle de l'auditeur** ; toute **différence** entre les registres de l'entité et la réponse du tiers est une **exception**, que l'auditeur est **tenu d'investiguer** ; l'élément probant est d'autant plus fiable qu'il vient de **sources indépendantes, extérieures à l'entité**.

 *Énoncé daté ; énoncé du 30/09 dans la fiche.*

*Condition* *(même fiche, gabarit §4)* :

> **AX-16 cesse** (péremption) si ISA 505 est remplacée ou modifiée au point que la confirmation externe, ou l'investigation des exceptions (§14), n'y figure plus.

> **AX-16 tombe** (réfutation) si l'on établit que, **à sa date**, la version lue d'ISA 505 ne prévoyait pas l'investigation des exceptions — c'est-à-dire que la lecture de la fiche est fausse.

*Fiche établie sur lecture d'ISA 505 et d'ISA 550 (publication IRE). Ancrage de PR-41 et PR-42 ; l'identité du tiers est instituée par CONV-16.*

**AX-17 — La responsabilité n'est pas transférée par la relation d'affaires** *(`ProfReg/Fiche_Axiome_A17_Responsabilite_Non_Transferee_OCDE_2026-09-30.md`, colonne A)*

> **AX-17.** Dans les *Principes directeurs de l'OCDE à l'intention des entreprises multinationales* (édition 2023) et dans la directive (UE) 2024/1760 (version consolidée au 18 mars 2026), les normes de conduite responsable distinguent trois liens entre une entreprise et un impact négatif : **le causer**, **y contribuer** substantiellement, ou lui être **directement lié** par une relation d'affaires. Seuls les deux premiers font de l'entreprise la **débitrice de la réparation**. Au troisième, elle doit **user de son influence** pour que l'entité à l'origine prévienne, atténue ou corrige l'impact. **La responsabilité de l'entité à l'origine n'est pas transférée** à l'entreprise avec laquelle elle est en relation d'affaires.

 *Énoncé daté ; énoncé de la fiche.*

*Condition* *(même fiche, gabarit §4)* :

> **AX-17 cesse** (péremption) si une version ultérieure des Principes directeurs de l'OCDE ou de la directive (UE) 2024/1760 met la **réparation** d'un impact à la charge d'une entreprise **seulement directement liée**, c'est-à-dire admet le transfert de responsabilité.

> **AX-17 tombe** (réfutation) si l'on établit que, **à sa date**, les textes lus étaient appliqués autrement — par exemple si des Points de contact nationaux mettaient déjà la réparation à la charge d'entreprises seulement directement liées.

*Fiche établie sur lecture des Principes directeurs de l'OCDE (2023, version française) et de la directive (UE) 2024/1760 consolidée au 18/03/2026. Ancrage de PR-46 (règle 3) et de PR-47 (CONV-18).*

`[LACUNES ET LIMITES]` Les énoncés sont ceux des fiches, dont plusieurs n'ont pas été relus depuis leur date ; AX-10 n'a pas de fiche au gabarit ; le triplet est posé pour les dix-sept ; **une seule condition a été confrontée à un cas selon la règle de provenance : AX-7, sur la charte de Roubaix — ne tombe pas à sa date, sous réserves (table des triplets ci-dessus)** , et huit cas restent à désigner. La table **n'établit** aucun axiome : elle les rend **contestables sur pièces**.

### §A.15.1 La table

| # | Énoncé | Statut | Origine / emplacement | Palier | Instruction |
|---|---|---|---|---|---|
| **CONV-1** `E1` *(proposé, §A.15.15)* | La **fraction actorielle est déclarée, jamais calculée** : aucun foncteur de calcul n'est mobilisable dans ProfReg | Architecture | — (aucun théorème) | PAL-3 | `Conventions_et_sanctions_2026-09-07.md` §2 ; **condition de réfutation : §A.15.15**  |
| **CONV-2** *hors critère* / `E6` *(proposé, §A.15.15)* | La **commutativité du carré triangulaire** NT-G7 ↔ NT-G2 ↔ NT-ARCH est **procédurale**, non formelle ; la 2-cellule complète reste hors Mathlib.  **De même la commutativité du carré B1↔B2** (phase INVENTAIRE-ASSETS-ACTIFS) : procédurale, portant sur la **phase d'aboutissement**, **jamais une dispense d'inventaire** — §A.15.9 | Déclaration | **`V3_commutatif`** (lecture des deux définitions, jamais appui : forme 1 par construction) ; carré B1↔B2 : **PR-51** (`carre_B1B2_commute_sur_les_chemins_admissibles`) | PAL-4 ; PAL-3 (B1↔B2) | *idem*  réfutation (triangle) : §A.15.10 |
| **CONV-3** `E1` | Le **régime d'obligation est un champ obligatoire** : aucun côté d'écriture n'est inscriptible sans `regimeobligation` déclaré | Typage | `LotL2_PR2_PR14.lean`, structure `Cote` | PAL-2 | *idem*  ; réfutation : §A.15.10 ;  **effet du défaut : refus — branche 1 du critère §A.15.11** : `regimeobligation` est une primitive de Couche 0, **constitutive** d'un côté d'écriture (NT-ARCH §2 : « une primitive, pas un attribut dérivé ») ; elle prime sur la branche 4 (attribution) par l'ordre du critère |
| **CONV-4** `E1` / `E4` *(proposé, §A.15.15)* | Le **valorimètre déclare sa source** : tout valorimètre ou seuil de F8 porte un champ `source_valuemetre` obligatoire, exigeant une **source déclarée et vérifiable** — désignation stable, résolution déclarée, vérification d'intégrité, porteur nommé et réfutable ; **le DID en est une forme possible, non la forme obligatoire** . **C'est PR-1 dans sa version fidèle** | Typage | PR-1, à porter en F8 | PAL-3 (une convention ne se dérive pas d'une autre) | *idem* ; **ancrages PR-28** et réfutation : §A.15.10 |
| **CONV-5** `E6` *(proposé, §A.15.15)* | **Déclencher une règle R-\* vaut régime d'usage normatif** | Traduction | PR10-a | PAL-4 | `PR10_Statut_du_seuil_2026-09-07.md` §7 — **voir §A.15.2** |
| **CONV-6** `E3` | La **représentation prospective est exigée** de toute écriture qui engage au-delà de l'exercice | Architecture | — (aucun théorème) | PAL-4 | Graphe §2septies  ; **ancrages PR-28** et réfutation : §A.15.10 ;  **effet du défaut : E3** (branche 4 — qui représente les intéressés futurs ; homologue de `V10a_planetaire_force_deliberation`) — §A.15.11 |
| **CONV-7** `E4` |   **Une inscription dont la condition de réfutation est obligatoire et absente est inscrite avec le marqueur `[CONDITION DE RÉFUTATION ABSENTE]` ; elle n'est pas refusée** — patron de CONV-15 ; **horizon** : critère de sortie ou caducité (§A.15.10, PR-32) ;  **effet du défaut : marqueur — branche 5 du critère §A.15.11** (l'objet existe ; la condition de réfutation est un terme d'appréciation) | Architecture | **PR-8** `le_marqueur_se_leve_exactement_sur_le_defaut`, `bien_formee_sans_refutation_n_est_pas_obligee` | PAL-4 | Graphe §2septies ; **§A.15.10** |
| **CONV-8** `E3` | Un **seuil au statut `NONDECLARE` appelle la délibération** — et cela se déclare, la seule exhaustivité du type ne l'établit pas | Architecture | — (aucun théorème) | PAL-4 | `Rapport_Etape0_Audit_2026-09-07.md` §5d — **voir §A.15.3**  ; **ancrage PR-28** (moitié positive) et réfutation : §A.15.10 |
| **CONV-9** `E6` *(proposé, §A.15.15)* | Toute mobilisation d'une primitive `seuil-valuatif` déclare, au **cinquième terme** du statut du seuil, **ce que l'agrégat sert à établir** ; `non déclaré` ne vaut pas déclaration | Typage | Décision du porteur |  **PAL-3** (principal) ; **PAL-4** (secondaire)  | **§A.14.9** (énoncé complet) |
| **CONV-10** `E6` *(proposé, §A.15.15)* | Dans toute instance du registre comptable augmenté L2, la valeur `plein` signifie **que le registre reconnaît le lien**, jamais qu'il le valorise | Interprétation | CONV-10 |  **PAL-2b**  | **§A.14.10** (énoncé complet) |
| **CONV-11** `E4` | Une écriture typée `e` dont l'apporteur de l'effort figure comme créancier n'est bien formée que si le **mouvement de maintien** est inscrit de façon structurée, et si l'écriture **nomme le registre qui le porte** | Bonne formation | Décision du porteur |  **PAL-2** (principal) ; **PAL-4** (secondaire)  | **§A.15.4** (énoncé complet) ; NT-ARCH §8.5.3bis ;  **effet du défaut : E4**, marqueur `[MAINTIEN NON STRUCTURÉ]` (branche 5) — §A.15.11 |
| **CONV-12** `E7` | Toute inscription mobilisant une obligation à deux niveaux distincts (entité / territoire) **déclare le niveau de chacune**. La **non-équivalence n'est pas déclarée** : elle est calculée | Typage | Décision du porteur | PAL-6′ | **§A.15.5** (énoncé complet) |
| **CONV-13** `E7` | Toute écriture d'obligation déclare, **à l'inscription**, le **successeur** vers lequel l'obligation échoit si son porteur disparaît. Champ obligatoire ; `non déclaré` vaut régime strict, il ne vaut pas permission de transférer | Typage | Décision du porteur | PAL-6′ | **§A.15.6** (énoncé complet) |
| **CONV-14** `E6` *(proposé, §A.15.15)* | **L'échelle de communalité ne s'agrège pas.** La communalité se qualifie sur **plusieurs axes juridiques distincts** — au moins l'**intérêt commun** et l'**inclusivité** — et selon les **instances** où elle se manifeste. **Ces axes se déclarent séparément ; aucun score composite n'en est dérivé, et aucun classement n'est établi entre choses de régimes juridiques différents** | Typage | Lecture du rapport Rochfeld-Cornu-Martin | PAL-4 | **§A.15.7** (énoncé complet) ; NT-G6 §2.1  ; garde **PR-28** ; séparabilité des axes : **PR-58**, **PR-59** |
| **CONV-15** `E5` | **Co-obligation F4.** Toute inscription qui déclare l'**appel immanent** d'un acteur déclare aussi sa **puissance affirmative**, et réciproquement — les **amendements A2 et A3 de NT-G2**, *non les axiomes AX-2 et AX-3*. Une paire **non cohérente** ou **incomplète** **s'inscrit** et porte le marqueur `[PAIRE F4 NON COHÉRENTE]` : **marqueur, jamais refus** | Typage | Décision du porteur | — | **§A.15.8** (énoncé complet) ; NT-G2 §3.2 |
| **CONV-16** `E4`  | **Le tiers d'une écriture duale est l'instance de contrôle commune.** Chaque registre de communalité désigne son instance de contrôle par une désignation **arrêtée** ; le tiers d'une écriture duale entre A et B est l'instance **désignée par les deux**, qui n'est **ni A ni B** et **n'est pas liée** ; **seule elle arbitre l'écart** et elle peut **constater la réalisation** du maintien ; à défaut, l'écart reste inscrit, **non arbitrable** | Institution | Décision du porteur | **PAL-2c** | **§A.15.12** (énoncé complet) ; appui PR-43 |
| **CONV-17** `E6`  | **Seul un constat attesté selon le protocole est porté au nom du registre.** Un constat sans miroir de sa contrepartie n'est porté **au nom du registre** devant un tiers extérieur ( **toute voie de PR-44, `Voie`** — huit ) que s'il est attesté selon les **sept rubriques** du protocole ; à défaut, la saisine est inscrite `[SAISINE HORS PROTOCOLE]` ; CONV-17 n'interdit à personne de signaler en son nom | Institution | Décision du porteur | **PAL-2c** | **§A.15.13** (énoncé complet) ; appui PR-45 |
| **CONV-18** `E4` / `E5`  | **Annotation de destination d'un engagement de vigilance.** Tout engagement porté à un registre de chaîne nomme le **site**, l'**objet** (parmi les objets déclarés du registre) et le **lien** déclaré (cause / contribue / directement lié, OCDE 2023) ; l'**instance commune** (CONV-16) vérifie la destination et **qualifie le lien**, le lien retenu primant sur le lien déclaré ; à défaut d'annotation `[DESTINATION NON DÉCLARÉE]` ; à défaut de qualification `[LIEN NON QUALIFIÉ PAR L'INSTANCE]` | Institution | Décision du porteur | **PAL-2c** | **§A.15.14** (énoncé complet) ; appui PR-47 |
| **CONV-19** `E6` *(proposé, §A.15.16)* | **Le signal de souffrance n'est jamais l'appui d'une créance.** `signalsouffrance` est un indice explicatif : il n'entre dans aucune qualification de créance et ne déclenche aucune règle R-\* qui conférerait un droit ; la légitimité d'une créance reste portée par G-JUSTICE | Usage (non-confusion) | NT-G9 §4.2 ; décision du porteur (12/10/2026) | — | **§A.15.16** (énoncé complet) ; appui PR-52 |
| **CONV-20** `E1` *(branche 1bis, §A.15.17)* | **Qualification du régime affectif : source, consentement, protection, support.** Une qualification de `regimeaffectif` n'est inscriptible qu'avec une source déclarée (`CLINIQUEEXTERNE`, `DIALOGUEPROFESSIONNEL` ou `ARCHIVAGEDESACTES` ; `INDÉTERMINÉE` ne qualifie pas), `consentementcollectif` = VRAI et `statut_rgpd_regimeaffectif` ∈ {ANONYMISE, PSEUDONYMISE, AGREGESEUL} ; sur support distribué, seul `NONCOLLECTE` est admis — `NONCOLLECTE` désigne l'absence de toute qualification inscrite, seule l'existence des traces étant tenue | Typage (données sensibles) | NT-G9 §10.1 ; décision du porteur (12/10/2026) | — | **§A.15.17** (énoncé complet) ; appui PR-52 |

**Décompte : **vingt** conventions inscrites** (CONV-1 à CONV-20).

**Les dix axiomes du sous-graphe AX sont instruits, chacun sur source lue, avec ses trois colonnes et son gabarit contradictoire.** AX-1 (v2, Stépanoff 2024 : **condition de réfutation adoptée** — AX-1 tombe si l'on documente un collectif dont une part significative des dépendances matérielles provient de territoires qu'il ne fréquente pas, et qui exerce sur ces dépendances-là non seulement une connaissance mais un soin — une action effective sur leurs conditions de renouvellement — comparable à celui qu'il exerce sur ses dépendances locales ; ne le réfutent ni la re-densification d'un réseau, ni la seule connaissance chiffrée de dépendances lointaines, ni l'existence d'inscriptions (Pruvost 2024, p. 424-484) ; seuil non fixé, lacune déclarée) ; AX-2 ; AX-3 (Demonsant *et al.*, *RFG* 2026) ; **AX-4 — mobilisabilité** et **AX-5 — non-fermeture des chaînes** (résultats de la Partie I) ; AX-7 ; **AX-9 — conflit et permanence** (Machiavel *Discours* I, 4 et III, 1 lus au verbatim ; la réserve sur le traducteur non identifié demeure) ; **AX-10** (sélectivité située de l'attention, Campo 2026) — **instruit dans `ProfReg/L1_repris_Campo_2026-09-07.md` §« Colonnes A/B/C »**, sous un nom de fichier qui ne le signale pas.

> **AX-3.** La présente table le nomme — *« AX-3 (Demonsant et al., RFG 2026) »* — et **§A.15.5 fait reposer sur lui le retrait du nœud D** : *« L'argument du retrait est AX-3 : fermer le carré rendrait la répartition dérivable de l'agrégation, et c'est le recouplage que AX-3 défait. »* **La fiche d'AX-3 est en §A.18** (énoncé, portée, ce qu'il ne dit pas, appui, garde-fou anti-permanence, condition de réfutation, reste de traduction, engagement distributif déclaré). **AX-10, instruit hors set, n'a pas de fiche au set : la lacune demeure ouverte.** Instruction : `Decision_P9_Verrou_Macro_x_Avaries_Communes_2026-09-14.md` §2.

 Trois axiomes sont instruits dans une fiche unique — `Fiches_Axiomes_A11_A12_A13_2026-09-11.md` :

> **AX-11 — l'isomorphisme des trois formes** *(famille 6 : **postulat de structure** ; énoncé comme « homologie de forme », §A.15.0)*. Ce qui autorise R1 à porter une exigence de soin et non une égalité comptable ; **le postulat dont dépend le plus, dans tout le set**. La fiche relève que NT-ARCH §2ter écrit **une inégalité (« commute par excès », L88) et un isomorphisme (L94) à six lignes d'intervalle**, et que la paraphrase de Jonas — responsabilité *proportionnelle* — **contredit l'asymétrie croissante** que le set pose dans le même paragraphe. `[INCOHÉRENCE INTERNE]` Statut : **valable sous forme affaiblie**.
>
> **AX-12 — le cadre EEA de G-EVOLUTIVITE** *(famille 5 : **cadre théorique importé**)*. Les cinq sources sont `VÉRIFIÉ` ; **l'étiquette « EEA » est employée par Boyer (qui la définit : « a statistical construct […] not a particular time or place ») et par Sperber, et contestée par les modèles d'évolution culturelle** ; Henrich 2015 argumente contre la thèse nativiste forte `[NON VÉRIFIÉ SUR EXEMPLAIRE]`.
>
> **AX-13 — la causalité mimétique de G-MIMETIQUE** *(famille 5)*. Les trois Girard fondateurs sont `✅ VÉRIFIÉ` ; le défaut est de **statut modal** — « dynamique causale » là où la théorie vaut comme grille d'interprétation. **Sa condition de réfutation est déclarée faible**, la théorie pouvant l'absorber.

**Familles 5 et 6, et pourquoi.** Les quatre autres familles — anthropologique, institutionnelle, constat historique daté, et *constat sur l'état d'un corpus théorique* forcée par AX-6 — ne logent aucun des trois. **Famille 5 (cadre importé)** : le modèle adopte une théorie externe comme cadre de travail ; il ne l'établit pas, il en hérite — **et il hérite de ses objections**, ce qu'une fiche de cette famille est tenue de nommer. **Famille 6 (postulat de structure)** : une thèse du modèle sur lui-même, affirmant que deux domaines partagent une forme. AX-11 en est le seul membre — *une famille à une entrée est un aveu autant qu'un rangement*.

**Les neuf autres grammaires** reçoivent, non une fiche, mais **une condition de réfutation déclarée d'une ligne**, versée dans chaque `NT-G*` §2.1. `[DETTE DE MÉTHODE DÉCLARÉE — une condition de réfutation sans gabarit contradictoire est un tiers de fiche, et aucune des neuf n'a jamais été testée.]`

 **AX-13** se lit comme « dynamique donnée à lire ». **AX-12** : l'étiquette EEA est écartée par décision du porteur (`praticabilite_cognitive`, `ATTRACTEUR-COGNITIF`) ; `profondeur_évolutive` est **suspendu** faute de source pour ses valeurs ; §2.1 de NT-G1 repose sur l'épidémiologie des représentations et l'évolution culturelle. Statut d'AX-12 : `valable sous conditions déclarées`. **AX-11** s'énonce comme « homologue de forme ». **Ce sont des actes de porteur.**

`[RÉSERVE SUR CE LOT]` Les trois objections les plus fortes qu'il porte reposent sur une **connaissance de seconde main** : aucune source primaire — Jonas, Boyer, Sperber, Tinbergen, Henrich, Girard — n'a été lue pour l'établir. **À contrôler sur exemplaire avant toute requalification.** `[PLAUSIBLE, NON VÉRIFIÉ]`

 **`A5` désigne deux choses.** Dans le sous-graphe des axiomes, **AX-5 est la non-fermeture des chaînes** ; dans la numérotation des amendements de grammaires, « A5 » désigne l'amendement qui lève le découplage M→R (NT-G8 §10.1) — et c'est **celui-là** que PR-5 formalise : PR-5 n'est pas un théorème compilé sans fiche d'axiome. **PR-4 et PR-7 sont compilés sans fiche d'axiome** — le premier n'en invoque aucun, le second s'appuie sur Le Naour 2024, vérifié mais non instruit.

 Fiche : `Fiche_Axiome_A7_Seuil_Arrete_Par_Les_Concernes_2026-09-11.md`.

> **(1) L'objecteur principal d'AX-7, le plus fort possible.** `Suffisance_dans_la_demonstration_2026-09-08.md` §A7 cite **Fretel, Higelé, Jany-Catrice & Tantot (2026)** : la normalisation de TZCLD a fait glisser les personnes *« du statut d'acteurs du projet à celui de publics cibles »*.
>
> **(2) Jany-Catrice & Vatan 2026 n'est pas « au corpus » : il est cité, non détenu.** Contrôle du 11 septembre : **aucune des six pièces du dossier de preuve de AX-7 ne figure dans les 129 fichiers de `biblio/`** — ni la Charte de la Caisse commune, ni le guide CIVAM, ni les documents TZCLD 2015/2017, ni l'article de *L'Économie politique* 2026, ni les deux évaluations.
>
> **La conséquence est de statut, non de validité.** L'existence des dispositifs est publique et hors de doute ; **ce que AX-7 affirme est que les critères y sont arrêtés par les bénéficiaires**, et cette affirmation n'est adossée à aucune pièce tenue. **Statut retenu : `posé — constat daté, dossier de preuve nommé mais non constitué`**, et non `valable sous conditions déclarées`.
>
> **Une objection, formulée dans la fiche et au dossier de personne** : les sept critères de Roubaix sont arrêtés par un **Comité Citoyen**, donc par une instance — entre elle et « les personnes auxquelles le seuil s'applique », il y a **une représentation**. **AX-7 énonce une immédiateté que ses propres cas n'établissent pas** : c'est la forme 8 appliquée à un axiome. **Elle est testable dès aujourd'hui** — il suffit de lire la Charte, qui n'est pas au dossier.

`[ÉTAPE 2 — RÉSIDU, réduit à AX-6]` **AX-6 n'a pas passé l'analyse contradictoire** : les objecteurs de AX-6 (Casal, Crisp, Benbaji, Arneson, Frankfurt) **ne sont pas au corpus**, et Jany-Catrice & Vatan 2026 — évaluation indépendante de TZCLD, au corpus — **n'est pas lu**. C'est le seul manque restant du sas de traduction.

### §A.15.2 CONV-5 — énoncé rédigé *(reconstruction)*

 L'énoncé ci-dessous est **reconstruit** à partir d'une étiquette de diagramme et d'une phrase du rapport PR-10, et validé par le porteur ; il n'est pas une citation.

> **CONV-5 (PR10-a).** Dans le périmètre où PR-10 opère, **« déclencher une règle R-\* » vaut « régime d'usage normatif »**, et réciproquement. Une mobilisation sous `[VALUATION SUSPENDUE]` ne déclenche donc aucune règle R-\*.

**Statut : convention de traduction**, et c'est la plus fragile de la table §A.15.1 (vingt conventions) `[JUGEMENT D'INSTRUCTION — non réexaminé sur l'ensemble des vingt]`. Le rapport d'origine le déclare sans détour : *« l'identification "déclencher une règle R-\*" = "régime d'usage normatif" est ma traduction, pas une définition du set. Le set ne définit pas le déclenchement au niveau où PR-10 opère. »*

**Ce qu'elle rend possible.** Sans elle, `suspension_ne_declenche_aucune_regle` (PR-10) **n'a pas d'énoncé**. Avec elle, il en a un — qui vaut ce que vaut la traduction.

`[DÉCOUPLAGE DE RÉGIMES — risque déclaré]` Si le set définit un jour le déclenchement autrement, `suspension_ne_declenche_aucune_regle` **change de sens sans cesser d'être vrai**. C'est la pire des situations, et elle est inscrite ici pour être surveillée. **Condition de réfutation** : une définition du déclenchement, posée au niveau où PR-10 opère, qui ne coïncide pas avec le régime d'usage normatif.

### §A.15.3 CONV-8 — énoncé rédigé *(reconstruction)*

 Même régime que CONV-5 : l'énoncé est reconstruit à partir de ce que NT-ARCH §8 en dit.

> **CONV-8.** Un seuil dont le statut est `NONDECLARE` **appelle la délibération**. Cette obligation est **déclarée comme règle d'architecture** ; elle ne se déduit pas de l'exhaustivité du type `StatutDette`.

**Origine.** Un énoncé à hypothèses inertes et à conclusion disjonctive sur les trois constructeurs de `StatutDette` est **vrai de tout** ; **NT-ARCH §8** le déclare : « tautologie structurelle (exhaustivité de `StatutDette`) ; il n'établit pas l'exclusion ».

**Appuis formels.** Patron : *déclarer la règle d'architecture, puis conclure par V4*, comme `V10a_planetaire_force_deliberation`. **Moitié négative** : `nonDeclare_ne_vaut_pas_permission` (PR-17), qui établit que le silence ne vaut pas permission. **Moitié positive** : `nondeclare_force_deliberation` (PR-28), sur ce patron — §A.15.10.

### §A.15.4 CONV-11 — obligation d'inscrire le mouvement de maintien

> **CONV-11.** Une écriture typée `e` dont l'apporteur de l'effort figure comme créancier dans le régime déclaré est **bien formée seulement si** le mouvement de maintien correspondant fait l'objet d'une **inscription structurée** — **porteur, contrepartie, solde, horizon, critère de vérification** — et si l'écriture **nomme le registre qui la porte**. *Effet du défaut : **E4*** — l'écriture est inscrite, **mal formée**, et porte `[MAINTIEN NON STRUCTURÉ]` ; elle ne sert pas d'appui (branche 5 du critère §A.15.11).
>
> **Appui formel.** `ProfRegPR23.MaintienCONV11` porte les **six** éléments de CONV-11 — porteur, contrepartie, **registre nommé**, situation (dû, engagé), horizon, critère — et le **solde n'est pas déclaré** : il est calculé comme l'écart dû − engagé (`MaintienCONV11.solde`), c'est-à-dire la dette de préservation au sens CARE. Pour un registre de milieu, le nommage est **vérifié** (`maintien_d_un_autre_registre_pas_d_appui`, PR-37) ; la lacune de nommage reste ouverte dans le cas général (`PR23_ne_certifie_pas_le_nommage`).
>
> **Le registre financier n'est pas requis.** Le registre de communalité, ou un rapport extra-financier dont les champs requis sont renseignés, satisfait la condition. Elle **n'est pas** satisfaite par une mention en langue naturelle sans champ propre, **quel que soit le document qui la porte — bilan compris**.

**Pourquoi une convention et non un théorème.** Motif de CONV-1 à CONV-4 et de CONV-9 : *une obligation ne se démontre pas, elle se déclare.* Écrire « toute écriture bien formée déclare son mouvement de maintien » serait vrai par le type — et écrit avec l'hypothèse « bien formée », ce serait la **forme 3** de §8ter.

**Le défaut visé est la forme de l'inscription, jamais son lieu.** La bonne formation n'est pas subordonnée à l'inscription **au passif du bilan**, sur le patron des provisions pour retraites (Richard, Bensadon & Rambaud 2018, p. 681). **Le porteur écarte ce critère** : subordonner la bonne formation d'une écriture de communalité à sa traduction au bilan ferait du régime financier l'arbitre du registre de communalité. Ce qui compte est que la mention **non structurée** n'a ni contrepartie, ni solde, ni horizon — rien ne s'en calcule, aucun tiers ne la conteste point par point.

**Articulation avec CONV-10.** CONV-11 pose que le registre financier n'est pas requis ; CONV-10 est ce qui rend cette clause compatible avec `registre_augmente_coherent`, en déclarant que `plein` reconnaît le lien sans le valoriser. **Les deux se lisent ensemble.**

**Appuis formels — PR-23** (`ProfReg/PR23_MouvementDeMaintien.lean`, **14 théorèmes, 13 sans aucun axiome**, 0 `sorryAx`, contrôle des neuf `Classical.choice` non déclenché). Sur le patron de PR-10 §7 : **il ne démontre pas CONV-11, il la motive et la borne.**

| | Théorème | Ce qu'il établit |
|---|---|---|
| *le trou* | `BienFormee_ne_borne_pas_le_maintien` | Une écriture typée `e`, **parfaitement bien formée au sens actuel**, dont le maintien n'est pas inscrit. L'obligation est motivée par un théorème, non par une intuition |
| *non-vacuité* | `CONV11_est_satisfiable` | L'obligation est tenable — une condition que rien ne satisfait serait un refus déguisé |
| *la morsure* | `deux_dettes_distinctes_meme_ecriture` | Deux dettes d'**écarts différents** produisent **la même écriture** sans inscription du maintien. Ce n'est pas une perte de précision, c'est une **non-identifiabilité** |
| *la morsure* | `priorite_sans_assiette` | Sans inscription, **R-PRIORITE-CREANCIERS ne rend aucun verdict**. Elle ne se trompe pas : elle n'a pas d'assiette |
| *contrepartie* | `le_maintien_separe_les_situations`, `priorite_mord_si_inscrite` | L'inscription lève la non-identifiabilité et la règle mord effectivement |
| *la glose* | `la_glose_ne_rend_rien_lisible`, `la_glose_varie_librement` | L'écart lisible ne dépend **que** du maintien : la mention en langue naturelle varie librement sans rien changer à la lecture — **quel que soit le document qui la porte** |
| *la garde* | `CONV11_satisfaite_sans_registre_financier` | CONV-11 est satisfaite sans registre financier. **Le critère du bilan écarté par le porteur n'est pas réintroduit** |
| *la lacune* | `PR23_ne_certifie_pas_le_nommage` | Le champ `registre` est **libre** : rien ne vérifie que le nom désigne un registre existant. **La lacune de couverture est démontrée, non concédée** |

`[RÉSERVE DE MODÈLE]` `Situation`, `Ecriture` et `ecart` sont les structures de l'auteur du fichier. Réserve du §2quinquies du graphe : un contre-exemple ne vaut que ce que vaut la fidélité de son modèle. Si l'écart modélisé n'est pas celui du registre, les théorèmes de la morsure sont **vrais et hors sujet**.

`[CONDITION DE RÉFUTATION]` CONV-11 tombe si l'on exhibe un régime où l'apporteur de l'effort figure comme créancier et où la lecture de R-PRIORITE-CREANCIERS n'exige aucun solde ; ou une mention non structurée à partir de laquelle un tiers calcule effectivement l'écart.

`[LACUNE DE COUVERTURE]` **La clause de nommage n'est pas certifiable en l'état** : `RegistreComptableAugmente` porte deux registres câblés et **aucun nom de registre** (§A.14.10). Elle reste déclarative tant que l'une des deux issues de CONV-10 n'est pas tranchée.

`[PORTÉE DÉCLARÉE — Couche 2]` CONV-11 s'applique aux inscriptions **postérieures au 8 septembre 2026**. Les deux lignes de l'Annexe K §K.6.3 qui portent un remboursement en glose **ne la satisfont pas** ; la reprise du cas K1 est une décision distincte, non prise ici.

---

### §A.15.5 CONV-12 — déclarer les niveaux, calculer la non-équivalence

> **CONV-12.** Toute inscription mobilisant une obligation à **deux niveaux distincts** (entité / territoire) **déclare le niveau de chacune**. La **non-équivalence des deux niveaux n'est pas un champ déclaré** : c'est un **contrôle calculé** à partir des niveaux. Aucune transition ne fusionne deux obligations de niveaux différents, et un niveau **non déclaré** ne vaut pas permission de fusionner.

 **AX-3 est porté par le set** : énoncé, portée, reste de traduction et condition de réfutation en **§A.18**. La motivation ci-dessous est donc contestable sur pièces. *Elle n'en est pas validée pour autant : `entite_et_territoire_ne_fusionnent_pas` établit que la substitution n'est pas une résolution.*

**D'où elle vient.** PR-13 `non_equivalence_declaree` est retenu **en substitution du nœud D** — la commutativité micro-macro CARE ↔ CENP, qui exigeait des *framed bicategories* hors Mathlib. L'argument du retrait est **AX-3** : fermer le carré rendrait la répartition dérivable de l'agrégation, et c'est le **recouplage** que AX-3 défait.

**Pourquoi une convention et non un théorème.** L'énoncé porte **deux choses de natures différentes** : une obligation de déclaration, et une interdiction de transition. La première ne se démontre pas — motif de CONV-1 à CONV-4, CONV-9 et CONV-11. L'écrire sous l'hypothèse « bien formée » serait la **forme 3** de §8ter. **Seule la première moitié est CONV-12** ; la seconde est dans PR-13, où elle se démontre.

**Pourquoi la non-équivalence n'est pas déclarée.** Si le niveau est un champ typé, la non-équivalence de deux niveaux **est calculable** : deux niveaux sont non équivalents si et seulement si leurs valeurs diffèrent. Un champ qui doublerait ce calcul pourrait donc **mentir** — c'est le défaut démontré en général par `champ_declare_peut_mentir` (PR-21 ; §8sexies). La décision du porteur applique la règle : *déclarer ce qui ne se calcule pas, calculer ce qui se calcule.*

`[ARGUMENT FORMEL, NON PLAIDÉ]` `un_champ_non_equivalence_declare_pourrait_mentir` (PR-13 §5) **est** `champ_declare_peut_mentir` instancié sur le couple de niveaux — le théorème est **réutilisé, non réécrit**, comme PR-22 réutilise PR-16.

**Appuis formels — PR-13** (`ProfReg/PR13_NonEquivalenceDeclaree.lean`, **16 théorèmes**, 0 `sorryAx`, contrôle des neuf non déclenché) :

| | Théorème | Ce qu'il établit |
|---|---|---|
| *l'interdiction* | `aucune_fusion_entre_niveaux_distincts`, `fusion_admise_seulement_au_meme_niveau` | La moitié qui se démontre : aucune fusion entre niveaux distincts, et toute fusion admise l'a été au même niveau, lisible sur le résultat |
| *le silence* | `niveau_non_declare_ne_vaut_pas_permission` (et sa symétrique à droite) | Un niveau non déclaré **refuse** la fusion. Patron de `nonDeclare_ne_vaut_pas_permission` (PR-17) |
| *le trou* | `aucun_predicat_sur_la_charge_ne_borne_le_niveau` | **Aucune** condition portant sur la charge ne contraint le niveau — plus fort que le patron de PR-23, qui exhibait un cas : ici la classe entière est écartée. Seule CONV-12 ferme le trou |
| *la morsure* | `sans_le_niveau_l_interdiction_est_inapplicable` | Deux situations aux verdicts **opposés** sont indiscernables si le niveau n'est pas inscrit. **CONV-12 n'est pas ornementale : sans elle l'interdiction est inapplicable** |
| *le contrôle* | `la_non_equivalence_est_calculee`, `sans_niveau_declare_aucun_verdict` | Le contrôle est total dès que les deux niveaux sont déclarés, et **il ne rend aucun verdict** sinon — il ne répond pas « équivalentes » |
| *la garde* | `entite_et_territoire_ne_fusionnent_pas` | PR-13 ne dit **rien** de la commutativité micro-macro. La substitution n'est pas une résolution |

`[CONDITION DE RÉFUTATION]` CONV-12 tombe si l'on exhibe une lecture où la non-équivalence porte davantage que la différence de niveau — auquel cas elle cesse d'être calculable et redevient déclarable (option écartée par le porteur).

 Le graphe ne porte **aucune arête `CONV-4 → PR-13`** : une convention ne se dérive pas d'une autre convention, et PR-13 ne porte pas la déclaration. *Les règles rapportées à un « patron CONV-9 » dérivent de **RSO-8** (§A.16.5).* L'arête réelle et vérifiable est **`PR-21 → PR-13`** — c'est un `import`.

### §A.15.6 CONV-13 — le successeur est déclaré à l'inscription

> **CONV-13.** Toute écriture d'obligation déclare, **au moment de l'inscription**, le **successeur** vers lequel l'obligation échoit si son porteur disparaît (faillite, dissolution, décès). Le champ est **obligatoire** ; la valeur `non déclaré` vaut **régime strict** — aucune dévolution — et **ne vaut pas permission de transférer**.

**D'où elle vient.** Le nœud **NC** (non-cessibilité), condition d'existence du palier **PAL-6′** : *« l'obligation inscrite n'est pas transférable ; aucune transition du registre ne substitue un porteur à un autre ; l'extinction est conditionnée à la réalisation vérifiée, jamais au transfert »*. **Portée bornée : l'extinction *par exécution*** est conditionnée à la réalisation vérifiée ; **aucun mode d'extinction n'opère par transfert** ; remise, prescription et disparition de l'objet relèvent du second axe (NT-ARCH §4bis), avec interprète nommé et écriture appariée. **Une dette AX-2 ne s'inscrit jamais en `ETEINTE`** (NT-ARCH §4bis.3). Fondement **AX-2** : une obligation soldable par transfert n'est pas une obligation.

**Pourquoi le champ, et pourquoi à l'inscription — c'est un théorème.** `devolution_libre_reconstitue_la_cession` (PR-11) : **pour tout couple de porteurs, il existe un régime de dévolution sous lequel l'obligation de l'un échoit à l'autre.** Si le successeur pouvait être choisi **au moment de la disparition**, la dévolution reconstituerait exactement la cession que NC interdit. **Le régime doit donc être figé à l'inscription** — la formalisation tranche cette moitié de l'arbitrage sans le porteur.

**Ce que la décision ne met pas en risque.** `obligation_non_cessible` est quantifié sur le régime : le transfert est refusé **pour tout régime de dévolution**. **Le champ successeur déclaré ne peut donc pas affaiblir NC.**

**Ce qu'elle coûte, et qui est démontré.** `regime_strict_bloque_a_la_disparition` et `regime_strict_fige_le_porteur` : sous le régime strict, la disparition du porteur est **refusée**, et aucun événement admis n'en change plus le porteur — l'obligation reste attachée à qui n'existe plus. **Cette contrepartie est une propriété du régime**, et c'est le prix de la valeur `non déclaré`.

`[CONSÉQUENCE OPÉRATOIRE — le registre inscrit l'événement, pas seulement l'état]` `l_effet_ne_distingue_pas_cession_et_devolution` exhibe un transfert **refusé** et une dévolution **admise** qui produisent **exactement la même obligation** ; `l_etat_efface_son_origine` montre que deux porteurs d'origine différents donnent, après dévolution, la même obligation. **La frontière n'est pas dans le résultat, elle est dans l'événement** — un registre qui n'inscrirait que l'état ne pourrait ni distinguer les deux, ni reconstituer la chaîne des porteurs. Exigence établie par PR-11.

`[CONDITION DE RÉFUTATION]` CONV-13 tombe si l'on exhibe un régime de dévolution où le successeur peut être choisi après l'inscription **sans** qu'une cession soit reconstituable.

 *Une obligation envers le milieu peut-elle avoir un héritier ?* CONV-13 impose de déclarer un successeur ; elle ne dit pas qu'il en existe toujours un de légitime. Le set n'a pas posé cette question.

---

---

## §A.16 Les règles de second ordre (RSO) — quatrième classe de nœuds

*Classe instituée par décision du porteur.*

### §A.16.1 Pourquoi cette classe existe

Hors RSO, le set dispose de **trois classes de nœuds** : les **axiomes** (AX-n), constats sur le monde, posés avec fiche et gabarit contradictoire ; les **conventions** ( **toutes les conventions de §A.15.1** ), obligations déclarées portant sur des inscriptions ; les **théorèmes** (ProfReg), conditions de bonne formation démontrées.

**Une famille d'énoncés portants n'entre dans aucune des trois — et ne le peut pas.** Le cas décisif est celui-ci :

> *Un énoncé déclaré selon la forme prescrite devient opposable au même titre qu'un énoncé prouvé.*

C'est la phrase qui donne leur force aux **conventions de §A.15.1, toutes** *(RSO-1 vise toutes les conventions, et toute convention versée ensuite)*, à R0-bis, à R0-ter, et à la maxime *déclarer ce qui ne se calcule pas*. Sans elle, la moitié déclarative du modèle est une documentation sans effet. Or :

- **elle n'est pas un axiome** : elle ne porte pas sur le monde, aucune enquête ne la confirmerait ni ne l'infirmerait ;
- **elle ne peut pas être une convention de plus** : elle est ce qui donne force aux conventions ; l'y ranger serait circulaire ;
- **elle ne peut pas être un théorème** : PR-21 établit au contraire la fragilité du déclaratif — un champ déclaré peut mentir dans les deux sens.

**Elle ne relève donc d'aucune des trois classes**, alors que le set l'invoque à chaque convention. Les autres énoncés de la table §A.16.4 sont dans le même cas. La quatrième classe les loge.

### §A.16.2 Ce qu'est une règle de second ordre

> **Définition.** Une **RSO** est un énoncé qui ne porte ni sur le monde, ni sur la forme d'une inscription, mais sur **ce que les procédures du modèle confèrent** : ce que déclarer produit, ce qu'un examen verbal établit, qui peut valider, ce qui fait d'une source une grammaire. Elle gouverne les autres classes.

**La ligne de partage avec une convention, et elle est nette.** *Une convention oblige une inscription ; une RSO confère un statut à un acte du modèle.* CONV-13 dit qu'une écriture doit déclarer son successeur — elle porte sur une écriture. RSO-1 dit que déclarer oblige — elle porte sur CONV-13.

**Ce que la classe ne fait pas.** Elle ne démontre rien, elle n'ajoute aucune autorité : elle **nomme et localise** des engagements qui opèrent sans relever d'une autre classe. Le gain est de traçabilité, non de fondation. L'écrire autrement serait un `[DÉCOUPLAGE DE RÉGIMES]`.

### §A.16.3 Test d'admission — la triple impossibilité *(obligatoire, jamais vide, jamais par renvoi)*

Une RSO n'est admise que si sa fiche écrit, en toutes lettres, les trois impossibilités :

| | Ce qu'il faut établir |
| --- | --- |
| **(i) Pas un axiome** | L'énoncé ne porte pas sur le monde : nommer l'enquête qui, si elle était conduite, ne le trancherait pas |
| **(ii) Pas une convention** | L'énoncé ne porte pas sur une inscription mais sur le régime des inscriptions : nommer au moins **une convention ou une règle qu'il gouverne** |
| **(iii) Pas un théorème** | Dire **pourquoi il ne peut pas être prouvé** — non pas qu'il ne l'est pas encore. Si la seule raison est « pas encore tenté », ce n'est pas une RSO : c'est un PR à écrire |

**Trois gardes contre le fourre-tout.** Une classe définie par « ce qui n'entre nulle part ailleurs » attire tout. Donc :

1. **La triple impossibilité est écrite, jamais renvoyée.** Une fiche qui dit « voir §A.16.3 » n'est pas instruite.
2. **Toute RSO nomme sa charge portante** : au moins une convention, une règle R-*, un invariant ou une décision d'architecture **désignés par leur nom**, qui tombent avec elle. Une RSO sans charge nommée est une opinion.
3. **Discipline de nombre : la classe est tenue à huit entrées.** Ce n'est pas un invariant mais une **discipline révisable**, du même type que le plafond de douze grammaires. Une neuvième entrée n'est pas interdite : elle oblige à réexaminer si la classe est bien formée, car une classe qui gonfle est une classe mal découpée.

### §A.16.4 La table des règles de second ordre

| ID | Énoncé | Ce qu'elle confère | Charge portante nommée |
| --- | --- | --- | --- |
| **RSO-1** | Un énoncé déclaré selon la forme prescrite est **opposable au même titre** qu'un énoncé prouvé | La force obligatoire du déclaratif |   **toutes les conventions inscrites en §A.15.1** *(vingt)*  ; R0-bis ; R0-ter ; §8sexies NT-ARCH |
| **RSO-2** | La **suspension tracée** d'une valuation empêche cette valuation d'opérer | L'existence d'un usage descriptif du MRC | R0-bis en entier ; quintuplet du statut du seuil ; indicateur I-4 |
| **RSO-3** | Une vérification **verbale** établit un couplage, à la condition expresse de ne jamais se dire preuve | La validité du régime procédural | Table canal→grammaire §A.7 ; plafond de douze grammaires ; clôture de C-Q7 ; CONV-2 |
| **RSO-4** | Il existe des instruments **sans engagement normatif réfutable propre** ; une source est une grammaire ssi elle en pose un et qu'il est transversal | La partition méthode / grammaire | Existence de l'annexe méthodologique ; §A.9 ; statut de R0-bis et R0-ter hors plafond |
| **RSO-5** | Le renvoi entre couches circule **dans un seul sens** : une couche haute consomme un invariant, ne le redéfinit jamais | La propagation du formel vers les fiches | §B.2 ; invariants ACT-ARCH-001 ; toute la stratification 0-1-2-3 |
| **RSO-6** | Un porteur unique peut tenir conception et validation **tant que l'incohérence est déclarée et que la classe est périmable** | La validité des actes de porteur en régime mono-porteur | Clôture des douze grammaires ; table canonique §A.15 « fait foi » ; sept arbitrages de charge valuative mixte ; clôture de C-Q7 |
| **RSO-7** | Le **cadrage situé** d'un chercheur est déclarable sans vider l'analyse, et reprenable par le collectif | L'existence de R0-ter | R0-ter ; protocole §A.8 (I-1, I-2, I-5) ; bascule Usage 2 → Usage 3 |
| **RSO-8**  | Le **non-déclaré refuse, il n'autorise pas** : l'absence de déclaration d'un champ obligatoire vaut **refus** de l'effet que la déclaration aurait conditionné — jamais permission, jamais valeur par défaut favorable | La valeur procédurale du silence | CONV-8, CONV-9, CONV-12, CONV-13 ; `etat_extinction = NONDECLARE` (NT-ARCH §4bis.3) ; habilitations ; `creance_repartissable = NONDECLARE` (NT-ARCH §8.5.6) |

 **Huit entrées** : **la discipline de huit est atteinte**. Toute neuvième entrée oblige au réexamen de §A.16.3, point 3. R-TRAÇAGE, R-PRÉSENT et R-VERSION n'y entrent pas : ce sont des règles d'édition du set (§A.19), qui portent sur le texte du modèle, non sur ce que ses procédures confèrent aux écritures d'un registre.

### §A.16.5 Instruction de chaque règle

**RSO-1 — l'opposabilité de la déclaration.**
*(i) Pas un axiome* : aucune enquête sur des dispositifs ne dirait si déclarer oblige — c'est une règle du modèle, pas un fait du monde. *(ii) Pas une convention* : elle gouverne **toutes les conventions de §A.15.1** , et les y ranger serait circulaire. *(iii) Pas un théorème* : ProfReg quantifie sur des écritures ; l'opposabilité d'un énoncé n'est pas une propriété d'écriture, et **PR-21 travaille contre** — `champ_declare_peut_mentir` établit qu'un déclaratif doublant un calcul peut mentir dans les deux sens.
`[CONDITION DE RÉFUTATION]` RSO-1 tombe si l'on exhibe une inscription conforme à une convention dont le non-respect **n'emporte aucune conséquence procédurale** : le déclaratif n'y obligerait pas, il informerait.
`[PORTÉE]` RSO-1 dit que la déclaration oblige ; elle **ne dit pas qu'elle dit vrai**. PR-21 reste entier : l'opposabilité n'est pas la véracité.
`[PORTÉE — conventions d'institution]` Pour une convention de statut **Institution** (CONV-16, 17, 18), RSO-1 confère l'opposabilité **dans le registre** : ses effets du défaut (§A.15.11) s'appliquent. Elle ne confère **ni** l'autorité de l'instance désignée, qui tient à sa **désignation arrêtée** par les registres (CONV-16), **ni** la force d'un dossier devant un tiers extérieur, qui tient à la **voie** (CONV-17, « ce que CONV-17 ne dit pas » (i)).

**RSO-2 — la suspension tracée neutralise.**
*(i) Pas un axiome* : c'est l'effet d'un acte d'inscription, non un constat. *(ii) Pas une convention* : R0-bis *est* la convention ; RSO-2 est ce qui la rend efficace. *(iii) Pas un théorème* : PR-10 démontre l'obligation de **déclarer** le statut du seuil ; aucun théorème ne peut établir que déclarer **suffise à suspendre** — ce serait mesurer l'effet d'un acte sur une portée normative, hors du domaine du formalisme.
`[CONDITION DE RÉFUTATION]` RSO-2 tombe si l'on documente un usage où un seuil déclaré suspendu a **néanmoins** produit un effet normatif sur les acteurs — le pilote §A.8 est le lieu de ce test.
`[RÉSERVE]` C'est la RSO la plus exposée empiriquement, et **la seule que le protocole pilote peut réellement tester.**

**RSO-3 — ce qu'établit une vérification verbale.**
*(i) Pas un axiome* : porte sur une méthode, non sur le monde. *(ii) Pas une convention* : elle gouverne CONV-2 (commutativité procédurale). *(iii) Pas un théorème* : par construction — un théorème est ce que la vérification verbale n'est pas ; prétendre le prouver serait le `[DÉCOUPLAGE DE RÉGIMES]` que la règle elle-même interdit.
`[CONDITION DE RÉFUTATION]` RSO-3 tombe si un couplage vérifié verbalement et tenu pour établi est **ensuite réfuté par sa formalisation**. `[PRÉCÉDENT DÉFAVORABLE — et il est lourd]` C'est **exactement ce qui s'est produit trois fois** : le carré M↔R, le couplage E↔A et le carré J↔E étaient tenus pour acquis en régime procédural, et les trois ont été réfutés par leur formalisation (PR-5, PR-9, VJE). **RSO-3 est donc la règle de second ordre la plus affaiblie du set**, et il faut l'écrire : ce qui a été vérifié verbalement et jamais formalisé n'est pas garanti — le plafond de douze grammaires est dans ce cas.

**RSO-4 — la partition méthode / grammaire.**
*(i) Pas un axiome* : c'est un critère de tri, non un fait. *(ii) Pas une convention* : elle décide ce qui entre au set. *(iii) Pas un théorème* : aucun théorème ne quantifie sur des sources.
`[CONDITION DE RÉFUTATION]` RSO-4 tombe si l'on montre qu'un instrument versé à l'annexe **pose en fait un engagement normatif réfutable propre** — auquel cas il est une grammaire clandestine et le plafond de douze est faux.
`[TENSION DÉCLARÉE]` **G-PERFORMATIVITE pose que tout instrument produit ce qu'il prétend mesurer.** Un tel instrument peut-il ne porter « aucun engagement normatif propre » ? La tension est réelle, elle n'est pas tranchée, et elle vise directement le statut hors plafond de R0-bis et R0-ter. `[INCOHÉRENCE INTER-COUCHES — niveau 1, déclarée.]`

**RSO-5 — l'unidirectionnalité du renvoi.**
*(i) Pas un axiome* : règle d'architecture. *(ii) Pas une convention* : elle gouverne où les conventions peuvent vivre. *(iii) Pas un théorème* : §8 de NT-ARCH le dit lui-même — « les théorèmes Lean quantifient sur des types, non sur des numéros de couche ». La stratification est **hors de portée du formalisme qui la valide**.
`[CONDITION DE RÉFUTATION]` RSO-5 tombe si une fiche de Couche 2 redéfinit localement un invariant de Couche 1 sans que le set le détecte — c'est-à-dire si le marqueur `[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ]` n'est pas déclenché par un cas réel.

**RSO-6 — le régime mono-porteur, et sa péremption.**
*(i) Pas un axiome* : porte sur le modèle, non sur le monde. *(ii) Pas une convention* : elle valide les actes par lesquels les conventions sont adoptées. *(iii) Pas un théorème* : aucun formalisme ne décide de la légitimité d'un validateur.
`[CONDITION DE PÉREMPTION — et c'est ce qui distingue RSO-6 des autres]` **RSO-6 est périmable par construction : elle cesse de valoir le jour où la communauté de gestion est instituée.** Elle n'est pas une règle du modèle mais une règle de sa période de constitution, et son maintien au-delà de ce jour serait une faute et non une continuité.
`[TENSION AVEC AX-7, DÉCLARÉE]` **AX-7 pose que le seuil est arrêté par les personnes auxquelles il s'applique.** Appliqué au MRC lui-même, AX-7 contredit RSO-6. Le set applique donc AX-7 aux dispositifs qu'il décrit et non à lui-même. **Cette asymétrie est inscrite** ; elle n'est pas résolue. `[INCOHÉRENCE INTER-COUCHES — niveau 2.]`

**RSO-7 — la déclarabilité du cadrage situé.**
*(i) Pas un axiome* : porte sur ce qu'un acte de déclaration peut atteindre. *(ii) Pas une convention* : R0-ter est la convention, RSO-7 est sa condition de possibilité. *(iii) Pas un théorème* : l'exhaustivité d'une auto-description n'est pas une propriété formalisable dans ProfReg.
`[CONDITION DE RÉFUTATION]` RSO-7 tombe si le pilote montre qu'un cadrage déclaré conforme **laisse un résidu opérant** que le collectif ne peut pas reprendre.

**RSO-8 — le non-déclaré refuse, il n'autorise pas.**
*(i) Pas un axiome* : elle porte sur l'effet d'un acte — ne pas déclarer —, non sur le monde. *(ii) Pas une convention* : elle **gouverne** CONV-8, CONV-9, CONV-12 et CONV-13, et les règles nommées dans la table ; la ranger parmi elles ferait des règles dérivées d'un « patron CONV-9 » des conventions tirées d'une convention, ce que le set interdit : une convention ne se dérive pas d'une autre (§A.15). *(iii) Pas un théorème* : `nonDeclare_ne_vaut_pas_permission` (PR-17), `niveau_non_declare_ne_vaut_pas_permission` (PR-13) et `regime_non_declare_ne_vaut_pas_permission` (PR-12) en sont les **ombres formelles** — chacun établit que *son* modèle refuse sur `NONDECLARE` ; aucun n'établit que le set **doit** refuser, ce qui porterait sur ce que la procédure confère.
`[CONDITION DE RÉFUTATION]` RSO-8 tombe si l'on documente un champ obligatoire dont le silence, traité comme refus, **fait perdre une obligation réelle qu'aucun autre canal ne porte** — c'est-à-dire si refuser sur le non-déclaré coûte davantage qu'il ne protège.
`[RANG]` RSO-8 est versée **à côté** de RSO-1, non sous elle (§A.16.6, contrainte d'ordre) : le refus qu'elle confère ne dépend pas de l'opposabilité d'une déclaration — il porte précisément sur son absence.
`[PORTÉE]` RSO-8 dit que le silence ne vaut pas permission ; elle ne dit pas **ce qui doit être déclaré** — chaque convention le dit pour son champ. **Tension à suivre** : CONV-15 inscrit une paire F4 incohérente **avec un marqueur**, sans refus ; RSO-8 vise l'**absence** de déclaration, CONV-15 une déclaration **incohérente** — les deux régimes ne se recouvrent pas, mais la frontière n'a été éprouvée sur aucun cas. *Même lecture pour **CONV-7** au marqueur : ce que RSO-8 refuse est l'effet — la bonne formation, l'opposabilité —, non l'inscription (§A.15.10).*
`[TENSION AVEC AX-1 ET AX-10, DÉCLARÉE]` Si les dépendances d'un collectif **échappent à ses liens de connaissance et de soin** (AX-1 v2) et si son attention est **située et organisée par des dispositifs** (AX-10), l'exhaustivité d'une auto-déclaration de cadrage est précisément ce qu'on ne doit pas attendre. **Deux axiomes du set travaillent contre une de ses règles** : c'est une raison du marqueur `[PLAUSIBLE, NON VÉRIFIÉ]` que porte R0-ter.

### §A.16.6 La circularité — ce que la classe en fait, et ce qu'elle n'en fait pas

**Il faut l'écrire sans l'atténuer.** RSO-1 pose que déclarer confère l'opposabilité. La classe RSO est créée **par une déclaration**. RSO-1 se fonde donc elle-même : `[RAISONNEMENT AUTORÉFÉRENTIEL]`.

**La classe ne dissout pas cette circularité. Elle ne le peut pas** — aucun dispositif ne peut fonder de l'intérieur ce qui lui donne force, et le prétendre serait exactement la faute que le régime de vérifiabilité-cohérence interdit.

**Ce que la classe fait, et c'est réel :**

| Sans la classe | Avec la classe |
| --- | --- |
| La circularité est **dispersée** — un peu dans chaque convention, dans R0-bis, dans chaque clôture de porteur | Elle est **localisée en un point**, RSO-1, et nommée |
| Elle est **invisible** : rien ne dit que la force du déclaratif est postulée | Elle est **déclarée**, avec sa condition de réfutation |
| Elle est **sans porteur** : aucun énoncé ne peut être contesté, faute d'exister | Elle est **contestable** : un lecteur peut viser RSO-1 |

> **Le gain est de traçabilité, pas de fondation.** Le MRC ne s'en justifie pas mieux ; il dit où il ne se justifie pas. C'est précisément ce que le régime demande — et c'est tout ce qu'il demande.

**Ce qui fonde réellement RSO-1 est extérieur au set** : c'est le fait institutionnel, largement attesté, que des régimes déclaratifs obligent — droit des sociétés, normes comptables, déclarations environnementales. **Ce rattachement n'est pas instruit** : il ferait de RSO-1 un candidat axiome de la famille « constats institutionnels », ce qui déplacerait le problème sans le supprimer, puisqu'il faudrait alors expliquer pourquoi le MRC hérite de cette force.

**Trois compléments** :

- **(i) AX-7 × RSO-6 se reproduit.** La tension déclarée en §A.16.5 (RSO-6 : *le set applique AX-7 aux dispositifs qu'il décrit, non à lui-même*) **reparaît** dans deux règles décidées par le porteur seul et appuyées sur AX-7 : la **branche D** et la **règle du seul débiteur** (NT-ARCH §4bis.3, *Rattachements* — AX-7 y est « un appui doctrinal, non une garantie »). Même asymétrie, deux occurrences de plus. **Aucune résolution n'est proposée** : RSO-6, périmable, en est la borne.
- **(ii) Aucune dérivation par « patron CONV-9 ».** Les règles relatives à l'extinction `NONDECLARE`, aux habilitations et à `creance_repartissable` dérivent de **RSO-8** (§A.16.4-5), qui confère le refus au silence, et non d'une convention : une convention ne se dérive pas d'une autre, et CONV-9 est une convention parmi d'autres.
- **(iii) Contrainte d'ordre.** *Aucune RSO n'est versée sous une autre RSO sans redéfinition de la classe* : §A.16.2 définit une RSO comme gouvernant les autres classes, non une RSO. RSO-8 est donc versée **à côté** de RSO-1. Conséquence : **R-TRAÇAGE** ne peut être versée comme une RSO qui tomberait sous RSO-1 — le rang est interdit.

### §A.16.7 Ce que cette classe change, et ne change pas

**Change.** Le graphe de dépendances a une quatrième classe de nœuds. Les énoncés de la table §A.16.4 sont inscrits, chacun avec sa condition de réfutation. **Quatre tensions internes** sont tracées : RSO-3 contre les trois réfutations de formalisation ; RSO-4 contre G-PERFORMATIVITE ; RSO-6 contre AX-7 ; RSO-7 contre AX-1+AX-10.

**Ne change pas.** Aucun théorème, aucun axiome, aucune convention. Le décompte ProfReg est inchangé. **Aucune RSO n'est démontrée** et aucune ne le sera : c'est leur définition.

### §A.16.8 `[LACUNES ET LIMITES DE CETTE SECTION]`

- **Les sept entrées viennent d'un audit dont la passe sur les douze grammaires était superficielle.** D'autres règles de second ordre peuvent y dormir. La discipline de huit est donc à la fois une garde et un pari.
- **RSO-3 est versée en sachant qu'elle est affaiblie** par trois précédents défavorables. La verser affaiblie plutôt que de ne pas la verser est un choix : le set préfère une règle inscrite avec son passif à une pratique non inscrite.
- **La distinction convention / RSO est nette en principe et ne l'a pas été testée sur un cas limite.** CONV-2 (commutativité procédurale) est le candidat le plus proche de la frontière : elle pourrait se lire comme une RSO. Elle est maintenue en convention, faute de raison décisive. `[À CONTRÔLER]` *CONV-2 porte deux carrés (§A.15.9) : le cas limite est doublé, non tranché.* **CONV-16** : « seule elle arbitre l'écart » confère un statut à l'acte de l'instance, ce qui est la marque d'une RSO ; elle est maintenue en convention (statut **Institution**, §A.15), faute de raison décisive. `[À CONTRÔLER]`
- **Aucune des sept n'a de gabarit contradictoire** au sens des fiches d'axiomes — défenseurs, objecteurs nommés, réponses. Elles ont une condition de réfutation, ce qui est moins. `[DETTE DE MÉTHODE DÉCLARÉE.]`
- **RSO-6 n'a pas de date de péremption**, seulement un événement déclencheur — l'institution de la communauté de gestion — dont rien ne garantit qu'il survienne. Une règle transitoire sans terme est une règle permanente qui s'ignore.

### §A.15.7 CONV-14 — l'échelle de communalité ne s'agrège pas

> **Ancrage compilé** : PR-27 `le_score_ne_determine_pas_les_axes` — deux profils qui diffèrent sur chacun des trois axes ont le même score agrégé. Non-implication : le score ne permet pas de retrouver les axes. *Ancrage de forme, non preuve de la convention : une convention se déclare.* Même lot : PR-27 `fraction_exhibe_une_source_eventuellement_vide` établit que l'obligation compilée de CONV-4 **admet une source vide** — l'écart entre la convention (source déclarée **et vérifiable**) et ce que ProfReg établit est un théorème.

**Énoncé.** *La communalité d'une chose se qualifie sur plusieurs axes juridiques distincts — au moins l'**intérêt commun** et l'**inclusivité** — et selon les **instances** où elle se manifeste (attributaire, délibérative, de contrôle). **Ces axes se déclarent séparément. Aucun score composite n'en est dérivé. Aucun classement n'est établi entre des choses relevant de régimes juridiques différents.***

**Pourquoi elle est déclarée et non calculée.** Parce que sa source l'exige, et au verbatim. Le rapport Rochfeld-Cornu-Martin écrit que *« Il ne s'agit pas d'une **mesure quantitative, mais juridique** »*, et que *« l'objectif de l'échelle de communalité n'est alors **pas de proposer un classement** dans la communalité des choses, **classement qui n'aurait aucun sens** en ce qu'il supposerait qu'il existe un modèle idéal (et qui obligerait à comparer des rapports juridiques qui présentent des caractéristiques **irréductiblement différentes**) »*.

> **CONV-14 est la seule convention du set dont la source interdit explicitement le calcul qu'elle interdit.** Les autres tirent leur nécessité de l'architecture du MRC ; celle-ci est **imposée de l'extérieur** par les auteurs de l'instrument que le MRC emprunte.

**Ce qu'elle sanctionne.** Un score composite de communalité — tel le champ `degre_communalité : Score 1-5`, suspendu en NT-G6 et absent de NT-ARCH F6.2 — et le conditionnement du niveau de protection de C-DROITS par un tel score.

**Patron.** Celui de **CONV-12** : *déclarer les niveaux, ne pas fabriquer l'équivalence.* CONV-12 laisse la non-équivalence se **calculer** ; **CONV-14 va plus loin : elle interdit jusqu'au calcul de comparaison**, parce que les termes ne sont pas commensurables en droit.

`[CONDITION DE RÉFUTATION]` CONV-14 tombe si l'on montre que les axes de la communalité juridique **ne sont pas déclarables séparément** — si qualifier un commun sur l'un contraint mécaniquement sa qualification sur l'autre, l'axe unique était le bon découpage.

> **Exercice de la condition sur témoins (ProfReg).** Premier sens, sur l'instance attributaire : l'intérêt commun ne détermine pas l'inclusivité (PR-58, `l_interet_commun_ne_determine_pas_l_inclusivite` ; PR-59, `le_premier_sens_porte_sur_l_attributaire`). Second sens, sur l'instance de contrôle : l'inclusivité ne détermine pas l'intérêt commun (PR-59, `l_inclusivite_du_controle_ne_determine_pas_l_interet_commun`). **L'instance délibérative reste sans témoin** dans la source (NT-G6 §2.1) : sur elle, la condition n'est pas exercée. *Témoins de forme, non preuve de la convention : une convention se déclare.*

`[PORTÉE]` CONV-14 interdit l'agrégation ; **elle n'interdit pas la comparaison de deux choses sur un même axe**, qui reste possible et sensée. Ce qu'elle refuse est le score composite et le classement inter-régimes.

### §A.15.8 CONV-15 — co-obligation de l'appel immanent et de la puissance affirmative

`[HOMONYMIE DÉCLARÉE]` **A2 et A3 désignent ici les amendements A2 et A3 de NT-G2** — l'appel immanent (`appelimmanent`, V1 : Jonas 1979) et la puissance affirmative (`puissanceaffirmative`, Morizot & Neyret 2026, amendement A3) —, **et non les axiomes AX-2 (dette non soldable) et AX-3 (avaries communes)** de §A.18. Le set emploie les mêmes sigles pour les deux ; la présente convention écrit toujours « amendement A2 / A3 de NT-G2 ».

**Énoncé.** *(i) **Co-obligation de déclaration.** Toute inscription F4 qui déclare l'appel immanent d'un acteur déclare aussi sa puissance affirmative, et réciproquement ; l'une sans l'autre est **incomplète**, et le silence sur l'une ne vaut pas cohérence (patron CONV-9, CONV-13). (ii) **Cohérence.** La paire est **cohérente** si l'appel immanent est non nul exactement quand la puissance affirmative est sous son seuil critique. (iii) **Marqueur, jamais refus.** Une paire **non cohérente** ou **incomplète** **s'inscrit**, et porte le marqueur `[PAIRE F4 NON COHÉRENTE]` (R0-bis : marqueur, non sanction). Les deux verdicts de protection — celui de R-HABITABILITE-CAPABILITE et celui de R-PUISSANCEAFFIRMATIVE — sont alors **inscrits l'un et l'autre** ; aucun n'efface l'autre.*

**Ce qui est compilé, et ce qui ne l'est pas.** `V1_commute_ssi_coherence` établit que, pour un même acteur, les deux règles rendent **le même verdict si et seulement si** la paire est cohérente : le marqueur se lève donc **exactement** là où la commutation F4↔F6 ne vaut pas, et il est **calculable** — c'est un contrôle, non un champ déclaré (PR-21). `V1_commutatif` lit la cohérence dans le type `ActeurF4Coherent` ; **ce type décrit le domaine sans marqueur, il n'interdit pas l'inscription d'une paire non cohérente** (la présente convention le précise ; V1 le rappelle en commentaire). `V1_coherence_discrimine` exhibe une paire non cohérente dont les verdicts divergent. **Non compilé** : la co-obligation (i) et le marqueur lui-même.

**Pourquoi un marqueur et non un refus** (décision de porteur). Refuser une paire non cohérente ferait disparaître du registre **précisément** les cas où l'habitabilité et la puissance affirmative d'un même acteur se contredisent — ceux qu'il importe de voir. Le marqueur les rend visibles sans les exclure.

 **Lequel des deux verdicts de protection s'applique** à une paire marquée : CONV-15 inscrit les deux et ne choisit pas. Une règle de priorité (par exemple : la protection s'applique dès que l'une des deux règles la déclenche) relève d'une décision distincte.

*Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* toute inscription F4 qui déclare l'un des deux termes déclare l'autre ; le marqueur est levé sur les seules paires dont les deux verdicts diffèrent, ou dont un terme manque — ce qui se vérifie par calcul. `[CONDITION DE RÉFUTATION]` CONV-15 tombe si l'on documente, sur des cas, que l'appel immanent et la puissance affirmative d'un même acteur portent **sur des objets distincts** (un milieu d'un côté, une capacité d'agir d'un autre acteur de l'autre), de sorte que les déclarer ensemble **fabrique** un couplage au lieu de l'enregistrer : la co-obligation serait alors un appariement forcé.

---

### §A.15.9 CONV-2 étendue — le carré B1↔B2 *(décision du porteur)*

**Énoncé.** La commutativité du carré B1↔B2 — en régime SYSTEMIQUE, le chemin direct et le chemin par la phase INVENTAIRE-ASSETS-ACTIFS aboutissent à la même phase, DELIBERATION — est **procédurale**. Elle porte sur la **phase d'aboutissement**, **jamais sur une dispense d'inventaire**.

**Pourquoi la clause.** En régime SYSTEMIQUE/HYBRIDE, la phase d'inventaire est **déclenchée** (NT-ARCH §5.1, « Déclenchement : regimeobligation = SYSTEMIQUE/HYBRIDE ») et la clôture sans inventaire est **interdite** (PR-4, `cloture_interdite_sans_inventaire`). Le « chemin direct » de `V3Verification` n'est donc **pas admissible** en régime SYSTEMIQUE : `V3_commutatif` compare un chemin licite à un chemin qui ne l'est pas, et ne l'établit que par construction (les deux branches systémiques de `chemin_direct` sont identiques — forme 1). Lue sans la clause, la formule « l'inventaire est une étape transparente vers DELIBERATION » (Note d'amendements, mai 2026) produirait une `[INCOHÉRENCE INTER-COUCHES]` avec §5.1 ; la clause la prévient.

**Couche 2.** *Porteur* : le porteur MRC. *Horizon* : v6 (2-cellule, comme le carré triangulaire). *Critère réfutable* : une fiche SYSTEMIQUE qui atteint DELIBERATION **sans inventaire clos non vide**, ou qui **n'atteint pas** DELIBERATION après un inventaire clos, rompt la commutation ; le premier cas relève en outre de PR-4.

**Appuis.** `V3_aboutit_deliberation` et `V3_actoriel_inchange` (lectures licites à témoins croisés — R-7) ; PR-4 et `inventaire_nonempty_discrimine` pour le passage obligé. **PR-51** (`ProfReg/PR51_CarreB1B2.lean`) démontre la commutation sur les seuls chemins admissibles : la règle des pas entre phases est déclarée, puis `aucune_deliberation_sans_inventaire` et `carre_B1B2_commute_sur_les_chemins_admissibles` (résultats) en concluent que deux chemins admissibles qui atteignent DELIBERATION passent tous deux par l'inventaire ; le chemin direct n'est pas admissible (`le_chemin_direct_n_est_pas_admissible`). CONV-2 reste une convention : la règle des pas est déclarée, non démontrée. `V3_commutatif` est conservé comme **lecture des deux définitions**, jamais appui.

**Frontière CONV / RSO.** Ce carré ajoute un second cas au candidat frontière signalé (lacunes de §A.16) ; CONV-2 reste une convention.

### §A.15.10 Conditions de réfutation de CONV-2, 3, 4, 6, 8 ; CONV-7 au marqueur ; ancrages PR-28

 *Formulations reprises sans modification de `ProfReg/Instruction_Suites_Audit_Axiomes_Conventions_RSO_2026-09-28.md` §2.*

**Conditions de réfutation** *(patron CONV-11, §A.15.4)* :

| Conv. | Condition de réfutation |
| --- | --- |
| **CONV-2** | *(carré B1↔B2 : §A.15.9)* — carré triangulaire : **CONV-2 tombe si** une fiche traversant NT-G7 → NT-G2 → NT-ARCH par les deux chemins aboutit à **deux statuts d'obligation différents** sans que l'écart soit tracé ; ou si une 2-cellule formelle (G.9.3) est produite et contredit la commutation                                                                       |
| **CONV-3** | **tombe si** l'on documente une écriture dont le régime d'obligation **ne peut pas** être déclaré à l'inscription sans la fausser — le repli serait alors un `NONDECLARE` explicite, non l'absence du champ                                                                                                                                                                             |
| **CONV-4** | **tombe si** une source satisfaisant les quatre propriétés (désignation, résolution, intégrité, porteur) s'avère **invérifiable par un tiers**, ou si une source privée de l'une d'elles l'est — les quatre propriétés ne seraient pas le bon critère                                                                                                                                   |
| **CONV-6** | **tombe si** une écriture engageant au-delà de l'exercice est correctement évaluée **sans** représentation prospective (cas documenté)                                                                                                                                                                                                                                                  |
| **CONV-8** | **tombe si** un seuil `NONDECLARE` peut être traité **sans** délibération sans produire d'attribution arbitraire (cas documenté)                                                                                                                                                                                                                                                        |

**CONV-7 — le marqueur plutôt que le refus.** *Décision du porteur : « comme pour CONV-15, le marqueur plutôt que le refus ».*

> **CONV-7.** Une inscription dont la condition de réfutation est **obligatoire** (légitimité `PRATIQUE` ou `planetaireNonDesignee`, NT-ARCH §5.2) et **absente** est **inscrite avec le marqueur `[CONDITION DE RÉFUTATION ABSENTE]`** ; elle n'est pas refusée. Le marqueur la rend identifiable et contestable ; **il ne la valide pas** : l'inscription marquée n'est pas bien formée au sens de PR-8, et **ne peut pas servir d'appui**. *Justification par le critère §A.15.11* : l'inscription a un objet (branche 1 non satisfaite), le défaut n'est pas une valeur simulée (branche 2), il ne porte ni sur un objet qui en conditionne d'autres (branche 3 — c'est le cas du **régime**, non de l'écriture) ni sur l'attribution (branche 4) ; il porte sur un **terme d'appréciation** : branche 5, marqueur. **Horizon du marqueur.** Le marqueur porte **un critère de sortie** — la pièce qui portera la condition de réfutation, et qui la déclarera — **ou une clause de caducité** ; à défaut de déclaration, la **caducité par défaut** est la version suivante du set (v5.7), comme pour un régime `CANDIDAT_NON_INSTANCIABLE`. Un marqueur a donc toujours un terme. À l'échéance, sans condition déclarée, il devient `[CONDITION DE RÉFUTATION ABSENTE — CADUQUE]` : l'écriture **reste au registre**, elle **ne peut plus être complétée** ; une condition de réfutation ultérieure exige une nouvelle écriture qui cite la première. `[MODALITÉ DE CADUCITÉ RETENUE PAR L'INSTRUCTEUR — révisable]` *Ancrage PR-32 :* `le_marqueur_a_toujours_un_horizon`, `marqueur_temoin_discriminant`.

- **Articulation avec RSO-8** (« le non-déclaré refuse, n'autorise pas ») : RSO-8 refuse **l'effet** que la déclaration aurait conditionné, non l'inscription. Sous CONV-7, ce qui est refusé à l'inscription marquée est la **bonne formation**, donc l'opposabilité comme inscription conforme (RSO-1 ne s'y applique pas) ; elle reste **au registre**, visible et contestable. Les deux règles se composent sans se contredire.
- **Ancrage** : PR-8 `le_marqueur_se_leve_exactement_sur_le_defaut` — le marqueur se lève **exactement** quand la réfutation est obligatoire et la condition absente (caractérisation, patron `V1_commute_ssi_coherence` de CONV-15). `bien_formee_sans_refutation_n_est_pas_obligee` : rien n'est « bloqué ».
- `[CONDITION DE RÉFUTATION]` **CONV-7 tombe si** l'on documente des inscriptions marquées `[CONDITION DE RÉFUTATION ABSENTE]` qui, faute de refus, **sont reprises comme appui sans que le marqueur soit lu** — c'est-à-dire si le marqueur ne protège pas contre l'usage qu'un refus aurait empêché.
- **Homologie** : `CANDIDAT_NON_INSTANCIABLE` est le marqueur de CONV-7 au niveau des régimes (inscrit, sans effet, avec horizon) ; le marqueur d'écriture porte de même un horizon (ci-dessus). NT-ARCH §8.4 ; PR-32.
- La **règle d'admission au registre des régimes** (NT-ARCH §8.4 : « un régime dont la condition de réfutation est vide n'est pas inscrit — sauf sous le statut `CANDIDAT_NON_INSTANCIABLE` ») **garde le refus**. Elle porte sur l'admission d'un **régime** au registre, non sur une **écriture** : CONV-7 ne la modifie pas. L'alignement éventuel des deux régimes est une décision distincte, **non prise**.

**Ancrages compilés — PR-28** (`PR28_AncragesConventions.lean`, 9 théorèmes, aucun axiome) — *une convention se déclare ; ces théorèmes établissent la forme de l'obligation, non sa justesse* :

| Conv. | Théorème | Rôle |
| --- | --- | --- |
| **CONV-8** | `nondeclare_force_deliberation` | **moitié positive** : sous la règle déclarée, un seuil `NONDECLARE` ne rend accessible que la délibération (patron `V10a_planetaire_force_deliberation`) |
| CONV-8 | `CONV8_temoin_discriminant` | la règle exclut un contexte ; un seuil déclaré laisse le niveau critique accessible |
| **CONV-6** | `BienFormee_ne_borne_pas_la_prospective` | **le trou** : la bonne formation de PR-8 ne porte pas CONV-6 |
| CONV-6 | `CONV6_est_satisfiable` | satisfiabilité |
| CONV-6 | `CONV6_ne_vaut_pas_dans_l_exercice` | garde de portée (lecture R-7, n° 70) |
| **CONV-4** | `CONV4_satisfaite_sans_DID` | le bornage de CONV-4 est satisfiable sans DID |
| CONV-4 | `source_sans_porteur_mal_formee` | la clause du porteur **mord** |
| CONV-4 | `CONV4_ne_prescrit_aucune_forme` | garde : toute forme de désignation est compatible |
| **CONV-14** | `la_comparaison_sur_un_axe_n_est_pas_le_classement` | garde de portée : la comparaison sur un axe porte une information que le score ne donne pas (autre ancrage : PR-27) |

`[RÉSERVE DE MODÈLE]` « Engager au-delà de l'exercice » est lu comme un horizon autre qu'`institutionnel` ; les quatre propriétés de CONV-4 sont des champs optionnels renseignés ou non — la **vérifiabilité** d'une source n'est pas modélisée.

`[LACUNES ET LIMITES]` Les cinq conditions et celle de CONV-7 n'ont été confrontées à aucun cas. La modalité de caducité du marqueur n'a été confrontée à aucun cas.

### §A.15.11 L'effet du défaut d'une condition de bonne formation — critère

 *Instruction : `ProfReg/Note_Critere_Refus_Marqueur_2026-09-28.md`. Le porteur retient le critère implicite qu'elle dégage, et l'ordre de ses branches.*

**Ce que le critère règle.** Quand une condition de bonne formation n'est pas satisfaite, le défaut produit un effet. Le critère dit lequel. Il s'applique **dans l'ordre**, et la première branche satisfaite fixe l'effet :

| Ordre | Branche | Effet | Exemples |
|---|---|---|---|
| 1 | **Pas d'objet** : sans le terme manquant, l'écriture ne qualifie rien — pas de miroir, pas d'ancrage, pas de primitive constitutive | **refus d'inscription** | violation de R1 ; écriture T sans ancrage ; **CONV-3** |
| 1bis | **L'inscription est elle-même le dommage** : la règle protège contre l'enregistrement même — donnée sensible sans base de légitimité, support irréversible ; inscrire puis marquer réaliserait ce que la règle prévient | **refus d'inscription** | **CONV-20** *(décision du porteur, 12/10/2026)* ; **CORPUS\_NON\_CONSENTI** *(décision du porteur, 29/10/2026)* |
| 2 | **Non-déclaration renommée** : une valeur simule une déclaration | **refus d'inscription** (RSO-8) | « sans objet » non motivé |
| 3 | **Objet qui en conditionne d'autres** : régime, table, référentiel | **refus d'inscription**, sauf statut candidat à horizon (`CANDIDAT_NON_INSTANCIABLE`) | régime sans condition de réfutation |
| 4 | **Attribution** : le défaut porte sur qui porte, répartit ou représente | **inscrite, mal formée, phase DÉLIBÉRATION** | CONV-8 ; P7 ; AX-3 ; P5 |
| 5 | **Terme d'appréciation** : l'objet existe, un terme qui permet de l'apprécier ou de le contester manque | **inscrite avec marqueur** — jamais une sanction (patron R0-bis) | **CONV-7** ; interprète manquant ; extinction sans interprète |

**L'ordre compte.** Un même défaut peut relever de deux branches. Les branches de refus (1 à 3, 1bis comprise) portent sur **l'inscription elle-même** et passent avant celles qui portent sur **son traitement** (4 et 5). CONV-3 en est le cas d'école : le régime d'obligation dit aussi qui porte (branche 4), mais il est d'abord **constitutif** du côté d'écriture (branche 1).

**Codes de l'effet du défaut** *Toute condition de bonne formation du set cite son code. Une règle qui n'en cite pas et dont l'effet n'est pas écrit est un **E0**, défaut de rédaction, à classer par le critère.*

| Code | Effet | Écriture au registre | Bien formée | Source dans le critère |
|---|---|---|---|---|
| **E1** | refus d'inscription | non | — | branches 1, 1bis, 2, 3 |
| **E2** | mise en attente, remontée au porteur | en suspens | — | **hors critère** : le défaut est dans le **référentiel** (lacune de table, **arbitrage A8** — non l'axiome AX-8), non dans l'écriture |
| **E3** | mal formée, phase DÉLIBÉRATION | oui | non | branche 4 |
| **E4** | mal formée, marquée | oui | non | branche 5, quand le terme manquant est une **condition de bonne formation** |
| **E5** | bien formée, marquée | oui | oui | branche 5, quand la règle déclare l'écriture bien formée **et** lui adjoint une réserve |
| **E6** | qualification dérivée refusée ou `INDETERMINE` | oui | oui | **hors critère** : porte sur ce qu'on tire de l'écriture |
| **E7** | requalification de la valeur | oui | selon le cas | **hors critère** : *idem* |
| **E0** | effet non écrit | — | — | défaut de rédaction |

**Classement de référence** *(inventaire de la note ; les règles qu'il ne couvre pas sont E0 jusqu'à classement)* :

| Code | Règles |
|---|---|
| E1 | violation de R1 (NT-ARCH §3bis) et asymétrie candidate en instruction ; **CONV-3** ; écriture T sans ancrage (§8.5) ; **écriture duale non ancrée : un côté sans ancrage, ou un seul teneur** (NT-ARCH §8.5.0, PR-31 `ancreeDuale` — décisions D7 et D9 du porteur, 07/10/2026) ; « sans objet » non motivé (Annexe H, gabarit) ; régime sans condition de réfutation ni horizon (§8.4) ; **seuil de blocage H.5 sans source** ; **CONV-20** (branche 1bis) — qualification du régime affectif sans source déclarée, sans consentement ou sans statut protecteur, ou sur support distribué (§A.15.17) ; **CORPUS\_NON\_CONSENTI** (branche 1bis) — corpus explicité en validation experte dont un acteur n'est pas couvert : refus du corpus entier, refus tracé sans contenu (NT-G4 §6bis ; NT-ARCH F3, `refus_inscription_corpus`) ; **hypothèse déclarée après le constat** (branche 2) — non inscrite comme `hypothese_declaree` (NT-ARCH §B.2ter ; PR-57) |
| E2 | couple absent de la table dont le miroir existe (**arbitrage A8**) ; lacunes `E−→C−`, `d→C−` |
| E3 | **CONV-8** ; P7 (§4.2bis.3) ; répartition AX-3 (§4.2ter) ; **triplet d'inscription de communalité incomplet** (Annexe H §H.1) ; **CONV-6** ; **P5 en principe** (hôte non déclaré, NT-ARCH §B.2bis.3) ; **canal G-JUSTICE → G-AFFECTIF** : qualification de dysfonctionnement non examinée mobilisée dans une décision touchant des personnes — branche 4, l'attribution du trouble (NT-ARCH F1, R-ORDRE-QUALIFICATION ; décision du porteur, 12/10/2026 ; PR-53) |
| E4 | **CONV-7** (avec horizon) ; interprète manquant (NT-G5) ; extinction sans interprète (§4bis) ; `ETEINTE` × AX-2 (§4bis.3) ; futurité mal formée (§A.5) ; **CONV-11** ; **P5, exception** : triplet incomplet dont le point 3 déclare qu'aucune gouvernance n'est imposée — `[INSTRUMENT HÔTE INCOMPLET]` ; **clôture non déclarée** (`C-CLOTURE-ACCES`, NT-ARCH §8.2bis) — `[CLÔTURE NON DÉCLARÉE]` ; **CONV-16** — `[ÉCART SANS INSTANCE DE CONTRÔLE]` ; **CONV-18**, défaut d'annotation — `[DESTINATION NON DÉCLARÉE]` ; **statut du seuil, réfutation réservée à la population visée** (§A.14.1, PR-18) — `[RÉFUTATION RÉSERVÉE AUX DÉCLARANTS]` ; **canal G-JUSTICE → G-AFFECTIF** : qualification de dysfonctionnement inscrite sans examen de l'hypothèse pendante — `[HYPOTHÈSE D'INJUSTICE NON EXAMINÉE]` (NT-ARCH F1 ; PR-53) |
| E5 | extinction déclarée par le seul débiteur ; **CONV-15** ; **deux registres sans aucune ligne réciproque** — `[AUCUNE LIGNE RÉCIPROQUE]` : l'écriture duale est vraie par définition (PR-35 `deux_silences_sont_en_ecriture_duale`), deux silences ne sont pas un accord (décision D9 du porteur, 07/10/2026) ; **CONV-18**, lien non qualifié par l'instance — `[LIEN NON QUALIFIÉ PAR L'INSTANCE]` ; **statut du seuil, population visée non déclarée** — `[POPULATION VISÉE NON DÉCLARÉE]` ; **seuil déclaré hors de la population visée** — `[SEUIL DÉCLARÉ PAR UN TIERS]` (§A.14.1, PR-18) ; **injustice dont la portée ou la persistance n'est pas déclarée** : passe vers G-AFFECTIF, `[PORTÉE NON DÉCLARÉE]` (NT-ARCH F6, R-HYPOTHESE-INJUSTICE) |
| E6 | règle de communalité (§8.5.6.2, 8.5.6.2bis, 8.5.6.4) ; **registre d'un milieu dont la déclaration des concernés est défaillante** (PR-37 : non arrêtée, sans concernés, sans critère d'inclusion, sans interprète, écrivant inadmissible, ou échue) — `[REGISTRE DU MILIEU NON OPPOSABLE]` : la qualification « en écriture duale avec le milieu » est refusée, les lignes restent inscrites (décision D8 du porteur, 07/10/2026) ; `D+` sans source d'engagement (§8.5.6.5) ; RSO-8 (refus de l'effet) ; **CONV-17** — `[SAISINE HORS PROTOCOLE]` : la qualification « porté au nom du registre » est refusée, la ligne reste inscrite et bien formée ; **critère d'accès aux droits hors du régime INFRASTRUCTURE** (NT-ARCH F6.2, `regime_du_dispositif` ; PR-17) — `[CRITÈRE D'ACCÈS HORS INFRASTRUCTURE]` ; **CONV-19** *(proposé)* — qualification de créance appuyée sur le seul `signalsouffrance` : refusée, l'écriture reste (§A.15.16) ; **injustice documentée par la seule souffrance** : l'hypothèse vers G-AFFECTIF est refusée, l'injustice reste inscrite (NT-ARCH F6 ; CONV-19 ; PR-53) ; **corpus inscrit qui a perdu sa couverture** (contestation retenue d'une absence ; révocation, `[LACUNE]`) : il ne sert plus d'appui à une délibération jusqu'à couverture rétablie, il reste inscrit (NT-G4 §6bis) ; **constat de RECHERCHE\_INTERVENTION non recevable** (attestant = porteur de l'instrument, ou personnes concernées non associées) : la qualification « constat recevable » est refusée, le constat reste inscrit, sans signal ni relance (NT-ARCH §B.2ter ; PR-57) |
| E7 | motif réfuté ; G4 sans instance attributaire ; seul débiteur contredit (lemme 4) ; **CONV-13** ; **CONV-12** ; **NT-G7, capabilité plancher : qualification en litige** ; **absence admise dont la contestation est retenue** : requalifiée non admise (NT-G4 §6bis ; PR-56, `une_contestation_retenue_fait_tomber_la_representation`)  |

**Application du critère aux règles E0 et à P5**

| Règle | Lecture | Branche | Code |
|---|---|---|---|
| **Triplet d'inscription de communalité** (entité, personne qui inscrit, rôle qui habilite ; Annexe H §H.1) | le triplet dit « **qui répond de l'avoir faite et à quel titre** » : l'écriture a un objet ; ce qui manque est **qui la porte** | 4 | **E3** |
| **Seuil qui déclenche un blocage** sans `source_valuemetre` ni poseur (Annexe H §H.5.1) | le seuil **conditionne** l'exécution automatique sur d'autres écritures et d'autres acteurs : c'est un référentiel | 3 | **E1** — le seuil n'est pas inscrit, donc le blocage automatique ne s'arme pas ; statut candidat à horizon admissible (patron `CANDIDAT_NON_INSTANCIABLE`) |
| **CONV-6** — représentation prospective d'une écriture qui engage au-delà de l'exercice | ce qui manque est **qui représente** les intéressés futurs ; homologue de `V10a_planetaire_force_deliberation` (représentant planétaire non désigné → DÉLIBÉRATION) | 4 | **E3** |
| **CONV-11** — mouvement de maintien non structuré | l'écriture `e` a un objet ; le défaut visé est **la forme** (« jamais son lieu ») : sans structure, la créance de l'apporteur ne s'apprécie ni ne se conteste | 5 (condition de bonne formation) | **E4**, marqueur `[MAINTIEN NON STRUCTURÉ]` |
| **NT-G7** — prétention dont la genèse menace une capabilité plancher (« refuse… ou qualifie en litige ») | **hors critère** : le défaut n'est pas un terme manquant mais un **jugement de fond**, réservé par la règle elle-même à l'instance délibérative ; or une condition de bonne formation « ne juge pas le fond » (NT-ARCH §8.5.3bis) | — | **hors critère** —  **E7 : la prétention est inscrite et qualifiée en litige** ; le refus d'inscription est écarté : il préjugerait ce que l'instance délibérative doit trancher |
| **P5** — `INSTRUMENTATION` sans `instrument_hote` (NT-ARCH §B.2bis.3) | **deux lectures** : (i) le triplet de l'hôte nomme **qui l'a conçu** et **ce qu'il impose en gouvernance** (« qui arbitre ») : attribution → branche 4 → **E3**, conforme au texte ; (ii) l'hôte dit **où** l'inscription est logée et quelles finalités elle importe : terme d'appréciation → branche 5 → **E4** | 4 ou 5 |   **lecture (i) retenue, avec voie intermédiaire** : **E3 en principe** (un hôte non déclaré laisse ignorer s'il gouverne — RSO-8) ; **E4**, marqueur `[INSTRUMENT HÔTE INCOMPLET]`, si le point 3 du triplet déclare explicitement qu'aucune gouvernance n'est imposée ; réfutée, cette déclaration ramène en E3 |
| **CORPUS\_NON\_CONSENTI** — corpus explicité, `mode_validation_concept = EXPERTAL`, un acteur non couvert (NT-G4 §6bis ; NT-ARCH F3) | **deux lectures écartées** : branche 4 (qui valide : E3, renvoi en délibération, à l'opposé de la règle) ; branche 5 (E4, qui ne protège de rien). Retenue : l'inscription est elle-même le dommage (motif ci-dessous) | 1bis | **E1** — refus du corpus **entier**, tracé sans contenu (`refus_inscription_corpus`) ; un consentement ultérieur fonde une **nouvelle** inscription qui cite la trace ; un changement de mode non motivé n'est pas retenu. Après inscription, la perte de couverture relève de **E6** ; la contestation retenue d'une absence, de **E7** |
| **Absence non opposable** — recherche infructueuse sans trace ni attestation (PR-56) | l'acteur n'est pas couvert ; la déclaration d'absence est un champ du corpus refusé : elle n'a pas d'écriture propre où porter un marqueur | — (absorbé) | **E1 du corpus** ; la recherche est conservée dans la trace du refus. Aucun marqueur propre |
| **Constat non recevable** de RECHERCHE\_INTERVENTION (NT-ARCH §B.2ter) | (i) attestant = porteur, ou concernés non associés : la branche 4 (E3) donnerait au constat la suite réservée au constat recevable — écartée ; ce qui est refusé est la qualification « recevable » ; (ii) hypothèse déclarée après le constat : elle simule une déclaration *ex ante* | (i) hors critère ; (ii) 2 | (i) **E6** — inscrit, sans signal ni relance ; (ii) **E1** — non inscrite comme `hypothese_declaree` |

> **Motif de la branche 1bis pour CORPUS\_NON\_CONSENTI** *(décision du porteur, 29/10/2026)*. Inscrire un corpus explicité dont les concepts sont validés par des experts, sans le consentement des personnes dont il explicite le savoir, donne à ces concepts la stabilité, la circulation et la force d'appui d'une écriture : leur savoir devient une ressource du registre, et son sens est fixé par d'autres qu'elles. Inscrire puis marquer réaliserait cette dépossession. **Portée :** le savoir *des* personnes ; non les données qui les concernent (RGPD ; CONV-20), ni les actes et transactions qui les impliquent, ni une valuation déclarée sur elles (PR-18, E5). Le mode EXPERTAL délimite la condition : en validation consensuelle ou majoritaire, les personnes concernées participent à la fixation du sens ; `[LACUNE]` le mode CONTESTE.
>
> `[CONDITION DE RÉFUTATION]` Le motif tombe si l'on documente qu'un corpus inscrit sans consentement en validation experte ne produit, sur le terrain, aucune différence d'usage ni d'effet sur les personnes par rapport à un corpus consenti. *Patron :* CONV-20 (§A.15.17). *Porteur :* porteur MRC ; *horizon :* institutionnel ; *critère :* le cas est nommé ici.

**Horizon de tout marqueur E4** *(piste 3)*. Tout marqueur d'écriture mal formée (E4) porte un **horizon**, selon la modalité de CONV-7 (§A.15.10) : un **critère de sortie** — la pièce qui lèvera le défaut, et qui la déclarera — **ou une clause de caducité** ; à défaut, **caducité par défaut à la version suivante du set** (v5.7). À l'échéance, sans levée du défaut, le marqueur devient caduc : l'écriture **reste au registre**, elle **ne peut plus être complétée** ; une levée ultérieure exige une nouvelle écriture qui cite la première. Le statut candidat de la branche 3 (`CANDIDAT_NON_INSTANCIABLE`) porte le même horizon. *Ancrage :* `ProfRegPR32.le_marqueur_a_toujours_un_horizon`, dont le modèle ne dépend d'aucune règle particulière. E5 (écriture bien formée, marquée) **n'est pas concerné** : sa réserve ne rend pas l'écriture inachevée.

**Marqueurs du registre et marqueurs épistémiques** *(piste 5)*. Les marqueurs du **régime de vérifiabilité** (`[ENGAGEMENT SANS SYMÉTRIE]`, `[CHANGEMENT DE BASE NON TRACÉ]`, `[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ]`…) qualifient des **énoncés et des analyses** ; ils ne sont **pas** l'effet du défaut d'une **écriture**, qui reçoit un marqueur ou un signal **du registre**. Application : P5 — l'effet est le signal `INSTRUMENT_HOTE_NON_DECLARE` (NT-ARCH §B.2bis.3), non le marqueur `[DÉCOUPLAGE DE RÉGIMES]` ; `C-CLOTURE-ACCES` — l'effet est **`[CLÔTURE NON DÉCLARÉE]`**, non `[ENGAGEMENT SANS SYMÉTRIE]`, effet **E4** (branche 5 : l'écriture a un objet ; manque le terme qui permet de contester l'exclusion) (NT-ARCH §8.2bis). **R0-bis n'est pas concerné** : son défaut porte sur une **mobilisation descriptive** par un analyste, non sur une écriture du registre ; le marqueur épistémique y est à sa place. `[DÉCLARÉ]`

**Ancrage Lean du critère** *(piste 7)*. `ProfReg/PR33_EffetDuDefaut.lean` : le type des effets, la fonction `classer` (le critère dans l'ordre), le classement de référence (`classement_de_reference`), l'ordre (`l_ordre_fait_prevaloir_l_objet`), `mal_formee_n_implique_pas_refusee`, `les_refus_ne_viennent_que_des_branches_un_a_trois`, `le_marqueur_ne_vient_que_de_l_appreciation_ou_du_candidat`, `sans_branche_pas_de_classement` ; branche 1bis : `l_inscription_dommageable_est_refusee_avant_tout_marqueur` (le même défaut, sans 1bis, serait E4). **Théorèmes de forme** : ils ne justifient ni le critère, ni la lecture d'une règle comme tel `Defaut`. P5 : `ProfReg/PR34_InstrumentHote.lean` (`P5_suit_le_critere`).

**Hors critère.** Deux familles d'effets ne portent pas sur l'inscription, mais sur ce qu'on en tire. Le critère ne les règle pas :
- les **qualifications dérivées** refusées ou `INDETERMINE` (communalité, §8.5.6 ; RSO-8 : refus de l'effet) ;
- les **requalifications** (motif réfuté → `NON_SATISFAITE`, CONV-13, CONV-12, lemme 4).

**Toutes les règles relevées sont classées** (ci-dessus) ; NT-G7 en E7 par décision du porteur.

`[CONDITION DE RÉFUTATION]` **Le critère tombe si** une règle décidée par le porteur reçoit du critère un autre effet que le sien, **et** que le porteur maintient le sien avec un motif que le critère ne formule pas. Il tombe aussi si un même défaut, **dans l'ordre**, reste classable de deux façons. *Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* chaque condition de bonne formation du set cite sa branche ; les règles non classées sont listées.

`[CARACTÈRE DU CRITÈRE]` C'est une **règle d'architecture déclarée**, dégagée des règles existantes. Elle ne se démontre pas. Son ancrage Lean (PR-33 : type des effets, fonction de classement) n'en établit que la **forme**.

### §A.15.12 CONV-16 — le tiers institué d'une écriture duale : l'instance de contrôle commune

> **CONV-16.** Tout registre de communalité **désigne son instance de contrôle**, par une désignation **arrêtée** (une désignation ratifiée ou non déclarée ne vaut pas). Le **tiers** d'une écriture duale entre le registre de A et celui de B est l'**instance de contrôle commune** : désignée par **les deux** registres, qui n'est **ni A ni B**, et qui n'est **pas liée** à l'un d'eux au sens d'ISA 550 §10(b). **Seule elle arbitre** un écart entre A et B (confirme, infirme, ne conclut pas — PR-41) ; elle peut **constater la réalisation** du maintien, au même titre que l'autre teneur (PR-39). **À défaut d'instance commune, l'écart reste inscrit et n'est pas arbitrable** : il n'est ni effacé, ni tranché par un tiers choisi après coup.

**Pourquoi une convention.** Qui est le tiers ne se démontre pas : cela se déclare. AX-16 (ISA 505) fonde **la place** du tiers ; CONV-16 en fixe **l'identité**, par une règle d'institution.

**Ce qui l'ancre dans le set et le corpus.**
- NT-G6 §2.1, d'après Rochfeld, Cornu & Martin 2021 : la communalité se qualifie « selon les **instances** (attributaire, délibérative, **de contrôle**) », l'instance de contrôle portant « un pouvoir de contrôle du respect de ces décisions ».
- Note APC du 20/09/2026 : rubrique « Communauté de contrôle — Qui est habilité à faire respecter les droits inscrits ».
- CR 2025-S25 (porteur) : « Ce sont ces communautés de contrôle qui peuvent dire si un engagement ou une dette est tenue ».
- CR 2026-S09 : « faire auditer par la communauté de contrôle les enregistrements avancés — si possible vérifier que les enregistrements duaux ont bien été effectués avec les autres entités ».

**Appui formel.** `ProfRegPR43.instanceCommune`, `arbitrerInstitue`, `etatInstitue` : `sans_instance_commune_rien_n_est_arbitre`, `l_instance_liee_n_arbitre_pas`, `seule_l_instance_commune_tranche`, `la_designation_doit_etre_commune_et_arretee`, `l_instance_ne_peut_etre_partie`, `l_instance_de_controle_peut_constater`.

**Effet du défaut** (§A.15.11) : **E4**, par analogie avec CONV-11 — l'écriture duale reste inscrite, l'écart n'est pas arbitrable, marqueur `[ÉCART SANS INSTANCE DE CONTRÔLE]`.

**Condition de réfutation.** CONV-16 tombe si l'on documente un dispositif d'écriture duale entre registres de communalité où l'arbitrage des écarts par une instance **non désignée par l'une des parties** est accepté par les deux et tenu dans la durée — ce qui montrerait que la désignation commune n'est pas nécessaire à la légitimité de l'arbitrage.

**Ce que CONV-16 ne dit pas.** (i) Comment l'instance est **composée** : les exemples du corpus varient — financeurs et apporteurs de moyens (Trichon, 14/01/2025), comité du bien-être d'un fleuve (CR 2024-S24), conseil d'une friche, AG d'une SCIC (Trichon, 11/03/2025). (ii) Que l'instance **soit** non liée : c'est une déclaration. (iii) Ce qui se passe si A et B ne s'accordent pas sur une instance : rien n'est arbitré, et c'est **voulu**.

### §A.15.13 CONV-17 — ce qui sort au nom du registre : le constat attesté selon le protocole

> **CONV-17.** Un constat inscrit dans un registre de communalité **sans miroir** de sa contrepartie (statut `refuse`, `nonVerifiable` ou `conteste`, PR-40) n'est **porté au nom du registre** devant un **tiers extérieur** — **toute voie de PR-44 (`Voie`)** : négociation, transaction (art. 2044 C. civ.), autorité administrative, parquet, juge, arbitrage, autorité de supervision, injonction de vigilance — que s'il est **attesté selon le protocole** suivant :
> 1. la **ligne visée** : contrepartie, nature (prélèvement, rejet…), quantité, date, lieu ;
> 2. des **pièces tracées** : pour chacune, son auteur et sa méthode déclarés (instrument, chaîne de conservation) ;
> 3. l'**instance de contrôle** désignée par une désignation **arrêtée** du registre, qui n'est ni le teneur ni la contrepartie (CONV-16) ;
> 4. la **déclaration de non-liaison** de l'instance envers la contrepartie ;
> 5. l'attestation est **sans qualification juridique** : elle constate, elle ne qualifie ni n'impute ;
> 6. la **demande de communication** adressée à la contrepartie, et sa réponse — le refus est une pièce ;
> 7. la **confrontation au miroir reconstitué** (déclarations de la contrepartie à l'administration, obtenues auprès de leur détenteur) : concordante, sous-déclarée, sur-déclarée, ou **non obtenue** — elle est toujours écrite.
>
> À défaut, la saisine au nom du registre est inscrite avec le marqueur **`[SAISINE HORS PROTOCOLE]`** ; la ligne reste inscrite, inchangée. **CONV-17 n'interdit à personne de signaler en son nom propre** : un tel signalement n'est pas inscrit comme porté au nom du registre.
>
> **Toute voie ajoutée à PR-44 étend CONV-17 et se trace comme décision du porteur.** La rubrique 6 ne tient pas lieu des actes préalables qu'une voie exige (mise en demeure de L.225-102-4 II, par exemple) .

**Pourquoi une convention.** Le droit n'impose pas cette discipline : n'importe qui peut signaler une pollution (art. 40 CPP ; police de l'eau). CONV-17 règle ce que le **registre** engage quand il parle : ce qui sort en son nom a été vérifié, de façon reproductible, et la contrepartie a été mise en mesure de répondre.

**Ce qui l'ancre.**
- CR 2026-S09 : un « registre parallèle … d'un point de vue unilatéral », tenu pour « les faire valoir plus tard dans une négociation ou dans le cadre de poursuite juridique ».
- Art. 1363 C. civ. (« Nul ne peut se constituer de titre à soi-même ») et art. 1358 (preuve des faits par tout moyen) : l'attestation n'est pas un titre, c'est un dossier recevable ; sa force vient des pièces extérieures `[VÉRIFIÉ sur reproductions]`.
- Ord. n° 2016-728, art. 1 : constatations « exclusives de tout avis sur les conséquences de fait ou de droit » — modèle de la rubrique 5 `[VÉRIFIÉ sur reproduction secondaire]`.
- ISA 505 §7 (AX-16) : le contrôle de la procédure de confirmation reste à celui qui atteste — modèle des rubriques 2 et 6 `[TRANSPOSITION DÉCLARÉE]`.

**Appui formel.** `ProfRegPR45.conforme`, `statut17`, `confronter` : `conv17_sans_protocole_hors_protocole`, `conv17_n_interdit_pas_de_signaler`, `conv17_avec_protocole_retrouve_PR44`, `chaque_rubrique_compte`, `la_reconstitution_suppose_un_detenteur_tiers`, `la_sous_declaration_est_chiffree`.

**Effet du défaut** (§A.15.11) : **E6** — ce qui est refusé n'est pas l'écriture (la ligne reste inscrite, bien formée) mais la **qualification dérivée** « porté au nom du registre » ; marqueur `[SAISINE HORS PROTOCOLE]`.

**Condition de réfutation.** CONV-17 tombe si l'on documente que, devant les tiers extérieurs visés, des saisines portées par une communauté **sans** protocole d'attestation sont reçues et suivies **comme** les saisines attestées — ce qui montrerait que le protocole n'ajoute rien à la force de ce qui sort du registre.

**Ce que CONV-17 ne dit pas.** (i) Quelle **force** a le dossier devant un tiers donné : cela dépend de la voie. (ii) Que les pièces soient **exactes** : leur méthode est déclarée, non vérifiée. (iii) Qui, juridiquement, **porte** la saisine devant le juge du préjudice écologique (qualité, art. 1248) : question d'organisation, hors convention.

### §A.15.14 CONV-18 — l'annotation de destination d'un engagement de vigilance

> **CONV-18.** Tout engagement porté à un **registre de chaîne** (registre de communalité tenu par une gouvernance de chaîne de valeur, PR-46) est **annoté** : (1) le **site** concerné ; (2) l'**objet** préservé, qui doit figurer parmi les objets **déclarés** du registre ; (3) le **lien** déclaré de l'entreprise à l'impact — **cause**, **contribue** (contribution substantielle), ou **directement lié** (OCDE 2023, I.A.12-13). L'**instance de contrôle commune** (CONV-16) **vérifie la destination** et **qualifie le lien** ; le lien qu'elle **retient** prime sur le lien déclaré pour qualifier l'engagement (dette de réparation ou non, AX-17). Un engagement sans annotation complète est inscrit, **mal formé**, marqué **`[DESTINATION NON DÉCLARÉE]`**. Un engagement annoté mais non encore qualifié par l'instance est qualifié sur le lien déclaré, marqué **`[LIEN NON QUALIFIÉ PAR L'INSTANCE]`**. Si l'instance ne confirme pas le site, la destination est **infirmée** ; l'engagement reste inscrit. Une vérification par un tiers **non désigné** ne vaut pas.

**Pourquoi une convention.** L'écriture duale entre une entreprise et le registre de chaîne est binaire : elle **perd le site et l'objet** (`la_projection_perd_le_fournisseur`, PR-46). Et la qualification de la réparation dépend d'un lien que l'entreprise déclare elle-même, et qu'elle a intérêt à minorer — `[ENGAGEMENT SANS SYMÉTRIE]`. CONV-18 porte la troisième arité en annotation **vérifiée**, et donne au lien sa contrepartie réfutable : la qualification par l'instance.

**Ce qui l'ancre.**
- Accord sur la sécurité incendie et la sécurité des bâtiments au Bangladesh (13/05/2013) : désignation des usines par niveau (§1-3), rapports d'inspection **par usine** (§11), liste agrégée (§19 a), inspecteur indépendant (§8).
- OCDE 2023, I.A.12-13, comm. 16 (« contribution substantielle » ; « la relation … n'est toutefois pas figée ») et 23.
- Directive (UE) 2024/1760 consolidée, art. 10 §1 a) et c) ; art. 3 §1 h) (vérification par un tiers indépendant).

**Appui formel.** `ProfRegPR47.annotationComplete`, `etat18` : `sans_site_destination_non_declaree`, `le_lien_retenu_prime`, `l_instance_requalifie_le_lien`, `un_verificateur_non_designe_ne_vaut_pas`, `destination_infirmee_et_objet_hors_registre`.

**Effet du défaut** (§A.15.11) : **E4** pour le défaut d'annotation (`[DESTINATION NON DÉCLARÉE]` : le terme manquant est une condition de bonne formation) ; **E5** pour le lien non qualifié (`[LIEN NON QUALIFIÉ PAR L'INSTANCE]` : bien formé, avec réserve).

**Condition de réfutation.** CONV-18 tombe si l'on documente une gouvernance de chaîne où les engagements **non annotés** par site et objet sont suivis et vérifiés **aussi efficacement** que des engagements annotés — ou où la qualification du lien par le déclarant seul n'a pas conduit à minorer la réparation.

**Ce que CONV-18 ne dit pas.** (i) **Comment** l'instance qualifie la contribution (AX-17, colonne C, point 1). (ii) La **dynamique** du lien : une vérification remplace la précédente. (iii) Le cas d'un registre de chaîne **sans instance commune** : l'engagement reste `[LIEN NON QUALIFIÉ PAR L'INSTANCE]`.

### §A.15.15 CONV-1 : condition de réfutation ; codes de l'effet du défaut de sept conventions *(proposés)*

 *Cette section ne modifie aucun énoncé de convention. Elle porte la condition de réfutation de CONV-1 et **classe** par le critère de §A.15.11 sept conventions de §A.15.1. Sources : `ProfReg/Conventions_et_sanctions_2026-09-07.md` §2 ; `~/Developer/ProfReg` (`CB3Attempt.lean`, `LotL2_PR2_PR14.lean`, `PR27_Candidats_Septembre.lean`).*

#### (1) CONV-1 — condition de réfutation

**Source.** La note d'instruction (`Conventions_et_sanctions_2026-09-07.md` §2) porte, pour CONV-1 : *« Condition de réfutation : l'exhibition d'un foncteur de calcul non arbitraire et gouverné obligerait à réviser la convention. »* Cette formule ne définit ni « non arbitraire » ni « gouverné » : elle est précisée ci-dessous, sur les appuis compilés.

> **Condition de réfutation de CONV-1.** CONV-1 tombe si l'on exhibe un **calcul de la fraction actorielle**, c'est-à-dire un changement de base V₁ → V₃ au sens de `CB3Attempt.lean`, qui soit à la fois :
> *(i)* **structurellement admissible** : un foncteur qui satisfait la condition monoïdale requise, **oplax**, celle que `CB3_candidate_not_oplax_monoidal` réfute pour le candidat identité ;
> *(ii)* **non arbitraire** : sa valeur est **déterminée par les inscriptions du registre**, sans paramètre libre fixé par qui calcule ;
> *(iii)* **gouverné** : ses éventuels paramètres sont eux-mêmes **déclarés selon CONV-4** (désignation, résolution, intégrité, porteur).
>
> **Ne la fait pas tomber** : un calcul qui exige un paramètre libre. C'est une déclaration déguisée en calcul, une « non-déclaration renommée » (§A.15.11, branche 2), et CONV-1 s'y applique au lieu de tomber.

**Appuis et bornes.** `CB3_candidate_not_oplax_monoidal` réfute **un** candidat. L'inexistence **générale** d'un tel foncteur est une **lacune déclarée** (`CB3Attempt.lean`), non un théorème. C'est pourquoi CONV-1 est une convention. `fraction_exhibe_sa_source` (LotL2) établit que toute fraction est de la forme `declaree s v` : **le calcul est exclu par le typage**. Mais PR-27 (`fraction_exhibe_une_source_eventuellement_vide`) montre que la source peut être vide : **la qualité de la source relève de CONV-4, non de CONV-1**.

*Couche 2.* Porteur : porteur MRC / architecte. Horizon : v6 (celui de la 2-cellule et de CB3). Critère : la condition est inscrite ici ; elle est éprouvée si un candidat foncteur est soumis (par un lecteur ou dans le formel) et que l'issue est inscrite.

#### (2) Codes de l'effet du défaut — les sept conventions sans code

*Règle rappelée (§A.15.11) : « Toute condition de bonne formation du set cite son code. Une règle qui n'en cite pas et dont l'effet n'est pas écrit est un E0. » Trois des sept ne sont **pas des conditions de bonne formation** d'une écriture ; elles ne sont donc pas des E0 mais **hors critère**, ce que la proposition déclare au lieu de leur forcer un code.*

| Conv. | Défaut visé | Lecture par le critère | Code proposé |
|---|---|---|---|
| **CONV-1** | une fraction actorielle **calculée** par le registre au lieu d'être déclarée | la valeur calculée **simule une déclaration** : branche 2 (non-déclaration renommée) | **E1** — et **par construction du typage** : `FractionActorielle` n'a que le constructeur `declaree`, le défaut n'est pas représentable |
| **CONV-2** (carré triangulaire) | un énoncé qui dit « la commutativité est prouvée » | porte sur un **énoncé**, non sur une écriture | **hors critère** — marqueur **épistémique** `[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ]` (§A.15.11, piste 5 : marqueurs du régime de vérifiabilité, distincts de ceux du registre) |
| **CONV-2** (carré B1↔B2, §A.15.9) | une fiche SYSTEMIQUE qui aboutit à DELIBERATION **sans inventaire clos non vide** | porte sur ce qu'on tire de la fiche (sa phase d'aboutissement) ; la clôture sans inventaire est interdite (PR-4) | **E6** — la qualification « aboutie en DELIBERATION » est refusée ; la fiche reste inscrite |
| **CONV-4** | *(a)* un valorimètre ou un seuil de F8 **sans source déclarée** | le valorimètre **conditionne d'autres écritures** : c'est un référentiel, branche 3 (cohérent avec le classement du seuil H.5) | **E1**, sauf statut candidat à horizon (`CANDIDAT_NON_INSTANCIABLE`) |
| | *(b)* une source présente à laquelle **manque une des quatre propriétés** (désignation, résolution, intégrité, porteur) | l'objet et sa source existent ; manque un terme qui permet de la **vérifier** : branche 5 (`source_sans_porteur_mal_formee`, PR-28 : mal formée) | **E4**, marqueur `[SOURCE NON VÉRIFIABLE]`, avec horizon (règle des E4) |
| **CONV-5** | une mobilisation sous `[VALUATION SUSPENDUE]` qui **déclenche** une règle R-\* | **deux lectures** : *(α)* la suspension neutralise (RSO-2) : le déclenchement est **sans effet**, E6 ; *(β)* par la réciproque de CONV-5, déclencher **vaut** régime normatif : le régime déclaré est **requalifié**, E7 | **E6 recommandé** (α) : c'est ce que dit l'énoncé (« ne déclenche donc aucune règle »), et RSO-2 le fonde. (β) ferait d'un défaut une requalification silencieuse.  |
| **CONV-9** | cinquième terme `non déclaré` | RSO-8 : le non-déclaré **refuse l'effet** que la déclaration aurait conditionné. L'agrégat ne sert à rien établir, et la mobilisation reste inscrite et bien formée (`BienFormee_ne_borne_pas_le_quintuplet`) | **E6** *(portée : inscriptions postérieures au 08/09/2026, §A.14.9)* |
| **CONV-10** | une instance de L2 qui lit `plein` comme une **valorisation** | porte sur ce qu'on tire de l'instance, non sur sa forme | **E6** — la qualification dérivée « valorisé » est refusée |
| **CONV-14** | *(a)* un **score composite** ou un **classement** entre axes ou régimes juridiques différents | qualification dérivée | **E6** — le score n'est pas inscrit comme qualification (appui : `le_score_ne_determine_pas_les_axes`, PR-27) |
| | *(b)* un axe **non déclaré** | RSO-8 | **E6** — non qualifié sur cet axe ; ne vaut pas qualification par défaut |

**Hors critère, et déclarées comme telles** : CONV-2, pour le carré triangulaire (énoncé méthodologique). **Aucune des sept n'est un E0** si ce classement est adopté. **Décompte** : 18 conventions, toutes codées ou déclarées hors critère ; CONV-19 et CONV-20 ont leur code en §A.15.16 et §A.15.17.

`[CONDITION DE RÉFUTATION DU CLASSEMENT]` Celle du critère (§A.15.11) s'applique. Le classement tombe si le porteur maintient pour l'une de ces conventions un autre effet, avec un motif que le critère ne formule pas. **Point le plus exposé** : CONV-5, où deux lectures sont possibles.

`[LACUNES]` *(i)* Le classement est une **lecture**, non un calcul. `PR33.classer` pourrait l'éprouver, en ajoutant ces cas au `classement_de_reference` (recompilation, décompte augmenté) : **non fait**. *(ii)* Le marqueur `[SOURCE NON VÉRIFIABLE]` (CONV-4 b) n'a pas d'autre régime propre : son horizon suit la règle générale des E4 (critère de sortie ou caducité à v5.7). *(iii)* La précision (i)-(iii) de la condition de CONV-1 est une **interprétation** de « non arbitraire et gouverné », à confirmer.

### §A.15.16 CONV-19 — le signal de souffrance n'est pas une preuve *(décision du porteur, 12/10/2026)*

> **CONV-19.** `signalsouffrance` (NT-G9 ; NT-ARCH F1, C-GENRE-METIER) est un **indice explicatif** : il n'entre dans **aucune qualification de créance** et ne déclenche **aucune règle R-\*** qui conférerait un droit. La légitimité d'une créance est portée par G-JUSTICE (NT-G7) ; la souffrance **n'y fait pas non plus obstacle**.

**Origine.** Règle de non-confusion de NT-G9 §4.2 : la souffrance *explique* (cohérence dynamique), elle ne *correspond* pas à un droit. Source : Honneth, *The Struggle for Recognition*, 1995 (au corpus, `biblio/`). Jusqu'ici homologue de CONV-5 dans l'encadré de NT-G9 ; le porteur en fait une convention propre, dont le périmètre n'est pas celui de PR-10.

**Ancrage de forme (PR-52).** `la_souffrance_seule_ne_qualifie_aucune_creance` est une **lecture** : `QualifieCreance` est défini de sorte que la convention y soit encodée ; il est cité avec son témoin `la_souffrance_n_empeche_pas_la_qualification`, jamais seul. Il établit la forme, non que la règle soit juste.

**Effet du défaut : E6** *(proposé)* — hors critère : le défaut porte sur ce qu'on tire de l'écriture. Une qualification de créance appuyée sur le seul signal de souffrance est **refusée** ; l'écriture qui porte le signal reste inscrite.

`[CONDITION DE RÉFUTATION]` **CONV-19 tombe si** l'on documente un dispositif où une créance fondée sur la seule souffrance déclarée est reconnue, tenue et non contestée par toutes les parties, sans que cela produise l'usage stratégique de la plainte que la règle prévient. *Porteur :* porteur MRC. *Horizon :* institutionnel, révisable. *Critère :* le cas est nommé dans la présente section.

### §A.15.17 CONV-20 — qualification du régime affectif : source, consentement, protection, support *(décision du porteur, 12/10/2026)*

> **CONV-20.** Une qualification de `regimeaffectif` n'est inscriptible que si (1) `sourcequalification` est déclarée — `CLINIQUEEXTERNE`, `DIALOGUEPROFESSIONNEL` ou `ARCHIVAGEDESACTES` ; `INDÉTERMINÉE` ne qualifie pas —, (2) `consentementcollectif` = VRAI, (3) `statut_rgpd_regimeaffectif` ∈ {ANONYMISE, PSEUDONYMISE, AGREGESEUL}. **Sur support distribué**, seul `NONCOLLECTE` est admis. **`NONCOLLECTE` désigne l'absence de toute qualification inscrite** : le registre ne tient que l'existence des traces *(décision du porteur, 12/10/2026)*.

**Origine.** NT-G9 §10.1 (règle d'inscription ; règle du support, `[ENGAGEMENT À HORIZON IRRÉVERSIBLE]`).

**Ce que la formalisation fait voir (PR-52).** Composées, les deux règles **ferment toute inscription sur support distribué** (`sur_support_distribue_rien_n_est_inscriptible`) : la seconde exige `NONCOLLECTE`, la première l'exclut (`noncollecte_n_est_jamais_legitime`). C'est conforme à NT-G9 (« inopérant par construction »). Ce n'est pas une incohérence une fois `NONCOLLECTE` défini comme l'absence de qualification : pour `ARCHIVAGEDESACTES`, le registre ne tient alors que l'existence des traces, sans qualification du régime (NT-G9 §10.1, reformulé).

**Ancrage de forme (PR-52).** `sans_source_rien_n_est_legitime` et `noncollecte_n_est_jamais_legitime` (lectures), `la_source_ne_suffit_pas` (la source est nécessaire, non suffisante), `sur_support_distribue_rien_n_est_inscriptible` ; témoin `inscriptible_temoin_discriminant`. La source admise n'interdit pas l'auto-qualification collective : `DIALOGUEPROFESSIONNEL` et `ARCHIVAGEDESACTES` sont tenus par le collectif lui-même ; ce que la règle écarte est la qualification **sans source déclarée**.

**Effet du défaut : E1**, par la **branche 1bis** du critère (§A.15.11) : l'inscription est elle-même le dommage — inscrire puis marquer enregistrerait des données sensibles sans base de légitimité. La branche est ajoutée au critère par décision du porteur (12/10/2026), sur le motif que le critère ne formulait pas ; ancrage de forme : `l_inscription_dommageable_est_refusee_avant_tout_marqueur` (PR-33).

`[CONDITION DE RÉFUTATION]` **CONV-20 tombe si** l'on documente qu'une qualification de régime affectif sans source déclarée, ou sans consentement, ne produit sur le terrain aucune différence d'usage ni de risque par rapport à une qualification conforme — la règle serait alors une formalité. *Porteur :* porteur MRC ; *horizon :* institutionnel ; *critère :* le cas est nommé ici.

## §A.17 Attribut de lecture `statut_grammaire` — déclarer qu'une catégorie n'a pas de prise

 Origine : `Lecture_Numero74_Meso-ESS_x_MRC_2026-09-14.md`, proposition P3.

### §A.17.1 Le motif — une asymétrie épistémique défavorable au MRC

La grille des canaux méso admet explicitement qu'un canal soit **inopérant** : Lamarche & Bastien le posent, et le numéro 74 d'*Interventions économiques* en donne des cas — Rafélis de Broves *et al.* écrivent que leurs données n'indiquent pas de différenciation par le canal relation à la nature ; Cordrie *et al.* tiennent le canal travail pour « relativement marginal ». Un canal inopérant y est un **résultat**, non un échec de codage.

Le MRC n'a pas d'équivalent. Ses douze grammaires sont réputées applicables en permanence, et **aucune procédure ne permet de déclarer que l'une d'elles est sans prise sur un cas**. Conséquence : une grammaire non renseignée est indistinguable d'un oubli. La non-pertinence n'est pas une écriture, donc elle n'est pas contestable.

Un dispositif qui ne peut jamais déclarer l'une de ses propres catégories sans prise est, de ce point de vue, en `[ENGAGEMENT SANS SYMÉTRIE]` : il exige partout ailleurs une condition de réfutation et n'en offre aucune sur son applicabilité. L'attribut `statut_grammaire` lève cette asymétrie — **et rien d'autre**.

### §A.17.2 Statut — attribut de lecture, et le mot compte

`statut_grammaire` **n'est pas un champ de Couche 2**. Il ne qualifie pas une écriture : il qualifie **le rapport d'une grammaire à un corpus ou à un cas**, et il est porté par la couche d'analyse, déclaré par l'analyste. Il ne vit ni en Couche 0, ni en Couche 1, ni en Couche 2, et **n'entre dans aucun compte de grammaires** (→ §C.2 de NT-ARCH : le plafond de douze est inchangé).

Le poser en Couche 2 serait un `[CHANGEMENT DE BASE NON TRACÉ]` : on ferait de l'applicabilité une propriété des écritures, alors qu'elle est une propriété de la lecture qu'on en fait.

### §A.17.3 Les quatre valeurs — amendement déclaré à P3

P3 propose trois valeurs ; l'attribut en compte quatre, et l'écart est motivé.

| Valeur | Sens |
| :-- | :-- |
| **STRUCTURANT** | La grammaire commande la lecture du cas : ses règles y sont activement mobilisées et l'analyse serait autre sans elle |
| **SECONDAIRE** | Elle a prise, sans commander |
| **INOPERANT** | **Elle n'a pas de prise — et c'est un résultat d'enquête**, ancré (→ §A.17.4) |
| **NON_INSTRUIT** | **Valeur par défaut.** La question n'a pas été posée sur ce corpus |

**Pourquoi la quatrième valeur, et pourquoi elle est par défaut.** Sans elle, un attribut non renseigné se lit comme un INOPERANT implicite, et le dispositif produit exactement le défaut qu'il est censé corriger. En posant `NON_INSTRUIT` **comme valeur par défaut**, l'absence de renseignement et la déclaration de non-instruction coïncident : le silence cesse d'être interprétable.

*Précédents internes.* La distinction `AUCUN` / `NON_DETERMINABLE` de la sous-couche C-CLOTURE-ACCES (→ NT-ARCH §8.2bis) pose exactement le même écart : un résultat d'enquête contre un état du matériau. Et le typage des espaces méso du numéro 74 l'a rencontré en situation — sept colonnes « non instruite » y risquaient d'être lues comme des « non », ce qui aurait inversé le sens du résultat.

### §A.17.4 Trois garde-fous — sans lesquels l'attribut est à rejeter

**(a) Ancrage obligatoire pour INOPERANT.** On déclare **sur quel matériau** on constate l'absence de prise. Un `INOPERANT` sans ancrage est **nul** : l'attribut retombe à `NON_INSTRUIT`. C'est la contrepartie du risque principal — déclarer inopérant ce qui gêne.

**(b) INOPERANT interdit si un signal de cette grammaire est levé dans le périmètre de lecture.** Une grammaire dont un signal est actif a, par définition, prise. La règle vaut sur l'ensemble du périmètre considéré, non écriture par écriture : déclarer G-JUSTICE inopérante sur un corpus où `R-CAPABILITES` se déclenche ailleurs serait une contradiction interne à la lecture.

**(c) INOPERANT ne dispense d'aucun invariant de Couche 1.** *(Garde-fou absent de P3.)* Déclarer une grammaire inopérante est un acte de **lecture**, jamais de dispense. La machine d'états, R1, l'obligation d'attribution avant criticité et R-INTERDIT-ABSOLU s'appliquent identiquement. Sans cette clause, l'attribut deviendrait une porte de sortie de l'architecture — et ce serait l'objection décisive contre lui.

### §A.17.4bis Résultat du contrôle de compatibilité avec les douze notes de grammaire

Contrôle conduit à la demande du porteur. Méthode : recherche des prétentions d'applicabilité universelle, relevé du câblage à la Couche 1, lecture des conditions de réfutation propres à chaque note. **Résultat : compatible, avec une exception et deux clauses.**

**(i) Exception — `INOPERANT` est indisponible pour G-PERFORMATIVITE (NT-G4).** Deux motifs, tous deux tirés de la note elle-même :

- son tableau d'identification la qualifie de « grammaire transversale **(tous modes)** » — **elle est la seule des douze** à porter cette mention ;
- son **garde-fou de réflexivité**, déclaré obligatoire, pose que *« le MRC est lui-même un registre de type comptable : il est donc performatif »*, et que le présenter comme un reflet du réel est un `[RAISONNEMENT AUTORÉFÉRENTIEL]`.

Déclarer G-PERFORMATIVITE `INOPERANT` serait donc un **acte d'inscription, accompli par un registre performatif, affirmant que la performativité n'a pas de prise sur lui** — l'énoncé se réfute en s'énonçant, et la note nomme déjà le défaut. `SECONDAIRE` reste disponible ; `INOPERANT` ne l'est pas.

**(ii) Clause — un `INOPERANT` répété n'est pas une réfutation.** Les conditions de réfutation des douze notes portent sur la **validité générale** d'une grammaire ou d'un champ (« si X ne produisait aucune différence observable, le champ serait redondant et devrait être retiré »). L'attribut, lui, porte sur le **rapport d'une grammaire à un corpus donné**. Ce sont deux objets distincts, et les confondre transformerait l'attribut en instrument de démolition par accumulation : *une grammaire peut être sans prise sur dix corpus et rester parfaitement valide*. Aucune série d'`INOPERANT`, si longue soit-elle, ne vaut réfutation — seule la condition de réfutation propre à la note peut la produire.

**(iii) Rappel — les grammaires câblées en Couche 1.** G-RESPONSABILITE (machine d'états, R-INTERDIT-ABSOLU, R1), G-JUSTICE (machine d'états, R-INTERDIT-ABSOLU), G-MESOLOGIE, G-COMMUNALITE et G-MIMETIQUE (R-INTERDIT-ABSOLU, R1) sont reliées à des invariants de Couche 1. Le garde-fou **(c)** s'y applique avec une acuité particulière : un `INOPERANT` déclaré sur l'une d'elles **ne suspend ni la machine d'états, ni R1, ni R-INTERDIT-ABSOLU**. Et le garde-fou **(b)** y est fréquemment mordant, ces grammaires portant des signaux susceptibles d'être levés dans le périmètre.

**Ce que le contrôle a trouvé de rassurant.** Aucune des douze notes ne revendique une applicabilité universelle, hors le cas G4. Les formules qui en avaient l'air sont des **conditions de déclenchement** — « toute interaction *sur un commun* » (NT-G6), « toute écriture *qui enregistre une adhésion* » (NT-G7) — et elles **soutiennent** l'inopérance plutôt qu'elles ne la contredisent : un corpus sans commun est un corpus où G-COMMUNALITE n'a pas de prise, et la note le dit déjà sans avoir le mot pour l'inscrire.

*Réserve de portée du contrôle.* Il a porté sur les tableaux d'identification, les tables de règles, les sections « conditions de réfutation » et sur une recherche de chaînes ; **il n'a pas relu intégralement les douze notes**. Une prétention d'universalité formulée sans les mots recherchés y échapperait.

### §A.17.5 Ce que l'attribut ne fait pas

Aucune primitive, aucun invariant, aucun signal, aucun valorimètre, aucun seuil. Il ne **désactive** rien : une grammaire déclarée `INOPERANT` reste dans le set, ses invariants tiennent, ses couplages restent tracés.

Et il **ne s'agrège pas**. Compter « neuf STRUCTURANT, trois INOPERANT » pour en tirer un taux de couverture du MRC sur un corpus serait un `[DÉCOUPLAGE DE RÉGIMES]` : quatre valeurs déclarées ne font pas une mesure, et leur distribution n'est pas un indice de pertinence. Ce qui se lit d'une colonne d'`INOPERANT` ancrés, c'est **où le modèle n'a rien à dire** — une information, pas une note.

### §A.17.6 Portée étendue aux canaux de la lecture méso

L'énumération est **commune** à deux objets, l'objet étant déclaré à chaque usage :

- **grammaires** du MRC (Couche 3) — usage principal, celui de la présente section ;
- **canaux** de la grille méso (→ §A.7) — usage dérivé, qui rend explicite ce que Lamarche & Bastien admettent sans le typer.

Les deux ne se confondent pas : un canal appartient à une grille externe, une grammaire au MRC. Maintenir une énumération unique évite deux vocabulaires parallèles pour un même geste ; **confondre les deux objets serait un `[CHANGEMENT DE BASE NON TRACÉ]`**, d'où l'obligation de déclarer lequel est qualifié.

### §A.17.7 Conditions de réfutation

**Sur l'usage.** Sur un corpus test, la part des `INOPERANT` **déclarés avec ancrage** doit être de **100 %**. En deçà, l'attribut sert à esquiver et doit être **retiré**, non allégé.

**Sur l'utilité — condition symétrique.** Si, après instruction de plusieurs corpus, **aucune** grammaire n'est jamais déclarée `INOPERANT`, l'attribut ne sert à rien et doit être retiré aussi. Les douze grammaires seraient alors, de fait, universellement applicables — ce qui est une thèse forte, et qu'il vaudrait mieux inscrire comme telle que laisser à l'état d'absence de contre-exemple.

*Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* renseignement sur au moins un corpus complet, avec au moins un `INOPERANT` ancré **et** un `STRUCTURANT` — faute de quoi l'attribut n'aura pas montré qu'il discrimine.

### §A.17.8 `[LACUNES ET LIMITES DE CETTE SECTION]`

- **L'attribut n'est renseigné sur aucun corpus.** Il existe ; il n'a pas servi. Son critère de vérification n'est donc pas satisfait.
- **La frontière STRUCTURANT / SECONDAIRE n'est pas outillée.** Elle repose sur le jugement de l'analyste — « commande la lecture » contre « a prise ». C'est assumé : le régime est procédural, et fabriquer un seuil serait pire. Mais la frontière est la plus contestable des trois, et les désaccords s'y logeront.
- **Le garde-fou (b) suppose un périmètre de lecture déclaré.** Si le périmètre est flou, l'interdiction est inapplicable. Le périmètre relève de l'analyste (→ §A.7) et n'est pas, lui, contraint par le présent attribut.
- **Contrôle de compatibilité (§A.17.4bis).** Résultat : compatible, hors G-PERFORMATIVITE pour laquelle `INOPERANT` est indisponible. **Lacune résiduelle** : le contrôle a porté sur les tableaux d'identification, les tables de règles, les sections « conditions de réfutation » et une recherche de chaînes — **les douze notes n'ont pas été relues intégralement**, et une prétention d'universalité formulée sans les mots recherchés y échapperait.

---

## §A.18 Fiche de l'axiome **AX-3** — découplage du sauvetage et de la répartition

*(Rédaction source : `ProfReg/Avarie_commune_A2_P6prime_2026-09-07.md` §4. **Cette section n'ajoute aucune thèse** : elle inscrit dans le set un axiome sur lequel il fait reposer une décision d'architecture.)*

> §A.15.5 motive la substitution de PR-13 au **nœud D** par ces mots : *« L'argument du retrait est **AX-3** : fermer le carré rendrait la répartition dérivable de l'agrégation, et c'est le **recouplage** que AX-3 défait. »* La présente fiche rend cet argument contestable sur pièces.

### §A.18.1 Énoncé *(colonne A)*

> **AX-3 — Découplage du sauvetage et de la répartition.** Lorsqu'un collectif fait face à un péril qui menace l'ensemble de ce qu'il a à préserver, la décision de l'action de sauvetage et la règle de répartition de sa charge **peuvent être séparées** : confiées à deux acteurs distincts, la seconde posée *a priori* et indépendamment de la première.
>
> Là où cette séparation n'est pas opérée, l'instrument qui détermine l'effort détermine simultanément sa répartition, et l'action collective se bloque sur l'arbitrage entre efficacité et équité.

### §A.18.2 Portée

`valable sous conditions déclarées`. Les conditions sont les **quatre conditions de qualification** du droit maritime, reprises telles quelles : **un péril commun** ; **un sacrifice volontaire** (jet ou dépense extraordinaire) ; **un intérêt commun** (la recherche du salut de tous) ; **un résultat utile** (une partie au moins de ce qui devait être sauvé l'a été). PR-12 est aligné sur ces quatre conditions. Le **terme du mandat** n'est pas une condition d'AX-3 : c'est une condition de bonne formation du **mandat du décideur**, sourcée par **AX-9**, versée en NT-ARCH §4.2ter.2. Hors de ces quatre conditions, AX-3 ne dit rien.

### §A.18.3 Ce que AX-3 ne dit pas — et c'est ce qui le rend utilisable ici

**AX-3 ne dit pas quelle règle de répartition retenir.** Le prorata des richesses à sauver est **une** règle ; ce n'est pas le contenu de l'axiome. L'axiome porte sur la **séparabilité** des deux fonctions, non sur la formule de la seconde.

Cette borne n'est pas une précaution de style : **le porteur écarte le prorata** pour le champ de l'emploi — *« ni les richesses, ni les capacités de contribuer, ni les vulnérabilités ne se laissent réduire à une valeur monétaire unique »* (`Application des avaries communes à TZCLD`). **AX-3 survit à cette exclusion ; une lecture d'AX-3 qui contiendrait le prorata n'y survivrait pas.**

### §A.18.4 Appui, et la distinction de statut qui le borne

**Structure et résultat théorique** : Demonsant, C., Levillain, K., Hatchuel, A. & Segrestin, B., « Pour une action climatique équitable : penser le sauvetage commun », *Revue française de gestion* n° 327, 2026/2, p. 85-104, DOI 10.1684/rfg.2026.130. Le résultat mobilisé est le découplage : *« là où les instruments associés à une ressource commune conduisaient à coupler le coût de l'atténuation et sa répartition, le modèle du péril commun permet de découpler la gestion de l'efficacité du sauvetage de la question de la répartition équitable des efforts. »*

**La longévité de la règle établit la faisabilité, jamais la validité.** Deux millénaires de mise en œuvre à travers des juridictions successives établissent que **le découplage est institutionnellement tenable** — qu'il ne relève pas de la construction théorique irréalisable. Ils n'établissent pas qu'il est juste.

> **Un argument de permanence est interdit ici**, en application du critère adopté d'après Stépanoff : *un facteur présent partout, ou depuis toujours, n'explique rien*. La longévité est **un fait à expliquer, non un argument** — et les auteurs eux-mêmes écrivent que la règle « présente des propriétés fondamentales qui font qu'elle a été maintenue » : la propriété explique la persistance, et non l'inverse. **Argumenter depuis la durée inverserait leur propre explication.**
>
> **La datation retenue est celle de la source : « plus de 2000 ans », renvoyant au *Digeste* romain, livre XIV, titre 2 (*Lex Rhodia de iactu*) ; l'accord international date de 1890 (Règles d'York et d'Anvers). Aucune autre datation n'est retenue, ici ou ailleurs dans le corpus.** *Rappel : la datation n'est de toute façon pas un argument — voir le garde-fou ci-dessus ; elle ne sert qu'à citer la règle correctement.*

### §A.18.5 Condition de réfutation

> **AX-3 tombe si**, sur les cas étudiés, la séparation du décideur et du répartiteur ne produit **aucune différence observable** sur les décisions prises, les contributions versées ou l'acceptabilité de l'action. Elle serait alors une distinction sans effet.

`[STATUT — ELLE N'A JAMAIS ÉTÉ TESTÉE.]`

### §A.18.6 Reste de traduction *(colonne C — obligatoire)*

Trois traits de la règle maritime **disparaissent** dans la transposition, et leur perte doit être déclarée à chaque usage :

1. **Le caractère volontaire du sacrifice.** En mer, le jet est décidé. Les sacrifices que le MRC inscrit — un poste d'alimentation compressé, un parcours professionnel interrompu — ne sont ni décidés ni consentis par ceux qui les portent.
2. **L'urgence, qui autorise le capitaine à décider seul.** Elle fonde l'efficacité du dispositif maritime ; elle est absente d'un péril chronique, et sa restitution artificielle coûterait la parité délibérative.
3. **Le collectif fermé et dénombrable.** *« Le périmètre des intéressés est donné en mer, il est à construire ailleurs, et sa construction est un acte politique que l'axiome ne couvre pas. »* **C'est la perte la plus lourde.**

> Construire le périmètre des intéressés, c'est **déclarer une clôture** : `C-CLOTURE-ACCES` (NT-ARCH §8.2bis, F8) en porte le triplet obligatoire — *qui est exclu du périmètre ; par quel dispositif ; qui a posé le dispositif*. **Le reste de traduction n'est pas comblé — il reste un acte politique que l'axiome ne couvre pas — mais il devient inscriptible**, donc contestable. `[L'INSTRUMENT N'A PAS ÉTÉ ÉPROUVÉ SUR CE CAS.]`

### §A.18.7 Ce que AX-3 importe, et qui doit être déclaré avec lui

`[ENGAGEMENT SANS SYMÉTRIE — CONTRE-PARTIE DÉCLARÉE]` La règle **conserve la distribution des richesses, par construction**, et les auteurs l'assument : *« dès lors que l'objectif est de sauver les richesses existantes (et non de corriger leur répartition inégale), alors le sauvetage doit préserver la distribution des richesses »*. **Importer AX-3 sans déclarer cette tension exposerait le set à l'accusation de naturaliser l'inégalité par une analogie maritime — et l'accusation serait fondée.**

**Deux éléments la désamorcent, et ils ne valent qu'ensemble :**
1. les auteurs **séparent explicitement** solidarité et responsabilité, la seconde restant traitée par la voie juridique — *« les questions de fautes et de responsabilités sont réglées par ailleurs »* ;
2. la transposition du porteur institue la scission dans le dispositif lui-même : `B = B_solidarité + B_réparation`, **jamais fusionnés**, avec l'interdiction qu'une déduction porte sur une obligation ordinaire.

**Règle d'usage qui en découle :** **AX-3 ne s'invoque jamais sans la scission solidarité / réparation.** Un usage d'AX-3 qui fusionnerait les deux compartiments présenterait une réparation comme un geste solidaire — c'est un `[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ]`.

### §A.18.8 Ce que le versement change pour §A.15.5, et ce qu'il ne change pas

**Il rend le retrait du nœud D contestable sur pièces** : un lecteur dispose de l'énoncé, de sa portée, de son reste de traduction et de sa condition de réfutation. **Il ne valide pas le retrait** — AX-3 reste un axiome **posé**, et le théorème `entite_et_territoire_ne_fusionnent_pas` établit que *la substitution n'est pas une résolution*.

**Et il laisse entier ce que l'instruction P9 a nommé** : si la répartition n'est pas dérivable de l'agrégation, quelque chose doit la produire — une règle posée d'avance et un porteur pour l'appliquer. **Le verrou n'est pas dissous par AX-3, il est déplacé du formel vers l'institutionnel.** C'est l'objet de NT-ARCH §4.2ter.

### §A.18.9 `[LACUNES ET LIMITES DE CETTE SECTION]`

1. **Source primaire non lue par le rédacteur de la présente section.** Demonsant et al. 2026 a été lu intégralement par le porteur ; les verbatims repris ici viennent de ses trois notes. `[CITATION AU SECOND DEGRÉ — patron W-1d.]`
2. **Aucune position adverse n'a été recherchée.** La critique de l'analogie maritime — en particulier sur le caractère fermé et dénombrable de l'expédition — est prévisible et non instruite. **Les auteurs la signalent eux-mêmes** : l'analogie est « indiscutablement à manier avec précaution », et leur piste « ouvre en réalité autant de questions qu'elle n'en ferme ».
3. **Rattachement de famille.** La fiche d'origine ne range AX-3 dans aucune des six familles d'axiomes ; **AX-3 relève de la famille 2, institutionnelle** — §A.15.0.
4. **Les travaux amont sur l'histoire de la règle n'ont pas été lus** — Arruda 2022, Fusaro 2023, UNCTAD 1991, Landes & Posner 1978, Demonsant et al. 2023 : la caractérisation de la permanence repose entièrement sur l'article de 2026.
5. **AX-3 n'a jamais été éprouvé sur un cas du set.** Sa condition de réfutation est écrite et non testée.

---

## §A.19 Règles d'édition du set

### §A.19.1 Statut

Les trois règles de cette section portent sur le **texte du modèle** : comment il change, comment ses changements se tracent, comment ses états se nomment. Elles ne portent ni sur le monde (ce ne sont pas des axiomes), ni sur une écriture de registre (ce ne sont pas des conventions), ni sur la forme d'une inscription démontrable (ce ne sont pas des théorèmes), et elles ne sont pas des règles de second ordre : une RSO confère un statut à un acte **du modèle** sur un registre (§A.16.2). Elles ne sont pas des nœuds du graphe de dépendances.

`[HOMONYMIE DÉCLARÉE]` Dans cette section, « inscription » désigne la **modification d'un fichier du set** ; ailleurs dans le set, une écriture d'un registre. Les deux sens ne se substituent pas.

`[QUESTION OUVERTE]` Tenir le set comme **registre de lui-même** — ce que suggère le garde-fou de réflexivité de NT-G4 §7 (« le MRC est lui-même un registre de type comptable ») — ferait de R-TRAÇAGE une candidate RSO ; RSO-6 note au contraire que le set n'applique pas AX-7 à lui-même. La question n'est pas instruite (fichier d'état, §2).

*Porteur :* porteur MRC. *Horizon :* institutionnel, révisable. *Lieu d'application :* le fichier d'état `_ETAT_INSCRIPTION_v5.7.md`, hors manifeste.

### §A.19.2 R-TRAÇAGE

1. **Source unique.** Toute inscription dans un fichier du set produit une ligne au registre des inscriptions du fichier d'état. Une inscription sans ligne au registre est non tracée.
2. **Les notes sont des pièces, pas la source.** Une note de décision datée reste le lieu du raisonnement et du détail d'exécution ; elle est rattachée à une ligne du registre, elle ne la remplace pas.
3. **Portée déclarée.** Chaque ligne déclare si elle touche le **set**, le **chantier de preuve** (ProfReg / Lean), ou ni l'un ni l'autre.
4. **Décisions en attente.** Tout marqueur de décision de porteur déposé dans un fichier du set est reporté aux décisions en attente du fichier d'état.

`[CONDITION DE RÉFUTATION]` La règle est mal posée si, sur trois mois, aucune recherche d'inscription n'a été facilitée par le registre. *Critère :* toute passe porte une ligne au registre le jour même.

### §A.19.3 R-PRÉSENT

Les fichiers du set ne portent ni numéro de version antérieure, ni récit de rédaction (« corrigé le… », « la rédaction antérieure… », identifiants de décisions comme provenance, mentions de sauvegardes ou d'archives). Ce qui a changé, et quand, s'inscrit au fichier d'état. Les marqueurs du régime (`[PLAUSIBLE, NON VÉRIFIÉ]`, `[LACUNE]`, `[CONDITION DE RÉFUTATION]`, `[OBLIGATION OUVERTE]`, `[INCOHÉRENCE…]`, `[DÉCOUPLAGE…]`…) restent dans les fichiers : ils décrivent l'état présent.

`[CONDITION DE RÉFUTATION]` La règle est mal posée si un énoncé du set devient incompréhensible sans son historique ; l'historique utile est alors réécrit comme justification au présent, non comme récit. *Critère :* recherche mécanique des chaînes de versions antérieures, `backup`, `_archives`, `corrigé le` sur le set : aucune occurrence hors versions de logiciels, normes ou documents externes. `[ÉCART CONSTATÉ]` Des marqueurs datés de correction ou de renommage subsistent dans quelques fichiers (NT-G4, NT-G6, NT-G10, Annexe K) : à trancher au regard de la présente règle.

### §A.19.4 R-VERSION

1. **Un numéro désigne un cycle.** Un état du set s'identifie par le numéro de son cycle **et** l'empreinte globale de son manifeste (« v5.7 @ `<empreinte>` »), comme ProfReg s'identifie par son arbre git. Le numéro seul ne désigne pas un état.
2. **Le gel** produit une copie figée et datée du répertoire du cycle (`MRC_v<n>_gel_<date>/`), en lecture seule, avec son manifeste ; ProfReg et `mrc-script` portent l'étiquette du gel à l'arbre correspondant.
3. **Après le gel de la v5.7**, le répertoire de travail ne porte pas de numéro ; le numéro du cycle suivant n'est attribué qu'à son gel.
4. **Version d'appui.** Toute écriture qui mobilise le MRC déclare sa version d'appui — numéro **et** empreinte du manifeste —, sa portée (usage, évolution, lecture) et, si évolution, sa ligne au registre.
5. **Pas d'écriture croisée.** Une écriture d'usage ne modifie pas le set ; un cas qui appelle un changement du modèle produit une proposition.
6. **Déclenchement.** Le gel est déclenché par le premier usage externe. Est un usage externe **un usage qui cite le MRC, avec une application détaillée, dans un texte diffusé** (article, note de mission, chapitre versé, registre livré). Une mention ou une présentation du MRC sans application détaillée ne déclenche pas le gel.

`[CONDITION DE RÉFUTATION]` La règle est mal posée si l'on compte plus de trois gels en six mois sans usage externe correspondant, ou si un état cité par son empreinte ne peut pas être reconstitué. *Critère :* le manifeste de chaque gel vérifie ses dix-sept fichiers (`shasum -c`).

# §B — Mécanisme de renvoi des sources : fiches (Couche 2) → grammaires (Couche 3)

*Solution de rattachement appliquée dans les fiches reproduites en Partie B du fichier Architecture.*

## §B.1 Recensement des sources externes des fiches de Couche 2

| **Fiche**      | **Source externe (telle que citée)**                     | **Domaine**                      |
| -------------- | -------------------------------------------------------- | -------------------------------- |
| F1 Travail     | Zimmermann & Didry (DPQT, qualité/capabilité du travail) | Sociologie/économie du travail   |
| F1 Travail     | Murray (risque / autonomie-subordination / expressivité) | Qualité de l'emploi              |
| F1 Travail     | Gibson-Graham (communalité de travail)                   | Performativité économique        |
| F1 Travail     | Tronto / Fisher-Tronto (care)                            | Éthique du care                  |
| F1 Travail     | Nussbaum (capabilités plancher)                          | Justice / capabilités            |
| F1 Travail     | Ostrom (gouvernance des communs)                         | Communs                          |
| F2 Milieu      | Plumwood (co-dégradations)                               | Écoféminisme                     |
| F2 Milieu      | Descola (ontologies relationnelles)                      | Anthropologie de la nature       |
| F2 Milieu      | Latour (agentivité des non-humains)                      | Anthropologie / STS              |
| F2 Milieu      | Jonas (responsabilité envers le vivant)                  | Éthique de la responsabilité     |
| F2 Milieu      | Nussbaum (capabilités non-humaines)                      | Justice / capabilités            |
| F2 Milieu      | Berque, Stépanoff, Marlin (milieu vécu, attachements)    | Mésologie                        |
| F3 Sémantique  | Ganter & Wille (Analyse Formelle de Concepts)            | Méthode formelle (non normative) |
| F3 Sémantique  | Sperber (attracteurs culturels)                          | Cognition culturelle             |
| F3 Sémantique  | Fricker (injustice herméneutique)                        | Justice épistémique              |
| F3 Sémantique  | Haraway, Gibson-Graham (inscription corpus)              | Savoirs situés / performativité  |
| F4 Existentiel | Jonas (appel\_immanent, irréversibilité)                 | Éthique de la responsabilité     |
| F4 Existentiel | Fricker (R-HERMENEUTIQUE)                                | Justice épistémique              |
| F8 Comptable   | Richard, Bensadon & Rambaud 2024 (IFRS / PCG)            | Comptabilité financière          |
| F8 Comptable   | Rambaud 2019 (comptabilité CARE) *(→ Rambaud 2015, thèse Dauphine)* | Comptabilité écologique          |
| F8 Comptable   | Dumeaux 2025 (juste prix écologique)                     | Valuation écologique             |
| F8 Comptable   | Bahougne 2020 (droit de la comptabilité publique)        | Droit comptable                  |
| F8 Comptable   | CNoCP 2016-02 (normes comptables publiques)              | Normalisation comptable          |

## §B.2 Sources déjà rattachables à une grammaire existante (renvoi direct)

Pour ces sources, aucune création ni complétion n'est nécessaire : elles figurent déjà (ou ont leur place naturelle) dans la bibliographie d'une NT-G existante. La fiche remplace la citation inline par un renvoi « → NT-Gx ».

| **Source (fiche)**             | **Grammaire d'accueil**   | **Statut**            |
| ------------------------------ | ------------------------- | --------------------- |
| Gibson-Graham (F1, F3)         | NT-G4 Performativité      | Déjà présent — renvoi |
| Haraway (F3)                   | NT-G4 Performativité      | Déjà présent — renvoi |
| Tronto/Fisher (F1)             | NT-G3 Soin                | Déjà présent — renvoi |
| Plumwood (F1, F2)              | NT-G3 Soin                | Déjà présent — renvoi |
| Nussbaum (F1, F2)              | NT-G7 Justice             | Déjà présent — renvoi |
| Fricker (F3, F4)               | NT-G7 Justice (et NT-G10) | Déjà présent — renvoi |
| Ostrom (F1)                    | NT-G6 Communalité         | Déjà présent — renvoi |
| Jonas (F2, F4)                 | NT-G2 Responsabilité      | Déjà présent — renvoi |
| Sperber (F3)                   | NT-G1 Évolutivité         | Déjà présent — renvoi |
| Berque, Stépanoff, Marlin (F2) | NT-G5 Mésologie           | Déjà présent — renvoi |

## §B.3 Grammaire à COMPLÉTER (sans ajout au compte) : NT-G5 Mésologie

Descola (ontologies relationnelles) et Latour (agentivité des non-humains) n'ont pas de grammaire d'accueil. Plutôt que de créer une grammaire « ontologies », la solution la plus économe est de COMPLÉTER NT-G5 Mésologie : la médiance de Berque (relation constitutive entité/milieu, déjà au cœur de NT-G5) est conceptuellement continue avec l'anthropologie de la nature de Descola et l'agentivité distribuée de Latour. \[PLAUSIBLE — continuité conceptuelle Berque/Descola/Latour à valider sur sources primaires.\] Cette complétion n'augmente pas le nombre de grammaires.

| **Source à ajouter**                          | **NT-G5 — emplacement proposé**                 | **Justification**                                               |
| --------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------- |
| Descola, Par-delà nature et culture (2005)    | Bloc B (présences non-humaines) + bibliographie | Ontologies relationnelles = cadre du milieu vécu non-humain     |
| Latour, Politiques de la nature / Face à Gaïa | Bloc B + bibliographie                          | Agentivité des non-humains = substrat de appel\_entendu\_milieu |

## §B.4 Grammaires ajoutées (2 — total de 12)

Deux familles de sources n'ont aucune grammaire d'accueil possible parmi les dix existantes, car elles relèvent de domaines normatifs distincts. Elles justifient deux ajouts, qui portent le total à exactement 12.

### §B.4.1 NT-G11 — G-TRAVAIL (grammaire de la qualité et de la capabilité au travail)

Accueille les sources de sociologie/économie du travail de F1 qui ne relèvent ni du care (NT-G3) ni des capabilités générales (NT-G7) : Zimmermann & Didry (dispositif de promotion de la qualité du travail, capabilité au travail) et Murray (risque / autonomie-subordination / expressivité). F1 consomme cette grammaire. Distinction de périmètre : NT-G3 porte le care (travail attentionnel) ; NT-G7 porte les capabilités comme catégorie de justice ; G-TRAVAIL porte spécifiquement la qualité de l'emploi et la reconnaissance du salarié comme juge de son métier (C-DPQT, C-MURRAY). Sans cette grammaire, ces sources resteraient orphelines en Couche 2. \[Décision du porteur : G-TRAVAIL est distincte de NT-G7 — la capabilité au travail (Zimmermann-Didry) est une spécialisation, non un synonyme de la capabilité générale (Nussbaum/Sen).\]

### §B.4.2 NT-G12 — G-VALUATION (grammaire comptable et de la valuation)

Accueille toutes les sources comptables de F8 : Richard, Bensadon & Rambaud **2018** (mouvements types IFRS/PCG, équation du bilan) ; **Rambaud 2015** (comptabilité CARE — thèse Dauphine) ; Dumeaux 2025 (juste prix écologique — réf. canonique fixée) ; **Bahougne & Camus 2020** (droit de la comptabilité publique) ; CNoCP 2016-02 (document primaire localisé). Elle est aussi le porteur naturel des sources de valuation déjà mobilisées par NT-ARCH/F8 (Callon, Çalışkan & MacKenzie sur la performativité des instruments de mesure). F8 consomme cette grammaire. Bénéfice de cohérence : la gouvernance des valorimètres (chantier B4 — source\_valuemetre OBLIGATOIRE) trouve son ancrage de Couche 3 ; un seuil comptable sans grammaire d'accueil est précisément l'instrument performatif non gouverné que le régime cherche à éviter (cf. NT-G4). \[DÉCOUPLAGE DE RÉGIMES\] potentiel entre F8 (Couche 2) et l'absence de grammaire : levé par cet ajout.

## §B.5 Source méthodologique non grammaticale (hors compte) : Ganter & Wille

L'Analyse Formelle de Concepts (Ganter & Wille) est une méthode formelle, non une grammaire normative : elle outille C-TCFP (treillis de concepts) sans porter d'engagement éthico-politique réfutable. La rattacher à une grammaire serait un \[CHANGEMENT DE BASE NON TRACÉ\] (confusion méthode/grammaire). Solution : la renvoyer à une annexe méthodologique/technique (Annexe G — formalisation), non à une NT-G. N'entre pas dans le compte des 12.

## §B.6 Solution d'ensemble — tableau de décision

| **Action**                   | **Grammaires concernées**                                                         | **Effet sur le compte** |
| ---------------------------- | --------------------------------------------------------------------------------- | ----------------------- |
| Renvoi direct (déjà présent) | NT-G1, G2, G3, G4, G6, G7                                                         | 0 (10 → 10)             |
| Complétion                   | NT-G5 Mésologie (+ Descola, Latour)                                               | 0 (reste 10)            |
| Ajout 1                      | NT-G11 G-TRAVAIL (Zimmermann-Didry, Murray)                                       | \+1 (→ 11)              |
| Ajout 2                      | NT-G12 G-VALUATION (Richard, Rambaud, Dumeaux, Bahougne, CNoCP, Callon-MacKenzie) | \+1 (→ 12)              |
| Hors grammaire               | Ganter & Wille → Annexe G méthodologique                                          | 0                       |

Résultat : 12 grammaires exactement, plafond respecté. Toute source externe d'une fiche de Couche 2 dispose alors d'une grammaire (ou annexe méthodologique) d'accueil ; les fiches remplacent leurs citations inline par des renvois « → NT-Gx ».

## §B.7 Mécanisme de renvoi à appliquer dans les fiches

Dans chaque fiche de Couche 2, le paragraphe « Fondements théoriques : … » est remplacé par une ligne de renvoi, par exemple pour F1 : « Fondements : care → NT-G3 ; capabilités → NT-G7 ; communs → NT-G6 ; performativité → NT-G4 ; qualité et capabilité au travail → NT-G11 (G-TRAVAIL). » Pour F8 : « Fondements comptables et valuation → NT-G12 (G-VALUATION). » Aucune source externe ne subsiste alors dans le corps des fiches.

## §B.8 Lacunes et limites

\[LACUNES ET LIMITES\] (1) La recevabilité des deux nouvelles grammaires (G-TRAVAIL, G-VALUATION) relève d'une décision du porteur ; une alternative existe pour G-TRAVAIL (absorption dans NT-G7). (2) Les références exactes (édition, pagination) de Descola, Latour, Zimmermann & Didry, Murray, Callon-Çalışkan-MacKenzie ne sont pas vérifiées sur source primaire ici — \[PLAUSIBLE, NON VÉRIFIÉ\], à inscrire au fichier d'avancement comme verrous bibliographiques avant rédaction des notes. (3) Le présent document propose la solution ; il ne crée pas encore les notes NT-G11/G12 ni n'applique les renvois dans les fiches — ce sont les étapes d'implémentation suivantes. (4) La continuité Berque/Descola/Latour (complétion NT-G5) est une inférence de cohérence, non une thèse attribuée aux auteurs.

---

# §C — Questions méthodologiques et programme de preuve ProfReg

## §C — Partie I : Questions méthodologiques à approfondir

### C-Q1. Frontière procédural / formel calculable

La mise en cohérence ajoute aux fiches des règles (déclenchements, cascades, obligations de déclaration). Question : lesquelles sont des invariants formellement prouvables (transitions, typages) et lesquelles restent des conventions procédurales ? Méthode proposée : pour chaque règle ajoutée, déclarer son régime (P = procédural / F = formel) ; toute règle marquée F sans théorème associé est un \[ENGAGEMENT SANS SYMÉTRIE\] jusqu'à preuve. Enjeu de cohérence : ne pas présenter une cohérence verbale comme une cohérence calculée.

### C-Q2. Gouvernance des valorimètres : déclaré vs calculé

fractionactorielle est gouvernée par déclaration : ce qui est établi par ProfReg est l'obligation de déclaration (invariant de typage **`fraction_exhibe_sa_source`**) et la réfutation du foncteur de calcul candidat (`CB3_candidate_not_oplax_monoidal`) ; l'inexistence générale d'un calcul reste une lacune déclarée. Par analogie, F8 impose source\_valuemetre OBLIGATOIRE. Question méthodologique : où passe la frontière entre un seuil légitimement gouverné par déclaration et un seuil qui pourrait être calculé par un dispositif gouverné sans arbitraire ? Sans critère explicite, l'obligation de déclaration risque d'être soit trop large (bloque des calculs légitimes), soit trop étroite (laisse passer des seuils performatifs). À instruire avec NT-G12 (G-VALUATION) et NT-G4.

### C-Q3. Synchronisation des champs de phase (risque de changement de base non tracé)

Les phases INVENTAIRE-ASSETS-ACTIFS et REPRESENTATION-PROSPECTIVE sont décrites dans NT-ARCH, instanciées dans F2/F4, et doivent s'écrire via le schéma de l'Architecture Multi-Agents et de F8. Trois localisations = risque de \[CHANGEMENT DE BASE NON TRACÉ\] si les noms/typages divergent. Méthode : un schéma d'écriture unique (source de vérité) dont fiches et NT-ARCH dérivent, avec test de non-divergence.

### C-Q4. Commutativité des couplages bidirectionnels non encore prouvés

Trois couplages ont leur forme établie, et aucun n'est une commutation inconditionnelle : M↔R **ne commute pas** et se ferme par l'acte conjoint voix inscrite + audit de genèse (PR-5, `le_carre_MR_ne_commute_pas`, `le_carre_ferme_apres_l_acte`) ; J↔E ne se ferme que sur révision inscrite (VJE, `VJE_carre_ne_commute_pas_sans_revision`, `VJE_ferme_apres_revision_externe`) ; E↔A est un **cycle** dont les deux ordres diffèrent, et ce qui est exigé est la terminaison (PR-9, `les_deux_ordres_different`, `un_canal_qui_ne_relit_pas_le_seuil_termine`). Reste hors Mathlib la 2-cellule du triangle NT-G7 ↔ NT-G2 ↔ NT-ARCH (CONV-2). Question ouverte : pour les autres couplages de la table NT-ARCH, lesquels exigent une commutation, lesquels une fermeture par un acte, lesquels une terminaison ? Un couplage dont la forme n'est pas établie reste \[DÉCOUPLAGE DE RÉGIMES\] potentiel à signaler.

### C-Q5. ACT-ARCH-001 — **CLOSE**

**Ce qui est acté** (NT-ARCH §7bis) : la combinaison `ATTRIBUEE` + `seuilentreecommunautemorale = NONDECLARE` est **interdite**, comme invariant de Couche 1.

**L'instant où l'interdiction mord** — « à l'attribution » (régime strict) ou « à une échéance nommée » (repli) — est fixé par l'**option C** : l'invariant est écrit **paramétré par l'échéance**, et le régime strict en est démontré comme l'instance où l'échéance vaut l'instant de l'attribution. Voir NT-ARCH §7bis, `ProfReg/PR3_AttributionSeuil.lean` et `Decision_PR3_2026-09-07.md`.

**Le théorème ProfReg que cette réponse conditionnait — PR-3 — est compilé** : 14 théorèmes, dont 13 ne dépendant d'aucun axiome, 0 `sorry`, 0 `sorryAx`.

### C-Q6. Autoréférentialité du registre (G-PERFORMATIVITE)

Le registre se déclare lui-même acteur tracé (C-INSCRIPTION) : risque qu'il se valide lui-même. La réponse partielle (DIDs/VCs) est cryptographique, non architecturale. Réponse partielle : RECHERCHE\_INTERVENTION est une **phase** de C-ENQUETE-V5 (NT-ARCH §B.2ter) dont le constat n'est recevable qu'attesté par une instance **distincte du porteur de l'instrument** et **associant les personnes concernées** — c'est le critère qui distingue une validation interne d'une validation par tiers ; PR-57 en établit la forme (`le_porteur_ne_s_atteste_pas`, `sans_les_concernes_pas_de_constat`, `l_enquete_rend_visible_la_contre_performativite`). Reste ouvert : la validation du registre lui-même (C-INSCRIPTION), hors d'un instrument mis à l'épreuve.

### C-Q7. SUFFICIENCY (NT-G7 / NT-ARCH) — **CLOSE**

**\[CHANGEMENT DE BASE TRACÉ\] CLOS — acte du porteur.** SUFFICIENCY désigne un unique seuil de suffisance, au sens satisminien de Gosseries 2011 §2 et de Meyer & Roser 2009 ch. 8. NT-G7 l'emploie comme **critère de justice** ; NT-ARCH l'énumère comme **valeur déclarable** de `principeintergenerationnel` (Couche 0). Les deux usages portent sur le même objet à deux niveaux de la même architecture : il n'y a pas changement de base, mais **changement de place** — un objet gouverné n'est pas un principe de gouvernance.

> **Sources.** **Meyer & Roser, « Enough for the Future »**, ch. 8 de Gosseries, A. et Meyer, L. H. (dir.), *Intergenerational Justice*, Oxford University Press, 2009, p. 219-248 : conception *sufficientarienne* explicitement adossée au **bien-être** des personnes futures (« the welfare rights and distributive justice claims of future people » ; « we have strong and particular reasons for interpreting intergenerational justice in terms of a sufficientarian conception of justice »). C'est l'usage NT-G7 de SUFFICIENCY comme seuil de bien-être : il est **vérifié sur source primaire**.
>
> **Gosseries, Axel, « Qu'est-ce que le suffisantisme ? », *Philosophiques*, vol. 38, n° 2, automne 2011, p. 465-492** (DOI 10.7202/1007460ar), lu intégralement. §2 : « Il considère que les titulaires d'obligations distributives en ont *fait assez* à partir du moment où chacun des bénéficiaires potentiels *a assez*. Et ce “avoir assez” n'est pas défini en termes relatifs […] Il l'est par rapport à un **seuil absolu**, typiquement exprimé en termes de *besoins de base*. » ; « le suffisantiste exige la **satisfaction d'un niveau minimum** […] égalitarisme du *satismin* ». **Même forme que Meyer & Roser 2009, p. 220** (« well-being above a certain given threshold »). Et c'est **Gosseries lui-même** qui adosse la conception intergénérationnelle à Meyer & Roser (§4 et bibliographie) : le rapprochement n'est pas une inférence du porteur.
>
> **Ce que NT-ARCH fait de SUFFICIENCY.** NT-ARCH §6 n'en fait pas un principe de gouvernance : il en fait **une valeur énumérée d'une primitive de Couche 0**, `principeintergenerationnel ∈ {NON-DECLINE / BETTER-FUTURE / SUFFICIENCY / NARROW-PATH / NON_DECLARE}`, glosée en NT-G2 §7 par « garantir un seuil suffisant à chaque génération » — contenu **distributif**. Aucune occurrence de SUFFICIENCY dans le set ne lui donne d'effet sur `legitimiterepresentant`, sur `conditionrefutation` ni sur le déclenchement de REPRESENTATION-PROSPECTIVE. **La gouvernance est dans l'obligation de déclarer, pas dans la valeur déclarée.**
>
> `[CONDITION DE RÉFUTATION]` Cette lecture tombe si l'on exhibe dans le set un point où SUFFICIENCY produit un **effet** sur la représentation elle-même, et non seulement sur le contenu de l'obligation transmise. Le balayage est textuel et peut avoir manqué une formulation périphrasée.
>
> `[RÉSERVE]` L'équivalence tient sur la **forme** du seuil, non sur sa **métrique** : Gosseries traite explicitement la métrique comme variable libre de la famille suffisantiste (§7). Meyer-Roser prennent le bien-être ; la version « typique » décrite en 2011 prend les besoins de base. Deux instances du même schéma, pas la même instance.
>
> `[LACUNE RÉSIDUELLE — hors C-Q7]` Ni Gosseries 2011 ni le volume de 2009 (contrôlé par extraction intégrale et recherche plein texte) ne contiennent **aucune occurrence** de NON-DECLINE, BETTER-FUTURE ou NARROW-PATH, ni de l'argument d'a-légitimité des politiques envers le futur. **Gosseries 2023 n'est pas au corpus.** Sur la **taxinomie à quatre principes**, la vérification page-à-page de Gosseries 2023 reste due ; elle n'est pas C-Q7 et demeure ouverte (cf. tableau §5). Ce qui est sourcé, c'est **une valeur sur quatre** — la seule qui posait un problème de double usage.
>
> **Jonas**, *Le Principe Responsabilité* (fondement de R-INTERDIT-ABSOLU) et **Nussbaum**, *Frontiers of Justice* (fondement de SENTIENCE) sont en biblio : leurs mentions `[VÉRIFIÉ]` sont recontrôlables.
>
> Détail de l'instruction : `Gosseries_Suffisantisme_2011_2026-09-08.md`.

### C-Q8. Mur d'individualisme vs habitabilité systémique (tension T5)

R-HABITABILITE-CAPABILITE couple une capabilité individuelle (Nussbaum) à une habitabilité systémique (Morizot-Neyret). \[DÉCOUPLAGE DE RÉGIMES\] assumé. Question méthodologique : comment instrumenter cette tension dans les fiches (F2, F4) sans la lisser — c'est-à-dire en gardant trace de ce que chaque registre exige séparément ? À traiter dans NT-G7 §2.

### C-Q9. Règle de priorité F6/F10 (co-activation) — **CLOSE**

Quand injustice épistémique (F6, NT-G7) et formalisme délibératif (F10, NT-G10) se co-activent, la règle `R-PRIORITE-F6-F10` (NT-G10 §6.2, ancrée Le Naour 2024) fixe l'ordre : F6 traite la précondition herméneutique, puis F10 reprend la légitimité du processus. PR-7 en établit la forme : la co-activation a un ordre unique (`la_coactivation_a_un_ordre_unique`), la priorité n'est pas un veto (`la_priorite_n_est_pas_un_veto`), F10 ne certifie pas sous F6 actif et reprend après traitement (`F10_ne_certifie_pas_sous_F6_actif`, `F10_reprend_apres_traitement`). PR-7 ne juge pas l'injustice (`PR7_ne_juge_pas_l_injustice`).

### C-Q10. Méthode de levée des verrous bibliographiques (A/B/C)

Le plan de vérification distingue lecture approfondie (A), référence à établir (B), pages à préciser (C). Question méthodologique : ordonnancement — B avant diffusion externe, A avant extension conceptuelle, C avant inscription page-à-page. Priorité immédiate : les deux sources de NT-G11 (Zimmermann-Didry, Murray), en catégorie B, conditionnent la solidité de la nouvelle grammaire.

## §C — Partie II : Programme de preuve ProfReg

**Le programme de preuve PR-1 → PR-25 est compilé.** La référence — énoncés, fichiers, décompte — est `MRC_v5.7_ProfReg_Consolide.md` §7 ; le décompte en vigueur figure en §D.3. Les théorèmes cités au niveau des fiches de Couche 2 sont ceux du Consolidé : la non-calculabilité de la fraction (F8 par analogie) relève de **CONV-1 + `fraction_exhibe_sa_source`** ; la REPRESENTATION-PROSPECTIVE planétaire (F4) relève de **PR-8** (`representation_pratique_refutation`, `le_defaut_exige_la_refutation`) et de **CONV-6 / CONV-7** ; `inventaire_nonempty_required` (InventaireNonVide F2) est une lecture du type, avec pour témoin `inventaire_nonempty_discrimine`.

### C-II.1 Énoncés compilés du programme

**PR-2** est compilé dans `LotL2_PR2_PR14.lean` ; **PR-3** dans `ProfReg/PR3_AttributionSeuil.lean` (§C-Q5) ; **PR-6** dans `VJEVerification.lean` — la biconditionnelle AM-G7-04 est fermée ; **PR-4, PR-7, PR-8** sont compilés ; PR-11 à PR-25 s'y ajoutent. **PR-26 à PR-59** formalisent, hors programme, des règles et conventions du set (Consolidé §2, §7).

### C-II.2 PR-1 et PR-10 : source déclarée et statut du seuil

**PR-1** (tout valorimètre/seuil de F8 exige une source déclarée — F8 / NT-G12 / B4) est porté par **CONV-4** (§A.15) et `fraction_exhibe_sa_source`. **PR-10** (`seuil_valuatif_must_declare_status`, `PR10_StatutSeuil.lean`, 16 théorèmes) : toute mobilisation d'une primitive `seuil-valuatif` déclare le **quintuplet** « statut du seuil » — généralisation hors-F8 de PR-1 ; cinquième terme : CONV-9 (§A.14).

> **Extension déclarée de PR-1 à l'articulation CARE/CENP.** Le périmètre de PR-1 (**CONV-4 / `fraction_exhibe_sa_source`**) est étendu par déclaration à `obligationpreservation` : la source déclarée doit pointer vers des **normes opposables** (p. ex. CSRD, DCE) plutôt que vers des valeurs arbitraires. Cette extension est un énoncé de Couche 1 **déclaré, non transcrit ni compilé** : `[PLAUSIBLE, NON VÉRIFIÉ]` en régime formel calculable ; elle constitue une **inscription unique** — la même exigence ne doit pas être réinscrite séparément au titre des corrections d'architecture (C1/B4) ni de l'articulation écologique (NT-ARCH §8.6.2), qui y renvoient.

### C-II.3 Hors Mathlib actuel — lacunes déclarées

| **ID**                   | **Énoncé**                                                    | **Statut**                                 |
| ------------------------ | ------------------------------------------------------------- | ------------------------------------------ |
| G.9.3 2-cellule complète | Commutativité de base ProfReg complète (framed bicategories). | Lacune déclarée — horizon v6.x             |
| CB3 inexistence complète | Aucun foncteur lax monoïdal V1→V3.                            | Ouvert — catégories enrichies hors Mathlib |
| Tension T4               | Risque de financiarisation du registre DÉBIT-CRÉDIT.          | **Hors programme de preuve** : question politique, suivie en NT-G12 (gouvernance des valorimètres, B4) et NT-G4 (vigilance performative) |

### C-II.4 Règle d'écriture « prouvé »

**N'est écrit « prouvé » que ce qui est compilé et audité.** L'interdiction reste entière pour tout le reste — invariants actés non transcrits, résolutions procédurales (V4c, V10b), lacunes déclarées (CB3 général, 2-cellule G.9.3). Tout énoncé non compilé est signalé \[PLAUSIBLE, NON VÉRIFIÉ\] en régime formel calculable, même s'il est procéduralement cohérent.

**Crible mécanique.** `ProfReg/crible_references.sh` vérifie que tout théorème cité existe. Il ne vérifie **pas** que l'énoncé cité dit ce qu'on lui fait dire.

### C-II.4bis Énoncés réfutés par leur propre formalisation

> **PR-5** : le carré M↔R **ne commute pas** (`le_carre_MR_ne_commute_pas`). Ce qui le ferme est un **acte** (voix inscrite + audit), non un calcul — même figure que VJE. C'est une machine d'états, non une lacune hors Mathlib.
>
> **PR-9** : le set décrit **les deux sens** du canal E→A ; le couplage **est** un cycle (`le_couplage_est_un_cycle` ; `les_deux_ordres_different`). Ce qui est formulable est la **terminaison**, et elle se vérifie sur le canal seul — l'instrumentation `signalversaffectif`, déclarée bloquante, ne l'est pas.
>
> `[ENSEIGNEMENT]` **Trois des cinq nœuds réputés hors chemin ou bloqués l'étaient sur la foi d'un énoncé non vérifié.** La règle qui en découle, homologue de celle tirée de PR-11 : *avant de déclarer un nœud bloqué, vérifier que son énoncé est exact.*

### C-II.4ter Paliers PAL-1 → PAL-6′ et décision macroéconomique

> Les six paliers sont **écrits comme énoncés, avec leur critère de passage** (`Etape4_Six_Paliers_2026-09-08.md`). **Cinq sont clos ; PAL-4 l'est sous la réserve de transposition que déclare AX-14** (Longino 1990 ; fiche `ProfReg/Fiche_Axiome_A14_Longino_Objectivite_Sociale_2026-09-28.md` ; §A.15.0). **Aucun ne l'est en régime formel calculable, et c'est la conclusion à porter.**
>
> **Décision du porteur — la macroéconomie est déclarée procédurale.** La conclusion macroéconomique du MRC — principes post-croissance, volume d'émission, articulation à la comptabilité nationale — **ne fait pas partie du programme de preuve**, et rien dans la thèse ne la présente comme démontrée : PAL-6 reste procédural et est déclaré comme tel. **La moitié « marquage » de PAL-6′ est démontrée** (PR-11, PR-12, PR-13, PR-19, CONV-12, CONV-13) ; ce qui est procédural est **le pas du dispositif d'entreprise vers l'agrégat national**, et lui seul. Restent explicitement non traités et à écrire comme tels : le **volume d'émission** ; le fait que l'argument du retrait du nœud D **suppose une émission sans créance qui n'existe pas** ; et la tension **T4**, réserve déclarée permanente.
>
> **Appuis de PAL-1 et PAL-5.** **PR-24** formalise le maillon **L1** — *ce que la présence perd, l'inscription le garde* — et donne à **PAL-1 un appui formel**, en réutilisant `liste_close_exclut_toujours` (PR-16). **PR-25** donne à **PAL-5** son appui : un observateur privé du registre financier **décide quand même** l'existence de la contrepartie. **Borne de l'appui de PAL-1** : `PR24_ne_dit_pas_que_le_registre_suffit` — l'inscription exclut aussi ; elle supprime la perte, non l'exclusion.

**Horizon v6.x** : CB3 complet, 2-cellule G.9.3 (§C-II.3).

**Lacunes et limites de cette note**

\[LACUNES ET LIMITES\] (1) Le partage P/F (question C-Q1) n'est pas encore appliqué règle par règle dans les fiches actualisées. (2) Le crible des références (§C-II.4) ne contrôle que l'existence des théorèmes cités, non la fidélité de l'énoncé cité.

---

# §D — Suivi : amendements, théorèmes, verrous, chantiers

> **Articulation avec le fichier d'état.** Cette section tient l'état des amendements, théorèmes, verrous bibliographiques et chantiers. Le suivi des **décisions prises et en attente** est tenu exclusivement dans `MRC_v5.7/_ETAT_INSCRIPTION_v5.7.md` (source unique) : en cas d'écart, le fichier d'état prime.

## §D.1 Amendements de grammaire et d'architecture (A/B) — état

| **ID** | **Porte**       | **Objet**                                                           | **Statut**                                                             |
| ------ | --------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| A1     | NT-G2           | Sujet collectif (C-SUJET-COLLECTIF)                                 | Intégré ; cohérence §C-SUJET-COLLECTIF vérifiée             |
| A2     | NT-G2+NT-G7     | R-HABITABILITE-CAPABILITE, condition d'identification des individus | Intégré ; vérifié V1 (V1\_commutatif) ; commutation caractérisée sous cohérence déclarée (`V1_commute_ssi_coherence`)                                  |
| A3     | NT-G2+NT-G7     | puissanceaffirmative, HABITABILITE\_PRODUCTIVE                      | Intégré ; vérifié V1                                                   |
| A4     | NT-G2 / NT-ARCH | Taxinomie Gosseries 2023 (4 principes), abandon « Gosseries 2025 »  | Intégré ; SUFFICIENCY : \[CHANGEMENT DE BASE TRACÉ\] **clos** (cf. §C-Q7) ; taxinomie à 4 principes non sourcée sur primaire |
| A5     | NT-G2+NT-G8     | Couplage bidirectionnel G-MIMETIQUE↔G-RESPONSABILITE (sens M→R)     | Documenté NT-G8 ;   **réfutée par PR-5** (`le_carre_MR_ne_commute_pas`) |
| B1     | NT-ARCH         | regimeobligation en Couche 0 + C-STATUT-DETTE                       | Intégré ; vérifié V2                                                   |
| B2     | NT-ARCH         | Phase INVENTAIRE-ASSETS-ACTIFS, typage InventaireNonVide            | Intégré ; vérifié V3/V4                                                |
| B3     | NT-ARCH         | Phase REPRESENTATION-PROSPECTIVE                                    | Intégré ; vérifié V10c                                                 |
| B4     | F8              | source\_valuemetre OBLIGATOIRE — source déclarée et vérifiable ; DID = forme possible  | À porter dans F8 (Couche 2) — cf. §6                                   |
| B5     | NT-G7           | typecapabilitecentrale, **3 valeurs à sources distinguées** — scission, NT-G7 §3.1ter | Intégré NT-G7 §2                                                       |
| B6     | NT-G4/NT-G6     | R-PERMIS-PERFORMATIF (G-PERF↔G-RESP)                                | Proposé — à porter en Couche 2/3 — cf. §6                              |

## §D.2 Amendements Hache (2011) — P1 à P4

Source : note « Référence à Émilie Hache dans les grammaires Responsabilité et Justice ». Effet net : montée du statut épistémique (PLAUSIBLE → VÉRIFIÉ) sans toucher aux théorèmes formels.

| **ID** | **Emplacement**                    | **Modification**                                                         | **Statut**                                                      |
| ------ | ---------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------- |
| P1     | NT-G2 §2.1 + biblio ; NT-G7 Bloc D | REVISIONCONCEPTUELLE ancrée Hache 2011 ch.2 p.55 + ch.1 p.31-32          | VÉRIFIÉ (réserve édition papier)                                |
| P2     | NT-G2 §5bis                        | Positionnement Hache/Jonas ; couplage Jonas↔Hache déclaré bidirectionnel | \[DÉCOUPLAGE NON DÉCLARÉ\] levé                                 |
| P3     | NT-G2 (règle de révision)          | source\_revision\_capabilite ancrée Hache ch.4 p.102-103                 | VÉRIFIÉ                                                         |
| P4     | NT-G2 §2.1                         | Hache récuse le seuil d'entrée ; tension Hache/Nussbaum-Jonas explicitée | \[INCOHÉRENCE INTER-COUCHES — couche 0\] documentée, non lissée |

## §D.3 Vérifications formelles ProfReg (Lean 4 / Mathlib)

**Le décompte en vigueur est tenu au seul `MRC_v5.7_ProfReg_Consolide.md` §1** (604 = 584 + 20 ; détail, audit et obligation de confirmation).

Blocs : V1 (carré F4–F6) ; V2 (compatibilité B1/R1) ; V3 (carré B1–B2 — `V3_commutatif`, forme 1 ; commutation sur les chemins admissibles : PR-51, CONV-2 étendue) ; V4 (cascade R-INTERDIT-ABSOLU) ; V10a/V10c (cohérence planétaire) ; V4c (préservation ACTORIEL) ; V10b (carré triangulaire NT-G7↔NT-G2↔NT-ARCH) ; VJE (commutativité J↔E, AM-G7-04 — **levé sous condition de révision inscrite**). Fichiers : BaseCategories, Actors, Interactions, ChangeOfBase, V1–V4 + V4c + V10/V10b + VJE Verification.lean.

| **Amendement**                             | **Vérification**                  | **Statut**           |
| ------------------------------------------ | --------------------------------- | -------------------- |
| A2+A3 (appelimmanent/puissanceaffirmative) | V1\_commutatif                    | VÉRIFIÉ              |
| B1 (regimeObligation + fractionactorielle) | V2 (R1\_preserved\_under\_CB1, …) | VÉRIFIÉ              |
| B2 (INVENTAIRE-ASSETS-ACTIFS)              | V3\_commutatif                    |  `V3_commutatif` : forme 1, jamais appui ; commutation **conclue sur les chemins admissibles**, la règle des pas étant déclarée : **PR-51** (`carre_B1B2_commute_sur_les_chemins_admissibles`) ; **CONV-2** étendue (§A.15.9) |
| Tension T3 (cascade SYSTEMIQUE)            | V4\_cascade\_coherente            | VÉRIFIÉ              |
| AM-G7-08 + AM-ARCH-01 (planétaire)         | V10a + V10c                       | VÉRIFIÉ              |
| ACT-G2-010 (préservation ACTORIEL)         | V4c\_actoriel\_preserved          | RÉSOLU PROCÉDURAL    |
| V10b (carré triangulaire)                  | — (aucun théorème)                 | RÉSOLU PROCÉDURAL — **CONV-2** ; `V10bVerification.lean` ne porte aucun théorème (Consolidé §2) |
| AM-G7-04 (commutativité J↔E)               | `VJE_carre_ne_commute_pas_sans_revision` + `VJE_ferme_apres_revision_externe` | **LEVÉ SOUS CONDITION.** Le carré ne se ferme pas de lui-même ; il se ferme dès qu'une révision est inscrite. |

## §D.4 Chantiers ouverts (à instruire — hors corps des notes)

| **ID**                          | **Description**                                                              | **Statut / blocage**                                                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| ACT-ARCH-001                    | Exclusion ATTRIBUEE + seuil NONDECLARE : règle Couche 2 → invariant Couche 1 | **ACTÉ (NT-ARCH §7bis) ; PROUVÉ (`PR3_AttributionSeuil.lean`, 14 théorèmes, 0 `sorryAx`).** Question temporelle résiduelle tranchée par l'option C — invariant paramétré par l'échéance. Voir §C-Q5 |
| VJE-sansResistance              | resistanceBloquante=false → metaluciditeRequise=false                        | **Compilé (PR-6, `VJEVerification.lean`)** — complète la biconditionnelle AM-G7-04                                                              |
| 2-cellule G.9.3 | Commutativité de base ProfReg complète                                       | Lacune déclarée — framed bicategories hors Mathlib actuel — horizon v6.x                                                                |
| CB3 inexistence complète        | Aucun foncteur lax monoïdal V1→V3                                            | Ouvert — théorie des catégories enrichies hors Mathlib                                                                                  |
| Tension T4                      | Risque de financiarisation du registre DÉBIT-CRÉDIT                          | Question politique, hors Lean 4                                                                                                         |

## §D.5 Verrous bibliographiques — état

| **ID**                                              | **Référence**                                     | **Statut**                                                                    |
| --------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------- |
| ACT-G2-013 RECIPROCITE                              | Gosseries 2009 ch.4 p.119-146                     | LEVÉ                                                                          |
| ACT-G2-013 SUFFICIENCY                              | André & Gosseries 2024 ch.I §II                   | LEVÉ                                                                          |
| ACT-G2-013 NON-AGGRAVATION                          | André & Gosseries 2024 ch.II §IV                  | LEVÉ                                                                          |
| « Gosseries 2025 »                                  | Trilogie RECIPROCITE/SUFFICIENCY/NON\_AGGRAVATION | ABANDONNÉ — \[SOURCE NON VÉRIFIABLE\]                                         |
| Nussbaum 2006                                       | Capabilités non-humaines ch.6                     | LEVÉ — source primaire lue                                                    |
| SUFFICIENCY (NT-G7 vs NT-ARCH)                      | Critère de justice (NT-G7) / valeur déclarable (NT-ARCH) — même seuil | **CLOS** — Gosseries 2011 §2 + Meyer & Roser 2009 ch. 8 ; changement de *place*, pas de base |
| Schlosberg 2007 INTEGRITE\_ECOSYSTEMIQUE            | **p.136 « Recognizing Integrity »** (ext. p.137)  | **LEVÉ** — VÉRIFIÉ SUR SOURCE PRIMAIRE ; terme exact « integrity of systems / autonomous integrity » ; registre normatif/recognitionnel TRANCHÉ |
| Marlin 2022 (NT-G5)               | HDR Bordeaux Montaigne, HAL tel-05218425          | **LEVÉ** — jointe, VÉRIFIÉ ; usage NT-G5 : pratique paysagiste, non gouvernance aquatique |
| Schlager & Ostrom 1992 (NT-G6)                      | Land Economics 68(3) p.249-262, DOI 10.2307/3146375 | **Pagination confirmée (notice éditeur)** — PLAUSIBLE (web) ; VÉRIFIÉ strict possible via PDF accessible |
| Girard 1972/1978, Schwager/Cowdell/Reineke (NT-G8)  | Pagination + correctifs                           | **LEVÉ pour l'essentiel** — Schwager 1987 VÉRIFIÉ (F7 pp.160/229) ; appui séculier : Cowdell 2013 VÉRIFIÉ (non « Goodhart 2003 ») ; Reineke 2014 VÉRIFIÉ ; Girard 1972 : ch. III p.102 VÉRIFIÉ sur TOC (réserve Laffont/Grasset) ; Girard 1978 : VÉRIFIÉ sur fichier à couche texte (Livre I) — **clos** ; les contrôles de pagination ne font pas partie du programme (décision du porteur : le verbatim vérifié fait foi) |

## §D.7 Cartographie Vagues de travail

Les chantiers ouverts sont rattachés à des « Vagues » de travail : Vague B.3 (canal E→A, F5) ; Vague C.1 (canaux de retour J→E, M→R commutativité ProfReg, phase REVISION\_PROXIMATE\_ULTIMATE) ; Vague C.2 (instance de contrôle extérieure du régime performatif, RECHERCHE\_INTERVENTION ; co-activation R-CRISE-MIMETIQUE) ; Vague C.3 (sens G-MIMETIQUE→G-SOIN, R-CARE-SACRIFICIEL en F7) ; Vague C.5 (règle de priorité F6/F10).

## §D.8 Lacunes et limites de cette section

\[LACUNES ET LIMITES\] (1) Les théorèmes V1–V4 sont transcrits dans leurs conséquences procédurales ; le rapport Lean 4 / ProfReg reste le livrable de référence. (2) Les contrôles page-à-page sur sources primaires (Gosseries 2023, Schlosberg 2007, Girard, Hache édition papier) ne sont pas clos.

## §D.9 Verrous bibliographiques des grammaires NT-G5, NT-G11, NT-G12 et de l'annexe méthodologique

| **Référence à vérifier**                                  | **Grammaire**  | **Statut**   |
| --------------------------------------------------------- | -------------- | -------------------------------------------------------- |
| Zimmermann 2020 (S1) + Référentiel DPQT (S3) | NT-G11 | **LEVÉ** — S1 jointe (Pragmata 3, 2020, VÉRIFIÉ) ; S3 : référence canonique fixée (CRTD/Cnam, dir. Clot, PDF 2025) ; fusion structurelle → W-8 |
| Murray (risque/autonomie/expressivité)                    | NT-G11         | \[PLAUSIBLE, NON VÉRIFIÉ\] — réf. exacte à préciser |
| Rambaud 2015 (thèse Dauphine, tel-01253474) | NT-G12    | **LEVÉ** — jointe, VÉRIFIÉ       |
| Dumeaux 2025 (juste prix écologique)                      | NT-G12         | **LEVÉ** — réf. canonique : thèse PSL, NNT 2025UPSLD046, HAL tel-05450164 (version courte jointe) |
| Callon, Caliskan & MacKenzie → « Ecologization » 1 & 2, *Economy and Society*, 2025 | NT-G12 | **LEVÉ** — VÉRIFIÉ (biblio) ; usage : « économisation performée / valorimètres » ; principe général de performativité → Unal et al. 2025 (NT-G4) |
| CNoCP avis 2016-02 (image fidèle)                         | NT-G12         | **Document primaire localisé** — PDF officiel economie.gouv.fr ; contrôle direct exécutable |
| Richard, Bensadon & Rambaud, 11e éd. **2018** (Dunod)     | NT-G12         | VÉRIFIÉ            |
| Bahougne **& Camus** 2020 (droit comptabilité publique)   | NT-G12         | **LEVÉ** — VÉRIFIÉ sur source primaire jointe (PUF Thémis, 520 p. ; co-signature Bahougne & Camus) |
| Descola 2005 (Par-delà nature et culture)                 | NT-G5          | **Confirmé PLAUSIBLE (web)** — Gallimard 2005       |
| Latour 1999/2015 (Politiques de la nature / Face à Gaïa)  | NT-G5          | *Face à Gaïa* 2015 confirmé ; *Politiques de la nature* 1999 reste \[PLAUSIBLE, NON VÉRIFIÉ\] |
| Ganter & Wille 1999 (Formal Concept Analysis)             | Annexe méthodo | \[PLAUSIBLE, NON VÉRIFIÉ\] — édition à confirmer |

## §D.10 Méthode de vérification des références primaires

> Statuts à jour : §D.5, §D.9, §D.11 et le fichier d'état (`_ETAT_INSCRIPTION_v5.7.md`, inventaire du registre des sources). Restent ouverts : Murray S2 (pages), Girard 1978 Livre II, Boyer 2022 (chapitre), Ganter & Wille (édition), Hochschild/Dejours (pages).

Pour chaque grammaire, les sources sont classées en trois catégories : (A) sources à vérifier par une lecture approfondie, parce que les concepts qu'elles fournissent sont structurants pour l'architecture du MRC et qu'une lecture erronée menacerait la cohérence inter-couches ; (B) sources mal identifiées ou mal sourcées, dont il faut d'abord établir/compléter la référence exacte ; (C) sources dont il faut préciser la page ou le chapitre d'où le concept utilisé est tiré. Une même source peut relever de plusieurs catégories.
*Priorisation. Catégorie B = bloquante pour la diffusion externe (une référence non établie ne peut être citée). Catégorie A = bloquante pour la cohérence conceptuelle (à traiter avant toute extension de l'architecture mobilisant ces concepts). Catégorie C = bloquante pour la traçabilité fine (inscription page-à-page), non pour l'usage interne.*

---

## §D.11 Contrôle des sources × biblio — renvois de grammaire et flux hors grammaires

Source unique du traçage : `_ETAT_INSCRIPTION_v5.7.md` (synthèse du contrôle des sources ; inventaire du registre). Les documents de contrôle détaillés sont des pièces de travail hors set. Les statuts de §D.5 et §D.9 en tiennent compte ; les NT-G1 à NT-G12 portent les corrections dans leur corps.

**D.11.1 — Renvoi de grammaire.** Toute source bibliographique doit figurer dans une NT-Gx ou dans la présente Annexe ; la note d'architecture renvoie, pour chaque source, à la grammaire qui la mobilise. Mapping :

| Source(s) | Porteur |
|---|---|
| Clot et al. 2021 ; Référentiel DPQT ; Zimmermann 2020/2018 ; De Munck & Zimmermann 2015 ; Murray | **NT-G11** (Travail) |
| Bourdieu & Passeron 1970 (prop. 2.2, p. 37) ; Bourdieu & Wacquant 1992 ; Crenshaw 1991 ; Fraser 2009 ; Fraser & Honneth 2003 ; Meyer & Roser 2009 ; Nussbaum ; Schlosberg (justice) | **NT-G7** (Justice) |
| Schwager 1987 ; Cowdell 2013 ; Reineke 2014 ; Girard 1972/1978/1982/1999/2007 ; Dupuy 2002 ; Anspach 2002 | **NT-G8** (Mimétique) |
| Honneth 1995/2000 ; Dejours ; Boyer-Petersen ; Karabegovic et al. 2024 ; Pairot 2026 ; Sunstein 2019 | **NT-G9** (Affectif) |
| Schlosberg 2007 (p. 136) ; Morizot & Neyret 2026 ; Karr & Dudley 1981 ; Cairns 1977 ; Roche & Campagne 2017 ; De Leo & Levin 1997 ; Gosseries 2023 | **NT-G2** (Responsabilité) |
| Berque 2010 ; Stépanoff 2024 ; Marlin 2022 ; Descola 2005 ; Latour 1999/2015 | **NT-G5** (Mésologie) |
| Ostrom 1990 ; Schlager & Ostrom 1992 ; Dardot & Laval 2014 ; Rochfeld, Cornu & Martin 2021 | **NT-G6** (Communalité) |
| Ferey 2024 ; Medina 2013 (via Ferey) ; Fraser 2004 ; Mansbridge | **NT-G10** (Démocratie épistémique) ; Ferey 2024 aussi en **NT-ARCH §B.2ter** (phase RECHERCHE\_INTERVENTION) |
| Richard-Bensadon-Rambaud 2018 ; Rambaud 2015 ; Dumeaux 2025 ; Bahougne & Camus 2020 ; CNoCP 2016-02 ; Ecologization (Callon, Caliskan & MacKenzie 2025) ; contribution ANC/PPC 2026 | **NT-G12** (Valuation) |
| « The modes of performativity » (Unal, Polillo, Caliskan & MacKenzie 2025) ; Haraway 1988 ; Gibson-Graham 2006 | **NT-G4** (Performativité) |
| Sperber 1996 ; Henrich 2015 ; Boyer ; Driscoll 2011 ; Buskell 2017-2019 | **NT-G1** (Évolutivité) |
| Puig de la Bellacasa 2017 ; Tronto 1993 ; Fisher & Tronto 1990 ; Plumwood 2002 | **NT-G3** (Soin) |

**D.11.2 — Flux hors grammaires, versés à la présente Annexe (couche descriptive/méthode) :**

- **Flux W-1 / GT « Technologie et Pouvoir »** : Pistor, K., *The Code of Capital*, Princeton UP, 2019, 316 p. ; Pistor, K., *The Law of Capitalism and How to Transform It*, 2025, 172 p. (deux ouvrages joints — les ancrages W-1b « via Pistor » sont contrôlables sur exemplaire, paginations à extraire au fil des usages). Cabanes, V., *Un nouveau droit pour la Terre*, Seuil, 2016 ; Higgins, P., *Eradicating Ecocide*, Shepheard-Walwyn, 2015 (références GT fournies par le porteur — rattachées au GT/écocide, **non** au registre de `INTEGRITE_ECOSYSTEMIQUE`).
- **Flux W-12 / BEE** : Feger, C. (dir.), Rambaud, A. (dir.), Morlat, C. & Le Corre, A. (2025), *Agir pour préserver les « bons états écologiques »…*, Note de synthèse, Chaire Comptabilité Écologique — jointe (36 p.). Références établies : Levrel & Missemer 2023 (*REF* 151(3), pp. 327-334) ; IPBES-BBA Brooks et al. 2026 (ch. 4). « Surun 2023 (CENP) » désigne Kervinio, Surun, Comte & Levrel 2023, *One Ecosystem* 8: e98100 (une seule source). **Réserve : note V0, non évaluée par les pairs — conceptions A1-A12 à contrôler avant durcissement.**
- **Flux W-2 / canaux méso** : Lamarche et al. 2021 (*Économie appliquée* n° 1, pp. 13-49 — retenir 2021, le « à paraître 2020 » = préprint HAL) ; Lamarche & Bastien 2025, *Mésoéconomie* (texte intégral joint — [PLAUSIBLE : date/éditeur à confirmer, extrait sans page de titre] ; réserve « seuls ch. 3 §1.2 et ch. 5 lus » levable) ; Ballon & Celle 2023 (*Revue Interventions économiques* n° 69 — VÉRIFIÉ, 22 p. lues). **Canal Gouvernance : l'argumentaire d'absorption lève l'`[ENGAGEMENT SANS SYMÉTRIE]`** — un canal méso est une dimension transverse, non un registre (précédent : futurité, absorbée sans grammaire dédiée par NT-G1/G2/G7) ; le canal gouvernance se décompose sans reste sur NT-G6 (propriété/gestion), NT-G7/W-14 (rapports de pouvoir) et NT-G10 (décision collective/représentation) → **pas de 13ᵉ grammaire** ; usage descriptif conservé ici (mécanisme de différenciation méso).
- **Flux PPC / test F8** : Bahougne & Camus 2020 (→ NT-G12) ; PPC, « Contribution à la consultation de l'ANC », 30 juin 2026, Axe 3.D — MPP (2116), GCP (2117), SOP couverts. Réserve : document-source PPC (proposition, non norme) ; `Note MPP ANC.pdf` à redéposer.
- **Renforts joints à verser au registre** : Zimmermann & Engelbrecht 2024 (*Transfer*) ; Laruffa & Zimmermann 2026 (*ELRR*) ; Caliskan & Wade 2022 (DARN 1/2, *She Ji* — **2022, pas 2025** ; usage propre : méthode empirique rights-of-nature, PAS la ligne performativité NT-G12) ; Rambaud 2015 ; Deranty & Genel (in *Reconnaissance ou mésentente ?*) ; Carruthers & Espeland 1998.

**D.11.3 — Restes déclarés** : les verdicts PLAUSIBLE (web) vérifient la *référence*, pas le contenu cité (verbatims des ouvrages non joints à contrôler sur exemplaire — niveau (2) de la méthode W-6) ; réserve d'édition Laffont/Grasset (Girard 1972) ; P1-2 et stabilité du seuil P2-11 = vérifications internes, hors objet W-6. **Les contrôles de pagination ne font pas partie du programme — décision du porteur : le verbatim vérifié fait foi.**

---

## §D.12 Régime mono-porteur assumé

**Périmètre.** Des matériaux de lecture et périmètres externes sont classés hors set ; le versement Fournier (`REDEFINITION-BUTS`) est conservé pour ses apports propres à NT-G7 et NT-G10 (versement tracé au fichier d'état).

**Régime de porteur.** La communauté de gestion du MRC comme commun **n'est pas encore instituée**. Le MRC est tenu en **régime mono-porteur assumé** (P. Musseau-Milesi · La Coop des Communs) : le porteur actuel tient les rôles de conception et de validation documentaire, mais les actes réservés à l'échelon gouverné de l'échelle de communalité (vote de clôture §A.4ter, promotion en Couche 0, re-délibération des signaux capture/neutralisation) **restent suspendus à l'institution de cette communauté** — `[INCOHÉRENCE INTER-COUCHES — niveau 2 : porteur cible non encore institué]`, déclarée, non lissée. La validation documentaire n'est pas un vote de la communauté : elle est **révisable par celle-ci dès son institution**.

# §E — Lacunes et limites de l'annexe consolidée

\[LACUNES ET LIMITES\] (1) Les lacunes propres à chaque composant (§A.3, §B.8, fin de §C, §D.8) sont conservées telles quelles et restent valides. (2) Le découpage retenu est à quatre couches 0–3, aligné ProfReg. (3) Le périmètre exact de la réserve d'extension (§A.3 : Exist, ProfReg comme instrument, DIDs/VCs) reste à arbitrer par le porteur. (4) Les énoncés du programme de preuve et leur transcription Lean 4 sont tenus dans `MRC_v5.7_ProfReg_Consolide.md` §7, livrable ProfReg de référence ; ils ne sont pas reproduits ici.

— MRC v5.7 — Annexe méthodologique étendue — régime mono-porteur assumé, cf. §D.12 ; décisions tracées dans `_ETAT_INSCRIPTION_v5.7.md` —
