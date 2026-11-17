**NT-G2 — Responsabilité (G-RESPONSABILITE)**

*Note de travail par grammaire — Grammaire transversale G-RESPONSABILITE (Fiche F4, Couches 0–3)*

*Finalité immanente, habitabilité, irréversibilité et justice intergénérationnelle*

Pierre Musseau-Milesi — La Coop des Communs — 30 mai 2026 — Régime : vérifiabilité-cohérence

> **Set MRC v5.7.** Architecture à **quatre couches**, alignée sur la nomenclature ProfReg : Couche 0 = primitives ; Couche 1 = régimes et invariants ; Couche 2 = modes d'application (fiches F1–F10) ; Couche 3 = grammaires transversales. Architecture : → `MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md` (les renvois « NT-ARCH §n » pointent vers sa Partie A). Méthodes, programme de preuve, verrous bibliographiques et chantiers : → `MRC_v5.7_Annexe_Methodologique.md`. Suivi des inscriptions et décisions : → `MRC_v5.7/_ETAT_INSCRIPTION_v5.7.md` (source unique).

**Version :** 5.7

**Statut :** Document de travail — régime vérifiabilité-cohérence

**Auteur :** Pierre Musseau-Milesi — La Coop des Communs

**Historique :** tenu au fichier d'état (`MRC_v5.7/_ETAT_INSCRIPTION_v5.7.md`) et au suivi de l'Annexe méthodologique (§D).

**Portée :** Grammaire G-RESPONSABILITE (F4 — Mode existentiel, F2 — Dégradation milieu, couplages F4↔F6, F4↔F7)

**Statut des vérifications formelles (ProfReg, Lean 4) :** décompte de référence et état audité : Consolidé §1 ; appuis propres à cette grammaire : encadré « Appuis formels (ProfReg) », fin du §7. Les signaux \[PLAUSIBLE, NON VÉRIFIÉ\] et \[INCOHÉRENCE INTER-COUCHES\] portant sur la commutativité F4↔F6 (A2 ; V1, sous cohérence déclarée), sur B1 vs R1 (V2), sur le carré B1↔B2 (PR-51 : commutation conclue sur les chemins admissibles, la règle des pas étant déclarée — CONV-2 étendue ; `V3_commutatif` n'en est qu'une lecture, forme 1) et sur la cascade R-INTERDIT-ABSOLU (V4) sont **levés** (voir §3.2, §7 et §9). Restent hors de portée de ProfReg : la préservation du régime ACTORIEL par la transition V4c (2-cellule complète de l'Annexe G, non encodable dans Mathlib actuel) et le carré triangulaire NT-G7 ↔ NT-G2 ↔ NT-ARCH (procédural, CONV-2).

**1. Objet et positionnement**

G-RESPONSABILITE est la grammaire transversale qui régit la manière dont le MRC inscrit et traite les obligations envers les entités vivantes — humaines et non-humaines — **dont le seuil d'entrée dans la communauté morale est déclaré**, lorsque des irréversibilités sont en jeu.

> Deux conditions encadrent ce périmètre. **(1)** « **aucune obligation envers une entité non-humaine ne peut être inscrite sans déclarer son seuil d'entrée dans la communauté morale** (sentience ou finalité immanente) » — la règle formalisée est `obligationrelationnelle_declaree = VRAI` seulement si `seuilentreecommunautemorale ≠ NONDECLARE`. **(2)** Le registre ne déclenche seul que la DELIBERATION : en régime SYSTEMIQUE, le niveau CRITIQUE de R-INTERDIT-ABSOLU exige un porteur DID identifié — c'est le verrou anti-urgence (voir la note de déclenchement, §3). Elle est fondée principalement sur Jonas (1979/1990), Morizot & Neyret (2026), Gosseries (*What is Intergenerational Justice?*, Polity, 2023 \[VÉRIFIÉ sur recensions IGJR 2024 et JPE 2024\]) et Nussbaum (*Frontiers of Justice*, 2006, ch. 6).

**Fondement opératoire — l'heuristique de la peur (Jonas) :** Jonas (*Le Principe Responsabilité*, 1979/trad. Cerf, 1990 \[VÉRIFIÉ\]) pose que, face à une décision irréversible, le scénario catastrophique a une priorité épistémique sur le scénario optimiste : la vulnérabilité de ce qui peut être détruit prime sur l'opportunité espérée. R-INTERDIT-ABSOLU est l'**opérateur formel** de cette heuristique dans le MRC — il n'est pas une interdiction rhétorique mais un signal calculable, déclenché via la catégorie indexée Exist (Annexe G) — **le registre ne déclenchant seul que la DELIBERATION, le niveau CRITIQUE étant conditionné à l'identification d'un porteur**. Cette asymétrie est délibérée et assumée : le risque de catastrophe irréversible n'a pas de contrepartie symétrique en opportunité manquée — c'est un \[ENGAGEMENT SANS SYMÉTRIE\] revendiqué dans la logique jonasienne, non un défaut de cohérence (voir §6bis).

G-RESPONSABILITE est distincte de G-JUSTICE (F6 — capabilités) et de G-MIMETIQUE (F7 — dynamiques mimétiques), avec lesquelles elle est couplée (voir section 5 et 7).

**Couches mobilisées :**

 - Couche 0 : primitive Interaction (porteur, horizon, obligation)

 - Couche 1 : règle R1 (DÉBIT/CRÉDIT), R-INTERDIT-ABSOLU

 - Couche 2 : C-SUJET-COLLECTIF, C-FINALITE-IMMANENTE, C-INDEXATION-HORIZON, C-MEMOIRE-PERTES, C-ENQUETE-V5

 - Couche 3 : règles dérivées R-HABITABILITE-CAPABILITE, R-PUISSANCEAFFIRMATIVE, R-PERMIS-PERFORMATIF (cf. NT-G6)

**2. Champs et structures de données**

**2.1 — C-SUJET-COLLECTIF (Couche 2)**

**Structure :** le sujet responsable est réparti en trois champs distincts (Amendement A1 — source : Jonas 1979, Morizot & Neyret 2026), complétés par le champ seuilentreecommunautemorale (A1 révisé — Nussbaum 2006, Jonas 1979). La source de sujetresponsable\_horizon est Gosseries 2023.

> obligationrelationnelle\_declaree Booléen VRAI si l'obligation envers l'entité
>
> non-humaine est inscrite, indépendamment
>
> de la désignation d'un porteur.
>
> Peut être VRAI alors que
>
> sujetresponsable\_declare est vide.
>
> Source : Jonas 1979, Morizot & Neyret 2026
>
> sujetresponsable\_declare DID acteur Porteur humain ou institutionnel identifié.
>
> (optionnel Peut être vide au moment de l'inscription —
>
> à l'ins- l'absence de porteur ne bloque pas
>
> cription) l'inscription de l'obligation.
>
> sujetresponsable\_horizon Texte Mécanisme institutionnel portant la
>
> responsabilité (traité, loi, mandat de
>
> tutelle, consortium DID).
>
> Source : Gosseries 2023, What is
>
> Intergenerational Justice? (institutions
>
> for future generations) \[VÉRIFIÉ\]
>
> seuilentreecommunautemorale Énumération SENTIENCE — Nussbaum 2006 : capacité
>
> à souffrir et à s'épanouir selon une forme
>
> de vie caractéristique.
>
> FINALITEIMMANENTE — Jonas 1979 : résistance
>
> à la destruction.
>
> NONDECLARE — par défaut ; déclenche
>
> DELIBERATION avant inscription.
>
> Source : Nussbaum 2006 (ch. 6), Jonas 1979

**Règle associée :** Le signal OBLIGATIONSANSRECIPROCITE est déclenché uniquement si sujetresponsable\_declare est absent ET obligationrelationnelle\_declaree est VRAI sur **deux cycles consécutifs**. L'absence de porteur ne bloque pas l'inscription — elle déclenche une phase DELIBERATION sur la gouvernance distributive.

**Règle associée (seuil d'entrée, A1 révisé) :** obligationrelationnelle\_declaree = VRAI ne peut être inscrit que si seuilentreecommunautemorale ≠ NONDECLARE. Sinon : signal \[ENGAGEMENT SANS SYMÉTRIE — seuil d'entrée absent\], déclenchant une phase DELIBERATION avant inscription. Sans ce seuil, toute entité (plante, sol, bactérie, molécule) pourrait déclencher une obligation relationnelle sans critère de réfutation — c'est l'\[ENGAGEMENT SANS SYMÉTRIE\] que cette règle résout. **Condition de réfutation :** si seuilentreecommunautemorale = SENTIENCE pour une entité structurellement non-sentiente (végétal, sol), la règle doit être révisée via REVISIONCONCEPTUELLE (Hache 2011, ch. 2 “ Comment répondre ? ”, p. 55). Nussbaum 2006 (ch. 6) : la sentience est le seuil d'entrée dans la communauté morale, mais la valeur ne s'y réduit pas — la capacité d'épanouissement selon une forme de vie caractéristique compte aussi.

**Avertissement de source (amendement P4, Hache 2011) :** le champ seuilentreecommunautemorale suit Nussbaum (2006) pour SENTIENCE et Jonas (1979) pour FINALITEIMMANENTE. Or Hache (2011, ch. 1 “ Changer de question ”, pp. 18-32) **récuse** la question du seuil d'entrée comme mal posée : “ Il ne s'agit plus de demander à un tiers s'il est apte à *être* moral, mais plutôt de se demander *comment être apte à répondre* ” (p. 32). Bien traiter un être ne passe pas par l'évaluation préalable de son aptitude morale, mais par la recherche des ressources pour lui répondre (p. 31). Cette tension Hache / Nussbaum-Jonas est un **\[INCOHÉRENCE INTER-COUCHES POTENTIELLE — couche 0\]** : le registre MRC *pose* un seuil que Hache *refuse*. Résolution adoptée, non lissée : seuilentreecommunautemorale est une primitive de couche 0 de type *procédural* (déclenche une délibération via NONDECLARE → DELIBERATION), non une coupure ontologique d'aptitude — ce qui est cohérent avec l'esprit de Hache. La tension est documentée, non supprimée.

> **Le porteur est optionnel à l'inscription ; son attribution exige des déclarations.** C-SUJET-COLLECTIF porte, en **NT-ARCH §4.2bis**, trois champs qui les fixent : `porteur_represente_des_membres`, `membres_representes` et `dimension_pouvoir` (liste **non exclusive** sur AVEC / SUR / DE, d'après Cousin & Audebrand 2026 et Huxham & Beech 2008), avec le signal `PORTEUR_COLLECTIF_SANS_DIMENSION_DECLAREE`. **Écrit comme condition de bonne formation de l'écriture d'attribution** (patron §8quater) : la machine d'états de Couche 1 n'est pas modifiée, et `NON_DECLARE` ne bloque pas l'inscription de l'obligation — il bloque son attribution. **Homologue explicite de la règle du seuil d'entrée ci-dessus** : là, déclarer qui entre dans la communauté morale avant d'inscrire une obligation envers elle ; ici, déclarer sur qui l'obligation retombe avant de l'attribuer. Pas de champ `type_porteur` : il serait réductible à `niveau_responsabilite`.

**\[CHANGEMENT DE BASE TRACÉ\]** : l'obligation relationnelle est première, le porteur est secondaire et optionnel à l'inscription — un champ unique de porteur, typé DID acteur collectif, rendrait l'inscription impossible sans porteur identifié.

> ### `[CONDITION DE RÉFUTATION DÉCLARÉE]`
>
> **Engagement propre de cette grammaire.** L'irréversibilité et la finalité immanente fondent une obligation dissymétrique
>
> **Cette grammaire tombe si** l'on documente une atteinte irréversible à une entité à finalité propre qui n'engendre, pour aucun acteur identifiable, d'obligation que le droit ou la pratique reconnaissent.
>
> Cette condition donne une **prise** ; elle n'est **pas une fiche d'axiome**. Elle ne nomme aucun objecteur, ne cite aucune position adverse, n'instruit aucune réponse — **une condition de réfutation sans gabarit contradictoire est un tiers de fiche**. `[DETTE DE MÉTHODE DÉCLARÉE.]` Voir `Fiches_Axiomes_A11_A12_A13_2026-09-11.md` §Z. **Elle n'a jamais été testée.**

**2.2 — C-FINALITE-IMMANENTE (Couche 2)**

**Champ puissanceaffirmative :** Amendement A3 — source : Morizot & Neyret 2026.

> appelimmanent Score 0-5 Finalité immanente de l'entité vivante
>
> (résistance à la destruction).
>
> Source : Jonas 1979
>
> puissanceaffirmative Score 0-5 Capacité de l'entité non-humaine à
>
> co-produire activement les conditions
>
> d'habitabilité (pollinisation, régulation
>
> climatique, fertilisation des sols, etc.).
>
> Distinct de appelimmanent : capte la
>
> dimension PRODUCTIVE, non la seule résistance.
>
> Source : Morizot & Neyret 2026
>
> seuilpuissanceaffirmative Nombre Seuil en dessous duquel la perte de
>
> puissance affirmative est irréversible.
>
> À co-construire avec experts écologues.
>
> Doit avoir une date de révision obligatoire
>
> et un champ source\_valuemetre (cf. section 4).
>
> Source : logique des valorimètres Callon,
>
> Caliskan & MacKenzie, *Ecologization* Part 1 & 2,
>
> *Economy and Society*, 2025, DOI 10.1080/03085147.2025.2488121
>
> et 10.1080/03085147.2025.2498825 \[VÉRIFIÉ (biblio)\]
>
> irreversibilitejonasienne Booléen VRAI si le calcul Exist déclenche un
>
> franchissement de l'horizon h.
>
> Source : Jonas 1979, Annexe G.5 MRC
>
> effondrementexistentielcalcul Booléen VRAI si la catégorie de base Vh s'effondre
>
> à l'horizon h (calcul formel ProfReg).

**Note sur la distinction appelimmanent / puissanceaffirmative :**

appelimmanent capte la finalité défensive jonasienne — l'entité résiste à sa destruction. puissanceaffirmative capte la contribution active à l'habitabilité — l'entité produit les conditions de la vie. La disparition des pollinisateurs illustre ce cas : aucun pollinisateur individuel ne déclenche un appelimmanent significatif, mais leur disparition collective franchit seuilpuissanceaffirmative et déclenche une dégradation irréversible de l'habitabilité productive. \[VÉRIFIÉ — Morizot & Neyret 2026, p. 32, § « Les pollinisateurs et la possibilité du goût »\]

**2.3 — C-INDEXATION-HORIZON (Couche 2)**

**Amendement A4 :** deux des champs ci-dessous en relèvent.

**Source :** principe\_intergenerationnel suit la taxinomie **à quatre principes** de Gosseries, *What is Intergenerational Justice?*, Polity, 2023 \[VÉRIFIÉ sur recensions IGJR 2024 et JPE 2024\].

> horizontemporelresponsabilite Énumération INSTITUTIONNEL / INTERGENERATIONNEL /
>
> PROFOND / PLANETAIRE — un horizon géologique équivaut à l'horizon planétaire et ne peut le dépasser
>
> principe\_intergenerationnel Énumération NON-DECLINE — interdiction de transmettre
>
> moins qu'hérité (réciprocité descendante)
>
> BETTER-FUTURE — obligation de transmettre
>
> plus qu'hérité (agrégation)
>
> SUFFICIENCY — garantir le « enough » à
>
> chaque génération
>
> NARROW-PATH — leximin égalitariste, priorité
>
> au moins bien loti (position propre de Gosseries)
>
> NON\_DECLARE — valeur par défaut, déclenche
>
> DELIBERATION
>
> Source : Gosseries 2023, What is
>
> Intergenerational Justice?, Polity \[VÉRIFIÉ\]
>
> Si NON\_DECLARE est dominant sur deux
>
> cycles → signal \[ENGAGEMENT SANS SYMÉTRIE\]
>
> convention\_attribution\_seuil DID DID de la délibération ou du texte
>
> institutionnel ayant produit le seuil
>
> utilisé dans C-INDEXATION-HORIZON.
>
> Source : logique des valorimètres
>
> co-construits (Callon et al. 2025)
>
> Tout seuil sans ce DID est une convention
>
> non gouvernée.

**Note :** Gosseries 2023 se reconnaît le plus proche du NARROW-PATH dans une version moins stricte.

**Justification Callon :** Callon, Caliskan & MacKenzie (2025, Part 2, p. 9) : « there is no general rule. Solutions are always local, uniquely crafted. » Tout seuil intergénérationnel est une convention localement produite. Le champ convention\_attribution\_seuil trace cette convention comme acteur inscrit en Couche 0.

**2.4 — C-MEMOIRE-PERTES (Couche 2)**

**Champs :**

> cyclesnontraites Entier Nombre de cycles où l'obligation est restée sans porteur

**Amendement B4** (source : Callon et al. 2025, Morizot & Neyret 2026) : trois champs.

> seuil\_qualification\_externe Texte Référence normative externe (écocide,
>
> Principe habitabilité Morizot & Neyret,
>
> jurisprudence climatique) utilisée pour
>
> qualifier la dette accumulée.
>
> Source : Morizot & Neyret 2026
>
> convention\_seuil\_source DID DID de la délibération ayant produit
>
> le seuil. Tout seuil sans ce DID est
>
> un instrument performatif non gouverné.
>
> Source : Callon et al. 2025 (risque
>
> de greenwashing, Part 2, pp. 10-11)
>
> source\_valuemetre DID Qui a conçu le valorimètre ? Avec quels
>
> acteurs ? Qui en est exclu ?
>
> OBLIGATOIRE — non optionnel.
>
> Source : performativité de l'instrument
>
> (C-INSCRIPTION, propriété 1.7)

**Précaution :** Un seuil calculé automatiquement sans convention\_seuil\_source déclaré serait un instrument performatif non gouverné — précisément ce que Callon et al. (2025, Part 2, pp. 10-11) qualifient de risque de greenwashing. Le champ source\_valuemetre est donc **obligatoire**, non optionnel.

**3. Règles de la grammaire G-RESPONSABILITE**

**3.1 — R-PUISSANCEAFFIRMATIVE (Couche 3, G-RESPONSABILITE)**

> R-PUISSANCEAFFIRMATIVE (Couche 3, G-RESPONSABILITE)
>
> Source : Amendement A3, Morizot & Neyret 2026
>
> Condition : puissanceaffirmative \< seuilpuissanceaffirmative
>
> ET irreversibilitejonasienne = VRAI (calcul Exist)
>
> Action : → Inscription C-MEMOIRE-PERTES avec horodatage
>
> → Déclenchement R-INTERDIT-ABSOLU niveau CRITIQUE si
>
> effondrementexistentielcalcul = VRAI
>
> → Alerte G-JUSTICE : capabiliteplancher menacée
>
> (via R-HABITABILITE-CAPABILITE — cf. 3.2)

**Note de déclenchement :** En régime SYSTEMIQUE (cf. B1), R-INTERDIT-ABSOLU déclenche niveau DELIBERATION (non CRITIQUE) en l'absence de porteur DID identifié. Le niveau CRITIQUE ne s'applique qu'une fois des porteurs identifiés via INVENTAIRE-ASSETS-ACTIFS + DELIBERATION. Cette cascade est **prouvée en régime formel** (V4 : V4\_cascade\_coherente) et encodée comme machine d'états de **Couche 1**, non comme convention de Couche 2 : NONATTRIBUEE → CRITIQUE est une contradiction formelle interdite (cascade\_deliberation\_before\_critique) ; NONATTRIBUEE → DELIBERATION est l'unique transition autorisée (nonattribuee\_force\_deliberation) ; ATTRIBUEE → CRITIQUE est la seule voie de libération du niveau CRITIQUE après désignation d'un porteur (critique\_released\_by\_porteur).

**Ancrage de `puissanceaffirmative` — **chaîne d'attribution à trois maillons**.**

> | Maillon | Ce qu'il porte |
> | --- | --- |
> | **Canguilhem**, *Le Normal et le pathologique* (1943/1966) ; *La Connaissance de la vie* (1952/1965) | **le concept — sous un autre nom** : la **normativité vitale**. « la santé […] est une certaine latitude, un certain jeu des normes de la vie » ; « le luxe de pouvoir tomber malade et de s'en relever » ; « le milieu du vivant est aussi l'œuvre du vivant » |
> | **Morizot & Neyret**, *Tracts* n° 70 (2026) | **l'expression** — et **ils la modalisent eux-mêmes** : « C'est ce qu'on **pourrait appeler** la puissance affirmative du vivant » |
> | **MRC** | **l'identifiant de champ** `puissanceaffirmative` — **sans le modalisateur, sans guillemets** |
>
> **Canguilhem n'est donc pas la source primaire de ce champ : il est la source primaire du concept que l'expression interprète.** L'écrire autrement est le `[CHANGEMENT DE BASE NON TRACÉ]` que cette section interdit explicitement dix-huit lignes plus bas.
>
> `[MOTIF DE CRIBLE — perte du modalisateur en chaîne de citation, NT-ARCH §8octies.]` À chaque maillon une précaution tombe. **Au troisième, une élaboration que ses auteurs signalent comme telle est devenue une primitive du modèle.**
>
> Trois glissements du Tract, à ne pas reprendre tels quels : *« le vivant l'**institue** »* — Canguilhem écrit une **œuvre**, c'est-à-dire une sélection, une polarisation, une organisation, non une fabrication ; *« il ne vit plus vraiment »* — le pathologique **demeure une allure de la vie**, réglée par des normes rétrécies ou dépréciées ; *« perte de la puissance d'invention »* — réduction de la **capacité à tolérer les variations et à instaurer un nouvel ordre**. **Le premier et le deuxième ont des conséquences dans le set : voir §2.1quater et NT-G5.**

La primitive ne vient pas des auteurs de l'amendement A3 : ils la tirent de **Georges Canguilhem, *Le Normal et le Pathologique*** — « ce qu'on pourrait appeler la **puissance affirmative du vivant** » (Morizot & Neyret 2026). Le conditionnel de leur phrase est exact et doit être conservé : **« puissance affirmative » n'est pas de Canguilhem.** Contrôle sur l'ouvrage, en biblio — **zéro occurrence** de l'expression. C'est une **dénomination de Morizot & Neyret pour un concept de Canguilhem**, et le concept, chez lui, s'appelle **normativité** (21 occurrences de « normativité », 35 de « normatif »).

*Ce que dit la source primaire, et qui fonde la règle mieux que sa reformulation :*

> « **Être en bonne santé c'est pouvoir tomber malade et s'en relever, c'est un luxe biologique.** Inversement, le propre de la maladie c'est d'être **une réduction de la marge de tolérance des infidélités du milieu**. » (Canguilhem, *Le Normal et le Pathologique*, Partie I)

Et, sur la réduction du milieu lui-même, à propos des travaux de Goldstein :

> « l'**instauration de nouvelles normes de vie par une réduction du niveau de leur activité**, en rapport avec un milieu nouveau mais **rétréci**. Le rétrécissement du milieu \[…\] répond à leur impuissance à répondre aux exigences du milieu normal, c'est-à-dire antérieur. » (*ibid.*)

*Ce que la source primaire établit pour la règle.* Trois choses, et la troisième est la plus importante.

**(1) Le seuil est lisible.** `seuilpuissanceaffirmative` ne mesure pas une quantité de vitalité : il marque le point où **la marge de tolérance aux infidélités du milieu se réduit**. C'est un seuil de *capacité de réponse*, non de niveau d'activité.

**(2) `effondrementexistentielcalcul` est bien fondé, et ce n'est pas la mort.** Ce que Canguilhem décrit n'est pas la disparition mais l'**instauration de normes de vie rétrécies** : le vivant continue, en ayant cessé de pouvoir répondre autrement. C'est exactement ce que la règle veut déclencher — un interdit qui mord **avant** la disparition. Morizot & Neyret le transcrivent en « effondrement de la puissance affirmative de la vie : elle cesse d'instituer son milieu et se contente de le subir » (2026).

**(3) L'asymétrie jonasienne trouve un second appui, indépendant du premier.** Chez Canguilhem, la santé n'est pas la symétrie du normal et du pathologique : c'est **le luxe de pouvoir tomber malade et s'en relever**, et la maladie est une *réduction* — l'un n'est pas l'inverse de l'autre. `[ENGAGEMENT SANS SYMÉTRIE]` revendiqué par la grammaire (§6bis) reçoit donc un appui venant de la philosophie de la biologie, distinct de l'appui jonasien et de l'appui Lemke. **Aucun des trois n'emprunte aux deux autres** — `[CORPUS NON AUTORÉFÉRENTIEL]`.

*Références.* Georges Canguilhem, *Le Normal et le Pathologique* \[en biblio, VÉRIFIÉ — pagination non contrôlée\]. Morizot, B. et Neyret, L. (2026), *Tracts n° 70 — Liberté, dignité, habitabilité*, Gallimard, p. 3-65 \[en biblio, VÉRIFIÉ\]. **Ne pas attribuer à Canguilhem l'expression « puissance affirmative »** : elle est de Morizot & Neyret, et le confondre serait un `[CHANGEMENT DE BASE NON TRACÉ]`.

### §2.1quinquies `seuilpuissanceaffirmative` — l'obligation comme condition de bonne formation

**Point de départ**, dans la table C-FINALITE-IMMANENTE : *« À co-construire avec experts écologues. […] **Doit** avoir une date de révision obligatoire et un champ `source_valuemetre` »* — et dans la table des actions, ACT-G2-004, colonne Porteur : **« À désigner »**.

> `[ENGAGEMENT SANS PORTEUR]` Ni porteur — la colonne le dit littéralement —, ni horizon de révision chiffré, ni critère disant à quoi se reconnaît une révision faite. **Et ce seuil commande la règle la plus lourde du set** : `R-PUISSANCEAFFIRMATIVE`, dont l'action mène à `R-INTERDIT-ABSOLU` niveau CRITIQUE.

**Condition de bonne formation.**

> *Une inscription mobilisant `seuilpuissanceaffirmative` n'est bien formée que si elle porte : **(i)** `source_valuemetre` (DID), **(ii)** une `date_revision` renseignée, **(iii)** la convention de mesure et le régime d'usage sous lesquels le seuil est mobilisé.*

| Porteur | Horizon | Critère de vérification |
| --- | --- | --- |
| **le déclarant de l'écriture** | **l'inscription** | **la présence des trois champs sur la pièce** |

> **La condition porte sur l'écriture, non sur un objet du monde.** Un seuil à co-construire un jour avec des experts attend un porteur qui n'existe pas ; une condition sur l'écriture a toujours un porteur : celui qui inscrit. *Elle ne dispense pas de co-construire le seuil ; elle empêche de le mobiliser tant qu'il ne l'est pas.*
>
> **Elle rend vérifiable l'exigence posée par la tension déclarée ci-dessous** : « `seuilpuissanceaffirmative` ne peut être mobilisé qu'avec sa source, sa convention de mesure, son régime d'usage et son porteur de déclaration — et **jamais comme seuil universel** ». `[ACT-G2-004 reste ouverte — la co-construction du seuil est une autre obligation, elle, à porteur réel.]`

### §2.1quater Le seuillage lui-même

**La question posée.** Canguilhem tient que *« la maladie, l'état pathologique, ne sont pas perte d'une norme »* mais **une autre allure de la vie**, réglée par des normes rétrécies ou dépréciées. Or `R-PUISSANCEAFFIRMATIVE` déclenche `R-INTERDIT-ABSOLU` **niveau CRITIQUE**. Un seuil qui fait basculer d'un état à un autre ne réintroduit-il pas le partage binaire normal / pathologique que *Le Normal et le pathologique* démonte ?

**La réponse est non, et le texte de la règle le montre.**

> **Le seuil ne déclenche rien à lui seul.** La condition de la règle est **conjonctive** : `puissanceaffirmative < seuilpuissanceaffirmative` **ET** `irreversibilitejonasienne = VRAI`. Et l'action est **étagée** : le franchissement du seuil inscrit une **perte en mémoire** (C-MEMOIRE-PERTES, horodatée) ; **CRITIQUE n'est atteint que sous une troisième condition**, `effondrementexistentielcalcul = VRAI`.
>
> **Trois conditions, trois niveaux — et c'est exactement la structure canguilhemienne.** Le seuil marque un **rétrécissement de la latitude normative**, que le registre inscrit sans rien conclure. L'irréversibilité marque que le rétrécissement **ne se relèvera pas** — c'est la perte du « luxe de pouvoir tomber malade et de s'en relever », qui est chez Canguilhem le critère, et non le niveau d'activité. L'effondrement seul déclenche CRITIQUE.
>
> **Le seuil du MRC ne sépare donc pas le sain du pathologique : il ouvre une mémoire.** Ce qui bascule est ailleurs, et ce qui bascule est la **non-réversibilité**.

La lecture ci-dessus tient **à la condition que CRITIQUE se lise « rétrécissement attesté et irréversible de la latitude normative », non « perte de vitalité »**. Les deux lectures produisent les mêmes déclenchements et **ne portent pas la même thèse** : la seconde dirait qu'une entité sous le seuil ne vit plus — ce que Canguilhem interdit et ce que le Tract frôle en écrivant *« il ne vit plus vraiment. Il dure. »* **La lecture retenue est la première.** `[LECTURE DÉCLARÉE.]`

`[CONDITION DE RÉFUTATION DE CETTE LECTURE]` Elle tombe si l'on montre qu'une des trois conditions est redondante — en particulier si `effondrementexistentielcalcul` se déduit du franchissement du seuil et de l'irréversibilité. **L'étagement serait alors décoratif, et le seuil redeviendrait binaire.** `[À CONTRÔLER — la définition d'`effondrementexistentielcalcul` n'a pas été examinée sous cet angle.]`

`[CE QUI RESTE OUVERT]` Le Tract écrit *« il ne vit plus vraiment »*, Canguilhem écrit que le pathologique demeure une allure de la vie. **Le set s'aligne ici sur Canguilhem contre son relais** — la source primaire corrige l'intermédiaire par lequel le MRC y accède. `[MOTIF — voir NT-ARCH §8octies, perte du modalisateur.]`

---

**\[TENSION DÉCLARÉE\] Le seuil et le refus de quantification de la source.** La règle ci-dessus déclenche CRITIQUE sur `puissanceaffirmative < seuilpuissanceaffirmative` — un **seuil quantifié**. Or la source écrit : « **Quantifier l'habitabilité ?** La nature d'une valeur protégée **exclut qu'on quantifie dans sa définition** là où commence l'atteinte à l'habitabilité de manière quantifiée \[…\] faire justice, c'est toujours traiter chaque cas comme un cas unique \[…\] l'habitabilité doit être un **instrument d'interprétation** au plus haut niveau » (Morizot & Neyret 2026).

Ce n'est **pas une contradiction, sous une condition qui doit être rappelée ici**. Les auteurs refusent la quantification *dans la définition de la valeur cardinale*, au niveau du droit ; ils n'interdisent pas qu'un dispositif situé déclare un seuil pour un cas — « traiter chaque cas comme un cas unique » le suppose même. **La garde correspondante existe déjà dans le set, mais elle est ailleurs** : tension T4 (§9) — « `convention_attribution_seuil` interdit tout seuil posé comme universel » — et règle **R0-bis** (Annexe méthodologique §A.14.3), qui exige le quadruplet « statut du seuil » de toute primitive `seuil-valuatif`. Or `seuilpuissanceaffirmative` **est typé `seuil-valuatif`** au §A.14.7. **PR-10** (`seuil_valuatif_must_declare_status`) en est la contrepartie formelle.

*Ce qui est donc exigé ici, et non ailleurs :* `seuilpuissanceaffirmative` ne peut être mobilisé qu'avec sa source, sa convention de mesure, son régime d'usage et son porteur de déclaration — et **jamais comme seuil universel**. À défaut, le déclenchement de CRITIQUE serait un `[DÉCOUPLAGE DE RÉGIMES]` entre la règle et la source qu'elle invoque. *Condition de réfutation de cette lecture :* elle tombe si l'on soutient que le refus de quantification des auteurs vaut à **tous** les niveaux, y compris situé — auquel cas la tension redevient une contradiction et la règle est à réécrire. Cette lecture restrictive est défendable et n'est pas tranchée par le texte. `[INFÉRENCE — contestable]`

**Appui externe — R-INTERDIT-ABSOLU comme contre-conduite à la résilience.** Lemke documente comment la gouvernementalité de la résilience neutralise l'heuristique de la peur : la résilience devient « the normative yardstick to measure individual and organizational fitness to adapt » (Lemke 2021, p. 173, VERBATIM VÉRIFIÉ sur source primaire — *The Government of Things*, NYU Press, 2021, ISBN 9781479808816, en biblio) et « we are invited to adapt » aux conditions dégradées au lieu de les changer (p. 188). Dans ce langage, R-INTERDIT-ABSOLU est précisément une **contre-conduite** : il refuse l'adaptation là où l'irréversibilité commande l'abstention. Cet appui **renforce** l'asymétrie jonasienne revendiquée par la grammaire (la symétrie résilience/catastrophe est ce que Jonas refuse) — renforcement d'ancrage, sans effet sur la règle.

**3.2 — R-HABITABILITE-CAPABILITE (Couche 3, couplage G-RESPONSABILITE ↔ G-JUSTICE)**

> R-HABITABILITE-CAPABILITE (Couche 3, couplage G-RESPONSABILITE ↔ G-JUSTICE)
>
> Source : Amendement A2, Morizot & Neyret 2026 (précondition habitabilité-dignité),
>
> **Nussbaum 2000 — *pour la seule condition d'identification des individus affectés (C1)***

> ### `[PORTÉE DU BLOC SOURCE]`
>
> **Nussbaum fonde la condition C1 de la règle, non la valeur qu'elle écrit** : cette même note déclare *« HABITABILITE_PRODUCTIVE et INTEGRITE_ECOSYSTEMIQUE ne proviennent pas de Nussbaum (individualiste — leur ancrage systémique la dépasse) »*.
>
> | Ce que Nussbaum fonde | Ce qu'elle ne fonde pas |
> | --- | --- |
> | La **condition C1** — identification des individus affectés ; capabilités plancher comme **seuil et non idéal** (Nussbaum 2006) | La **valeur écrite** — `habitabilite_systemique` = HABITABILITE_PRODUCTIVE, d'ancrage **Morizot & Neyret 2026** et **Schlosberg 2007** |
>
> **La règle couple deux régimes et l'assume (tension T5) ; elle ne présente pas le second sous l'autorité du premier.**
>
> `[MOTIF]` **Un en-tête peut revendiquer une autorité que le corps refuse** — cf. « Canguilhem, source primaire » (§2.1) et « Nussbaum 2000 » sur `type_capabilité_centrale` (NT-G7). **Les blocs source sont le point aveugle du set** : ils sont écrits une fois, à la création de la règle, et jamais relus quand le corps évolue.

> Condition : etathabitabilitemilieu = INHABITABLE (F2)
>
> ET entités vivantes concernées identifiées (DID dans defiinventairemilieu)
>
> ET seuilentreecommunautemorale ≠ NONDECLARE pour chaque entité identifiée (A1)
>
> \[condition d'identification des individus affectés — Nussbaum 2006\]
>
> Action : → Inscription automatique dans C-CAPABILITES :
>
> capabiliteplancher = "conditions de vie sur Terre"
>
> effetcapabilite = DESTRUCTION
>
> `habitabilite_systemique` = HABITABILITE\_PRODUCTIVE
>
> \[cf. section 4, NT-G7\]
>
> → Déclenchement R-CAPABILITES (F6) — protection automatique
>
> → Alerte vers F4 : appelimmanent += score proportionnel à
>
> intensitecodegradation

**Vérification de cohérence (commutativité) :** Le trajet F4→F6 (appelimmanent → R-CAPABILITES) et le trajet F2→F6→F4 (INHABITABLE → R-HABITABILITE-CAPABILITE → appelimmanent) **commutent** : **sous la condition de cohérence déclarée à l'inscription**, et seulement sous elle. `V1_commute_ssi_coherence` établit la caractérisation : pour un même acteur, les deux règles rendent le même verdict **si et seulement si** la cohérence tient. `V1_commutatif` en est le sens « si », lu dans le type `ActeurF4Coherent` (NT-ARCH §8ter-bis, R-3) ; `V1_coherence_discrimine` exhibe la divergence d'une paire incohérente. **La cohérence elle-même est déclarée, non démontrée.** Condition établie par la preuve : la commutativité tient si et seulement si appelimmanent (A2) et puissanceaffirmative (A3) sont déclarés **cohérents à l'inscription** — A2 et A3 forment une paire couplée obligatoire (ActeurF4Coherent.coherence), ils ne peuvent être inscrits séparément. *La co-obligation est une obligation de **déclaration** : les deux se déclarent ensemble. Une paire **non cohérente** ou incomplète **s'inscrit** avec le marqueur `[PAIRE F4 NON COHÉRENTE]` — elle n'est pas refusée ; le type `ActeurF4Coherent` décrit le domaine sans marqueur. A2 et A3 sont ici les **amendements** de NT-G2, non les axiomes A2 et A3.* **Réserve Nussbaum :** Nussbaum 2006 est individualiste (la continuité d'une espèce n'a de poids moral que via le bien d'individus existants, ch. 6) ; l'habitabilité traitée comme propriété systémique émergente (Morizot-Neyret) ne commute avec ce registre qu'après identification des individus affectés — d'où la condition d'identification ci-dessus. Médiation individualiste/systémique non close formellement en V1–V4 (nécessite la 2-cellule ProfReg complète de l'Annexe G, hors Mathlib actuel) — cf. tension T5 §9.

**Condition de réfutation :** Si R-HABITABILITE-CAPABILITE, une fois déclenchée, ne produisait aucune modification observable dans C-CAPABILITES sur deux cycles, la règle serait un \[ENGAGEMENT SANS SYMÉTRIE\] formel sans effet opérationnel.

**3.3 — Couplage G-RESPONSABILITE ↔ G-MIMETIQUE (sens R→M et M→R)**

**Instrumentation :** les deux sens sont formalisés ; le sens M→R l'est dans F7 par l'amendement A5.

> Sens R→M :
>
> Signal RISQUEEXISTENTIELIMMINENT (F4)
>
> → activation automatique du champ diagnosticmimetique dans C-MIMETISME (F7)
>
> → champ pré-rempli : "crise existentielle = terrain privilégié de médiation
>
> interne (Girard) — vérifier unanimitefocalisation"
>
> → alerte R-VICTIME-EMISSAIRE avant résolution de la crise
>
> Sens M→R :
>
> Signal focalisationvictimaire (F7, niveau LEV)
>
> → activation R-MECONNAISSANCE sur l'institution fondée pendant la crise
>
> → ajout dans C-SUJET-COLLECTIF : mecanismeporteur à réviser si fondé sur
>
> une focalisation victimaire (acteurexclufondation non nul)
>
> → principeprecautionasymetrique = VRAI pour les décisions post-crise
>
> concernant l'acteur exclu

**Portée architecturale :** Ce couplage affecte également NT-G8 (G-MIMETIQUE). Voir section 8 pour les actions requises sur NT-G8.

**4. Valeurs enrichies de `habitabilite_systemique` (C-CAPABILITES / NT-G7)**

> Les valeurs enrichies par cette section — HABITABILITE\_PRODUCTIVE, INTEGRITE\_ECOSYSTEMIQUE — relèvent de **`habitabilite_systemique`** (NT-G7 §3.1ter), dont les sources déclarées sont Morizot & Neyret 2026 et Schlosberg 2007, distinct de `typecapabilitecentrale` et de sa source « Nussbaum 2000 » : les deux champs portent deux régimes de qualification.
>
> `[POINT DE GOUVERNANCE]` **Ce champ est déclaré par NT-G7 et enrichi par NT-G2** : deux grammaires écrivent dans un même champ, et sa « règle de révision » vit ici plutôt que chez son propriétaire : un défaut visible depuis NT-G2 n'est corrigeable que depuis NT-G7.

**Valeurs de `habitabilite_systemique`** (Amendement B5 — source : Morizot & Neyret 2026, Nussbaum 2006, Schlosberg 2007).

**Sources distinguées :** Les trois valeurs ne partagent pas la même source. HABITABILITE\_PRODUCTIVE et INTEGRITE\_ECOSYSTEMIQUE ne proviennent pas de Nussbaum (individualiste — leur ancrage systémique la dépasse). Distinction de source ci-dessous.

> HABITABILITE\_PRODUCTIVE Capacité fonctionnelle systémique d'une entité
>
> non-humaine à maintenir les conditions de la vie
>
> (pollinisation, régulation climatique, fertilisation
>
> des sols).
>
> Source : Morizot & Neyret 2026 \[VÉRIFIÉ\]
>
> INTEGRITE\_ECOSYSTEMIQUE Capacité d'un écosystème à maintenir ses processus
>
> de régénération. Dépasse Nussbaum (capabilité
>
> systémique, non individuelle).
>
> Source : Schlosberg, Defining Environmental Justice,
>
> OUP, 2007, **p. 136, section « Recognizing Integrity »**
>
> (extension aux écosystèmes p. 137)
>
> \[VÉRIFIÉ SUR SOURCE PRIMAIRE\].
>
> Terme exact chez Schlosberg : « integrity of systems » /
>
> « autonomous integrity » — « *the quality of a self-directing,
>
> self-regulating, or self-correcting entity or system* » (p. 136),
>
> articulant autonomie + résilience + autopoïèse.
>
> **Registre tranché =
>
> normatif/recognitionnel** (l'intégrité comme fondement du respect
>
> et de la justice) ; le versant indicateur mesurable (Karr/Cairns)
>
> n'est pas retenu.
>
> *Note de Couche 0 : Schlosberg définit une intégrité large*
>
> *(de la « bodily integrity » individuelle, Nussbaum p. 395,*
>
> *jusqu'aux écosystèmes p. 137) ; ce champ en instancie le seul*
>
> *versant écosystémique — restriction déclarée.*
>
> ENVIRONNEMENT\_PROPRE Capacité d'un être vivant à vivre dans son propre
>
> environnement naturel (« life with other species »,
>
> mobilité dans l'habitat naturel).
>
> Source : Nussbaum 2006, Frontiers of Justice, ch. 6
>
> \[VÉRIFIÉ\]

**Champ de traçabilité :**

> source\_revision\_capabilite DID DID de la délibération ayant confirmé ou
>
> révisé la valeur. Trace si la valeur a été
>
> importée de Nussbaum ou co-construite
>
> collectivement. Empêche la fermeture de
>
> REVISIONCONCEPTUELLE (Hache 2011).

**Règle de révision :** Toutes les valeurs de **`habitabilite_systemique`** listées ci-dessus sont révisables par REVISIONCONCEPTUELLE (Hache 2011). Aucune ne peut être posée comme universelle sans source\_revision\_capabilite renseigné.

**Ancrage de source (amendement P3, Hache 2011) :** l'exigence que source\_revision\_capabilite empêche la fermeture de REVISIONCONCEPTUELLE est ancrée dans Hache (2011), ch. 4 “ Moraliser l'économie ? ”, pp. 102-103 : “ ce qu'il y a de moral dans ces calculs n'est pas soluble dans une procédure ou une quantification \[...\] accompagner la dimension morale d'une évaluation économique, c'est, littéralement, \[...\] rendre visibles les préoccupations morales à l'œuvre ”. Tout seuil ou toute capabilité calculé(e) doit donc demeurer visible dans son ancrage moral ; c'est la raison pour laquelle source\_revision\_capabilite est obligatoire. Statut de la citation : **VÉRIFIÉ** (lecture directe, pages identifiées — fichier hache-2011-4-moraliser-leconomie.pdf).

**5. Couplages avec les autres grammaires**

| **Grammaire**                | **Sens** | **Règle**                                                                                     | **Statut**                                                                                                                                     |
| ---------------------------- | -------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Annexe G (formel calculable) | R↔Exist  | Catégorie indexée Exist + C-INDEXATION-HORIZON → R-INTERDIT-ABSOLU                            | Couplage bidirectionnel formalisé — irréversibilité jonasienne calculable (absence d'inverse à droite dans ProfReg)                                 |
| G-JUSTICE (F6)               | R→J      | R-HABITABILITE-CAPABILITE (A2) ; R-HERMENEUTIQUE comme précondition à DELIBERATION (sens R→J) | Formalisé — commutation **sous cohérence déclarée** (V1 : `V1_commute_ssi_coherence`, caractérisation ; `V1_commutatif`, lecture)                                                                                               |
| G-MIMETIQUE (F7)             | R↔M      | Sens R→M et M→R (A5)                                                                          | Formalisé                                                                                                                                           |
| G-PERFORMATIVITE (F3)        | P→R      | R-PERMIS-PERFORMATIF (B6 — voir NT-G6)                                                        | Proposé — portée NT-G6                                                                                                                              |
| G-RESPONSABILITE (Couche 0)  | —        | B1 : regime\_obligation + C-STATUT-DETTE + transitions V4                                     | Consolidé — \[INCOHÉRENCE INTER-COUCHES\] confirmée ET résolue (V2 : systemique\_requires\_R1\_extension ; V4 : machine d'états transition\_valide) |

**Couplage G-RESPONSABILITE ↔ G-JUSTICE — asymétrie hiérarchique :**

Morizot & Neyret (2026) posent l'habitabilité comme *précondition* des capabilités. Cette relation est asymétrique : etathabitabilitemilieu = INHABITABLE est un signal déclencheur automatique de capabiliteplancher menacée — non l'inverse. R-HABITABILITE-CAPABILITE formalise cette asymétrie.

**5bis. Position vis-à-vis des positions concurrentes**

G-RESPONSABILITE ne réduit pas l'éthique de la responsabilité à une analyse coûts-bénéfices. L'heuristique de la peur (cf. §1) est asymétrique par construction : le risque de catastrophe irréversible n'a pas de contrepartie symétrique en opportunité manquée. Cette asymétrie est un \[ENGAGEMENT SANS SYMÉTRIE\] délibéré et assumé dans la logique jonasienne, non une incohérence — elle est signalée explicitement et rendue calculable (Annexe G) pour éviter qu'elle soit invoquée rhétoriquement.

La grammaire se distingue ainsi de deux familles d'approches : (1) les approches conséquentialistes agrégatives, qui mettraient en balance la perte irréversible et un gain attendu — ce que l'heuristique de la peur interdit ; (2) les approches purement procédurales sans seuil d'irréversibilité, qui laisseraient hors-champ comptable précisément ce qu'aucune compensation ne rattrape. La distinction appelimmanent / puissanceaffirmative (§2.2) permet en outre de ne pas confondre la résistance défensive d'un vivant et sa contribution active à l'habitabilité — distinction absente des cadres fondés sur la seule sentience individuelle.

**Positionnement Hache / Jonas (amendement P2) :** Hache (2011) hérite de Jonas mais lui adresse une critique structurée (ch. 1 “ Changer de question ”, pp. 20-25) : Jonas “ représente la première génération de philosophes écologistes \[...\] qui ont rompu radicalement avec la philosophie morale classique ”, mais “ la philosophie morale à laquelle appelait le texte de Jonas est restée à l'état de projet — il s'est plus intéressé à fonder métaphysiquement le concept de responsabilité qu'à explorer le chantier moral qu'il ouvrait ”. G-RESPONSABILITE doit donc déclarer **où elle suit Jonas et où elle suit Hache** : elle suit Jonas pour l'heuristique de la peur et appelimmanent (fondement de l'irréversibilité), et elle suit Hache pour REVISIONCONCEPTUELLE (révision des catégories quand les ressources conceptuelles manquent à bien traiter un être). Sans cette distinction explicite, le couplage Jonas-Hache de la note serait un **\[DÉCOUPLAGE DE RÉGIMES NON DÉCLARÉ\]** ; il est ici déclaré et tracé.

**6. Conditions de réfutation**

En régime vérifiabilité-cohérence, G-RESPONSABILITE est réfutable si :

> 1\. **\[RÉFUTATION R1\]** Si R-HABITABILITE-CAPABILITE (A2), une fois déclenchée, ne produisait aucune modification observable dans C-CAPABILITES sur deux cycles — la règle serait un \[ENGAGEMENT SANS SYMÉTRIE\] formel sans effet opérationnel.
>
> 2\. **\[RÉFUTATION R2\]** Si puissanceaffirmative (A3) ne corrélait pas avec des indicateurs biophysiques mesurables (defiinventairemilieu dans F2) — le champ serait \[PLAUSIBLE, NON VÉRIFIÉ\] et devrait être remplacé par un indicateur co-construit avec des experts écologues (logique des valorimètres Callon et al. 2025).
>
> 3\. **\[RÉFUTATION R3\]** Si principe\_intergenerationnel = NON\_DECLARE était la valeur dominante après deux cycles de délibération — la distinction des principes de Gosseries serait sans effet pratique et devrait être simplifiée.
>
> 4\. **\[RÉFUTATION R4\]** Si aucun signal OBLIGATIONSANSRECIPROCITE n'était jamais déclenché sur les interactions enregistrant des obligations envers des entités non-humaines, la scission du champ sujetresponsable (A1) serait sans effet sur le comportement du registre.
>
> 5\. **\[RÉFUTATION R5\]** Si le couplage G-RESPONSABILITE ↔ G-MIMETIQUE (A5) ne produisait aucune activation de diagnosticmimetique lors d'une crise existentielle réelle, le sens R→M serait une règle vide.

**7. Actions en cours et horizon de vérification**

* * **Vérification des actions : les statuts ci-dessous s'appuient sur les Rapports de vérifications formelles V1+V2+V3+V4 et V4c+V10b+VJE (§10), sur l'état de référence de ProfReg (Consolidé §1 ; encadré « Appuis formels (ProfReg) » ci-dessous) et sur les lectures Gosseries 2023 / Nussbaum 2006.**

**Actions — statut**

| **ID action** | **Description**                                                       | **Horizon** | **Porteur** | **Statut**                                                                                                                                        |
| ------------- | --------------------------------------------------------------------- | ----------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ACT-G2-001    | Vérifier commutativité des carrés F4↔F6 dans ProfReg (Annexe G)       | Vague C.1   | Porteur MRC | ✅ RÉSOLU —  commutation **caractérisée** (`V1_commute_ssi_coherence`), sous condition de co-obligation A2+A3 **déclarée**                                                                          |
| ACT-G2-002    | Résoudre désignation sujetresponsable pour entités non-humaines       | Vague C.2   | Porteur MRC | 🟠 PARTIELLEMENT RÉSOLU — A1 (obligation avant porteur) + seuilentreecommunautemorale ; représentation politique reste ouverte (B3, cf. NT-ARCH) |
| ACT-G2-003    | Formaliser articulation habitabilité ↔ capabilités comme règle dédiée | Vague C.1   | Porteur MRC | ✅ RÉSOLU — A2 formalisé + commutativité prouvée (V1) + condition d'identification des individus (Nussbaum)                                     |

**Actions — statut (suite)**

| **ID action** | **Description**                                                               | **Horizon**             | **Porteur**    | **Statut**                                                                                                                                                                                 |
| ------------- | ----------------------------------------------------------------------------- | ----------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ACT-G2-004    | Co-construire seuilpuissanceaffirmative avec experts écologues                | Vague C.2               | À désigner     | 🟠 EN ATTENTE — nécessite DID expert écologue ; tension T2 résiduelle (stabilité du seuil)                                                                                                       |
| ACT-G2-005    | Vérifier compatibilité de B1 (regime\_obligation) avec R1 dans ProfReg        | Avant implémentation B1 | Porteur MRC    | ✅ RÉSOLU — \[INCOHÉRENCE INTER-COUCHES\] confirmée ET résolue (V2 : systemique\_requires\_R1\_extension) par introduction de C-STATUT-DETTE                                                     |
| ACT-G2-006    | Contrôler Gosseries (titre, édition, taxinomie principes intergénérationnels) | Avant validation A4     | Documentaliste | 🟢 RÉSOLU — source : *What is Intergenerational Justice?*, Polity, 2023 ; taxinomie à 4 principes vérifiée sur recensions IGJR 2024 + JPE 2024. Reste : contrôle page-à-page sur source primaire |
| ACT-G2-007    | Contrôler Nussbaum 2006 Frontiers of Justice — liste capabilités non-humaines | Avant validation B5     | Documentaliste | 🟠 PARTIELLEMENT RÉSOLU — ch. 6 vérifié (ENVIRONNEMENT\_PROPRE, sentience) ; liste complète nécessite lecture intégrale ch. 6 + index                                                            |
| ACT-G2-008    | Implémenter C-STATUT-DETTE comme extension de R1                              | Avant implémentation B1 | Porteur MRC    | 🟠 SPÉCIFIÉ FORMELLEMENT (V2+V4) — reste l'implémentation dans le registre ; cf. NT-ARCH                                                                                                         |
| ACT-G2-009    | Inscrire biconditionnelle fraction\_actorielle=1 ↔ ACTORIEL comme règle C1    | Avant implémentation B1 | Porteur MRC    | ✅ RÉSOLU par déclaration — règle de Couche 1, non convention de Couche 2 ; `B1_coherence_condition` est une forme 1 déclarée, jamais appui seul (Consolidé §2.2)                                                                                         |

**Actions — formalisation et implémentation**

| **ID action** | **Description**                                                                                 | **Horizon**             | **Porteur**              | **Statut**                                                                                                                                                                                                                                            |
| ------------- | ----------------------------------------------------------------------------------------------- | ----------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ACT-G2-010    | Compléter la 2-cellule ProfReg de l'Annexe G (préservation régime ACTORIEL par transition V4c)  | Hors Mathlib actuel     | Porteur MRC + formaliste | ✅ RÉSOLU PROCÉDURAL — V4c\_actoriel\_preserved, V4c\_regime\_unchanged, V4c\_actoriel\_preserved\_alias *(alias de V4c\_actoriel\_preserved ; les trois sont des formes 1 déclarées)*, compilés 1er juin 2026, 0 sorry. Lacune résiduelle déclarée : 2-cellule G.9.3 hors Mathlib — horizon v6.x.                                           |
| ACT-G2-011    | Clore la médiation individualiste/systémique (tension T5) entre Nussbaum et registre systémique | Vague C.2               | Porteur MRC              | 🟡 PARTIELLEMENT CLOS — ACT-G2-010 RÉSOLU procédural. Médiation individualiste/systémique (T5) partiellement couverte par V1 (commutativité F4↔F6). Reste structurel (Schlosberg 2007 via Cannavó 2008) — Vague C.2. |
| ACT-G2-012    | Implémenter le typage InventaireNonVide de la phase INVENTAIRE-ASSETS-ACTIFS (B2)               | Avant implémentation B2 | Porteur MRC              | 🟠 SPÉCIFIÉ (V4 : inventaire\_nonempty\_required,  lecture du type, témoin `inventaire_nonempty_discrimine`) — reste l'implémentation                                                                                                                                            |

**Appuis formels (ProfReg).** La grammaire n'établit aucune thèse par preuve ; ProfReg établit la **forme** de ses règles sur six points (natures : Consolidé §2.2) :
- **cascade R-INTERDIT-ABSOLU et machine d'états** (§3.1, note de déclenchement) : V4 (`transition_valide` ; `inventaire_nonempty_required`, lecture du type, témoin `inventaire_nonempty_discrimine`) ; le niveau CRITIQUE n'est atteint que par l'attribution (`critique_exige_attribution`, PR-3, résultat) ;
- **seuil d'entrée et attribution** (§1, condition (1) ; NT-ARCH §7bis, ACT-ARCH-001) : PR-3 — un seuil non déclaré interdit l'attribution (`seuil_non_declare_interdit_attribution`, `attribution_exige_un_seuil_declare`) et ferme donc la porte de CRITIQUE (`seuil_non_declare_bloque_critique`) ; composé avec PR-10, l'attribution exige le quadruplet complet du statut du seuil (`attribution_exige_seuil_et_quadruplet`) ; témoin `PR3_clauseSeuil_temoin_mal_forme`. *Délimitation :* PR-3 porte sur l'**attribution** (`C-STATUT-DETTE = ATTRIBUEE`) ; la règle d'**inscription** de `obligationrelationnelle_declaree` (§2.1, A1) reste déclarée, sans théorème ;
- **statut du seuil de `seuilpuissanceaffirmative`** (§2.1quinquies) : PR-10, `seuil_valuatif_must_declare_status` ;
- **commutativité F4↔F6** (§3.2) : V1, `V1_commute_ssi_coherence` (résultat), sous la cohérence A2+A3 déclarée à l'inscription ; **B1 vs R1** : V2, `systemique_requires_R1_extension` (lecture R-7) ;
- **carré B1↔B2 et phase INVENTAIRE-ASSETS-ACTIFS** : PR-51 (§9, point 1) ; PR-4 — des trois déclencheurs de l'inventaire, chacun suffit (`PR4_les_trois_declencheurs_suffisent_chacun`) ; l'appel immanent non entendu y entre comme projection booléenne **déclarée** du signal F4, et seul le milieu se constate sur un état (`le_milieu_declenche_sans_qu_aucun_acteur_ait_declare`) ; la clôture est interdite sans inventaire (`cloture_interdite_sans_inventaire`), et le type seul n'en produit aucun (`le_type_ne_produit_aucun_inventaire`) ;
- **`fraction_actorielle` et charge de la preuve** : CONV-1 et `fraction_exhibe_une_source_eventuellement_vide` (PR-27), réfutation du seul candidat de calcul `CB3_candidate_not_oplax_monoidal` (§9, point 5) ; forme du renversement de la charge : PR-15 (ancrage contre-capture, fin de note).

**Hors ProfReg :** le carré triangulaire NT-G7 ↔ NT-G2 ↔ NT-ARCH (CONV-2 ; V10b ne porte aucun théorème) ; la 2-cellule G.9.3 (V4c, ACT-G2-010) ; la médiation individualiste / systémique (T5) ; la stabilité de `seuilpuissanceaffirmative` (T2) ; la tension T4.

**8. Impacts sur les autres notes de travail**

Les amendements A2, A5 et B1-B6 ont des portées transversales. Les modifications suivantes sont requises sur d'autres NT :

| **Note**                                | **Impact**                                                                                                                                                                                                                                                                                                                                          | **Amendement source** | **Priorité**                                                                                                                       |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **NT-G7** (G-JUSTICE / C-CAPABILITES)   | Ajout valeurs HABITABILITE\_PRODUCTIVE \[VÉRIFIÉ\], INTEGRITE\_ECOSYSTEMIQUE \[Schlosberg 2007 — VÉRIFIÉ SUR RECENSION\], ENVIRONNEMENT\_PROPRE \[Nussbaum 2006 ch.6 — VÉRIFIÉ\] + champ source\_revision\_capabilite                                                                                                                               | A3, B5                | Haute                                                                                                                              |
| **NT-G8** (G-MIMETIQUE)                 | Formalisation sens M→R du couplage G-MIMETIQUE ↔ G-RESPONSABILITE                                                                                                                                                                                                                                                                                   | A5                    | Haute                                                                                                                              |
| **NT-G6** (G-PERFORMATIVITE)            | Ajout R-PERMIS-PERFORMATIF (couplage G-PERFORMATIVITE ↔ G-RESPONSABILITE)                                                                                                                                                                                                                                                                           | B6                    | Moyenne                                                                                                                            |
| **NT-ARCH** (Architecture / Couche 0+1) | Ajout regime\_obligation + fraction\_actorielle (DÉCLARÉE) + collectif\_hybride\_declare + C-STATUT-DETTE + machine d'états transition\_valide (4 règles de transition V4, Couche 1) + phase INVENTAIRE-ASSETS-ACTIFS typée InventaireNonVide + phase REPRESENTATION-PROSPECTIVE (+ legitimiterepresentant + conditionrefutation) dans C-ENQUETE-V5 | B1, B2, B3            | Critique — \[INCOHÉRENCE INTER-COUCHES 0-1\] résolue formellement (V2+V4) ; reste implémentation + 2-cellule Annexe G (ACT-G2-010) |

**9. Lacunes et limites**

\[LACUNES ET LIMITES\]

> 1\. Carrés de commutativité et cascade. Les commutativités F4↔F6 (V1) et la cohérence de la cascade R-INTERDIT-ABSOLU (V4) sont **prouvées** ; **la commutativité B1↔B2 est conclue sur les chemins admissibles** (PR-51, `carre_B1B2_commute_sur_les_chemins_admissibles`), une fois **déclarée** la règle des pas entre phases — **CONV-2 étendue** (Annexe §A.15.9) reste une convention : aucun chemin admissible n'atteint la délibération sans inventaire (`aucune_deliberation_sans_inventaire`), le chemin direct n'est pas admissible dès que l'inventaire est requis (`le_chemin_direct_n_est_pas_admissible`), et la commutation n'est jamais une dispense d'inventaire. `V3_commutatif` est vrai par construction (les deux branches systémiques de `chemin_direct` rendent `deliberation`, comme `chemin_via_inventaire` : forme 1, patron V10b / B-5) ; il n'est qu'une **lecture** des deux définitions, jamais appui. Le carré triangulaire NT-G7 ↔ NT-G2 ↔ NT-ARCH reste procédural (CONV-2). **V4c et V10b sont des `RÉSOLUS PROCÉDURAUX`**, à ne pas surdéclarer comme prouvés formellement. **Le carré J↔E ne commute pas sans révision inscrite** : `VJE_carre_ne_commute_pas_sans_revision` établit que **le carré ne se ferme pas de lui-même**, et `VJE_ferme_apres_revision_externe` que la révision en est une **prémisse**. ACT-G2-010 → RÉSOLU PROCÉDURAL (V4c\_actoriel\_preserved, V4c\_regime\_unchanged, V4c\_actoriel\_preserved\_alias *(alias de V4c\_actoriel\_preserved ; les trois sont des formes 1 déclarées)*, compilés 1er juin 2026, 0 sorry). Lacune résiduelle déclarée : 2-cellule ProfReg complète (G.9.3) hors Mathlib actuel — horizon v6.x.
>
> 3\. **Nussbaum, Frontiers of Justice (2006) : partiellement vérifié.** Le ch. 6 (sentience comme seuil, ENVIRONNEMENT\_PROPRE) est vérifié en régime procédural. La liste complète des capabilités animales nécessite la lecture intégrale du ch. 6 et de l'index (ACT-G2-007).
>
> 4\. **Schlosberg 2007 — INTEGRITE\_ECOSYSTEMIQUE : \[VÉRIFIÉ SUR SOURCE PRIMAIRE\].** Définition-source : **p. 136, section « Recognizing Integrity »** — « integrity of systems » / « autonomous integrity », « *the quality of a self-directing, self-regulating, or self-correcting entity or system* » ; extension « to larger ecosystems » p. 137 ; continuité avec la « bodily integrity » individuelle (Nussbaum p. 395). « Ecological integrity » : 0 occurrence. Registre TRANCHÉ = normatif/recognitionnel ; convergence documentée avec le corpus d'intégrité écologique joint (Karr & Dudley 1981 ; Cairns 1977 — noyau commun résilience + auto-organisation), sans traitement en indicateur mesurable. Ne pas confondre avec « physical integrity of nature » (p. 192, autre passage — signaux de délibération).
>
> 5\. **\`fraction\_actorielle\` comme valeur délibérée — RÉSOLU (T1).** Ce que ProfReg établit : l'obligation de déclaration est portée par **CONV-1** (obligation déclarée) et `fraction_exhibe_sa_source` (qui exhibe le champ source — **éventuellement vide** : `fraction_exhibe_une_source_eventuellement_vide`, PR-27) — et le foncteur de calcul candidat est réfuté ( `CB3_candidate_not_oplax_monoidal`) ; l'inexistence générale d'un calcul n'est pas prouvée — c'est une lacune déclarée. convention\_attribution\_seuil est obligatoire ; révision obligatoire à chaque cycle reste un garde-fou procédural à maintenir.
>
> 6\. **Tension T5 — Nussbaum individualiste vs. registre systémique : partiellement résolue.** A2 ajoute une condition d'identification des individus affectés avant déclenchement. La médiation individualiste/systémique n'est pas close formellement en V1–V4 (nécessite la 2-cellule ProfReg complète de l'Annexe G). \[DÉCOUPLAGE DE RÉGIMES STRUCTUREL — documenté dans Schlosberg 2007 lui-même (Cannavó 2008)\], non un défaut propre au MRC (ACT-G2-011).
>
> 7\. **\`seuilpuissanceaffirmative\` (T2 résiduelle).** Seuil à co-construire ; s'il est traité comme fixe (même co-construit une fois), il risque de clore REVISIONCONCEPTUELLE (Hache 2011). Résolution : date de révision obligatoire + source\_valuemetre rattachant le seuil à une délibération périodique. \[PLAUSIBLE, NON VÉRIFIÉ — la stabilité du seuil reste une tension structurelle\].
>
> 8\. **Tension T4 — Callon et al. comme fondateurs critiques du MRC : NON RÉSOLUE (structurelle permanente).** \[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ — tension fondatrice\] Toute architecture comptable porte le risque de financiarisation (Callon et al. 2025, Part 2). Hors portée du mode formel calculable : gouvernée procéduralement, non éliminée, par trois conditions nécessaires (non suffisantes) : (1) source\_valuemetre toujours renseigné et traçable ; (2) REVISIONCONCEPTUELLE reste une phase ordinaire ; (3) convention\_attribution\_seuil interdit tout seuil posé comme universel.

**10. Sources**

| **Auteur**                                     | **Titre / Référence**                                                                                                                                         | **Statut**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Jonas, H.                                      | *Le Principe Responsabilité* (Cerf, 1990 \[1979\])                                                                                                            | VÉRIFIÉ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Morizot, B. & Neyret, L.                       | *Liberté, dignité, habitabilité. Donner au siècle la valeur qui lui manque*, Tracts n° 70, Gallimard, 2026, pp. 3-65 (Cairn 9782073167996)                    | VÉRIFIÉ (biblio) — passage pollinisateurs p. 32 VÉRIFIÉ (contrôle des sources) ; « habitabilité productive » non paginée                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Nussbaum, M.                                   | *Women and Human Development* (2000)                                                                                                                          | VÉRIFIÉ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Nussbaum, M.                                   | *Frontiers of Justice* (2006)                                                                                                                                 | VÉRIFIÉ (ch. 6) — liste complète des capabilités animales à contrôler                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Gosseries, A.                                  | *What is Intergenerational Justice?* (Polity, 2023)                                                                                                           | VÉRIFIÉ sur recensions IGJR 2024 + JPE 2024 — taxinomie à 4 principes                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Callon, M., Caliskan, K. & MacKenzie, D.       | « Ecologization, part 1 & 2 », *Economy and Society*, 2025, DOI 10.1080/03085147.2025.2488121 et 10.1080/03085147.2025.2498825                                | VÉRIFIÉ (biblio) — références paginées à contrôler                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Schlosberg, D.                                 | *Defining Environmental Justice* (OUP, 2007)                                                                                                                  | VÉRIFIÉ SUR SOURCE PRIMAIRE (biblio) — p. 136 « Recognizing Integrity » (« integrity of systems » / « autonomous integrity ») ; extension écosystèmes p. 137 ; registre normatif/recognitionnel tranché                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Cannavó, P. F.                                 | Recension de Schlosberg, *Ethics & International Affairs*, Vol. 22 n°3, Fall 2008, pp. 336-338                                                                | VÉRIFIÉ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Rapport de vérifications formelles V1+V2+V3+V4 | ** Lean 4 / ProfReg — Rapport V1+V2+V3+V4 (30 mai 2026, 13 théorèmes) + Rapport V4c+V10b+VJE (1er juin 2026, 11 théorèmes) — total 30 théorèmes prouvés, 0 sorry | VÉRIFIÉ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Hache, E.                                      | *Ce à quoi nous tenons* (2011)                                                                                                                                | VÉRIFIÉ — source de REVISIONCONCEPTUELLE : ch. 2 “ Comment répondre ? ” p. 55 (révision des règles devenues trop étroites, d'après James) ; ch. 1 p. 31-32 (l'absence de ressources pour bien traiter un être est un défaut du registre, non de l'être) ; ch. 4 p. 102-103 (le moral n'est pas soluble dans la quantification → source\_revision\_capabilite). Lien REVISIONCONCEPTUELLE → injustice herméneutique (Fricker 2007) = couplage MRC déclaré, non héritage bibliographique (cf. §2.1, §5bis, NT-G7 bloc D). |
| Girard, R.                                     | *(sources G-MIMETIQUE — voir NT-G8)*                                                                                                                          | Voir NT-G8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Fricker, M.                                    | *Epistemic Injustice* (2007)                                                                                                                                  | VÉRIFIÉ — via NT-G7                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

# 11\. Note de vulgarisation — G-RESPONSABILITE pour le site-vitrine du MRC

*Destination : site-vitrine du MRC. Public : académiques non spécialistes de l'éthique de la responsabilité et de la justice intergénérationnelle, y compris des chercheurs dont les cadres théoriques sont éloignés ou critiques de ces programmes. Régime : vérifiabilité-cohérence.*

## Pourquoi un registre doit inscrire ce qu'il ne pourra pas réparer

Un collectif décide, agit, échange. Certaines de ses décisions engagent des êtres qui ne sont pas à la table : les générations qui ne sont pas encore nées, les espèces qui ne votent pas, les milieux qui ne déposent pas plainte. Quand une décision franchit un seuil d'irréversibilité — une forêt qui ne repoussera pas, un climat qui ne reviendra pas, une espèce qui disparaît — aucune compensation ultérieure ne rétablit l'état antérieur. Le MRC — Modèle de Registres de Communalité — inscrit ce type d'engagement comme information de conception dans la grammaire G-RESPONSABILITE, au lieu de le laisser hors-champ comptable.

## Ce que G-RESPONSABILITE affirme — et ce qu'elle n'affirme pas

G-RESPONSABILITE s'appuie sur l'éthique de la responsabilité (Jonas), sur des travaux d'écologie philosophique (Morizot & Neyret) et sur la justice intergénérationnelle (Gosseries). Ces programmes suscitent des débats légitimes. Il est nécessaire de nommer d'emblée ce que cette grammaire ne fait pas.

Elle n'affirme pas que les entités non-humaines ont des « droits » au même sens que les personnes, que toute irréversibilité est interdite, ni qu'un calcul peut trancher à la place d'une délibération politique. Ce qu'elle affirme est plus limité : lorsqu'une obligation envers un vivant — humain ou non — est en jeu et qu'une irréversibilité menace, le registre doit inscrire cette obligation, désigner (ou reconnaître l'absence de) son porteur, et rendre la décision réfutable. Ignorer une obligation parce qu'aucun porteur n'est encore identifié n'est pas neutre.

## Le principe responsabilité (Jonas 1979)

Hans Jonas (*Le Principe Responsabilité*, 1979) déplace le centre de l'éthique : ce n'est plus la réciprocité entre contemporains égaux, mais la vulnérabilité de ce qui peut être détruit irréversiblement par notre puissance technique. Une entité vivante émet un « appel immanent » — une résistance propre à sa destruction — qui précède toute reconnaissance juridique. Transposé au MRC : le champ appelimmanent capte cette finalité défensive, et une obligation peut être inscrite avant même qu'un responsable soit désigné. L'absence de porteur ne supprime pas l'obligation ; elle ouvre une délibération sur qui doit la porter.

## Habitabilité avant capabilités (Morizot & Neyret 2026)

Morizot & Neyret (*Liberté, dignité, habitabilité*, 2026) posent l'habitabilité d'un milieu comme *précondition* de toute vie digne : sans conditions de vie maintenues, parler de libertés ou de capabilités est vide. Le MRC en tire une asymétrie inscrite dans le registre : un milieu devenu inhabitable déclenche automatiquement une alerte sur les capabilités-plancher menacées (règle R-HABITABILITE-CAPABILITE), et non l'inverse. La grammaire distingue aussi la simple résistance d'un vivant (appelimmanent) de sa contribution active à l'habitabilité (puissanceaffirmative) : la disparition des pollinisateurs n'émeut aucun appel individuel significatif, mais franchit collectivement un seuil d'irréversibilité productive.

## Le seuil d'entrée dans la communauté morale (Nussbaum 2006)

Martha Nussbaum (*Frontiers of Justice*, 2006, ch. 6) fonde le statut moral des animaux non-humains sur leur dignité propre et leur capacité à s'épanouir selon leur forme de vie. La sentience est le seuil d'entrée dans la communauté morale — mais la valeur ne s'y réduit pas. Nuance critique inscrite dans le MRC : Nussbaum est *individualiste* — la continuité d'une espèce n'a de poids moral que si elle passe par le bien d'individus existants. Le MRC traite par ailleurs l'habitabilité comme propriété systémique. Ces deux régimes ne se rejoignent qu'après identification des individus affectés ; cette tension est documentée, non lissée (elle est elle-même reconnue comme non résolue chez Schlosberg 2007, recension Cannavó 2008).

## Justice entre les générations (Gosseries 2023)

Axel Gosseries (*What is Intergenerational Justice?*, Polity, 2023) distingue quatre principes possibles de justice intergénérationnelle : ne pas transmettre moins qu'on a hérité (NON-DECLINE), transmettre davantage (BETTER-FUTURE), garantir un seuil suffisant à chaque génération (SUFFICIENCY), ou donner priorité au moins bien loti (NARROW-PATH). Le MRC ne tranche pas entre eux : il oblige à *déclarer* lequel est appliqué, et signale comme défaut une obligation intergénérationnelle dont aucun principe n'a été délibéré. Nuance critique (Gosseries, ch. 5) : les politiques envers le futur sont inévitablement *a-légitimes* — non illégitimes, mais privées de la validation de ceux qu'elles engagent. La représentation des générations futures est une nécessité pratique, pas une solution de pleine légitimité démocratique ; le registre l'inscrit comme telle, avec une condition de réfutation obligatoire.

**La non-cléronomicité, et les trois raisons de ne pas en faire un avantage décisif.**

Une source primaire de Gosseries est au corpus : « Qu'est-ce que le suffisantisme ? », *Philosophiques*, vol. 38, n° 2, automne 2011, p. 465-492 (DOI 10.7202/1007460ar), lue intégralement. Elle ne porte **ni** la taxinomie à quatre principes **ni** l'a-légitimité du ch. 5 de 2023 — sur ces deux points l'attribution reste `[PLAUSIBLE, NON VÉRIFIÉ sur source primaire]`. Elle porte en revanche la définition de SUFFICIENCY (§2 : seuil **absolu**, « satisfaction d'un niveau minimum », *satismin*), vérifiée, et la propriété suivante.

**La propriété.** Une théorie de la justice intergénérationnelle est **cléronomique** si elle définit ce qu'une génération doit à la suivante en prenant pour référence ce dont elle a hérité de la précédente — elle est alors *réactive*. Gosseries (§4) :

> « le suffisantiste est par contre capable de définir ce qu'une génération doit à la génération suivante **sans référence aucune** à ce qu'elle a effectivement reçu de la précédente. Ce qu'il faut, c'est que la génération suivante **ait assez**. » ; note 29 : « On dirait en anglais qu'une règle non-cléronomique est *non-compliance insensitive*. » `[VÉRIFIÉ sur source primaire]`

**Ce que cela soutient dans le MRC.** Une dette qui ne se calcule pas sur l'héritage reçu **ne s'éteint pas par la défaillance du prédécesseur**. C'est l'appui le plus direct du corpus pour l'imprescriptibilité de la dette intergénérationnelle (AX-2) : le défaut d'une génération ne diminue pas l'obligation de la suivante, il la laisse entière.

**Les trois limites, données par l'auteur lui-même** — elles sont inscrites ici parce que l'argument ne peut pas être emprunté sans elles :

1. **Le suffisantisme n'est pas nécessairement non-cléronomique.** La définition de Brundtland (1987, p. 53 — « répond aux besoins du présent sans compromettre la capacité des générations futures de répondre aux leurs ») est suffisantiste **et n'est pas strictement non-cléronomique**. La propriété caractérise *certaines formes* de suffisantisme, pas la doctrine.
2. **La propriété n'est pas exclusive.** Des théories cléronomiques et **non** suffisantistes — l'utilitarisme par l'investissement, l'égalitarisme rawlsien dans une moindre mesure — comportent une obligation d'accumuler et « détiennent les ressources normatives suffisantes pour répondre au risque de dégradation progressive de l'héritage ». Le même effet s'obtient sans passer par SUFFICIENCY.
3. **Le revers.** « une doctrine non-cléronomique peut représenter un **fardeau démesuré** pour les générations succédant à d'autres qui seraient peu consciencieuses. C'est le revers de la médaille. » `[VÉRIFIÉ sur source primaire]`

`[ENGAGEMENT SANS SYMÉTRIE — évité]` La troisième limite est une **objection frontale à l'imprescriptibilité**, formulée par un défenseur du suffisantisme : elle dit que l'insensibilité au défaut du prédécesseur, qui protège les suivants, charge aussi les suivants de tout ce que les précédents n'ont pas fait. Le MRC ne la tranche pas ; il exige qu'une inscription déclarant `principeintergenerationnel = SUFFICIENCY` sur un horizon irréversible porte une `conditionrefutation` où cette charge est nommée.

`[CONDITION DE RÉFUTATION]` L'appui de la non-cléronomicité à AX-2 tombe si l'on adopte une forme cléronomique de suffisantisme (voie 1 ci-dessus) : l'imprescriptibilité doit alors être fondée ailleurs. Le set ne prescrit aucune des deux formes.

**Source.** Gosseries 2011, §4 et notes 27-30. Brundtland, G. H. *et al.*, *Our Common Future*, OUP, 1987, p. 53 `[CITÉ PAR Gosseries 2011 — non vérifié sur primaire]`.

## Réviser les catégories plutôt que trier les êtres (Hache 2011)

Émilie Hache (*Ce à quoi nous tenons*, La Découverte, 2011) récuse la question « cet être mérite-t-il d'entrer dans la communauté morale ? » comme mal posée : il ne s'agit pas de demander à un tiers s'il est apte à *être* moral, mais de se demander *comment être apte à lui répondre* (ch. 1, p. 31-32). Quand les règles d'un régime deviennent trop étroites pour nommer ce qui arrive, la pratique morale oblige à les réviser (ch. 2, p. 55, d'après James). Le MRC en tient compte doublement : le seuil d'entrée dans la communauté morale y est une *procédure* (un seuil non déclaré déclenche une délibération), non une coupure ontologique d'aptitude ; et la phase RÉVISION\_CONCEPTUELLE permet de rouvrir les catégories du registre quand elles ne permettent plus de répondre. La tension Hache / Nussbaum-Jonas est documentée dans la note technique, non supprimée.

## Ce que G-RESPONSABILITE apporte concrètement au MRC

G-RESPONSABILITE n'est pas une théorie décorative : elle est intégrée comme une contrainte procédurale dans le registre.

Première contrainte : une obligation envers un vivant peut être inscrite avant que son porteur soit désigné ; l'absence de porteur déclenche une délibération, jamais un effacement de l'obligation.

Deuxième contrainte : aucune obligation envers une entité non-humaine ne peut être inscrite sans déclarer son seuil d'entrée dans la communauté morale (sentience ou finalité immanente) — ce qui empêche que n'importe quelle entité déclenche n'importe quelle obligation sans critère de réfutation.

Troisième contrainte : quand une dette écologique n'a pas de porteur identifiable (régime « systémique »), le registre interdit formellement de la traiter en urgence critique avant qu'une délibération ait désigné un porteur — une cascade vérifiée formellement, non une simple recommandation.

Quatrième contrainte : tout seuil (d'irréversibilité, d'attribution) doit porter la trace de la délibération qui l'a produit. Un seuil sans cette trace est traité comme un instrument non gouverné — le risque de financiarisation que la grammaire surveille en permanence sans prétendre l'éliminer.

## Le périmètre de la grammaire

G-RESPONSABILITE ne traite que les obligations liées à des irréversibilités envers des vivants. La *futurité* — la manière dont un collectif institue son rapport à l'avenir — est lue ailleurs, comme méthode à l'échelon méso : chez les auteurs qui l'ont documentée (Lamarche et al. 2021), la futurité « oriente » les dispositifs, elle n'« oblige » pas ; elle ne déclenche cette grammaire qu'à l'approche d'un horizon irréversible. Elle est distincte de G-JUSTICE (qui traite les capabilités), de G-MIMETIQUE (qui traite les dynamiques de désignation de victimes) et de G-PERFORMATIVITE (qui traite les effets des instruments de mesure), avec lesquelles elle est couplée. Confondre ces registres conduit à prescrire des dispositifs inadaptés. Ce bornage est une déclaration de périmètre, non une limitation accidentelle.

## Ce que ce cadre demande — et ne demande pas — au lecteur

Mobiliser G-RESPONSABILITE n'exige pas d'adhérer à une métaphysique du vivant ni à une doctrine particulière de la justice intergénérationnelle. Il exige de reconnaître : (1) que certaines décisions franchissent des seuils d'irréversibilité qu'aucune compensation ne rattrape ; (2) qu'une obligation peut être réelle avant que son porteur soit nommé ; (3) que toute obligation envers des absents (générations futures, non-humains) doit rester réfutable par un critère déclaré, plutôt que posée comme une évidence morale. Un chercheur en droit de l'environnement, en économie écologique ou en théorie politique peut utiliser G-RESPONSABILITE comme outil de diagnostic partiel, sans en faire la seule lentille d'analyse. La grammaire est conçue pour coexister avec les autres registres du MRC. Cet usage analytique obéit à une discipline d'inscription : ne pas importer un seuil sans déclarer son statut. Mobiliser en description une catégorie à seuil valuatif de cette grammaire — le seuil d'entrée dans la communauté morale, le seuil de puissance affirmative, l'appel immanent — exige de déclarer que le seuil est importé du modèle, non endossé par l'analyste : clause de suspension de valuation, règle R0-bis (Annexe méthodologique §A.14).

\[LACUNES ET LIMITES — texte de vulgarisation\] (1) Gosseries 2023 est vérifié sur recensions ; les pages exactes des quatre principes restent à contrôler sur exemplaire. (2) La tension entre l'individualisme de Nussbaum et le régime systémique de l'habitabilité est assumée comme structurelle et déclarée — sa clôture formelle est hors du régime procédural. (3) La question de savoir si une futurité *instituée* crée une obligation propre (et non une simple orientation) est reportée à une délibération ultérieure — horizon irréversible déclaré. (4) Ce texte ne remplace pas la note technique NT-G2 : les définitions opérationnelles restent en §2-§5.

*Fin de NT-G2*

**Rattachement aux fiches de Couche 2**

Fiche(s) consommatrice(s) : F2 (milieu), F4 (existentiel). Sources de Couche 2 hébergées par cette grammaire : Jonas (appel\_immanent, irréversibilité, responsabilité envers le vivant). Les fiches concernées remplacent leurs citations externes par un renvoi « → NT-G2 » ; aucune source externe ne subsiste dans le corps des fiches.

— Les actions de révision et le suivi des décisions sont tenus dans `MRC_v5.7/_ETAT_INSCRIPTION_v5.7.md` (source unique) et au suivi de l'Annexe méthodologique (§D). —

---

**Ancrage contre-capture (anti-irréversibilité) — Pistor 2025, ch. 3 et 7**

La finalité de la chose s'inscrit en C-FINALITE-IMMANENTE opposable dans chaque convention (clause téléologique : une prétention conforme à la lettre mais contraire à la finalité est inopposable — chez Pistor, *« the only defense »* contre l'arbitrage, ch. 5). Pour toute opération à risque irréversible : principe de précaution *« if in doubt, don't do it »* et renversement de la charge de preuve d'innocuité sur l'opérateur (ch. 7) ; dette systémique pressentie inscrite SYSTEMIQUE_NON_ATTRIBUEE et forcée vers DELIBERATION avant clôture. Opérateurs porteurs : R-INTERDIT-ABSOLU, C-FINALITE-IMMANENTE.

*Forme du renversement : PR-15.* Le renversement n'est déclaré que si un porteur de la charge est nommé (`sans_porteur_nomme_pas_de_renversement`) ; la charge n'est satisfaite que par une preuve **reconstructible**, c'est-à-dire refaisable depuis le registre par un tiers (`preuve_non_reconstructible_ne_satisfait_pas`) ; tant qu'elle ne l'est pas, elle ne retombe sur aucun acteur affecté (`charge_ne_retombe_pas_sur_les_affectes`). Ces trois énoncés sont des lectures des définitions de PR-15 (`RenversementDeclare`, `ChargeSatisfaite`, `BienFormeeInstruction`), témoignées par `PR15_discrimine`. PR-15 ne juge pas la validité de la preuve : une preuve reconstructible satisfait la charge sans être évaluée (`charge_satisfaite_et_renversement_declare_coexistent`) ; juger la preuve relève d'une instance, non du registre. `[SOURCE HORS SET]` La spécification de PR-15 vient de l'instrument D4 d'un texte cité « I.3.6 §6.5 », qui n'est pas dans le set.

*Condition de réfutation.* (i) L'homologie « précaution de Pistor ≡ heuristique de la peur (Jonas) / R-INTERDIT-ABSOLU » est une inférence de structure (asymétrie assumée des deux côtés, §6bis) ; réfutée si la précaution de Pistor admet une balance coûts/bénéfices que l'interdit jonasien exclut (alors non substituables). (ii) Une inversion de charge hors irréversibilité plausible dégénère en veto d'obstruction ; le déclencheur reste l'irréversibilité, critère délibéré.

*Source.* Pistor, K., *The Law of Capitalism and How to Transform It*, Yale University Press, 2025 (ISBN 978-0-300-28280-1) — VÉRIFIÉ (citations confirmées au mot près sur PDF ; pagination de l'édition imprimée non reportée, ancrage par chapitre).

*Réserve de second rang.* Les sources de second rang citées via Pistor (Calabresi & Melamed 1972, Galanter, Thelen & Streeck, Hesselink, Luhmann, Fox, Werbach & Cornell) restent `[SOURCE NON VÉRIFIABLE — à contrôler]` pour tout usage autonome : elles ne sont mentionnées ici que comme citées-par-Pistor.
