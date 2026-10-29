# MRC v5.7 — NT-ARCH · Architecture des Couches 0 à 3

> **Terminologie « écriture duale »** (`Note_Desambiguisation_Ecriture_Duale_2026-09-29.md`). **« Écriture duale » désigne la seule écriture miroir entre deux teneurs** (N2, formalisée par PR-35) ; l'objet de L2 est le **registre comptable augmenté** (Lean : `RegistreComptableAugmente`, `registre_augmente_{coherent, preserve_R1, non_equivalence}`, `registreAugmenteDe/Bis`, `lien_inter_acteurs_porte_par_un_registre_augmente`, `les_deux_registres_augmentes_ont_le_meme_socle`).

*Fichier unique d'architecture du Modèle de Registre de Communalité : primitives (Couche 0), régimes et invariants (Couche 1), modes d'application — fiches F1–F10 (Couche 2), système des douze grammaires transversales (Couche 3)*

Pierre Musseau-Milesi · La Coop des Communs · MRC v5.7 · Régime : vérifiabilité-cohérence

> **État d'inscription.** Le suivi des inscriptions effectuées, des décisions prises et des décisions en attente est tenu **exclusivement** dans `MRC_v5.7/_ETAT_INSCRIPTION_v5.7.md`. Ce fichier n'en porte aucune trace dans son corps.

---

## §0. Objet, périmètre et traçage des changements de base

Ce fichier porte, en un seul document, l'architecture transversale des Couches 0 et 1, l'architecture des Couches 2 et 3, les fiches de la Couche 2 et l'index du set. Il porte tout ce qui est nécessaire à l'architecture du MRC ; le cadre théorique est complété par les douze notes de grammaire (NT-G1 → NT-G12) et par l'annexe méthodologique. **Le MRC est ainsi décrit de manière exhaustive en 14 fichiers** (cf. §D.1).

**Architecture à quatre couches, alignée sur ProfReg.**

| Couche | Contenu | Localisation dans le set |
|---|---|---|
| **Couche 0** | Primitives (catégories de base déclarées et stables) | Partie A |
| **Couche 1** | Régimes d'obligation, R1 DÉBIT/CRÉDIT, statut de dette, machine d'états, invariants | Partie A |
| **Couche 2** | Modes d'application (fiches F1–F10) : instruments, champs, signaux, valorimètres | Partie B |
| **Couche 3** | Les douze grammaires transversales (NT-G1 → NT-G12) | Partie C + notes NT-G |

**Règle de circulation.** Une grammaire de Couche 3 **consomme** un invariant, ne le redéfinit pas ; une fiche de Couche 2 qui mobilise une règle de Couche 1 **renvoie** à la Partie A (renvoi posé dans un seul sens, sinon \[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ\]). Les invariants structurels ne vivent jamais en Couche 2 : ils remontent en Couche 1.

**Renvois.** Les notes de grammaire citent « NT-ARCH §n » : ces renvois pointent vers la Partie A, §n, du présent fichier.

---

# PARTIE A — Couches 0 et 1 : primitives, régimes et invariants

*(numérotation §1–§11, à laquelle renvoient les notes de grammaire)*

## §1. Objet et positionnement

NT-ARCH porte les primitives et invariants que le MRC mobilise transversalement, indépendamment de toute grammaire de Couche 3 et de tout régime comptable de Couche 2. Elle est le lieu d'inscription univoque des invariants structurels de Couche 0 et de Couche 1. Toute fiche de Couche 2 (F8 mode comptable notamment) qui mobilise C-STATUT-DETTE renvoie à NT-ARCH plutôt que de redéfinir la règle — renvoi posé dans un seul sens pour éviter \[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ\].

Principe directeur. Les transitions de la machine d'états sont des invariants structurels de Couche 1, non des conventions de Couche 2 sujettes à délibération locale.

Ancrage des sources. Conformément au périmètre de NT-ARCH, cette note ne cite aucune source académique externe : ses ancrages philosophiques et bibliographiques sont portés par les notes de grammaire et lui sont reliés par renvoi. Voir NT-G2 (Responsabilité) pour le régime d'obligation et le principe intergénérationnel ; NT-G7 (Justice) pour les capabilités et l'horizon planétaire ; NT-G1 (Évolutivité) pour la révision des règles. Les sources externes correspondantes figurent dans la section Bibliographie de ces notes.

Couches mobilisées : Couche 0 — primitives regimeobligation, fractionactorielle, collectifhybridedeclare (extensions de la primitive Interaction). Couche 1 — règle R1 (DÉBIT/CRÉDIT), invariant B1, machine d'états transition\_valide, typage InventaireNonVide. Interfaces — C-STATUT-DETTE et valorimètres (F8) ; phases INVENTAIRE-ASSETS-ACTIFS et REPRESENTATION-PROSPECTIVE (workflow).

## §2. Primitive de Couche 0 — regimeobligation (B1)

Une obligation peut être actorielle (un porteur identifié), systémique (sans porteur attribué) ou hybride. Cette distinction est une primitive, pas un attribut dérivé.

regimeobligation Énumération ACTORIEL / SYSTEMIQUE / HYBRIDE (déclaré) *constitutif* d'un côté d'écriture : son absence **refuse l'inscription** (CONV-3 ; Annexe §A.15.11, branche 1), la valeur déclarée ne pouvant être ni calculée ni supposée.
fractionactorielle Score 0-1 DÉCLARÉE — jamais calculée par ProfReg
collectifhybridedeclare Liste d'identifiants décentréalisés si SYSTEMIQUE ou HYBRIDE

Invariant de Couche 1 (B1). La valeur 1 de la fraction actorielle est la manière déclarée d'indiquer qu'une obligation est entièrement portée par un acteur identifié. Cette règle rend l'attribution visible, discutable et révisable ; elle n'est pas une attribution calculée par le système. Lorsque cette compatibilité est déclarée, la preuve formelle garantit la préservation de la symétrie de l'écriture R1 (`R1_preserved_under_CB1`, module V2Verification ; `B1_coherence_condition`, P2Synthesis, en est l'alias déclaré, de même énoncé, jamais appui seul). L'équivalence « fraction = 1 ⇔ ACTORIEL » est une hypothèse de ce théorème (`CompatibleExtension`), non sa conclusion. Portée formelle exacte : l'obligation de déclaration est portée par **CONV-1** (obligation déclarée) et `fraction_exhibe_sa_source` (qui exhibe le champ source — **éventuellement vide** : `fraction_exhibe_une_source_eventuellement_vide`, PR-27) — et le foncteur candidat de calcul est **réfuté** ( `CB3_candidate_not_oplax_monoidal`) ; l'inexistence générale d'un foncteur lax monoïdal V₁→V₃ reste une lacune déclarée (→ Annexe méthodologique §C-II.3). Condition de réfutabilité : si un foncteur de calcul non arbitraire et gouverné était exhibé, c'est la convention déclarative qui devrait être révisée. Une fraction posée sans convention\_attribution\_seuil est un instrument performatif non gouverné (cadre performatif → NT-G4). B1 lève la présupposition implicite d'un porteur toujours identifiable — `[CHANGEMENT DE BASE TRACÉ]` (fichier d'état).

Théorème d'extension : systemique\_requires\_R1\_extension — le régime SYSTEMIQUE exige l'extension R1 (C-STATUT-DETTE) ci-dessous ; il ne peut être inscrit sans elle.

## §2bis. Attribut transversal de Couche 0 — charge\_valuative

`[CHANGEMENT DE BASE TRACÉ — attribut de typage, aucune primitive nouvelle ; tracé au fichier d'état]`

Chaque primitive de Couche 0 — et, par extension déclarée, chaque champ déclencheur des grammaires de Couche 3 — porte un attribut **déclaré, jamais calculé** :

**charge\_valuative** Énumération RELATIONNELLE / SEUIL-VALUATIF (déclaré)

- **RELATIONNELLE** : les conditions d'application du descripteur s'énoncent sans prédicat évaluatif ; la valuation entre comme *référence conventionnelle déclarable* (le terme de comparaison). Usage descriptif admissible sous simple déclaration de la référence.
- **SEUIL-VALUATIF** : la valuation est une *direction de mal* posée au seuil, non décollable de l'identification. Usage descriptif admissible **seulement** sous **clause de suspension de valuation** : déclaration que le seuil est importé du modèle, non endossé, avec le statut du seuil — quadruplet de R0-bis { source ; convention de mesure ; régime d'usage normatif / descriptif-suspendu ; porteur de la déclaration }, que CONV-9 complète d'un cinquième terme, l'usage de l'agrégat (quintuplet, Annexe §A.14.1) — et le marqueur `[VALUATION SUSPENDUE]`. Le statut porte en outre un terme **facultatif**, `population_visee` (Annexe §A.14.1 ; PR-18). Règle R0-bis et critère de séparabilité : → Annexe méthodologique §A.14 ; table de typage complète : §A.14.7. Que la convention de mesure soit un terme **déclaré**, et non déduit de la doctrine du seuil, tient à **AX-6** : la doctrine du seuil ne fixe pas sa métrique (Annexe §A.15.0 ; analyse contradictoire non close, étape 2 du protocole).

Le typage s'établit par examen de la **définition d'origine** de la primitive, pas de son nom ; les cas mixtes sont marqués et traités, par prudence, comme SEUIL-VALUATIF.

**Orthogonalité déclarée.** Cet axe *descriptif/normatif* (charge d'obligation d'une catégorie) est **orthogonal** à l'axe des trois régimes d'usage (§8.1.1 : opposabilité/fiabilité d'une inscription). Les confondre — « descriptif = Usage 1 » — est un `[CHANGEMENT DE BASE NON TRACÉ]` : on peut faire un usage descriptif-suspendu en Usage 2 (registre d'enquête contrôlé).

*Condition de réfutation.* L'attribut est mal posé si une primitive SEUIL-VALUATIF, une fois son seuil suspendu, ne décrit plus rien (le descripteur disparaît avec la norme) : elle ne serait alors employable qu'en régime normatif, et l'attribut devrait recevoir une valeur d'inséparabilité. Test conduit et réussi sur cas-témoin : → Annexe §A.14.8.

## §2ter. Primitives de Couche 0 — catégories de base, orientations et changements de base

`[CHANGEMENT DE BASE TRACÉ — les sections I.2 à I.5 de l'Annexe G (« Grammaire jonasienne et registre profunctor ») sont portées au titre des primitives de Couche 0 ; décision du porteur. Aucune primitive nouvelle.]`

**Motif.** L'orientation des catégories de base conditionne la portée de théorèmes compilés — elle décide de ce qu'un carré de commutativité établit. La règle de tri (Annexe méthodologique §A.9) l'assigne à la Couche 0 : c'est une primitive, non une méthode.

### §2ter.1 R1 sous forme profunctor et carré de commutation

Pour tout (x, y) ∈ Xᵒᵖ × Y, si M\_met(x,y) ≠ 0, il existe F\_y : V\_met → V\_att telle que

 M_att(x,y) ≥ F_y( M_met(x,y) )

où F\_y encode `vulnerabiliteconstitutive` et `finaliteimmanente` de l'entité y, **et ≥ est l'ordre de V\_att** (Annexe G §I.2).

Le carré correspondant — M\_met inscrit les DÉBITS, M\_att les CRÉDITS, F\_y encode l'exigence de soin — **commute par excès** : le chemin M\_att doit dominer le chemin F\_y ∘ M\_met. Trois conditions de validité :

1. **Totalité** — si M\_met(x,y) ≠ 0 alors M\_att(x,y) doit être défini : pas de DÉBIT sans CRÉDIT correspondant.
2. **Suffisance** — M\_att(x,y) ≥ F\_y(M\_met(x,y)) : le soin fourni est au moins égal à l'exigence encodée par la vulnérabilité de y.
3. **Non-saturation** — si F\_y(M\_met(x,y)) = ⊤, l'exigence n'est pas satisfaisable : le carré ne peut être fermé, l'inscription du DÉBIT est bloquée → **R-INTERDIT-ABSOLU**.

 Cette forme est **homologue** à la forme éthique — chez Jonas, la responsabilité est « une fonction du pouvoir et du savoir » (*Le Principe responsabilité*, 1979, trad. fr. p. 171), la menace a priorité sur la promesse (p. 54-55), et l'enjeu « ne doit jamais être l'intégralité des intérêts des autres concernés » (p. 60) — et, pour les traits T1 et T2 seulement, à la forme comptable (dette écologique inscrite et couverte par des contributions de restauration). Voir **AX-11** (Annexe §A.15.0 ; traits T1-T3). La forme profunctor est celle qui permet la traçabilité formelle ; elle ne fonde pas l'homologie. *La forme est dite homologue, non isomorphe : un isomorphisme supposerait un foncteur qu'aucun texte ne produit ; et la « responsabilité proportionnelle » n'est pas dans Jonas, qui écarte une « relation simple ».*

### §2ter.2 Asymétrie de F\_y — la logique jonasienne des seuils

Une logique comptable ordinaire poserait F\_y proportionnelle. La logique jonasienne impose une **asymétrie croissante** *(l'asymétrie et l'interdit sont dans Jonas, p. 54-55 et 60-61 ; la **croissance** monotone de α est une transposition déclarée du MRC)* : plus l'entité se dégrade, plus le soin requis pour un même prélèvement augmente, jusqu'à l'irréversibilité. Avec h(y,t) = `etathabitabilitemilieu` (F2) :

 F_y(v) = f_min(v) si h(y,t) > h_critique
 = f_min(v) · α(h(y,t)), α > 1 si h_irréversible < h(y,t) ≤ h_critique
 = ⊤ si h(y,t) ≤ h_irréversible

Trois régimes : **normal** (`risqueexistentiel = ABSENT`, R1 satisfaisable par des CRÉDITS ordinaires) ; **précaution** (POTENTIEL ou IMMINENT, CRÉDITS croissants, `principeprecautionasymetrique = VRAI`) ; **interdit** (IRREVERSIBLE, `irreversibilitejonasienne = VRAI`, aucun CRÉDIT réaliste → R-INTERDIT-ABSOLU, blocage de l'inscription).

La mesure d'asymétrie locale Δ(x,y) = écart( M\_att(x,y), F\_y(M\_met(x,y)) ) gouverne les déclenchements de C-SIGNAL (F4) : Δ > θ sur n ≥ 2 cycles → R-CARE chronique ; `irreversibilitejonasienne` + Δ > 0 → RISQUEEXISTENTIELIMMINENT ; F\_y(M\_met) = ⊤ → INTERDITSATURATION.

### §2ter.3 Orientation de la tour des catégories de base

**C-CATEGORIE-BASE** (Couche 0) pose que l'acte de décider quelles métriques comptent est un acte politique traçable. Son corollaire : **l'orientation** de chaque catégorie de base l'est aussi.

| Catégorie | Support | Produit monoïdal | Ordre (sens des flèches) | Fondement |
| :-- | :-- | :-- | :-- | :-- |
| V₀ | Bool | && (unité `true`) | `≤` — `false` → `true` | convention usuelle, ici déclarée |
| V₁ = V\_met | [0,1] | min (unité 1) | **`≤`** | **contraint**, voir ci-dessous |
| V₂ = V\_att | ℝ≥0∞ (porte ⊤) | *voir lacune §2ter.5* | **`≥`** — convention de coût | **Annexe G §I.2, déclaré** |

**L'orientation de V₁ n'est pas un choix, c'est une conséquence.** Le changement de base CB₂ : V₁ → V₂, f ↦ −log f, envoie 1 sur 0 et 0 sur ⊤ : il **renverse l'ordre**. Il n'est un foncteur que si source et cible portent des orientations opposées. V\_att étant orienté en `≥`, V₁ est orienté en `≤`. La contrainte est confirmée indépendamment par CB₁ (`false` ↦ 0, `true` ↦ 1), qui exige `0 → 1` dans V₁.

La convention de coût est donc bien celle du MRC : elle vit sur V\_att, et −log la transporte en son inverse sur V\_met. Ce n'est pas une contradiction mais la contravariance du changement de base — ce qui manquait était **la trace du renversement**.

*Condition de réfutation.* L'identification V\_att ↔ V₂ et V\_met ↔ V₁ repose sur la mention « métrique Lawvere » de l'Annexe G §III.2 et sur la présence de ⊤ des deux côtés ; elle n'est écrite comme telle nulle part. Si un document du corpus établissait une autre correspondance, la conclusion sur V₁ tomberait et §2ter.4 serait à reprendre.

### §2ter.4 Portée exacte de CB₃

Sous l'orientation `≤` de V₁, la condition de lax monoïdalité du candidat φ(f) = f vers (ℝ, ×, 1) s'écrit `a·b ≤ min(a,b)` : elle est **vraie** pour tout a, b ∈ [0,1]. Le candidat identité **est** lax monoïdal.

Le théorème compilé `CB3_candidate_not_oplax_monoidal` réfute l'inégalité inverse, `min(a,b) ≤ a·b`, qui est la condition **oplax**, et rien de plus.

**Conséquence sur l'invariant B1\_coherence\_condition (§2).** L'obligation de déclarer `fractionactorielle` n'en est pas affaiblie : elle repose sur la **convention CONV-1** — *aucun foncteur de calcul de la fraction actorielle n'est mobilisable dans ProfReg* — appuyée par l'invariant de typage **`fraction_exhibe_sa_source`**, et sur la **lacune déclarée** portant sur l'inexistence générale d'un foncteur de calcul V₁→V₃ — non sur la réfutation d'un candidat. La condition de réfutabilité est celle de §2 : l'exhibition d'un foncteur de calcul non arbitraire et gouverné obligerait à réviser la convention déclarative, non à retirer un théorème.

### §2ter.5 Lacune ouverte — produit monoïdal de V₂

L'Annexe G §III.2 déclare la catégorie de base comme **métrique de Lawvere**, dont le produit monoïdal est l'**addition** (unité 0). Or CB₂ = −log transporte `min` en `max` : `−log(min(a,b)) = max(−log a, −log b)`. Le produit induit sur V₂ par le changement de base est donc **max** — structure ultramétrique — et non l'addition.

`[INCOHÉRENCE INTER-COUCHES — niveau 0]` : la structure monoïdale de V₂ est déclarée en Annexe G et **induite différemment** par le changement de base codé. Trois issues possibles, non tranchées : CB₂ n'est pas le bon changement de base ; V₂ n'est pas une métrique de Lawvere mais une ultramétrique ; ou V₂ porte deux structures selon l'usage, ce qui devrait être déclaré. Le choix conditionne ce qui peut être prouvé sur l'**agrégation** des dettes — `max` et `+` n'agrègent pas de la même façon — et donc le verrou de commutativité micro-macro (nœud D).

> **(i) Aucun théorème compilé ne dépend du choix.** `ChangeOfBase.lean` ne porte sur CB₂ que `CB2_one` et `CB2_zero` : trancher `max` / `+` n'engage aucune recompilation. Le fait lui-même — CB₂ transporte `min` en `max` — **n'est pas compilé** : c'est un calcul à la main, exact. Le compiler passerait par les réels et ferait croître le nombre de théorèmes dépendant de `Classical.choice` (§8), ce qui serait à déclarer. **(ii) PR-19 agrège par somme** (`agreger`, sur des coûts entiers, non sur V₂). Son résultat — une série d'écritures toutes triviales sous le seuil peut produire un agrégat non conforme (`serie_bien_formee_agregat_non_conforme`) — **n'existe que sous `+`** : sous `max`, le fractionnement ne fait pas échapper au seuil. Si l'agrégation des dettes de V₂ devait un jour rejoindre celle de PR-19, le choix de v6 en fixerait la portée. `[PLAUSIBLE — PR-19 ne porte pas sur V₂]` **(iii) Piste non instruite** : la troisième issue (« deux structures selon l'usage ») pourrait s'adosser au cinquième terme de CONV-9, qui déclare ce que l'agrégat sert à établir. `[PLAUSIBLE, NON VÉRIFIÉ]`

> ### Motifs déclarés pour l'arbitrage `max` / `+`
>
> L'arbitrage `max` / `+` porte sur trois issues. Deux motifs de contenu sont déclarés ici, **comme motifs déclarés et non comme décision**, et ils ne vont pas dans le même sens.
>
> **(a) Un motif normatif en faveur de `max`, importé.** La littérature mobilisée par le n° 74 d'*Interventions économiques* — soutenabilité forte, non-substituabilité des capitaux, « conditionner l'accumulation et les profits à la préservation du vivant » (Bodet, Lamarche & Richez-Battesti), robustesse face au dépassement des limites (Hamant 2024) — argue uniformément pour la **non-compensation**. Or `max` est la structure non compensatoire et `+` la structure compensatoire : une dette maximale ne se compense pas par un excédent ailleurs, une somme si.
>
> `[LIMITE DE CE MOTIF, STRICTE]` **Ce n'est pas un argument mathématique et il ne tranche rien.** Laisser une thèse écologique décider d'une structure algébrique serait un `[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ]`. Le motif est versé pour que l'arbitrage v6 ne se prenne pas *par commodité*, faute d'avoir une raison écrite. `[PLAUSIBLE, NON VÉRIFIÉ — inférence versée, non résultat.]`
>
> **(b) Une contrainte retirée du côté de `+`, et c'est le résultat le plus utile.** La transposition de la règle des **avaries communes** (axiome **AX-3**, Demonsant, Levillain, Hatchuel & Segrestin 2026) repose, dans sa forme maritime, sur un **prorata** — taux = coût des pertes / somme des richesses à sauver. **Un prorata présuppose `+`** : il faut un total à diviser, donc une agrégation compensatoire. Si le set devait porter la règle sous cette forme, `max` deviendrait algébriquement indisponible.
>
> **Or la transposition retenue par le porteur écarte explicitement le prorata** — *« ni les richesses, ni les capacités de contribuer, ni les vulnérabilités ne se laissent réduire à une valeur monétaire unique »* (`Application des avaries communes à TZCLD`) — et lui substitue une obligation de **déclaration publique et révisable** de position. **La contrainte qui imposerait `+` est donc levée par cette transposition, arrêtée pour d'autres motifs.**
>
> `[CE QUE CELA N'ÉTABLIT PAS]` Renoncer au prorata **n'établit pas `max`** : cela retire une raison de retenir `+`, et rien de plus. Une répartition sans formule ne choisit aucune structure monoïdale — elle n'en mobilise aucune. **Deux motifs déclarés ne font pas un arbitrage** ; le §2ter.5 reste ouvert et la décision reste de porteur, horizon v6. Instruction : `Decision_P9_Verrou_Macro_x_Avaries_Communes_2026-09-14.md`.

## §3. Sous-couche d'interface — C-STATUT-DETTE (V2)

C-STATUT-DETTE qualifie l'état d'attribution d'une obligation. Sa définition vit en NT-ARCH (invariant) ; son implémentation comptable (mouvements DÉBIT/CRÉDIT) vit en F8, qui renvoie ici.

C-STATUT-DETTE Énumération
ATTRIBUEE porteur identifié (ACTORIEL)
SYSTEMIQUE\_NON\_ATTRIBUEE sans porteur, en attente (SYSTEMIQUE/HYBRIDE)
EN\_DELIBERATION phase d'attribution en cours

La règle R1 (DÉBIT/CRÉDIT, symétrie interne) reste l'invariant comptable de référence. C-STATUT-DETTE en est l'extension pour les obligations sans porteur immédiat : une dette systémique est inscriptible (CRÉDIT) sans débiteur attribué, sous réserve d'entrer dans la machine d'états ci-dessous.

### §3bis. Règle R1 — formulation constitutive, typage et asymétries autorisées

**R1 — symétrie DÉBIT / CRÉDIT (règle *constitutive comptable*, non métaphore épistémique).** R1 est l'invariant littéral : toute écriture a une écriture miroir, **Côté A (DÉBIT) ↔ Côté B (CRÉDIT)**, sous l'équation du bilan `A = D + S' + ΔS` (seize mouvements régime-invariants → NT-G12). R1 reste la règle constitutive ; elle est *qualifiée, non remplacée*, par le typage **P-C-E-D-e-d** (Couche 2, F8 sous-couche T) : chaque côté est typé `P` Patrimoine / `C` Créance / `E` Engagement / `D` Dette / `e` effort fourni / `d` résultat (composites admis). `D` est l'inverse de `C` par symétrie ; le champ `respect_R1` vérifie que le couple (typage, miroir) appartient à la table des compatibilités.

**Deux asymétries autorisées — et seulement deux :**

- *Dette systémique* : une dette est inscriptible côté CRÉDIT sans débiteur attribué côté DÉBIT → statut `SYSTEMIQUE_NON_ATTRIBUEE`, forcé vers DELIBERATION (machine d'états, §4).
- *Engagement existentiel `E+`* : un engagement envers un acteur non tracé (générations futures, biosphère, nappe fossile) inscrit `E` sans miroir comptable → `asymetrie_existentielle = VRAI`, objet de R-INTERDIT-ABSOLU (→ NT-G2).

Toute autre écriture sans miroir typé est une **violation** de R1, non une asymétrie gouvernée.

> **Condition de réfutation du « seulement deux ».** La liste des asymétries autorisées reste **close** et **garde le refus** : toute autre écriture sans miroir typé est une violation, y compris une asymétrie candidate **pendant son instruction** (RSO-8 : le non-déclaré refuse). Le « seulement deux » est **éprouvé** — le don (§8.5.2bis), la consommation sans bénéficiaire (§8.5.2ter) — et **non démontré**. *Il tombe si* un candidat, instruit par le porteur sur le patron de l'instruction du don, est **admis** comme troisième asymétrie : un miroir **légitimement** absent, qu'aucune ligne de la table ni aucune lacune (arbitrage A8, distinct de l'axiome AX-8) n'explique. *Porteur :* porteur MRC / architecte. *Horizon :* institutionnel. *Critère :* chaque candidat instruit est versé, admis ou rejeté avec ses motifs. `[DISTINCTION DÉCLARÉE — la table §8.5.2, liste close elle aussi, ne refuse pas un couple absent : elle le met en attente (arbitrage A8, distinct de l'axiome AX-8). Audit_Postulats §3.3.]`

> Le **don**, sur le cas des AMEP, est un candidat à une **troisième asymétrie**, instruit et **rejeté** : il se type sans asymétrie par deux branches déjà présentes dans la table §8.5.2 — `e ↔ d` et `e ↔ D−` —, l'électricité partagée étant un **flux** de signe `neutre` et non un patrimoine. **L'instruction relève en revanche deux lacunes de la table de Couche 2**, qui ne sont pas des asymétries puisque le miroir y existe et que seule manque la ligne qui l'apparie : une **arité à trois livres** non déclarée, et **l'impossibilité de typer le don d'un poste**. → **§8.5.2bis** (F8). *Le « seulement deux » de la présente section est ainsi une affirmation éprouvée, non démontrée.* Instruction : `Decision_P6_Don_Troisieme_Asymetrie_2026-09-14.md`.

**Exigence de réfutabilité (distincte de R1 — *par analogie déclarée*).** Indépendamment de la symétrie comptable, le régime de vérifiabilité-cohérence exige que tout engagement fort (« X implique Y », « il est établi que… », recommandation, obligation) déclare sa condition de réfutation et la position adverse documentée — c'est la section « conditions de réfutation » de chaque grammaire. Faute de quoi : \[ENGAGEMENT SANS SYMÉTRIE — contre-partie manquante\]. **Ne pas assimiler cette symétrie épistémique à la symétrie comptable R1** : les confondre est un \[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ\].

## §4. Machine d'états transition\_valide (V4) — quatre invariants de Couche 1

NONATTRIBUEE → DELIBERATION ✅ unique transition autorisée (nonattribuee\_force\_deliberation)
NONATTRIBUEE → CRITIQUE ❌ contradiction formelle interdite (cascade\_deliberation\_before\_critique)
EN\_DELIBERATION → ATTRIBUEE ✅ condition pour libérer CRITIQUE (critique\_released\_by\_porteur)
ATTRIBUEE → CRITIQUE ✅ seule voie d'accès au niveau CRITIQUE

> `[CHANGEMENT DE BASE TRACÉ]` **Correspondance avec le code.** Les quatre flèches ci-dessus mêlent statuts et niveaux. Le modèle Lean (`Primitives.lean`) n'a pas quatre états : `transition_valide : StatutDette → NiveauRIA → Prop` croise **3 statuts** (`nonAttribuee`, `enDeliberation`, `attribuee`) × **2 niveaux** (`deliberation`, `critique`), soit **6 cas**, et dit quel niveau est accessible depuis quel statut. Les flèches 1, 2 et 4 sont des cas de `transition_valide`. La flèche 3 (EN_DELIBERATION → ATTRIBUEE) est la **seule transition entre statuts** : elle n'existe que dans `transitionV4c` (V4c, résolution **procédurale**) ; `critique_released_by_porteur` la prend en **hypothèse**, il ne la prouve pas.

> Cette machine n'a **aucun état terminal, et n'en reçoit pas**. Elle gouverne la **trajectoire d'attribution** ; l'extinction de l'obligation relève d'un **second axe**, versé en **§4bis** et typé à quatre lemmes. Le second axe laisse intactes les quatre transitions et leurs théorèmes compilés.

Conséquence procédurale. Une dette systémique non attribuée ne peut jamais déclencher directement un niveau CRITIQUE : elle est forcée vers la délibération, qui doit produire un porteur (ATTRIBUEE) avant que la criticité soit mobilisable. Cela interdit l'usage d'une urgence existentielle pour court-circuiter l'attribution de responsabilité. Articulation avec NT-G2 : en régime SYSTEMIQUE, R-INTERDIT-ABSOLU déclenche DELIBERATION (non CRITIQUE) en l'absence de porteur identifié.

## §4bis. L'extinction de l'obligation — un second axe, à quatre lemmes (décision du porteur)

`[DÉCISION DU PORTEUR — formule : **« l'obligation s'éteint ; la trace demeure »**. Logique d'inscription : le tétralemme (NT-G5 Bloc C).]`

### §4bis.1 Ce que la décision tranche, et ce qu'elle refuse de trancher

La machine d'états de §4 sait ouvrir une obligation, la faire délibérer, l'attribuer et la rendre critique ; elle ne sait pas la refermer. Deux lectures s'offrent — lacune, ou choix d'un registre où rien ne s'éteint.

> **Les deux lectures ne portent pas sur le même objet, et c'est ce que la décision établit.** La position « rien ne s'éteint » défend **la mémoire** ; la position « il faut une sortie » défend **la comptabilité**. Elles ne sont contradictoires que si l'on confond l'obligation et sa trace.
>
> ### **L'obligation s'éteint ; la trace demeure.**

**Ce que la Couche 2 porte de cette distinction.** La table §8.5.2 refuse l'extinction **gratuite** d'une dette — `D− ↔ d` est la seule cellule ABSENTE de §8.5.5, et le refus est motivé — et admet l'extinction **payée**, `D− ↔ C− + e`, qui exige un effort effectif. **La Couche 2 distingue donc effacer et solder ; le second axe donne à la Couche 1 l'état qui enregistre l'extinction.**

### §4bis.2 L'extinction n'est pas un cinquième état de §4

**La machine d'états de §4 ne porte pas l'extinction.** Ses quatre flèches *(dans le code : 3 statuts × 2 niveaux, une seule transition entre statuts — note de §4)* et les théorèmes compilés qui les portent — `transition_valide`, `nonattribuee_force_deliberation`, `cascade_deliberation_before_critique`, `critique_released_by_porteur` — **en sont indépendants**.

**Raison d'architecture, et elle n'est pas de prudence seulement.** §4 gouverne **la trajectoire d'attribution** : qui répond de l'obligation, et à quelle condition la criticité devient mobilisable. L'extinction est d'un autre ordre : elle dit **si ce qui est dû l'est encore**. Ce sont deux questions indépendantes — une obligation attribuée peut être éteinte, une obligation non attribuée peut l'être aussi (remise, prescription, disparition de l'objet). **Les fondre dans un graphe unique aurait fait dépendre l'extinction de l'attribution**, ce qui aurait donné à tout débiteur non attribué une obligation inextinguible.

`[GARDE FORMELLE — qu'une énumération à quatre lemmes ne casse aucun théorème compilé de ProfReg doit être établi avant implémentation. Le second axe ne touche ni `transition_valide` ni les théorèmes de V4 et de PR-3 (vérifié par recompilation). **Il touche PR-11** : `seule_la_realisation_eteint` établit que seule la réalisation vérifiée éteint, dans un modèle qui ignore la remise et la prescription. **Résolution** : NC (Annexe §A.15.6) est bornée à l'extinction **par exécution** ; « jamais par transfert » vaut pour tout mode (PR-11 : `obligation_non_cessible`, lecture ; témoin : `PR11_ne_verifie_pas_la_realisation`) ; remise, prescription et disparition de l'objet relèvent du présent axe. **Ses conditions de bonne formation sont formalisées par PR-26** (`PR26_ExtinctionSecondAxe.lean`) : le silence ne solde rien (`le_silence_ne_solde_rien`, lecture ; témoins : `seul_debiteur_bien_forme_mais_marque`, `deux_regimes_divergents_ne_suffisent_pas`) ; la lecture paresseuse du quart lemme est refusée (dépendance 4 → 3 : `deux_regimes_divergents_ne_suffisent_pas` ; un lemme 3 attesté lève le refus : `le_tiers_atteste_leve_le_refus`) ; l'axe est orthogonal à l'attribution (`l_extinction_ne_depend_pas_de_l_attribution`) ; le seul débiteur est marqué, non sanctionné ; une extinction bien formée peut être une remise (`une_extinction_bien_formee_peut_etre_une_remise`) ; une dette AX-2 ne s'inscrit jamais en `ETEINTE`. **Ce que PR-26 ne formalise pas reste procédural** : la trace (§4bis.5), la qualité des interprètes, le statut « homologue mondain » des lemmes 3 et 4. **Mode procédural, non formel calculable.**]`

### §4bis.3 Le champ `etat_extinction` — quatre lemmes et un hors-tétralemme

L'ordre des lemmes est celui de Yamauchi, porté par NT-G5 Bloc C : affirmation, négation, **binégation**, **biaffirmation**.

> `[CONTRÔLÉ SUR SOURCE PRIMAIRE — `Controle_Yamauchi_x_Audit_Tetralemme_2026-09-21.md`.]` L'ordre ne se justifie pas par la formule de Berque — *« la biaffirmation en dernier parce qu'elle ouvre à tous les possibles »* : **l'ouvrage dit autre chose, et dans l'autre sens** : *« mon intention étant de placer la position de la binégation **au centre de toute la logique**. Si la position de la biaffirmation est possible … c'est parce qu'elle est **précédée par la logique de la binégation, faute de laquelle le point de vue de la biaffirmation ne peut s'établir**. » `[VERBATIM — SOURCE PRIMAIRE]` **Ce n'est pas le quatrième lemme qui est le terme culminant : c'est le troisième qui est le centre, et la condition du quatrième.**
>
> **Dépendance qui en résulte, et qui est une condition de bonne formation.** Une inscription en `ETEINTE_ET_NON_ETEINTE` **n'est bien formée que si l'indécidabilité a d'abord été attestée** : soit par une inscription antérieure en `INDECIDABLE_ATTESTE` sur la même obligation, soit par la déclaration, dans l'écriture même, que l'extinction n'est pas décidable sous un régime unique. **Elle interdit la lecture paresseuse du quart lemme** — *deux régimes divergent, donc lemme 4* — en exigeant qu'on ait d'abord montré que la question **ne se décide pas sous un régime unique**.

| Valeur | Lemme | Ce qu'elle atteste | Exigence d'écriture |
| :-- | :-: | :-- | :-- |
| `ETEINTE` | **1** | ce qui était dû ne l'est plus | **l'écriture d'extinction**, appariée en §8.5.2 — typiquement `D− ↔ C− + e` — **et** `interprete_extinction` renseigné |
| `NON_ETEINTE` | **2** | ce qui était dû l'est encore | `interprete_extinction` renseigné |
| `INDECIDABLE_ATTESTE` | **3** | **l'interprète atteste que l'extinction n'est pas décidable en l'état** | `interprete_extinction` **et** un **critère de résolution déclaré** — à quelle condition cela cesserait d'être indécidable ; sans critère, mal formée (PR-26 : `tiers_lemme_sans_critere_mal_forme`) |
| `ETEINTE_ET_NON_ETEINTE` | **4** | **deux prises contraires sur la même obligation** | **deux prises déclarées**, chacune avec son `interprete_extinction` **et son régime** (couche R) |
| `NONDECLARE` | *hors tétralemme* | rien n'a été écrit sur l'extinction | **refuse, n'autorise pas** (**RSO-8**, Annexe §A.16.5) |

> **`NONDECLARE` n'est pas le tiers lemme, et les confondre serait ici la faute la plus coûteuse du set.** `NONDECLARE` est un état du **registre** — on n'a rien écrit ; la binégation est un état de la **relation** — l'extinction n'est pas décidable, l'interprète le dit, et il dit à quelle condition cela cesserait. **Par défaut, une obligation n'est pas éteinte** : le silence ne solde rien. La position « rien ne s'éteint » est donc le régime par défaut du registre, non le seul régime possible.

**Ternarité transposée.** NT-G5 pose que la relation s'écrit `r = S/P pour I`. Ici : **S** est l'obligation, **P** le prédicat d'extinction, **I** l'interprète qui constate. Une inscription d'extinction n'est bien formée que si les trois termes sont renseignés. Le défaut produit **un marqueur nommé, jamais une sanction** (patron R0-bis) : `[EXTINCTION SANS INTERPRÈTE]`.

> ### **Une dette de régime AX-2 ne s'inscrit jamais en `ETEINTE`.**
>
> **Règle.** Une obligation de régime **AX-2** — héritée, renouvelée à chaque cycle, sans créancier apte à donner quittance (fiche AX-2 ; PR-12 `Regime.A2`) — ne peut prendre que les valeurs `NON_ETEINTE`, `INDECIDABLE_ATTESTE`, `ETEINTE_ET_NON_ETEINTE` ou `NONDECLARE`. **Une inscription `ETEINTE` sur une dette AX-2 est mal formée** et lève `[CONFUSION DES DEUX DETTES]` (patron calculé de PR-12) : elle traiterait comme soldable ce qu'AX-2 pose comme non soldable.
>
> **Le quart lemme est le régime ordinaire d'AX-2.** C'est le cas de §4bis.4 : la part soldable s'éteint au régime comptable (le fournisseur est payé), la dette envers le milieu ne s'éteint pas au régime CARE. Deux prises, deux régimes, sous la dépendance 4 → 3. **AX-2 trouve ici une écriture, et non un simple refus.**
>
> *Appui de terrain* : dans l'entre-subsistance, « il importe ici d'être quitte » entre personnes en interconnaissance (Pruvost, *La Subsistance au quotidien*, 2024, p. 443) ; envers le milieu, AX-2 pose qu'on ne peut pas l'être. *Formalisation* : **PR-26 `une_dette_A2_ne_s_eteint_jamais` et `le_quart_lemme_est_le_regime_de_A2`**. *Réfutation* : la règle tombe si l'on exhibe une obligation de régime AX-2 dont un créancier apte à donner quittance est identifiable — elle relèverait alors d'AX-3, non d'AX-2.

> ### `[EXTINCTION DÉCLARÉE PAR LE SEUL DÉBITEUR — décision du porteur.]`
>
> **Règle.** Une extinction `ETEINTE` d'une obligation `ATTRIBUEE` dont `interprete_extinction` est **le seul débiteur**, **et dont les concernés relevant du seuil déclaré (§7bis) ne tiennent pas eux-mêmes l'écriture miroir** — aucun créancier tracé n'inscrivant son `C−` —, est **bien formée**, mais porte `[EXTINCTION DÉCLARÉE PAR LE SEUL DÉBITEUR]` : marqueur, jamais sanction (R0-bis). **Toute prise contraire d'un concerné relevant de ce seuil fait passer l'inscription au lemme 4** (`ETEINTE_ET_NON_ETEINTE`), sous la dépendance 4 → 3.
>
> **Ce qu'elle règle.** La **clôture de complaisance** — un débiteur soldant au nom de concernés qui n'ont rien constaté — devient **visible par forme**. Sans elle, §4bis la laisserait passer : l'interprète y est obligatoire, non sa qualité.
>
> **Rattachements.** *§7bis* : ACT-ARCH-001 impose un seuil de concernés déclaré à toute obligation `ATTRIBUEE` ; **le coût de la règle — déclarer les concernés — est donc déjà acquitté** pour elles. Il reste entier pour les obligations `SYSTEMIQUE_NON_ATTRIBUEE`, auxquelles la règle ne s'applique pas. *AX-7* (seuil arrêté par les concernés) fournit un **appui doctrinal, non une garantie**, et il est en tension déclarée avec RSO-6. **AX-7 — posé ; constat documenté.** Axiome de référence : `Fiche_Axiome_A7_Seuil_Arrete_Par_Les_Concernes_2026-09-11` (Annexe méthodologique §A.15.0). Le dossier de preuve correspondant est constitué : *emplacement* — `ProfReg/Fiche_Axiome_A7_Seuil_Arrete_Par_Les_Concernes_2026-09-11.md`, épreuve `ProfReg/Examen_A7_Charte_Roubaix_2026-09-28.md` ; *pièces* — dossiers `TZCLD/` et `RADIS/` (charte du Comité citoyen de Roubaix) ; *porteur* — P. Musseau ; *mise à jour* — conditions de péremption et de réfutation de la fiche (Annexe §A.15.0). AX-7 demeure un axiome d'architecture : ce dossier ne vaut pas preuve Lean de l'axiome.
>
> **Effet sur les théorèmes compilés.** La règle porte sur le second axe, hors programme de preuve ; elle **lit** §7bis sans le modifier ; les quatre flèches de §4 *(3 statuts × 2 niveaux dans le code — note de §4)* n'en dépendent pas. **Aucun effet** sur V4 (`transition_valide`) ni sur PR-3 (recompilés ; état d'audit : §8) ; la garde de non-régression `la_machine_d_attribution_ignore_l_extinction` (PR-26, R-5) échouerait si une révision couplait les deux axes.
>
> **Ce que PR-26 formalise de la présente règle, et ce qu'il ne formalise pas.** Formalisés : le marqueur (`marqueurSeulDebiteur`, `seul_debiteur_bien_forme_mais_marque`) et sa levée quand les concernés tiennent le miroir (`le_miroir_des_concernes_leve_le_marqueur`). **Non formalisée** : *« toute prise contraire d'un concerné relevant de ce seuil fait passer l'inscription au lemme 4 »* — PR-26 n'a pas de notion de **prise d'un concerné** (une prise y porte un interprète et un régime, non la qualité de celui qui la tient). La règle reste **procédurale**. *Motif* : sa condition de réfutation (ci-dessous) n'a encore aucun cas typé — les six extinctions RATP ne le sont pas ; formaliser une règle dont on ne sait pas si elle est une lourdeur serait prématuré. *À rouvrir* : quand un cas d'extinction portant le marqueur sera typé en C-STATUT-DETTE.
>
> *Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* une extinction inscrite avec ce marqueur sur un cas documenté, ou la démonstration qu'aucune n'en relève. *Condition de réfutation* : la règle est une lourdeur si, sur corpus, la majorité des extinctions portent le marqueur **sans qu'aucun concerné n'ait matière à les contester**. `[À VÉRIFIER — les six extinctions RATP (J1-ter) ne sont pas typées en C-STATUT-DETTE ; la règle ne s'y appliquerait qu'une fois ce typage fait, et le créancier y tient son miroir.]`

`[TRANSPOSITION DÉCLARÉE, NON IDENTITÉ — chez Berque, les quatre prises sont *ressources, contraintes, risques, agréments*. Le quart lemme d'extinction ne les reprend pas : il décline les **régimes** de la couche R. La structure est empruntée, le contenu ne l'est pas, et l'emprunt est déclaré.]`

### §4bis.4 Ce que les deux lemmes centraux règlent, et qu'aucun booléen ne réglait

**Le tiers lemme règle l'engagement existentiel — mieux qu'une exclusion.** **Exclure `E+ ↔ ∅` de l'accès à l'état terminal**, au motif qu'un engagement envers un acteur non tracé n'a personne pour en constater le solde, n'est pas nécessaire : un tel engagement se type `INDECIDABLE_ATTESTE`, avec son interprète et son critère de résolution déclaré. La différence n'est pas de forme. **Exclure dirait « cette obligation ne peut pas s'éteindre » ; le tiers lemme dit « on ne peut pas en décider, et voici à quelle condition on le pourrait »** — le premier énoncé est une propriété prêtée à la chose, le second un état de l'enquête, réfutable et daté.

**Le quart lemme est le régime ordinaire d'une obligation à deux régimes.** Une dette peut être **éteinte au sens du régime comptable et non éteinte au sens du régime CARE** : le fournisseur est payé, la dette envers le milieu que la chose incorpore ne l'est pas. Ce n'est pas une contradiction à tolérer, c'est ce que le set tient déjà sous un autre nom — **la règle de §8.4bis : « une chose, deux régimes de qualification, deux porteurs »** (`une_chose_deux_natures`). **Le quart lemme en est la forme temporelle** : une chose, deux régimes, **deux dates d'extinction**.

> **Et la source fournit mieux qu'un argument d'ordre : elle fournit le cas.** Yamauchi, exposant Nāgārjuna : *« **Ce n'est que si l'on prouve qu'il n'y a ni naissance ni disparition qu'il peut y avoir et naissance et disparition.** »* `[VERBATIM — SOURCE PRIMAIRE]` **L'application du tétralemme à l'extinction n'est donc pas un emprunt lointain : c'est le locus classique du corpus dont le concept est tiré**, et la phrase est mot pour mot la structure de §4bis appliquée à son objet.

 **Les valeurs 3 et 4 sont des homologues mondains des lemmes 3 et 4 de Yamauchi, non ces lemmes eux-mêmes.** La valeur 3 inscrit une **indécidabilité relative attestée, à critère de résolution** — la négation relative (*paryudāsa-pratiṣedha*) de la source, *« la cruche n'est pas dans la maison »* : elle n'y est pas maintenant, on ira en acheter une (p. 97-98) —, non la négation absolue (*prasajya-pratiṣedha*) qui fait le tiers lemme. La valeur 4 inscrit une **pluralité de rapports déclarée**, que la logique mondaine admet : affirmation et négation ne se contredisent pas si elles ne s'établissent *« ni en même temps, ni dans le même rapport »* (p. 280). Le MRC reprend de Yamauchi **la division exhaustive** (p. 71), **l'ordre** et **la dépendance 4 → 3**, comme convention d'écriture propre. **Il ne prétend inscrire ni la négation absolue ni la biaffirmation du *soku*** : elles forment *« la vérité du Sens Vainqueur »* et *« ne relève[nt] pas du logos »* (p. 88-89) — et un registre est un dispositif du logos. **Inscrire la biaffirmation du *soku* est inopérable — ce n'est pas une préférence** : aucun registre ne distingue une biaffirmation sous rapport unique d'une écriture contradictoire. *Fondement :* lecture intégrale du chapitre III (`Controle_Yamauchi_Chap3_x_Arbitrage_7_2026-09-26.md`). « La source maintient la clause d'Aristote » est inexact : la phrase qui le suggère est la **présentation du traducteur** ; chez Yamauchi, la clause **définit** la logique du logos / mondaine (p. 42-43, 280-281), que le lemme transcende (*« dans le lemme, [la contradiction] est non seulement admise, on en fait même ce qu'il y a de plus pertinent »*, p. 85). *Réfutation :* la décision tombe si l'on exhibe un passage où Yamauchi soumet sa propre binégation ou biaffirmation à l'unicité de rapport. *Conséquence sur les conditions de réfutation de §4bis.7 (ii)* : **ni la valeur 3 ni la valeur 4 ne prouvent une logique non bivalente** ; remplies, elles prouvent que l'indécidabilité ou la pluralité de rapports est **déclarée et tracée au lieu d'être lissée** — c'est leur fonction, et elle suffit.

### §4bis.5 La trace — et pourquoi elle n'est pas soumise au tétralemme

> **Le tétralemme porte sur l'obligation, jamais sur sa trace.** Une trace qui serait *« à la fois inscrite et non inscrite »* ne serait pas une trace ; une trace *« ni inscrite ni non inscrite »* non plus. **La trace est binaire et à sens unique** : une fois écrite, elle demeure.

**L'écriture qui éteint est elle-même inscrite.** Elle porte son écriture miroir, son interprète, sa date, et — pour le lemme 3 — son critère de résolution, ou — pour le lemme 4 — ses deux prises. **Rien n'est effacé ; quelque chose est soldé.**

#### Table de champs de `C-MEMOIRE-PERTES` — proposition

Le compartiment, invoqué dans tout le set, reçoit ici sa table de champs **à titre de proposition** : c'est le coût déclaré de la décision d'extinction (§4bis).

| Champ | Type | Description |
| :-- | :-- | :-- |
| `objet_memorise` | Référence | L'obligation, la perte ou l'écriture d'extinction dont la trace est conservée |
| `nature_trace` | Énumération | PERTE\_DOCUMENTEE / DETTE\_HERITEE\_QUALITATIVE / **EXTINCTION\_CONSTATEE** / **DEPART\_DE\_PORTEURS** — la troisième valeur relève de la décision d'extinction (§4bis). La quatrième trace le départ de personnes qui portaient un travail, ou une parole sur ce travail, que personne d'autre dans le collectif ne porte ; `objet_memorise` désigne le métier ou le travail concerné (C-GENRE-METIER, F1) ; `interprete_constat` est un membre ou une instance du collectif restant, puisque les partants ne sont plus là pour déclarer. Elle est lue par `denidutravailreelpresume` (F1) : hypothèse à examiner, jamais qualification *(décision du porteur, 12/10/2026)*. `[LACUNE]` Le critère qui distingue ce départ d'un roulement ordinaire (répétition dans un même métier, motif lié au travail) reste à instruire ; porteur : responsable Couche 2 NT-G9 ; horizon : épreuve de la table sur un cas |
| `interprete_constat` | DID ou collectif désigné | Qui a constaté. **Obligatoire** — même exigence que `interprete_extinction` |
| `date_constat` | Date | — |
| `source_constat` | Référence | Source déclarée et vérifiable au sens des quatre propriétés de §B.2 |
| `alterable` | **Constante FAUX** | **Une trace ne se modifie pas.** Elle peut être complétée par une trace ultérieure qui la cite, jamais réécrite |

`[À VALIDER — cette table est proposée au titre de la décision d'extinction et n'est éprouvée sur aucun cas. `R-INCAPACITE-LLM-VALIDER` s'applique.]`

### §4bis.6 Ce que l'extinction rend possible

| Objet | Sans second axe | Ce que l'extinction à quatre lemmes lui rend |
| :-- | :-- | :-- |
| **Lot S6 — interruption** | bloqué : *« interrompre suppose une sortie »* | la sortie existe ; une interruption peut déclarer sa condition de levée sans être une clôture déguisée |
| **Suspension (S4)** | une suspension sans fin | la reprise se constate par un retour du lemme 3 ou 2 vers 1 ou 2 |
| **Attestation périodique (A5)** | atteste une obligation qui ne se referme pas | l'attestation porte sur une trajectoire qui peut aboutir |
| **Horizons déclarés** | échéances sans effet inscriptible | l'échéance passe, un état peut changer |
| **`resultat_distribuable`, `taux_couverture_DNH`** | trajectoire d'extinction que rien ne constate | le constat existe, et il est typé |

### §4bis.7 Portée, réserves, conditions de réfutation

`[EXTENSION DE PORTÉE DÉCLARÉE, NON TACITE]` NT-G5 (Bloc C) borne expressément le tétralemme à G-MESOLOGIE : *« neuf autres grammaires portent des prédicats booléens sur des relations ; l'extension n'est ni proposée ni écartée — elle n'est pas instruite »*, avec la consigne **« ne pas élargir tacitement »**. **Le second axe est une extension, et il porte plus loin que ce que la réserve envisage** : il applique la logique non à une autre grammaire de Couche 3, mais à un objet de **Couche 1**. Il est donc **déclaré et borné à l'extinction** : `[CHANGEMENT DE BASE TRACÉ]`. **Aucune autre énumération booléenne du set n'est convertie.**

 `[SOURCE LUE — *Logos et lemme* est déposé en biblio. Contrôle : `Controle_Yamauchi_x_Audit_Tetralemme_2026-09-21.md`.]` **L'ordre des lemmes est confirmé au verbatim** ; **l'argument « ne mène à rien » ne figure pas dans l'ouvrage** (l'énoncé de la source est en §4bis.3) ; **la primauté revient au tiers lemme, non au quart** ; « syllemme » **compte zéro occurrence** et n'est pas un concept de Yamauchi. **Une réserve demeure** : **« lemme » désigne chez Yamauchi un mode d'appréhension intuitif** — *« une chose regardée directement »*, *« nullement une inférence du logos »* — et non une valeur d'énumération : **ce que le registre inscrit n'est pas un lemme, c'est le lemme *invoqué par un interprète***, ce qui est la raison de fond de l'obligation faite à `interprete_extinction`.

**Conditions de réfutation.** *(i)* Le second axe tombe si l'on exhibe une obligation dont l'état d'extinction **ne peut pas être déterminé indépendamment de son état d'attribution** : les deux axes n'en feraient qu'un, et §4 devrait être étendu plutôt que doublé. *(ii)* Le typage à quatre lemmes tombe si, à corpus clos, **les valeurs 3 et 4 restent vides** : le booléen suffirait — même condition qu'en NT-G5 Bloc C. *(iii)* La formule tombe si l'on exhibe une obligation dont l'extinction, même attestée et inscrite, **retire effectivement quelque chose à la mémoire du registre** : il existerait alors des obligations dont la permanence *est* la substance et non la trace, et la distinction serait fausse. *Ces obligations ont un nom dans le set : ce sont celles d'**AX-2**. La condition (iii) vise donc AX-2, et la règle « une dette AX-2 ne s'inscrit jamais en `ETEINTE` » (§4bis.3) en est la conséquence : la distinction obligation / trace tient pour AX-2 parce que l'obligation AX-2 ne s'éteint pas.*

*Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* une obligation portée à `ETEINTE` par une écriture appariée en §8.5.2, avec interprète nommé, dont la trace est inscrite en `C-MEMOIRE-PERTES` et **demeure lisible après extinction** ; et au moins une obligation en `ETEINTE_ET_NON_ETEINTE` sur deux régimes déclarés.

## §5. Phases de workflow rattachées (B2, B3)

### §5.1 INVENTAIRE-ASSETS-ACTIFS — typage InventaireNonVide (B2)

Déclenchement : regimeobligation = SYSTEMIQUE/HYBRIDE, OU MILIEUDEGRADEPERSISTANT (renvoi NT-G5), OU APPELIMMANENTNONENTENDU (renvoi NT-G2). Contenu obligatoire : liste des identifiants décentralisés (DID) des entités mobilisées + rôle, état de mobilisation, valorimètre + convention d'attribution, seuilentreecommunautemorale pour chaque entité non-humaine.

seuilentreecommunautemorale ∈ { SENTIENCE / FINALITEIMMANENTE / NONDECLARE }. Ancrage de source et justification philosophique : → NT-G7 §2 (capabilités, Bloc A) et NT-G2 §3.

InventaireNonVide = { l : List DID // l ≠ \[\] }

Clôture interdite avec liste vide (inventaire\_nonempty\_required, *lecture du type : la contrainte est dans le sous-type, le théorème la projette ; sa non-vacuité est témoignée par `inventaire_nonempty_discrimine` — le type est habité, et la liste vide en est exclue*). Contrainte de Couche 1.

> `[DÉCISION DU PORTEUR — `INDECIDABLE_ATTESTE` ne déclenche pas la phase d'inventaire]` Le troisième déclencheur, `APPELIMMANENTNONENTENDU`, est le signal F4 de §4.3 : il se lève **exactement** sur `appel_entendu_milieu ∈ {NON_ENTENDU, ENTENDU_ET_NON_ENTENDU}`. **Sur `INDECIDABLE_ATTESTE`, il ne se lève pas, et l'inventaire n'est pas déclenché par cette voie** — ni sur `ENTENDU`, ni sur `NONDECLARE`. La phase ENQUÊTE que §4.3 ouvre sur `INDECIDABLE_ATTESTE`, avec son critère de résolution, est l'action générale de C-ENQUETE-V5 ; `INVENTAIRE-ASSETS-ACTIFS` n'en est qu'une phase, et **ouvrir l'enquête n'implique pas l'inventaire**.
>
> **Pourquoi.** *(i)* Déclencher sur l'indécidabilité attestée ce que déclenche la non-entente rabattrait le lemme 3 sur le lemme 2 — exactement le codage de l'indécidabilité en négation que NT-G5 retire (« ce que le lemme 3 retire »). *(ii)* **La prudence est assurée par une autre porte** : `MILIEUDEGRADEPERSISTANT`, calculé sur l'état mesuré, déclenche l'inventaire **sans aucun déclarant** (PR-4, `le_milieu_declenche_sans_qu_aucun_acteur_ait_declare`) ; si le milieu est dégradé, l'inventaire est dû quel que soit l'état de l'appel. *(iii)* Le patron de prudence de PR-10 (`mixte` traité comme `seuil-valuatif`) ne se transpose pas : il porte sur une **ambiguïté de typage**, non sur une **valeur attestée** avec interprète et critère.
>
> **Appui compilé.** PR-4 porte le signal comme projection booléenne déclarée, **`false` sur `INDECIDABLE_ATTESTE`** : la présente décision en est le fondement textuel.
>
> *Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* aucune phase `INVENTAIRE-ASSETS-ACTIFS` n'est ouverte sur le seul motif d'un `INDECIDABLE_ATTESTE`. *Condition de réfutation :* la décision tombe si un cas documenté montre une indécidabilité attestée **dont la résolution a échoué faute d'inventaire**, alors que le milieu n'était pas mesuré `MILIEU_DEGRADE_PERSISTANT` et que le régime d'obligation était actoriel — c'est-à-dire alors qu'aucune des deux autres portes n'était ouverte.

### §5.2 REPRESENTATION-PROSPECTIVE (B3)

Déclenchement : horizontemporelresponsabilite = INTERGENERATIONNEL ET porteurs incluant des générations non encore nées.

legitimiterepresentant ∈ { PRATIQUE (défaut) / DELIBERATIVE / JURIDIQUE / planetaireNonDesignee }
conditionrefutation Texte — OBLIGATOIRE si legitimiterepresentant = PRATIQUE ou planetaireNonDesignee

Champs : représentant prospectif (DID institutionnel), principeintergenerationnel appliqué (cf. §6), horizon de mandat. Ancrage de source : → NT-G2 §7 (principeintergenerationnel, légitimité représentative) et NT-G7 §4.4 (horizon planétaire). \[ENGAGEMENT À HORIZON IRRÉVERSIBLE\] maintenu — délibération nécessaire avant conclusion.

Cas HorizonTemporel.planetaire (AM-ARCH-01). Lorsque HorizonTemporel = PLANETAIRE et que le porteur est structurellement absent, legitimiterepresentant prend la valeur planetaireNonDesignee et conditionrefutation devient OBLIGATOIRE — invariant de Couche 1, non bonne pratique. Le fondement académique (absence de structures délibératives globales) est porté par NT-G7 §4.4 et sa bibliographie.

**Conventions d'architecture applicables au cas planétaire.** Lorsque `HorizonTemporel = PLANETAIRE` et qu'aucun porteur ne peut être structurellement identifié, le MRC applique `CONV-6`, qui exige l'inscription d'une représentation prospective, et `CONV-7`, qui exige une condition de réfutation explicite. Ces conventions rendent traçable et contestable l'opération de représentation ; elles ne sont pas présentées comme des théorèmes ProfReg.

## §6. Principe intergénérationnel — taxinomie de référence (A4)

\[CHANGEMENT DE BASE TRACÉ\] principeintergenerationnel prend ses valeurs dans la taxinomie à quatre principes : NON-DECLINE / BETTER-FUTURE / SUFFICIENCY / NARROW-PATH. L'ancrage de source, l'état de vérification de chaque principe et la résolution du \[CHANGEMENT DE BASE TRACÉ\] de la valeur SUFFICIENCY (usage capabilité NT-G7 vs usage gouvernance NT-ARCH) sont portés par NT-G2 §7 et son protocole de vérification ; le suivi de cette vérification figure au fichier d'avancement.

principeintergenerationnel ∈ { NON-DECLINE / BETTER-FUTURE / SUFFICIENCY / NARROW-PATH / NON\_DECLARE }

## §7. Couplages et invariants inter-couches

**Ce que les couplages présupposent (AX-5).** L'axiome **AX-5** (non-fermeture des chaînes, Annexe §A.15.0) pose que l'atteinte, son inscription, l'obligation, les ressources, l'action et sa vérification demeurent disjointes tant qu'un montage spécifique ne les relie pas. Les couplages ci-dessous sont de tels montages : aucun n'est supposé se faire de lui-même. Leur condition de réfutation est celle d'AX-5 (§9).

Couche 0 ↔ Couche 1. regimeobligation (C0) est lié à C-STATUT-DETTE (C1) par B1\_coherence\_condition (alias déclaré de `R1_preserved_under_CB1`, §2). L'invariant tient dans les deux sens : ACTORIEL impose fractionactorielle = 1 et un statut potentiellement ATTRIBUEE ; SYSTEMIQUE impose l'extension R1 et un statut initial SYSTEMIQUE\_NON\_ATTRIBUEE.

**§7bis. Invariant ACT-ARCH-001 (`attribuee_seuil_declare_required`).** La combinaison `C-STATUT-DETTE = ATTRIBUEE` avec `seuilentreecommunautemorale = NONDECLARE` est **interdite** : elle constitue un **invariant de Couche 1** (non une bonne pratique). *Énoncé.* Toute dette dont le statut passe à ATTRIBUEE **doit** porter un `seuilentreecommunautemorale ≠ NONDECLARE` au moment de l'attribution (attribuer une responsabilité à un porteur suppose que le seuil d'entrée dans la communauté morale soit déclaré ; l'attribuer « dans le vide » du seuil serait un `[ENGAGEMENT SANS SYMÉTRIE]`). *Cohérence.* Aligné sur B1 (déclaration comme invariant) et homologue de CONV-1 et `fraction_exhibe_sa_source`. *Contrepartie réfutable (Couche 1).* L'invariant est **révisable** vers un repli « re-déclaration à échéance » (plutôt qu'« à l'attribution ») **si** le cas « seuil matériellement non déterminable à l'instant de l'attribution » se révèle empiriquement **récurrent** (position adverse conservée). *Statut de preuve.* **PR-3 est compilé et audité** : `ProfReg/PR3_AttributionSeuil.lean`. *État d'audit PR-3.* Sur l'instantané audité du 2 octobre 2026, `PR3_AttributionSeuil.lean` contient 15 théorèmes, dont 12 sans axiome, 0 `sorryAx`. *Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable.

**§7bis-a. L'invariant est paramétré par l'échéance de déclaration.**

La contrepartie réfutable ci-dessus pose une alternative — « à l'attribution » ou « à échéance ». **L'invariant n'est pas écrit dans l'un des deux régimes, il est écrit paramétré par l'échéance de déclaration**, et le régime strict énoncé au §7bis en est démontré comme l'instance où l'échéance vaut l'instant de l'attribution — l'identité est établie **dans les deux sens** (`stricte_est_instance_du_repli`, `repli_a_l_instant_d_attribution_est_strict`).

*Ce que cela permet.* La révision vers le repli est une **opération** : changer de régime, c'est déplacer un paramètre, non réécrire le set. Et le constat empirique de récurrence auquel cette révision est conditionnée **n'est pas préempté** — c'est la raison même de ce paramétrage.

*L'échéance nommée est obligatoire, et c'est un théorème.* `repli_sans_echeance_degenere` exhibe une dette ATTRIBUEE, portant un seuil, dont le seuil n'a **jamais** été déclaré, et qui satisfait pourtant l'invariant sous échéance non nommée. Un repli sans date est donc `NONDECLARE` sous un autre nom, avec en prime une obligation devenue opposable. **Une échéance non nommée n'est pas un régime admissible.**

*Conséquence de la machine d'états, démontrée.* `seuil_non_declare_bloque_critique` établit qu'un seuil non déclaré interdit l'attribution (§7bis) et que l'attribution est la seule porte de CRITIQUE (§4) — **donc contester le seuil protège de l'attribution.** Cet enchaînement n'est écrit comme règle nulle part ; il est une conséquence de deux règles du set. C'est ce que le repli à échéance désamorce, en permettant d'attribuer pendant que le seuil se discute.

*Composition avec PR-10.* Le §A.14.7 de l'Annexe type `seuilentreecommunautemorale` comme **`seuil-valuatif`** ; R0-bis lui est donc applicable. Attribuer une obligation exige par conséquent non seulement un seuil déclaré (§7bis) mais son **quadruplet complet** — source, convention de mesure, régime d'usage, porteur de la déclaration (`attribution_exige_seuil_et_quadruplet`) ; le cinquième terme, l'usage de l'agrégat, relève de CONV-9. Cette exigence est plus forte que celle qu'énonce le §7bis seul : elle naît de la composition de deux règles actées séparément.

*Ce que PR-3 ne tranche pas.* `PR3_ne_departage_pas_les_seuils` — la règle exige qu'un seuil soit déclaré, elle ne départage ni SENTIENCE ni FINALITEIMMANENTE. `PR3_ne_choisit_pas_le_regime` — elle instrumente le choix du régime temporel, elle ne le fait pas. *Porteur :* porteur MRC. *Horizon :* révisable, conditionné au constat empirique de récurrence du §7bis. Voir `Decision_PR3_2026-09-07.md` et `Rapport_PR3_2026-09-07.md`.

**§7ter. Invariant `obligationpreservation_derivable`.** L'`obligationpreservation` (F2, niveau entreprise / CARE) est posée comme devant être **dérivable des normes territoriales** (`milieuuri` multi-parties) — **homologue macro de CONV-1 et de `fraction_exhibe_sa_source`**. *Énoncé* **.** Une obligation de préservation déclarée au niveau d'une entité (CARE) doit pouvoir être **rattachée** (dérivée, non postulée) à **une norme de l'un des milieux dans lesquels l'entité trajecte — plusieurs milieux pouvant coexister au sein du même environnement sans s'emboîter** (`milieuuri`, multi-parties). **Le rattachement déclare lequel, et ne présuppose aucune instance supérieure.** À défaut de tout rattachement, elle est déclarée `[NON DÉRIVÉE — à rattacher]`.

> **Le rattachement ne suppose pas une tour de périmètres emboîtés** (relevé des emplacements qui la supposent : `Post-Croissance/Amendements…_2026-09-18.md` §7).
>
> **Lire « milieu » comme un contenant géographique imposerait la tour.** Chez Berque, le milieu n'est pas un contenant, et la coexistence non emboîtée de milieux distincts au sein d'un même environnement est une thèse centrale :
>
> > « chaque espèce habite son propre milieu […]. **Ces milieux divers n'en coexistent pas moins au sein du même environnement.** » — Berque, « Qu'est-ce que l'espace de l'habiter ? », in *Habiter, le propre de l'humain*, La Découverte, 2007, p. 63 `[VERBATIM VÉRIFIÉ sur PDF joint]`
>
> Et sur l'échelle :
>
> > « **Échelle** — À la différence de la proportion géométrique, qui est abstraite, **rapport de taille concret entre les êtres et les choses, relevant de la ternarité** : la carte à l'échelle du 1 : 25 000 n'est pas le territoire, parce qu'on peut vivre sur le territoire (S), mais pas sur la carte (P). » — Berque, glossaire, 2018 `[VERBATIM VÉRIFIÉ — source secondaire]`
>
> **L'échelle est trajective, non topologique** : ce n'est pas un niveau d'une tour, c'est un rapport S/P pour un I. Deux échelles d'un même objet ne s'emboîtent donc pas — elles **se recouvrent**, chacune avec son interprète. *La mésologie fournit ainsi ce que l'invariant doit pouvoir écrire.* Le champ `milieuuri` est **multi-parties** : une formule au singulier d'appartenance ou de contenance (« dont elle relève ») imposerait la tour.
>
> **Portée, bornée.** Cette lecture vaut **pour ce seul emplacement**. Les quatre autres emplacements supposant la tour — `00_Cadre_chantier_carte_verrous.md` §2, `03_Verrou_commutativite_micro-macro.md` §3 voie 1, `05_Couche_normative_DeSchutter.md` §3, note consolidée §7.2 — **conservent leur marquage**, et leur relevé mécanique reste dû `[OBLIGATION OUVERTE]`.
>
> **Ce que ce § ne décide pas.** Rien sur la structure d'agrégation (`max`, `+`, deux structures, aucune), qui reste ouverte et relève de l'algèbre (§2ter.5). Le garde-fou de §2ter.5 s'applique mot pour mot : **aucune thèse d'organisation, et aucune onto-logique, ne décide d'une structure algébrique.** `[DÉCOUPLAGE DE RÉGIMES ÉVITÉ — déclaré.]`
>
> *Critère de vérification :* le relevé mécanique retire ce § de sa liste, **et** au moins un cas documenté exhibe deux milieux se recouvrant sans s'emboîter pour une même entité.
> `[CONDITION DE RÉFUTATION]` Si, sur les corpus du MRC, tout périmètre d'écriture pertinent se révèle inclus dans un périmètre supérieur unique, l'emboîtement est un fait du matériau et **c'est la présente lecture qui est fautive**.
> `[RÉSERVE DE SOURCE]` Baschet n'est pas lu ici ; sa position est reprise telle que la note d'amendements du 18 septembre la rapporte `[patron W-1d]`. La convergence Berque / Baschet est une **inférence de cohérence déclarée**, non une thèse attribuée à l'un ou à l'autre. *Statut de preuve.* La **preuve formelle** (PR analogue à PR-5, commutativité micro-macro CARE→CENP, nœud D du chantier macro — hors set, horizon v6 (cf. `MRC_v5.7_ProfReg_Consolide.md` §4)) est **hors Mathlib actuel, horizon v6.x** : `[PLAUSIBLE, NON VÉRIFIÉ]`, non bloquant pour v5.7. La forme atteignable en v5.7 est la **gouvernance calculable de la non-clôture** : déclaration obligatoire du rattachement (ou de son absence). *Couplage.* À lire avec la **voie 3 (double comptabilité déclarée)** du verrou 03 (Annexe méthodologique §A.6) : les deux dettes CARE/CENP restent distinctes, leur non-équivalence est déclarée, `[DÉCOUPLAGE DE RÉGIMES]` assumé. *Porteur :* porteur MRC / architecte. *Horizon :* institutionnel (invariant) ; preuve intergénérationnelle/v6.x.

NT-ARCH ↔ NT-G2 (Responsabilité). G-RESPONSABILITE consomme regimeobligation et la machine d'états (cascade R-INTERDIT-ABSOLU). *La commutativité B1↔B2 est **procédurale**, déclarée comme telle — **CONV-2 étendue** (Annexe §A.15.9), jamais une dispense d'inventaire : `V3_commutatif` est vrai par construction (les deux branches systémiques de `chemin_direct` rendent `deliberation`, comme `chemin_via_inventaire` : forme 1, patron V10b / B-5) ; il n'est qu'une **lecture** des deux définitions. Le contenu calculable est porté par `V3_aboutit_deliberation` (en régime systémique, on aboutit à la délibération) et `V3_actoriel_inchange`, lectures à témoins croisés. **La commutation sur les chemins admissibles est démontrée par PR-51** (`PR51_CarreB1B2.lean`), la règle des pas entre phases étant déclarée : le chemin direct n'est pas admissible dès que l'inventaire est requis (`le_chemin_direct_n_est_pas_admissible`) ; aucun chemin admissible n'atteint la délibération sans inventaire (`aucune_deliberation_sans_inventaire`) ; deux chemins admissibles qui l'atteignent passent tous deux par l'inventaire, sur une écriture qui porte un inventaire non vide (`carre_B1B2_commute_sur_les_chemins_admissibles`) ; témoins : `carre_temoin_discriminant`, `le_carre_a_un_chemin_admissible`.*

NT-ARCH ↔ NT-G7 (Justice). seuilentreecommunautemorale (renseigné en phase INVENTAIRE) conditionne R-HABITABILITE-CAPABILITE ; commutativité F4↔F6 **caractérisée sous cohérence déclarée** (`V1_commute_ssi_coherence` ; `V1_commutatif` en est une lecture) . Extension AM-ARCH-01 : cas HorizonTemporel.planetaire (→ §5.2). Le « mur d'individualisme » à respecter (capabilité individuelle vs habitabilité systémique, tension T5, \[DÉCOUPLAGE DE RÉGIMES\] assumé) est documenté et instrumenté en NT-G7 §2, avec ses sources.

NT-ARCH ↔ F8 (mode comptable). C-STATUT-DETTE défini ici, implémenté en F8 ; source\_valuemetre OBLIGATOIRE en F8 — **source déclarée et vérifiable, dont le DID est une forme possible et non la forme obligatoire** (CONV-4) — par analogie à CONV-1 / `fraction_exhibe_sa_source` (B3). Renvoi unidirectionnel F8 → NT-ARCH.

## §8. Statut des vérifications formelles

**État d'audit ProfReg.** Sur l'instantané audité du 13 octobre 2026, ProfReg contient 604 théorèmes, aucun `sorryAx`, 10 usages de `Classical.choice` et aucun `axiom` déclaré (`lake build` du porteur ; journal : `~/Developer/ProfReg/audit/audit_2026-10-13_PR59.log`). Le décompte en vigueur est celui du Consolidé §1 ; il est régénérable par `lake env lean Audit.lean`. `ProfReg/Sonde_PCEDed.lean` (aucun `Classical.choice`) est construit et audité. **Ces théorèmes portent sur un texte — §8.5 — et non sur l'architecture ; aucun n'établit une thèse du MRC**, et l'avertissement d'antériorité en tête du fichier borne ce qu'on peut en citer. Chaque recompilation prime sur la précédente, conformément à la règle du point de décompte ci-dessous. Théorèmes rattachés à NT-ARCH : R1\_preserved\_under\_CB1 (et son alias déclaré B1\_coherence\_condition), systemique\_requires\_R1\_extension, nonattribuee\_force\_deliberation, cascade\_deliberation\_before\_critique, critique\_released\_by\_porteur, inventaire\_nonempty\_required, V1\_commutatif. ACT-G2-010 (préservation ACTORIEL par V4c) — RÉSOLU PROCÉDURAL. Les lacunes résiduelles et points ouverts (2-cellule : F3 §3.5) sont suivis en Annexe méthodologique (§C, §D), hors corps de cette partie.

**Conventions d'architecture rattachées.** *Une convention est opposable et non démontrable (Annexe §A.15). Elle n'est pas comptée parmi les théorèmes ProfReg ; les ancrages compilés cités en établissent la forme, jamais la justesse. Énoncés canoniques : Annexe §A.15.1.*

| Conv. | Énoncé (condensé de l'Annexe §A.15.1) | Mobilisée en | Ancrage ProfReg (forme, non preuve) |
| :-- | :-- | :-- | :-- |
| **CONV-1** | La fraction actorielle est déclarée, jamais calculée : aucun foncteur de calcul n'est mobilisable dans ProfReg | §2, §2ter.4, §7, §7bis, §7ter, §9, §B.2 | **Fraction actorielle.** L'exigence de déclaration relève de `CONV-1`. ProfReg démontre que toute fraction actorielle construite dans le type porte un champ source (`fraction_exhibe_sa_source`) ; ce champ peut être vide (`fraction_exhibe_une_source_eventuellement_vide`) |
| **CONV-2** | La commutativité du carré triangulaire NT-G7 ↔ NT-G2 ↔ NT-ARCH, et celle du carré B1↔B2, sont procédurales ; jamais une dispense d'inventaire | §7, §B.2 | **Triangle V10b.** La compatibilité du triangle relève de `CONV-2`. Elle n'est pas comptée parmi les théorèmes ProfReg en vigueur. `V3_commutatif` n'en est qu'une lecture (forme 1). **Carré B1↔B2** : PR-51 — `carre_B1B2_commute_sur_les_chemins_admissibles`, `aucune_deliberation_sans_inventaire` (sur les chemins admissibles ; jamais une dispense d'inventaire) ; lectures `le_chemin_direct_n_est_pas_admissible`, `entrer_en_deliberation_exige_l_inventaire` ; témoins `carre_temoin_discriminant`, `le_carre_a_un_chemin_admissible` |
| **CONV-3** | Le régime d'obligation est un champ obligatoire : aucun côté d'écriture n'est inscriptible sans `regimeobligation` déclaré | §2 | Structure `Cote` (`LotL2_PR2_PR14.lean`) — typage, non théorème |
| **CONV-4** | Le valorimètre déclare sa source : tout valorimètre ou seuil de F8 porte `source_valuemetre`, source déclarée et vérifiable (désignation, résolution, intégrité, porteur nommé) ; le DID en est une forme possible, non la forme obligatoire | §7 (NT-ARCH ↔ F8) | PR-28 : `source_sans_porteur_mal_formee` (la clause du porteur mord), `CONV4_satisfaite_sans_DID` (satisfiabilité), `CONV4_ne_prescrit_aucune_forme` (garde). Codes de l'effet du défaut proposés, E1 / E4 (Annexe §A.15.15) |
| **CONV-5** | Dans le périmètre où PR-10 opère, « déclencher une règle R-\* » vaut « régime d'usage normatif », et réciproquement : une mobilisation sous `[VALUATION SUSPENDUE]` ne déclenche aucune règle R-\* (convention de traduction, Annexe §A.15.2) | §2bis | PR-10 : `suspension_ne_declenche_aucune_regle` (lecture : `DeclencheRegle` est défini comme le régime d'usage normatif, ce qui encode la convention ; témoin : `PR10_suspension_temoin_mal_forme`). Code de l'effet du défaut proposé, E6 ; une seconde lecture donnerait E7 — point le plus exposé du classement (Annexe §A.15.15). `[DÉCOUPLAGE DE RÉGIMES — risque déclaré]` : si le set définit le déclenchement autrement, le théorème change de sens sans cesser d'être vrai (Annexe §A.15.2) |
| **CONV-6** | La représentation prospective est exigée de toute écriture qui engage au-delà de l'exercice | §5.2 | PR-28 : `BienFormee_ne_borne_pas_la_prospective`, `CONV6_est_satisfiable` ; garde de portée `CONV6_ne_vaut_pas_dans_l_exercice` (lecture ; témoin : `BienFormee_ne_borne_pas_la_prospective`) |
| **CONV-7** | Une condition de réfutation obligatoire et absente produit un marqueur, non un refus ; le marqueur porte un horizon | §5.2, §8.4ter | PR-32 : `regime_sans_refutation_n_autorise_aucune_ecriture`, `candidat_ssi_critere_de_sortie_et_caducite` ; borne : `PR8_ne_suffit_pas` (PR-16) — une condition de réfutation inscrite n'est pas pour autant exerçable (L3) |
| **CONV-8** | Un seuil `NONDECLARE` appelle la délibération ; cela se déclare, l'exhaustivité du type ne l'établit pas | §8 | PR-28 : `nondeclare_force_deliberation` (moitié positive ; témoins : `CONV8_temoin_discriminant`) ; PR-17 : `nonDeclare_ne_vaut_pas_permission` (moitié négative, établie sur le régime du dispositif : patron) ; patron `V10a_planetaire_force_deliberation` |
| **CONV-9** | Toute mobilisation `seuil-valuatif` déclare au cinquième terme ce que l'agrégat sert à établir ; « non déclaré » ne vaut pas déclaration | §2ter.5, §8quater, §8.4ter, §8.5, §8.5.6.2 | `BienFormee_ne_borne_pas_le_quintuplet` (le trou) ; patron repris par `le_non_declare_ne_qualifie_pas_et_marque` |
| **CONV-10** | Dans le registre comptable augmenté L2, `plein` signifie que le registre reconnaît le lien, jamais qu'il le valorise | §8septies | `accord_sur_l_existence_pas_sur_la_valeur` (PR-20) |
| **CONV-11** | Une écriture `e` dont l'apporteur figure comme créancier n'est bien formée que si le mouvement de maintien est inscrit de façon structurée et si le registre qui le porte est nommé | §8octies, §8.5, §8.5.3, §8.5.3bis | PR-23 (motive et borne) ; PR-37 (registre d'un milieu) |
| **CONV-12** | Une obligation à deux niveaux déclare le niveau de chacune ; la non-équivalence est calculée, non déclarée | §8octies | — (patron cité) |
| **CONV-13** | Toute écriture d'obligation déclare à l'inscription le successeur ; « non déclaré » vaut régime strict | §8octies-bis | — (patron cité) |
| **CONV-14** | L'échelle de communalité ne s'agrège pas : axes déclarés séparément, aucun score composite | §8.5.6.2bis | PR-28 : `la_comparaison_sur_un_axe_n_est_pas_le_classement` |
| **CONV-15** | Co-obligation F4 : déclarer l'appel immanent oblige à déclarer la puissance affirmative, et réciproquement ; une paire incohérente s'inscrit avec marqueur | §8 | — |
| **CONV-16** | Le tiers d'une écriture duale est l'instance de contrôle commune, désignée par les deux registres, ni A ni B | §8.5 | PR-43 : `seule_l_instance_commune_tranche`, `l_instance_commune_tranche_toujours`, `sans_instance_commune_rien_n_est_arbitre`, `l_instance_liee_n_arbitre_pas`, `la_designation_doit_etre_commune_et_arretee`, `l_instance_ne_peut_etre_partie`, `l_instance_de_controle_peut_constater` ; témoin : `instance_commune_temoin_discriminant` |
| **CONV-17** | Seul un constat attesté selon le protocole (sept rubriques) est porté au nom du registre devant un tiers extérieur ; à défaut, la saisine est inscrite `[SAISINE HORS PROTOCOLE]` ; nul n'est empêché de signaler en son nom | §8.5 | PR-45 : `conv17_sans_protocole_hors_protocole`, `conv17_n_interdit_pas_de_signaler`, `conv17_avec_protocole_retrouve_PR44`, `chaque_rubrique_compte`, `la_reconstitution_suppose_un_detenteur_tiers`, `la_sous_declaration_est_chiffree` ; témoins : `conforme_temoin_discriminant`, `confronter_temoin_discriminant` |
| **CONV-18** | Tout engagement porté à un registre de chaîne est annoté — site, objet (parmi les objets déclarés du registre), lien déclaré ; l'instance commune (CONV-16) vérifie la destination et qualifie le lien, le lien retenu primant sur le lien déclaré ; à défaut d'annotation `[DESTINATION NON DÉCLARÉE]`, à défaut de qualification `[LIEN NON QUALIFIÉ PAR L'INSTANCE]` | §8.5 | PR-47 : `sans_site_destination_non_declaree`, `le_lien_retenu_prime`, `l_instance_requalifie_le_lien`, `un_verificateur_non_designe_ne_vaut_pas`, `destination_infirmee_et_objet_hors_registre` ; témoin : `etat18_temoin_discriminant` |
| **CONV-19** | Le signal de souffrance est un indice explicatif, jamais l'appui d'une créance : il n'entre dans aucune qualification de créance et ne déclenche aucune règle qui conférerait un droit (règle de non-confusion de NT-G9 §4.2) | §B.3 F1 (C-GENRE-METIER) | PR-52 : `la_souffrance_seule_ne_qualifie_aucune_creance` (lecture : `QualifieCreance` encode la convention ; témoin : `la_souffrance_n_empeche_pas_la_qualification`). Code de l'effet du défaut proposé, E6 (Annexe §A.15.16) |
| **CONV-20** | Une qualification du régime affectif n'est inscriptible qu'avec une source déclarée (clinique externe, dialogue professionnel ou archivage des actes), le consentement collectif et un statut de protection (anonymisé, pseudonymisé ou agrégé seul) ; sur support distribué, seul NONCOLLECTE est admis — NONCOLLECTE désignant l'absence de toute qualification inscrite, aucune qualification n'y est inscrite | §B.3 F1 (C-GENRE-METIER) | PR-52 : `sans_source_rien_n_est_legitime`, `noncollecte_n_est_jamais_legitime` (lectures), `la_source_ne_suffit_pas`, `sur_support_distribue_rien_n_est_inscriptible` ; témoin : `inscriptible_temoin_discriminant`. Effet du défaut : E1, branche 1bis du critère (Annexe §A.15.11, §A.15.17) |

**Quatre classes de nœuds.** Le set distingue : les **axiomes** ( **AX-1 à AX-17** — table canonique Annexe §A.15.0, constats sur le monde, avec fiche et gabarit contradictoire) ; les **conventions** ( **CONV-1 à CONV-20** — table canonique Annexe §A.15.1, obligations déclarées portant sur des inscriptions ; la table ci-dessus les porte toutes) ; les **théorèmes** (ProfReg, conditions de bonne formation démontrées) ; et les **règles de second ordre — RSO-1 à RSO-8** (Annexe **§A.16**), qui ne portent ni sur le monde ni sur la forme d'une inscription mais sur **ce que les procédures du modèle confèrent**. *Une convention oblige une inscription ; une RSO confère un statut à un acte du modèle.* La première d'entre elles, **RSO-1 — déclarer selon la forme prescrite rend opposable** —, est ce qui donne force aux **vingt** conventions et à la règle de §8sexies ; **elle se fonde elle-même** : la circularité est déclarée en §A.16.6, non résolue. **Les RSO n'entrent pas au décompte ProfReg** : aucune RSO n'est un théorème, et aucune ne le deviendra.

**Effet du défaut.** Toute condition de bonne formation du set cite le code de l'effet de son défaut (E0 à E7), fixé par le critère ordonné de l'Annexe §A.15.11 : la première branche satisfaite l'emporte. *Ancrage de forme, PR-33 :* `l_ordre_fait_prevaloir_l_objet` (CONV-3 relève de la branche 1 avant la branche 4), `mal_formee_n_implique_pas_refusee`, `les_refus_ne_viennent_que_des_branches_un_a_trois`, `le_marqueur_ne_vient_que_de_l_appreciation_ou_du_candidat`, `sans_branche_pas_de_classement`, `l_inscription_dommageable_est_refusee_avant_tout_marqueur` (branche 1bis : l'inscription est elle-même le dommage), et `classement_de_reference` pour onze règles. Ces théorèmes établissent la forme du critère ; ils ne disent ni que le critère est juste, ni qu'une règle réelle est bien classée — ce classement est une lecture déclarée. `[LACUNE]` Le classement de référence compilé ne couvre pas toutes les règles que l'Annexe §A.15.11 classe.

**Alignement des couches avec ProfReg.** Le set suit la nomenclature à quatre couches de la documentation ProfReg (consolidée au set : `MRC_v5.7_ProfReg_Consolide.md`) : aucune table de correspondance n'est nécessaire. Les théorèmes Lean quantifient sur des types (`RegimeObligation`, `StatutDette`, `ContexteProspectif`…), non sur des numéros de couche. **Point de décompte.** Le décompte (en vigueur : Consolidé §1) n'est pas une déclaration de porteur : c'est une **sortie d'outil régénérable**. Le fichier `Audit.lean`, à la racine du projet ProfReg, est produit mécaniquement à partir de l'ordre d'import de `ProfReg.lean` et des déclarations `theorem` / `lemma` atteignables depuis lui ; `lake env lean Audit.lean` en donne à la fois la liste et l'audit d'axiomes. **Critère de décompte : toute déclaration `theorem` ou `lemma` atteignable depuis `ProfReg.lean`.** Sans critère écrit, deux relectures donnent deux nombres sans qu'aucune ait tort. Répartition sur l'instantané audité du 7 octobre 2026 : **271 théorèmes ne dépendant d'aucun axiome**, 224 dépendant du seul `propext`, 28 de `propext` + `Quot.sound`, et **10 des trois axiomes de Lean** (`propext`, `Quot.sound`, `Classical.choice`) — ces dix étant ceux dont un type est construit sur les réels (`ℝ`, `ENNReal`, `unitInterval`). **Aucun `sorryAx`.**

**Programme de preuve : PR-1 → PR-59** (décompte en vigueur : Consolidé §1). PR-24 est le premier appui formel de PAL-1 (PAL-1 et PR-24 sont rattachés à AX-1 v2 et à **AX-10**, sélectivité située de l'attention : Consolidé, ligne des axiomes), PR-25 l'appui de PAL-5 ; PR-6 est porté par `VJEVerification.lean`. **Le contrôle des `Classical.choice` ne sonne pas** pour PR-23, qui n'emploie ni réel ni littéral de chaîne, conformément à la leçon de §8quinquies. Compilé et audité sous Lean 4.31.0-rc1 ; linter `unusedVariables` silencieux.

> **Le résultat structurel.** Le nombre de théorèmes dépendant de `Classical.choice` reste limité aux théorèmes qui passent par les réels à mesure que le programme de preuve croît : c'est un fait stable, non une coïncidence de décompte : **l'architecture n'a besoin d'aucun choix ; seule la mesure en a besoin.** Toute recompilation qui ferait croître ce nombre signale qu'une **dépendance non voulue** est entrée dans un énoncé d'architecture. *Le contrôle détecte aussi un passage par les chaînes de caractères, non par les seuls réels — voir §8quinquies.* Toute recompilation qui donnerait un autre décompte prime et doit être tracée. *Réserve de portée.* L'audit d'axiomes établit que les preuves sont **complètes** ; il n'établit pas qu'elles démontrent ce que les noms annoncent. Trois sur-revendications identifiées sont traitées au §8bis.

**Réserve de portée (V10b).** `V10b_seuil_nondeclare_force_deliberation` est une tautologie structurelle (exhaustivité de `StatutDette`) : il n'établit pas l'exclusion `ATTRIBUEE + seuil NONDECLARE`. **Cette exclusion est un invariant de Couche 1 (ACT-ARCH-001, §7bis) ; **PR-3 est compilé** (`PR3_AttributionSeuil.lean` ; notamment `seuil_non_declare_interdit_attribution`, `attribution_exige_un_seuil_declare`, témoin `PR3_clauseSeuil_temoin_mal_forme`). Ne pas citer V10b comme établissant l'exclusion : la décision est de gouvernance (invariant déclaré), la preuve est distincte.

**§8bis. Sur-revendications identifiées et traitées.**

L'audit d'axiomes établit qu'une preuve est **complète** ; il n'établit pas qu'elle démontre ce que son nom annonce. Le linter `unusedVariables` de Lean a signalé quatre théorèmes portant une hypothèse inerte. Relecture faite, trois des quatre sur-revendiquent ; elles sont traitées ci-dessous.

| Théorème                                   | Ce qu'il énonçait réellement                                                                                                                                                              | Traitement                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `critique_released_by_porteur`             | `inv` et `h_delib` inertes : ni l'inventaire non vide ni le passage par la délibération n'y jouaient de rôle. Le titre annonçait pourtant « la désignation d'un porteur libère CRITIQUE » | **Corrigé.** Énonce le passage de fermé à ouvert : `¬ transition_valide statut_avant critique ∧ transition_valide statut_apres critique ∧ inv.val ≠ []`. Les trois hypothèses servent                                                                                                                                                                                                                                                                       |
| `V10a_planetaire_force_deliberation`       | `estPlanetaireSansPorteur` inerte : le statut lui était fourni séparément, le mot « planétaire » ne faisait rien                                                                          | **Corrigé** par la règle d'architecture `ReglePlanetaire` (§5.1), qui fait *découler* le statut de l'hypothèse planétaire au lieu de le supposer                                                                                                                                                                                                                                                                                                                      |
| `V10a_synthese`                            | même défaut                                                                                                                                                                               | **Corrigé** de même                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `V10b_seuil_nondeclare_force_deliberation` | trois hypothèses inertes, conclusion disjonctive sur les trois constructeurs de `StatutDette` — vraie de tout                                                                             | **Déclaré par le set** ci-dessus comme tautologie structurelle. **Converti en CONV-8** (décision du porteur), par cohérence avec CONV-1, CONV-2, CONV-6 et CONV-7. Le patron d'un vrai théorème à cette place est indiqué dans le bloc CONV-8 : déclarer la règle d'architecture, puis conclure par V4 — comme `V10a_planetaire_force_deliberation` |

**§8ter — quatrième forme.** Cas type, dans `VJEVerification.lean` : un énoncé de commutativité J↔E qui pose `revisionEffectuee := true` **par surcharge de champ** sur le résultat du sens J→E écrase le seul champ que le sens E→J consulte. **Rien de la branche J→E n'atteint alors le résultat** ; le théorème démontre les théorèmes 2 et 3 réunis sur un état dont la révision est décrétée dans l'énoncé. Seul l'avertissement `unusedSimpArgs` du linter (`appliquerSensJE`, argument `simp` inutile) le signale.

C'est une **quatrième forme de sur-revendication**, distincte des trois du tableau ci-dessus : ni hypothèse inutilisée, ni hypothèse reprise dans la conclusion, mais **une hypothèse introduite dans le terme même de l'énoncé**. Aucun outil ne la détecte directement ; un argument `simp` devenu inutile peut servir de fil, et rien ne garantit qu'il y en ait toujours un.

**Le contenu réel est meilleur que la revendication**, ce qui justifie une refondation plutôt qu'une conversion en convention : que le carré J↔E ne se ferme pas sans un acte de révision extérieur au calcul est précisément ce que l'architecture soutient par ailleurs — *une révision conceptuelle est un acte, non une fonction*. Trois théorèmes le portent : `VJE_carre_ne_commute_pas_sans_revision` (le trajet composé laisse l'état inchangé), `VJE_ferme_apres_revision_externe` (la fermeture, sous un nom qui dit que la révision est une prémisse), `sensJE_ne_produit_pas_la_revision`. AM-G7-04 est **levé sous condition de révision inscrite**, non inconditionnellement (NT-G7 §4.2 et §10).

**Quatre formes de défaut, et deux seulement sont outillées.** (1) *Preuve incomplète* — détectée par `#print axioms` (`sorryAx`), automatisée par `Audit.lean`. (2) *Hypothèse inutilisée* — détectée par le linter `unusedVariables`, déjà actif. (3) *Hypothèse reprise dans la conclusion* — **aucun outil ne la détecte** : c'est du Lean parfaitement légal. *Deux variantes : **3a**, hypothèse inerte, que `unusedVariables` détecte (§8quater) ; **3b**, hypothèse utilisée pour être restituée — le **dépliage** d'une définition —, invisible au linter et tranchée par la règle de §8ter-bis.* CONV-6 est la conversion d'un cas de cette troisième forme. Elle relève de la relecture humaine — `[LACUNE DÉCLARÉE]`, aggravée à chaque lot ajouté.

**§8ter-bis — la règle de partage entre dépliage et forme 3.** *Décision du porteur ; instruction : `ProfReg/Instruction_D-13_Regle_Depliage_Forme3_2026-09-28.md`.* Le patron « condition de bonne formation » (§8octies-bis) et la forme 3 (§8ter) désignent le même objet formel : un théorème qui prend une définition de bonne formation en hypothèse et en rend une clause. La règle les départage.

- **R-1 — Motif.** Un théorème est un **dépliage** d'un prédicat défini P (une `def` du set à valeurs `Prop` ou `Bool`, employée comme condition) s'il prend P en hypothèse et en tire sa conclusion par la seule définition de P (M⁺), ou s'il conclut `¬ P` par la seule définition de P (M⁻). Conjonctions et chaînages de dépliages sont des dépliages. *Hors motif* : (i) les compositions où intervient un lemme à contenu propre d'une autre définition ; (ii) les lectures de **fonctions** (`appliquer`, `fusionner`…) ; (iii) les lectures positives, qui concluent P et valent témoin.
- **R-2 — Licéité.** Un dépliage est licite s'il est accompagné (a) d'un **témoin bien formé** (`∃ x, P x`) et (b) d'un **témoin mal formé discriminant**, qui échoue **sur la clause dépliée**, les autres étant satisfaites. Les témoins sont dans le module ou y sont cités par leur nom. Pour une hypothèse de type (`NonEnumerable`), (b) peut être un témoin de conditionnalité.
- **R-3 — Statut.** Un dépliage licite est une **lecture** : l'obligation est **déclarée** dans la définition, sa **discrimination** est **démontrée** par les témoins. Un dépliage n'est **jamais cité seul** comme appui d'un axiome, d'un palier ou d'une CONV : l'appui cite la paire « définition + témoins ».
- **R-4 — Défaut.** Un dépliage sans les témoins de R-2 est une **forme 3 (variante 3b)** : compléter, retirer ou convertir en CONV.
- **R-5 — Exception : garde de non-régression déclarée.** Un énoncé vrai par construction est admis sans témoins si (i) son objet est la coïncidence ou la séparation **entre deux artefacts écrits séparément** (deux définitions, deux modules, une définition et une fiche) ; (ii) sa docstring porte `GARDE DE NON-RÉGRESSION — VRAIE PAR CONSTRUCTION, DÉCLARÉE` et nomme l'artefact gardé ; (iii) le Consolidé le range à part ; (iv) il n'est jamais cité comme appui ; (v) **un dépliage d'une seule définition ne peut pas être une garde.**
- **R-6 — Crible.** À chaque lot : extraction des théorèmes dont une hypothèse (ou la conclusion niée) a pour tête une `def` du set et dont la preuve tient en trois lignes au plus, puis relecture contre R-1 et R-2. Crible **procédural**, non un métaprogramme.
- **R-7 — Lectures de fonctions.** Une **lecture de fonction** rend la valeur d'une fonction définie dans le set sur une classe d'entrées, et sa preuve se réduit au dépliage de la définition (`rfl`, `unfold`, `simp [f]`, analyse de cas). Elle est **licite** si le module contient, ou cite par son nom, un **témoin discriminant** : une autre entrée pour laquelle la fonction rend une **autre** valeur. Sans ce témoin, c'est une **forme 1** — l'énoncé serait vrai quelle que soit la règle. Comme pour R-3, une lecture n'est **jamais citée seule comme appui** : l'appui cite la paire « définition + témoin ». *Hors du motif* : (i) une **propriété calculée** qui relie plusieurs évaluations (involution, commutativité, monotonie) est un **résultat** ; (ii) un **lemme de construction** (obligation de preuve d'un champ de structure) est licite par nature, jamais appui ; (iii) une **invariance d'un champ que la fonction ne touche pas** est une forme 1, sauf si un témoin montre que la fonction modifie autre chose. Une fonction à **sortie constante** par construction n'a pas de témoin possible : l'énoncé qui la lit est une **garde** (R-5), déclarée comme telle. **Table nominative** des lectures licites et de leurs témoins : Consolidé §2.2 ; **contrôle mécanique** de la table : `R7_Controle.lean`, un `example` par ligne, hors décompte. Le crible R-6 s'étend aux lectures de fonctions.

**Premier passage du crible.** 41 dépliages : 14 licites en l'état (dont un sous renvoi), 27 complétés par 14 témoins, **aucun retrait**. Deux gardes déclarées : `PR12_coincide_avec_la_fiche`, `la_machine_d_attribution_ignore_l_extinction`. L'éponyme de PR-15 est `sans_porteur_nomme_pas_de_renversement` ; c'est une **lecture** (R-3), dépliage de `RenversementDeclare`, témoignée par `charge_satisfaite_et_renversement_declare_coexistent` (témoin bien formé) et `PR15_discrimine` : elle n'est jamais citée seule comme appui. `[LACUNE DÉCLARÉE]` Les lectures de fonctions (hors motif ii) ne sont pas criblées.

**§8quater — la forme 3 sur le cinquième terme du statut du seuil.** Pour le cinquième terme du statut du seuil (CONV-9, Annexe §A.14.9), un énoncé qui prend en hypothèses « mobilisation bien formée » et « primitive `seuil-valuatif` » et dont la conclusion reprend son hypothèse de déclaration ne démontre rien : c'est la **troisième forme de sur-revendication**, que le linter de la deuxième (`unusedVariables`) signale par ses hypothèses inertes. Le théorème est `BienFormee_ne_borne_pas_le_quintuplet`, qui **exhibe le trou** — une mobilisation parfaitement bien formée au sens de R0-bis dont le cinquième terme n'est pas déclaré. **L'obligation est ainsi motivée par un théorème plutôt que par une intuition** ; la forme 3, comme la forme 4, n'est détectée que par un outil qui n'était pas prévu pour elle. `[LACUNE CONFIRMÉE — la forme 3 n'a toujours pas de crible.]`

**§8quinquies — le contrôle du compte `Classical.choice` et les chaînes de caractères.** §8 pose que le nombre de théorèmes exigeant `Classical.choice` est fixé, et que toute croissance de ce nombre signale une dépendance non voulue. Cas type : un registre de communalité typé `String` (PR-20) fait croître le compte, car la comparaison de deux littéraux de chaîne tire `Classical.choice` — vérifié sur un exemple minimal isolé. Ce n'est pas un passage par les réels mais par les **chaînes de caractères**. Le remède améliore le modèle : une mention dont les valeurs sont énumérables se type par une **énumération**, non par du texte libre. Deux enseignements, et le second est le plus utile. (a) **Le contrôle fonctionne** : il détecte un défaut dès sa première mise à l'épreuve. (b) **Il se lit** « une dépendance non voulue est entrée », et non « les réels sont entrés ».

**§8quinquies-bis — second cas, même cause.** Dans PR-6, un énoncé portant sur `sourceResistanceDID = some did` ferait croître le compte : `Classical.choice` entre par la comparaison d'égalité sur `String`, **exactement la cause identifiée sur PR-20**. L'énoncé est formulé sur `Option.isSome`, qui ne compare aucune chaîne.

> **Deux déclenchements, la même cause.** Le contrôle fait ce qu'on attend de lui — mais il ne dit pas *pourquoi* les chaînes de caractères le déclenchent : la règle opératoire (§8quinquies-ter) est établie sur des cas, non comprise. `[LACUNE DÉCLARÉE]`

**§8quinquies-ter — la règle des deux portes.** *Instruction : `ProfReg/Instruction_Suites_Audit_Axiomes_Conventions_RSO_2026-09-28.md` §4 ; vérifiée par compilation sur deux cas minimaux (`decide`, `rfl` et `==` sur `String` : aucun axiome ; `simp` sur `("A" : String) ≠ "B"` : `Classical.choice` ; `(x : ℝ) = x` par `rfl` : `Classical.choice`). Une règle « pas de littéral `String` dans un énoncé » serait trop large et trop étroite.*

> Deux portes, et deux seulement, ont fait entrer `Classical.choice` dans le programme : (1) `simp` sur une égalité propositionnelle de `String` — remède : `decide`, `rfl`, ou `==` booléen ; (2) tout énoncé dont un type est construit sur les réels (`ℝ`, `ENNReal`, `unitInterval`), quelle que soit sa preuve — cette porte est voulue, et chaque passage est déclaré au Consolidé §3. Le contrôle compte les déclarations qui passent par la porte (2) ; toute autre croissance signale la porte (1) ou une troisième, à identifier.

`[PORTÉE]` Établie sur deux cas minimaux et sur les occurrences du programme ; **non démontrée en général** — le comportement de `simp` dépend des lemmes de Mathlib, qui changent d'une version à l'autre.

**§8sexies — une cinquième forme, et elle n'est pas dans les preuves.** Les quatre formes de §8ter sont toutes situées dans l'écriture d'un théorème. La sonde sur la grammaire P-C-E-D-e-d en exhibe une cinquième, ailleurs :

> **Un champ déclaré qui double un contrôle calculable peut diverger de lui.**

Le cas type est un champ `respect_R1` (§8.5) qui enregistrerait le résultat d'un contrôle que la machine peut faire ; le set calcule ce contrôle au lieu de le déclarer. **PR-21 le démontre en général** — `ProfReg/PR21_ChampDouble.lean` : pour *tout* contrôle calculable et *toute* donnée, il existe une fiche dont le champ déclaré contredit le contrôle, et le mensonge va **dans les deux sens** (`les_deux_mensonges_existent`). L'argument est `le_champ_ajoute_un_degre_de_liberte` : le champ **double l'espace des états**, et la moitié de ce qu'il ajoute est incohérente ; **la forme corrigée n'a rien à quoi mentir**.

**Ce que la cinquième forme n'est pas.** Elle ne condamne aucun champ déclaré dont le contenu n'est pas dérivable des autres — la source d'un seuil, le porteur d'une déclaration, le régime d'une écriture. **Le défaut est le doublement d'un calcul, jamais la déclaration.** La règle qui en résulte tient en une phrase, et elle est symétrique de CONV-9 : *déclarer ce qui ne se calcule pas, calculer ce qui se calcule.*

#### §8octies — huitième forme : l'engagement sur-revendiqué

Les sept formes recensées portent sur des **énoncés formels** et sur des **objets périmés**. Une huitième porte sur les **notes de grammaire**.

> **Forme 8.** *Le résumé d'une grammaire énonce son engagement sous une forme plus forte que celle que son corps et ses sources soutiennent* : **universelle** là où elle est conditionnelle (NT-G4), **unidimensionnelle** là où elle est multiple (NT-G6), **exclusive** là où elle est prioritaire (NT-G11), **causale** là où elle est interprétative (NT-G8).

**Signe distinctif, et il la rend facile à cribler : la formulation correcte est presque toujours déjà dans le document.** NT-G4 porte « ne cherche pas la correspondance » (L98) ; NT-G11 porte « suppose une dispute professionnelle productive » (L46) et **deux** champs de juge là où son §2.1 n'en retient qu'un.

**Diagnostic.** Une section « question structurante » (§2.1) écrite comme une **accroche**, sans être réalignée sur le corps qu'elle résume, est le lieu de la forme 8 — alors qu'elle est la partie la plus lue de chaque note.

**La forme 8 n'est pas un accident : le crible des §2.1 la relève dans la plupart des notes.** Durcissements relevés : G1 (universel + métrologique), G2 (universel → doublement conditionnel), G3 (modal), G4, G6, G7 (unidimensionnel), G8 (causal), G11 (exclusif), G12 (causal + universel). Incertaine : G5 (défaut de lisibilité, non de logique). **Conformes : G9 et G10** — et ce n'est pas un hasard, leurs §2.1 sont *descriptifs de périmètre* plutôt qu'assertifs ; **celui de G9 est plus prudent que son corps**, et c'est le modèle de réécriture. Rapport : `Crible_2.1_Neuf_Grammaires_2026-09-11.md`.

> **Dans les neuf cas, la formulation correcte est déjà dans la note** — section lacunes, bloc théorique, règle d'inscription, table de champs, ou classement explicite en engagement réfutable. **Le défaut n'est pas un défaut de savoir, c'est un défaut de relecture.**

**Trois motifs mécaniques s'en dégagent, et ils sont outillables** — c'est le premier outillage de la forme 8 :

1. **Le champ en deux exemplaires.** Un champ portant deux typologies sous une source unique (NT-G7 `type_capabilité_centrale`), ou deux champs là où le résumé n'en nomme qu'un (NT-G11 `salarie_comme_juge` / `collectif_comme_juge`). **Deux occurrences sur douze, trouvées les deux fois par la table des champs.**
2. **La reformulation actée non répercutée.** Le corps acte une version affaiblie, le résumé garde la forte (NT-G12 : « participent à instituer » acté, « constitue » maintenu au §2.1). Un `grep "[Rr]eformulation actée"` la trouve.
3. **La perte du modalisateur en chaîne de citation**. **À chaque maillon d'une chaîne d'emprunt, une précaution tombe ; au troisième, une élaboration que ses auteurs signalaient comme telle est devenue une primitive du modèle.**

> **Le cas type.** Morizot & Neyret écrivent : *« C'est ce qu'on **pourrait appeler** la puissance affirmative du vivant »* — un modalisateur explicite, sur une expression qui interprète un concept de Canguilhem portant un autre nom (**la normativité vitale**). En faire l'identifiant de champ `puissanceaffirmative`, **sans guillemets et sans modalisateur**, sous un en-tête « Canguilhem, source primaire », c'est perdre ces précautions — alors que la même section interdit d'attribuer l'expression à Canguilhem.
>
> **Trois maillons, trois pertes** : Canguilhem nomme un concept ; les auteurs relais forgent une expression et la signalent comme leur ; un nom de champ la reprend et l'attribue au premier maillon.
>
> `[OUTILLAGE]` Le motif se cherche : **tout champ dont le nom provient d'une source qui le modalise**. Les marqueurs à relever dans les sources — *« ce qu'on pourrait appeler »*, *« ce que nous proposons de nommer »*, *« une sorte de »*, guillemets de distance — **et l'absence de ces marqueurs dans la note qui emprunte**. C'est un crible de sources, non de cohérence interne : il exige d'avoir lu ce que la note cite.
>
> **Portée, et elle dépasse le cas.** La forme 8 porte, dans ses deux premiers motifs, sur l'écart entre un résumé et son corps — un défaut interne, criblable sans sortir du document. **Ce troisième motif porte sur l'écart entre une note et sa source**, et il n'est pas criblable sans lire la source. `[LACUNE D'OUTILLAGE DÉCLARÉE — le set n'a lu au verbatim qu'une petite part de sa bibliographie.]`

> **Ce que l'alignement coûte, et ce qu'il rapporte.** Aucune grammaire ne perd un champ, une règle ou un usage : **les neuf durcissements sont des excès de résumé, pas des erreurs de conception**, et **chaque §2.1 dit ce que sa note soutient.** Deux alignements vont même dans le sens de la force plutôt que de la prudence : NT-G4, dont l'engagement est **plus fort** (l'effet échappe à l'intention, c'est pourquoi il faut le gouverner), et NT-G7, dont le §2.1 tient la promesse de pluralité qu'il énonce.

**NT-G7 — deux typologies dans un seul champ : un défaut plus grave qu'une erreur d'attribution.** Un champ `type_capabilité_centrale`, de type `Texte` donc incontrôlable, porterait deux typologies de deux cadres normatifs distincts sous la source unique « Nussbaum 2000 ». **Or une partie de ces valeurs relève d'un cadre que Nussbaum récuse expressément** — la note l'établit sur source primaire : « elle refuse de tenir un écosystème pour bon *by definition* (§vii "No Nature Worship") ». **Le champ mettrait sous le nom d'une autrice des valeurs contre lesquelles elle argumente.**

> **Motif de contrôle du crible : une cellule qui porte un historique est un champ mal découpé.** *Une note en cellule signale un champ à scinder ; elle ne le scinde pas.*

Le patron est celui de la règle de §8.4bis (formalisée par **PR-22**) : deux régimes de qualification → deux champs, `capabilite_individuelle` et `habitabilite_systemique`. **La tension T5 n'est pas logée à l'intérieur du champ mais dans la règle R-HABITABILITE-CAPABILITE**, où elle est assumée — patron de **CONV-12**.

**NT-G5 — un diagnostic « défaut de lisibilité » manquerait l'objet, et ce cas vaut méthode.** Testé sur l'axe de la forme 8 (résumé vs corps), « les deux régimes **doivent être couplés** » n'affirme rien de réalisé : « doivent » est déontique. **Mais c'est une obligation, et elle se teste sur l'axe des obligations — la Couche 2 : elle ne nomme ni porteur, ni horizon, ni critère.** `[ENGAGEMENT SANS PORTEUR — INCOHÉRENCE INTER-COUCHES, niveau 2.]`

> **Leçon de méthode : un crible ne voit que sur son axe.** La forme 8 est un axe ; elle n'épuise pas les défauts d'un §2.1. Un énoncé peut être conforme à son corps **et** mal formé comme obligation.

Forme retenue, par **§8quater** — *une obligation s'écrit comme condition de bonne formation* : *une inscription dans C-MILIEU-VECU n'est bien formée que si les deux régimes sont renseignés*. **Écrite comme condition de bonne formation, l'obligation n'a pas besoin d'être instrumentée dans C-SIGNAL** — le contrôle porte sur l'écriture. **Le défaut n'est pas d'instrumentation mais de lieu de l'obligation.**

> **Deux compléments à cette forme.**
>
> **(i) Le porteur manquant n'est pas le déclarant.** Une condition à **deux** champs, désignant « le déclarant de l'écriture » comme porteur, laisserait l'obligation flotter ailleurs : `appel_entendu_milieu = VRAI` — **entendu par qui ?** Un rapport S/P sans interprète n'est pas une médiance mais la binarité que la grammaire récuse. La condition porte donc sur **trois** termes — S, P **et `interprete_appel` (I)** — en extension déclarée du présent §8quater, jamais en élargissement tacite (même réserve de nommage que CONV-11). `[ENGAGEMENT SANS PORTEUR — levé par le troisième terme.]` *Ancrage PR-31 :* `le_marqueur_de_milieu_se_leve_exactement_sur_l_interprete_manquant` (S et P renseignés, I manquant : marqueur `[INSCRIPTION DE MILIEU SANS INTERPRÈTE]`, jamais une sanction), `trois_termes_temoin_discriminant`, `l_interprete_ne_se_deduit_pas_du_declarant` — le champ I n'est pas redondant par construction ; la condition de réfutation d'A-TÉTRA-3, empirique, n'est pas levée.
>
> **(ii) La divergence n'est pas une ouverture : elle n'est pas signalée.** `mode_metabolique_actif` est du côté de S, `appel_entendu_milieu` du côté de P. Attendre leur convergence, c'est attendre `S = P` — le **bond mystique** de Berque, qui s'accomplit « en énantiomère » : la religion absolutise P, le scientisme absolutise S. **Un signal de divergence serait le second, sous un marqueur mésologique.** Ce que C-SIGNAL reste libre de porter est l'**absence de déclaration de l'écart** par son interprète, jamais l'écart lui-même. → `NT-G5 §2.1ter`.
>
> **Ce que ce cas ajoute à la leçon de méthode du §8quater.** Le crible établit qu'« un crible ne voit que sur son axe ». Ce cas montre un cran de plus : **les cribles du set partagent un même axe de fond — le tiers exclu.** Un défaut qui consiste à n'offrir que deux valeurs là où la chose en a quatre n'est visible par aucun d'eux, *parce qu'aucun ne peut écrire la question*. C'est pourquoi la forme de §8quater peut fixer le **lieu** de l'obligation sans voir qu'il lui manque un **terme**. `[FORME CANDIDATE — trois cas (NT-G5 §2.1, §7ter, entretien John-C) ; ce n'est pas une démonstration.]` Instruction : `Note_Tetralemme_x_MRC_Amendements_2026-09-21.md`.

### §8octies-bis Trois motifs transversaux

*Le criblage multi-axes fait apparaître trois régularités.*

**1. Le bloc source est le point aveugle du set.** Trois cas relevés, tous de la même forme : **un en-tête revendique une autorité que le corps de la même section refuse.** « Canguilhem, source primaire » pour `puissanceaffirmative`, vingt lignes avant l'avertissement inverse ; « Nussbaum 2000 » sur `type_capabilité_centrale`, pour des valeurs que la note déclare non-nussbaumiennes ; « Nussbaum 2000 » dans le bloc source de R-HABITABILITE-CAPABILITE, dont la seule action écrit une valeur d'un autre ancrage.

> **La cause est mécanique : un bloc source est écrit une fois, à la création de la règle, et jamais relu quand le corps évolue.** C'est la variante « source » de la forme 8 — et **elle est criblable** : pour chaque règle, comparer les auteurs de son bloc source aux auteurs des champs qu'elle lit et écrit.

**2. Le champ qui porte une identité et un état.** Trois champs relevés présentent la même faute : `attracteur_culturel` (l'attracteur **et** son activation), `capabilité_plancher_menacée` (la capabilité **et** le franchissement), `obligation_preservation` (l'obligation **et** son porteur).

> **C'est la variante discrète du champ en deux exemplaires** — non pas deux typologies, mais **une chose et un prédicat sur cette chose**. Le patron de correction est constant : deux champs, et le second est un booléen.
>
> **Et chaque fois, la fusion a une conséquence opérationnelle** : une règle incalculable (`attracteur_culturel = ACTIF` sur du texte libre), une condition de réfutation intestable, **un DÉBIT imputé à un acteur lu dans un champ où il peut légitimement manquer**.

**3. Une obligation sans porteur se répare en déplaçant son objet, non en cherchant son porteur.** Les cinq obligations en cause attendent toutes un porteur qui n'existe pas — « à désigner », « à trancher », « à co-construire ». **Écrites comme conditions de bonne formation, elles portent sur l'écriture et non sur le monde** : leur porteur est alors le déclarant, qui existe toujours.

> **Ce que la réécriture ne fait pas, et qu'il faut dire.** Elle ne remplace pas l'obligation de fond : co-construire un seuil, trancher une incompatibilité restent à faire, et restent sans porteur. **Elle empêche seulement de mobiliser ce qui n'est pas fait.** *La condition de bonne formation ne crée pas le porteur manquant — elle rend visible son absence au moment où quelqu'un voudrait passer outre.*
>
> **Deux de ces conditions tiennent leur patron du set lui-même** : la contre-écriture de R-VIOLENCE-SYMBOLIQUE exige un DID distinct, en application de `autorefutation_n_est_pas_refutation` (PR-16 ; patron entier : L3 — une condition de réfutation n'est bien formée que si elle est exerçable par un tiers, `refutation_exige_un_tiers`, en un lieu de dépôt, `refutation_exige_un_lieu`, avec reprise de l'objection, `refutation_exige_une_reprise` ; lectures témoignées par `PR16_alterite_temoin_discriminant`, `PR16_moyens_temoin_discriminant`, `PR16_reprise_temoin_discriminant` ; transposition déclarée d'AX-14, Longino 1990, que PR-16 ne prouve pas) ; et `puissance_revendicative = BLOQUEE` suit **CONV-13** — *on ne diffère pas la désignation d'un porteur à un moment où plus personne n'aura intérêt à la faire.*

 `R-CAPABILITES` et l'ancrage §15 de NT-G7 lisent encore `capabilité_plancher_menacée` ; `OBLIGATION_PRESERVATION_VIOLEE` en NT-G5 lit encore le champ fusionné. **Les champs sont scindés, les règles qui les lisent ne le sont pas.**

`[MÉTHODE DU CRIBLE — §2.1 × corps de note.]` Relever la forme logique de l'engagement au §2.1 (quantificateur, modalité, exclusivité), puis vérifier qu'elle est celle que le corps et les sources soutiennent. Instruction : `Correction_G4_G6_G11_2026-09-11.md`.

> **Une remarque sur les conditions de réfutation, et elle vaut au-delà de ce cas.** Sur neuf conditions de réfutation, trois sont remplies dès leur premier test. **C'est leur succès, non leur échec** — elles sont écrites pour être testables. **Les six autres ne sont pas validées pour autant, elles sont seulement non testées.**

**Portée de la lacune.** Les quatre formes de §8ter portent sur les théorèmes du programme (décompte en vigueur : Consolidé §1) ; la cinquième porte sur **tous les schémas de champs du set**, qui n'ont jamais été criblés pour elle. `respect_R1` est le seul cas trouvé, et il l'a été par hasard — comme les formes 3 et 4. `[LACUNE DÉCLARÉE — le crible des schémas reste à faire.]`

**§8septies — une sixième forme, dans la documentation.**

> **Un théorème dont l'énoncé est exact, mais dont le témoin est dégénéré au regard de ce que sa documentation annonce.**

Le cas type est `accord_sur_l_existence_pas_sur_la_valeur` (PR-20 §4). Un commentaire disant « on n'exige pas que les deux comptabilités disent la même chose » suggérerait une **liberté d'évaluation**. Or son témoin est un **socle vide** : les deux registres divergent là où il n'y a aucun lien. Sur un lien existant ils coïncident, par construction — l'instance n'a pas de quoi exprimer un montant (CONV-10, Annexe §A.14.10). **L'énoncé est exactement ce qui est prouvé ; c'est une telle documentation qui promettrait davantage.**

**Ce qui distingue la sixième de la troisième.** La forme 3 **dans sa variante 3a** (hypothèse inerte) est détectable par `unusedVariables`, et l'a été (§8quater) ; la variante 3b (dépliage) ne l'est pas — §8ter-bis. La sixième est **hors de portée de tout linter** : rien dans le code ne relie un commentaire à la force du témoin qu'il décrit. `[FORME CANDIDATE — un seul cas ; sa frontière avec la forme 3 est un argument, non une démonstration.]`

> **Quatre fois sur quatre, les formes non outillées ont été trouvées par accident** — formes 3, 4, 5 et 6. C'est la régularité la plus solide du dispositif de contrôle, et c'est un constat contre lui.

**Correction.** Le commentaire de PR-20 §4 dit ce que le théorème dit ; elle ne touche **aucune preuve**, ni le compte de théorèmes.

**Règle de rédaction qui en découle, à appliquer à tout nouvel énoncé :** une obligation s'écrit comme **condition de bonne formation** de l'inscription, jamais comme hypothèse du théorème. Le théorème doit **conclure** l'obligation. C'est le patron de PR-3, PR-8, PR-10, PR-14 et PR-15. *Lecture exacte : l'obligation est **déclarée** dans la définition de bonne formation ; le théorème qui prend cette définition en hypothèse la **lit** ; ce qui est **démontré**, c'est que la définition discrimine — un témoin bien formé, un témoin mal formé par clause. « Conclure l'obligation » s'entend en ce sens, et pas autrement.*

## §9. Conditions de réfutation

Si une dette SYSTEMIQUE\_NON\_ATTRIBUEE pouvait déclencher CRITIQUE sans passer par DELIBERATION sans produire de pathologie observable, la machine d'états serait sur-contraignante. Si fractionactorielle pouvait être calculée de façon non arbitraire par un dispositif gouverné, l'invariant de déclaration (CONV-1) deviendrait une restriction injustifiée. Si regimeobligation s'avérait toujours réductible à ACTORIEL après enquête, la primitive serait redondante avec un simple champ porteur-non-encore-identifié. Si l'on documentait un dispositif où l'inscription d'une atteinte produit, sans montage supplémentaire, la désignation d'un débiteur, l'affectation d'une ressource, l'action et sa vérification, AX-5 tomberait, et les couplages de §7 seraient redondants avec l'inscription seule.

## §9bis. Vulnérabilité de substrat (T0) — limite de portée déclarée

Toutes les protections internes du registre (inaliénabilité, clause téléologique, standing élargi, machine d'états) supposent, pour produire effet hors du registre, d'être reconnues par un ordre juridique dont le substrat normatif reste le droit privé capitaliste (ancrage source : sections « Ancrage contre-capture » des grammaires, notamment → NT-G6 et → NT-G4). Aucun opérateur du set ne neutralise cette vulnérabilité : une clause d'inaliénabilité peut être requalifiée en restriction illicite, une clause téléologique écartée comme imprécise, un standing collectif refusé — chaque fois au nom de la cohérence interne du droit existant, sans capture délibérée.

T0 est donc déclaré comme **limite de portée** du registre, non comme risque gouvernable en interne. Les seuls leviers identifiés — ancrage juridictionnel par facteurs objectifs et plaidoyer pour un *just private law* — sont **externes au registre et sans porteur DID identifié** : ils sont signalés `[INCOHÉRENCE INTER-COUCHES — niveau 2]`, non résolus. Présenter une protection interne comme opposable *erga omnes* sans franchir T0 serait un `[DÉCOUPLAGE DE RÉGIMES]` (registre ≠ droit étatique environnant).

*Condition de révision.* Cette inscription est correcte tant qu'elle n'attribue à aucun opérateur la neutralisation de T0 ; elle serait à réviser si un dispositif interne au registre se montrait capable d'opposabilité externe sans relais juridictionnel — ce qui, en mode procédural, n'est ni établi ni plausible.

## §9ter. Vulnérabilité de base probante (T1) — seconde limite de portée déclarée

*(Source : `Lecture_Numero74_Meso-ESS_x_MRC_2026-09-14.md`. Instruction : `Decision_P8_Ecart_Recit_Pratique_x_Ecosysteme_2026-09-14.md`.)*

**L'objection, telle qu'elle est formulée.** Beaucreux & Gallois (2026), en conclusion d'une analyse des mutuelles santé françaises : *« Ces spécificités fortement mises en évidence dans les discours portés tendent toutefois à se confondre au regard des pratiques. […] Ainsi, ce n'est plus l'action qui différencie les acteurs, c'est le récit bâti autour de l'action. »*

**Pourquoi c'est l'objection la plus sévère que le champ méso adresse au registre, et non une remarque parmi d'autres.** Le MRC inscrit des **déclarations** : un porteur déclare un seuil, une source, une clôture, une dimension de pouvoir. La règle de second ordre **RSO-1** rend la déclaration opposable au même titre qu'un énoncé prouvé — c'est la force du dispositif. **Si la différenciation survit dans le récit alors qu'elle a disparu des pratiques, cette force devient le défaut** : le registre certifie du récit, et le certifie d'autant mieux qu'il est bien formé. *Un registre qui n'a aucun accès à la pratique ne distingue pas un porteur qui tient ses déclarations d'un porteur qui les rédige bien.*

**Le lien avec le garde-fou de réflexivité, qui est ici sa vraie mesure.** NT-G4 §7 pose que le MRC, registre de type comptable, est **lui-même performatif**, et qu'en présenter les inscriptions comme le *reflet* d'un réel est un `[RAISONNEMENT AUTORÉFÉRENTIEL]`. T1 dit d'où viendrait, concrètement, la sanction de ce garde-fou : **l'écart entre ce qui est inscrit et ce qui est fait est précisément ce que le registre ne voit pas**, et il ne peut pas le voir depuis ses propres inscriptions.

**T1 — l'énoncé.** *L'écart entre le récit qu'un acteur porte sur son activité et la pratique effective de cette activité n'est pas instruisible depuis le registre. Il requiert une enquête de première main, extérieure au registre, portant sur la pratique et non sur ce qui en est déclaré.*

**Pourquoi aucun champ n'est versé — et c'est la décision, non une abstention.** Un champ « écart récit/pratique » serait **non renseignable sur le corpus actuel** : sur les 579 fiches du corpus MRC, **433 sont de la littérature grise (194), de l'académique-comme-matériau (193) ou des verbatims d'audition (46)** — c'est-à-dire du **discours sur la pratique**, non de la pratique observée. **Un champ que rien ne permet de renseigner est pire que la lacune** : il produit des `NON_DETERMINABLE` en série, qui se lisent ensuite comme des absences d'écart. **La lacune est donc inscrite, et le champ ne l'est pas.**

**Ce que T1 n'est pas.** T1 n'est **pas** une généralisation de `ecart_formel_réel` (NT-G6), et le confondre serait un `[CHANGEMENT DE BASE NON TRACÉ]`. `ecart_formel_réel` compare un **droit formel** (C-DROITS) à un **droit exercé** — lecture *law in books / law in action*, dont l'Annexe §A.13 déclare que « le terme de comparaison est une référence conventionnelle déclarable ». **Un droit formel est un instrument inscrit ; un récit n'en est pas un.** Étendre le champ à ce second écart reviendrait à lui changer son terme de comparaison sans le dire, et à faire porter un même score à deux objets hétérogènes. *Deux écarts, deux termes de comparaison, deux instruments — ou, ici, un instrument et une limite déclarée.*

**Rapport à T0 (§9bis), et différence.** T0 est une vulnérabilité de **substrat juridique** : ce que le registre inscrit n'est pas opposable hors de lui sans relais juridictionnel. T1 est une vulnérabilité de **base probante** : ce que le registre inscrit ne dit pas ce qui est fait. **T0 borne la portée des inscriptions vers l'extérieur ; T1 borne leur prise sur le réel en amont.** Aucune des deux n'est gouvernable en interne ; toutes deux sont déclarées comme limites de portée, non comme risques gérés. `[INCOHÉRENCE INTER-COUCHES — niveau 2]`, non résolue.

**Condition de levée — bornée et vérifiable.** T1 est levée, en tout ou partie, le jour où le corpus comporte un matériau de **première main sur la pratique** — observation directe, données d'activité, archives d'exécution — permettant de confronter une déclaration inscrite à ce qu'elle décrit, **sur au moins un cas complet**. Le protocole d'entretiens semi-directifs en cours (v0.1, 10 septembre 2026) ne suffit pas à lui seul : **un entretien est un discours sur la pratique**, donc du matériau du même genre que celui qui manque. Il y contribue si, et seulement si, il est adossé à un matériau d'exécution.

**Condition de réfutation de T1 lui-même.** T1 tombe si l'on établit qu'un dispositif interne au registre permet de détecter l'écart récit/pratique sans matériau extérieur — par exemple par la seule cohérence des inscriptions entre elles dans la durée. **Cette voie n'est pas exclue et n'est pas instruite** : une déclaration qui contredit dans le temps les écritures du même porteur est détectable au registre. Ce que cela détecterait est une **incohérence déclarative**, non un écart à la pratique — mais la frontière mérite une instruction propre. `[À INSTRUIRE — porteur : porteur MRC ; horizon : institutionnel ; critère : exhiber une incohérence déclarative qui n'est pas réductible à une erreur d'inscription.]`

## §10. Inscription dans le régime de vérifiabilité-cohérence

NT-ARCH ne cherche pas la correspondance entre regimeobligation et une vérité ontologique de la responsabilité. Elle cherche la cohérence : le régime déclaré est-il cohérent avec la fraction déclarée (B1), le statut de dette (V2) et les transitions autorisées (V4) ? Les trois exigences sont instanciées : inscription traçable, cohérence inter-couches (invariants prouvés), gouvernance des lacunes (suivi au fichier d'avancement).

## §11. Note de vulgarisation — NT-ARCH couche 0 et 1 pour le site-vitrine du MRC

*Destination : site-vitrine du MRC. Public : académiques non spécialistes de l'architecture de gouvernance, y compris des chercheurs dont les cadres théoriques sont éloignés ou critiques de ces programmes. Régime : vérifiabilité-cohérence.*

## Quand une obligation n'a pas encore de porteur, que fait le registre ?

Un collectif peut engager des décisions qui affectent des tiers absents de la table : générations futures, espèces non-humaines, milieux dégradés, sociétés d'autres régions. Ces tiers ne peuvent ni signer un contrat ni consentir. L'obligation envers eux est réelle, mais sans porteur désigné capable de la réclamer. Le MRC — Modèle de Registres de Communalité — n'invente pas un porteur fictif : il inscrit l'obligation dans un état explicite — SYSTEMIQUE\_NON\_ATTRIBUEE — qui déclenche une procédure de délibération et d'inventaire. L'objectif n'est pas de fermer la question mais de la rendre traçable et gouvernable.

## Ce que NT-ARCH affirme — et ce qu'elle n'affirme pas

NT-ARCH ne prend pas position sur qui est ultimement responsable d'une dette systémique, ni sur quelle théorie de la justice intergénérationnelle est la plus fondée. Elle affirme quelque chose de plus étroit : le régime d'obligation (attribué ou non) doit être déclaré explicitement dans le registre — et les transitions entre régimes obéissent à des invariants structurels qui ne peuvent pas être outrepassés par une convention locale.

## La machine d'états : pourquoi on ne peut pas sauter les étapes

On ne peut pas traiter une situation comme urgente (CRITIQUE) sans avoir d'abord tenté de l'attribuer à un acteur responsable. L'enchaînement inscription → délibération → attribution → accès au niveau critique n'est pas une bureaucratie : c'est le verrou contre l'usage de l'urgence comme justification pour contourner la responsabilité.

## Deux verrous : dire « c'est attribué » oblige à dire pour qui, et « préserver » oblige à dire selon quelles normes

Deux invariants sont actés. Le premier interdit de déclarer une obligation « attribuée » tout en laissant non déclaré le seuil d'entrée dans la communauté morale — c'est-à-dire de dire « c'est réglé » sans dire *pour qui* cela compte (§7bis). Une position de repli est conservée en réserve : si le cas « seuil matériellement non déterminable au moment de l'attribution » se révélait empiriquement récurrent, l'interdiction serait assouplie en re-déclaration à échéance — l'invariant est réfutable, pas dogmatique. Le second exige que l'obligation de préservation d'une organisation soit dérivable des normes du territoire où elle opère, plutôt que d'un chiffre choisi par l'acteur seul (§7ter) — l'homologue, à l'échelle du milieu, de l'obligation de déclarer la fraction actorielle. Certaines règles de l'architecture sont déjà vérifiées formellement, d'autres restent à formaliser. L'invariant selon lequel une obligation ne peut être attribuée sans seuil déclaré est contrôlé dans ProfReg par le module PR-3 : le système bloque l'attribution et la criticité lorsque le seuil est non déclaré. En revanche, la preuve formelle de l'invariant de préservation présenté au §7ter relève d'un développement ultérieur et n'est pas présentée comme disponible dans cette version.

## La limite déclarée : le substrat peut être hostile

Le registre repose sur un substrat qu'il ne contrôle pas — droit applicable, infrastructure technique, rapports de force. Ce substrat peut lui être hostile (recodage des communs en actifs, neutralisation par l'écart entre droit formel et droit réel). NT-ARCH l'inscrit comme **limite de portée déclarée** (§9bis), non comme un problème résolu : un registre qui prétendrait se protéger lui-même de son substrat par ses seules règles internes se validerait lui-même.

## Ce que ce cadre demande au lecteur

Mobiliser NT-ARCH n'exige pas d'adhérer à une théorie particulière de la responsabilité ou de la justice. Il exige de reconnaître : (1) que certaines obligations ne peuvent pas encore être attribuées — et que ce fait doit être inscrit, pas ignoré ; (2) que l'urgence ne justifie pas de sauter la délibération ; (3) que représenter des générations futures exige de déclarer sur quelle base on le fait, faute de quoi la représentation n'est pas un acte gouverné mais une usurpation non tracée ; (4) qu'un registre honnête déclare ses propres limites — seuils non calculables, substrat non maîtrisé — au lieu de les absorber en silence.

\[LACUNES ET LIMITES — texte de vulgarisation\] (1) Les invariants d'architecture décrits ici sont actés et inscrits ; *leur part formalisable est **compilée** (programme PR-1 → PR-59) ; restent à l'horizon v6 la 2-cellule (F3 §3.5) et le produit monoïdal de V₂ ; les **paliers** restent procéduraux.* (2) ProfReg contient **604 théorèmes** ; le décompte en vigueur, son audit (`sorryAx`, `Classical.choice`, aucun `axiom` déclaré) et son journal sont tenus au Consolidé §1 ; il est régénérable par `lake env lean Audit.lean`. Toute recompilation ultérieure prime. (3) Ce texte ne remplace pas la note technique NT-ARCH : la machine d'états et les invariants sont définis en §2-§8.

---

# PARTIE B — Couche 2 : modes d'application (fiches F1–F10)

## §B.1 Principe de séparation et cartographie

Une fiche instrumente *comment* une obligation s'applique dans un domaine donné (champs, signaux, valorimètres, mouvements comptables). Les invariants structurels n'y vivent jamais — ils remontent en Partie A. Une fiche ne porte aucune source académique externe : elle renvoie « → NT-Gx » (mécanisme de renvoi : → Annexe méthodologique, §B).

| Fiche | Domaine d'application (Couche 2) | Grammaire(s) consommatrice(s) (Couche 3) |
|---|---|---|
| F1 | Travail / care (pratiques, distribution) | G-SOIN (NT-G3), G-TRAVAIL (NT-G11) |
| F2 | Milieu (métabolisme + attention, habitabilité) | G-MESOLOGIE (NT-G5), G-SOIN branche non-humain (NT-G3) |
| F3 | Sémantique (corpus, concepts) | G-PERFORMATIVITE (NT-G4), G-JUSTICE (NT-G7) ; méthode AFC (→ Annexe méthodologique) |
| F4 | Sujet responsable, obligation, irréversibilité | G-RESPONSABILITE (NT-G2) |
| F5 | Psychologie proximate, attracteurs cognitifs | G-EVOLUTIVITE (NT-G1) |
| F6 | Injustices épistémiques, droits, parité délibérative | G-JUSTICE (NT-G7), G-COMMUNALITE (NT-G6) |
| F7 | Crise mimétique, victime, méconnaissance | G-MIMETIQUE (NT-G8) |
| F8 | Mode comptable — mouvements DÉBIT/CRÉDIT, valorimètres | Toutes (interface R1) — **renvoi Partie A** + G-VALUATION (NT-G12) |
| F9 / F10 | Démocratie épistémique, formalisme délibératif | G-DEMOCRATIE-EPISTEMIQUE (NT-G10) |

G-AFFECTIF (NT-G9) traverse F1 et F5, et F7 par R-CARE-SACRIFICIEL ; G-PERFORMATIVITE (NT-G4) est transversale à toutes les fiches.

 De cette transversalité suit une conséquence : **une sous-couche consommée par plusieurs fiches ne se domicilie dans aucune**. C-TRACABILITE, invoquée par F3, F6 et F7 sans définition, est ouverte à ce titre en **§B.2bis** — hors fiches.

## §B.2 Invariants de cohérence Couche 2 ↔ Partie A

1. Toute écriture en régime `SYSTEMIQUE/HYBRIDE` déclenche INVENTAIRE-ASSETS-ACTIFS (§5.1) et ne peut atteindre `CRITIQUE` sans passer par la machine d'états (§4).
2. Tout valorimètre (F8) déclare sa source : `source_valuemetre` est **OBLIGATOIRE** et exige une **source déclarée et vérifiable**, par analogie à **CONV-1** et à son appui compilé `fraction_exhibe_sa_source` (`LotL2_PR2_PR14.lean`).

 > ### `[BORNAGE DE L'INVARIANT — DÉCISION DU PORTEUR. Instruction : `C3_Specification_Identifiants_et_Bornage_Invariant_2026-09-19.md`.]`
 >
 > **Une source est *déclarée et vérifiable* lorsque les quatre propriétés suivantes sont établies. L'écriture déclare quelle forme établit quelle propriété.**
 >
 > | | Propriété | Ce qu'elle interdit |
 > | :-: | :-- | :-- |
 > | 1 | **Désignation stable** — l'identifiant désigne un objet et un seul, et ne change pas quand l'objet change d'hébergement ou de dépositaire | le renvoi par titre ou par URL seule |
 > | 2 | **Résolution déclarée** — il existe une procédure nommée et accessible à un tiers par laquelle l'identifiant rend la description de l'objet | l'identifiant qui ne mène nulle part |
 > | 3 | **Vérification d'intégrité** — un tiers peut établir que ce qu'il obtient est bien ce qui a été désigné : empreinte, signature, ou attestation | la source modifiable après l'écriture sans trace |
 > | 4 | **Porteur nommé et réfutable** — l'identifiant dit **qui répond** de l'objet et **à quelles conditions cette réponse serait invalidée** | la source « scientifique » sans auteur ; l'instrument sans `conditionrefutation` |
 >
 > **Le DID (W3C DID Core 1.0, recommandation du 19 juillet 2022) est une forme possible de source déclarée et vérifiable ; il n'en est pas la forme obligatoire.** Sont également admises : une URL accompagnée de l'empreinte du document ; un identifiant de balise accompagné de l'empreinte du substrat ; un DOI ou identifiant d'archive ; un **LEI**, et un **vLEI** lorsqu'il existe ; une référence de norme publiée datée. **N'est pas admis** un renvoi en langue naturelle sans champ propre, **quel que soit le document qui le porte**.
 >
 > **La quatrième propriété est constitutive, et c'est elle qui empêche que le bornage affaiblisse la garde.** Une source qui satisfait les trois premières et pas la quatrième — un identifiant résoluble et vérifiable **dont personne ne répond** — ne satisfait pas l'invariant. Un DID non résoluble et sans porteur nommé ne le satisfait pas davantage.
 >
 > **Ce que le bornage restitue.** L'appui compilé `fraction_exhibe_sa_source` établit **l'obligation de déclarer une source**, jamais la forme de cette source : une exigence de forme dirait davantage que son appui. `[CHANGEMENT DE BASE TRACÉ — l'invariant est une exigence de propriétés, non de forme.]`
 >
 > **Preuve d'usage.** Le registre de données fiabilisées RATP 2025 satisfait l'invariant borné — empreintes SHA-256 de ses deux substrats, identifiant de balise iXBRL par fait, motif d'extraction pour tout fait non balisé — et **ne satisferait pas un invariant exigeant le DID**, faute de tout DID.
 >
 > **Raison de fond, et elle est doctrinale.** Le rapport fondateur pose que *« l'interopérabilité ne se décrète pas techniquement »* et exige notamment *« une gouvernance du système qui ne reconcentre pas, sous couvert de décentralisation, le pouvoir d'accréditation entre les mains des acteurs les mieux dotés »* (p. 131). **Rendre le DID obligatoire réserverait le registre à ceux qui savent en produire un** — une instance de gestion de l'eau (K3) n'enregistre pas une méthode DID, un grand groupe le pourrait.
 >
 > `[CE QUE LE BORNAGE NE GUÉRIT PAS — les deux seuils « typiques » de §8.9, marqués `[SEUIL SANS SOURCE]`, n'ont **aucune** source, sous aucune forme. Le bornage élargit les formes admises ; il n'admet pas l'absence.]` Cette clause s'appuie sur `fraction_exhibe_sa_source` (→ Annexe méthodologique).
3. Toute fiche mobilisant `C-STATUT-DETTE` **renvoie** à la Partie A §3 (un seul sens), ne redéfinit pas la règle.

Le respect de ces trois invariants est la condition pour que la commutativité prouvée (V1 *— sous l'hypothèse de cohérence logée dans le type, dont la nécessité est témoignée par `V1_coherence_discrimine` ; caractérisation : `V1_commute_ssi_coherence` —*, *la commutativité B1↔B2 (V3) est procédurale, déclarée comme telle (**CONV-2 étendue**, Annexe §A.15.9) : `V3_commutatif` est vrai par construction (forme 1)* ; *V10b est procédural et ne porte aucun théorème : CONV-2*) se propage du formel ProfReg jusqu'aux fiches.

## §B.2bis Sous-couche transversale C-TRACABILITE — ouverture minimale : instrument-hôte et opération instituante

*(Proposition P5 — `Lecture_Numero74_Meso-ESS_x_MRC_2026-09-14.md`. Instruction complète : `Decision_P5_Operation_Instituante_2026-09-14.md`.)*

> ### `[LACUNE RÉVÉLÉE]` C-TRACABILITE est invoquée sans être définie
>
> L'instruction de non-réductibilité exigée par P5, conduite contre `C-TRACABILITE`, établit que **cet opérateur n'a aucune définition de Couche 2** hors de l'ouverture minimale ci-dessous. Il est invoqué comme porteur d'obligation en **NT-G4** (localisation principale ; « exige que les conditions de genèse de tout instrument soient elles-mêmes inscrites » ; champ `légitimité_corpus_tracee` ; règle `R-MECONNAISSANCE` ; §7 ; §7ter Pistor), en **NT-G8** (`R-MECONNAISSANCE`, §6 : « porteur : acteur institutionnel désigné dans C-TRACABILITE ») et en **NT-G7** (provenance tracée, clean hands) — soit **trois grammaires de Couche 3 qui délèguent à une sous-couche de Couche 2 sans domicile**. Aucune fiche F1–F10 ne la porte ; elle ne figure dans aucune table de champs.
>
> `[INCOHÉRENCE INTER-COUCHES — niveau 2, déclarée, non lissée]` Une obligation de Couche 3 sans instrument de Couche 2 n'est pas une obligation : c'est une intention. Tant que la sous-couche n'est pas complétée, toute phrase du set affirmant que « les conditions de genèse sont inscrites dans C-TRACABILITE » énonce un programme, non un état.
>
> **Ce que fait le présent §B.2bis, et ce qu'il ne fait pas.** Il **ouvre** la sous-couche au seul titre de ce que P5 requiert — l'hôte d'une inscription — et lui donne un domicile transversal. Il **ne reconstitue pas** les conditions de genèse en général (qui a produit l'instrument, avec quel consentement, sous quelle légitimité), que les trois notes appellent et que seule une instruction propre peut verser.

**Titre de domiciliation transversale.** §B.1 pose que « G-PERFORMATIVITE (NT-G4) est transversale à toutes les fiches ». Une sous-couche consommée par F3, F6 et F7 et applicable à toute écriture ne peut donc vivre dans une fiche sans être restreinte par elle : elle se domicilie en Partie B **hors fiches**, au même rang que les invariants §B.2.

**B.2bis.1 Champs**

| **Champ** | **Type** | **Valeurs / Exemples** | **Description** |
| --- | --- | --- | --- |
| operation\_instituante | Énumération | PROBLEMATISATION / INSTRUMENTATION / LEGITIMATION / AUCUNE / **NON\_INSTRUIT** (défaut) | Opération de travail politique dont l'écriture est le produit (→ B.2bis.4, homonymie déclarée) |
| instrument\_hote | Texte structuré ou AUCUN | triplet obligatoire, cf. B.2bis.2 | Dispositif préexistant dans lequel l'inscription est logée |
| finalites\_importees | Texte | « arbitrage de l'allocation par les metteurs en marché », « matérialité financière », « périmètre d'agrément » | Finalités que l'hôte impose et que l'inscription n'a pas choisies |
| INSTRUMENT\_HOTE\_NON\_DECLARE | Signal | VRAI / FAUX | Déclenché par la condition B.2bis.3 |

**B.2bis.2 Triplet obligatoire de `instrument_hote`**

Renseigner `instrument_hote` n'est pas nommer un dispositif : c'est renseigner **trois éléments conjoints**, faute de quoi le champ est réputé non renseigné.

1. **Quel dispositif préexistant accueille l'inscription** — REP et cahiers des charges d'éco-organismes, CSRD/ESRS, référentiels ANC/CNoCP, taxonomie, label, agrément, statut juridique, appel à projets.
2. **Qui l'a conçu et pour quelle finalité initiale** — porteur identifié (DID lorsqu'il existe), jamais une catégorie générique.
3. **Ce que l'hôte impose** — en forme (mise en forme et rationalisation de l'activité), en gouvernance (qui arbitre), ou en calendrier.

La valeur **AUCUN** est admissible et signifie : l'inscription n'est logée dans aucun dispositif préexistant. Elle est une déclaration, non un défaut de renseignement.

**B.2bis.3 Condition de bonne formation et signal**

- Si `operation_instituante = INSTRUMENTATION`, alors `instrument_hote` est **obligatoire** (triplet complet). À défaut : `INSTRUMENT_HOTE_NON_DECLARE = VRAI`, l'écriture est **mal formée**, et la phase **DÉLIBÉRATION** est requise. **Effet du défaut, classé par le critère (Annexe §A.15.11).** **(a) En principe : E3** — `INSTRUMENT_HOTE_NON_DECLARE = VRAI`, écriture mal formée, phase **DÉLIBÉRATION** (branche 4). Motif : un hôte non déclaré laisse **ignorer s'il gouverne** l'obligation (qui arbitre, ce qu'il impose) ; sous RSO-8, le non-déclaré ne vaut pas l'hypothèse favorable. **(b) Exception : E4** — lorsque le triplet est incomplet **mais que son point 3 déclare explicitement que l'hôte n'impose aucune gouvernance**, le défaut ne porte pas sur l'attribution : l'écriture est inscrite, **mal formée**, et porte le marqueur `[INSTRUMENT HÔTE INCOMPLET]` (branche 5) ; pas de DÉLIBÉRATION. *Réfutabilité de l'exception* : la déclaration « aucune gouvernance imposée » est réfutable par tout tiers ; **réfutée, l'écriture repasse en E3** (patron du motif réfuté). `[MARQUEUR ET CLAUSE DE RÉFUTATION NOMMÉS PAR L'INSTRUCTEUR — révisables]` Le `[DÉCOUPLAGE DE RÉGIMES]`, marqueur épistémique, ne fait pas partie de l'effet ; le signal du registre `INSTRUMENT_HOTE_NON_DECLARE` en tient lieu. Le marqueur `[INSTRUMENT HÔTE INCOMPLET]` (cas b) porte un horizon (Annexe §A.15.11). *Ancrage PR-34* : `hote_non_declare_delibere`, `la_voie_intermediaire_ne_dispense_pas_du_triplet`, `P5_temoin_discriminant`, `sans_gouvernance_declaree_le_marqueur_suffit`, `P5_suit_le_critere`.
- Réciproquement, si `instrument_hote ≠ AUCUN`, alors `operation_instituante ≠ AUCUNE` : une inscription logée dans un dispositif préexistant est, par ce fait même, une opération instituante. **Le couplage tient dans les deux sens** — c'est la condition pour qu'il ne soit pas un `[DÉCOUPLAGE DE RÉGIMES]` à son tour.
- Si `instrument_hote ≠ AUCUN`, alors `finalites_importees` est non vide.

**B.2bis.4 Homonymie déclarée — « problématisation » a trois sens dans le set**

`[CHANGEMENT DE BASE TRACÉ]` Le mot est **déjà pris deux fois**. (i) **Annexe K** (§ cas chiffrés) l'emploie au sens de la sociologie de la traduction — « problématisation, intéressement, enrôlement, mobilisation » (grammaire GRAM-ANT) : c'est un *moment de l'enrôlement d'acteurs*. (ii) **NT-G4 §7** l'emploie au sens foucaldien via Lemke — « tout instrument est *effet* et *instrument* de sa problématisation » (règle du double conditionnement) : c'est le *champ de problèmes dont un dispositif est la réponse*. (iii) La valeur `PROBLEMATISATION` de `operation_instituante` est un **troisième sens** — l'opération de travail politique par laquelle un acteur construit publiquement un problème (Smith 2019, via Cordrie, Grassart & Bayard 2026).

**Règle d'usage :** le mot n'est jamais employé seul dans le set. On écrit `operation_instituante = PROBLEMATISATION`, ou « problématisation (GRAM-ANT) », ou « problématisation (Foucault/Lemke) ». Un emploi nu est un `[CHANGEMENT DE BASE NON TRACÉ]`. *(Même figure que l'homonymie « pronostic » déclarée en Annexe §A.5bis — NT-G10 le tient pour le pronostic catastrophique jonasien.)*

**B.2bis.5 Non-duplication avec `regime_comptable` (F8)**

F8 porte déjà `regime_comptable ∈ IFRS / PCG / CARE` et `C-MOUVEMENT-TYPE.R`, dont NT-G12 dit (ancrage Chiapello 2016) que **le choix d'un référentiel produit des effets économiques propres**. C'est **l'effet d'hôte, restreint au périmètre comptable** — et c'est, hors de la présente sous-couche, le seul endroit du set où il est instrumenté. `[RÉDUCTION PARTIELLE ÉTABLIE, DÉCLARÉE.]`

**Règle de non-duplication :** lorsque l'hôte est un référentiel comptable, `regime_comptable` **est** l'instance spécialisée ; `instrument_hote` ne le redéclare pas, il le **désigne** (élément 1 du triplet = renvoi à `regime_comptable`), et n'ajoute que les éléments 2 et 3. Hors périmètre comptable — REP, label, agrément, cahier des charges, appel à projets — `regime_comptable` est sans objet et `instrument_hote` porte seul.

**B.2bis.6 Non-réductibilité tracée — le test exigé par P5**

P5 conditionne toute inscription à l'instruction d'une redondance possible avec G-PERFORMATIVITE. **Elle est conduite et tracée** (`Decision_P5_...`, §3). Résumé, trois tests, deux sens chacun :

1. **Contre `boucle_confirmante_détectée`** — le signal détecte **le point fixe**, c'est-à-dire le seul cas où l'effet est *aligné* sur l'intention ; NT-G4 déclare explicitement qu'il est **aveugle au cas où l'effet va contre l'intention**. L'effet d'hôte est exactement ce cas : le réemploi solidaire logé dans la REP obtient une gouvernance des fonds qui bénéficie aux metteurs en marché. **Non réductible — et l'inscription lève partiellement une lacune que NT-G4 déclare elle-même sans instrument.** La forme de cette levée partielle est établie par PR-54 : l'effet d'hôte voit un cas contraire, et hors effet d'hôte la contre-performativité n'est vue par aucun signal.
2. **Contre `C-TRACABILITE` (conditions de genèse)** — la genèse est une propriété **de l'instrument** ; l'hôte est une propriété **de l'écriture**. Le même instrument du MRC, appliqué deux fois, peut être logé une fois dans CSRD et une fois dans CARE : la genèse est identique, l'hôte diffère. **Les arités diffèrent, la réduction échoue.** *(Même figure architecturale que `C-CLOTURE-ACCES`, §8.2bis de F8 : la clôture n'est pas inscrite comme propriété de l'espace mais comme condition d'une écriture.)* `[RÉSERVE — le test n'a pas pu être conduit contre une définition, puisqu'il n'en existe pas : voir l'encadré de lacune ci-dessus. Il porte sur l'objet tel que les trois notes le décrivent, non sur une table de champs.]`
3. **Contre `source_valuemetre` / `convention_seuil_source` (NT-G12)** — la source d'un valorimètre est *qui a posé le seuil* ; l'hôte est *dans quel dispositif l'écriture est logée*. Un seuil peut déclarer sa source (le porteur MRC) tout en étant logé dans CSRD, qui lui impose des finalités que la source n'a pas choisies ; inversement une écriture logée nulle part peut avoir une source non déclarée. **Indépendance établie dans les deux sens.** Réduction partielle dans le seul périmètre comptable : traitée par B.2bis.5.

**B.2bis.7 Garde-fous**

1. **Déclarer n'est pas guérir.** Un `instrument_hote` renseigné ne neutralise pas la finalité importée : il la rend contestable. Prétendre que la déclaration suffit serait un `[RAISONNEMENT AUTORÉFÉRENTIEL]`.
2. **Le typage ne vaut pas jugement.** `INSTRUMENTATION` n'est pas un défaut. Cordrie, Grassart & Bayard documentent que c'est souvent la seule voie disponible ; ce que le registre exige est la déclaration de son coût, non l'abstention.
3. **Aucune dispense d'invariant.** `operation_instituante = AUCUNE` ou `NON_INSTRUIT` ne dispense d'aucun invariant de Couche 1 : ni R1, ni la machine d'états, ni l'obligation de porteur. *(Homologue du troisième garde-fou de `statut_grammaire`, Annexe §A.17.)*
4. **Porteur obligatoire, et sa limite.** L'élément 2 du triplet exige un concepteur assignable. La tension déclarée en **NT-G4 §7bis** — la « stratégie sans sujet » de Foucault : un dispositif peut avoir une stratégie cohérente sans concepteur assignable — **s'applique ici sans atténuation**. Lorsque l'hôte n'a pas de concepteur assignable, l'élément 2 se renseigne `[NON ASSIGNABLE — tension NT-G4 §7bis]` et l'écriture reste bien formée. `[ENGAGEMENT SANS SYMÉTRIE écarté par cette clause.]`

**B.2bis.8 Conditions de réfutation**

*Du signal.* `INSTRUMENT_HOTE_NON_DECLARE` est un formalisme sans effet si, sur cas documentés, aucune écriture déclarant un hôte et ses finalités importées ne voit cette déclaration reprise dans une contestation ou une renégociation. L'obligation serait alors un `[ENGAGEMENT SANS SYMÉTRIE]`. *Rattachement AX-4 :* le signal opère à partir de `convocable`, non de `visible` — une déclaration d'hôte que nul ne peut convoquer ne réfute rien et n'établit rien.

*Du typage.* `operation_instituante` est **indécidable et doit être révisé** si, sur cas documentés, les trois valeurs ne se distinguent pas sans arbitraire — notamment si toute écriture type `INSTRUMENTATION`. *(Patron de réfutation homologue à `violence_symbolique`, NT-G7 §3.1.)* **Ce champ ne porte aucun engagement propre en dehors de son couplage à `instrument_hote` : c'est ce couplage, et lui seul, qui le fait franchir la règle de tri §A.9.**

**B.2bis.9 Critère de vérification — non satisfait**

 Aucun des champs ci-dessus n'a été appliqué à un cas. Le contrôle est reporté au corpus d'entretiens semi-directifs en cours de constitution (protocole v0.1 du 10 septembre 2026). **Ce champ est celui qui se prête le mieux à ce corpus** : le travail politique se raconte, et le triplet de l'hôte est une question d'entretien directe (« dans quel dispositif avez-vous dû loger cela, et qu'est-ce que cela vous a imposé ? »), là où `enjeu_acces` (F8 §8.2bis) appelle un matériau documentaire. `[PLAUSIBLE, NON VÉRIFIÉ — appréciation d'applicabilité, non résultat.]`

**B.2bis.10 Sources**

Cordrie, B., Grassart, C. & Bayard, V., « Le réemploi solidaire au risque de la récupération. Analyse d'un espace méso critique en construction à partir du travail politique des acteurs », *Revue Interventions économiques / Papers in Political Economy*, n° 74, 2026, DOI 10.4000/15naa, URL journals.openedition.org/interventionseconomiques/29702 — VÉRIFIÉ (lecture directe du PDF, décodage glyphique ; **pagination non disponible**, citations fiables au mot et non à la ponctuation fine). Verbatim retenu : « La REP constitue en ce sens un instrument porteur d'effets d'inertie […] qui ne peut complètement se départir de la façon dont il a été conçu et orienté au départ. » — **Smith, Andy, « Travail politique et changement institutionnel : une grille d'analyse », *Sociologie du travail*, vol. 61, n° 1, 2019, DOI 10.4000/sdt.14661** — référence **VÉRIFIÉE (biblio, relevée dans l'apparat de Cordrie et al.)**, **texte non lu** : les trois opérations sont **citées via Cordrie et al. uniquement** `[SOURCE NON VÉRIFIÉE de manière autonome — patron W-1d]`. Formulations retenues, telles que Cordrie et al. les donnent : la *problématisation* est « le processus par lequel des acteurs transforment des situations perçues comme [problématiques] » ; l'*instrumentation* « renvoie à la manière dont les acteurs traduisent leurs diagnostics et leurs revendications en dispositifs » ; la *légitimation* « au processus par lequel des acteurs cherchent à faire reconnaître leurs normes et leurs finalités ». — Ancrages internes : NT-G4 §7bis, NT-G12 §3 et Chiapello 2016.

## §B.2ter Phase RECHERCHE\_INTERVENTION de C-ENQUETE-V5 — enquête publique démocratique et constat d'effet

*Décisions du porteur (12/10/2026, fichier d'état §2, n° 47 à 50). Forme : PR-57, `PR57_EnqueteEtContrePerformativite.lean`.*

> `[LACUNE RÉVÉLÉE]` C-ENQUETE-V5 n'a pas de table de phases dans NT-ARCH : ses phases (ENQUÊTE, DELIBERATION, INVENTAIRE-ASSETS-ACTIFS, REVISION\_PROXIMATE\_ULTIMATE, ENQUETECOLLECTIVE, CONVENTION) ne sont nommées que dans les colonnes « Action / Phase » des tables de signaux ; l'Annexe H.9 en donne une liste. La présente section ouvre **une** phase ; la table complète reste à établir.

**B.2ter.1 Définition.** RECHERCHE\_INTERVENTION est une **phase** de C-ENQUETE-V5 : l'**enquête publique démocratique** au sens de Ferey (2024, ch. 5 §III, p. 319-325), c'est-à-dire une enquête sur un problème public, conduite par une association d'enquêteurs et de groupes concernés, qui :
1. institue le problème en articulant observation et conceptualisation (ch. 2 §III) ;
2. déclare la solution projetée comme **hypothèse** — « l'énonciation d'une situation problématique en termes de problème n'a de signification que si le problème institué se réfère […] à une solution possible » (Dewey, cité p. 140) ;
3. la met à l'épreuve par l'action et en mesure les effets ; un effet inattendu **relance** l'enquête (quotas de genre de la Constituante chilienne, p. 141) ;
4. satisfait les quatre conditions de l'enquête publique : communication, contrainte des spécialistes, association des enquêteurs aux groupes concernés, accessibilité publique de la connaissance (p. 319) ;
5. déclare sa propre position (réflexivité, ch. 3 §III, p. 198-200).

`[CHANGEMENT DE BASE TRACÉ]` Le terme est celui du MRC (Piste 6 ; Annexe K §K.7.2), non celui de Ferey, chez qui « recherche-intervention » n'apparaît pas (une occurrence de « recherche-action », citation de Di Iorio & Farias 2020, p. 222, rapportée p. 320). Le concept repris est l'enquête publique démocratique. L'Annexe K définissait RECHERCHE\_INTERVENTION comme la combinaison ENQUETE\_OBSERVATIONNELLE ⊗ ENQUETE\_COLLECTIVE ⊗ AUTOGOUVERNANCE : cette combinaison est désormais **déclarée comme plusieurs valeurs** de `regime_inscription_corpus` (F3, champ devenu liste), sans valeur composite ; elle ne définit pas la phase.

**B.2ter.2 Champs**

| **Champ** | **Type** | **Valeurs** | **Description** |
| --- | --- | --- | --- |
| hypothese\_declaree | Texte daté + DID porteur | solution projetée, effet attendu, date | Déclarée à l'inscription de l'instrument (genèse, C-TRACABILITE), **avant** toute épreuve ; une hypothèse déclarée après le constat n'est pas admise |
| effet\_constate | Énumération | ALIGNE / CONTRAIRE / A\_QUALIFIER / NON\_INSTRUIT (défaut) | Effet constaté par la phase ; NON\_INSTRUIT ne vaut pas ALIGNE |
| instance\_enquete | DID + liste DID | attestant ; personnes concernées associées | L'attestant est distinct du porteur de l'instrument ; l'instance associe les personnes concernées (contrainte des spécialistes, Ferey p. 319 ; représentation des absents : F10) |
| CONTRE\_PERFORMATIVITE\_ATTESTEE | Signal | VRAI / FAUX | `effet_constate = CONTRAIRE` dans un constat recevable |

**Recevabilité d'un constat** : attestant ≠ porteur de l'instrument **et** personnes concernées associées **et** `hypothese_declaree` antérieure au constat.

**Effet du défaut** (Annexe §A.15.11). Un constat dont l'attestant est le porteur de l'instrument, ou qui n'associe pas les personnes concernées, reste inscrit, mais la qualification « constat recevable » est refusée (**E6**) : il ne lève aucun signal et ne relance pas la phase. Une hypothèse déclarée après le constat n'est pas inscrite comme `hypothese_declaree` (**E1**, branche 2 : elle simule une déclaration *ex ante*, `hypothese_apres_coup_non_admise`) ; le constat reste sans hypothèse antérieure, donc non recevable.

**B.2ter.3 Effet.** CONTRE\_PERFORMATIVITE\_ATTESTEE **relance** la phase RECHERCHE\_INTERVENTION, puis ouvre DELIBERATION (révision de la catégorie de base ou de l'instrument ; inscription en C-MEMOIRE-PERTES si l'effet est irréversible). Un constat A\_QUALIFIER relance la phase sans lever le signal. Aucune relance sans constat nouveau.

**B.2ter.4 Déclencheurs**

| Déclencheur | Appui | Limite |
| --- | --- | --- |
| Contestation par une personne concernée (effet contraire allégué) | Ferey : l'enquête part de la « difficulté ressentie » (p. 138-139) et du besoin de connaître des concernés (p. 322) | Déclencheur principal |
| `boucle_confirmante_detectee` (F3) | Ferey : le recensement officiel de Buenos Aires ne parcourt que les « zones critiques » repérées par les décomptes précédents (p. 322) | Vérifier que le point fixe n'est pas un effet Goodhart |
| Réfutation Goodhart (NT-G10 : `qualiteenquete = SATISFAISANTE` et écart formel / réel croissant) | Ferey : des observations « qui amassent des faits » sans mener nulle part (Dewey, cité p. 324) | — |
| `INSTRUMENT_HOTE_NON_DECLARE` ou hôte déclaré (§B.2bis) | Appui MRC seul (P5), non Ferey | Appui déclaré comme propre au MRC |
| Échéance déclarée | Faible : Ferey critique les « enquêtes routinisées menées par des spécialistes administratifs » (p. 325) | **N'ouvre la phase que si la revue associe les personnes concernées** |

**B.2ter.5 Ce que ProfReg établit (PR-57).** NON\_INSTRUIT ne vaut pas ALIGNE (`non_instruit_ne_vaut_pas_aligne`) ; le porteur ne s'atteste pas lui-même (`le_porteur_ne_s_atteste_pas`) ; sans les concernés, pas de constat recevable (`sans_les_concernes_pas_de_constat`) ; une hypothèse déclarée après coup n'est pas admise (`hypothese_apres_coup_non_admise`) ; témoin `constat_temoin_discriminant` ; A\_QUALIFIER relance sans signal (`a_qualifier_relance_sans_signal`) ; pas de relance sans constat (`pas_de_relance_sans_constat`) ; **l'enquête rend visible une contre-performativité que PR-54 montre invisible** (`l_enquete_rend_visible_la_contre_performativite`) ; sans constat, la lacune demeure (`sans_constat_la_lacune_demeure`) ; une échéance sans les concernés n'ouvre pas la phase (`echeance_sans_concernes_n_ouvre_pas`). **Hors ProfReg** : la qualité de l'enquête (NT-G10, `qualiteenquete`), la justesse d'un constat, les cas qu'aucun déclencheur n'atteint.

**B.2ter.6 Conditions de réfutation.** La phase est un formalisme sans effet si, sur cas documentés, aucun constat CONTRAIRE ou A\_QUALIFIER ne débouche sur une révision ou une renégociation de l'instrument. L'exigence d'association des concernés est mal posée si elle rend, sur cas documentés, toute enquête impossible à réunir : la représentation des absents (F10) doit alors en tenir lieu, sous les mêmes gardes qu'en NT-G4 §6bis.

**B.2ter.7 Source.** Ferey, C., *Une justification épistémique pragmatiste de la démocratie. Connaissance et participation politique en contexte inégalitaire : de John Dewey à la philosophie féministe contemporaine*, thèse de doctorat en philosophie, Université Paris Nanterre, 2024 (NNT 2024PA100101 ; HAL tel-05005015). VÉRIFIÉ — lecture directe (biblio), pages de l'édition imprimée.

## §B.3 Contenu des fiches F1–F10 (complet)

*Reproduction des dix fiches F1–F10, renvois « → NT-Gx » appliqués.*

*Reproduction fidèle des fiches F1–F4 et F8. Les actions de cohérence de la section A n'y sont pas appliquées.*

### Fiche 1 — Mode travail étendu

Localisation : Couche 2 — fiche opérationnelle Mode travail.

**1.1 Objet et fondements théoriques**

La Fiche Mode travail étendu réinstancie dans la Couche 2 les trois couches opérationnelles travail (C-DPQT, C-MURRAY, C-COMMUNALITE-TRAVAIL) et la branche travail de la règle R-CARE, ainsi que la sous-couche **C-GENRE-METIER**, que G-SOIN et G-AFFECTIF partagent : qualité et capabilité au travail → NT-G11 ; care → NT-G3 ; régime affectif collectif → NT-G9 ; capabilités plancher → NT-G7 ; performativité / communalité de travail → NT-G4 ; communs → NT-G6.

**1.2 Champs nommés réintégrés**

Sous-couche C-DPQT (Dispositif de Promotion de la Qualité du Travail)

| **Champ**             | **Type**    | **Valeurs / Exemples**                                              | **Description**                                                                            |
| --------------------- | ----------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| type\_deliberation    | Énumération | RESOLUTION\_PROBLEME / DISPUTE\_MANIERE\_FAIRE / REDEFINITION\_BUTS | Type de délibération engagée dans le dispositif DPQT                                       |
| frontiere\_metier     | Texte libre | ex. soins infirmiers                                                | Frontière de métier délimitant le périmètre de la délibération                             |
| profondeur\_justice   | Énumération | SURFACE / INTERMEDIAIRE / PROFONDE                                  | Niveau d'atteinte à la justice dans le travail                                             |
| salarie\_comme\_juge  | Booléen     | VRAI / FAUX                                                         | Le salarié est-il reconnu comme juge légitime des conditions d'exercice de son métier ?    |
| acteurs\_deliberation | Liste DIDs  | \[DID acteur 1, DID acteur 2…\]                                     | Acteurs participant effectivement à la délibération DPQT (identifiés par DIDs, Annexe H.1) |
| dispositif\_soutien   | Texte libre | ex. comité de métier                                                | Dispositif institutionnel portant la délibération                                          |

Sous-couche C-MURRAY (Risque / Autonomie-Subordination / Expressivité)

| **Champ**                | **Type**      | **Valeurs / Exemples**                               | **Description**                                                 |
| ------------------------ | ------------- | ---------------------------------------------------- | --------------------------------------------------------------- |
| risque\_murray           | Score 1-5     | 1 (faible) à 5 (élevé)                               | Niveau de risque professionnel subi (santé, emploi, revenus)    |
| autonomie\_subordination | Score -5 à +5 | \-5 (subordination totale) à +5 (autonomie complète) | Degré d'autonomie ou de subordination                           |
| expressivite             | Score 1-5     | 1 (nulle) à 5 (pleine)                               | Capacité à exprimer ses valeurs et son identité dans le travail |
| etat\_travail\_murray    | Énumération   | VIABLE / FRAGILE / DEGRADE                           | État synthétique selon les trois axes de C-MURRAY (→ NT-G11)                    |

Sous-couche C-COMMUNALITE-TRAVAIL (Commun de capabilités)

| **Champ**                 | **Type**    | **Valeurs / Exemples**                   | **Description**                                                         |
| ------------------------- | ----------- | ---------------------------------------- | ----------------------------------------------------------------------- |
| type\_equilibre           | Énumération | STABLE / INSTABLE / EN\_TRANSITION       | Type d'équilibre du commun de capabilités en milieu de travail          |
| ambiance\_transition      | Texte libre | ex. restructuration en cours             | Description de l'ambiance de transition du collectif de travail         |
| COMMUN\_GOUVERNE\_FRAGILE | Signal      | VRAI / FAUX                              | Le commun de travail est-il gouverné de manière fragile ?               |
| codeveloppement\_pa       | Texte libre | ex. co-construction PA avec travailleurs | Description du processus de co-développement des plans d'action         |
| commun\_uri               | DID         | did:registre:travail:metier-x            | Identifiant décentralisé du commun de capabilités concerné (Annexe H.1) |

Règle R-CARE — 4 défis (branche travail)

| **Champ**                  | **Type**   | **Valeurs / Exemples**            | **Description**                                                                           |
| -------------------------- | ---------- | --------------------------------- | ----------------------------------------------------------------------------------------- |
| defi\_inventaire\_travail  | Texte      | Types de travail de care recensés | Défi 1 — Inventaire : génère écriture C-GENRE-METIER sur types de care non reconnus       |
| defi\_operations\_travail  | Texte      | Opérations de care identifiées    | Défi 2 — Opérations : instancie via C-DPQT (type\_deliberation = DISPUTE\_MANIERE\_FAIRE) |
| emotion\_dominante\_genre  | Texte      | ex. anxiété organisationnelle     | Défi 3 — Coûts : émotion dominante du **genre professionnel** (C-GENRE-METIER) associée au travail de care non reconnu — coût du travail émotionnel non reconnu (→ NT-G3, NT-G9). Distincte de `regimeaffectif`, qui qualifie le régime (ci-dessous) |
| defi\_attribution\_travail | DID acteur | DID acteur responsable            | Défi 4 — Attribution : génère écriture CRÉDIT vers acteur responsable via C-DROITS        |
| soin\_avec                 | Booléen    | VRAI / FAUX                       | Précondition SOIN\_AVEC : la relation de care est-elle mutuellement attentive ?           |


Sous-couche C-GENRE-METIER — régime affectif collectif (→ NT-G9 ; partagée avec G-SOIN, → NT-G3)

*Les champs sont ceux de NT-G9 §3.1 et §10.1, sous leurs noms. Ils qualifient un régime **collectif** ; ils ne psychologisent pas les personnes (condition de réfutation de NT-G9 §2.1). `[INFÉRENCE DÉCLARÉE]` NT-G9 ne fixe que les valeurs que ses règles nomment (CONCENTRÉE, BLOQUÉ, ABSENTE, et les énumérations de `regimeaffectif`, `sourcequalification`, `statut_rgpd_regimeaffectif`, `sphereviolee`) ; les autres valeurs ci-dessous sont proposées, révisables. `typeLutte`, lu par R-MESENTENTE, n'a qu'une valeur nommée dans le set (LUTTEEXTERNE, NT-G9 §3.2) — `[LACUNE]` ; porteur : rédacteur NT-G9 ; horizon : Vague B.3 ; critère : énumération close ou ouverte déclarée.*

| **Champ** | **Type** | **Valeurs / Exemples** | **Description** |
| --- | --- | --- | --- |
| regimeaffectif | Énumération | DEEPACTING / SURFACEACTING / DISSOCIATION / DESIDENTIFICATION | Régime émotionnel du collectif de travail |
| sourcequalification | Énumération | CLINIQUEEXTERNE / DIALOGUEPROFESSIONNEL / ARCHIVAGEDESACTES / INDÉTERMINÉE | Qui qualifie le régime ; `INDÉTERMINÉE` ne qualifie pas (**CONV-20**) |
| consentementcollectif | Booléen | VRAI / FAUX | Les acteurs ont consenti à la qualification par un tiers (**CONV-20**) |
| statut\_rgpd\_regimeaffectif | Énumération | ANONYMISE / PSEUDONYMISE / AGREGESEUL / NONCOLLECTE | Régime de protection des données de qualification (**CONV-20**) ; `NONCOLLECTE` : aucune qualification inscrite, seule l'existence des traces est tenue |
| porteetemporelle | Durée | horizon de conservation | Applicable sur support effaçable seulement |
| chargeemotionnelledistribuee | Énumération | CONCENTRÉE / RÉPARTIE | Distribution de la charge émotionnelle (champ partagé avec G-SOIN) |
| reconnaissancechargeemotionnelle | Booléen | VRAI / FAUX | La charge émotionnelle est-elle reconnue ? |
| vitalitediscussionprofessionnelle | Énumération | VIVANTE / ATONE / ABSENTE | Vitalité de la controverse sur le travail : une unanimité sans controverse est à qualifier, non à présumer saine |
| unanimiteaffective | Booléen | VRAI / FAUX | Cohésion affective apparente du collectif |
| seuildisposition | Énumération | ATTEINT / NON\_ATTEINT | Disposition à passer à l'action (l'envie) ; reçoit `modificateur_affectif` (F5) |
| seuilcapacite | Énumération | ATTEINT / BLOQUÉ | Capacité réelle d'agir ; **la disposition ne produit pas la capacité** |
| sphereviolee | Énumération | ETRE\_IDENTITE / FAIRE\_CONTRIBUTION / NON\_DECLAREE | Sphère de reconnaissance atteinte ; une atteinte à l'une n'implique pas l'autre |
| signalsouffrance | Booléen | VRAI / FAUX | **Indice explicatif, jamais appui d'une créance (CONV-19)** |
| etatdelademande | Énumération | ADRESSABLE / NON\_ADRESSABLE | La souffrance est opérante si la demande est encore adressable |
| evenementmesentente | Booléen | VRAI / FAUX | Rupture de comparabilité : réinitialise la lecture des trajectoires, n'est pas un changement d'état |
| typeLutte | Énumération | LUTTEEXTERNE / … | Nature de la lutte qui accompagne la mésentente — **valeurs non fixées** `[LACUNE]` |
| hypotheseinjusticependante | Entrée | reçue de F6 (`hypothese_injustice_vers_affectif`) | Hypothèse explicative à examiner avant toute qualification de dysfonctionnement ; **ne qualifie pas** le régime (PR-53, `l_hypothese_seule_ne_qualifie_pas_le_regime`). Points d'arrivée : testimoniale → `sphereviolee`, R-PIEGE-RECONNAISSANCE ; herméneutique → `etatdelademande`, `evenementmesentente` |
| denidutravailreeldetecte | Dérivé | VRAI si `sphereviolee` = FAIRE\_CONTRIBUTION | **Déni du réel déclaré** : l'atteinte à la reconnaissance de la contribution est déclarée ; entre dans une qualification sous CONV-20 |
| denidutravailreelpresume | Dérivé | VRAI si aucune atteinte à la contribution n'est déclarée **et** si un signal empêche de la déclarer : `ideologiedefensivedetectee`, R-ACTIVITE-EMPECHEE, `hypotheseinjusticependante`, `piegereconnaissancesuspecte`, ou une trace C-MEMOIRE-PERTES de nature DEPART\_DE\_PORTEURS sur le même métier | **Déni du réel présumé** : hypothèse à examiner, **jamais une qualification** ; déclaré et présumé ne se recouvrent pas (PR-53, `declare_et_presume_s_excluent` ; témoin `deni_presume_temoin`) |

*Règles de bonne formation de la sous-couche.* **CONV-20** : une qualification n'est inscriptible qu'avec une source déclarée, le consentement collectif et un statut protecteur ; **sur support distribué, aucune qualification n'est inscriptible** (`sur_support_distribue_rien_n_est_inscriptible`, PR-52 ; témoin `inscriptible_temoin_discriminant`) — `[ENGAGEMENT À HORIZON IRRÉVERSIBLE]` rendu inopérant par construction (support distribué : → Annexe H). Effet du défaut : E1, branche 1bis du critère (l'inscription est elle-même le dommage ; Annexe §A.15.11). **CONV-19** : `signalsouffrance` n'entre dans aucune qualification de créance (`la_souffrance_seule_ne_qualifie_aucune_creance`, lecture, témoin `la_souffrance_n_empeche_pas_la_qualification`, PR-52). Effet du défaut : E6 *(proposé)*.

*Règle d'ordre (canal G-JUSTICE → G-AFFECTIF ; NT-G9 §4.2).* Une qualification de dysfonctionnement du collectif n'est bien formée que si l'hypothèse d'injustice pendante (`hypotheseinjusticependante`) et, le cas échéant, le déni présumé ont été **examinés** — à commencer par l'hypothèse de mésentente. **Deux défauts** (Annexe §A.15.11) : qualification seulement inscrite sans examen → **E4**, marqueur `[HYPOTHÈSE D'INJUSTICE NON EXAMINÉE]` ; qualification non examinée **mobilisée dans une décision touchant des personnes** (C-SANCTIONS, R-REFERENT, `REDEFINITION_BUTS`) → **E3**, phase DÉLIBÉRATION : le défaut porte alors sur l'attribution du trouble (PR-53, `ordre_non_respecte_deux_effets`). *Cycle* : avec A→J (la souffrance alimente F6 comme indice), le canal forme un cycle ; il termine parce que J→A ne relit pas la souffrance et qu'une injustice issue de la seule souffrance ne passe pas (`le_cycle_AJ_termine`, `la_souffrance_ne_se_confirme_pas_elle_meme`). *Condition de réfutation du déni dérivé* : si des dénis présumés sont régulièrement confirmés par un dialogue professionnel sans qu'aucune atteinte à la contribution ne soit jamais déclarée, la dérivation manque son objet — retour à un champ propre (décision du porteur, 12/10/2026). Cas types instruits : déni partagé par le collectif, déni tenu par l'institution, travail invisible par construction, reconnaissance sur le mauvais objet, silence par crainte, départ des porteurs — ce dernier lu sur C-MEMOIRE-PERTES (`nature_trace` = DEPART\_DE\_PORTEURS) ; le critère qui le distingue d'un roulement ordinaire reste à instruire `[LACUNE]`.

**1.3 Connexions C-SIGNAL et règles activées**

| **Signal C-SIGNAL**       | **Condition de déclenchement**                                   | **Action / Phase C-ENQUETE-V5**                                        |
| ------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------- |
| GENRE\_GELE\_PERSISTANT   | emotion\_dominante\_genre élevée sur 3 interactions consécutives | Déclenche R-REFERENT + inscription C-SANCTIONS                         |
| GESTION\_INSTRUMENTALE    | salarie\_comme\_juge = FAUX ET profondeur\_justice = SURFACE     | Déclenche alerte DPQT + phase DELIBERATION dans C-ENQUETE-V5           |
| R-MALTRAITANCE            | risque\_murray ≥ 4 ET autonomie\_subordination ≤ -3              | Déclenche C-SANCTIONS (type GELE\_PERSISTANT)                          |
| COMMUN\_GOUVERNE\_FRAGILE | type\_equilibre = INSTABLE ET codeveloppement\_pa absent         | Déclenche signal COMMUN\_GOUVERNE\_FRAGILE + phase AUTOGOUVERNANCE     |
| R-REFERENT                | defi\_attribution\_travail vide ET GENRE\_GELE\_PERSISTANT       | Déclenche inscription C-DROITS : attribution forcée d'un référent care |
| R-DEEP-ACTING             | chargeemotionnelledistribuee = CONCENTRÉE ET reconnaissancechargeemotionnelle = FAUX ET regimeaffectif = SURFACEACTING sur 2 cycles | Inscription C-MEMOIRE-PERTES ; signal R-CARE chronique (→ NT-G3) |
| R-ACTIVITE-EMPECHEE       | seuilcapacite = BLOQUÉ ET vitalitediscussionprofessionnelle = ABSENTE sur 2 cycles | Bloque les interventions purement communicationnelles ; priorité aux conditions du pouvoir d'agir |
| R-PIEGE-RECONNAISSANCE    | regimeaffectif = DEEPACTING ET unanimiteaffective = VRAI ET sphereviolee = FAIRE\_CONTRIBUTION non reconnue, gratifications identitaires distribuées | Signal `piegereconnaissancesuspecte` |
| R-MESENTENTE              | evenementmesentente = VRAI ET typeLutte = LUTTEEXTERNE | Suspend la lecture continue des trajectoires ; annotation de réinitialisation |
| IDEOLOGIE\_DEFENSIVE      | signaux `ideologiedefensivedetectee`, `neutralisationemotionnelledetectee` ; champ `pertetracabiliteinstitutionnelle` | Inscription C-MEMOIRE-PERTES (dégradation lente, sans signal critique immédiat) |
| R-ORDRE-QUALIFICATION     | qualification de dysfonctionnement ET (`hypotheseinjusticependante` OU `denidutravailreelpresume`) non examiné | E4 `[HYPOTHÈSE D'INJUSTICE NON EXAMINÉE]` ; E3 (DÉLIBÉRATION) si la qualification est mobilisée dans une décision touchant des personnes |

**1.4 Connexions inter-fiches**

| **Connexion**           | **Description**                                                                                                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| → F2 (Mode milieu)           | R-CODEGRADATION et signal codegradation\_calculable (statut formel : F3 §3.5) sont activés si GENRE\_GELE\_PERSISTANT (F1) + MILIEU\_DEGRADE\_PERSISTANT (F2) simultanément. |
| → F5 (Évolutivité cognitive) | resistance\_cognitive\_revision peut rendre compte de la persistance de GENRE\_GELE\_PERSISTANT malgré les délibérations (lecture par AX-12, non explication causale établie). `modificateur_affectif` (F5) agit sur `seuildisposition` (C-GENRE-METIER) ; `signalversaffectif` (F5) alimente les signaux d'idéologie défensive. |
| → F6 (Justice)               | injustice\_epistemique HERMENEUTIQUE bloque DELIBERATION si type\_deliberation = REDEFINITION\_BUTS.                                                                         |
| → F7 (Mimétique)       | Si une réforme professionnelle se résout par désignation d'un métier-bouc-émissaire ou d'un manageur-coupable, R-VICTIME-EMISSAIRE est activée.                              |

### Fiche 2 — Mode milieu étendu

Localisation : Couche 2 — fiche opérationnelle Mode milieu.

**2.1 Objet et fondements théoriques**

La Fiche Mode milieu étendu réinstancie la règle R-CARE appliquée à la branche non-humain, R-CODEGRADATION (→ NT-G3), et C-MILIEU-VECU (texture vécue de l'habitabilité). Fondements : co-dégradations et care non-humain → NT-G3 ; milieu vécu, ontologies relationnelles et agentivité non-humaine → NT-G5 ; responsabilité envers le vivant → NT-G2 ; capabilités non-humaines → NT-G7.

**2.2 Champs nommés réintégrés**

Sous-couche C-MILIEU-VECU (Habitabilité du milieu)

| **Champ**                  | **Type**    | **Valeurs / Exemples**                             | **Description**                                                                  |
| -------------------------- | ----------- | -------------------------------------------------- | -------------------------------------------------------------------------------- |
| etat\_habitabilite\_milieu | Énumération | HABITABLE / FRAGILE / INHABITABLE                  | État synthétique de l'habitabilité du milieu non-humain                          |
| texture\_vecue             | Texte libre | ex. zone humide en voie d'assèchement              | Description qualitative de la texture vécue du milieu                            |
| indicateurs\_biophysiques  | Liste DID   | \[did:capteur:turbidite-X, did:satellite:image-Y\] | Indicateurs biophysiques actifs (Annexe H.3 dMRV)                                |
| seuil\_alerte\_milieu      | Nombre      | ex. 0.3                                            | Seuil d'alerte du valorimètre BIOPHYSIQUE déclenchant MILIEU\_DEGRADE\_PERSISTANT |
| obligation\_preservation   | Texte       | ex. maintien de la zone humide                     | Obligation de préservation juridiquement ou moralement contraignante             |
| milieu\_uri                | DID         | did:registre:milieux:zone-humide-x                 | DID du milieu concerné — peut être un consortium multi-parties (Annexe H.5)      |

Règle R-CARE — 4 défis (branche non-humain)

| **Champ**                     | **Type**       | **Valeurs / Exemples**                                | **Description**                                                                   |
| ----------------------------- | -------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------- |
| defi\_inventaire\_milieu      | Texte          | Entités non-humaines recensées                        | Défi 1 — Inventaire : génère écriture C-MILIEU                                    |
| type\_operation\_care\_milieu | Énumération    | SURVEILLANCE / RESTAURATION / PREVENTION / PROTECTION | Défi 2 — Opérations : type d'opération de care exercée sur le milieu              |
| cout\_care\_milieu            | DID valorimètre | did:valuemetre:biophysique-x                          | Défi 3 — Coûts : DID du valorimètre BIOPHYSIQUE mesurant le coût du care           |
| defi\_attribution\_milieu     | DID acteur     | DID acteur responsable                                | Défi 4 — Attribution : acteur responsable du care du milieu (tracé dans C-DROITS) |
| soin\_avec\_milieu            | Booléen        | VRAI / FAUX                                           | Précondition SOIN\_AVEC milieu : la pratique de soin est-elle co-construite ?     |

Signal composite R-CODEGRADATION (→ NT-G3) — calculable

| **Champ**                        | **Type**           | **Valeurs / Exemples**                                                | **Description**                                                                                                               |
| -------------------------------- | ------------------ | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| signal\_codegradation            | Signal composite   | GENRE\_GELE\_PERSISTANT + MILIEU\_DEGRADE\_PERSISTANT simultanés      | Détecte la co-dégradation structurelle travail de care / milieu non-humain                                                    |
| intensite\_codegradation         | Score 1-3          | 1 (faible) / 2 (modérée) / 3 (structurelle)                           | Intensité de la co-dégradation diagnostiquée                                                                                  |
| lien\_causal\_codegradation      | Texte              | ex. externalisation du care = externalisation des coûts sur le milieu | Description du lien causal entre dégradation du travail et du milieu                                                          |
| codegradation\_2morphisme | Référence F3 §3.5 | lien\_2morph:M-TRAVAIL→M-MILIEU                                       | Le 2-morphisme dans la bicatégorie Mode rendant la corrélation calculable (F3 §3.5, signal codegradation\_calculable) |

**2.3 Connexions C-SIGNAL et règles activées**

| **Signal C-SIGNAL**              | **Condition de déclenchement**                                                               | **Action / Phase C-ENQUETE-V5**                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| MILIEU\_DEGRADE\_PERSISTANT      | etat\_habitabilite\_milieu = FRAGILE / INHABITABLE sur 2 interactions ou indicateur \< seuil | Déclenche C-SANCTIONS (MILIEU\_DEGRADE\_PERSISTANT) + phase AUTOGOUVERNANCE        |
| R-CODEGRADATION                  | GENRE\_GELE\_PERSISTANT (F1) ET MILIEU\_DEGRADE\_PERSISTANT simultanés                       | Déclenche REVISION\_PROXIMATE\_ULTIMATE + alerte grammaire Responsabilité          |
| codegradation\_calculable        | 2-morphisme M-TRAVAIL → M-MILIEU propage dégradations corrélées (statut formel : F3 §3.5)                   | Traitement conjoint formellement justifié — révision dispositifs travail et milieu |
| OBLIGATION\_PRESERVATION\_VIOLEE | obligation\_preservation non nulle ET etat\_habitabilite\_milieu = INHABITABLE               | Déclenche DÉBIT vers acteur responsable (C-DROITS) + signal vers C-MEMOIRE-PERTES  |
| SOIN\_AVEC\_MILIEU\_ABSENT       | soin\_avec\_milieu = FAUX ET type\_operation = SURVEILLANCE                                  | Alerte sous-qualité de care + délibération dans C-ENQUETE-V5                       |

**2.4 Connexions inter-fiches**

| **Connexion**           | **Description**                                                                                                                                                       |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| → F1 (Mode travail)          | R-CODEGRADATION est l'interface principale entre les deux fiches ; le 2-morphisme la rend calculable.                                                            |
| → F4 (Mode existentiel)      | etat\_habitabilite\_milieu = INHABITABLE active appel\_immanent (→ NT-G2).                                                                                            |
| → F5 (Évolutivité cognitive) | praticabilite\_cognitive = IMPRATICABLE peut expliquer l'échec de dispositifs de protection du milieu.                                                              |
| → F7 (Mimétique)       | Si la dégradation d'un milieu est attribuée à une espèce-bouc-émissaire (ex. ragondin, loup) plutôt qu'à des structures systémiques, R-VICTIME-EMISSAIRE est activée. |

### Fiche 3 — Mode sémantique étendu

Localisation : Couche 2 — fiche opérationnelle Mode sémantique.

**3.1 Objet et fondements théoriques**

La Fiche Mode sémantique étendu réinstancie les trois couches de la branche sémantique : C-RIS (Registre d'Interactions Sémantiques), C-TCFP (Treillis de Concepts Formels Pondérés) et C-INSCRIPTION-CORPUS. S'y ajoute la sous-couche C-2MORPHISME-INTER-CORPUS (statut formel : §3.5). Fondements : analyse formelle de concepts → Annexe méthodologique ; attracteurs culturels → NT-G1 ; injustice herméneutique → NT-G7 ; savoirs situés et performativité → NT-G4.

**3.2 Champs nommés réintégrés**

Sous-couche C-RIS (Registre d'Interactions Sémantiques)

| **Champ**                       | **Type**      | **Valeurs / Exemples**                             | **Description**                                                                    |
| ------------------------------- | ------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------- |
| type\_acteur\_semantique        | Énumération   | TOKEN / CONCEPT / CATEGORIE / CADRE                | Type d'acteur sémantique engagé dans l'interaction                                 |
| stade\_constitution\_semantique | Énumération   | EMERGENT / EN\_COURS / STABILISE / CONTESTE        | Stade de constitution sémantique du concept ou catégorie                           |
| valuemetre\_semantique\_actif   | DID           | did:valuemetre:semantique-x                        | DID du valorimètre sémantique actif                                                 |
| asymetrie\_DEBIT\_CREDIT        | Score -5 à +5 | \-5 (asymétrie forte défavorable) à +5 (favorable) | Asymétrie DÉBIT / CRÉDIT sémantique                                                |
| appel\_entendu\_semantique      | Booléen       | VRAI / FAUX                                        | L'appel du token marginal a-t-il été entendu dans la constitution du sens commun ? |
| regime\_metabolique\_actif      | Énumération   | CONSTRUCTIF / REPRODUCTIF / DESTRUCTIF             | Régime métabolique de l'interaction sémantique                                     |

Sous-couche C-TCFP (Treillis de Concepts Formels Pondérés)

| **Champ**                              | **Type**    | **Valeurs / Exemples**                                | **Description**                                              |
| -------------------------------------- | ----------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| plage\_stabilite\_theta\_min           | Nombre      | 0 à 1                                                 | Borne inférieure de la plage de stabilité                    |
| plage\_stabilite\_theta\_max           | Nombre      | 0 à 1                                                 | Borne supérieure de la plage de stabilité                    |
| solidite\_tcfp                         | Score 1-5   | 1 (très fragile) à 5 (très solide)                    | Solidité du concept dans le treillis (fréquence + consensus) |
| reversibilite\_tcfp                    | Énumération | REVERSIBLE / PARTIELLEMENT\_REVERSIBLE / IRREVERSIBLE | Réversibilité de la stabilisation du concept                 |
| risque\_defausse\_intergen\_semantique | Booléen     | VRAI / FAUX                                           | Risque de défausse sémantique intergénérationnelle           |
| etat\_habitabilite\_semantique         | Énumération | HABITABLE / FRAGILE / INHABITABLE                     | État d'habitabilité sémantique pour les locuteurs marginaux  |
| extension\_uri                         | Liste DID   | \[did:objet:1, did:objet:2\]                          | Extension du concept : liste des DIDs d'objets couverts      |
| intension\_uri                         | Liste DID   | \[did:propriete:1, …\]                                | Intension du concept                                         |

Sous-couche C-INSCRIPTION-CORPUS (Légitimité politique du corpus)

| **Champ**                               | **Type**     | **Valeurs / Exemples**                                                           | **Description**                                                           |
| --------------------------------------- | ------------ | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| regime\_inscription\_corpus             | Liste énumérée | AUTOGOUVERNANCE / ENQUETE\_OBSERVATIONNELLE / ENQUETE\_COLLECTIVE / DELIBERATION ; une combinaison se déclare comme plusieurs valeurs, sans valeur composite | Régime(s) d'inscription du corpus (liste depuis le 12/10/2026 ; RECHERCHE\_INTERVENTION n'est pas une valeur mais une phase de C-ENQUETE-V5, §B.2ter) |
| consentement\_explicitation\_corpus     | Booléen (dérivé) | VRAI si et seulement si chaque personne de `perimetre_declare_corpus` figure dans `consentements_attestes` ; périmètre non déclaré : aucune valeur, marqueur `[PÉRIMÈTRE NON DÉCLARÉ]` | Les personnes concernées ont-elles toutes consenti à l'explicitation de leur corpus ? (dérivé depuis le 12/10/2026 ; PR-56) |
| consentements\_attestes                 | Liste DID + VC | \[(DID personne, VC de consentement, date)\] ; consentement obtenu après coup admis | Consentement attesté, personne par personne (Annexe H.2) |
| recherche\_consentement                 | Par personne | tentatives (date, canal) ; attestation de l'instance de contrôle (PR-43) ; contestation retenue (VRAI / FAUX) | Trace de la recherche du consentement d'une personne déclarée en « recherche infructueuse » ; **opposable** si au moins une tentative datée avec son canal **ou** une attestation de l'instance, et aucune contestation retenue (la personne s'est manifestée, ou la recherche est démentie) |
| mode\_validation\_concept               | Énumération  | CONSENSUEL / MAJORITAIRE / EXPERTAL / CONTESTE                                   | Mode de validation du concept dans le corpus                              |
| refus\_inscription\_corpus              | Trace datée, sans contenu | date ; DID du porteur de l'inscription ; `mode_validation_concept` déclaré ; DID des personnes non couvertes ; `recherche_consentement` | Existence d'une tentative d'inscription refusée au titre de CORPUS\_NON\_CONSENTI (patron `NONCOLLECTE`, CONV-20) ; citée par toute nouvelle inscription du même corpus (`[LACUNE]` : critère d'identité du corpus) |
| motif\_changement\_mode                  | Texte + DID  | motif ; porteur                                                                  | Requis si le mode diffère de celui de la tentative refusée ; sans motif, la condition se lit avec le mode de la tentative (NT-G4 §6bis) |
| contestation\_possible\_corpus          | Booléen      | VRAI / FAUX                                                                      | La contestation est-elle formellement possible ?                          |
| etres\_rendus\_visibles\_semantique     | Liste DID    | \[DID acteurs/entités\]                                                          | Êtres rendus visibles par le corpus sémantique                            |
| acteurs\_exclus\_conception\_semantique | Liste DID    | \[DID acteurs\]                                                                  | Acteurs exclus de la conception (injustice herméneutique potentielle)     |
| solidite\_politique                     | Score 1-5    | 1 (très fragile) à 5 (très solide)                                               | Solidité politique du corpus                                              |
| perimetre\_declare\_corpus              | Liste DID    | \[DID acteurs/entités\]                                                          | Acteurs et entités que le corpus (ou l'instrument qui le mobilise) déclare représenter ; non renseigné : marqueur `[PÉRIMÈTRE NON DÉCLARÉ]` |
| exclusion\_performative\_detectee        | Booléen (dérivé) | VRAI si perimetre\_declare\_corpus \\ etres\_rendus\_visibles\_semantique ≠ ∅ ; aucune valeur si le périmètre n'est pas déclaré (marqueur, non FAUX) | L'instrument écarte, par ses catégories ou ses règles, une partie de ce qu'il déclare représenter (→ NT-G4 §3.1bis ; Mitchell 2002) |

Sous-couche C-2MORPHISME-INTER-CORPUS (statut formel : §3.5)

| **Champ**                      | **Type**     | **Valeurs / Exemples**          | **Description**                                                        |
| ------------------------------ | ------------ | ------------------------------- | ---------------------------------------------------------------------- |
| corpus\_source                 | DID corpus   | did:corpus:source               | Corpus source du 2-morphisme                                           |
| corpus\_cible                  | DID corpus   | did:corpus:cible                | Corpus cible du 2-morphisme                                            |
| inclusion\_floue               | Booléen      | VRAI / FAUX                     | M\_source(x,y) ≤ M\_cible(x,y) pour tout (x,y) ?                       |
| amplitude\_2morphisme          | Score 0-1    | 0 (égalité) à 1 (écart maximal) | Amplitude du 2-morphisme entre les deux profunctors                    |
| points\_glissement             | Liste paires | \[(x1,y1), (x2,y2)…\]           | Points (acteur, contexte) où l'écart est maximal                       |
| irreversibilite\_inter\_corpus | Booléen      | VRAI / FAUX                     | Le 2-morphisme inverse existe-t-il ? Si FAUX, irréversibilité formelle |

**3.3 Connexions C-SIGNAL et règles activées**

| **Signal C-SIGNAL**                | **Condition de déclenchement**                                                      | **Action / Phase C-ENQUETE-V5**                                         |
| ---------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| TOKEN\_MARGINAL\_NON\_ENTENDU      | appel\_entendu\_semantique = FAUX ET asymetrie\_DEBIT\_CREDIT \< -2                 | Phase ENQUÊTE + inscription C-MEMOIRE-PERTES                            |
| CONCEPT\_INHABITABLE               | etat\_habitabilite\_semantique = INHABITABLE                                        | REVISION\_PROXIMATE\_ULTIMATE + signal vers grammaire Justice (F6)      |
| DEFAUSSE\_SEMANTIQUE\_INTERGEN     | risque\_defausse\_intergen\_semantique = VRAI ET reversibilite\_tcfp = IRREVERSIBLE | Inscription C-MEMOIRE-PERTES + alerte grammaire Responsabilité (F4)     |
| CONCEPT\_POLITIQUEMENT\_FRAGILE    | solidite\_politique ≤ 2 ET contestation\_possible\_corpus = FAUX                    | Alerte corpus + phase DELIBERATION                                      |
| CORPUS\_NON\_CONSENTI              | consentement\_explicitation\_corpus = FAUX ET mode\_validation\_concept = EXPERTAL  | **Refus d'inscription du corpus entier** (E1, branche 1bis, Annexe §A.15.11 ; NT-G4 §6bis), sauf si chaque acteur est couvert : consentement attesté (VC, Annexe H.2), recueilli le cas échéant après l'explicitation, **ou** représentation des absents (F10 : absence admise — `absencestructurelle`, ou recherche infructueuse **opposable** au sens de `recherche_consentement` —, `mecanismesubstitution`, `porteurrepresentationabsents`). Le refus est tracé sans le corpus (`refus_inscription_corpus`) ; un consentement ultérieur fonde une nouvelle inscription, qui cite la trace ; un changement de `mode_validation_concept` non motivé n'est pas retenu. **Perte de couverture après inscription** (contestation retenue d'une absence, E7) : R-HERMENEUTIQUE (F6), blocage de DELIBERATION sur ce corpus (E6) jusqu'à couverture rétablie |
| carre\_non\_commutatif      | Écart **déclaré** entre les deux chemins du carré (chemin SVD / chemin FCA pondérée) ≥ seuil **déclaré** ; seuil non déclaré : marqueur, pas de signal (PR-50) | REVISION\_CONCEPTUELLE — réviser foncteur F = −log ou catégorie de base |
| boucle\_confirmante\_detectee | Boucle Mode → M-SEMANTIQUE → Mode (statut formel : §3.5 ; forme : PR-54)                      | Inscription du point fixe comme acteur, délibération obligatoire ; déclencheur de la phase RECHERCHE\_INTERVENTION (§B.2ter) |

**3.4 Connexions inter-fiches**

| **Connexion**           | **Description**                                                                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| → F5 (Évolutivité cognitive) | attracteur\_culturel cible les concepts stade\_constitution\_semantique = STABILISE avec solidite\_tcfp élevée.                                      |
| → F6 (Justice)               | acteurs\_exclus\_conception\_semantique déclenche type\_injustice\_epistemique = HERMENEUTIQUE. exclusion\_performative\_detectee = VRAI le déclenche aussi (NT-G4 §3.1bis, §4.2) : deux critères distincts — exclu comme auteur du corpus ; écarté de ce que le corpus déclare représenter. |
| → F4 (Mode existentiel)      | DEFAUSSE\_SEMANTIQUE\_INTERGEN active risque\_existentiel si entité vivante concernée.                                                               |
| → ProfReg (PR-50)            | `PR50_CarreNonCommutatif.lean` établit la **forme** du signal carre\_non\_commutatif, et elle seule : un signal levé atteste une non-commutation en ce point (`signal_implique_non_commutation`) ; un carré qui commute ne signale jamais (`commutatif_ne_signale_pas`) ; le signal **n'est pas** la non-commutativité — sous le seuil, un carré qui ne commute pas ne signale rien (`non_commutation_sous_le_seuil_ne_signale_pas`) ; le verdict dépend du seuil déclaré (`signal_temoin_discriminant`) et de l'écart déclaré (`le_signal_depend_de_l_ecart_declare`) : le choix de la mesure est une déclaration ; sans seuil déclaré, pas de signal mais un marqueur (`seuil_non_declare_ne_signale_pas`) ; l'action REVISION\_CONCEPTUELLE suit le signal (`action_temoin_discriminant`). **Restent hors ProfReg** : le calcul de l'écart SVD / FCA pondérée (les deux chemins y sont des fonctions quelconques), la sous-couche C-2MORPHISME-INTER-CORPUS, et la 2-cellule (horizon v6). Statut des autres objets formels invoqués par les fiches : §3.5. |
| → F10 (Démocratie épistémique) | La représentation des absents (`sujetsepistemiquesabsents`, `absencestructurelle`, `mecanismesubstitution`, `porteurrepresentationabsents`) est l'une des deux clés qui rendent inscriptible un corpus soumis à CORPUS\_NON\_CONSENTI ; elle ne couvre pas un acteur joignable qui n'a pas consenti (PR-55). |
| → ProfReg (PR-54, PR-55)     | `PR54_BoucleEtContrePerformativite.lean` établit la **forme** de `boucle_confirmante_detectee` et de sa lacune : le signal atteste un point fixe aligné (`boucle_confirmante_atteste_l_alignement`) ; une boucle contre-performative — effet contraire à l'intention, Unal et al. 2025, p. 20 — ne le lève jamais (`la_contre_performativite_ne_leve_pas_la_boucle`) ; l'effet d'hôte (§B.2bis, PR-34) voit un cas contraire (`l_effet_d_hote_voit_un_cas_contraire`) ; hors effet d'hôte, la contre-performativité n'est vue par aucun signal (`hors_hote_la_contre_performativite_est_invisible`) ; les signaux lisent des déclarations, non les faits (`le_registre_ne_lit_pas_l_hote_reel`, `un_hote_reel_declare_aucun_echappe`) ; témoins : `boucle_temoin_discriminant`, `desalignement_sans_hote_temoin`. `PR55_CorpusNonConsenti.lean` établit la forme de CORPUS\_NON\_CONSENTI : le signal lit le mode de validation (`corpus_non_consenti_lit_le_mode_de_validation`) ; la représentation ne couvre pas un acteur joignable (`la_representation_ne_couvre_pas_un_joignable`) ; **l'absence n'est jamais un verrou** (`l_absence_n_est_jamais_un_verrou`) ; les deux clés sont nécessaires (`les_deux_cles_sont_necessaires`) ; témoin : `corpus_signal_temoin_discriminant`. `[PÉREMPTION PARTIELLE]` PR-55 modélise un signal inscrit qui bloque la délibération jusqu'à la levée ; la règle en vigueur refuse l'inscription (NT-G4 §6bis) : la couverture (`couvert`, `leve`) en est la condition d'inscriptibilité, tandis que `le_changement_de_mode_ne_leve_pas` et `bloque_temoin_discriminant` ne valent plus que pour la perte de couverture après inscription ; la trace du refus et le changement de mode motivé sont sans théorème (Consolidé §2.1). `PR56_ConsentementEtAbsenceOpposable.lean` (importe PR-55) établit la forme du consentement par personne et de l'absence opposable : le consentement du corpus est dérivé (`le_consentement_du_corpus_est_derive`, témoin `consentement_derive_temoin`) ; une recherche sans trace ni attestation n'est pas une absence (`sans_trace_ni_attestation_pas_d_absence`) ; une contestation retenue fait tomber la représentation (`une_contestation_retenue_fait_tomber_la_representation`) ; la trace seule ou l'attestation seule suffit (`trace_ou_attestation_temoin`) ; PR-56 n'admet jamais plus de représentations que PR-55 (`pr56_restreint_pr55`) ; l'absence opposable n'est jamais un verrou (`l_absence_opposable_n_est_jamais_un_verrou`). |
| → F7 (Mimétique)       | Si un concept est désigné comme bouc-émissaire d'une dérive sémantique (ex. un mot « toxique » comme cause unique), R-VICTIME-EMISSAIRE est activée. |

**3.5 Statut formel des objets catégoriels invoqués par les fiches**

*Seul lieu du set qui dit, pour les objets catégoriels mobilisés par les fiches F1 à F8, ce que ProfReg établit et ce qui reste hors ProfReg. Les fiches y renvoient. Aucune section numérotée d'Annexe G n'est citée par les fiches : ces sections ne figurent pas dans le set. Les renvois à l'Annexe G §I.2 et §III.2 (§2ter) sont d'un autre ordre : ils portent sur des définitions de Couche 0, non sur des objets formels.*

| Objet | Fiches | Dans ProfReg | Hors ProfReg |
| :-- | :-- | :-- | :-- |
| Signal carre\_non\_commutatif | F3 | **Forme du signal** (PR-50, `PR50_CarreNonCommutatif.lean`) : deux chemins, écart déclaré, seuil déclaré ; voir §3.4 | Calcul de l'écart SVD / FCA pondérée ; niveaux MOYEN / CRITIQUE (Annexe K), dont les seuils restent à déclarer (CONV-9) |
| Signal boucle\_confirmante\_detectee | F3 | **Forme du signal et de sa lacune** (PR-54, `PR54_BoucleEtContrePerformativite.lean`) : point fixe aligné ; contre-performativité non vue ; levée partielle par l'effet d'hôte ; voir §3.4 | Structure de la boucle Mode → M-SEMANTIQUE → Mode (réduite à un booléen) ; détection générale du désalignement effet / intention — confiée à l'enquête (phase RECHERCHE\_INTERVENTION, §B.2ter ; forme du constat : PR-57) |
| 2-morphismes inter-corpus (C-2MORPHISME-INTER-CORPUS) | F3 | Rien | Bicatégorie des modes, inclusion floue, amplitude, irréversibilité inter-corpus |
| 2-morphisme M-TRAVAIL → M-MILIEU (codegradation\_2morphisme, codegradation\_calculable) | F1, F2 | Rien | Propagation calculée des dégradations corrélées : le signal est déclaré, non calculé |
| Catégorie indexée Exist ; catégorie ordonnée des horizons H ; effondrement\_existentiel\_calcul | F4, F8 | Le type `HorizonTemporel` et les théorèmes qui le mobilisent (`V10a_planetaire_force_deliberation`, `V10a_synthese`) | Calcul formel d'irréversibilité ; « calcul, non déclaration » s'entend comme calcul procédural |
| Projection π : V^CARE → V^IFRS | F8 | Rien | Projection et mesure de sa perte informationnelle |
| 2-cellule (carré triangulaire NT-G7 ↔ NT-G2 ↔ NT-ARCH) | Partie A, §8 | Rien : commutativité procédurale (CONV-2) | 2-cellule complète, horizon v6 |

*Condition de révision.* Une ligne passe de « hors ProfReg » à « dans ProfReg » par versement d'un module compilé et audité, et seulement ainsi. *Porteur :* porteur MRC / responsable ProfReg. *Horizon :* v6 pour la 2-cellule ; non daté pour les autres.

### Fiche 4 — Mode existentiel étendu

Localisation : Couche 2 — fiche opérationnelle Mode existentiel.

**4.1 Objet et fondements théoriques**

La Fiche Mode existentiel étendu réinstancie les deux couches jonasiennes : C-FINALITE-IMMANENTE (téléologie propre des entités vivantes) et C-SUJET-COLLECTIF (responsabilité de l'espèce comme acteur). Elle rétablit la distinction entre appel\_entendu (réponse éthique ; **champ : `appel_entendu_milieu`, NT-G5** ) et appel\_immanent (→ NT-G2). Elle ajoute la sous-couche C-INDEXATION-HORIZON qui organise les écritures par horizons temporels indexés et rend l'irréversibilité jonasienne formellement calculable. Fondements : appel\_immanent / irréversibilité jonasienne → NT-G2 ; R-HERMENEUTIQUE → NT-G7.

**4.2 Champs nommés réintégrés**

Sous-couche C-FINALITE-IMMANENTE (Téléologie jonasienne)

| **Champ**                     | **Type**    | **Valeurs / Exemples**                                     | **Description**                                                                            |
| ----------------------------- | ----------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| finalite\_immanente           | Texte       | ex. maintien de l'intégrité cellulaire                     | Finalité propre de l'entité vivante, indépendamment de toute reconnaissance externe        |
| type\_finalite                | Énumération | AUTOCONSERVATION / REPRODUCTION / DEVELOPPEMENT / RELATION | Type de finalité immanente identifiée                                                      |
| vulnerabilite\_constitutive   | Score 1-5   | 1 (robuste) à 5 (très vulnérable)                          | Degré de vulnérabilité constitutive de l'entité                                            |
| obligation\_sans\_reciprocite | Booléen     | VRAI / FAUX                                                | L'obligation envers cette entité existe-t-elle sans attendre de réciprocité ?              |
| appel\_immanent               | Texte       | ex. appel à ne pas être détruit                            | Description de l'appel immanent, antérieur à toute réponse éthique                         |
| distinction\_appel\_entendu   | Booléen     | VRAI / FAUX                                                | L'appel\_immanent est-il distinct de  **`appel_entendu_milieu`**  ? VRAI pour activer R-INTERDIT-ABSOLU (→ NT-G2) |

Sous-couche C-SUJET-COLLECTIF (Responsabilité de l'espèce)

| **Champ**                         | **Type**                      | **Valeurs / Exemples**                                                 | **Description**                                                                                    |
| --------------------------------- | ----------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| niveau\_responsabilite            | Énumération                   | INDIVIDUEL / COLLECTIF / INSTITUTIONNEL / ESPECE                       | Niveau de responsabilité diagnostiqué                                                              |
| risque\_existentiel               | Énumération                   | ABSENT / POTENTIEL / IMMINENT / IRREVERSIBLE                           | Niveau de risque existentiel                                                                       |
| sujet\_responsable                | DID acteur collectif          | did:registre:espece:humaine                                            | Acteur collectif portant la responsabilité                                                         |
| horizon\_temporel\_responsabilite | Texte / référence H           | ex. 3 générations, 10 000 ans (lien vers C-INDEXATION-HORIZON)         | Horizon temporel de la responsabilité exercée                                                      |
| mecanisme\_porteur                | Texte                         | ex. traité international, droit des générations futures                | Mécanisme institutionnel portant la responsabilité                                                 |
| irreversibilite\_jonasienne       | Booléen + calcul Exist | VRAI / FAUX, calcul d'irréversibilité formelle dans Exist (statut formel : F3 §3.5) | L'acte ou l'omission est-il irréversible au sens de l'interdit absolu (→ NT-G2) ? Formellement calculable |
| principe\_precaution\_asymetrique | Booléen                       | VRAI / FAUX                                                            | Applique-t-on le principe de précaution asymétrique (pire scénario prioritaire) ?                  |

**4.2bis Extension de C-SUJET-COLLECTIF — le porteur qui porte pour d'autres**

*(Proposition P7 — `Lecture_Numero74_Meso-ESS_x_MRC_2026-09-14.md`. Instruction complète : `Decision_P7_Porteur_Collectif_Dimension_Pouvoir_2026-09-14.md`. Appui : Cousin & Audebrand 2026, d'après Huxham & Beech 2008.)*

> ### `[LA MOITIÉ DE P7 EST REJETÉE — non-réductibilité échouée]`
>
> P7 demandait un champ `type_porteur ∈ { PERSONNE / ORGANISATION / METAORGANISATION / ECOSYSTEME / NON_DECLARE }`. **Il est rejeté au titre de la règle §A.9.** `niveau_responsabilite` (ci-dessus, même sous-couche) type déjà le porteur — `INDIVIDUEL / COLLECTIF / INSTITUTIONNEL / ESPECE` — et quatre des cinq valeurs proposées s'y rabattent. Verser un second typage parallèle du même objet serait un **duplicat de champ**, défaut dont le set porte un précédent : `type_capabilité_centrale`, **duplicat de NT-G7 traité en F6.2**. *On ne répare pas une typologie insuffisante en lui en juxtaposant une seconde.*
>
> **Ce qui manque n'est pas un type de porteur, mais une propriété de la relation d'attribution** : le porteur porte-t-il **pour d'autres acteurs du registre** ? `INSTITUTIONNEL` ne le dit pas — une entreprise et une fédération y tombent ensemble. C'est ce que les deux champs ci-dessous inscrivent, et c'est la seule moitié de P7 qui franchisse §A.9.

**4.2bis.1 Champs**

| **Champ** | **Type** | **Valeurs / Exemples** | **Description** |
| --- | --- | --- | --- |
| porteur\_represente\_des\_membres | Énumération | VRAI / FAUX / **NON\_DECLARE** (défaut) | Le porteur désigné porte-t-il l'obligation pour des acteurs qui sont eux-mêmes inscrits au registre ? |
| membres\_representes | Liste DID | \[did:acteur:…\] | Obligatoire et non vide si VRAI. Jamais une catégorie générique — même exigence que `sujet_responsable` |
| dimension\_pouvoir | **Liste** de valeurs, **non exclusives** | AVEC / SUR / DE — au moins une si VRAI | Dimensions de pouvoir effectivement exercées par le porteur sur, avec, ou indépendamment de ses membres |
| PORTEUR\_COLLECTIF\_SANS\_DIMENSION\_DECLAREE | Signal | VRAI / FAUX | Déclenché par la condition 4.2bis.3 |

**4.2bis.2 Les trois dimensions — définitions retenues**

| Valeur | Définition opérationnelle | Ce que la déclaration rend opposable |
| --- | --- | --- |
| **AVEC** | Le porteur atteint ses objectifs **en collaboration** avec ses membres — « collaboration encapacitante aux côtés d'autres acteurs » | Un membre peut opposer au porteur une décision prise **sans** lui |
| **SUR** | Le porteur atteint ses objectifs en exerçant un **contrôle** sur ses membres — « coercition, domination, manipulation, ou subjectivisation » | Un membre peut opposer que l'obligation attribuée **retombe sur lui** sans qu'il ait été partie à l'attribution |
| **DE** | Le porteur agit en **autonomie relative** vis-à-vis de ses membres — l'« agence » de l'entité | Un tiers peut opposer au porteur un acte propre, que les membres n'ont ni décidé ni couvert |

> `[CORRECTION DE P7 — les trois dimensions ne sont pas exclusives.]` P7 écrivait `dimension_pouvoir ∈ { AVEC / SUR / DE }`, c'est-à-dire un choix unique. **La source dit l'inverse** : « trois dimensions de pouvoir **distinctes et complémentaires** », et le résultat empirique de l'article est précisément qu'une métaorganisation fait les trois — elle « accompagne, structure, mais aussi contraint et se réapproprie les dynamiques ascendantes de ses membres ». **Une énumération exclusive aurait falsifié la source en l'important.** Le champ est donc une **liste**.

**4.2bis.3 Condition de bonne formation — et pourquoi ce n'est pas une modification de Couche 1**

> **Une écriture qui attribue une obligation à un porteur n'est bien formée que si `porteur_represente_des_membres` est renseigné ; et, s'il vaut VRAI, que si `membres_representes` est non vide et `dimension_pouvoir` porte au moins une valeur.** À défaut : `PORTEUR_COLLECTIF_SANS_DIMENSION_DECLAREE = VRAI`, écriture mal formée, phase **DÉLIBÉRATION**. *Ancrage PR-31 :* `representant_sans_dimension_mal_forme`, `P7_temoin_discriminant`, `la_lecture_exclusive_ne_porte_pas_deux_dimensions` (AVEC et SUR ensemble : aucune valeur unique ne les porte). La phase DÉLIBÉRATION n'est pas modélisée.

P7 présentait son objet comme « un enjeu de Couche 1, pas d'ergonomie », au motif que la machine d'états exige que la DÉLIBÉRATION **produise un porteur** (`ATTRIBUEE`) avant que `CRITIQUE` soit mobilisable. **Le constat est juste, la conséquence ne l'est pas.** §8quater établit le patron : *une obligation s'écrit comme condition de bonne formation* — le contrôle porte alors sur l'écriture, et **n'a besoin ni d'un signal de Couche 1, ni d'une transition nouvelle**. La machine d'états est **inchangée** : ce qui change est ce qu'une écriture d'attribution doit porter pour en être une.

**Homologue déclaré.** C'est exactement la figure de la règle du **seuil d'entrée** (amendement A1 révisé des grammaires, NT-G2 §2.1 — *non l'axiome AX-1* ) : `obligationrelationnelle_declaree = VRAI` ne peut être inscrit que si `seuilentreecommunautemorale ≠ NONDECLARE`. Là, le set exige de déclarer **qui entre dans la communauté morale** avant d'inscrire une obligation envers elle ; ici, il exige de déclarer **sur qui l'obligation retombe** avant de l'attribuer. **Même exigence, autre bout de la relation.**

**Ce que la condition ne fait pas, et qu'il faut dire.** `NON_DECLARE` **ne bloque pas l'inscription de l'obligation** — le `[CHANGEMENT DE BASE TRACÉ]` tient : l'obligation relationnelle est première, le porteur secondaire et optionnel à l'inscription. La condition ne mord qu'au moment de l'**attribution**. *Elle ne crée pas le porteur manquant ; elle empêche de tenir pour attribué ce dont on ignore sur qui il retombe.*

**4.2bis.4 Le test d'opposabilité que P7 posait comme condition de rejet**

P7 posait sa propre contrepartie : *« Si l'importation faisait glisser le porteur MRC — catégorie juridico-comptable — vers une catégorie organisationnelle, il faudrait la rejeter. Le test : la déclaration doit rester opposable au sens de RSO-1. »*

**Le test est conduit, et c'est lui qui a commandé la forme retenue.** `type_porteur` aurait importé une **catégorie organisationnelle** — métaorganisation, écosystème — c'est-à-dire précisément le glissement que P7 s'interdisait ; c'est un second motif de son rejet, indépendant de la réductibilité. `porteur_represente_des_membres` est en revanche une **propriété de la structure de l'obligation** : elle ne dit pas ce que le porteur *est* (fédération, réseau, union), elle dit pour qui il *porte*. **Juridico-comptable, non organisationnelle.**

**Opposabilité, au sens de RSO-1 — la déclaration change ce qui est opposable, et à qui.** Colonne 3 du tableau 4.2bis.2 : chaque valeur ouvre une prise nommée à un acteur nommé. Sans elle, une obligation attribuée à un porteur qui exerce un pouvoir `SUR` retombe sur des membres **qui n'ont été ni partie à l'attribution ni désignés par elle** — et rien, au registre, ne le rend contestable.

**4.2bis.5 Garde-fous**

1. **Déclarer `SUR` n'est pas une accusation.** Les trois dimensions sont complémentaires et l'exercice d'un contrôle est constitutif d'une organisation faîtière. Lire `SUR` comme un signal d'injustice serait confondre cette sous-couche avec **C-POUVOIR** (F6), qui traite l'asymétrie *abusive* — `violence_symbolique`, `parite_participation`. **Les deux ne se remplacent pas** : C-POUVOIR détecte un défaut, `dimension_pouvoir` déclare un exercice.
2. **La déclaration ne transfère rien.** Le porteur reste le porteur ; déclarer que l'obligation retombe sur des membres ne les rend pas porteurs, et ne dispense pas d'un DID de porteur.
3. **Aucune dispense d'invariant.** `NON_DECLARE`, `FAUX`, ou l'une quelconque des dimensions ne dispense d'aucun invariant de Couche 1 : ni R1, ni la machine d'états, ni l'exigence de porteur identifié.
4. **Rien ne se calcule.** Aucun score, aucun seuil, aucun indice de « concentration de pouvoir ». Agréger les `dimension_pouvoir` d'un espace pour en tirer une mesure serait un `[DÉCOUPLAGE DE RÉGIMES]` — même clause qu'en §8.2bis (F8).

**4.2bis.6 Conditions de réfutation**

*Des champs.* Ils tombent si, sur cas documentés, la déclaration d'une dimension de pouvoir ne change **rien à ce qui est opposable, ni à qui** — l'exigence serait alors un `[ENGAGEMENT SANS SYMÉTRIE]`, et RSO-1 ne la couvrirait pas. *Rattachement AX-4 :* l'opposabilité suppose au moins l'état `convocable` ; une déclaration que les membres ne peuvent pas convoquer ne réfute ni n'établit rien.

*De la distinction elle-même.* `porteur_represente_des_membres` est **indécidable et doit être révisé** si l'on ne peut pas trancher, sans arbitraire, entre un porteur qui porte pour des membres et un porteur qui porte pour lui-même — par exemple lorsque les membres ne sont pas inscrits au registre, ou lorsque la représentation est de fait et non de statut. *(Patron homologue à `violence_symbolique`, NT-G7 §3.1.)*

**4.2bis.7 Critère de vérification — non satisfait**

 P7 demandait « l'écriture d'un cas où le porteur attribué est une fédération, et vérification que `dimension_pouvoir` change ce qui est opposable, et à qui ». **Le cas documenté existe** — l'Union pour le Réemploi Solidaire (URS), chez Cordrie, Grassart & Bayard —, **l'écriture n'est pas faite.** Elle appelle de connaître les statuts de l'URS et la composition de sa gouvernance, que l'article ne donne pas. Le corpus d'entretiens semi-directifs en cours de constitution se prête à ce contrôle : la question « qui décide, et pour qui portez-vous ? » est une question d'entretien. `[PLAUSIBLE, NON VÉRIFIÉ — appréciation d'applicabilité.]`

**4.2bis.8 Sources**

Cousin, L. & Audebrand, L. K., « Le pouvoir des métaorganisations de l'économie sociale et solidaire dans les espaces mésostratégiques », *Revue Interventions économiques*, n° 74, 2026, DOI 10.4000/15nae — VÉRIFIÉ (lecture directe du PDF décodé ; **pagination non disponible**, citations fiables au mot et non à la ponctuation fine). Définition retenue : le pouvoir d'une métaorganisation est « sa capacité à atteindre ses objectifs, que ce soit en collaboration (avec ses membres), de manière autonome (vis-à-vis de ses membres), ou en exerçant un contrôle (sur ses membres) ». — **Huxham, C. & Beech, N. (2008)**, source de la définition tridimensionnelle, et **Ahrne, G. & Brunsson, N. (2005, 2008)**, source de la notion de métaorganisation (« organisations dont les membres sont des organisations ») : **cités via Cousin & Audebrand uniquement** `[SOURCES NON VÉRIFIÉES de manière autonome — patron W-1d]`. **Le mot « métaorganisation » n'est pas versé au set** : seule la propriété qu'il servait à désigner l'est — ce qui borne la dette de source.

**4.2ter Le répartiteur — qui répartit une charge, et ce que la délibération doit produire**

*(Instruction : `Decision_P9_Verrou_Macro_x_Avaries_Communes_2026-09-14.md`. Appui : axiome **AX-3**, → Annexe **§A.18**.)*

> ### `[LE TROU QUE CETTE SOUS-SECTION COMBLE]`
>
> La machine d'états (§4) établit qu'une dette `SYSTEMIQUE_NON_ATTRIBUEE` est **forcée vers DELIBERATION**, et que `CRITIQUE` n'est atteignable qu'une fois l'obligation `ATTRIBUEE` — c'est l'un des résultats compilés du set (`nonattribuee_force_deliberation`, `cascade_deliberation_before_critique`, `critique_released_by_porteur`). **Elle exige donc que la délibération produise un porteur. Elle ne dit rien de ce qu'elle doit produire quand la charge se répartit entre plusieurs intéressés.**
>
> *Le registre sait exiger qu'on désigne qui porte. Il ne sait pas inscrire qui a réparti, ni selon quelle règle.* Tant que c'est le cas, une répartition entre intéressés est un fait extérieur au registre, que celui-ci enregistre par ses effets sans jamais pouvoir l'ouvrir à la contestation.

**4.2ter.1 Champs**

| **Champ** | **Type** | **Valeurs / Exemples** | **Description** |
| --- | --- | --- | --- |
| charge\_repartie | Énumération | VRAI / FAUX / **NON\_DECLARE** (défaut) | La charge de l'obligation est-elle répartie entre plusieurs intéressés, plutôt que portée par un porteur unique ? |
| porteur\_decision\_DID | DID acteur | did:… | Qui décide l'action dont la charge est répartie |
| porteur\_repartition\_DID | DID acteur | did:… | Qui applique la règle de répartition de cette charge |
| regle\_repartition | Texte structuré | formule ; barème ; ou **DECLARATION\_DE\_POSITION\_SANS\_FORMULE** | La règle appliquée, et le fait qu'elle ait été **posée avant** la décision ou non |
| interesses\_DID | Liste DID | \[did:acteur:…\] | Les intéressés entre lesquels la charge est répartie. Jamais une catégorie générique |

**4.2ter.2 Condition de bonne formation — et la séparation qui en est le contenu**

> **Condition complémentaire : le mandat du décideur est borné.** Si `charge_repartie = VRAI`, l'écriture n'est bien formée que si le mandat de `porteur_decision_DID` porte un **terme**, et si ce terme est **fixé par un porteur distinct du décideur** (champ `terme_mandat_decision` : date et DID de qui l'a fixé). À défaut : **aucune répartition** (PR-12, `sans_mandat_borne_aucune_repartition`, lecture ; témoin : `PR12_ne_qualifie_aucune_dette` — mandat borné et avarie qualifiée, la répartition produit un effet). *Source* : AX-9 — Machiavel, *Discours* I, 34-35 : le dictateur « n'était nommé que pour un temps limité », et une autorité non bornée cesse d'être institutionnelle. *Pourquoi ici et non en AX-3* : la condition ne qualifie pas **la perte** (AX-3, quatre conditions, §A.18.2), elle borne **celui qui a décidé** — elle appartient au découplage décideur / répartiteur.

> **Si `charge_repartie = VRAI`, l'écriture n'est bien formée que si les quatre champs suivants sont renseignés, et si `porteur_repartition_DID ≠ porteur_decision_DID`.** À défaut : écriture **mal formée**, phase **DÉLIBÉRATION**. *Appui compilé* : PR-27 `l_avarie_qualifiee_ne_suffit_pas` (une avarie qualifiée ne rend pas la répartition bien formée si le décideur répartit) et `le_repartiteur_non_nomme_ne_decouple_pas`.

**Ce que la non-égalité des deux DID inscrit.** C'est le contenu même d'AX-3 : *la décision de l'action de sauvetage et la règle de répartition de sa charge peuvent être séparées, la seconde posée a priori et indépendamment de la première.* Là où la séparation n'est pas opérée, « l'instrument qui détermine l'effort détermine simultanément sa répartition, et l'action collective se bloque sur l'arbitrage entre efficacité et équité ».

**Ce que la condition ne fait pas, et il faut le dire.** Elle **n'interdit pas** qu'un même acteur décide et répartisse — elle interdit de l'écrire sans le déclarer. Un acteur qui tient les deux rôles renseigne le même DID dans les deux champs : **l'écriture est alors mal formée, et c'est exactement le verdict voulu** — non parce que le cumul serait fautif, mais parce que le registre doit alors traiter la répartition comme non séparée, avec la conséquence qu'AX-3 attache à cette situation. *Le champ ne juge pas le cumul ; il empêche qu'il passe inaperçu.*

**`DECLARATION_DE_POSITION_SANS_FORMULE` est une valeur légitime, et c'est délibéré.** La transposition retenue par le porteur — `Application des avaries communes à TZCLD` — écarte le prorata monétaire et lui substitue une déclaration publique et révisable de position. Le répartiteur n'a alors **rien à calculer**, et le registre enregistre des positions déclarées, non des parts dues. **Cette valeur existe pour que ce cas s'inscrive comme tel plutôt que de ressembler à une absence de règle.** Sa conséquence est déclarée en 4.2ter.5.

**4.2ter.3 Non-réductibilité — test conduit contre §4.2bis (P7), dans les deux sens**

| | `porteur_represente_des_membres` (§4.2bis) | `porteur_repartition_DID` (ici) |
| --- | --- | --- |
| Ce que l'acteur fait | il **porte** l'obligation pour d'autres | il **ne porte rien** : il applique une règle entre des tiers |
| Ce qu'il doit à ceux qu'il touche | il répond de l'obligation devant eux | il répond de la **règle** et de son application |
| Ce que la déclaration ouvre | un membre oppose une décision prise sans lui | un intéressé oppose une part, ou l'absence de règle posée d'avance |

- *Sens 1.* Un porteur peut représenter des membres **sans rien répartir** — une fédération porte une obligation unique au nom des siens.
- *Sens 2.* Un répartiteur peut répartir **sans représenter personne** — c'est même la condition de son office : la dispatche maritime n'est mandatée par aucun des intéressés.

**Indépendance établie dans les deux sens.** Les deux sous-sections traitent deux moments distincts de l'attribution : **qui porte** (§4.2bis), **qui répartit** (§4.2ter).

**4.2ter.4 Garde-fous**

1. **Le registre n'est pas désigné répartiteur.** L'assignation « le registre est la dispatche » est une construction de note (`ProfReg/Avarie_commune_A2_P6prime_2026-09-07.md`, §3a, qui la déclare telle) et **n'est pas inscrite ici**. La présente sous-section fait l'inverse d'une assignation : elle **oblige à nommer** qui répartit — le registre compris s'il le fait, et alors sous son DID.
2. **Aucun calcul, aucune formule imposée.** `regle_repartition` est un champ **déclaré**. Le registre n'évalue ni la justesse de la règle ni l'exactitude des parts ; il inscrit quelle règle a été appliquée, par qui, et si elle était posée d'avance. Calculer une part à la place du répartiteur ferait du registre la dispatche souveraine — ce que le garde-fou 1 écarte.
3. **Aucune dispense d'invariant.** `charge_repartie = NON_DECLARE` ou `FAUX` ne dispense d'aucun invariant de Couche 1, ni de l'exigence de porteur, ni de la machine d'états.
4. **La répartition ne vaut pas quittance.** Inscrire qu'une charge a été répartie **n'éteint aucune obligation** — le set ne dispose d'aucun état terminal (→ 4.2ter.5). Lire une répartition inscrite comme un solde serait un `[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ]`.
5. **AX-3 ne s'invoque pas sans sa contre-partie.** L'axiome **conserve la distribution des richesses par construction** (→ §A.18.7) ; toute mobilisation de ces champs dans un dispositif de solidarité doit porter la scission **solidarité / réparation**, jamais fusionnées.

**4.2ter.5 Ce que cette sous-section laisse ouvert — deux questions, dont une engage la Couche 1**

> `[DÉCOUPLE SANS CLORE — constat repris et inscrit.]` Avec `DECLARATION_DE_POSITION_SANS_FORMULE`, il n'y a **ni parts, ni taux, donc aucune clôture vérifiable de l'épisode**. La séparation des deux rôles est inscrite ; la fin de la répartition ne l'est pas. *C'est le prix, assumé, du renoncement au prorata monétaire.*

> §4 porte quatre transitions et aucune sortie ; les termes `ETEINTE`, *extinction de l'obligation*, *clôture de l'épisode* comptent **zéro occurrence** dans le set. **Le registre sait ouvrir une obligation, la faire délibérer, l'attribuer et la rendre critique ; il ne sait pas la refermer.** Lacune ou choix ? Les deux lectures sont tenables — un registre de communalité peut poser que rien ne s'éteint — **et le set ne dit pas laquelle il retient**.

**4.2ter.6 Conditions de réfutation**

*Des champs.* Ils tombent si, sur cas documentés, la déclaration du répartiteur et de sa règle ne change **rien à ce qui est contestable, ni par qui** — l'exigence serait un `[ENGAGEMENT SANS SYMÉTRIE]`. *Rattachement AX-4 :* la contestation suppose l'état `convocable`, non `visible`.

*De la distinction elle-même.* `charge_repartie` est **indécidable et doit être révisé** si l'on ne peut trancher, sans arbitraire, entre une charge répartie entre intéressés et une charge portée par un porteur unique qui se finance auprès de tiers. *(Patron homologue à `violence_symbolique`, NT-G7 §3.1.)*

*De l'axiome qui les fonde.* **AX-3 tombe si, sur les cas étudiés, la séparation du décideur et du répartiteur ne produit aucune différence observable** sur les décisions prises, les contributions versées ou l'acceptabilité de l'action (→ §A.18.5). **Ces champs tombent avec lui** — et ils en sont l'instrument de test.

**4.2ter.7 Critère de vérification — non satisfait**

 Le cas documenté existe et il est celui du porteur : la « dispatche territoriale de l'emploi » de `Application des avaries communes à TZCLD`, avec son fonds à deux compartiments et son assiette de sauvegarde `W_i`. **L'écriture n'est pas faite.** Elle est le premier test disponible, et elle ne dépend d'aucune source à acquérir.

Sous-couche C-INDEXATION-HORIZON

| **Champ**                   | **Type**             | **Valeurs / Exemples**                                           | **Description**                                                                                  |
| --------------------------- | -------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| horizon\_h                  | Énumération ordonnée | INSTITUTIONNEL ≤ INTERGENERATIONNEL ≤ PROFOND ≤ PLANETAIRE   | Horizon temporel dans la catégorie ordonnée H (statut formel : F3 §3.5)                                       |
| categorie\_base\_horizon\_h | DID catégorie        | did:registre:V:0-1 ou did:registre:V:R\_pos                      | Catégorie de base V\_h propre à l'horizon h                                                      |
| acteurs\_horizon\_h         | Liste DID            | \[DID acteurs à l'horizon h\]                                    | Acteurs définis à l'horizon h (peuvent être abstraits aux horizons longs)                        |
| foncteur\_changement\_h\_h2 | Référence            | phi:h→h'                                                         | Foncteur de changement de base vers un autre horizon                                             |
| effondrement\_calculable    | Booléen              | VRAI / FAUX                                                      | À l'horizon h, la catégorie de base V\_h admet-elle encore les acteurs de la décision actuelle ? |

**4.3 Connexions C-SIGNAL et règles activées**

| **Signal C-SIGNAL**                      | **Condition de déclenchement**                                        | **Action / Phase C-ENQUETE-V5**                                                       |
| ---------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| APPEL\_IMMANENT\_NON\_ENTENDU            | appel\_immanent non nul ET  **`appel_entendu_milieu` ∈ {`NON_ENTENDU`, `ENTENDU_ET_NON_ENTENDU`}** `[NT-G5 §3.1. Sur `INDECIDABLE_ATTESTE` : pas d'inscription de perte, phase ENQUÊTE avec le critère de résolution déclaré. Sur `NONDECLARE` : marqueur, jamais signal.]`  *ProfReg (PR-4) porte ce signal sous la forme d'une **projection booléenne déclarée** : `true` exactement sur les deux valeurs ci-dessus ; la projection ne distingue pas `ENTENDU`, `INDECIDABLE_ATTESTE` et `NONDECLARE`.* *Sur `INDECIDABLE_ATTESTE`, l'inventaire n'est pas déclenché : §5.1, décision du porteur.* | Phase ENQUÊTE + inscription C-MEMOIRE-PERTES                                          |
| RISQUE\_EXISTENTIEL\_IMMINENT            | risque\_existentiel = IMMINENT ou IRREVERSIBLE                        | principe\_precaution\_asymetrique = VRAI + REVISION\_PROXIMATE\_ULTIMATE obligatoire  |
| OBLIGATION\_SANS\_RECIPROCITE            | obligation\_sans\_reciprocite = VRAI ET sujet\_responsable absent     | Alerte vers C-DROITS : attribution obligatoire d'un sujet\_responsable                |
| IRREVERSIBILITE\_JONASIENNE              | irreversibilite\_jonasienne = VRAI                                    | Inscription C-MEMOIRE-PERTES + blocage de toute phase pouvant aggraver la perte       |
| effondrement\_existentiel\_calcul | À un horizon h, V\_h ne peut plus accueillir les acteurs (statut formel : F3 §3.5) | R-INTERDIT-ABSOLU déclenchée formellement — calcul, non déclaration                   |
| irreversibilite\_changement\_base | Un 1-morphisme vertical n'admet pas d'inverse à droite                | Inscription C-SOLIDITE comme IRREVERSIBLE — vérification consentement et délibération |

R-HERMENEUTIQUE comme précondition à la phase DELIBERATION : dans le mode existentiel, si type\_injustice\_epistemique = HERMENEUTIQUE avec niveau supérieur au seuil (Fiche 6), la phase DELIBERATION est formellement bloquée jusqu'à résolution de l'injustice. Cette précondition s'applique prioritairement lorsque les entités concernées ne peuvent pas parler en leur propre nom (entités non-humaines, générations futures).

**4.4 Connexions inter-fiches**

| **Connexion**           | **Description**                                                                                                                                                                                 |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| → F2 (Mode milieu)           | etat\_habitabilite\_milieu = INHABITABLE active appel\_immanent sur les entités vivantes.                                                                                                       |
| → F3 (Mode sémantique)       | DEFAUSSE\_SEMANTIQUE\_INTERGEN active risque\_existentiel si entité vivante concernée.                                                                                                          |
| → F6 (Justice)               | R-HERMENEUTIQUE est la précondition formelle à DELIBERATION dans les contextes existentiels.                                                                                                    |
| → F5 (Évolutivité cognitive) | principe\_precaution\_asymetrique est cognitivement difficile (biais de présent) ; praticabilite\_cognitive = DIFFICILE sur ce champ.                                                         |
| → F7 (Mimétique)       | Les crises existentielles (climat, IA) sont des terrains privilégiés du mécanisme victimaire : R-VICTIME-EMISSAIRE et R-MECONNAISSANCE doivent être activées en parallèle de R-INTERDIT-ABSOLU. |
| → F3 §3.5                    | C-INDEXATION-HORIZON et le calcul d'irréversibilité formelle invoquent une catégorie indexée Exist et une catégorie ordonnée d'horizons **non formalisées dans ProfReg** ; seul le type `HorizonTemporel` (institutionnel ≤ intergénérationnel ≤ profond ≤ planétaire) y est déclaré. Statut : F3 §3.5. |

### Fiche F8 — Mode comptable / capitaux

Localisation : Couche 2 — fiche opérationnelle Mode comptable étendu, articulant transversalement les fiches F1 à F4. F8 n'introduit pas un cinquième mode mais inscrit le geste comptable lui-même comme dispositif gouvernable de Couche 2.

Fondements : → NT-G12 (mouvements IFRS/PCG, comptabilité CARE, juste prix écologique, droit de la comptabilité publique, performativité des instruments).

#### 8.1 Objet et fondements théoriques

La Fiche F8 Mode comptable étendu introduit en Couche 2 le geste comptable comme dispositif d'inscription gouvernable. Elle ne crée pas un cinquième mode d'application au sens des fiches F1 à F4 — les acteurs et les enjeux qu'elle traite sont déjà couverts par les modes travail, milieu, sémantique et existentiel. Elle inscrit l'articulation comptable elle-même, c'est-à-dire le passage par une comptabilité tenue (en partie double), comme un acteur tracé du registre, soumis aux mêmes règles d'inscription, de signal et de gouvernance que les autres dispositifs.

Le besoin opérationnel à l'origine de F8 a été démontré empiriquement par l'application de bout en bout au cas K1 (Exploitation B CARE / IDEA4) en mai 2026. Ce cas a établi que la comptabilité CARE articule transversalement les quatre modes existants — capitaux humains (M-TRAVAIL), capitaux naturels (M-MILIEU), catégories comptables (M-SEMANTIQUE), engagements de long terme (M-EXISTENTIEL) — et que cette articulation est elle-même un objet de gouvernance. Le cas K3 (bassins versants Lac Togo, Niayes, Drôme), traité ultérieurement, a confirmé cette transversalité pour le mode milieu pur et a fait apparaître un quatrième périmètre — la comptabilité territoriale de bassin — qui partage la même structure.

F8 adopte une architecture en trois couches articulées qui distingue clairement ce qui est mathématiquement invariant à tout régime comptable, ce qui dépend du régime adopté (IFRS, PCG, CARE, gestion, autres), et ce qui relève du typage ontologique propre au MRC (grammaire P-C-E-D-e-d).

> **Ancrage de l'architecture multi-régime.** Le choix de traiter le régime comptable comme une *variable déclarée* (`C-MOUVEMENT-TYPE.R`) et non comme un donné neutre opérationnalise une thèse de sociologie comptable dont l'ancrage et les sources sont portés par les grammaires : → NT-G12 (G-VALUATION — sociologie des régimes comptables, financiarisation par le choix de référentiel, origine comptable des catégories économiques) et → NT-G4 (G-PERFORMATIVITE — performativité des instruments comptables et garde-fou de réflexivité du registre). Renvoi croisé : le traitement du PIB comme régime dans `.R` (non l'invariant `.M`) et le découplage financement public / PIB relèvent du chantier macro (hors set, horizon v6).

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Principe directeur — F8 encadre, mais ne prétend pas articuler théoriquement les différents régimes comptables. Le verbe articuler suggérerait une théorie générale explicite que le droit positif ne fournit pas. F8 encadre la coexistence de plusieurs régimes — budgétaire, générale, analytique, comptabilité-matières en comptabilité publique ; financière, de gestion en comptabilité privée ; CARE, IIRC, LIFTS, comptabilité-action en comptabilités alternatives — chacun conservant sa logique propre , le MRC inscrivant les différentiels inter-régimes comme données opposables.** |

#### 8.1.1 Positionnement dans les trois régimes d'usage du MRC

L'actualisation de la note de cadrage (mai 2026) distingue trois régimes d'usage du MRC qui n'engagent pas la même fiabilité, ni les mêmes garanties techniques, ni les mêmes obligations juridiques. F8 est conçue comme dispositif principalement de l'Usage 3 (infrastructure notariée organisationnelle), mais avec des entrées explicites pour l'Usage 2 (registre d'enquête contrôlé). L'Usage 1 (grille heuristique LLM) n'est pas admissible pour les écritures comptables — voir la règle R-INCAPACITE-LLM-VALIDER (Couche 2, mode sémantique, K2) qui s'applique a fortiori aux mouvements typés P-C-E-D-e-d dont la subtilité ontologique excède la compétence de validation autonome d'un système probabiliste.

#### 8.2 Champs nommés réintégrés — vue d'ensemble

F8 est composée de **huit** sous-couches articulées. Les trois premières forment l'architecture C-MOUVEMENT-TYPE (couches Mathématique, Régime, Typage). Les cinq suivantes spécialisent F8 selon les régimes les plus utilisés et selon les exigences propres du MRC — dont **C-CLOTURE-ACCES** (§8.2bis), qui porte les conditions d'éligibilité sous lesquelles une écriture est faite.

> La ligne **« Connexions inter-fiches et inter-annexes »** de la table ci-dessous n'est pas une sous-couche : c'est la section §8.10. Elle figure dans la table comme entrée de lecture, mais elle **ne compte pas** parmi les huit sous-couches.

| **Sous-couche**                          | **Fonction**                                                                                                | **Source**                                                            |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| C-MOUVEMENT-TYPE.M                       | Les seize mouvements mathématiques invariants (→ NT-G12) sur l'équation A = D + S' + ΔS.                    | → NT-G12 (typologie des seize mouvements).            |
| C-MOUVEMENT-TYPE.R                       | Pour chacun des 16, traductions parallèles par régime comptable (IFRS, PCG, CARE, gestion).                 | Multi-source ; densifiée itérativement.                               |
| C-MOUVEMENT-TYPE.T                       | Typage P-C-E-D-e-d et règles miroir R1 raffinées.                                                           | Note synthétique MRC × CARE ; livrable K1 × K3.                       |
| C-COMPTABILITE-CARE                      | Spécialisation CARE : comptes étendus, valorimètre, amortissement écologique, articulation aux fiches F1-F4. | → NT-G12 (fondement CARE) ; cas K1. |
| C-CYCLE-PRIX                             | Cycle performatif du juste prix écologique (→ NT-G12) ; instance type du cycle e ↔ d.                       | → NT-G12 (juste prix écologique) ; cas K3 (proposition Defalvard sur la redevance Bercy). |
| C-PRIORITE-CREANCIERS                    | Implémentation de la règle R-PRIORITE-CREANCIERS (Couche 1) : ordonnancement du remboursement.              | Note de cadrage Piste 3 ; cas K1 et K3.                               |
| C-CLOTURE-ACCES                          | Conditions d'éligibilité de l'écriture : qui est exclu du périmètre, par quel dispositif, et quel accès en dépend (§8.2bis). | Proposition P2 ; appui : *Interventions économiques* 74, 2026. |
| C-SIGNAL.F8                              | Signaux propres au mode comptable.                                                                          | Conception F8 ; intègre signal\_translation\_manquante.     |
| Connexions inter-fiches et inter-annexes | Liens F8 → F1, F2, F3, F4, F7 ; renvoi à F3 §3.5 et à l'Annexe H.11.                                               | Architecture du set.                                  |

#### 8.2bis Sous-couche C-CLOTURE-ACCES — conditions d'éligibilité de l'écriture

 Origine : `Lecture_Numero74_Meso-ESS_x_MRC_2026-09-14.md`, proposition P2. **Domiciliation en F8, décision du porteur** — l'alternative, F6 (justice / droits), est écartée en raison du recouvrement avec `droit_exclusion` ; l'éligibilité est une **condition d'inscription**, objet propre de F8. La sous-couche domicilie la composante « clôture concurrentielle » de l'Annexe méthodologique §A.7, dimension de lecture sans domicile ailleurs.

**Ce que la sous-couche fait, et le geste n'est pas évident.** La clôture d'un espace n'est pas inscrite **comme propriété de l'espace** — le MRC n'a pas d'espace méso pour primitive, et lui en donner une serait un `[CHANGEMENT DE BASE NON TRACÉ]`. Elle est inscrite **comme condition d'une écriture** : toute écriture est faite sous un régime d'éligibilité, qui dit qui peut inscrire quoi et à quel titre. **L'espace se lit ensuite par agrégation** de ces conditions sur un périmètre construit par l'analyste, conformément au §A.7. C'est le seul chemin qui verse la clôture sans faire de l'espace méso une primitive.

**Deux champs, déclarés, jamais calculés.**

`cloture_declaree` — Texte structuré, triplet obligatoire : **{ qui est exclu du périmètre ; par quel dispositif ; qui a posé le dispositif }**. Le dispositif peut être un statut, un agrément, un label, un cahier des charges, un seuil d'éligibilité, une norme technique. Homologue de forme du quadruplet « statut du seuil » de R0-bis (→ Annexe §A.14) : ce qui est exigé n'est pas un jugement sur la clôture, c'est l'exhibition de ce qui la produit.

`enjeu_acces` — Énumération : **MARCHE / FINANCEMENT / COMMANDE-PUBLIQUE / AGREMENT / GISEMENT-MATIERE / RECONNAISSANCE / AUCUN / NON_DETERMINABLE**.

**Distinction obligatoire entre AUCUN et NON_DETERMINABLE.** `AUCUN` est un **résultat** : la frontière existe et ne commande aucun accès. `NON_DETERMINABLE` est un **état du matériau** : l'enquête ne permet pas de le dire. Les confondre inverse le sens de toute lecture agrégée — une colonne de `AUCUN` établit qu'un espace ne clôt rien ; une colonne de `NON_DETERMINABLE` n'établit rien du tout.

**Condition de bonne formation (niveau champ, non invariant de Couche 1).** Si `enjeu_acces` ∉ { AUCUN, NON_DETERMINABLE }, alors `cloture_declaree` est **obligatoire** : déclarer qu'un accès dépend d'une frontière sans dire quelle frontière barre qui est un défaut **E4** : l'écriture est inscrite, **mal formée**, et porte **`[CLÔTURE NON DÉCLARÉE]`**, avec horizon (branche 5 du critère, Annexe §A.15.11 ; le marqueur épistémique est réservé aux énoncés — piste 5). La réciproque n'est pas exigée — une clôture peut être déclarée sans qu'aucun accès n'en dépende, et c'est précisément le cas `AUCUN`.

**Test de non-réductibilité (règle de tri, Annexe §A.9).**

| Champ candidat au recouvrement | Écart |
| :-- | :-- |
| `droit_exclusion` (F6, faisceau Schlager-Ostrom) | Porte le **droit d'exclure d'une ressource**, détenu par les ayants droit d'un commun. `cloture_declaree` porte l'**exclusion d'un périmètre économique** et ne suppose ni ressource commune ni titulaire de droit. Un espace peut clore sans que personne n'y détienne de droit d'exclusion. |
| `source_valuemetre` (F8) | Exhibe l'origine d'un **instrument de mesure**, non les conditions d'accès à un périmètre. |
| `regime_comptable` (C-MOUVEMENT-TYPE.R) | Dit **sous quel régime** l'écriture est faite, non **qui a le droit** de la faire. |

Aucun des trois ne couvre les deux champs ; leur combinaison non plus. Le test est passé.

**Ce que la sous-couche ne fait pas.** Aucune primitive de Couche 0, aucun invariant de Couche 1, aucun signal, aucun valorimètre, aucun seuil. *L'absence de signal est conforme à la logique de F8 et non une omission* : les signaux de §8.9 sont rattachés aux **quatre lieux de tension** du dispositif comptable, non aux sous-couches une à une — C-MOUVEMENT-TYPE.M et C-MOUVEMENT-TYPE.T n'en portent pas davantage. De même, la condition de bonne formation ci-dessus est un **contrôle de champ**, du même genre que `respect_R1`, et non un signal. Rien ici ne se calcule et rien ne se déclenche. Les deux champs sont **descriptifs et déclarés**, au même titre que les autres champs de Couche 2, et leur agrégation en lecture méso reste une opération d'analyste, procédurale, jamais un indice. Les présenter comme une mesure du degré de clôture serait un `[DÉCOUPLAGE DE RÉGIMES]`.

**Contrepartie réfutable — et elle porte sur l'existence même de la sous-couche.** Si, sur un corpus instruit de bout en bout, `enjeu_acces` vaut `AUCUN` sur la quasi-totalité des écritures, alors le canal Produits-Concurrence est **inopérant pour ce corpus** et doit être déclaré tel, la sous-couche étant laissée vide plutôt que renseignée de force. Lamarche & Bastien admettent explicitement qu'un canal soit inopérant ; un canal inopérant est un résultat, non un échec de codage. Et si ce constat se répétait sur tous les corpus du MRC, **c'est la sous-couche qui serait à retirer**, non les corpus à changer.

*État de l'instructibilité.* Sur le registre de soin (579 fiches), les champs sont **probablement non renseignables sans retour aux matériaux sources** : « marché » y apparaît 2 fois, « concurrence » 1 fois. Sur un périmètre resserré, ils le sont : le cas de l'évaluation agro-environnementale documente une clôture disputée à enjeu matériel, et trois cas du numéro 74 d'*Interventions économiques* instruisent directement `enjeu_acces` — éligibilité ESS aux fonds réemploi (FINANCEMENT), collectivités sociétaires de SCIC (FINANCEMENT, COMMANDE-PUBLIQUE), don du surplus dans les AMEP (AUCUN, et les autrices écrivent qu'il n'y a pas de clôture de l'espace concurrentiel). **Le versement est donc gagé sur des cas existants, non sur une anticipation.**

*Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* renseignement effectif des deux champs sur au moins un périmètre resserré, avec au moins une valeur `AUCUN` **et** une valeur non nulle — faute de quoi la sous-couche n'aura pas montré qu'elle discrimine.

#### 8.3 Sous-couche C-MOUVEMENT-TYPE.M — couche mathématique invariante

Tout bilan obéit à l'équation fondamentale A = D + S' + ΔS, où A désigne l'actif, D les dettes, S' la situation nette hors résultat (capitaux propres avant l'exercice) et ΔS la variation de cette situation nette pendant l'exercice (résultat de l'exercice). Tout mouvement comptable se traduit par une variation simultanée de deux composantes de l'équation, dans le respect de l'égalité. La table source des seize combinaisons possibles (→ NT-G12) les énumère, qui sont régime-invariantes : tout régime comptable utilise tout ou partie de ces seize mouvements, avec des dénominations différentes.

Champs de la sous-couche C-MOUVEMENT-TYPE.M

| **Champ**                   | **Type**          | **Valeurs / Exemples**                         | **Description**                                                                           |
| --------------------------- | ----------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------- |
| sigle\_mouvement            | Énumération       | a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p | Sigle du mouvement type dans la typologie source (→ NT-G12). Régime-invariant.                                    |
| variations                  | Couple (X↑↓, Y↑↓) | (A↑, D↑), (A↓, ΔS↓)…                           | Couple des deux variations affectées sur (A, D, S', ΔS).                                  |
| description\_geometrique    | Texte             | ex. : augmentation simultanée de A et de D     | Description neutre de la nature géométrique du mouvement.                                 |
| exemple\_canonique\_richard | Texte             | ex. : achat d'un terrain à crédit              | Exemple canonique de la typologie source (→ NT-G12) pour ce mouvement, en IFRS / PCG.          |
| mouvement\_uri              | **Énumération fermée**  | a … p ; libellé lisible : did:registre:mouvement:richard:e | Identifiant du mouvement type, partagé par toutes ses traductions de régime. **La sous-couche M étant figée à seize valeurs (§8.3), il n'y a rien à résoudre : la désignation est l'énumération elle-même.** La forme `did:` est conservée comme libellé lisible, **non comme identifiant à résoudre**. |

Liste exhaustive des seize mouvements (couche M)

| **Sigle** | **Variations** | **Exemple canonique (IFRS / PCG)**                |
| --------- | -------------- | ------------------------------------------------- |
| a         | A↑ / A↓        | Achat terrain au comptant : terrain↑ caisse↓      |
| b         | D↑ / D↓        | Transformation dette fournisseur en effet à payer |
| c         | S'↑ / S'↓      | Incorporation de réserves au capital              |
| d         | ΔS↑ / ΔS↓      | Compensation interne au résultat                  |
| e         | A↑ / D↑        | Achat à crédit : terrain↑ dette↑                  |
| f         | A↓ / D↓        | Remboursement d'un emprunt : caisse↓ dette↓       |
| g         | A↑ / S'↑       | Apport en capital : caisse↑ capital↑              |
| h         | A↓ / S'↓       | Remboursement du capital aux associés             |
| i         | D↓ / S'↑       | Conversion d'une dette en capital                 |
| j         | D↑ / S'↓       | Distribution de réserves en dettes                |
| k         | A↑ / ΔS↑       | Vente comptant = produit                          |
| l         | A↓ / ΔS↓       | Charge payée comptant ; perte fortuite            |
| m         | D↓ / ΔS↑       | Remise de dette = produit exceptionnel            |
| n         | D↑ / ΔS↓       | Contravention non payée comptant                  |
| o         | S'↓ / ΔS↑      | Rectification d'erreur exercice précédent         |
| p         | S'↑ / ΔS↓      | Cas inverse de o                                  |

|                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Propriété d'invarianceLes seize mouvements ne supposent aucun régime particulier. Les exemples canoniques sont donnés en IFRS / PCG parce que c'est le périmètre du manuel source, mais la structure géométrique ne dépend pas du référentiel. La sous-couche M est donc figée par construction : aucun mouvement n'y est ajouté.** |

#### 8.3bis Le domaine de la sous-couche M — invariance de régime, non invariance d'entité

`[Décision du porteur. Source : contrôle de F8 au regard du postulat fondateur sur le domaine de M et la vocation de T (`Controle_Postulat_Domaine_M_et_T_2026-09-19.md`), §7.6.]`

L'encadré d'invariance ci-dessus dit vrai et ne dit pas tout. **Il établit l'invariance de régime — IFRS, PCG, CARE et la comptabilité de gestion donnent la même géométrie. Il n'établit aucune invariance d'entité, et il ne le peut pas.**

L'équation `A = D + S' + ΔS` présuppose deux objets qui n'existent que là où un surplus est calculé et affecté : **`S'`, la situation nette hors résultat, et `ΔS`, le résultat de l'exercice.** Une entité que l'on gouverne collectivement sans passer par une organisation dotée d'une comptabilité visant le calcul d'un profit ou d'un surplus **n'a ni `S'` ni `ΔS`** : ni capital, ni réserves, ni résultat à affecter.

**Conséquence, calculée sur la liste des seize.**

| | Mouvements | Statut pour une entité sans calcul de surplus |
| :-- | :-- | :-- |
| Portent sur `S'` | `c`, `g`, `h`, `i`, `j`, `o`, `p` (7) | **sans objet** |
| Portent sur `ΔS` | `d`, `k`, `l`, `m`, `n`, `o`, `p` (7, dont `o` et `p` déjà comptés) | **sans objet** |
| Ne mettent en jeu que des choses et des obligations | **`a`** (A↑/A↓), **`b`** (D↑/D↓), **`e`** (A↑/D↑), **`f`** (A↓/D↓) | disponibles |

**Douze des seize mouvements sont sans objet pour une entité qui ne calcule pas de surplus ; quatre seulement subsistent.**

**La source dit la même chose.** NT-G12 §2.2, bloc A : *« la comptabilité financière formalise un jeu fini de mouvements types et l'équation fondamentale du bilan »* (Richard, Bensadon & Rambaud 2018, table 6.1). **Le domaine que la source assigne à cette table est la comptabilité financière d'entreprise.** F8 en reprend la géométrie et le domaine, déclaré.

> **Ce que cette déclaration n'enlève pas.** La sous-couche M reste figée, complète et démontrée sur son domaine. Aucun mouvement n'est retiré. La **phrase « tout mouvement comptable »** en tête de §8.3 vaut pour tout mouvement d'une comptabilité tenue en partie double au service d'un calcul de surplus, et non pour toute inscription du registre. **L'inscription d'une entité sans comptabilité de surplus relève de la sous-couche T seule — voir §8.5.0.**

*Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* toute assertion de complétude portant sur M déclare le domaine sur lequel elle porte.

`[RÉSERVE DÉCLARÉE — le partage `S'` / `ΔS` n'a pas été instruit séparément. Une association tenant une comptabilité d'engagement a un résultat sans avoir de capital : pour elle, les sept mouvements de `ΔS` pourraient être disponibles et les sept de `S'` non. **Le décompte de douze vaut pour une entité qui n'a ni l'un ni l'autre ; un décompte intermédiaire reste à établir.**]`

#### 8.4 Sous-couche C-MOUVEMENT-TYPE.R — traductions par régime comptable

Pour chacun des seize mouvements de la couche M, la couche R fournit plusieurs traductions parallèles selon le régime comptable adopté. Chaque traduction est inscrite comme une écriture autonome qui partage le même sigle de mouvement mais diffère en dénomination, conditions de reconnaissance et compte d'imputation. Les régimes actuellement inscrits sont au nombre de quatre : IFRS, PCG, CARE et comptabilité de gestion. Trois régimes additionnels (→ NT-G12) sont projetés. La couche R est densifiée itérativement par l'inscription des cas d'usage de l'annexe K du set (`MRC_v5.7_Annexe_K_Cas_Chiffres.md`).

Champs de la sous-couche C-MOUVEMENT-TYPE.R

| **Champ**                  | **Type**                         | **Valeurs / Exemples**                                                            | **Description**                                                                                 |
| -------------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| sigle\_mouvement\_ref      | Référence                        | Pointeur vers C-MOUVEMENT-TYPE.M.sigle\_mouvement                                 | Le mouvement de la couche M dont cette traduction est une instanciation.                        |
| regime\_comptable          | Énumération                      | **Admis : IFRS / PCG / CARE / GESTION.** **Candidats non instanciables : US\_GAAP / IIRC** `[statut `CANDIDAT_NON_INSTANCIABLE` : §8.4ter]`   | Régime comptable de la traduction. Régimes admis et candidats non instanciables sont distingués dans l'énumération elle-même : un champ ne laisse pas écrire ce que la règle interdit. Le sous-régime PCP figure dans la table de traduction ci-dessous. |
| denomination\_regime       | Texte                            | ex. : provision pour risque environnemental (IAS 37)                              | Nom de l'écriture dans le régime considéré.                                                     |
| compte\_imputation         | Texte                            | ex. : 151 (PCG) ; provision environnementale (IFRS)                               | Compte ou catégorie d'imputation. Format ouvert.                                                |
| conditions\_reconnaissance | Texte                            | ex. : obligation juridique ou implicite ; fiabilité de mesure suffisante (IAS 37) | Conditions sous lesquelles le mouvement est reconnaissable dans ce régime.                      |
| exemple\_chiffre           | Couple (montant, devise) + texte | ex. : 32 651,70 € — coût de préservation NH Exploitation B 2024                   | Exemple chiffré tiré de l'annexe K du set (`MRC_v5.7_Annexe_K_Cas_Chiffres.md`), si disponible. |
| traduction\_uri            | **Clé composite**  | `sigle_mouvement` × `regime_comptable` × sous-régime éventuel ; libellé lisible : did:registre:mouvement:richard:l\#regime:CARE | Identifiant de cette traduction, distinct du mouvement M dont elle dérive. **Le côté mouvement est fermé ; le côté régime ne l'est pas**, puisque §8.4bis admet qu'un collectif déclare un régime. Le registre des régimes déclarés (§8.4ter) porte, pour chaque régime, son porteur, sa date de déclaration et sa condition de réfutation — réponse au manque relevé en §8.4bis, « aucun des sept champs ne dit qui a déclaré le régime ». |

Tableau de traduction — première esquisse des seize mouvements en quatre régimes

Le tableau ci-dessous fournit une première esquisse de la couche R. Une cellule « = IFRS » signifie que la traduction est identique à la colonne IFRS. Le tableau est une amorce ; il sera densifié au fil des cas d'usage Annexe K.

> §8.13 pose que « la couche R accueille un sous-régime PCP (Plan Comptable Public) distinct du PCG » et en fait reposer l'application au PPI aligné climat, qualifiée de « cas paradigmatique ». La colonne PCP porte ce sous-régime. Deux cellules sont dérivables de §8.13 — la conception dualiste de l'État, où un même équipement produit un décaissement budgétaire et un actif en comptabilité générale ; **les quatorze autres portent `[À RENSEIGNER]` et le resteront jusqu'à instruction par un spécialiste de la comptabilité publique.** Une colonne vide déclarée vaut mieux qu'une colonne annoncée et absente.

> L'absence de traduction d'un régime se lit dans la colonne « Gestion » sous la forme explicite **« Hors champ »**, et — c'est le point important — **l'assiette de `signal_translation_manquante` n'est pas cette table.** Le signal se déclenche écriture par écriture, quand une écriture inscrite en CARE n'a pas de traduction disponible dans un régime de référence ; son décompte relève de l'**extension comptable, Annexe H §H.11.2**, et non d'un marquage de cellule. Une table de mouvements ne peut pas porter un signal qui porte sur des écritures.

| **Sigle** | **IFRS**                                                  | **PCG** | **CARE**                                                                                 | **Gestion**                                       | **PCP**  |
| --------- | --------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------- | --------- |
| a         | Mouvement intra-actif                                     | \= IFRS | Étendu aux actifs CARE (financier, naturel, humain) ; pas de divergence structurelle     | Transferts intra-stocks ou intra-immobilisations  | `[À RENSEIGNER]` |
| b         | Mouvement intra-dette                                     | \= IFRS | Étendu aux dettes NH ; pas de divergence                                                 | Reclasse­ments de dettes selon section analytique | `[À RENSEIGNER]` |
| c         | Mouvement intra-S'                                        | \= IFRS | \= IFRS                                                                                  | Pas de pertinence directe                         | `[À RENSEIGNER]` |
| d         | Mouvement intra-résultat                                  | \= IFRS | \= IFRS                                                                                  | Affectation entre centres de profit               | `[À RENSEIGNER]` |
| e         | Achat à crédit ; reconnaissance d'un actif et d'une dette | \= IFRS | Inclus M12 (dette NH) et M13 (capital humain). Reconnaissance étendue aux créanciers NH. | Idem IFRS, ventilation analytique                 | Actif en comptabilité générale — **coexiste** avec un mouvement `l` en comptabilité budgétaire (§8.13) |
| f         | Remboursement d'un emprunt                                | \= IFRS | Peut concerner le remboursement d'une D NH par charge de préservation (cf. l)            | Suivi des décaissements opérationnels             | `[À RENSEIGNER]` |
| g         | Apport en capital numéraire                               | \= IFRS | \= IFRS                                                                                  | Hors champ                                        | `[À RENSEIGNER]` |
| h         | Remboursement du capital                                  | \= IFRS | Subordonné à R-PRIORITE-CREANCIERS Niveau 4 (cf. § 8.7)                                  | Distribution aux actionnaires                     | `[À RENSEIGNER]` |
| i         | Conversion d'une dette en capital                         | \= IFRS | Cas rare ; nécessite consentement de la communauté NH si dette NH                        | Hors champ                                        | `[À RENSEIGNER]` |
| j         | Distribution de réserves en dettes                        | \= IFRS | Subordonné à R-PRIORITE-CREANCIERS Niveau 4                                              | Hors champ                                        | `[À RENSEIGNER]` |
| k         | Vente comptant = produit                                  | \= IFRS | \= IFRS (aucune extension nouvelle ; reste un produit ordinaire)                         | Suivi par section analytique de vente             | `[À RENSEIGNER]` |
| l         | Charge payée comptant                                     | \= IFRS | Inclus M11 (charge de préservation NH). Reconnaissance explicite de l'effort de soin.    | Charges opérationnelles ventilées par section     | Décaissement budgétaire — **coexiste** avec un mouvement `e` en comptabilité générale (dualisme de l'État, §8.13) |
| m         | Remise de dette = produit exceptionnel                    | \= IFRS | À surveiller : signal d'effacement injustifié d'une obligation NH (signal\_remise\_NH)   | Hors champ                                        | `[À RENSEIGNER]` |
| n         | Contravention ; dette imposée                             | \= IFRS | Reconnaissance d'une D NH sans paiement immédiat (cf. M12)                               | Charges exceptionnelles                           | `[À RENSEIGNER]` |
| o         | Rectification d'erreur exercice antérieur                 | \= IFRS | \= IFRS                                                                                  | Hors champ                                        | `[À RENSEIGNER]` |
| p         | Cas inverse de o                                          | \= IFRS | \= IFRS                                                                                  | Hors champ                                        | `[À RENSEIGNER]` |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Économie cognitive — quatre divergences sur seizeSur les seize mouvements, quatre seulement (e, f, l, n) font apparaître une divergence opérationnelle entre IFRS/PCG et CARE. Les douze autres sont structurellement identiques entre régimes — seul le périmètre d'application diffère. Cette propriété est un argument décisif pour la diffusion de F8 auprès de praticiens non spécialistes : trois quarts de la comptabilité CARE est identique à la comptabilité classique.** |

#### 8.4bis Le régime est déclaré par un collectif — décision du porteur

*Appui formel : `ProfReg/PR22_RegimeDeclare.lean`.*

**Ce qui est décidé.** Les composites `P + C` de §8.5.3 ne sont pas des typages de la couche T : ce sont **des qualifications d'une même chose dans deux régimes**. Ils remontent en couche R.

**La raison, et elle n'est pas un rangement.** L'alternative posée dans l'instruction — la double nature du sol est-elle *ontologique* (couche T) ou *conventionnelle* (couche R) ? — est mal posée. Le régime n'est pas le contraire de l'ontologique :

> **C'est au collectif de décider de la nature ontologique, voire des natures ontologiques, attachées à une chose qui fait l'objet d'un attachement collectif.**

Un sol peut être un foncier de valeur marchande sous certaines conditions et un substrat du vivant sous d'autres ; ce sont ces conditions que le collectif pose, et la couche R est le lieu où elles s'inscrivent. **Remonter `P + C` en couche R ne déclasse pas le sol agricole : cela nomme qui décide.** `une_chose_deux_natures` l'inscrit — une chose, deux natures, deux régimes, **deux porteurs**.

**Deux conséquences démontrées, que le registre des régimes déclarés (§8.4ter) satisfait.**

**(1) Le régime exige un porteur.** La couche R porte sept champs et **aucun ne dit qui a déclaré le régime**. Les régimes établis ont un normalisateur implicite (l'IASB pour IFRS) ; un régime déclaré par un collectif n'en a aucun s'il n'est pas inscrit. Le champ `porteur_du_regime` est versé comme colonne de ce registre. Patron : `porteurDeLaDeclaration` de PR-18, où le porteur est exhibé par construction du type ( *le porteur est un **champ** de la qualification : c'est la définition, non un théorème*).

**(2) `regime_comptable` ne peut pas être une énumération close.** Si les régimes peuvent être déclarés par des collectifs, et si la population des collectifs n'est pas énumérable, **toute liste close en exclut un** — c'est `liste_close_exclut_toujours` (PR-16, écrit pour les réfutants) **appliqué au régime**, et non réécrit : `enumeration_close_exclut_un_collectif`, `une_liste_close_de_collectifs_Nat_exclut_quelqu_un`. Seule l'ouverture n'exclut personne (`ouverture_n_exclut_personne`).

> **Ce n'est pas un confort de modélisation. La décision du porteur rend l'ouverture de ce champ nécessaire**, et le théorème qui l'établit a été écrit pour une tout autre question.

`[GARDE]` L'ouverture ne déclasse aucun régime établi et n'affirme pas qu'ils se valent : `PR22_ne_supprime_pas_les_regimes_etablis`, `PR22_ne_departage_pas_les_regimes`. Elle cesse d'exclure, rien de plus.

 Elle ne calcule aucun miroir. Une fois `P + C` en couche R, **le miroir se prend régime par régime** et chaque qualification a le sien ; la question du « miroir des composites » ne se pose plus pour ces trois cas — les plus attestés du corpus. Pour le seul cas restant, `e + D−`, elle est **tranchée par décision du porteur — voir §8.5.3bis.**

#### 8.4ter Registre des régimes déclarés

`[Décision du porteur. Le typage de `traduction_uri` en clé composite (§8.4) laisse ouvert le côté régime, que §8.4bis déclare non énumérable. Ce registre en est la contrepartie.]`

**Ce que ce registre satisfait.** §8.4bis établit deux conséquences de la décision du porteur : *« le régime exige un porteur — la couche R porte sept champs et aucun ne dit qui a déclaré le régime »*, et *« `regime_comptable` doit cesser d'être une énumération close »*. Le champ `porteur_du_regime` **est versé ici comme colonne du registre**, et l'ouverture prend la forme d'un registre plutôt que d'une liste : **on n'y entre pas en étant prévu, on y entre en déclarant.**

**Champs du registre.** Chaque régime inscrit porte quatre champs, et aucun n'est facultatif.

| Champ | Type | Description |
| :-- | :-- | :-- |
| `regime_comptable` | Chaîne libre | Le nom du régime. **L'énumération est close pour les régimes admis à ce jour et ouverte à l'inscription.** `regime_comptable` ne peut pas être une énumération close : le théorème `enumeration_close_exclut_un_collectif`, démontré dans `PR22_RegimeDeclare.lean`, établit dans le domaine des régimes déclarés qu'une énumération close exclut un collectif. Il réemploie le patron général `liste_close_exclut_toujours` de `PR16_RefutationTiers.lean`. Le registre doit donc être ouvert à l'inscription par déclaration (§8.4bis) |
| `porteur_du_regime` | Référence | **Qui a déclaré ou normalisé ce régime.** Patron : `porteurDeLaDeclaration` (PR-18), où le porteur est exhibé par construction du type |
| `date_declaration` | Date | Date de la norme, de la publication doctrinale, ou de la déclaration du collectif |
| `condition_refutation` | Texte | **À quelles conditions ce régime cesserait d'être applicable ou serait tenu pour faux.** Sans elle, le régime est un cadre non gouverné |

**Registre.**

| Régime | Statut | `porteur_du_regime` | `date_declaration` | `condition_refutation` |
| :-- | :-- | :-- | :-- | :-- |
| **IFRS** | admis | IASB / IFRS Foundation | norme en vigueur à la date de l'écriture | Le normalisateur retire ou modifie la norme appliquée ; l'écriture cite alors la version |
| **PCG** | admis | Autorité des normes comptables (ANC) | règlement en vigueur à la date de l'écriture | *idem* |
| **CARE** | admis | **Doctrine — pas de normalisateur.** Rambaud, *La valeur de l'existence en comptabilité*, thèse Dauphine, 2015 (HAL tel-01253474) | 2015 | Tombe si l'on établit qu'un capital naturel ou humain dégradé ne produit pas une obligation de rétablissement — c'est-à-dire que la « dette de préservation » ne se comporte pas comme une dette |
| **GESTION** | admis | **Aucun normalisateur** — convention interne à chaque organisation | déclarée par l'organisation | Tombe avec la convention interne qui la porte. **Un régime de gestion n'est opposable qu'à l'organisation qui l'a déclaré** |
| **PCP** (sous-régime) | admis | CNoCP, avis n° 2016-02 du 4 juillet 2016 ; cadre : Bahougne & Camus, *Droit de la comptabilité publique*, PUF, 2020 | 2016 | *idem* normalisateur |
| US\_GAAP | **`CANDIDAT_NON_INSTANCIABLE`** | FASB (Financial Accounting Standards Board) | `[CRITÈRE DE SORTIE]` | `[CRITÈRE DE SORTIE]` **Pièces exigées, vérifiables par un tiers :** (i) la référence **datée** de la version de l'*Accounting Standards Codification* publiée par le FASB et citée par une écriture ; (ii) la condition de réfutation « *idem* normalisateur », comme IFRS et PCG ; (iii) une **colonne de traduction** en table §8.4. **Caducité : retrait du registre à la v5.7 si le critère n'est pas rempli**, sans nouvel arbitrage |
| IIRC | **`CANDIDAT_NON_INSTANCIABLE`** | `[À CONFIRMER — IFRS Foundation, d'après le titre de son communiqué d'août 2022 annonçant l'achèvement de la consolidation avec la Value Reporting Foundation, qui portait le cadre d'*Integrated Reporting* ; texte non lu]` | `[CRITÈRE DE SORTIE]` | `[CRITÈRE DE SORTIE]` **Pièces exigées, vérifiables par un tiers :** (i) le **porteur actuel confirmé sur le texte** du communiqué ou sur la page du cadre ; (ii) la référence **datée** de la version du cadre d'*Integrated Reporting* ; (iii) la condition de réfutation « *idem* normalisateur » une fois le porteur confirmé ; (iv) une **colonne de traduction** en table §8.4. *À la sortie, examiner le renommage de la valeur : l'IIRC n'existe plus comme organisme.* **Caducité : retrait du registre à la v5.7 si le critère n'est pas rempli**, sans nouvel arbitrage |

> `[Décision du porteur.]` **`US_GAAP` et `IIRC` figurent** en `CANDIDAT_NON_INSTANCIABLE`, chacun avec un critère de sortie écrit — les pièces qui rendraient la ligne complète et qui les émet — et une clause de caducité. **`LIFTS` et `ACTION` ne figurent pas au registre** : aucun porteur ne peut leur être désigné sans instruction bibliographique, donc aucun critère de sortie vérifiable n'est écrivable, et une valeur de tiers lemme sans critère de résolution est un `NONDECLARE` renommé (patron CONV-9).
>
> **Ne pas inscrire n'est pas interdire.** Le registre reste ouvert à l'inscription : *« on n'y entre pas en étant prévu, on y entre en déclarant »*. LIFTS ou la comptabilité-action y entrent **par déclaration complète** — porteur, date, condition de réfutation. Leur absence du registre des **régimes** ne retire rien à leur mention comme **doctrines** (`doctrine_juste_prix`, F8) ni comme comptabilités alternatives dans le principe directeur de F8.
>
> `[OBLIGATION OUVERTE]` *Porteur :* porteur MRC / architecte. *Horizon :* gel de la v5.7 pour les deux candidats. *Critère :* colonnes `date_declaration` et `condition_refutation` renseignées sur pièces, ou retrait.

> **Condition de bonne formation d'un régime déclaré par un collectif.** L'inscription nomme **le collectif**, **la date de sa délibération**, et **la condition de réfutation** du régime. **Homologie déclarée** : `CANDIDAT_NON_INSTANCIABLE` est, au niveau des régimes, **le marqueur de CONV-7** — inscrit, sans effet (aucune écriture autorisée), avec un horizon (critère de sortie et caducité). Le refus ne vaut que pour un régime sans condition de réfutation **ni** critère de sortie et caducité. Le marqueur CONV-7 porte en retour un horizon (Annexe §A.15.10). *Ancrage PR-32 :* `regime_sans_refutation_n_autorise_aucune_ecriture`, `candidat_ssi_critere_de_sortie_et_caducite`, `regime_temoin_discriminant`. Un régime dont la condition de réfutation est vide n'est pas inscrit — **sauf sous le statut `CANDIDAT_NON_INSTANCIABLE`, seule exception, qui exige un critère de sortie vérifiable par un tiers et une clause de caducité, et n'autorise aucune écriture** : c'est la transposition au régime de ce que la quatrième propriété de §B.2 exige d'une source — **savoir qui répond, et à quelles conditions cette réponse serait invalidée**.

`[GARDE, reprise de §8.4bis]` L'ouverture **ne déclasse aucun régime établi et n'affirme pas qu'ils se valent** (`PR22_ne_supprime_pas_les_regimes_etablis`, `PR22_ne_departage_pas_les_regimes`). La colonne `porteur_du_regime` rend visible ce qui est implicite pour les régimes normalisés et manquant pour les autres — elle ne met pas l'IASB et un collectif de bassin sur le même plan, elle exige des deux qu'ils soient nommés.

 `[LACUNE DÉCLARÉE — sept lignes actives, cinq admises et deux candidates déclarées comme telles (US_GAAP, IIRC) ; les deux candidates restent incomplètes jusqu'à leur critère de sortie ou leur caducité au gel de la v5.7.]`

*Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* un régime déclaré par un collectif est inscrit avec ses quatre champs, et une écriture qui s'y réfère résout son `traduction_uri` sans ambiguïté.

#### 8.5 Sous-couche C-MOUVEMENT-TYPE.T — typage P-C-E-D-e-d et règles miroir

La grammaire P-C-E-D-e-d est issue de la note synthétique MRC × CARE × comptabilité financière (avril 2026) et a été validée empiriquement par K1 et K3 (livrable Lecture P-C-E-D-e-d K1 × K3, mai 2026). Elle raffine la règle constitutive R1 (symétrie DÉBIT / CRÉDIT) en typant chacune des deux écritures miroirs selon six primitives. R1 reste la règle constitutive ; la grammaire ne la remplace pas, elle la qualifie.

#### 8.5.0 Le domaine propre de la sous-couche T — les deux registres et l'écriture duale

> **Ce paragraphe emploie « écriture duale » au sens du porteur** : deux côtés d'une même relation, inscrits dans **deux registres tenus par des teneurs identifiés et distincts**, chaque côté portant son **ancrage déclaré** — les livres d'une comptabilité tenue ou un registre de communalité, indifféremment (décision du porteur D7, 07/10/2026, ci-dessous). C'est le seul sens retenu ; il est formalisé par **PR-35** (`PR35_EcritureDuale.lean` : registres à teneur, en relation symétrique par construction de la définition (`ecriture_duale_symetrique`, déclarée, jamais appui seul ; témoin : `ecriture_duale_temoin_discriminant`, vraie sur le prêt bancaire, fausse après une extinction inscrite d'un seul côté), écart, état de rapprochement, qui nomme les opérations manquantes de chaque côté (`l_etat_de_rapprochement_nomme_l_ecart`) ; ancrage AX-15, rapprochement banque / client ; tiers : AX-16, CONV-16 (PR-43) ; constat porté au nom du registre : CONV-17 (PR-45) ; annotation de destination d'un engagement porté à un registre de chaîne : CONV-18 (PR-47) ; suites : PR-38 à PR-49). Il **ne doit pas être confondu** avec L2, le **registre comptable augmenté** : un même fait porté dans deux registres d'un même ensemble de relations, sans teneur.
>
> **Raccord et entité sans comptabilité.** PR-36 démontre que la double tenue d'une organisation (registre augmenté) et l'écriture duale se composent (`raccord_augmente_duale`). PR-37 formalise le cas où l'autre côté est un **milieu** : son registre a pour **titulaire** le milieu et pour **écrivant** un collectif désigné par une déclaration **arrêtée par les concernés** (AX-7) — c'est le « triplet porteur » de `inscription_communalite_uri_ref` ci-dessous — et il **porte le maintien** (CONV-11). *Ancrages PR-37, lectures de `bienForme` et `registreOpposable` :* le milieu n'écrit pas son registre (`le_milieu_n_ecrit_pas_son_registre`) ; une déclaration seulement ratifiée ne fonde pas le registre (`la_ratification_ne_fonde_pas_le_registre`) ; sans maintien, ou avec un maintien porté par un autre registre que celui du titulaire, le registre n'a pas d'appui (`sans_maintien_pas_d_appui`, `maintien_d_un_autre_registre_pas_d_appui`). Témoins : `ecriture_duale_avec_un_milieu` (déclaration arrêtée, registre bien formé, écart vide), `registre_de_milieu_temoin_discriminant` (arrêtée, l'écart est vide ; ratifiée, il reste), `registre_mal_nomme_l_ecart_revient`.

**La sous-couche T type les écritures d'une comptabilité tenue et celles d'un registre de communalité.** Son domaine est strictement plus large que celui de la sous-couche M (§8.3bis), et cette différence de domaine est sa raison d'être, non un effet de bord.

**Ce que la grammaire P-C-E-D-e-d doit rendre possible, et qu'aucune des deux autres sous-couches ne rend possible : l'écriture duale.** Une organisation dotée d'une comptabilité classique et une entité qui n'en a pas inscrivent les deux côtés d'une même relation **dans la même grammaire** — la première dans ses livres, la seconde dans son registre de communalité. C'est cette commensurabilité-là, et non la couverture des seize mouvements, qui justifie l'existence d'une ontologie des positions à côté d'une géométrie des mouvements.

> **Généralisation de la condition de §8.5.2bis.4, portée au niveau de la sous-couche.** *« Le registre financier n'est pas requis. Le registre de communalité, ou un rapport extra-financier dont les champs requis sont renseignés, satisfait la condition. »* Posé pour une condition d'inscription particulière, il vaut **pour tout typage T** : *le lieu de l'inscription est indifférent, sa forme ne l'est pas.* Une écriture T est bien formée si ses champs requis sont renseignés, que le livre qui la porte soit un grand livre ou un registre de communalité ; elle ne l'est pas si elle repose sur une mention en langue naturelle sans champ propre, **quel que soit le document qui la porte — bilan compris**.

**Attestation dans le set.** §8.1 fonde F8 sur les cas K1 et K3. L'Annexe K nomme leurs types d'instance : K1, *« un exploitant qui tient un registre de communalité de son propre sol et troupeau »* ; K3, *« une instance (OLGE/PLE/CLE) qui tient un registre de communalité d'un bien commun partagé par des centaines d'acteurs »*. **Une instance de gestion de l'eau de ce type ne calcule aucun surplus.** Le domaine ici déclaré n'étend donc pas F8 : il inscrit ce dont F8 tirait déjà sa légitimité, et que son modèle de données instancie par l'ancrage alternatif ci-dessous.

*Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* une écriture duale complète entre une organisation à comptabilité tenue et une entité sans comptabilité, les deux côtés typés et appariés par la table §8.5.2.

`[CONSÉQUENCE NÉGATIVE DÉCLARÉE — la sous-couche T ne peut pas être évaluée par sa seule couverture des seize mouvements. La métrique de §8.5.5 est accompagnée de sa symétrique, faute de quoi elle mesurerait une seule des deux vocations de T.]`

Champs de la sous-couche C-MOUVEMENT-TYPE.T

| **Champ**                | **Type**               | **Valeurs / Exemples**                                                                       | **Description**                                                                                                           |
| ------------------------ | ---------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| traduction\_uri\_ref     | Référence **facultative**  | Pointeur vers C-MOUVEMENT-TYPE.R.traduction\_uri | Traduction de la couche R que ce typage qualifie. **Renseigné lorsque l'écriture appartient à une comptabilité tenue. Vide lorsqu'elle appartient à un registre de communalité — voir `inscription_communalite_uri_ref` et la condition d'ancrage ci-dessous.** |
| **inscription\_communalite\_uri\_ref**  | **Clé composite + triplet porteur** | `entité` × `registre` × `inscription`, où l'entité est désignée par un identifiant stable existant — **LEI**, SIREN, identifiant d'instance de gestion (OLGE/PLE/CLE) — ou par un DID | Inscription d'un registre de communalité que ce typage qualifie, **lorsque l'entité concernée ne tient pas de comptabilité relevant d'un régime admis**. **Toute inscription déclare en outre un triplet porteur — l'entité, la personne qui inscrit, et le rôle qui l'y habilite au sein du consortium de gouvernance (Annexe H §H.1)** — sur le patron du `vLEI` de la GLEIF, qui *« combine cryptographiquement l'identité de l'entité, l'identité personnelle d'un individu, et le rôle officiel que cet individu exerce »* (rapport fondateur, p. 130). **Une entité sans comptabilité n'a pas de commissaire aux comptes : le triplet est la seule garantie disponible sur qui a écrit en son nom.** |
| typage\_primitive        | Énumération multivalue | P / C / E / D / e / d ; composites X+Y autorisés                                             | Typage de l'écriture côté A. Les types composites sont autorisés (cf. arbitrage 11.3, option A retenue).                  |
| typage\_miroir           | Énumération multivalue | P / C / E / D / e / d ; composites X+Y autorisés                                             | Typage de l'écriture miroir côté B, selon les règles de cohérence du tableau 8.5.1.                                       |
|  **→ contrôle calculé** | **Aucun champ** — prédicat dérivé de `typage_primitive` et `typage_miroir` | *sans objet : le contrôle se calcule, il ne se déclare pas* | Vérification que (typage\_primitive, typage\_miroir) appartient à la table des compatibilités miroir.                     |
| destinataire\_effort     | Énumération            | FOURNISSEUR / CLIENT / SALARIE / NH\_NATUREL / NH\_HUMAIN / GENERATION\_FUTURE / INDIFFERENT / **SANS\_BENEFICIAIRE**  | Pour les typages e ou d, destinataire de l'effort ou du résultat. Champ qualifiant utile pour les arbitrages de priorité. **`SANS_BENEFICIAIRE` type l'effort qui ne va vers personne — consommation propre de patrimoine : amortissement, dépréciation, perte fortuite, destruction. À ne pas confondre avec `INDIFFERENT`, qui est un bénéficiaire réel dont l'identité n'importe pas à l'écriture ; `SANS_BENEFICIAIRE` est un résultat, non un défaut de renseignement.** |
| asymetrie\_existentielle | Énumération ternaire | VRAI / FAUX / **NON\_DETERMINABLE**  | Pour les typages E sans miroir comptable (engagement existentiel envers acteur non tracé, cf. R-INTERDIT-ABSOLU). NON\_DETERMINABLE : on ne sait pas si l'acteur engagé est traçable. |
| **creance\_repartissable**  | Énumération ternaire | VRAI / FAUX / NON\_DETERMINABLE ; **`NONDECLARE` refuse, n'autorise pas** (patron CONV-9) | **Porte sur le bénéficiaire d'un `E+`** — le miroir `C+` quand il existe, le bénéficiaire désigné sinon — **et sur chaque classe de créance `C+` d'une écriture `D+ ↔ C+` relevant d'une forme d'affectation admise (fiducie, ORE, ORIC — §8.5.6.2bis)**. **VRAI** : le bénéficiaire détient, seul ou avec d'autres, un **droit individuel sur une quote-part de valeur** — distribution, remboursement au-delà du nominal, boni de liquidation, retour du patrimoine, prix de cession représentatif d'une quote-part de la situation nette. **FAUX** : aucun titulaire ne détient un tel droit (ex. réserves statutairement impartageables). **NON\_DETERMINABLE** : l'écriture ne permet pas d'établir l'un ou l'autre. **Sans objet** pour `E+ ↔ ∅` avec `asymetrie_existentielle = VRAI`. **Le champ porte sur la VALEUR, non sur les UTILITÉS** : un droit d'usage divis (affouage, pâturage) répartit des utilités sans conférer de quote-part de valeur, et reste FAUX. Critère repris de Rochfeld, Cornu & Martin 2021 — intérêts « divisibles et répartissables » exclus de l'intérêt commun (p. 332, 336). Voir §8.5.6.2 |
| **classe\_creance**  | Énumération | **VALEUR\_ECONOMIQUE** / **USAGE** / **PRESTATION** / **AUTRE** (déclarée) | **Porte sur le `C+` d'une écriture `D+ ↔ C+` relevant d'une forme d'affectation admise (§8.5.6.2bis).** Dit ce que la créance donne à son titulaire : **VALEUR\_ECONOMIQUE** — une quote-part de la valeur de la chose, en cours ou au terme (droit de l'investisseur, attribution finale du patrimoine fiduciaire) ; **USAGE** — l'accès ou la jouissance d'une utilité de la chose ; **PRESTATION** — l'exécution d'obligations de faire ou de ne pas faire au service d'une finalité (créancier d'ORE ou d'ORIC). **Une même chose porte en général plusieurs classes** ; chacune est une écriture distincte, avec son propre `creance_repartissable`. |
| **source\_engagement\_D**  | Couple (type, référence) | `type` : **ACTE\_FORME\_ADMISE** / **TEXTE\_INSTITUANT** / **REGLES\_PROPRES\_COLLECTIF** ; **`NONDECLARE` refuse, n'autorise pas** (CONV-9) ; `référence` au sens de §B.2 borné | **Exigé pour tout `D+` d'une chose inscrite comme commun.** Cite ce qui donne **le pouvoir d'engager** le collectif, distinct du **droit d'écrire** que donne le rôle du triplet porteur (Annexe H §H.1.3bis) : l'acte de la forme admise (§8.5.6.2bis), le texte qui institue l'instance, ou **la clause des statuts et la délibération datée** qui l'exerce. Correspondance : ACTE / TEXTE → `legitimiterepresentant = JURIDIQUE` ; RÈGLES PROPRES → `DELIBERATIVE` (§5.2). Règles : §8.5.6.5. |

> **Toute écriture de la sous-couche T porte au moins un ancrage.**
>
> | Cas | Champ renseigné | Ce que l'écriture doit déclarer en plus |
> | :-- | :-- | :-- |
> | Comptabilité tenue | `traduction_uri_ref` | **un régime comptable est déclaré** — la traduction R pointée porte `regime_comptable` parmi les valeurs admises (§8.4) |
> | Registre de communalité | `inscription_communalite_uri_ref` | **l'entité et son registre de communalité sont nommés** — modalité d'ancrage des entités ou concernés sans comptabilité admise |
> | Écriture duale | **un par côté**, de l'un ou l'autre type | deux teneurs identifiés et distincts ; chaque côté porte son propre ancrage déclaré ; l'arité (B7) nomme la contrepartie |
>
> **Une écriture T sans aucun ancrage n'est pas une écriture mal renseignée : c'est un typage qui ne qualifie rien.** Elle est refusée. *Ancrage PR-31 :* `sans_ancrage_refusee`, `le_registre_de_communalite_suffit`, `la_duale_exige_un_ancrage_par_cote` ; pour l'écriture duale (`CoteDuale`, `ancreeDuale`) : `ancree_duale_ssi`, `deux_comptabilites_tenues_ancrent_une_duale`, `le_registre_de_communalite_ancre_un_cote`, `un_seul_teneur_pas_de_duale`.
>
> **Décision du porteur D7 — 07/10/2026 : ancrage de l'écriture duale élargi.** L'ancrage de l'écriture duale est élargi à deux registres tenus par des teneurs identifiés, chaque côté portant son ancrage déclaré. Le registre de communalité constitue une modalité d'ancrage pour les entités ou concernés sans comptabilité admise.
>
> L'application écologique vise à documenter l'affectation des financements, les engagements et leur réalisation, par homologie avec la traçabilité des relations bancaires (AX-15). **Cette homologie n'assimile pas l'engagement écologique à une dette financière et ne confère aucun pouvoir d'émission monétaire.** Les exigences propres au financement écologique restent distinctes du contrôle général d'ancrage.
>
> *Ce que la décision remplace.* L'ancrage du 28/09 (PR-31, booléen `duale` sans teneurs) exigeait cumulativement une traduction comptable et une inscription de communalité ; il refusait ainsi le couple banque / emprunteur que PR-35 tient pour une écriture duale (vérification en Lean du 03/10). `[CHANGEMENT DE BASE TRACÉ — D7]`
>
> *Porteur :* porteur MRC. *Horizon :* institutionnel, révisable. *Critère de vérification :* un couple de deux comptabilités tenues, un couple comptabilité / registre de communalité et un couple de deux registres de communalité sont ancrés ; un côté sans ancrage, ou un seul teneur, ne l'est pas (théorèmes PR-31 ci-dessus).
>
> `[CONDITION DE RÉFUTATION — proposée, à confirmer par le porteur]` L'élargissement tombe si l'on établit, pour un couple de registres dont l'un au moins n'est pas une comptabilité tenue, qu'aucun état de rapprochement contrôlable ne peut être établi entre eux (PR-35, propriété (iii)) : l'homologie avec la relation bancaire ne serait alors pas attestée.
>
> `[RESTE À FAIRE — le schéma du DID `did:registre:communalite:` n'est pas spécifié. La forme donnée ci-dessus est un gabarit, non une convention arrêtée ; elle doit être alignée sur l'Annexe H §H.1 (DID des entités) avant tout usage en Usage 3.]`

#### 8.5.1 Définition des six primitives

| **Sigle** | **Nom**                       | **Définition opérationnelle**                                                                                                        |
| --------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| P         | Patrimoine                    | Bien, chose ou actif détenu et mobilisable par l'acteur. Réifié, mesurable, transmissible.                                           |
| C         | Créance                       | Droit d'usage ou de paiement attaché à un acteur identifié, ouvert et non encore réglé. Non réifié.                                  |
| E         | Engagement                    | Promesse interne ou externe par laquelle l'acteur se lie pour l'avenir, sans exigibilité contractuelle immédiate. Passif structurel. **Accueille la composante S' de l'équation du bilan — capitaux propres et réserves — par rabattement déclaré : voir §8.5.1ter.** |
| D         | Dette                         | Obligation exigible de rendre une valeur ou un soin à un créancier identifié. Inverse de C par symétrie R1.                          |
| e         | effort fourni                 | Action ou ressource mobilisée par un acteur en faveur d'un autre — travail, soin, matière, mesuré par une charge.                    |
| d         | résultat répondant aux désirs | Action ou ressource produite en réponse à une demande — vente, usage, mesuré par un produit.                                         |

#### 8.5.1bis Le troisième signe — `neutre`

Le tableau §8.5.2 signe `P`, `C`, `E` et `D` — `P+`, `C−`, `E+`, `D−` — mais **jamais `e` ni `d`**, qui y figurent nus. Le modèle emploie donc **trois signes et n'en nomme que deux**. Le troisième est déclaré ici :

| **Signe** | **Sur quelles primitives** | **Ce qu'il porte** |
| --- | --- | --- |
| `+` | `P` `C` `E` `D` | entrée, naissance, augmentation du poste |
| `−` | `P` `C` `E` `D` | sortie, extinction, diminution du poste |
| `neutre` | `e` `d` | **flux, non poste** : un effort et un résultat ne s'augmentent ni ne s'éteignent, ils passent |

**Pourquoi ce n'est pas cosmétique.** Un typage sans le troisième signe est un type partiel : la formalisation de la grammaire ne compile pas sans lui (`SondePCEDed.Signe`). La distinction poste / flux qu'il inscrit est celle-là même que §8.5.3bis retient pour les charges de personnel — `e` est un flux, et l'extinction de dette qu'il produit relève de la transition, non du type (§8.5.3bis).

#### 8.5.1ter Le rabattement de S' sur E — décision du porteur

`[Origine : jalon J1 conduit sur le registre de données fiabilisées du groupe RATP 2025 (`PPC/RATP/J1_typage_PCEDed_RATP_2025.json`).]`

**Le problème.** La sous-couche M (§8.3) pose l'équation `A = D + S' + ΔS` et en fait le socle régime-invariant de tout mouvement. La sous-couche T type **trois de ses quatre composantes** : `A` par `P` et `C`, `D` par `D` et `E`, `ΔS` par `e` et `d`. **`S'` — la situation nette hors résultat, c'est-à-dire le capital et les réserves — n'est typée par aucune des six primitives prise dans son sens premier.** Ni chose tenue, ni droit contre quelqu'un, ni obligation exigible, ni flux : sans la décision ci-dessous, les capitaux propres n'auraient pas de place dans la grammaire qui prétend typer les deux côtés de toute écriture.

**L'enjeu sur le registre RATP.** Sur les 68 faits de mouvement du registre RATP qualifiés d'écritures, **40 portent sur une composante de capitaux propres** : sans la décision, aucune règle de la table ne les type, et la totalité du tableau de variation des capitaux propres — un des cinq états primaires — reste hors d'atteinte du registre.

**La décision.** `S'` est **rabattue sur `E`**, par déclaration et non par démonstration : *les capitaux propres sont l'engagement structurel, non exigible, de l'organisation envers ses apporteurs.* Le miroir est `C` dans le livre de l'apporteur — sa créance résiduelle, sans terme et sans exigibilité.

| Écriture de capitaux propres | Typage | Miroir | Ligne de §8.5.2 |
| :-- | :-- | :-- | :-- |
| Apport, dotation, augmentation de capital | `E+` | `C+` chez l'apporteur | ligne `E+`, branche contractuelle |
| Distribution, remboursement de capital, absorption de perte | `E−` | `C−` chez l'apporteur, ou `D+` si la distribution est constatée avant paiement | **ligne `E−`** |
| Transfert interne entre composantes de capitaux propres | `E+` ↔ `E−` | dans le même livre | **arité intra-écriture ; voir §8.5.2ter** |

**Ce que la décision ne fait pas, et il faut le dire.** Elle **n'ajoute pas de septième primitive**. L'option d'une primitive `S` dédiée est écartée : elle toucherait la grammaire elle-même, là où le défaut se répare en Couche 2. Elle **ne prétend pas** que les capitaux propres et un engagement environnemental de long terme soient de même nature : ils partagent une propriété — un passif structurel non exigible envers un tiers identifiable — et c'est cette propriété qui est typée, pas leur identité. Le champ `destinataire_effort` et le champ `compte_passif_CARE` continuent de les distinguer.

**Condition de réfutation de la décision.** Elle tombe si l'on exhibe une écriture de capitaux propres dont le rabattement sur `E` produit une conséquence fausse ailleurs dans F8 — en particulier si `C-PRIORITE-CREANCIERS` venait à traiter une distribution aux apporteurs (Niveau 4) comme l'extinction d'un engagement de Niveau 2, ce que le rabattement pourrait suggérer à tort. **La garde est explicite : le rabattement est un fait de typage (sous-couche T) et n'emporte AUCUN effet sur `niveau_prioritaire` (§8.7), qui reste déterminé par la nature du créancier et non par la primitive.** Toute lecture contraire est un `[DÉCOUPLAGE DE RÉGIMES]`.

*Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* typage effectif d'un tableau de variation des capitaux propres complet, avec au moins une écriture `E+` et une écriture `E−` appariées à leur miroir.

> **Ce que le rabattement ne règle pas seul.** En plaçant les capitaux propres dans `E`, il leur donne une propriété que la règle de communalité (§8.5.6.2) doit discriminer : le jalon J1-ter le montre sur le registre RATP 2025 (41 écritures `INDETERMINE`). **Le rabattement est maintenu** : il oblige les écritures de S′ à déclarer ce qui les sépare d'un engagement de commun.
>
> **Obligation d'écriture.** Toute écriture `E+` de S′ — apport, dotation, transfert entre composantes — déclare `creance_repartissable` (§8.5, table des champs). **Valeur attendue pour le capital et les réserves distribuables d'une société de capitaux : VRAI.** Valeur possible, **à déclarer et non à présumer**, pour des réserves statutairement impartageables : FAUX. Pour un transfert interne `E+ ↔ E−`, la valeur est celle de **la composante créditée**.
>
> **Ce que cela ne fait pas.** Le rabattement reste un fait de typage sans effet sur `niveau_prioritaire` (§8.7), et **la table §8.5.2 n'est pas modifiée** : aucun couple n'est ajouté ni retiré, R1 est inchangé. `[BRANCHE C MAINTENUE OUVERTE — l'obligation ouverte du bornage ci-dessous (déplacer S′ en couche R) n'est ni levée ni affaiblie. La branche B la rend moins pressante, elle ne la tranche pas.]`

> **Le rabattement de `S'` sur `E` ne vaut que sur le domaine de la sous-couche M.** Il s'applique aux écritures dont un régime comptable est déclaré, c'est-à-dire dont `traduction_uri_ref` est renseigné (§8.5, condition d'ancrage). **Il ne s'applique pas aux écritures ancrées sur `inscription_communalite_uri_ref` : dans un registre de communalité, la question des capitaux propres ne se pose pas** — l'entité n'en a pas (§8.3bis).
>
> **Conséquence de lecture, qui est l'objet du bornage.** Hors comptabilité déclarée, la primitive `E` garde sa seule définition de §8.5.1 : *promesse par laquelle l'acteur se lie pour l'avenir, sans exigibilité contractuelle immédiate*, et rien d'autre. **Un `E+` inscrit dans un registre de communalité ne se lit jamais comme un apport, et son miroir `C+` ne se lit jamais comme une créance résiduelle sur l'entité.**
>
> **Pourquoi ce bornage est nécessaire.** La garde du rabattement — *« n'emporte AUCUN effet sur `niveau_prioritaire` »* — est **unilatérale** : elle protège la priorité des créanciers et ne protège rien du côté communalité. Le miroir déclaré du rabattement étant `C+` chez l'apporteur, *« sa créance résiduelle »*, un engagement de commun typé `E+` acquerrait par la table, sans bornage, un miroir lisible comme une créance résiduelle sur ce commun. **La règle A3 ferme la réversion par `P` ; le rabattement en ouvrirait une autre par `E`.** Le bornage fait tenir le couplage dans les deux sens.
>
> **Ce que le bornage ne fait pas.** Il ne retire rien. Les sept mouvements gagés sur `S'` — `c`, `g`, `h`, `i`, `j`, `o`, `p` — restent typables, la ligne `E−` est maintenue, et les faits du registre RATP 2025 gagés sur les cellules `c`, `g` et `h` conservent leur typage. Un retrait complet du rabattement ferait retomber la couverture de **16/16 à 9/16**. `[ÉCART DE COMPTAGE NON LISSÉ — §8.5.1ter annonce « 40 des 68 faits » portant sur une composante de capitaux propres ; le décompte des cellules de §8.5.5 gagées sur `S'` donne 42 (20 + 19 + 3). L'écart de deux n'est pas expliqué et reste à contrôler.]`
>
> **La question de fond reste ouverte.** Le bornage ferme la brèche sans trancher si `S'` a sa place dans la grammaire. **L'option de fond est le déplacement de `S'` en couche R, sur le modèle exact de la décision 6 (§8.5.2ter)** — *ce qui est propre à un régime relève de R, non du typage*. Les décisions 2 et 6 appliquent deux critères opposés à la même question ; le bornage rend la tension supportable, il ne la résout pas. `[OBLIGATION OUVERTE — porteur : porteur MRC / architecte ; horizon : institutionnel ; critère : instruire le traitement de `S'` en couche R, et établir ce qu'une écriture de capitaux propres type en T si ce n'est pas `E`.]`
>
> **Cellule `i` (`D− ↔ E+`), issue de la décision 7.** Elle ne tient que par le rabattement et se trouve bornée avec lui. La lecture de communalité qu'en donne §8.5.5 — *« l'opération par laquelle une dette écologique pourrait devenir un engagement statutaire »* — **n'est pas disponible dans un registre de communalité en l'état** : elle devrait être refondée sur autre chose que la conversion en capital. `[LACUNE DÉCLARÉE.]`

#### 8.5.2 Règles de cohérence miroir (R1 raffinée)

* La quatrième colonne exécute la voie (a) de la sonde P-C-E-D-e-d : elle déclare, ligne à ligne, laquelle des deux relations chaque ligne exprime. Sans elle, le mot « miroir » désignerait deux choses dans le même tableau — `SondePCEDed.la_table_melange_deux_relations`. **Cette colonne est une lecture du porteur, non un résultat démontré** ; c'est elle qui lève le `[CHANGEMENT DE BASE NON TRACÉ]`, en le déclarant plutôt qu'en le prouvant.*

> ### **La table §8.5.2 a vocation à être exhaustive.**
>
> **Ce que la décision tranche.** Deux lectures de cette table **ne peuvent pas être vraies ensemble** (instruction de P6) : *indicative* (elle illustre des cas typiques) ou *exhaustive* (elle définit ce qui est typable). Le porteur retient **exhaustive**.
>
> **Trois conséquences, et aucune n'est cosmétique.**
>
> 1. **Le contrôle calculé de R1 a une assiette.** Le respect de R1 se *calcule* par appartenance du couple (`typage_primitive`, `typage_miroir`) à cette table — il n'existe pas de champ `respect_R1`. Une table indicative rendrait ce calcul sans objet ; la décision le fonde. **C'est elle qui porte le contrôle.**
> 2. **Un couple absent de la table n'est pas typable**, et la lecture indicative qui permettrait de typer hors table « par analogie » est fermée. **Un couple absent n'est pas pour autant une violation de R1** : le qualifier ainsi rangerait des actes licites parmi les violations. Deux situations doivent être distinguées (§8.5.2bis.4) :
>
> | | **Violation de R1** | **Lacune de table** |
> | :-- | :-- | :-- |
> | **Définition** | Un miroir **qui devrait exister n'existe pas** | Un miroir **existe** et **aucune ligne ne l'apparie** |
> | Où est la contrepartie | Nulle part — l'écriture est unilatérale hors des deux asymétries autorisées | Dans le livre du cédant, du bénéficiaire, ou d'un tiers |
> | Ce qui manque | L'écriture miroir elle-même | La ligne de la table §8.5.2 |
> | Niveau du défaut | **Couche 1** — l'invariant R1 est enfreint | **Couche 2** — la table est incomplète |
> | Statut de l'écriture | **Refusée** | **Mise en attente**, et remontée au porteur |
> | Ce qu'il faut faire | Corriger l'écriture | Verser une ligne, ou déclarer le cas hors domaine |
>
> **Une lacune de table ne se répare pas en déplaçant un invariant** (§8.5.2bis.4) — et elle ne se sanctionne pas non plus comme une violation. Conséquence opérationnelle inscrite en **Annexe H §H.5.2** : le contrat qui contrôle R1 **met en attente** un couple absent, il ne le refuse pas. *Ancrage PR-29 :* `absent_n_implique_pas_violation` (`P− ↔ ∅` violation ; `C− ↔ E−`, lacune) et `le_statut_ne_se_lit_pas_sur_la_table` (même couple, deux statuts : **le statut dépend d'un fait extérieur à la table** — que le miroir soit inscrit ailleurs).
> 3. **Une lacune de la table est bloquante, et obligeante.** Ce que la table ne porte pas, le registre ne l'écrit pas. Compléter une ligne manquante n'est donc pas une amélioration facultative : c'est la levée d'une impossibilité d'inscription. `[OBLIGATION OUVERTE — porteur : porteur MRC / architecte ; horizon : institutionnel ; critère : toute ligne ajoutée déclare sa nature de relation et son arité.]`
>
> **Ce que la décision ne fait pas.** Elle ne complète aucune ligne : chaque lacune se traite cas par cas — verser une ligne, ou déclarer le cas hors domaine.
>
> **Condition de réfutation de la décision elle-même.** Elle tombe si l'on exhibe une écriture légitime — **soit attestée dans un régime déclaré du set (IFRS, PCG, CARE), soit attestée dans un registre de communalité dont les conditions de bonne formation sont satisfaites** — dont le couple ne figure pas dans la table **et** dont on établit qu'il ne doit pas y figurer. Le registre aurait alors à choisir entre l'exhaustivité et sa propre couverture.

> ### `[B7 — LES TROIS ARITÉS]`
>
> La colonne « Nature de la relation » connaît **trois** valeurs (§8.5.2bis.4) :
>
> | Arité | Définition | Ce que l'écriture doit déclarer |
> | :-- | :-- | :-- |
> | **intra-écriture** | Un seul acteur, deux côtés dans le même livre | rien de plus |
> | **inter-acteurs** | Deux acteurs, deux livres : le miroir est chez la contrepartie | l'identité de la contrepartie |
> | **inter-acteurs à trois livres** | Trois acteurs : la contrepartie d'un des côtés se trouve dans le livre d'un **tiers**, qui n'est partie ni au débit ni au crédit | **l'identité du tiers et la nature de ce qui s'inscrit chez lui** |
>
> **Cas attestés de la troisième arité.** Le don AMEP, où le `e` est du producteur, le `D−` du bénéficiaire et la contrepartie `C−` dans le livre du fournisseur de ce dernier (§8.5.2bis.4). Le **remboursement obligataire transitant par un agent payeur**, rencontré au jalon J1 sur le registre RATP. La **novation** — changement de créancier — où la dette s'éteint chez l'un et naît chez l'autre. Et, avec la décision 5, **le transfert de chose dont les obligations ne suivent pas le même chemin que la chose** : on cède un ouvrage en conservant la charge de remise en état, et l'obligation reste inscrite dans un troisième livre. *Ancrage PR-29 :* `trois_livres_sans_tiers_mal_formee`, `trois_livres_temoin_discriminant` ; `la_troisieme_arite_n_est_pas_la_deuxieme` — une écriture bien formée à deux livres, relue à trois, ne l'est plus : **le modèle à deux livres de PR-20 ne porte pas cette garde**.
>
> **Ce que cela rend possible.** Le contrôle de réciprocité de la table **est calculable sur les branches à deux livres** : un couple `X ↔ Y` d'arité inter-acteurs exige que la ligne `Y` porte `X` ; un couple d'arité intra-écriture ne l'exige pas, puisque les deux côtés sont dans le même livre ; un couple à trois livres exige que le tiers soit nommé. Sans cette distinction, le contrôle d'appartenance resterait sensible à la convention de lecture de l'analyste.

> **Le constat.** Sur une colonne « Nature de la relation » unique, la règle de réciprocité énoncée ci-dessus ne tient pas : **8 des 15 branches** notées inter-acteurs ou mixtes échouent au contrôle (`P+→D+`, `P−→C+`, `E+→D+`, `E+→C+`, `E+→D−`, `E−→C−`, `E−→D+`, `d→C−`), et **10** en lecture littérale du « + ». Le résultat du contrôle dépend alors d'une convention de lecture non déclarée ; les points (c) et (a) ci-dessous la déclarent. *Compilé :* `ProfRegPR29.la_colonne_d_origine_ne_satisfait_pas_B7`, `le_decompte_depend_de_la_lecture_du_plus`.
>
> **(c) Le « + » de la ligne `D−` est composite** — c'est la lecture de §8.5.4 : `C− + e` porte `C−` et porte `e`. Le « ou » des autres lignes reste une alternative.
>
> **(a) La colonne est dédoublée.** « Nature de la relation » seule désigne deux choses : **l'existence d'une contrepartie** et **le lieu de l'écriture**. La colonne *Lieu de l'écriture* (ci-dessous, dernière colonne) sépare les deux. **Trois** branches notées « inter-acteurs » sont des écritures **à un livre dont la contrepartie est nommée** (`P+→D+`, `P−→C+`, `E−→D+`) — `E+→D+` et `E+→C+`, que la table dit « **chez B** », sont à **deux livres** —, et `E+→D−` (mixte) aussi : le débit et le crédit sont dans le livre de A, l'autre acteur n'y figure que comme contrepartie. **La règle de réciprocité ne vaut que pour les branches à deux livres** — c'est la relation miroir, non la relation débit/crédit (`SondePCEDed.la_table_melange_deux_relations`). *Compilé :* `le_dedoublement_conserve_la_contrepartie` (aucune contrepartie n'est perdue) ; `branches_fideles_a_la_table` (27 branches, transcription contrôlée).
>
> **Restent quatre lacunes de table, et quatre seulement**, en deux familles : **la vie d'un apport** — `E+→C+` (l'apporteur acquiert sa créance : la ligne `C+` ne porte pas `E+`), `E+→D+` (la mise souscrite non versée : la ligne `D+` ne porte pas `E+`), `E−→C−` (la mise est rendue : la ligne `C−` ne porte pas `E−`) — et **l'extinction d'un droit par une prestation** — `d→C−` (la ligne `C−` ne porte pas `d`). Les lignes `C+`, `C−` et `D+` ne connaissent qu'un miroir de créance ou de dette ; elles ignorent l'engagement (`E`) et le résultat (`d`) que la table admet pourtant de l'autre côté (`sous_la_colonne_dedoublee_restent_quatre_lacunes`). *Relecture des 27 branches* : aucune affectation n'est contredite par le texte de la table. **Elles sont traitées cas par cas, comme toute lacune de table** (arbitrage A8 : mise en attente, remontée au porteur ; verser une ligne ou déclarer le cas hors domaine). `[OBLIGATION OUVERTE — porteur : porteur MRC / architecte ; horizon : institutionnel ; critère : chacune des **quatre** lacunes reçoit une ligne étendue (`C+`, `C−` ou `D+`), ou est déclarée hors domaine, avec sa raison.]`
>
> **Portée.** Les branches « cas par cas » (`D+ ↔ D−`) et la ligne composite `P+ + D+ ↔ P− + D−` ne sont pas contrôlées (la table formalisée ne porte que des typages simples). Les cinq théorèmes cités portent sur **un texte** : ils se comptent dans la **colonne texte** du décompte ProfReg. `[RÉSERVE DE MODÈLE — l'affectation d'un lieu à chaque branche est la lecture de l'instructeur, validée par le porteur.]`
>
> *Condition de réfutation.* Le dédoublement tombe si une branche notée « un livre » se révèle, sur un cas documenté, inscrite dans deux livres **sans** que sa contrepartie y soit un miroir — la colonne ne séparerait alors pas ce qu'elle prétend séparer. *Porteur :* porteur MRC / architecte. *Horizon :* institutionnel. *Critère :* le contrôle de réciprocité rejoué sur un cas J1 avec la colonne dédoublée.

| **Côté A (DÉBIT)** | **Côté B (CRÉDIT) — possibilités admises**                       | **Lecture intuitive**                                                  | **Nature de la relation** | **Lieu de l'écriture**  |
| ------------------ | ---------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------- | --- |
| P+                 | D+ (dette fournisseur), e (effort propre de A), ou **P−** en **intra-écriture seulement**  | A s'endette pour acquérir, A produit par son effort, ou **A déplace un poste de patrimoine vers un autre poste du même livre** | `D+` : **inter-acteurs** — `e` et `P−` : **intra-écriture** (un seul acteur, deux côtés). **Le transfert de chose ENTRE DEUX ACTEURS ne relève pas de cette ligne** : voir la ligne composite ci-dessous | `D+` : **un livre**, contrepartie nommée (le fournisseur) — `e`, `P−` : un livre |
| P−                 | C+ (créance sur acheteur), d (résultat servi), **P+** en **intra-écriture seulement**, ou **e**  | A vend à crédit, A solde par produit immédiat, **A déplace un poste de patrimoine vers un autre poste du même livre**, ou **A consomme son propre patrimoine par un effort qui ne va vers personne** | `C+` : **inter-acteurs** — `d`, `P+` et `e` : **intra-écriture**. La branche `e` exige `destinataire_effort = SANS_BENEFICIAIRE`. **Le transfert de chose ENTRE DEUX ACTEURS ne relève pas de cette ligne** | `C+` : **un livre**, contrepartie nommée (l'acheteur) — `d`, `P+`, `e` : un livre |
| **`P+ + D+`**  | **`P− + D−`** | **A acquiert une chose ET la position d'obligé qui l'accompagne ; B cède la chose ET en est libéré** | **inter-acteurs**. Seule forme admise du transfert de chose entre deux acteurs — vente, don, reprise. Condition de bonne formation : l'écriture **déclare le sort des `D` et `E` attachés à l'objet** — transférées, éteintes, ou conservées par le cédant. **Si les obligations vont à un tiers, l'arité est *inter-acteurs à trois livres* (B7) et le tiers est nommé** | deux livres ; trois si les obligations vont à un tiers (B7) — *ligne composite, non contrôlée par PR-29* |
| C+                 | D+ (dette du débiteur) — symétrie stricte                        | Toute créance d'un côté = dette de l'autre                             | **inter-acteurs** — objet de PR-20 | `D+` : **deux livres** |
| C−                 | D− (extinction de dette miroir)                                  | Règlement effectif d'un dû                                             | **inter-acteurs** — objet de PR-20 (ligne d'extinction) | `D−` : **deux livres** |
| E+                 | ∅ si non tracé ; D+ ou C+ chez B ; **e**, **E−** ou **D−**  | Engagement unilatéral possible (existentiel), contractuel symétrique, **né d'un effort de A**, **transféré depuis une autre composante d'engagement**, ou **né de l'extinction d'une dette exigible** — conversion d'une dette en capital | `D+`/`C+` : **inter-acteurs**, et **le seul cas où le second livre peut manquer** —  `SondePCEDed.seul_E_plus_admet_le_vide_table_1809`  *(porte sur la présente table, `E−` compris)*. `e` et `E−` : **intra-écriture**. **`D−` : mixte** — `D−` intra-écriture dans le livre de l'émetteur, contrepartie `C−` chez le créancier devenu apporteur. **Seconde ligne mixte de la table** | `∅` : sans second livre (asymétrie existentielle) —  `D+`, `C+` : **deux livres** (« chez B ») — **LACUNES : les lignes `D+` et `C+` ne portent pas `E+`** — `e`, `E−` : un livre — `D−` : un livre, contrepartie `C−` chez le créancier devenu apporteur |
| E−  | C− (extinction de la créance de l'apporteur), D+ (dette de distribution constatée) ou **d**  | A éteint un engagement structurel : distribution aux apporteurs, remboursement de capital, absorption d'une perte, ou **reprise d'un engagement constaté en excès** — rectification d'un exercice antérieur | `C−` et `D+` : **inter-acteurs**. **`d` : intra-écriture**, symétrique de la branche `e` de la ligne `E+`. `E−` n'hérite PAS de l'exception à `∅` : seul `E+` l'admet | `C−` : **deux livres — LACUNE : la ligne `C−` ne porte pas `E−`** — `D+` : un livre, contrepartie nommée — `d` : un livre |
| D+                 | C+ (créance miroir chez le créancier) ou **D−**  | Symétrie comptable standard, ou **une dette en remplace une autre** | `C+` : **inter-acteurs** — objet de PR-20. `D−` : **arité déclarée cas par cas** — *intra-écriture* si le créancier ne change pas (reclassement : dette fournisseur → effet à payer) ; ***inter-acteurs à trois livres*** si le créancier change (novation), et l'écriture **nomme alors l'ancien et le nouveau créancier** | `C+` : **deux livres** — `D−` : cas par cas (un livre si reclassement ; trois livres si novation) |
| D−                 | C− (extinction créance) + e (effort de A), ou **D+**  | Le remboursement consomme une dette par un effort effectif, ou **une dette en remplace une autre** | `C− + e` : **mixte** — `C−` inter-acteurs, `e` intra-écriture ; le « + » est un composite, non une alternative `[LECTURE — voir §8.5.4]`. `D+` : **arité déclarée cas par cas**, voir la ligne `D+` | `C− + e` : **composite** (« + » déclaré composite) — `C−` deux livres, `e` un livre — `D+` : cas par cas |
| e                  | d (résultat reçu par B désirant), D− chez B (si B créancier), **E+** ou **P−**  | Distingue l'effort marchand, l'effort de préservation, **l'effort qui fait naître un engagement** et **l'effort qui consomme un patrimoine** | `d` et `D−` : **inter-acteurs** (« chez B ») — `E+` et `P−` : **intra-écriture** (un seul acteur, deux côtés) | `d`, `D−` : **deux livres** — `E+`, `P−` : un livre |
| d                  | e (effort reçu de B) ou C− (extinction créance si B avait droit) | Tout produit reçoit comme miroir l'effort qui le contrepasse           | **inter-acteurs** dans les deux branches | `e` : **deux livres** — `C−` : **deux livres — LACUNE : la ligne `C−` ne porte pas `d`** |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Asymétrie autorisée — engagement existentielLe type E+ admet une exception au principe miroir. Un engagement pris envers un acteur non tracé (générations futures, biosphère planétaire, nappe fossile millénaire des Niayes) inscrit une primitive E sans miroir comptable explicite. Cette asymétrie est précisément l'objet de R-INTERDIT-ABSOLU (Couche 1, §2ter.1 ; statut formel : F3 §3.5) : l'engagement existentiel précède tout dispositif d'inscription. Le champ asymetrie\_existentielle = VRAI est levé sur ces cas.** |

#### 8.5.2bis Instruction du don — troisième asymétrie candidate **rejetée**, et deux lacunes de la table révélées

*(Proposition P6 — `Lecture_Numero74_Meso-ESS_x_MRC_2026-09-14.md`. Instruction complète : `Decision_P6_Don_Troisieme_Asymetrie_2026-09-14.md`. Cas support : Grassart & Sébert 2026, AMEP.)*

**La question.** P6 demande d'instruire, sur un cas, si une écriture de don constitue une **troisième asymétrie autorisée** de R1 aux côtés de la dette systémique et de l'engagement existentiel `E+`, ou si elle se type sans reste dans la table §8.5.2.

**Verdict : rejetée. Les asymétries autorisées restent deux — et cette instruction les éprouve.** §3bis énonce « deux, et seulement deux ». Un « seulement » non éprouvé est une affirmation ; il devient un résultat quand un candidat sérieux échoue. **C'est le cas ici, et c'est le premier apport de P6.**

**8.5.2bis.1 Le cas.** Les AMEP (Associations pour la Mutualisation d'une Énergie de Proximité, 22 en service en 2026) ne facturent pas le surplus photovoltaïque aux consommateur·ices de la boucle : *« Plutôt que de facturer le surplus aux consommateur·ices de la boucle, elles en font don à ces derniers »*, foyers en précarité énergétique ou associations locales. C'est le cas limite recherché : un flux sortant sans contrepartie exigée du récipiendaire.

**8.5.2bis.2 Le typage — la table absorbe, par deux branches déjà présentes**

| Branche | Côté A (donateur) | Côté B | Ligne de §8.5.2 mobilisée |
| --- | --- | --- | --- |
| **Flux** | `e` — effort fourni, signe `neutre`, `destinataire_effort = CLIENT` ou `INDIFFERENT` | `d` — résultat reçu par B désirant | ligne `e`, première branche |
| **Extinction** | `e` | `D−` — la dette de B envers **son fournisseur** diminue | ligne `e`, seconde branche |

La seconde branche n'est pas une reconstruction : l'article l'établit sur le mécanisme même de l'autoconsommation collective — *« les consommateur·ices en question réduisent les flux de consommation pourvus par chacun de leurs fournisseurs : c'est autant de kWh déduit de leur facture »*.

**Conséquence.** Aucun miroir ne manque, donc **aucune asymétrie**.

**8.5.2bis.3 Ce que l'hypothèse adverse de P6 disait, et pourquoi elle est fausse aussi**

P6 posait l'écriture comme « le donateur inscrit un `e` ; le bénéficiaire reçoit un `P` sans contracter de `D` », et l'hypothèse adverse comme « un **transfert de patrimoine** sans engagement, qui se type sans reste ». **Les deux formulations sont mal formées, et de la même façon.**

- Le couple `e ↔ P+` **ne figure pas dans la table**. La ligne `e` n'admet jamais `P+`.
- La ligne `P+` admet `e` — mais cette occurrence est déclarée **intra-écriture** par la colonne « Nature de la relation » : « un seul acteur, deux côtés », lecture « A produit par son effort ». La lire comme un don entre deux acteurs, c'est **remélanger les deux relations que cette colonne a séparées** (`SondePCEDed.la_table_melange_deux_relations`).
- Enfin l'électricité partagée n'est pas un patrimoine : c'est un **flux**, de signe `neutre` au sens de §8.5.1bis — « un effort et un résultat ne s'augmentent ni ne s'éteignent, ils passent ».

**P6 a le bon cas et la mauvaise écriture.** Le typage correct est `e ↔ d` / `e ↔ D−`, disponible sans rien ajouter.

**8.5.2bis.4 Deux lacunes de la table, révélées par l'instruction — et ce ne sont pas des asymétries**

> **Lacune 1 — l'arité.** Le don AMEP exige **trois** arités : le `e` est du producteur, le `D−` est du bénéficiaire, et la **contrepartie `C−` est dans le livre d'un troisième acteur — le fournisseur**. La même chose vaut du TURPE, de l'accise et de la TVA, qui restent dus par le bénéficiaire à des tiers *« indépendamment de leurs fournisseurs »* : **la gratuité du don ne rend gratuite aucune des dettes que le bénéficiaire porte par ailleurs.** Le mot « miroir » désigne ici une troisième chose : la valeur *inter-acteurs à trois livres* est portée à la colonne « Nature de la relation » (encadré B7 de §8.5.2). `[Reste ouverte la reprise ligne à ligne de l'arité des onze lignes existantes.]`

> **Lacune 2 — le don d'une chose.** Le don d'un bien durable — un local, un véhicule, un stock — n'a pas de ligne simple : ses deux côtés sont des `P`. Ce n'est pas la gratuité qui le rend intypable comme couple simple ; c'est qu'un transfert de chose entre acteurs emporte les obligations attachées. Il se type par la ligne composite `P+ + D+ ↔ P− + D−` (§8.5.2ter, décision 5).

**Pourquoi aucune des deux n'est une asymétrie, et pourquoi ce point est décisif.** Une asymétrie autorisée est un cas où **le miroir est légitimement absent** — la dette systémique n'a pas de débiteur, l'engagement existentiel n'a pas d'acteur tracé. Ici le miroir **existe** : il est dans le livre du fournisseur (lacune 1), ou dans celui du récipiendaire (lacune 2). Ce qui manque est la **ligne qui les apparie**, non la contrepartie elle-même. Déclarer asymétrique un miroir présent serait un `[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ]` — et coûterait une modification de **Couche 1** là où le défaut est en **Couche 2**. **Une lacune de table ne se répare pas en déplaçant un invariant.**

**8.5.2bis.5 Le critère de vérification de P6**

P6 demande « une écriture test AMEP versée à l'Annexe K, avec `respect_R1` renseigné ». **Il n'existe pas de champ `respect_R1`** : le respect de R1 est un **contrôle calculé** — et PR-21 (`le_champ_ajoute_un_degre_de_liberte`) démontre que le renseigner rouvrirait exactement la **cinquième forme de sur-revendication** (§8quinquies).

**Critère retenu :** l'écriture test est bien formée si le couple (`typage_primitive`, `typage_miroir`) **appartient** à la table — ce qui se **calcule** —, et la fiche de cas déclare, le cas échéant, l'arité de la relation et le livre tiers où se trouve la contrepartie. **Rien à renseigner sur le respect de R1 : il se vérifie.**

**8.5.2bis.6 Ce qui n'est pas fait**

`[CAS NON CHIFFRÉ.]` L'article de Grassart & Sébert est une enquête qualitative : il ne donne **ni kWh, ni euros, ni clé de répartition**. L'écriture test est donc établie en **type**, non en montants, et **n'est pas versée à l'Annexe K**, qui est une annexe de cas chiffrés. La verser sans chiffres en ferait un cas d'usage sans cas.

`[AUCUNE PREUVE FORMELLE.]` Régime procédural. Rien ici n'est démontré : l'appartenance du couple à la table est une lecture de la table, et les deux lacunes sont des constats d'absence de ligne.

#### 8.5.2ter Sept décisions du porteur : les lignes ajoutées, la ligne composite de transfert, le renvoi de l'exigibilité à la couche R, et la couverture des seize mouvements

`[Origine : jalon J1, typage des 106 faits de mouvement du registre de données fiabilisées du groupe RATP 2025 (`PPC/RATP/J1_typage_PCEDed_RATP_2025.json`, `PPC/RATP/Rapport_J1_J2_RATP_2026-09-18.md`).]`

##### Ce que le jalon J1 exhibe

Le registre RATP est le premier corpus du set à présenter des écritures **attestées par des commissaires aux comptes, dans un régime déclaré (IFRS), en nombre**. Confrontées aux seules lignes d'origine de la table §8.5.2, **33 des 68 écritures n'y trouvent aucun couple**, et la table ne type que **4 des 16 mouvements régime-invariants de §8.3** : ni l'achat comptant — l'exemple canonique que §8.3 donne elle-même du mouvement `a` —, ni la charge payée comptant, ni la vente comptant d'un service.

Le diagnostic isole **trois causes distinctes**.

##### Décision 1 — la ligne `P+ ↔ P−`, et le diagnostic de la LACUNE 2

**Cause.** Cinq des six primitives désignent un rapport entre acteurs : `C` un droit contre quelqu'un, `D` une obligation envers quelqu'un, `E` une promesse faite à quelqu'un, `e` un effort pour quelqu'un, `d` un résultat servi à quelqu'un. **Une seule, `P`, désigne un état — une chose tenue.** Les lignes d'origine apparient un état à un rapport ; elles n'apparient pas deux états.

**Le diagnostic.** La LACUNE 2 de §8.5.2bis.4 — le don d'un poste — ne tient pas à la gratuité. Ce qui rend le don d'une chose intypable est que ses deux côtés sont des `P` ; la gratuité retire seulement le `D+` ou le `C+` qui aurait fourni la contrepartie relationnelle. **Le même défaut frappe l'achat comptant** — où la dette naît et s'éteint dans le même instant, donc n'est jamais inscrite — **et l'arbitrage entre deux postes de trésorerie**. Sans cette ligne, la table type le crédit et non le comptant ; la portée du défaut est trois fois plus large que le cas AMEP ne le laisse voir.

**La ligne.** `P+ ↔ P−`, d'**arité intra-écriture** :

| Cas | Arité | Exemple |
| :-- | :-- | :-- |
| Acquisition décaissée ; arbitrage entre deux postes de patrimoine | **intra-écriture** (un acteur, deux côtés) | Achat d'une immobilisation au comptant ; virement d'un dépôt à terme vers la trésorerie |

Le transfert d'une chose entre deux acteurs — vente au comptant, don d'un bien durable — relève de la ligne composite (décision 5).

**Condition de réfutation.** La ligne est à retirer si l'on établit que la sous-couche T ne doit typer que les écritures porteuses d'une obligation ou d'un effort — auquel cas c'est le **domaine** de la table qu'il faut borner explicitement, et non ses lignes qu'il faut ajouter. Des deux voies, le porteur retient l'ajout : un défaut de table appelle une ligne, non une tolérance.

##### Décision 2 — la ligne `E−` et le rabattement de `S'`

Voir **§8.5.1ter** pour la décision de rabattement elle-même. La ligne `E−` en est la contrepartie nécessaire dans la table : **elle s'impose de toute façon**, indépendamment du rabattement, puisque les distributions aux apporteurs et les absorptions de pertes existent dans tous les régimes. Une table qui typerait l'augmentation d'un engagement structurel et non son extinction ne serait pas symétrique.

`E−` **n'hérite pas** de l'exception à `∅` : seul `E+` l'admet, et l'asymétrie existentielle porte sur la *naissance* d'un engagement envers un acteur non tracé, jamais sur son extinction. **Les asymétries autorisées restent deux** — §3bis n'est pas touché.

##### Décision 3 — la valeur `SANS_BENEFICIAIRE`

**Cause.** L'amortissement n'est ni un `P ↔ P` ni un problème de `S'` : c'est une **consommation de patrimoine sans bénéficiaire**. Son miroir devrait être un `e`, mais `e` est défini comme un effort « en faveur d'un autre », et l'amortissement n'est en faveur de personne.

**Détail révélateur, et il porte sur l'architecture de F8.** En régime CARE, la même écriture se type `(e, D−)` et **passe**, parce que CARE fournit le créancier manquant — la communauté NH représentée par son consortium. La sous-couche T, présentée comme le typage ontologique propre au MRC, orthogonal au régime, aurait donc, sans la présente décision, **une couverture variable selon le régime** ; la décision rend l'écriture typable dans les deux régimes.

**Ce qui est ajouté — une valeur ET une branche.** `destinataire_effort = SANS_BENEFICIAIRE` (§8.5), **et** la branche `e` de la ligne `P−` de §8.5.2, symétrique de la branche `e` que porte la ligne `P+` : là où `P+ ↔ e` se lit « A produit par son effort », `P− ↔ e` se lit « A consomme son patrimoine par un effort ». Le couple de l'amortissement, de la dépréciation, de la perte fortuite et de la destruction est `(P−, e)`, et **cette branche n'est bien formée que si `destinataire_effort = SANS_BENEFICIAIRE`** — condition de champ, du même genre que celle de §8.2bis, et non un signal. Elle se distingue de `INDIFFERENT` comme `AUCUN` se distingue de `NON_DETERMINABLE` en §8.2bis : **`SANS_BENEFICIAIRE` est un résultat — il n'y a personne —, `INDIFFERENT` est un bénéficiaire réel dont l'identité n'importe pas.** Les confondre inverserait le sens de toute lecture agrégée des efforts.

**L'option écartée.** Déclarer une **troisième asymétrie autorisée** pour la consommation sans bénéficiaire toucherait la Couche 1 et le §3bis, dont le « deux, et seulement deux » est éprouvé par l'instruction du don. Le défaut étant en Couche 2, il est réparé en Couche 2. **Une lacune de table ne se répare pas en déplaçant un invariant** (§8.5.2bis.4).

##### Décision 4 — la ligne `e ↔ E+`, l'engagement né d'un effort

**Cause.** La famille `e` se type dans quatre directions. `P+ ↔ e` type **le patrimoine né d'un effort** — « A produit par son effort ». `P− ↔ e` (décision 3) type **le patrimoine consommé par un effort**. `e ↔ d` et `e ↔ D−` typent **l'effort qui sert un tiers**. La quatrième est **l'engagement né d'un effort** : une charge inscrite en contrepartie d'un passif que l'acteur se reconnaît sans qu'il soit exigible.

**Le cas qui l'exhibe.** Les dotations nettes aux provisions du groupe RATP (`ratp:NetAdditionsToProvisions`, exercices 2024 et 2025), seules écritures du corpus que les décisions 1 à 3 ne typent pas. Une dotation aux provisions est exactement cela : un effort de l'exercice qui constate un engagement futur non exigible.

**La ligne.** `e ↔ E+`, **arité intra-écriture** — un seul acteur, deux côtés. C'est ce qui la distingue des deux branches marchandes de la ligne `e`, toutes deux inter-acteurs : l'engagement naît **chez A**, pas chez B. La réciproque est portée par la ligne `E+`, qui accueille `e` par la même décision.

**Ce que la ligne ne fait pas.** Elle ne type pas l'engagement né d'un effort **envers un créancier identifié** : ce couple est `(e, D+)` — une charge à payer, non une provision — et il **reste absent de la table** (décision 6 ci-dessous).

**Réciprocité.** La table pose ses couples de façon **réciproque** — `C+ ↔ D+` figure aussi bien en ligne `C+` qu'en ligne `D+`. La ligne `e` porte donc aussi `P−`, réciproque de la branche `P− ↔ e` de la décision 3. Aucun couple n'est créé par là ; la convention de lecture de la table est respectée.

**Condition de réfutation.** La ligne tombe si l'on établit qu'une provision n'est pas un effort de l'exercice mais une simple réévaluation de passif — auquel cas son côté A ne serait pas `e` et le couple serait à chercher ailleurs. Le débat existe en doctrine comptable ; le porteur tranche pour la lecture « effort ».

##### Décision 5 — le transfert de chose est composite, et le `P ↔ P` est réservé à l'intra-écriture

**Ce qui rend le défaut visible.** La construction de la correspondance `M × relation → T` (§8.5.5) oblige à déclarer la relation de chaque cellule, et donc l'arité du mouvement `a`.

**Le défaut.** **Un transfert de chose entre deux acteurs n'est jamais un pur échange de patrimoines.** Celui qui acquiert la chose acquiert la **position d'obligé** qui l'accompagne — entretien, conformité, traitement en fin de vie, et dans la grammaire CARE la dette envers les capitaux NH que la chose incorpore. Celui qui la cède en est libéré. Une écriture `P+ ↔ P−` inter-acteurs n'inscrit que le mouvement de la chose : **elle est amputée des obligations qui la suivent.**

**Ce qui est retenu.**

| Cas | Typage |
| :-- | :-- |
| Arbitrage entre deux postes du même livre | `P+ ↔ P−`, **arité intra-écriture** |
| Acquisition au comptant, dans le livre de l'acquéreur | `P+ ↔ P−`, intra-écriture |
| **Transfert de chose entre deux acteurs** — vente, don, reprise | **`P+ + D+ ↔ P− + D−`**, ligne composite. **Le `P ↔ P` inter-acteurs n'est pas admis** |

**Condition de bonne formation.** Toute écriture composite de transfert **déclare le sort des `D` et `E` attachés à l'objet** : **transférées** au cessionnaire, **éteintes**, ou **conservées par le cédant** — on vend une mine en gardant la charge de remise en état. En arité intra-écriture, aucune obligation n'est transférée et le pur `P ↔ P` est complet ; c'est le seul cas où il l'est.

**Ce que la décision établit.** L'absence d'un `P ↔ P` inter-acteurs n'est pas une lacune : un pur `P ↔ P` inter-acteurs est une fiction qui n'existe qu'en laissant tomber les obligations. La LACUNE 2 sur le don d'une chose se lit de même — on donne des terrains pollués précisément parce que le don transfère les charges. **Ce qu'il faut n'est pas la ligne simple, c'est le composite** ; l'arité n'est pas un détail de tenue de livre, elle détermine si l'écriture est complète.

**Ce que la décision apporte au cas RATP.** Quand Île-de-France Mobilités reprend le matériel roulant à sa valeur nette comptable, l'obligation d'entretien et la dette NH incorporée dans l'acier trouvent où s'inscrire. Le jalon J2 établit que la RATP n'a aucun droit de disposition sur cette matière ; la décision 5 fournit la forme d'écriture qui le dit.

**Condition de réfutation.** La décision tombe si l'on exhibe un transfert de chose entre deux acteurs dont on établit qu'il ne transfère, n'éteint ni ne laisse aucune obligation — auquel cas le pur `P ↔ P` inter-acteurs devrait être admis. `[L'arité à trois livres (B7) est ici requise : le cessionnaire des obligations n'est pas toujours le cessionnaire de la chose.]`

##### Décision 6 — la distinction provision / charge à payer relève de la couche R, non de la couche T

**La question.** La décision 4 porte `e ↔ E+` : l'engagement **non exigible** né d'un effort — la provision. Le couple `e ↔ D+` — l'engagement **exigible** né d'un effort, c'est-à-dire la charge à payer — n'y figure pas. Faut-il verser la ligne ?

**La décision : non.** La frontière entre provision et charge à payer est **une question de droit comptable**, qui varie selon les régimes et selon l'appréciation de l'exigibilité. Elle relève de `C-MOUVEMENT-TYPE.R`, qui porte déjà `denomination_regime`, `compte_imputation` et `conditions_reconnaissance`, et non de `C-MOUVEMENT-TYPE.T`, qui type la **nature ontologique de la relation**.

**Conséquence pratique.** Une écriture qui constate un engagement né d'un effort se type `e ↔ E+` **dans tous les régimes**. C'est la couche R qui dit ensuite si le régime la comptabilise en provision — IAS 37, comptes 15x du PCG — ou en charge à payer — comptes 408, 428 et suivants. Aucune ligne nouvelle n'est versée en T.

> **Une tension est ouverte par cette décision, et elle est déclarée plutôt que lissée.** `[INCOHÉRENCE À INSTRUIRE — niveau 2.]` §8.5.1 distingue `E` de `D` **par l'exigibilité** : `E` est une « promesse […] sans exigibilité contractuelle immédiate », `D` une « obligation exigible ». Si l'exigibilité relève de la couche R, **le critère qui sépare les deux primitives de T est un critère de R.**
>
> Deux façons de tenir l'ensemble, et le porteur n'a pas tranché entre elles :
>
> 1. **Lecture temporelle.** `E+` type l'engagement **à sa naissance**, avant que le régime n'ait déterminé son exigibilité. `D` reste réservé aux obligations dont l'exigibilité est établie et le créancier identifié — la dette contractée, non l'engagement constaté. La définition de §8.5.1 est alors à préciser, non à changer.
> 2. **Amendement de §8.5.1.** Distinguer `E` de `D` par **l'identification du créancier** plutôt que par l'exigibilité. C'est plus cohérent avec la ligne `E+ ↔ ∅`, où l'absence de miroir tient à ce que l'acteur n'est pas tracé — donc au créancier, non à l'exigibilité.
>
> **La seconde est plus propre et plus coûteuse** : elle touche une primitive, et §8.5.1 en compte six. `[OBLIGATION OUVERTE — porteur : porteur MRC / architecte ; horizon : institutionnel ; critère : §8.5.1 énonce sans ambiguïté ce qui sépare `E` de `D`.]`

**Ce que la décision reconnaît implicitement.** Le jalon J1 montre que la sous-couche T, présentée comme ontologique et orthogonale au régime, a en pratique **une couverture qui varie selon le régime** — sans la décision 3, l'amortissement se type en CARE et non en IFRS. La décision 6 va dans le même sens et l'assume : **T ne type pas indépendamment de R, elle type ce que R laisse indéterminé.** C'est une position défendable ; elle n'est simplement pas celle que §8.5 annonce.

##### Décision 7 — les trois derniers trous : `b`, `i` et `o`

`[Décision prise au vu de la table de correspondance §8.5.5, qui isole trois mouvements que les décisions 1 à 6 ne couvrent pas.]`

**`o` — la branche `d` de la ligne `E−`.** Sans elle, la ligne `E+` aurait sa branche `e` — l'engagement né d'un effort — et la ligne `E−` n'aurait pas sa branche `d` : `p` serait couvert et `o` ne le serait pas — asymétrie de versement, non propriété du modèle. La branche `d` : *A reprend un engagement constaté en excès, et un produit apparaît* — la rectification d'un exercice antérieur. Arité **intra-écriture**, symétrique de `E+ ↔ e`. **Le couple `o`/`p` est symétrique.**

**`b` — une dette en remplace une autre, et le pendant n'est pas symétrique de `P+ ↔ P−`.** Les lignes `D+` et `D−` s'apparient. Mais **aucun composite n'est requis**, et c'est la différence avec la décision 5 : dans un transfert de chose, les obligations *suivent* la chose et doivent être inscrites en plus ; dans un reclassement de dette, **l'obligation est l'objet même du mouvement**, il n'y a rien qui l'accompagne. L'arité fait tout le travail :

| Cas | Arité | Ce que l'écriture déclare |
| :-- | :-- | :-- |
| Reclassement — dette fournisseur devenue effet à payer, **même créancier** | **intra-écriture** | rien de plus |
| **Novation** — le créancier change | ***inter-acteurs à trois livres*** (B7) | **l'ancien et le nouveau créancier**, dont les livres portent respectivement `C−` et `C+` |

La novation mobilise la troisième arité (B7). **Sans elle, la ligne `D+ ↔ D−` serait ambiguë** : on ne saurait distinguer un changement d'instrument d'un changement de créancier.

**`i` — la conversion d'une dette en capital, et c'est la plus intéressante des trois.** La ligne `E+` accueille `D−`. Ce que l'écriture inscrit n'est pas un transfert mais **un changement de régime d'obligation** : ce qui était exigible envers un créancier devient structurel envers un apporteur, et **c'est le même acteur qui change de position**. L'arité est **mixte** — `D−` et `E+` sont tous deux dans le livre de l'émetteur, la contrepartie `C−` est chez le créancier devenu apporteur. C'est la **seconde ligne mixte** de la table, après `D− ↔ C− + e`.

> **Pourquoi ce cas mérite d'être signalé au-delà de la table.** La conversion d'une dette en capital est, dans la grammaire du MRC, **l'opération par laquelle une dette écologique pourrait devenir un engagement statutaire** : une `DETTE_NATURELLE` exigible envers un consortium de gouvernance NH se convertirait en engagement inscrit aux statuts — ce que le couplage « société à mission » de l'Annexe H §H.10.2 rend juridiquement pensable. **La ligne existe ; le cas d'usage, lui, reste à instruire.** `[À INSTRUIRE — arbitrage A5.]`

**Ce que les trois lignes établissent, et ce qu'elles posent.** La couverture des seize mouvements est de **16 sur 16**. La question posée en A1 en devient plus pressante : **si T couvre les seize mouvements, qu'ajoute-t-elle à M ?** La réponse est dans la structure de §8.5.5 et non dans le décompte : **T n'ajoute rien à la géométrie, elle ajoute la relation.** Un même mouvement se type différemment selon la relation déclarée — `e` donne `P+ ↔ D+` pour un achat à crédit et `C+ ↔ D+` sous IFRIC 12 ; `b` donne un reclassement ou une novation selon l'arité. **La couverture complète ne rend pas T redondante : elle rend visible que la correspondance est une fonction à deux arguments, et qu'un seul des deux vient de M.**

**Condition de réfutation des trois lignes.** Elles tombent si l'on exhibe, pour l'une d'elles, une écriture licite dont le typage contredit la lecture retenue : un reclassement de dette qui transférerait une obligation à un tiers (ce qui ferait de `b` un composite, contre la décision 7) ; une conversion de dette en capital où le créancier ne deviendrait pas apporteur (ce qui invaliderait l'arité mixte de `i`) ; une rectification d'exercice antérieur qui ne passerait pas par les capitaux propres (ce qui sortirait `o` du domaine de `E−`).

##### Effet mesuré sur le registre RATP

Le jalon J1 est rejoué sur la table amendée : `PPC/RATP/J1bis_effet_amendement_F8_2026-09-18.json`. **Les 56 écritures RATP informatives ont toutes un couple dans la table : le corpus RATP est intégralement typable.** La couverture des seize mouvements de §8.3 est établie en §8.5.5.

##### Statut de ces décisions

`[AUCUNE PREUVE FORMELLE.]` Régime procédural. Ces lignes sont des **décisions de porteur**, prises sur un constat d'absence de ligne établi par appartenance à une table — ce qui se lit, ne se démontre pas. La proposition initiale a été formulée par un assistant (Claude) sur instruction du porteur ; `R-INCAPACITE-LLM-VALIDER` s'applique à la proposition, non à la décision, qui est celle du porteur.

#### 8.5.3 Types composites — règle constitutive retenue

Conformément à l'arbitrage 11.3 de la note de cadrage actualisée (option A retenue, cf. livrable K1 × K3 et note d'approfondissement), les types composites X + Y sont autorisés.

> Les composites sont **autorisés et rares** : des cinq cas du tableau ci-dessous, trois relèvent de la couche R, un de la relation inter-acteurs, un se résout en `e` seul.
>
> **Composites en vigueur dans le set.**
>
> | Composite | Ce qu'il type | Origine |
> | :-- | :-- | :-- |
> | **`P+ + D+ ↔ P− + D−`** | **Transfert d'une chose entre acteurs** — la chose et la position d'obligé qui l'accompagne. L'écriture déclare le sort des `D` et `E` attachés : transférées, éteintes, ou conservées par le cédant | décision 5 (§8.5.2ter) |
> | **`P+ + D+ ↔ C+`** | **Détention d'une chose dont les utilités sont dues à des membres identifiés** — même forme que le précédent, contenu différent : le `D+` n'est pas l'obligation attachée à une chose transférée, c'est **l'usage dû**. Voir §8.5.6 | **A3** (§8.5.6) |
> | **`D− ↔ C− + e`** | Remboursement par effort effectif | table d'origine |

| **Cas type composite**                 | **Composite**           | **Cas attesté**                                                                   |
| -------------------------------------- | ----------------------- | --------------------------------------------------------------------------------- |
|  **→ couche R** |  | **Décision du porteur.** Ce n'est pas un composite de la couche T : c'est **une chose, deux régimes de qualification** — « au sens juridique » / « au sens CARE » (Annexe K §K.6.1). Voir §8.4bis. |
|  **→ couche R** |  | Idem — animal-bien dans un régime, créance éthologique dans un autre |
|  **→ couche R** |  | Idem — transmissible dans un régime, créance des générations futures dans un autre |
|  **→ relation inter-acteurs** |  | **Décision du porteur.** La barre oblique, seule du tableau, désigne deux acteurs : c'est l'objet de **PR-20**, non un composite |
|  **→ `e` seul, sous condition CONV-11** |  | **Décision du porteur**, **conforme à l'Annexe K §K.6.3** : l'extinction partielle de dette n'est pas une seconde nature de l'écriture. Elle n'est pas pour autant une glose : **la condition de bonne formation CONV-11 (§8.5.3bis) en est la contrepartie obligatoire.** |

#### 8.5.3bis Les charges de personnel — `e` seul, et la condition de bonne formation qui en est la contrepartie

*Décision du porteur. Instruction : `Contre_Decision3_Bensadon_2026-09-08.md`, `Verification_Vuattoux_x_Contre_Decision3_2026-09-08.md`, `Instruction_PR20_x_Condition_v2_2026-09-08.md`.*

**Ce qui est décidé.** Les charges de personnel se typent **`e` seul**. L'extinction partielle de dette humaine relève de la **transition** (patron `transition_valide`), non du typage : inscrire l'effet dans le type ferait porter au typage ce que la machine d'états porte.

**Ce qui est instruit contre, et qui n'est pas écarté.** Dans le régime CARE, la charge de personnel a bien deux faces. Richard, Bensadon & Rambaud (*Comptabilité financière*, 11ᵉ éd., Dunod, 2018, ch. 18 §5) posent le principe fondateur du modèle : traiter les êtres humains « **non pas comme une charge** […] **mais comme un passif** », l'usage fait d'eux étant « une sorte de dette sociale et écologique qu'il est nécessaire de **rembourser** » (p. ~310). Typer `e` seul est donc, pris isolément, le traitement contre lequel CARE se définit — et le manuel ajoute que « les concepts de charge et de résultat sont **subjectifs** : ils dépendent de la vision qu'imprime à la comptabilité une personne dominante » (p. 666). **Le choix du typage n'est pas un rangement : il inscrit un point de vue de lecture.**

**Pourquoi `e` seul tient malgré cela.** Sur l'exemple chiffré du même manuel (p. 313-316), CARE-TDL ne porte **ni un type à deux faces ni un type et un effet** : il porte **deux mouvements dans deux sections**, « Charges sur capital humain — amortissements 21 750 » en exploitation, et « Charges internes pour maintien 18 000 » face au produit « Restauration du capital humain 21 500 » en activités de maintien. **Le composite `e + D−` ne décrit donc pas davantage CARE que `e` seul** ; ce qui décrit CARE, c'est `e` **plus** un mouvement de maintien doté de sa contrepartie. C'est cette seconde moitié que la condition ci-dessous rend obligatoire.

> **CONV-11 — condition de bonne formation, contrepartie obligatoire du typage `e` seul.**
> *(Énoncé canonique et instruction : Annexe méthodologique **§A.15.4** ; table de la série : **§A.15**.)*
>
> Une écriture typée `e` dont l'apporteur de l'effort figure comme créancier dans le régime déclaré est **bien formée seulement si** le mouvement de maintien correspondant fait l'objet d'une **inscription structurée** — **porteur, contrepartie, solde, horizon, critère de vérification** — et si l'écriture **nomme le registre qui la porte**.
>
> **Le registre financier n'est pas requis.** Le registre de communalité, ou un rapport extra-financier dont les champs requis sont renseignés, satisfait la condition. Elle **n'est pas** satisfaite par une mention en langue naturelle sans champ propre, **quel que soit le document qui la porte — bilan compris**.

**Le défaut visé est la forme de l'inscription, jamais son lieu.** Un critère opposant le passif et l'annexe, sur le patron des provisions pour retraites (manuel, p. 681, art. 335-1 PCG : « une simple information en annexe suffit, bien que cette position, à notre avis, ne soit pas conforme ») **est écarté par le porteur** : subordonner la bonne formation d'une écriture de communalité à sa traduction au bilan ferait du régime financier l'arbitre du registre de communalité. Ce qui en est retenu est que la mention **non structurée** n'a ni contrepartie, ni solde, ni horizon — rien ne s'en calcule, aucun tiers ne la conteste point par point.

**Sens de « bien formée » ici.** Patron de R0-bis (Annexe §A.14.3) : un prédicat **décidable sur l'inscription seule**, qui **ne juge pas le fond** (une écriture bien formée peut être fausse ou contestée), et dont le défaut produit **un marqueur nommé**, non une sanction. Conformément à §8quater, la condition doit être **conclue** par un théorème, jamais posée en hypothèse. *— conclue sur des instances, par des témoins des deux côtés ; un théorème qui la pose en hypothèse n'en est qu'une lecture (§8ter-bis, R-3).* `[RÉSERVE DE NOMMAGE]` `BienFormee` est déjà un prédicat de PR-10 et **ne porte pas** cette exigence (`BienFormee_ne_borne_pas_le_quintuplet`) : CONV-11 est un **second prédicat nommé**, ou une extension déclarée du premier — jamais un élargissement tacite.

`[CONDITION DE RÉFUTATION]` CONV-11 tombe si l'on exhibe un régime où l'apporteur de l'effort figure comme créancier et où la lecture de la priorité n'exige aucun solde ; ou une mention non structurée à partir de laquelle un tiers calcule effectivement l'écart.

**Pourquoi la contrepartie n'est pas une précaution mais une condition.** R-PRIORITE-CREANCIERS (§8.7) n'opère pas sur ce qui a été payé mais sur **l'écart entre le dû et le payé** — et le manuel l'établit sur son propre exemple : « le résultat est basé sur les **budgets prévus** de maintien », l'écart de fin de période attestant, le cas échéant, « d'une **défaillance** de l'entreprise » (p. 315-316). Un écart ne se calcule qu'entre deux grandeurs inscrites. **Sans inscription du mouvement de maintien, la règle de priorité n'a pas d'assiette.** Sur les chiffres de l'Annexe K, il resterait ≈ 31 000 € de charge qui ne disent rien de 2 901 312 € de dette humaine.

**Préalable de couche 0.** Le mot **dette** désigne deux objets distincts dans la littérature CARE, et le typage `e` seul n'a pas la même réponse selon celui que le set retient :

| | Construction | Ce qui est au passif | Le paiement du salarié est… |
|---|---|---|---|
| **A** | Richard, Bensadon & Rambaud 2018, ch. 18 §5 | **le capital apporté** (« Employé 43 500 » dès l'ouverture) | **un remboursement** |
| **B** | Vuattoux, « CARE et dialogue social », §1.1 | **l'écart non financé** (« la dette qui apparaît lorsque ces conditions ne sont pas financées ») | **une non-création de dette** |

> **Le set retient la construction A**, et c'est vérifiable sur ses propres chiffres : l'Annexe K §K.6.2 inscrit « dettes humaines — salaires décents long terme **2 901 312 €** », soit un **stock de coût de maintien**, non un écart de sous-financement. La déclaration est faite ici pour éviter un `[CHANGEMENT DE BASE NON TRACÉ]` : sous la construction B, le remboursement n'est pas un mouvement et CONV-11 serait sans objet.

`[LACUNE DE COUVERTURE — ouverte]` R-PRIORITE-CREANCIERS hiérarchise des **classes** de créanciers. Vuattoux (§4.4) documente une **sélectivité à l'intérieur** de la classe humaine — entre quatre dimensions non substituables (santé physique, santé psychosociale, identité professionnelle, sécurité économique) et entre statuts d'emploi : « la majorité des situations restées sans arbitrage concernait les salariés en parcours d'insertion plutôt que les permanents ». Le salaire relève de la *sécurité économique*, « qui connaît les arbitrages les plus rares ». **Une règle de priorité qui ne connaît qu'un créancier « humain » ne mord pas sur cette sélectivité.** À instruire séparément ; la non-substituabilité des quatre dimensions est un **invariant candidat**, absent du set.

 **PR-23 est écrit et compilé** : `ProfReg/PR23_MouvementDeMaintien.lean`. Il ne démontre pas CONV-11 — une obligation se déclare — mais il la **motive** et la **borne**, sur le patron de PR-10 §7 : `BienFormee_ne_borne_pas_le_maintien` exhibe le trou ; `deux_dettes_distinctes_meme_ecriture` et `priorite_sans_assiette` établissent que **sans inscription du maintien, deux dettes d'écarts différents sont indiscernables au registre et R-PRIORITE-CREANCIERS ne rend aucun verdict** ; `CONV11_satisfaite_sans_registre_financier` vérifie que la condition ne réintroduit pas le critère du bilan écarté par le porteur ; et `PR23_ne_certifie_pas_le_nommage` **démontre la lacune** plutôt que de la concéder. Ce qui suit reste vrai de PR-20 seul :

`[ÉTAT DE FORMALISATION]` **CONV-11 n'est pas un corollaire de PR-20.** Confrontation faite : l'équivalence **du registre comptable augmenté** porte sur **l'existence** du lien, non sur sa valorisation — L2 ne dispose d'aucune arithmétique, et `pFin` est à valeurs dans un type quelconque (le témoin de `registre_augmente_non_equivalence` fait porter au registre **financier** des booléens). Sur les cinq exigences de CONV-11 *(six éléments dans `MaintienCONV11`, PR-23 §6)*, **une seule est acquise** — la contrepartie (`registre_augmente_coherent`, PR-20) ; le porteur a un patron (PR-18, PR-22) ; **solde, horizon et critère de vérification n'ont rien** dans L2. CONV-11 appelle donc un objet de preuve propre — **PR-23** — écrit sur le patron de PR-10 §7 : ne pas énoncer « toute écriture bien formée déclare X » (qui reprendrait l'hypothèse en conclusion, forme 3 de §8ter), mais **exhiber le trou**.

#### 8.5.4 La sonde P-C-E-D-e-d — ce qu'elle établit, ce qui en est fait

*Instruction : `Sonde_PCEDed_2026-09-08.md`. Fichier : `ProfReg/Sonde_PCEDed.lean`, 0 `sorryAx`, aucun `Classical.choice`.*

**Statut.** La sonde formalise §8.5 dans sa rédaction d'origine, sans l'améliorer. Elle est importée par `ProfReg.lean` et auditée par `Audit.lean` : le contrôle qui vaut au set est `#print axioms`, jamais un `grep sorry`.

**Ce que la sonde établit — et l'état de chacun de ses résultats.**

| Résultat | Théorème | État |
| --- | --- | --- |
| Le typage à six primitives et les composites se formalisent sans difficulté | `la_sonde_ne_condamne_pas_le_typage` | **Acquis.** La grammaire n'est pas mise en cause |
| `E+` est le **seul** typage tabulé qui admette l'absence de contrepartie — et un engagement sans miroir n'est pas une dette sans créancier | `seul_E_plus_admet_le_vide`, `engagement_sans_miroir_n_est_pas_dette_sans_creancier` | **Acquis, et il resserre R-INTERDIT-ABSOLU** : l'asymétrie existentielle passe de remarque du texte à propriété de la table.  **Vérifié sur la table actuelle, `E−` compris** : `seul_E_plus_admet_le_vide_table_1809` |
| Le mot « miroir » désigne **deux relations** dans le même tableau | `la_table_melange_deux_relations`, `second_couple_asymetrique` | **Traité en deux temps.** Moitié inter-acteurs : **PR-20**, raccordée à `registre_augmente_coherent` (voie (b) de la note). Déclaration du partage : **colonne « nature de la relation » ajoutée en §8.5.2** (voie (a)).  Sur la table actuelle, les deux couples asymétriques subsistent (`les_resultats_de_la_sonde_tiennent_table_1809`) — ils sont **déclarés** par cette colonne |
| Le champ `respect_R1` est un booléen déclaré doublant un contrôle calculable | `respect_R1_declare_peut_mentir`, `respect_R1_declare_peut_se_sous_estimer` | **Traité et généralisé.** Pas de champ : contrôle calculé ; **PR-21** démontre le fait pour tout contrôle calculable ; **§8quinquies** en fait la cinquième forme de sur-revendication |
| La table des miroirs n'est pas définie sur les composites | `miroir_non_defini_sur_les_composites` | **Dissous pour les cas attestés**, tous sortis de la couche T (§8.5.3) |

**Une base qui borne la citation.** La sonde type `solAgricoleK1 = P⁺ + C⁺` et `chargesPersonnelK1 = e° + D⁻` — **deux lectures que la couche T ne retient pas** (§8.5.3). Ses énoncés restent exacts (ces lectures sont typables : c'est ce que la sonde montre) mais **ils ne certifient pas un typage en vigueur**, et l'en-tête du fichier le déclare. `[BASE DÉCLARÉE]`

**Ce qui reste ouvert, et c'est dans le texte, pas dans le code.**

1. **Les champs `typage_primitive` et `typage_miroir` de §8.5 autorisent toujours « composites X+Y », et renvoient à l'arbitrage 11.3 option A comme à une règle en vigueur — alors que la totalité des composites attestés est sortie de la couche T par les décisions du porteur (§8.5.3).** Le tableau de §8.5.3 est entièrement raturé et son chapeau porte encore « constituent même la norme ». `[INCOHÉRENCE INTER-COUCHES]` — la couche T n'a plus de composite attesté et son schéma de champs en admet encore. **Deux issues** : *(a)* fermer la couche T aux composites et requalifier 11.3 comme état daté ; *(b)* la laisser ouverte et déclarer quel cas non encore rencontré la justifierait.

2. **La lecture du « + » de la ligne `D−` est une lecture, non un résultat.** La sonde l'a lu comme un composite là où le « ou » de `P+` est une alternative, parce que les gloses vont dans ce sens ; la colonne de §8.5.2 hérite de cette lecture. **Si les deux « + » étaient des « ou », un des couples asymétriques tomberait** — mais pas le résultat, qui repose sur `P+ ↦ e` et `P− ↦ C+`, tous deux explicitement « ou ». `[LECTURE DÉCLARÉE]`

3. **La colonne « nature de la relation » déclare le partage ; elle ne le démontre pas.** Un contradicteur peut soutenir que la table décrit une relation *orientée* entre acteurs — du fournisseur vers le client — auquel cas l'asymétrie est normale et le partage inutile. La réponse du set est que la grammaire annote elle-même « symétrie stricte » la ligne `C+` ; **c'est une lecture du texte, et elle est réfutable.** `[ENGAGEMENT AVEC SYMÉTRIE — condition de réfutation : exhiber une lecture orientée qui rende compte des neuf lignes sans partage.]`

4. **La moitié intra-écriture n'est pas formalisée** — voie (c) de la note, non retenue : R1 est déjà prouvé au niveau où il vaut, et le point 1 doit être tranché avant qu'un raffinement par le typage ait un objet.

#### 8.5.5 Table de correspondance `C-MOUVEMENT-TYPE.M` × relation → `C-MOUVEMENT-TYPE.T`

##### Pourquoi une table de correspondance, et non une fusion

Les deux sous-couches ne portent pas sur le même objet. **M type le mouvement** — une géométrie sur `A = D + S' + ΔS`, un prédicat à une place, démontré complet : quatre mouvements intra-composante et six paires à deux sens font seize, et pas davantage. **T type les deux côtés** — une ontologie des positions, un prédicat à deux places, qui ne se démontre pas mais se déclare et s'éprouve. Les fusionner attacherait un étage non démontrable à un étage démontré.

Surtout, **la correspondance n'est pas biunivoque, et le registre RATP en fournit la preuve** : le mouvement `e` (A↑ / D↑) se type `P+ ↔ D+` pour un achat à crédit et `C+ ↔ D+` pour une acquisition d'actif de concession sous IFRIC 12 — même géométrie, deux ontologies, parce que le régime de propriété diffère. Ce qui sélectionne parmi les typages possibles est **la relation déclarée entre les acteurs**. La structure juste est donc une correspondance à deux arguments, non une table à une entrée.

> `[CE QUE LA TABLE REND POSSIBLE]` Sans elle, l'analyste qui type une écriture doit inventer sa convention de lecture — c'est le cas du jalon J1, dont les 56 résultats dépendent de cette convention. Avec elle, le chemin est déterministe : on lit la géométrie du mouvement, on **déclare la relation**, on obtient le typage. La colonne « relation déclarée » doit rester visible : sans elle, la table se lirait comme un dictionnaire et laisserait croire que T se dérive de M, ce qui est faux.

##### La table

Statuts **calculés** par appartenance à la table §8.5.2 telle qu'elle figure dans le présent document, non déclarés.

| Sigle | Variations | Relation déclarée | Arité | Couple | Statut | Instance attestée |
| :-: | :-- | :-- | :-- | :-- | :-- | :-- |
| `a` | A↑ / A↓ | Arbitrage entre deux postes de patrimoine du même acteur | intra-écriture | `P+ ↔ P−` | **ADMIS** | RATP : variation des dépôts et placements à court terme (2 faits) |
| `a` | A↑ / A↓ | Acquisition d'une chose au comptant | intra-écriture | `P+ ↔ P−` | **ADMIS** | RATP : acquisitions d'immobilisations ; achats d'instruments financiers (4 faits) |
| `a` | A↑ / A↓ | Transfert d'une chose entre deux acteurs — vente, don, reprise | inter-acteurs | `P+ + D+ ↔ P− + D−` | **ADMIS** | — |
| `b` | D↑ / D↓ | Reclassement d'une dette envers le même créancier | intra-écriture | `D− ↔ D+` | **ADMIS** | — |
| `b` | D↑ / D↓ | Novation — changement de créancier | inter-acteurs à trois livres | `D− ↔ D+` | **ADMIS** | — |
| `c` | S'↑ / S'↓ | Incorporation de réserves au capital | intra-écriture | `E+ ↔ E−` | **ADMIS** | RATP : transferts et autres variations de capitaux propres (20 faits) |
| `d` | ΔS↑ / ΔS↓ | Compensation interne au résultat | intra-écriture | `d ↔ e` | **ADMIS** | — |
| `e` | A↑ / D↑ | Acquisition à crédit d'une chose | inter-acteurs | `P+ ↔ D+` | **ADMIS** | RATP : achats consommés ; émissions obligataires ; souscriptions d'emprunts (7 faits) |
| `e` | A↑ / D↑ | Acquisition d'un droit sur le concédant — IFRIC 12 | inter-acteurs | `C+ ↔ D+` | **ADMIS** | RATP : acquisitions d'actifs de concession (2 faits) |
| `f` | A↓ / D↓ | Remboursement par effort effectif | mixte | `D− ↔ C−+e` | **ADMIS** | RATP : remboursements obligataires et de billets de trésorerie (3 faits) |
| `f` | A↓ / D↓ | Remboursement transitant par un agent payeur | inter-acteurs à trois livres | `D− ↔ C−+e` | **ADMIS** | — |
| `g` | A↑ / S'↑ | Apport en capital | inter-acteurs | `E+ ↔ C+` | **ADMIS** | RATP : transactions avec les propriétaires, augmentations (19 faits) |
| `h` | A↓ / S'↓ | Remboursement du capital aux apporteurs | inter-acteurs | `E− ↔ C−` | **ADMIS** | RATP : transactions avec les propriétaires, diminutions (3 faits) |
| `i` | D↓ / S'↑ | Conversion d'une dette en capital | mixte | `D− ↔ E+` | **ADMIS** | — |
| `j` | D↑ / S'↓ | Distribution de réserves constatée en dette | inter-acteurs | `E− ↔ D+` | **ADMIS** | — |
| `k` | A↑ / ΔS↑ | Vente d'un bien au comptant | intra-écriture | `P− ↔ d` | **ADMIS** | RATP : cessions d'immobilisations et de placements encaissées (4 faits) |
| `k` | A↑ / ΔS↑ | Vente d'un SERVICE au comptant — volet service | inter-acteurs | `e ↔ d` | **ADMIS** | — |
| `k` | A↑ / ΔS↑ | Vente d'un SERVICE au comptant — volet règlement | inter-acteurs | `P+ + D+ ↔ P− + D−` | **ADMIS** | — |
| `l` | A↓ / ΔS↓ | Amortissement, dépréciation, perte fortuite | intra-écriture | `P− ↔ e` | **ADMIS** | RATP : dotations aux amortissements (2 faits) |
| `l` | A↓ / ΔS↓ | Charge payée comptant à un tiers | inter-acteurs | `d ↔ e` | **ADMIS** | — |
| `m` | D↓ / ΔS↑ | Remise de dette — relation entre les deux livres | inter-acteurs | `C− ↔ D−` | **ADMIS** | — |
| `m` | D↓ / ΔS↑ | Remise de dette — forme fusionnée dans le livre du débiteur | intra-écriture | `D− ↔ d` | **ABSENT** | — |
| `n` | D↑ / ΔS↓ | Provision — créancier non identifié | intra-écriture | `e ↔ E+` | **ADMIS** | RATP : dotations nettes aux provisions (2 faits) |
| `n` | D↑ / ΔS↓ | Charge à payer, contravention — créancier identifié | inter-acteurs | `e ↔ E+` | **ADMIS** | — |
| `o` | S'↓ / ΔS↑ | Rectification d'erreur d'un exercice antérieur | intra-écriture | `E− ↔ d` | **ADMIS** | — |
| `p` | S'↑ / ΔS↓ | Cas inverse de o | intra-écriture | `E+ ↔ e` | **ADMIS** | — |

##### Notes de cellule

- **`a` — Arbitrage entre deux postes de patrimoine du même acteur** (`P+ ↔ P−`, ADMIS) — Aucune obligation n'est transférée : c'est le seul cas où un pur P ↔ P est complet.
- **`a` — Acquisition d'une chose au comptant** (`P+ ↔ P−`, ADMIS) — Exemple canonique du mouvement a en §8.3. La contrepartie du cédant fait l'objet de la cellule suivante.
- **`a` — Transfert d'une chose entre deux acteurs — vente, don, reprise** (`P+ + D+ ↔ P− + D−`, ADMIS) — COMPOSITE (décision 5) ; le `P ↔ P` inter-acteurs n'est pas admis. Un transfert de chose transfère la position d'obligé : entretien, conformité, fin de vie, dette NH incorporée. Le cédant en est libéré. Un pur P ↔ P inter-acteurs serait une écriture amputée. Cas RATP directement concerné : biens de retour et biens de reprise.
- **`b` — Reclassement d'une dette envers le même créancier** (`D− ↔ D+`, ADMIS) — Décision 7. Aucun composite n'est requis : l'obligation est l'objet même du mouvement, rien ne l'accompagne.
- **`b` — Novation — changement de créancier** (`D− ↔ D+`, ADMIS) — Décision 7. Cas d'espèce de la troisième arité (B7) : l'écriture nomme l'ancien et le nouveau créancier, dont les livres portent C− et C+.
- **`c` — Incorporation de réserves au capital** (`E+ ↔ E−`, ADMIS) — Typable par le rabattement de S' sur E (§8.5.1ter).
- **`d` — Compensation interne au résultat** (`d ↔ e`, ADMIS) — Un produit compense une charge dans le même livre. Lecture à confirmer.
- **`e` — Acquisition à crédit d'une chose** (`P+ ↔ D+`, ADMIS) — Lecture canonique de la ligne P+.
- **`e` — Acquisition d'un droit sur le concédant — IFRIC 12** (`C+ ↔ D+`, ADMIS) — MÊME MOUVEMENT, AUTRE TYPAGE. Sous IFRIC 12 l'actif n'est pas un patrimoine mais une créance. C'est la démonstration que la correspondance M → T n'est pas biunivoque : le régime de propriété commande le typage.
- **`f` — Remboursement par effort effectif** (`D− ↔ C−+e`, ADMIS) — Seule ligne composite de la table d'origine.
- **`f` — Remboursement transitant par un agent payeur** (`D− ↔ C−+e`, ADMIS) — La contrepartie C− est dans le livre d'un tiers. Relève de LACUNE 1.
- **`g` — Apport en capital** (`E+ ↔ C+`, ADMIS) — Typable par le rabattement de S' sur E.
- **`h` — Remboursement du capital aux apporteurs** (`E− ↔ C−`, ADMIS) — Typable par la ligne E− (décision 2).
- **`i` — Conversion d'une dette en capital** (`D− ↔ E+`, ADMIS) — Décision 7. Changement de régime d'obligation : ce qui était exigible envers un créancier devient structurel envers un apporteur, et c'est le même acteur qui change de position. Seconde ligne mixte de la table. C'est, dans la grammaire du MRC, l'opération par laquelle une dette écologique pourrait devenir un engagement statutaire.
- **`j` — Distribution de réserves constatée en dette** (`E− ↔ D+`, ADMIS) — Admis par la ligne E− (décision 2).
- **`k` — Vente d'un bien au comptant** (`P− ↔ d`, ADMIS) — La chose sort, le produit est servi.
- **`k` — Vente d'un SERVICE au comptant — volet service** (`e ↔ d`, ADMIS) — DÉCOMPOSITION PROPOSÉE, volet 1 sur 2. Aucune sortie de patrimoine : A fournit un effort, B reçoit un résultat.
- **`k` — Vente d'un SERVICE au comptant — volet règlement** (`P+ + D+ ↔ P− + D−`, ADMIS) — DÉCOMPOSITION, volet 2 sur 2. Le règlement est un transfert de chose entre acteurs — donc composite (décision 5). La forme fusionnée P+ ↔ d reste ABSENTE, et c'est un résultat : la grammaire refuse de fondre le service et son paiement dans une seule écriture.
- **`l` — Amortissement, dépréciation, perte fortuite** (`P− ↔ e`, ADMIS) — Exige destinataire_effort = SANS_BENEFICIAIRE (décision 3).
- **`l` — Charge payée comptant à un tiers** (`d ↔ e`, ADMIS) — DÉCOMPOSITION : A reçoit l'effort du fournisseur ; le règlement relève de la cellule a inter-acteurs.
- **`m` — Remise de dette — relation entre les deux livres** (`C− ↔ D−`, ADMIS) — Le créancier perd sa créance, le débiteur perd sa dette. Le produit exceptionnel est la CONSÉQUENCE dans le livre du débiteur, non un côté de l'écriture.
- **`m` — Remise de dette — forme fusionnée dans le livre du débiteur** (`D− ↔ d`, ABSENT) — La ligne D− exige C− + e, c'est-à-dire un effort effectif. La grammaire refuse l'extinction gratuite d'une dette vue depuis un seul livre — ce qui est cohérent avec signal_remise_NH (§8.9).
- **`n` — Provision — créancier non identifié** (`e ↔ E+`, ADMIS) — Décision 4.
- **`n` — Charge à payer, contravention — créancier identifié** (`e ↔ E+`, ADMIS) — Décision 6 : la distinction provision / charge à payer relève de la couche R, non du typage. Le typage est donc le même que celui de la provision ; c'est `denomination_regime` et `compte_imputation` qui distinguent. Le couple `e ↔ D+` n'est PAS versé.
- **`o` — Rectification d'erreur d'un exercice antérieur** (`E− ↔ d`, ADMIS) — Décision 7. Branche d de la ligne E−, symétrique de la branche e de la ligne E+ : le couple o/p est symétrique.
- **`p` — Cas inverse de o** (`E+ ↔ e`, ADMIS) — Admis par la branche e de la ligne E+ (décision 4).

##### Couverture des seize mouvements — résultat calculé

**Les seize mouvements sont couverts** : pour chacun, au moins une relation déclarée conduit à un couple appartenant à la table §8.5.2.

Deux mouvements, `k` et `m`, sont couverts **par décomposition**, sans ligne propre (voir ci-dessous) ; trois, `b`, `i` et `o`, le sont par les lignes de la décision 7 (`D+ ↔ D−`, `E+ ↔ D−`, `E− ↔ d`).

**Sur 26 cellules : 25 admises, 1 absente** — et cette dernière est un refus motivé, non un trou : voir la remise de dette ci-dessous.

> **Ce que la couverture complète ne signifie pas.** Elle ne rend pas la sous-couche T redondante avec M, et le décompte ne doit pas se lire ainsi. **T n'ajoute rien à la géométrie ; elle ajoute la relation.** Un même mouvement se type différemment selon la relation déclarée : `e` donne `P+ ↔ D+` pour un achat à crédit et `C+ ↔ D+` sous IFRIC 12 ; `b` donne un reclassement ou une novation selon l'arité ; `a` donne un arbitrage ou un transfert composite. **La correspondance est une fonction à deux arguments, et un seul des deux vient de M.** C'est cela, et non la couverture, qui justifie que les deux sous-couches restent distinctes.

##### La métrique symétrique — ce que T type et qu'aucun mouvement de M n'atteint

**Pourquoi.** Le décompte 16/16 mesure la couverture de T **par le domaine de M**. Employé seul, il fait de la complétude de M la norme de T, alors que §8.5.0 déclare à T un domaine strictement plus large. La métrique symétrique mesure l'autre moitié : **combien de couples de la table §8.5.2 aucun mouvement de M n'atteint.**

**Résultat calculé.** Sur les **23 couples distincts** de la table §8.5.2, **17 sont atteints** par au moins une cellule de la table de correspondance ci-dessus et **6 ne le sont par aucune**.

| Couple non atteint | Pourquoi | Nature |
| :-- | :-- | :-- |
| `E+ ↔ ∅` | Un mouvement de M exige **deux** variations simultanées ; l'engagement existentiel n'a qu'un côté | **Structurellement hors d'atteinte de M** — c'est l'asymétrie autorisée de §8.5.2 |
| `E+ ↔ D+` | Engagement chez A, dette chez B : **deux livres**, aucune géométrie de bilan unique | **Structurellement hors d'atteinte de M** |
| `e ↔ D−` | Effort de A, extinction de dette **chez B** : deux livres | **Structurellement hors d'atteinte de M** |
| `d ↔ C−` | Produit chez A, extinction de créance chez B. En un seul livre, la géométrie serait `A↓ / ΔS↑`, **qui ne figure pas parmi les seize** : l'équation l'interdit | **Structurellement hors d'atteinte de M** |
| `P− ↔ C+` | Vente à crédit d'une chose — géométrie `a` (A↑/A↓). Aucune cellule de `a` ne la porte : l'arité inter-acteurs de `a` est occupée par la seule forme composite | **Lacune de la table de correspondance** |
| `P+ ↔ e` | Production d'une immobilisation par les moyens propres — géométrie `k` (A↑/ΔS↑). Aucune cellule de `k` ne la porte | **Lacune de la table de correspondance** |

**Ce que ce résultat établit, et qui n'était pas anticipé.** Quatre des six couples non atteints le sont pour une seule et même raison : **leurs deux côtés sont dans deux livres différents, ou il n'y a pas de second côté.** Un mouvement de M est une variation de l'équation **d'un bilan** ; il ne peut pas, par construction, décrire une relation dont les deux termes n'appartiennent pas au même bilan.

> **L'angle mort de M est exactement le domaine de la thèse 2.** Ce que T type et que M n'atteint pas, c'est la relation entre deux livres — c'est-à-dire la forme même de l'écriture duale entre une organisation à comptabilité tenue et une entité qui n'en a pas (§8.5.0). **Le 16/16 et le 17/23 ne mesurent pas deux degrés de la même chose : ils mesurent les deux vocations distinctes de la sous-couche T.**

**Les deux lacunes, elles, sont à combler.** `P− ↔ C+` et `P+ ↔ e` ont une géométrie disponible et aucune cellule. La première est vraisemblablement une **conséquence non propagée de la décision 5** : si le transfert d'une chose entre acteurs est composite parce qu'il transfère les obligations attachées, la vente à crédit l'est aussi, et le couple `P− ↔ C+` de la ligne `P−` devrait être restreint ou composé comme l'a été `P+ ↔ P−`. `[RESTE À FAIRE — porteur : porteur MRC / architecte ; critère : statuer sur la propagation de la décision 5 à la branche `C+` de la ligne `P−`, et verser une cellule `k` pour la production immobilisée.]`

##### Les relations de communalité et leur sigle — seconde moitié de la métrique symétrique

Les vingt-six relations déclarées de la table de correspondance sont **toutes des relations de comptabilité d'entreprise** — achat à crédit, IFRIC 12, novation, apport en capital, distribution de réserves, rectification d'exercice antérieur. Aucune n'est une relation de communalité. Le tableau suivant ouvre la colonne manquante.

| Relation de communalité | Typage proposé | Sigle M | Cas du set |
| :-- | :-- | :-- | :-- |
| Engagement d'un collectif envers un acteur non tracé — nappe fossile, générations futures | `E+ ↔ ∅` | **aucun, et aucun possible** | K3 (Niayes) ; R-INTERDIT-ABSOLU |
| Don du surplus à un bénéficiaire, la contrepartie étant chez le fournisseur de ce dernier | `e` / `D−` / `C−` — trois livres (B7) | **aucun** : la géométrie se répartit sur trois bilans dont deux n'existent pas | AMEP (§8.5.2bis) |
| Effort de préservation fourni au bénéfice d'un milieu, sans contrepartie monétaire | `e ↔ E+`, `destinataire_effort = NH_NATUREL` | `n` — **formellement disponible, matériellement inapplicable** : `n` suppose un `ΔS` que l'entité n'a pas | K1, K3 |
| Contribution de travail bénévole à un commun | `e ↔ d` ou `e ↔ E+` | `k` / `n` — **même remarque** | NT-G11 |
| Dégradation constatée d'un commun, inscrite comme dette | `e ↔ E+` puis `E+ ↔ D+` vers le livre d'un responsable | partiellement `n` ; le second couple **hors d'atteinte** | K3 |

> **La catégorie qui importe est la troisième colonne, ligne 3.** Pour une entité sans bilan, **même les couples que M atteint ne sont atteints que dans le livre de quelqu'un d'autre.** Le sigle existe, et il ne s'applique pas à elle. C'est la formulation la plus exacte de ce que §8.3bis déclare et de ce que §8.5.0 répare.

`[STATUT — les cinq relations ci-dessus sont des **propositions**, construites à partir des cas attestés du set (K1, K3, AMEP, NT-G11) et non d'un corpus d'écritures de communalité, qui n'existe pas encore. `R-INCAPACITE-LLM-VALIDER` s'applique : elles sont à valider cellule par cellule par le porteur. **Tant qu'aucun registre de communalité réel n'a été typé, cette moitié de la métrique reste une prévision, là où la première moitié est un calcul.**]`

`[RÉSERVE SUR LE CALCUL LUI-MÊME — le décompte 17/23 est obtenu par un encodage déclaré des deux tables non par extraction automatique du document : une autre lecture des lignes `P+ + D+` et `C−+e` donnerait un autre dénominateur. Par ailleurs, trois cellules atteintes portent une arité *inter-acteurs* alors que leur géométrie tient dans un seul livre — notamment `e` / IFRIC 12, `C+ ↔ D+`. C'est la reprise des arités (B7), non résolue ici : **tant que les arités n'ont pas été reprises ligne à ligne, la frontière entre « un livre » et « deux livres » n'est pas fiable, et le résultat de 4 couples « structurellement hors d'atteinte » peut varier.**]`

##### Deux décompositions, et ce qu'elles établissent

Le jalon J1 compte `k` — la vente au comptant d'un service — parmi les mouvements intypables. **La correspondance montre que c'est une erreur de lecture, et la nature de l'erreur importe.**

Une vente de service au comptant n'est pas une écriture, c'en est deux : `e ↔ d` pour le service — A fournit un effort, B reçoit un résultat — et un transfert de chose entre acteurs pour le règlement. Les deux branches sont typables. **Ce qui reste absent est la forme fusionnée `P+ ↔ d`, et son absence est un résultat, non un trou** : la grammaire refuse de fondre le service et son paiement dans une seule écriture. C'est cohérent avec ce qu'elle fait partout ailleurs — elle type des relations, et un service rendu et un paiement reçu sont deux relations.

Même figure pour `l`, la charge payée comptant à un tiers : `d ↔ e` pour l'effort reçu, et le règlement comme transfert. Et pour `m`, la remise de dette : typable en `C− ↔ D−` **entre les deux livres**, absente sous sa forme fusionnée `D− ↔ d` dans le seul livre du débiteur. Là encore le refus est signifiant : la grammaire ne type pas l'extinction gratuite d'une dette comme un gain, ce qui est cohérent avec `signal_remise_NH` (§8.9).

##### Le refus qui subsiste — et c'est un résultat

Une seule cellule sur vingt-six reste absente : **la remise de dette sous sa forme fusionnée**, `D− ↔ d`, vue depuis le seul livre du débiteur.

Elle n'est pas un trou. La remise de dette **est typable** — en `C− ↔ D−`, entre les deux livres : le créancier perd sa créance, le débiteur perd sa dette. Ce que la table refuse, c'est de la typer comme un **gain** apparaissant dans un seul livre. La ligne `D−` exige `C− + e`, c'est-à-dire un **effort effectif** ; une dette ne s'éteint pas gratuitement de l'intérieur.

**Ce refus est cohérent avec ce que F8 fait par ailleurs.** `signal_remise_NH` (§8.9) se déclenche précisément sur le mouvement `m` appliqué à une dette NH sans consentement du consortium de gouvernance. La table et le signal disent la même chose : **l'effacement d'une obligation regarde son créancier, et ne se constate pas unilatéralement comme un produit.**

`[RÉSULTAT DÉCLARÉ, non obligation ouverte. Si le porteur souhaitait néanmoins verser `D− ↔ d`, il faudrait établir qu'une dette peut s'éteindre sans contrepartie chez le créancier — ce que ni le droit des obligations ni la grammaire du MRC ne paraissent admettre.]`

##### Statut de cette table

`[AUCUNE PREUVE FORMELLE.]` Régime procédural. Les statuts sont calculés par appartenance à une table, ce qui se lit et ne se démontre pas. **Les vingt-six cellules sont des propositions de correspondance** : la relation déclarée de chacune est une lecture, et une autre lecture donnerait d'autres cellules. Onze d'entre elles sont gagées sur des écritures attestées du registre RATP 2025, couvertes par une opinion de commissaires aux comptes ; les quinze autres ne le sont pas. **État : 25 cellules ADMISES, 1 ABSENTE** — la remise de dette sous sa forme fusionnée.

**Métrique symétrique : 17 des 23 couples de §8.5.2 sont atteints par au moins un mouvement de M ; 6 ne le sont par aucun.** `R-INCAPACITE-LLM-VALIDER` s'applique : la table a été construite par un assistant et sa validation, cellule par cellule, revient au porteur.

**Condition de réfutation de la table elle-même.** Elle tombe si l'on exhibe une écriture dont la relation est correctement déclarée et dont le typage n'est pas celui que la cellule correspondante prévoit — auquel cas c'est la cellule qui est fausse, non l'écriture. Elle tombe aussi, plus radicalement, si l'on établit qu'une même relation déclarée peut conduire à deux typages différents : la correspondance ne serait alors pas une fonction, et il faudrait un troisième argument.

---

#### 8.5.6 Condition d'inscription d'une chose comme commun — décision du porteur

`[Arbitrage A3. Instruction complète : `A3_Instruction_Typage_Commun_2026-09-21.md`. Source lue pour l'instruction : Rochfeld, J., Cornu, M. & Martin, G.-J. (dir.), *L'Échelle de communalité*, Rapport final n° 17-34, Mission de recherche Droit et Justice, avril 2021.]`

##### 8.5.6.1 Levée d'homonymie — deux « `P + C` » qui ne sont pas le même objet

Avant toute règle de fond, une homonymie doit être levée, faute de quoi la qualification inter-régimes de §8.4bis avalerait la présente décision.

| | `P + C` de **§8.4bis** | La conjonction de la présente décision |
| :-- | :-- | :-- |
| Logique | **disjonction** — la chose est `P` *ou* `C` selon le régime déclaré | **conjonction** — la chose est tenue *et* des usages sont dus |
| Acteurs | un seul livre, deux qualifications | **deux livres** |
| Couche | **R** — c'est une qualification de régime | **T** — c'est une relation typée |
| Écriture | `P + C` | **`P+ + D+ ↔ C+`** |

**La notation `P + C` reste réservée à la disjonction inter-régimes de §8.4bis.** La conjonction s'écrit sous sa forme réelle, qui nomme ses deux livres et ne prête à aucune confusion.

**Pourquoi `D+` et non `C` du côté du collectif.** Sous R1, `C` et `D` sont miroirs (§8.5.2 : *« toute créance d'un côté = dette de l'autre »*). Une créance **des membres** est, dans le livre du collectif qui tient la chose, une **dette**. Écrire `P + C` dans un seul livre dirait que la communauté détient la chose **et détient une créance** — contre elle-même. `[AUCUNE LIGNE NOUVELLE N'EST REQUISE EN §8.5.2 — `P+ + D+ ↔ C+` est la ligne composite de la décision 5 dans sa forme de détention et non de transfert.]`

##### 8.5.6.2 La règle

> ### **Une chose typée `P+` sans miroir `D+ ↔ C+` et sans `E+` qualifiant n'est pas inscrite comme un commun.**
>
> **Est qualifiant** un `E+` qui satisfait l'une des deux conditions :
> - **(a)** `E+ ↔ ∅` avec `asymetrie_existentielle = VRAI` — l'engagement envers un acteur non tracé ; c'est l'intérêt diffus au sens de Rochfeld, Cornu & Martin, *« voire en l'absence de prérogatives distribuées »* (p. 79) ;
> - **(b)** `creance_repartissable = FAUX` — aucun bénéficiaire ne détient de droit individuel sur une quote-part de la valeur engagée.
>
> **N'est pas qualifiant** un `E+` avec `creance_repartissable = VRAI`. **Avec `NON_DETERMINABLE`, le calcul rend `INDETERMINE`** : il ne qualifie ni n'exclut. **Avec `NONDECLARE`, l'`E+` ne qualifie pas** (patron CONV-9 : la valeur non déclarée refuse, elle n'autorise pas), et l'écriture porte le marqueur `[ENGAGEMENT SANS QUALIFICATION DE RÉPARTISSABILITÉ]` — un marqueur, jamais une sanction (patron R0-bis).
>
> **Le fondement.** Le rapport source place la communalité dans **la qualité de l'intérêt** — indivisible, transindividuel — et dans **l'inclusivité**, jamais dans la nature comptable de l'obligation. Il écarte nommément l'« intérêt d'un groupe », dont les intérêts sont *« divisibles et répartissables »*, *« ni transindividuel ni indivisible »* (p. 332), et conclut que *« les intérêts pluri-personnels individualisés et divisibles n'intègrent pas la catégorie de l'intérêt commun »* (p. 336). **Un `E+` n'est donc pas un indice de communalité par lui-même** — ce que §8.5.1ter déclare (*« c'est cette propriété qui est typée, pas leur identité »*).
>
> **Aucun typage n'est interdit.** La communalité n'est pas déclarée : elle est **lue sur l'écriture**. Une forêt communale typée `P+` seul par la commune est une propriété publique — ce qu'elle est en droit. Pour l'inscrire comme commun, la commune inscrit **le `D+` envers ses habitants et le `C+` de ceux-ci**, et c'est alors vrai de l'écriture et pas seulement de l'intention.

> ### `[DÉCISION DU PORTEUR — branche B retenue, branche A écartée, branche C maintenue ouverte.]`
>
> **Le constat de J1-ter.** Sans critère de divisibilité, le calcul rend `INDETERMINE` pour 41 écritures du registre RATP 2025 et **aucun `VRAI`** : la règle ne classe pas les capitaux propres parmi les communs, elle **échoue à les exclure** — la condition de §8.5.6.4 (instances déclarées) n'étant remplie par aucune. Le défaut est réel, non urgent.
>
> **Branche A écartée** — exclusion par catégorie comptable (« miroir `C+` chez un apporteur, ou contrepartie composante de capitaux propres »). Trois motifs : elle laisse passer les provisions ; elle **exclurait les réserves impartageables d'une SCIC**, objet du droit des sociétés le plus proche d'un intérêt commun ; elle applique en couche T une catégorie de la couche R, contre la décision 6.
>
> **Branche B retenue** — le critère de divisibilité porté par l'écriture : champ `creance_repartissable` (§8.5) et « `E+` qualifiant » (ci-dessus).
>
> **Rejeu sur le registre RATP 2025** (`PPC/RATP/J1ter_rejeu_branche_B_8.5.6_2026-09-26.json`). Sur les 41 écritures, **35 ne qualifient plus** (capital, dotation, réserves, intérêts minoritaires : `creance_repartissable = VRAI`) et **6 restent `INDETERMINE`** : les 4 écritures de la **réserve pour biens remis en dotation** (`ratp:ReserveForAssetsAllocatedToRATPMember`), toutes de mouvement nul, et les 2 **dotations aux provisions**, dont une seule non nulle (FB-0021, −18 M€). **Aucune ne qualifie.** `[LES VALEURS DU REJEU SONT DES HYPOTHÈSES DÉCLARÉES (H1-H3), non des déclarations validées — en particulier pour la dotation en capital d'un EPIC.]`
>
> **Ce que le rejeu montre, et c'est l'intérêt de la branche.** Elle ne produit pas zéro : elle **isole les cas où la question se pose réellement** — une réserve qui est la contrepartie de biens *affectés*, dont la RATP n'a pas la libre disposition (jalon J2), et une provision dont la nature n'est pas ventilée. **Ce sont exactement les deux figures que le rapport source rapproche de la communalité : l'affectation et l'engagement de conservation.** `[INFÉRENCE — aucune n'est ici établie comme commun.]`
>
> **Coût déclaré.** La règle consomme un champ **déclaré**. Elle reste calculée sur l'écriture, mais un de ses arguments dépend d'une déclaration. `[COÛT ASSUMÉ — il est la condition pour que la règle discrimine dans le domaine d'une comptabilité tenue.]`
>
> **Portée bornée.** Le critère est versé **sur `E+` seulement**. Qu'il faille l'appliquer aussi au `C+` de la configuration `D+ ↔ C+` — une indivision à quotes-parts n'est pas un commun — **n'est pas instruit**. `[PORTÉE DÉCLARÉE — ne pas élargir tacitement.]`
>
> **Non-réductibilité (§A.9), première instruction.** `creance_repartissable` ne se réduit pas à `nature_prerogative` (F6) : un `DROIT_SUBJECTIF` peut être répartissable (un dividende) ou non (un droit d'usage d'un commun), et `nature_prerogative` ne sépare pas les deux. `[À CONFIRMER — instruction amorcée, non close.]`
>
> **Condition de réfutation.** La branche tombe si l'on exhibe une communalité reconnue en droit **dont le bénéficiaire détient un droit individuel sur une quote-part de valeur**. Le candidat des droits d'usage divis (affouage, pâturage) est **écarté par construction** — ils répartissent des utilités, non de la valeur —, et c'est la raison pour laquelle le champ porte sur la valeur. **Si cette distinction ne tient pas sur un cas, le champ est mal défini.**
>
> *Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* sur le registre RATP 2025, aucune écriture de capital d'apporteur ne qualifie ; sur un cas SCIC typé, les réserves impartageables qualifient **sous réserve de §8.5.6.4**. `[CAS SCIC NON ENCORE TYPÉ.]`
>
> La table §8.5.2 n'est pas modifiée ; `SondePCEDed.seul_E_plus_admet_le_vide` n'est pas touché, et la sonde porte aussi la table actuelle : `seul_E_plus_admet_le_vide_table_1809`. **PR-30 est le premier ancrage de §8.5.6** — branche B : `la_branche_B_exclut_le_capital_d_apporteur` (garde : la règle sans critère de divisibilité n'exclut pas le capital d'apporteur, la branche B l'exclut), `non_determinable_rend_indetermine`, `le_non_declare_ne_qualifie_pas_et_marque`, `qualifiant_temoin_discriminant` — vérifié sur les sources (`MRC_v5.7_ProfReg_Consolide.md`).

**Ce que la règle écarte, et pourquoi.** La formulation de l'arbitrage A3 — *« un commun ne se type jamais `P` ; seuls `D` et `E` lui conviennent »* — n'est pas retenue, pour trois raisons. Elle est **circulaire** : il faut savoir que la chose est un commun pour appliquer l'interdit, alors que c'est ce que le registre devrait établir. Elle **perd les figures propriétaires porteuses de communalité**, auxquelles le rapport source consacre une section entière — *« Le retournement du paradigme de la propriété exclusive »*. Et elle **ne voit pas que le travail est fait par `D`** : ce n'est pas l'absence de patrimoine qui fait le commun, c'est **l'obligation qui l'accompagne**.

**Forme de la règle.** Calculée et non déclarée, comme le contrôle R1 et comme les statuts de §8.5.5 ; l'un de ses arguments, `creance_repartissable`, est toutefois déclaré (§8.5.6.2bis). **Elle ne ferme rien : elle rend l'inscription comme commun coûteuse en déclarations plutôt qu'interdite.**

##### 8.5.6.2bis Les formes d'affectation admises — fiducie, ORE, ORIC *(décision du porteur)*

`[Source : Rochfeld, Cornu & Martin (dir.), *L'Échelle de communalité*, 2021, P2, T1, §4 (p. 275-315) et Annexe 1, propositions 10 à 12.]`

**Ce que la décision tranche.** Le MRC **admet trois formes d'affectation volontaire à un intérêt commun** comme supports d'inscription d'un commun, à côté de l'écriture `E+ ↔ ∅` (§8.5.2), qui reste suffisante lorsqu'aucun créancier n'est institué. Le rapport source les désigne comme telles : *« Deux techniques visent spécifiquement cette fin : l'obligation réelle environnementale […] et les licences libres […]. Outre ces deux instruments spéciaux, la fiducie pourrait permettre une telle affectation volontaire »* (p. 277) ; il propose de généraliser la première en **obligation réelle d'intérêt commun** (p. 283 ; Annexe 1, proposition 10.4). **Les trois s'écrivent `P+ + D+ ↔ C+`**, et non `E+ ↔ ∅` — c'est pourquoi elles appellent des conditions d'écriture propres.

**Règle A — la condition s'apprécie classe de créance par classe de créance.** Chaque `C+` porté sur la chose est une **écriture distincte**, qualifiée par `classe_creance` et par `creance_repartissable` (§8.5, table des champs). **Une écriture `D+ ↔ C+` relevant d'une forme admise qualifie pour la condition T de §8.5.6.2 si et seulement si son `C+` porte `creance_repartissable = FAUX`.** La chose satisfait la condition T si **au moins une** de ses classes qualifie. Les autres classes — en particulier une `VALEUR_ECONOMIQUE` répartissable — **restent inscrites, et ne sont pas agrégées** (CONV-14). *Fondement :* la communalité est une **part**, non un état — *« toute propriété serait donc plus ou moins exclusive, plus ou moins inclusive, et c'est cette part variable qui composerait celle de la communalité »* (Rochfeld, Cornu & Martin 2021, p. 78).

**Règle B — complétude : toute classe de créance est déclarée, y compris la valeur vendue.** *(Obligatoire pour la fiducie ; appliquée à l'ORE et à l'ORIC sous la forme de la contrepartie, voir ci-dessous.)* Une chose inscrite comme commun au titre d'une fiducie **déclare toutes les classes de créance qui portent sur le patrimoine fiduciaire** : l'usage des bénéficiaires, **la valeur économique réservée aux financeurs**, et **l'attribution du patrimoine au terme** (art. 2011 : les bénéficiaires reçoivent le patrimoine fiduciaire). **Tant qu'une classe n'est pas déclarée, le calcul rend `INDETERMINE`** et l'écriture porte `[INSCRIPTION DE COMMUN INCOMPLÈTE — CLASSE DE CRÉANCE NON DÉCLARÉE]` — marqueur, jamais sanction (patron R0-bis). *Patron :* l'obligation de déclarer le sort des `D` et `E` attachés à une chose transférée (§8.5.6.5). *Ce que la règle empêche :* qu'une chose soit présentée comme commun par sa seule écriture d'usage pendant que sa valeur est revalorisée et cédée hors du registre — la réversion que §8.5.6.5 déclare prévenir. **Le MRC ne juge pas la cession de la valeur : il la rend lisible à côté de l'usage.**

**Conditions propres à chaque forme.**

| | **Fiducie** (C. civ. art. 2011 s.) | **ORE** (C. env. art. L. 132-3) | **ORIC** (proposition de réforme — Annexe 1, prop. 10.4, projet d'art. 2031 C. civ.) |
| :-- | :-- | :-- | :-- |
| **Statut juridique** | droit positif | droit positif | **`DE_LEGE_FERENDA` — proposition non adoptée** `[à ma connaissance ; recherche d'adoption sans résultat — à confirmer]` |
| **Écriture** | `P+ + D+` (fiduciaire, patrimoine séparé) `↔ C+` **par classe** | `P+ + D+` *propter rem* (propriétaire) `↔ C+` du créancier | idem ORE |
| **Classes attendues** | `USAGE` (bénéficiaires) ; `VALEUR_ECONOMIQUE` (financeurs, attribution au terme) ; le cas échéant `AUTRE` | `PRESTATION` (créancier) | `PRESTATION` (créancier) ; `USAGE` si une obligation réelle d'accessibilité est stipulée (rapport, p. 274) |
| **`creance_repartissable`** | **déclaré par classe.** `USAGE` → **FAUX** si le droit est attaché à la personne et incessible, exclu de la succession (rapport, p. 292-293) ; `VALEUR_ECONOMIQUE` → **VRAI** en règle générale ; attribution au terme → VRAI si le patrimoine est réparti entre bénéficiaires, FAUX s'il est attribué à un bénéficiaire tenu de le réapporter (p. 287) | **FAUX attendu** : une prestation écologique n'est pas une quote-part de valeur — **à déclarer, non à présumer** | **FAUX attendu**, à déclarer |
| **Créancier admissible** | bénéficiaires désignés, **ou règles permettant leur désignation** (art. 2018, 4°) | collectivité publique, établissement public, personne morale de droit privé agissant pour la protection de l'environnement | collectivité publique, établissement public, **personne morale de droit privé à but non lucratif** (projet d'art. 2031) |
| **Finalité** | but déterminé du contrat | maintien, conservation, gestion ou restauration d'éléments de la biodiversité ou de fonctions écologiques | **protection d'un intérêt commun environnemental, culturel, social ou scientifique** — liste limitative (p. 283) |
| **ATTRIBUTAIRE** (`porteur_instance`) | **bénéficiaires** (classe `USAGE`) | **le créancier, seulement si un accès ou un usage est stipulé**, et au titre de représentant d'un intérêt collectif (p. 304-305, 338) ; sinon non tenue | idem ORE ; tenue si une obligation d'accessibilité est stipulée |
| **CONTROLE** | tiers désigné (art. 2017) ; bénéficiaires et constituant (art. 2027) | **le créancier** ; tiers lésés (action extracontractuelle, p. 305) | le créancier |
| **DELIBERATIVE** | **non instituée** — à déclarer par ailleurs (§8.5.6.4) | **non instituée** — idem | **non instituée** ; le **comité ad hoc** que prévoit le projet (*« Le contrat définit alors la composition, les pouvoirs et l'organisation de ce comité »*) est un candidat, **contractuel** |
| **Contrepartie** | — | **engagements réciproques obligatoires** (contrat à titre onéreux, p. 310) : **déclarés comme écriture** | le projet les maintient : **déclarés** |

**L'ORIC, et la limite de ce que le registre peut en dire.** Admettre une forme non adoptée n'est pas l'instituer. **Une inscription au titre de l'ORIC porte `statut_juridique_forme = DE_LEGE_FERENDA`** (F6) et se lit comme **un engagement contractuel écrit sur le modèle de l'ORIC** : l'effet *propter rem* que la loi attache à l'ORE — la transmission aux propriétaires successifs — **n'est pas acquis hors de l'ORE** `[PLAUSIBLE, NON VÉRIFIÉ — la validité des obligations réelles conventionnelles hors texte est discutée ; le rapport évoque le droit réel de jouissance spéciale comme voie voisine, p. 277-278]`. **Le registre ne présente jamais une inscription `DE_LEGE_FERENDA` comme opposable.** Ce que l'admission apporte est ailleurs : la grammaire est prête le jour où la forme est adoptée, et un engagement volontaire pris sur ce modèle aujourd'hui s'écrit sans être déformé.

**Ce qui reste applicable.** §8.5.6.4 s'applique **intégralement** : aucune des trois formes n'institue d'instance délibérative, qui doit donc être déclarée par ailleurs — comité de mission d'une société à mission, comité ad hoc contractuel, ou autre forme déclarée. **Une chose qui satisfait la condition T par une forme admise, sans instance délibérative déclarée, n'est pas inscrite comme commun.** La table §8.5.2 et R1 s'appliquent telles quelles.

**Illustration — le marais des Lagneux** (rapport, p. 308). Une commune, propriétaire, consent une ORE au Conservatoire d'espaces naturels de Savoie, avec une convention de gestion. **Typage** : commune `P+ + D+` *propter rem* ↔ Conservatoire `C+`, `classe_creance = PRESTATION`, `creance_repartissable = FAUX`. **La condition T est satisfaite.** Mais les engagements réciproques ne sont pas documentés par la source (`NONDECLARE`, écriture incomplète), et aucune instance délibérative n'est connue. **Résultat : `INDETERMINE`, non inscrit comme commun en l'état.** `[CAS DE PAPIER — reconstitué à partir d'un paragraphe du rapport ; aucun contrat consulté.]`

**Le critère de divisibilité est fixé pour ces trois formes, et pour elles seules.** Le critère de divisibilité s'applique au `C+` des écritures `D+ ↔ C+` relevant d'une forme admise. **Pour les autres écritures `D+ ↔ C+`** — propriété collective ordinaire, indivision à quotes-parts —, **la question reste ouverte.** `[PORTÉE DÉCLARÉE — ne pas élargir tacitement.]`

`[CONDITIONS DE RÉFUTATION]` **(1)** La règle A tombe si l'on exhibe une chose reconnue comme commun par sa communauté **dont toutes les classes de créance sont répartissables en valeur**. Candidat : la **fiducie de compensation « réserve à compensation »** (p. 297), où le fiduciaire vend des unités de compensation. Sous les règles A et B, le cas ne réfute pas : la vente s'écrit en `VALEUR_ECONOMIQUE`, l'utilité écologique en `USAGE` ou `PRESTATION`. **Il réfuterait si aucune classe non répartissable n'y était identifiable.** **(2)** La règle B tombe si la déclaration de la valeur économique se révèle **impossible à obtenir en pratique** sur les fiducies réelles (secret des affaires, financeurs non identifiés) : elle deviendrait alors une condition que personne ne remplit, c'est-à-dire vide.

*Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Ancrage PR-30 :* règle A — `une_classe_non_repartissable_suffit`, `la_qualification_agregee_n_est_pas_la_qualification_par_classe` ; règle B (fiducie) — `classe_manquante_rend_indetermine`, `la_completude_prime_sur_la_classe_qualifiante`. *La forme des règles, non leur justesse.*

*Critère de vérification :* un cas de fiducie et un cas d'ORE réels typés, toutes classes déclarées, `porteur_instance` renseigné pour les trois instances.

`[DROIT EN VIGUEUR NON VÉRIFIÉ]` Les articles cités le sont d'après le rapport (avril 2021). Durée maximale de la fiducie, nullité de la fiducie-libéralité (art. 2013), qualité de fiduciaire (art. 2015), onérosité de l'ORE : **à contrôler sur Légifrance avant tout usage probant.**

##### 8.5.6.3 Les trois configurations de communalité, et la configuration négative

| Cas | Droit | Livre du détenteur ou du collectif | Livre du bénéficiaire | Commun ? |
| :-- | :-- | :-- | :-- | :-: |
| **Chose commune** — art. 714 C. civ. | inappropriable par nature ; *« l'usage est commun à tous »*, *« des lois de police règlent la manière d'en jouir »* | **aucun `P`** ; registre de communalité (§8.5.0) | usage universel ; instance délibérative tenue par la loi de police | **oui** |
| **Propriété collective avec règles d'usage** | propriété | **`P+ + D+`** | **`C+`** des membres | **oui**, sous la condition de §8.5.6.4 |
| **Intérêt diffus sans prérogative distribuée** | aucun titre | — | **aucun acteur identifié** → **`E+ ↔ ∅`** | **oui** |
| **Affectation volontaire à un intérêt commun** — fiducie, ORE, ORIC  | contrat (fiducie : C. civ. art. 2011 s. ; ORE : C. env. art. L. 132-3 ; ORIC : **proposition non adoptée**) | **`P+ + D+`** (fiduciaire ; propriétaire, *propter rem*) | **`C+` par classe** (`classe_creance`) | **oui**, si au moins une classe est non répartissable, **et** sous les conditions de §8.5.6.2bis et §8.5.6.4 |
| **Chose sans maître** — art. 713, *res nullius* | appropriable par occupation, **aucune règle d'usage** | aucun, puis **`P+` seul** après occupation | aucun | **non** |
| **Propriété privée ou publique exclusive** | propriété | **`P+` seul** | aucun | **non** |

**Correction de vocabulaire inscrite.** La catégorie du commun sans propriétaire est la **chose commune** de l'article 714, **non la *res nullius*** de l'article 713. Le rapport source fait lui-même la distinction : *« Ce n'est donc pas une res nullius sur laquelle un droit de propriété naîtrait par simple occupation, mais une res communes qui ne peut appartenir à quiconque et dont l'usage reste commun à tous. »* **La différence porte la règle** : une res nullius est sans propriétaire *et sans règle d'usage*, et elle devient un `P` pur dès l'occupation — c'est le degré zéro, non le commun. **Le cas « aucune propriété » n'est donc pas le cas sans créance : c'est le cas le plus pur de créance sans patrimoine.**

`[RÉSERVE DE DROIT — le rapport précise que les frontières ne sont pas nettes en pratique : *« selon les cas, l'eau peut être considérée comme un bien privé, un bien public ou encore être considérée comme un res nullius ou une chose commune »*. La table ci-dessus est opératoire pour le typage, non pour la qualification juridique d'un cas d'espèce.]`

##### 8.5.6.4 Nécessaire et non suffisant — le pont F6 ↔ F8

Le rapport source décompose la communalité en **trois instances** : **attributaire** (qui accède à la chose et en jouit), **délibérative** (qui est informé et participe aux décisions), **de contrôle** (qui peut défendre un droit d'usage et agir en justice).

> **`P+ + D+ ↔ C+` établit l'instance attributaire, et elle seule.** Une chose dont les utilités sont distribuées mais dont personne ne fixe collectivement les règles n'est pas un commun : c'est une indivision, une servitude, ou une fiducie. **Le typage T est donc une condition nécessaire et non suffisante.**

**Contrepartie obligatoire de la règle.** Toute inscription d'une chose comme commun déclare, dans **C-DROITS (F6)**, `communalite_instance` **incluant DELIBERATIVE et CONTROLE**, et nomme leurs porteurs par `droit_gestion` et `droit_exclusion`. *Ancrage PR-58 :* le typage est nécessaire (`le_typage_est_necessaire`) et non suffisant (`une_indivision_n_est_pas_un_commun`) ; sans instance délibérative ou de contrôle, pas de commun (`sans_instance_deliberative_pas_de_commun`, `sans_instance_de_controle_pas_de_commun`) ; une forme admise sans délibération n'est pas un commun (`une_forme_admise_sans_deliberation_n_est_pas_un_commun`, le marais des Lagneux) ; `P+` seul n'est jamais un commun (`la_propriete_seule_n_est_jamais_un_commun`) ; l'intérêt diffus se passe d'attributaire (`l_interet_diffus_se_passe_d_attributaire`) ; témoin `commun_temoin_discriminant`. *La forme de la règle, jamais qu'une chose est un commun.*

**Le pont, et sa clé.** Les deux fiches parlent du même objet dans deux vocabulaires ; la correspondance est la suivante :

| `nature_prerogative` (C-DROITS, F6) | Typage correspondant (T, F8) | Configuration |
| :-- | :-- | :-- |
| **DROIT\_SUBJECTIF** | **`C+`** — droit d'usage attaché à un acteur identifié | propriété collective avec règles d'usage |
| **UTILITE\_PUBLIQUE** | usage universel **sans `P`** | chose commune, art. 714 |
| **INTERET\_DIFFUS** | **`E+ ↔ ∅`** — asymétrie existentielle (§8.5.2) | intérêt diffus, générations futures |

**Le pont a une seconde jambe.** `droit_ne_pas_etre_exclu_usage` (C-DROITS, F6), *« contre-écriture R1 du `droit_exclusion` »* qui lève un `[ENGAGEMENT SANS SYMÉTRIE]`, **est la créance du membre écrite dans le vocabulaire de F6** : c'est le même geste que le `D+` du collectif — dire que tenir la chose oblige envers ceux qui en usent. **Identité déclarée : `droit_ne_pas_etre_exclu_usage` (F6) et le `C+` du membre (F8) sont le même objet vu deux fois.** `[RÉSERVE HÉRITÉE — ce champ porte `[source NON VÉRIFIÉE → W-6]` (Holder & Flessas 2008, via Fournier §2) ; l'identité hérite de cette réserve.]`

##### 8.5.6.5 Ce que la règle préserve, et ce qu'elle ne fait pas

**Ce qu'elle préserve.** A3 visait la réversion documentée par le rapport fondateur du Web 3 — *l'hyper-financiarisation de la nature* (Annexe H §H.12.3). La règle y répond mieux qu'une interdiction : **une chose ne peut pas être présentée comme un commun dans le registre tout en étant tenue comme un `P` pur.** Et la céder oblige à déclarer le sort des `D` attachés — donc à exhiber, au moment de la cession, l'obligation que la présentation comme commun supposait.

**Ce qu'elle ne fait pas.** Elle dit ce qu'une écriture établit ; **elle ne dit pas qui a qualité pour inscrire le `D+`**. Cette question relève du consortium de gouvernance (Annexe H §H.1) et du triplet porteur (§H.1.3bis).

> ### `[DÉCISION DU PORTEUR — qui a qualité pour inscrire le D+ d'un commun : renvoi aux règles propres du collectif, déclarées dans l'écriture.]`
>
> **Périmètre.** Ne relèvent pas de la règle : les formes admises (§8.5.6.2bis), où **l'acte désigne l'obligé** ; les `E+ ↔ ∅`, sans `D+` ; le retrait d'une habilitation, réglé en Annexe H §H.2.1. **Le résidu est le `D+` pris par un collectif sans acte qui en désigne l'obligé.**
>
> **Règle 1 — le registre ne confère aucune habilitation, il exige qu'elle soit citée** (`source_engagement_D`, §8.5), au sens de §B.2 borné. **Le MRC n'impose ni majorité, ni quorum, ni collège** : il renvoie à ceux que le collectif s'est donnés (§B.2, raison de fond ; rapport fondateur p. 131).
>
> **Règle 2 — portée bornée.** Un `D+` fondé sur les règles propres d'un collectif **n'engage que ce collectif** et ne grève aucun tiers non soumis à ces règles (patron §8.4ter, régime GESTION).
>
> **Règle 3 — la pratique ne suffit pas.** Un `D+` sans source d'engagement — légitimité `PRATIQUE` seule — n'est pas un `D+` de commun : `[HABILITATION NON ÉTABLIE — D+ SANS SOURCE D'ENGAGEMENT]`, marqueur, jamais sanction (R0-bis) ; l'écriture peut demeurer `E+ ↔ ∅` si ses conditions sont réunies.
>
> **Règle 4 — contestation.** Tout membre peut contester que la source citée donne le pouvoir d'engager ; l'habilitation passe en **suspension** (Annexe H §H.2.1), donc publique. Le registre inscrit l'ouverture et l'issue de la contestation ; il ne la tranche pas.
>
> *Porteur :* porteur MRC / architecte (règle) ; le collectif (chaque source). *Horizon :* institutionnel, révisable. *Critère de vérification :* un `D+` de commun inscrit sur un terrain K3 avec une source d'engagement vérifiable par un tiers. *Condition de réfutation :* un cas documenté de `D+` **conforme** à des règles propres déclarées qui engage le collectif **contre** une partie de ses membres — capture des règles (cf. `signal_collège_absent`, Annexe K). `[LIMITE DÉCLARÉE — renvoyer aux règles propres, c'est renvoyer aussi à leurs asymétries ; la citation de la source les rend visibles, elle ne les corrige pas.]`
>
> *Ancrage PR-30 :* `citer_ses_regles_n_engage_pas_les_tiers` (règle 2), `la_pratique_seule_marque_et_ne_qualifie_pas` (règle 3), `droit_d_ecrire_n_est_pas_pouvoir_d_engager` (témoin PLE Niayes). La règle 4 (contestation) n'est pas modélisée.
>
> *Application K3 (instruction §4) :* CLE Drôme — `TEXTE_INSTITUANT` + délibération, inscriptible dans sa compétence **sous condition** : Si l'eau de la Drôme est une chose commune, les volumes prélevables ne s'écrivent peut-être pas en `D+` de la CLE : ils relèveraient du cas prescriptif de §8.5.6.5 (`prescription_etat`), qui n'est pas instruit, et le classement de la CLE dans le tableau K3 reste conditionnel. ; PLE Niayes — `REGLES_PROPRES_COLLECTIF`, inscriptible **envers ses membres seulement** (non décisionnaire à l'égard des industriels) ; OLGE Lac Togo — **habilitation non établie** tant que l'instance n'est pas instituée, les communes pilotes pouvant engager dans leur compétence.

**Condition de réfutation de la règle.** Elle tombe si l'on exhibe une chose **tenue pour un commun par sa communauté et par le droit**, dont l'écriture ne porte ni `D+ ↔ C+` ni `E+`, et dont on établit qu'elle ne devrait pas les porter. Le cas candidat le plus sérieux est celui d'une communalité purement **prescriptive** — une chose qu'aucun titulaire ne revendique et dont l'État seul règle l'usage (`prescription_etat`) : il faudrait alors établir que la prescription étatique ne s'inscrit ni comme `C+` universelle ni comme `E+`.

*Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* une chose inscrite comme commun dont l'écriture porte l'un des trois patrons, et dont `communalite_instance` inclut DELIBERATIVE et CONTROLE avec leurs porteurs nommés.

#### 8.6 Sous-couche C-COMPTABILITE-CARE — spécialisation du régime CARE

C-COMPTABILITE-CARE est une spécialisation de la couche R pour le régime CARE (→ NT-G12). Elle détaille les comptes étendus de l'actif et du passif CARE, le valorimètre associé, le principe d'amortissement écologique, et les conditions opérationnelles d'inscription. Elle est l'analogue des champs nommés des fiches F1 à F4 pour le mode comptable.

Champs de C-COMPTABILITE-CARE

| **Champ**                     | **Type**                  | **Valeurs / Exemples**                                                     | **Description**                                                                                                     |
| ----------------------------- | ------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| compte\_actif\_CARE           | Énumération               | ACTIF\_FINANCIER / ACTIF\_NATUREL / ACTIF\_HUMAIN                          | Catégorie d'actif CARE. Étend les catégories du bilan financier.                                                    |
| compte\_passif\_CARE          | Énumération               | CAPITAUX\_PROPRES / DETTE\_FINANCIERE / DETTE\_NATURELLE / DETTE\_HUMAINE  | Catégorie de passif CARE. Inclut les dettes NH.                                                                     |
| amortissement\_ecologique     | Couple (montant, méthode) | ex. : (32 651,70 €, IDEA4)                                                 | Amortissement périodique destiné à provisionner le maintien des capitaux NH. Distinct de l'amortissement financier. |
| valuemetre\_uri               | **Identifiant stable et résoluble**  | référence de méthode publiée (DOI, norme datée) + empreinte de la version employée ; ou DID ; ex. did:registre:valuemetre:idea4 | Identifiant du valorimètre utilisé pour évaluer les capitaux NH (Annexe H.2). **Satisfait les quatre propriétés de §B.2 ; le DID est une forme possible, non obligatoire.** |
| consentement\_inscription\_NH | Énumération ternaire | VRAI / FAUX / **NON\_DETERMINABLE**  | Le consortium de gouvernance NH a-t-il consenti à l'inscription du capital NH considéré ? NON\_DETERMINABLE : **aucun consortium de gouvernance NH n'existe ou n'a été consulté**. À distinguer de FAUX, qui est un refus. Cas attesté : le registre RATP 2025, où aucun consortium n'existe. **Titulaire : voir l'encadré A5 ci-dessous — le consortium de gouvernance (Annexe H §H.1) est le seul titulaire admis ; un organe de contrôle ne l'est pas.** |
| resultat\_distribuable        | Montant                   | ex. : 69 207,30 € (K1) après application R-PRIORITE-CREANCIERS             | Résultat après préservation NH, sur lequel s'arbitre la distribution (cf. C-PRIORITE-CREANCIERS, § 8.7).            |
| taux\_couverture\_DNH         | Pourcentage               | ex. : 100 % (effort effectif sur DNH inscrite à l'exercice)                | Taux de couverture des dettes NH par les efforts effectifs de l'exercice. Doit tendre vers 100 % à long terme.      |
| doctrine\_CARE\_appliquee     | Référence                 | → NT-G12 ; IDEA4 v4 ; doctrine locale                                  | Doctrine CARE de référence pour le calcul des amortissements et des dettes NH.                                      |
| **portee\_attestation**  | Énumération | ECRITURE / PROCEDURE / TRAJECTOIRE | Portée de l'attestation produite par un tiers sur ces écritures. **Une attestation de portée `PROCEDURE` ne vaut pas attestation des écritures qu'elle couvre** : elle atteste que le dispositif qui les produit a été examiné. Obligatoire dès qu'une attestation de tiers est invoquée. |
| **periodicite\_attestation**  | Durée | ex. : 2 ans (OTI, ≥ 50 salariés) ; 1 an (comité de mission) ; continue (dMRV) | Périodicité du passage de l'attestataire. **Une attestation dont la périodicité excède la fréquence des écritures ne peut pas porter sur les écritures individuelles.** |

> ### `[A5 — TITULAIRE DE `consentement_inscription_NH`. Décision du porteur. Instruction : `A5_Instruction_Societe_a_Mission_2026-09-21.md` ; renvoi : Annexe H §H.10.2.]`
>
> **Le seul titulaire admis est le consortium de gouvernance du commun** (Annexe H §H.1), qui déclare son `legitimiterepresentant` et, le cas échéant, sa `conditionrefutation` (§5.2).
>
> **Un organe de contrôle n'est pas un titulaire admis, et l'organisme tiers indépendant d'une société à mission en particulier ne l'est pas.** La raison n'est pas de défiance : **consentir au nom d'un non-humain est un acte de l'instance attributaire** — parler pour le bénéficiaire — tandis que l'OTI est un organe de l'instance **de contrôle** (§8.5.6.4). Prendre l'un pour l'autre, c'est prendre un vérificateur de procédure pour un porte-parole. `[DÉCOUPLAGE DE RÉGIMES évité, déclaré.]`
>
> **Ce que l'OTI peut néanmoins porter** : une attestation de `portee_attestation = PROCEDURE` ou `TRAJECTOIRE` sur les écritures de préservation NH, avec sa `periodicite_attestation`. **Cela ne rend pas `consentement_inscription_NH` VRAI** ; cela documente que la procédure d'inscription a été examinée par un tiers accrédité.
>
> **Ce que l'attestation établit au regard de §B.2 borné** : la **quatrième propriété** — porteur nommé et réfutable — et **partiellement la troisième**. Pas la justesse du valorimètre : l'intervention est une **assurance modérée**, qui vérifie la sincérité des indicateurs sans garantir leur exactitude.
>
> `[LACUNE NON LEVÉE — pour le registre RATP 2025, `consentement_inscription_NH` reste NON\_DETERMINABLE : l'EPIC n'est pas une société à mission et aucun consortium de gouvernance NH n'existe. **Le couplage A5 ne crée pas de titulaire là où il n'y en a pas.**]`

#### 8.6.1 Exemple chiffré — application au cas K1 (Exploitation B)

| **Champ**                                      | **Valeur K1**                                                              | **Source**                                                                                                        |
| ---------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| compte\_actif\_CARE — actif naturel net        | 8 959,2 €                                                                  | K1 tableau 1 (annexe K du set, Exploitation B)                                                                            |
| compte\_actif\_CARE — actif humain net         | 2 921 925 €                                                                | K1 tableau 1                                                                                                      |
| compte\_passif\_CARE — dette naturelle         | 10 605,9 €                                                                 | K1 tableau 2                                                                                                      |
| compte\_passif\_CARE — dette humaine totale    | 2 952 930 €                                                                | K1 tableau 2 (dont 2 901 312 € de salaires décents long terme)                                                    |
| amortissement\_ecologique de l'exercice        | 32 651,70 €                                                                | K1 tableau 3 (coût de préservation NH = écart entre résultat classique et résultat CARE)                          |
| valuemetre\_uri                                | did:registre:valuemetre:idea4 + did:registre:valuemetre:cout-pres-exploitB | K1 tableau 3 (acteurs valorimètre)                                                                                 |
| resultat\_distribuable                         | 69 207,30 €                                                                | K1 tableau 3 ; sous réserve de R-PRIORITE-CREANCIERS                                                              |
| taux\_couverture\_DNH (NH naturelle, exercice) | ≈ 100 % au prorata du plan annuel                                          | K1 section K.6 — la couverture est partielle au regard de la dette totale ; complète au regard du plan d'exercice |

#### 8.6.2 Articulation écologique CEC ↔ CARE — table de versement, miroir typé, routage des irréversibles

L'articulation des **trois comptabilités écologiques** — gestion écosystème-centrée (CEC), organisationnelle (CARE), nationale (dette écologique / CENP) — est instrumentée ici comme Couche 2, sans primitive nouvelle (fondements et sources : → NT-G12 ; méthode du verrou micro-macro : → Annexe méthodologique §A.6).

**Table de versement CEC ↔ objets MRC.**

| Notion CEC | Objet MRC | Localisation |
|---|---|---|
| Dette écologique | `SYSTEMIQUE_NON_ATTRIBUEE` (forcée vers DELIBERATION) | Partie A, machine d'états |
| Contribution | Écriture allouée `HYBRIDE` | Partie A / F8 |
| Part imputable | `fractionactorielle` **déclarée** (B1) | Partie A |
| Cible de bon état | `seuilalertemilieu` / `seuilentreecommunautemorale` | F2 |
| Comptes | F2 (milieu) + F8 (mouvements typés) | Couche 2 |

*Critère de vérification.* Un cas CEC se transcrit en F2/F8 **sans champ orphelin**. *Condition de réfutation.* Si la transcription d'un cas CEC/CARE exige une primitive de Couche 0 nouvelle non réductible aux champs F2/F8/F4 existants, la table est invalide localement et une décision de gouvernance est requise.

**Contre-écriture CARE typée (miroir obligatoire).** Toute écriture de préservation CARE déclare le statut de son miroir : `ATTRIBUEE` (local), `SYSTEMIQUE` (collectif CEC), ou `E+` existentiel (→ F4). C'est l'une des deux asymétries déjà autorisées par R1 (§3bis : dette systémique / engagement existentiel), non une violation. *Critère :* zéro charge de préservation sans miroir typé.

**Règle unique de routage F4 (irréversibles).** Tout objet dont la restauration est hors d'atteinte sort de la dette remboursable (F8) et bascule en mode existentiel F4, `[ENGAGEMENT À HORIZON IRRÉVERSIBLE — délibération avant conclusion]`. La frontière F8/F4 s'appuie sur l'invariant ACT-ARCH-001 (§7bis). Cas d'application déclaré : capital écologique non restaurable (CEC/CARE) ; la règle est unique, tout cas nouveau s'y rattache sans réinscription séparée.

**Garde-fou de régime.** Ne jamais présenter la commutativité micro-macro ni l'articulation individuel↔systémique comme closes : la forme atteignable ici est la gouvernance déclarée de la non-clôture (double comptabilité déclarée, → Annexe §A.6) ; présenter cette double comptabilité comme une complétude serait un `[DÉCOUPLAGE DE RÉGIMES]`.

#### 8.7 Sous-couche C-PRIORITE-CREANCIERS — implémentation de la règle R-PRIORITE-CREANCIERS

La règle R-PRIORITE-CREANCIERS (Couche 1, Piste 3 de la note de cadrage) formalise l'ordre suivant : on rembourse d'abord les capabilités plancher (Niveau 1), puis les dettes envers les capitaux NH (Niveau 2), puis les dettes financières contractuelles (Niveau 3), avant toute distribution discrétionnaire au capital financier (Niveau 4). F8 implémente cette règle au niveau opérationnel via C-PRIORITE-CREANCIERS, en cohérence avec l'Annexe H.4 (covenants) et H.5 (smart contracts).

Champs de C-PRIORITE-CREANCIERS

| **Champ**                     | **Type**        | **Valeurs / Exemples**                                                     | **Description**                                                                                                                |
| ----------------------------- | --------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| niveau\_prioritaire           | Énumération     | N1\_CAPABILITES / N2\_DETTE\_NH / N3\_DETTE\_FINANCIERE / N4\_DISTRIBUTION | Niveau de priorité de l'inscription considérée selon R-PRIORITE-CREANCIERS.                                                    |
| seuil\_capabilites\_satisfait | Énumération ternaire | VRAI / FAUX / **NON\_DETERMINABLE**  | Niveau 1 — Toutes les capabilités plancher (Fiche F6) sont-elles satisfaites pour les acteurs concernés ? NON\_DETERMINABLE : les capabilités plancher n'ont pas été évaluées. |
| dette\_NH\_couverte\_exercice | Énumération ternaire | VRAI / FAUX / **NON\_DETERMINABLE**  | Niveau 2 — Les charges de préservation effectivement réalisées couvrent-elles le plan de l'exercice ? NON\_DETERMINABLE : la dette NH n'a pas été calculée pour l'exercice. |
| dette\_financiere\_honoree    | Énumération ternaire | VRAI / FAUX / **NON\_DETERMINABLE**  | Niveau 3 — Les dettes financières contractuelles exigibles sont-elles honorées ? NON\_DETERMINABLE : l'exigibilité n'a pas été vérifiée. |
| distribution\_autorisee       | Ternaire calculé | VRAI ssi N1 ∧ N2 ∧ N3 tous VRAI ; **NON\_DETERMINABLE si l'un au moins est NON\_DETERMINABLE et qu'aucun n'est FAUX** ; FAUX sinon  | Niveau 4 — La distribution discrétionnaire est-elle autorisée selon les niveaux 1-3 ? **Une valeur NON\_DETERMINABLE n'autorise pas la distribution : elle n'établit pas qu'elle soit interdite, et c'est pourquoi elle ouvre la phase DELIBERATION plutôt qu'elle ne lève `signal_distribuable_avant_NH`.** |
| regime\_application           | Énumération     | **SOFT** (seule valeur disponible) /  **PROJETÉ**  | SOFT : signal critique **sans blocage**. HARD : blocage via smart contract (Annexe H.5) — **valeur PROJETÉE, non instanciable** tant que les spécifications de H.5 ne sont pas versées : ni chaîne, ni langage de contrat, ni schéma pour `smart_contract_uri`, ni mécanisme d'interruption. Toute écriture porte donc `SOFT`. |
| smart\_contract\_uri          | **Sans instance — SUSPENDU**  | did:registre:smartcontract:priorite-creanciers-cas-X | Identifiant du smart contract qui exécute la règle. Annexe H.5. **`HARD` et l'Usage 3 sont PROJETÉS (A7, §8.7bis) : le champ n'a aucune instance.** Sa première spécification n'est **ni la chaîne ni le langage, mais le mécanisme d'interruption** — qui arrête l'exécution, sur quel constat, avec quelle trace. Le rapport fondateur en fait le défaut central des dispositifs existants : le contrat s'exécute *« automatiquement et sans possibilité d'interruption manuelle »* (p. 113). |
| motif\_violation              | Texte           | ex. : plafond mordant Bercy (K3 Drôme)                                     | Si distribution\_autorisee = FAUX mais une distribution est néanmoins inscrite, motif documenté.                               |

#### 8.7bis `R-PRIORITE-CREANCIERS` signale et ne bloque pas — décision du porteur

**Le constat.** `regime_application = HARD` signifie « blocage via smart contract H.5 ». L'Usage 3 exige « smart contracts d'Annexe H.5 actifs ». **Aucune spécification n'existe** : l'Annexe H décrit des fonctions et n'arrête ni chaîne, ni langage de contrat, ni schéma d'URI, ni mécanisme d'interruption — elle le déclare elle-même en H.5.3. Le seul cas chiffré du set, K1, porte `SOFT` et `smart_contract_uri = ∅`.

**La décision.** `HARD` et l'Usage 3 sont marqués **PROJETÉS**. En conséquence :

> **`R-PRIORITE-CREANCIERS` est explicitement non contraignante. Elle signale et ne bloque pas.**

**Ce que le set annonce et ce qu'il fait coïncident** : un dispositif d'inscription et d'alerte, qui signale sans bloquer. Le régime effectivement praticable est l'**Usage 2** : le jalon J1, qui a typé 56 écritures du registre RATP 2025, s'y est déroulé, et il a produit un résultat.

**Ce qui subsiste, et qui est l'essentiel.** Une distribution inscrite alors que `distribution_autorisee` est FAUX **passe**, mais elle passe **sous condition** : `motif_violation` devient obligatoire, `signal_distribuable_avant_NH` est levé, et la phase DELIBERATION s'ouvre. Le registre ne l'empêche pas ; **il rend impossible de la faire sans laisser de trace et sans se justifier**. C'est une contrainte d'inscription, non d'exécution — et c'est ce que le mode procédural sait faire.

**Ce que cela clarifie pour le cas K3.** Le plafond mordant Bercy y est qualifié de « violation Niveau 3 ». La décision A7 *(non l'axiome AX-7)* vaut pour les trois terrains : **les trois sont en SOFT**, et la violation est inscrite avec son motif plutôt que bloquée. La différence entre les terrains n'est pas un régime d'application, c'est un **degré de renseignement des champs**.

**Condition de réfutation, et chemin de sortie.** La décision tombe le jour où les spécifications de H.5 sont versées — chaîne, langage, schéma d'URI, mécanisme d'interruption — et où un covenant est effectivement déployé. `[OBLIGATION OUVERTE — porteur : porteur MRC / architecte ; horizon : institutionnel ; critère : un smart contract de R-PRIORITE-CREANCIERS déployé sur un cas réel, dont l'identifiant renseigne `smart_contract_uri`. Tant que ce critère n'est pas rempli, aucune présentation externe du modèle ne peut annoncer un blocage.]`

**Réserve sur le blocage lui-même.** Le rapport fondateur de l'Annexe H documente qu'un contrat qui s'exécute « de façon automatique et sans possibilité d'interruption manuelle » sur un oracle compromis exécute une preuve corrompue (Annexe H §H.12.1). **Le régime HARD n'est donc pas seulement indisponible : il n'est pas souhaitable sans mécanisme d'interruption déclaré.** La décision A7 ne fait pas que constater un manque ; elle met le set à l'abri d'une automatisation prématurée.

#### 8.7.1 Application au cas K3 — le plafond mordant Bercy comme violation Niveau 3

K3 documente précisément la violation Niveau 3 de R-PRIORITE-CREANCIERS via le mécanisme du plafond mordant Bercy. Les recettes de redevance de l'Agence de l'eau Rhône-Méditerranée-Corse au-delà d'un plafond fixé par Bercy sont captées par le budget général de l'État au lieu d'être affectées à la préservation NH. Le champ motif\_violation est renseigné comme « plafond mordant Bercy — captation budget général ». Le régime\_application est SOFT sur les trois terrains (décision A7, §8.7bis) ; pour la Drôme, le dispositif est institutionnel existant, sans smart contract.

#### 8.8 Sous-couche C-CYCLE-PRIX — cycle performatif du juste prix écologique

C-CYCLE-PRIX implémente la conception du juste prix écologique (→ NT-G12) comme cycle performatif. Cette conception articule la fixation des prix à la couverture des dettes NH : un prix n'est juste écologiquement que s'il intègre le coût de préservation des capitaux NH mobilisés par la production. Le cycle e ↔ d (effort de préservation ↔ résultat de préservation attesté) est l'instance type. Il a été documenté en K3 via la proposition Defalvard (Visi'eau, septembre 2024) sur la transformation de la redevance Agence de l'eau en financement direct de l'animation territoriale.

Champs de C-CYCLE-PRIX

| **Champ**                  | **Type**      | **Valeurs / Exemples**                                               | **Description**                                                                                     |
| -------------------------- | ------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| prix\_inscrit              | Montant       | ex. : prix de marché ou prix réglementé                              | Prix actuel inscrit dans la comptabilité.                                                           |
| cout\_preservation\_inclus | Énumération ternaire | VRAI / FAUX / **NON\_DETERMINABLE**  | Le prix inscrit inclut-il le coût de préservation NH ? NON\_DETERMINABLE : la décomposition du prix n'est pas documentée. |
| ecart\_juste\_prix         | Montant signé | ex. : −12 % par rapport au juste prix écologique                        | Écart entre prix inscrit et juste prix écologique calculé.                                          |
| cycle\_e\_d\_actif         | Énumération ternaire | VRAI / FAUX / **NON\_DETERMINABLE**  | Le cycle e (effort de préservation) ↔ d (résultat attesté par dMRV) fonctionne-t-il effectivement ? NON\_DETERMINABLE : aucune attestation de résultat n'a été produite — à distinguer de FAUX, qui exige `rupture_cycle` documentée. |
| rupture\_cycle             | Texte         | ex. : plafond Bercy ; absence de VC ; instance gouvernance manquante | Si cycle\_e\_d\_actif = FAUX, motif documenté de la rupture.                                        |
| doctrine\_juste\_prix      | Référence     | → NT-G12 ; LIFTS ; doctrine locale                                | Doctrine de calcul du juste prix appliquée.                                                         |
| **hors\_champ\_optimisation**  | Texte — **obligatoire dès que le seuil déclenche un effet financier** | ex. : « optimiser le coût de préservation de l'eau laisse hors champ la biodiversité des berges et la qualité du sol, qu'aucun indicateur du cycle ne mesure » | **Ce que l'optimisation de ce seuil laisserait hors champ.** Contrepartie obligatoire de tout déclenchement : *« dès lors qu'un indicateur mesurable déclenche automatiquement une récompense financière, les porteurs de projets sont structurellement incités à optimiser cet indicateur spécifique »* au détriment de ce qui se mesure mal (rapport fondateur §2.2.1.2, p. 114 ; Goodhart 1975 ; KlimaDAO). **Le champ ne demande pas de résoudre le biais, il demande de le nommer avant qu'il opère.** Renvoi : Annexe H §H.4 et §H.12.2 |

#### 8.9 Sous-couche C-SIGNAL.F8 — signaux propres au mode comptable

Les signaux propres à F8 sont rattachés aux quatre lieux de tension du dispositif comptable : (a) la rupture du cycle e ↔ d ; (b) la violation de la priorité créanciers ; (c) l'asymétrie informationnelle entre régimes ; (d) l'effacement injustifié d'une obligation NH.

| **Signal**                             | **Condition de déclenchement**                                                                                                                             | **Action / Phase C-ENQUETE-V5**                                                                                                                                |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| signal\_distribuable\_avant\_NH        | distribution\_autorisee = FAUX ∧ une distribution est inscrite (mouvement j ou h en CARE)                                                                  | **Lève une alerte critique et n'empêche rien** ; `motif_violation` devient obligatoire ; déclenche la phase DELIBERATION. *(Le blocage relèverait du régime HARD, PROJETÉ — A7.)* |
| signal\_amortissement\_NH\_insuffisant | taux\_couverture\_DNH \< seuil\_doctrinal                                                                  | Inscription C-MEMOIRE-PERTES ; alerte au consortium de gouvernance NH ; phase ENQUETE\_OBSERVATIONNELLE                                                        |
| signal\_cycle\_prix\_derive            | ecart\_juste\_prix \> seuil\_doctrinal du juste prix `[SEUIL SANS SOURCE — la doctrine de calcul est nommée en §8.8 (`doctrine_juste_prix`) mais aucune valeur de seuil n'y est arrêtée.]`                                                                              | Renvoie à C-CYCLE-PRIX ; déclenche révision du valorimètre ; phase REDEFINITION\_BUTS dans C-DPQT si applicable                                                 |
| signal\_translation\_manquante         | Une écriture est inscrite dans un régime CARE / IIRC   sans qu'une traduction soit disponible dans un régime de référence externe (typiquement IFRS) | Marqueur explicite du différentiel inter-régime ; consultation par auditeurs et financeurs ; documentation pour la jurisprudence sur l'image fidèle (→ NT-G12) |
| signal\_remise\_NH                     | Mouvement m (D↓ / ΔS↑) appliqué à une dette NH sans consentement du consortium de gouvernance NH                                                           | **Alerte critique ; l'inscription n'est pas empêchée** ; remontée au consortium de gouvernance NH ; phase AUTOGOUVERNANCE. *(Le blocage relèverait du régime HARD, PROJETÉ — A7.)* |
| signal\_priorite\_violee               | Mouvement j ou h inscrit malgré distribution\_autorisee = FAUX en régime SOFT                                                                              | Inscription explicite de motif\_violation ; transmission au registre public ; phase ENQUETE\_COLLECTIVE                                                        |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Signal signal\_translation\_manquante — Ce signal rend visible la quantité d'information CARE / IIRC / LIFTS que la publication financière IFRS efface. Son utilité opérationnelle est triple : il alimente le rapport de gestion par une donnée chiffrée (volume d'écritures CARE sans miroir IFRS) ; il documente, pour la jurisprudence future, le champ des obligations que la comptabilité financière dominante n'inscrit pas — utile pour la qualification de l'image fidèle au sens du droit comptable positif (→ NT-G12) ; il quantifie la perte informationnelle de la projection π : V^CARE → V^IFRS (statut formel : F3 §3.5).** |

#### 8.10 Connexions inter-fiches et inter-annexes

| **Connexion**                       | **Description**                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| → F1 (Mode travail)                 | Le typage e (effort des salariés reçu) du mouvement l ou e en CARE est cohérent avec la sous-couche C-DPQT (Fiche 1) — type\_deliberation et frontiere\_metier qualifient le destinataire de l'effort. La D NH humaine au passif CARE matérialise quantitativement l'engagement R-CARE branche travail (Fiche 1, défi 3 — coûts).                                                       |
| → F2 (Mode milieu)                  | Les composites P + C de l'actif naturel et les D NH naturelles au passif CARE matérialisent quantitativement R-CARE branche non-humain (Fiche 2, défi 3 — coûts). Le signal codegradation\_calculable (Fiche 2) peut être renforcé par signal\_amortissement\_NH\_insuffisant si la couverture des D NH est durablement insuffisante.                                                   |
| → F3 (Mode sémantique)              | Le typage P-C-E-D-e-d (sous-couche T) est un dispositif sémantique : il qualifie les écritures par six primitives ontologiques. Il s'inscrit dans C-RIS (Registre d'Interactions Sémantiques) de la Fiche 3 et peut être rapproché de C-TCFP (Treillis de Concepts Formels Pondérés) pour les analyses comparatives inter-régimes.                                                      |
| → F4 (Mode existentiel)             | Le champ asymetrie\_existentielle = VRAI (sous-couche T) est cohérent avec C-FINALITE-IMMANENTE (Fiche 4) : un engagement existentiel envers un acteur non tracé (génération future, nappe fossile millénaire) est précisément le type E+ sans miroir. R-INTERDIT-ABSOLU (Couche 1, §2ter.1 ; statut formel : F3 §3.5) peut être déclenchée par F8 si un mouvement l ou n violerait formellement l'engagement. |
| → F7 (Mimétique)              | F8 doit être vigilante au signal focalisation\_victimaire si une décision comptable désigne un type de production (élevage, agro-industrie) comme bouc émissaire des dérives de l'ensemble. Le typage P pur (prélèvement sans contrepartie e ni d, K3) doit toujours être lu en cohérence avec la grammaire mimétique pour éviter une désignation injustifiée.                          |
| → F6 (Mode justice / droits) | **Distinction déclarée, non recouvrement.** `droit_exclusion` (faisceau Schlager-Ostrom, F6) porte le droit d'exclure d'une **ressource**, détenu par des ayants droit ; `cloture_declaree` (§8.2bis) porte l'exclusion d'un **périmètre économique**, sans supposer ni ressource commune ni titulaire de droit. Les deux peuvent coexister sur une même écriture et ne doivent pas être fusionnés. |
| → Annexe méthodologique §A.7 (lecture méso) | Les champs de C-CLOTURE-ACCES sont renseignés **par écriture** ; la clôture d'un espace se lit **par agrégation** sur un périmètre construit par l'analyste. C'est ce qui lève le reste déclaré « clôture concurrentielle » du §A.7 sans faire de l'espace méso une primitive. |
| → Couche 1 — R-PRIORITE-CREANCIERS  | F8 est l'instance opérationnelle de R-PRIORITE-CREANCIERS. Voir C-PRIORITE-CREANCIERS (§ 8.7).                                                                                                                                                                                                                                                                                          |
| → Couche 1 — R-INTERDIT-ABSOLU      | F8 peut déclencher R-INTERDIT-ABSOLU par le champ asymetrie\_existentielle = VRAI ; voir → F4.                                                                                                                                                                                                                                                                                          |
| → F3 §3.5                          | La projection π : V^CARE → V^IFRS (non formalisée dans ProfReg, F3 §3.5) reçoit en F8 une interprétation opérationnelle : elle opère entre couches R (R-CARE et R-IFRS), efface les écritures sans traduction IFRS, et alimente signal\_translation\_manquante.                                                                                                                                                         |
| → Annexe H.4 (covenants)            | Les covenants smart-contract correspondant à R-PRIORITE-CREANCIERS sont implémentés en H.4 et identifiés par smart\_contract\_uri (§ 8.7).                                                                                                                                                                                                                                              |
| → Annexe H.5 (smart contracts)      | Le régime HARD de R-PRIORITE-CREANCIERS est exécuté par les smart contracts de H.5. Le régime SOFT lève un signal sans blocage.                                                                                                                                                                                                                                                         |
| → Annexe H.11 (extension comptable) | L'extension H.11 dédiée aux dispositifs comptables CARE (logiciels certifiés, formats d'export, audits étendus) accueille la couche technique de F8. Recommandation conforme aux arbitrages de la note de cadrage.                                                                                                                                    |
| → Annexe K — cas chiffrés (`MRC_v5.7_Annexe_K_Cas_Chiffres.md`)           | F8 est instanciée par K1 (Exploitation B, comptabilité agricole CARE) et K3 (bassins versants, comptabilité territoriale). Elle sera enrichie par K4 (DPQT hospitalier, comptabilité de gestion santé) et K2 (gouvernance LLM, comptabilité sémantique).                                                                                                                                |

#### 8.11 Inscription de F8 dans les trois régimes d'usage du MRC

La note de cadrage distingue trois régimes d'usage du MRC. F8 a vocation à servir les Usages 2 et 3 ; l'Usage 1 n'est pas admissible pour les écritures comptables.

| **Régime d'usage**                                  | **Statut de F8**                                                                                                                                                        | **Conditions d'utilisation**                                                                                                                                                                                            |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Usage 1 — Grille heuristique LLM                    | Non admissible pour écritures opposables. Admissible comme prompt structuré pour explorer un corpus.                                                                    | Toutes les sorties sont en staging, marquées « non validée ». R-INCAPACITE-LLM-VALIDER s'applique strictement.                                                                                                          |
| Usage 2 — Registre d'enquête contrôlé               | Admissible. F8 fournit le typage P-C-E-D-e-d et la couche M comme grille d'inscription. Les écritures sont validées humainement après proposition par LLM ou chercheur. | Application des règles de cohérence miroir (§ 8.5.2) ; champ statut\_rgpd renseigné pour les écritures touchant à des personnes ; consentement préalable explicite si DPA fournisseur LLM absent.                       |
| Usage 3 — Infrastructure notariée organisationnelle **** | Régime de référence **visé** par F8 — **aucune écriture ne peut aujourd'hui y être inscrite**. Écritures opposables : identité de l'inscripteur signée, statut explicite, source horodatée, hash, traçabilité.                              | Application des huit sous-couches de F8 ; smart contracts d'Annexe H.5 actifs ; régime HARD de R-PRIORITE-CREANCIERS opérationnel ; journalisation des accès LLM ; cloisonnement des données personnelles ou sensibles. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Articulation aux arbitrages Q9 à Q12 de la note de cadrage. F8 répond comme suit à ces arbitrages : Q9 (statut sorties LLM) — proposition non validée par défaut, R-INCAPACITE-LLM-VALIDER renforcée pour les typages composites ; Q10 (seuil RGPD) — champ statut\_rgpd obligatoire en Usage 2 et 3 pour toute écriture touchant à des personnes (M8, M13) ; Q11 (statut notarial) — F8 fournit les critères d'intégrité d'écriture requis (couche M régime-invariante, signature, horodatage, hash) ; Q12 (architecture trois couches) — option A retenue (architecture trois couches adoptée).** |

#### 8.12 Exemple intégré — F8 appliquée au cas K1 (Exploitation B)

Le tableau ci-dessous propose la lecture intégrée d'une opération unique du cas K1 — l'inscription du coût de préservation NH de 32 651,70 € sur l'exercice — à travers les huit sous-couches de F8. Cette lecture illustre concrètement comment chaque sous-couche qualifie l'écriture sans contradiction.

| **Sous-couche**       | **Valeur pour l'écriture « coût de préservation NH 2024 = 32 651,70 € »**                                                                                                                                                                                                                                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C-MOUVEMENT-TYPE.M    | sigle\_mouvement = l ; variations = (A↓ caisse, ΔS↓ résultat) ; description\_geometrique = « diminution simultanée d'un actif et du résultat »                                                                                                                                                                                                                                                         |
| C-MOUVEMENT-TYPE.R    | regime\_comptable = CARE ; denomination\_regime = « charge de préservation des capitaux NH » ; compte\_imputation = compte CARE de préservation, lié au D NH ; conditions\_reconnaissance = effort de remboursement partiel d'une dette NH inscrite ; exemple\_chiffre = 32 651,70 € — Exploitation B 2024. En régime IFRS : ∅ (aucune traduction directe) → déclenche signal\_translation\_manquante. |
| C-MOUVEMENT-TYPE.T    | typage\_primitive = e (effort vers les NH) ; typage\_miroir = D− (extinction partielle de dette NH naturelle) ; **contrôle R1 : ADMIS** — couple présent en table §8.5.2, calculé et non déclaré  ; destinataire\_effort = NH\_NATUREL (sol, biodiversité, troupeau) ; asymetrie\_existentielle = FAUX                                                                                                                                                                |
| C-COMPTABILITE-CARE   | compte\_actif\_CARE = ACTIF\_NATUREL ; compte\_passif\_CARE = DETTE\_NATURELLE ; amortissement\_ecologique = (32 651,70 €, méthode IDEA4) ; valuemetre\_uri = did:registre:valuemetre:cout-pres-exploitB ; consentement\_inscription\_NH = VRAI (attesté VC consortium Chambre + Agence eau + associations) ; taux\_couverture\_DNH = ≈ 100 % du plan annuel                                           |
| C-PRIORITE-CREANCIERS | niveau\_prioritaire = N2\_DETTE\_NH ; dette\_NH\_couverte\_exercice = VRAI ; regime\_application = SOFT (Exploitation B hors dataroom augmentée à ce stade) ; smart\_contract\_uri = ∅                                                                                                                                                                                                                 |
| C-CYCLE-PRIX          | cycle\_e\_d\_actif = VRAI (l'effort de préservation produit un résultat mesurable attesté par IDEA4) ; cout\_preservation\_inclus = VRAI ; ecart\_juste\_prix = à calculer selon la doctrine du juste prix (→ NT-G12)                                                                                                                                                                                                          |
| C-CLOTURE-ACCES       | `enjeu_acces` = **NON_DETERMINABLE** ; `cloture_declaree` = ∅. **Et c'est un résultat de lecture, non un oubli** : le cas K1 tel qu'il est documenté n'énonce aucun régime d'éligibilité conditionnant l'inscription. Ce qui trancherait : savoir si un financement (Agence de l'eau, aide à la transition) est subordonné à l'évaluation IDEA4 — auquel cas `enjeu_acces` = FINANCEMENT et le consortium attestataire serait le poseur du dispositif. **Ne pas coder AUCUN** : la frontière n'a pas été cherchée, elle n'a pas été trouvée absente (→ §8.2bis) |
| C-SIGNAL.F8           | signal\_translation\_manquante levé (IFRS ne traduit pas cette écriture) ; signal\_distribuable\_avant\_NH neutre (couverture effective de N2)                                                                                                                                                                                                                                                         |
| Connexions            | → F2 (R-CARE branche non-humain défi 3 coûts ; valeur quantifiée) ; → F1 (cohérent avec la composante e qui réduit le résultat distribuable disponible pour les charges de personnel) ; → Annexe H.2 (VC consentement consortium NH) ; → F3 §3.5 (instance type de la projection π effaçante)                                                                                                       |

#### 8.13 Interface avec le droit de la comptabilité publique (→ NT-G12)

L'interface avec le droit de la comptabilité publique (sources : → NT-G12) impose trois corrections de formulation pour F8, intégrées ci-dessous.

| **Point de droit positif**                                   | **Conséquence pour F8**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Coexistence vs articulation                          | F8 ne prétend pas articuler théoriquement les régimes comptables. La couche R inscrit la coexistence de plusieurs régimes (IFRS, PCG, CARE, gestion) ; chaque régime conserve sa logique propre. Le différentiel inter-régime est inscrit comme donnée opposable (signal\_translation\_manquante), sans synthèse théorique.                                                                                                                                                                                                                                  |
| Image fidèle (→ NT-G12)                              | F8 ne convoque pas le principe de « substance over form » qui n'est pas inscrit en droit positif français. Elle se réfère au principe positif d'image fidèle (→ NT-G12) en notant que la couche R-CARE peut être lue comme une contribution à l'image fidèle par enrichissement informationnel (capitaux NH rendus visibles), à condition que la doctrine de calcul soit explicitée (champ doctrine\_CARE\_appliquee, § 8.6) et attestée par VC (champ consentement\_inscription\_NH).                                                                       |
| Dualisme État vs monisme collectivités territoriales | F8 distingue, pour le régime comptable public, les sous-régimes budgétaire / générale / analytique / comptabilité-matières, conformément au droit positif (→ NT-G12). La couche R accueille un sous-régime PCP (Plan Comptable Public) distinct du PCG. La conception dualiste de l'État (un même équipement = décaissement budgétaire + actif comptable général) est inscrite comme cas particulier du typage composite : un mouvement l (A↓/ΔS↓) en comptabilité budgétaire coexiste avec un mouvement e (A↑/D↑) en comptabilité générale. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Application au PPI aligné climat (méthode d'alignement climat des PPI, → NT-G12). Le PPI aligné climat comme cas paradigmatique où F8 trouve une application directe. Cette méthode quantifie en creux une dette envers les capitaux naturels — chiffrable, programmée, mais extra-comptable dans le régime PCP actuel. F8 permet de l'inscrire comme D NH naturelle au passif CARE de la collectivité, miroir d'une C NH à l'actif. Le mouvement type est e (A↑ / D↑). La traduction PCP reste ∅, ce qui déclenche signal\_translation\_manquante et alimente le débat sur l'évolution future du PCP — interface directe entre F8 et la jurisprudence comptable publique.** |

#### 8.14 Gouvernance de F8

Les arbitrages de conception de F8 — options retenues et arbitrages restant ouverts pour les versions ultérieures — sont consignés dans `MRC_v5.7/_ETAT_INSCRIPTION_v5.7.md` (annexe « Arbitrages F8 »), non dans le corps de la fiche.

 **Recommandation transversale pour la diffusion : F8 est conçue pour être lisible par un comptable, un financeur, un gestionnaire de bassin ou un juriste non spécialiste de la théorie des catégories. Trois entrées de lecture sont possibles selon le profil : (a) entrée praticien comptable — commencer par § 8.3 (table des seize mouvements), puis § 8.4 (traductions par régime) ; (b) entrée gestionnaire de communs — commencer par § 8.6 (comptabilité CARE) et § 8.7 (priorité créanciers) ; (c) entrée juriste — commencer par § 8.13 (interface droit comptable) puis § 8.9 (signaux). Le tableau de l'exemple intégré (§ 8.12) sert de boussole pour toutes les entrées.**

— Fin de la Fiche F8 —

### Fiche F5 — Mode psychologie proximate / attracteurs cognitifs

Localisation : Couche 2 — fiche opérationnelle. *(Champs repris de NT-G1 §3.1-3.2.)*

**F5.1 Objet.** Réinstancie les attracteurs cognitifs durables, la distinction proximate/ultimate et la résistance à la révision → NT-G1. Engagement : **AX-12** (attracteurs cognitifs ; famille 5 — cadre importé ; *valable sous conditions déclarées*) ; l'étiquette « EEA » est écartée par le porteur (Annexe §A.15.0 ; NT-G1).

**F5.2 Champs nommés réintégrés** — Sous-couche C-PSYCHOLOGIE-PROXIMATE

| **Champ** | **Type** | **Valeurs / Exemples** | **Description** |
| --- | --- | --- | --- |
| système\_cognitif\_implique | Énumération | SYSTEME\_1 / SYSTEME\_2 / DUAL / SOCIO-MORAL | Système cognitif mobilisé (→ NT-G1) |
| niveau\_explication | Énumération | PROXIMATE / ULTIMATE / DUAL | Niveau d'explication (Tinbergen 1963) |
| attracteur\_culturel | Texte libre | réciprocité, hiérarchie, rituel sacrificiel | Attracteur cognitif en jeu (Boyer, Sperber) |
| résistance\_cognitive\_révision | Énumération | FAIBLE / FORTE / BLOQUANTE | Résistance à la révision des règles |
| profondeur\_évolutive | **SUSPENDU** | — | Voir NT-G1 : aucune source du corpus ne permet de dater l'apparition d'une disposition |
| praticabilite\_cognitive | Énumération | PRATICABLE / PARTIELLEMENT / IMPRATICABLE | Adéquation cognitive |
| modificateur\_affectif | Réel \[-1,1\] | impact sur `seuildisposition` (F1, C-GENRE-METIER) | Reçu de G-AFFECTIF (→ NT-G9) |
| signalversaffectif | Booléen + origine | VRAI si `résistance_cognitive_révision` = FORTE ou BLOQUANTE ; origine déclarée par `source_asymetrie_pouvoir` (ATTRACTEUR-COGNITIF / POSITIONNELLE-SOCIALE, NT-G7) | Sortie vers G-AFFECTIF : alimente `ideologiedefensivedetectee` (F1). **Ne relit pas `seuildisposition`** : condition de terminaison du couplage (PR-9, `un_canal_qui_ne_relit_pas_le_seuil_termine`) |

**F5.3 Signaux et règles** (→ NT-G1 §3.2) : **R-ATTRACTEUR** (`coincidence_attracteur=VRAI ET effet_coincidence=PIEGE` → C-SIGNAL `PIEGE_ATTRACTEUR`) ; **RESISTANCE\_COGNITIVE\_FORTE** (`résistance_cognitive_révision=FORTE/BLOQUANTE` → phase ENQUETE) ; **ATTRACTEUR\_SANS\_ACTION** (A1). Porteur de R-ATTRACTEUR : `ACTEUR_PRESTIGE_BIAS` (A3, Henrich 2015). Phase de traitement : `REVISION_PROXIMATE_ULTIMATE`.

**F5.4 Couplage avec G-AFFECTIF.** Le canal de retour vers G-AFFECTIF est instrumenté par `signalversaffectif`. Les deux sens forment un **cycle** ; les deux ordres de propagation diffèrent (`les_deux_ordres_different`, PR-9) : ce qui est exigé est la **terminaison**, non la commutation — elle tient parce que `signalversaffectif` ne relit pas le seuil qu'écrit l'autre sens (`un_canal_qui_ne_relit_pas_le_seuil_termine` ; lecture, témoin : `un_canal_qui_relit_le_seuil_ne_termine_pas`). `[RÉSERVE]` PR-9 nomme « E→A » le canal qui écrit `seuildisposition`, que NT-G9 appelle A→E : la correspondance des étiquettes est déclarée en NT-G9 §10.2. La valeur seuil de `signalversaffectif` (FORTE ou BLOQUANTE) est une décision d'instrumentation, révisable. Le discriminant `source_asymetrie_pouvoir = ATTRACTEUR-COGNITIF` (W-14b) route vers cette face.

— Fin de la Fiche F5 —

### Fiche F6 — Mode justice / droits

Localisation : Couche 2 — fiche opérationnelle. *(Champs repris de NT-G7 §3.1 et NT-G6 §3.1. Embarque le versement NT-G7 de Fournier.)*

**F6.1 Objet.** Réinstancie les capabilités plancher, les injustices épistémiques, la parité de participation et le pouvoir → NT-G7 ; les faisceaux de droits et l'écart formel/réel → NT-G6.

**F6.2 Champs nommés réintégrés** — Sous-couche C-CAPABILITES / C-POUVOIR (→ NT-G7)

| **Champ** | **Type** | **Valeurs / Exemples** | **Description** |
| --- | --- | --- | --- |
| capabilite\_individuelle | Énumération | santé, affiliation, sens… | **Nussbaum 2000**, liste p. 76-78 |
| habitabilite\_systemique | Énumération | HABITABILITE\_PRODUCTIVE / INTEGRITE\_ECOSYSTEMIQUE | **Morizot & Neyret 2026 ; Schlosberg 2007** — *non Nussbaum* |
| niveau\_injustice\_épistémique | Énumération composée | type : TESTIMONIALE / HERMENEUTIQUE / ABSENTE ; portee : SYSTEMATIQUE / LOCALE / NON\_DECLARE ; persistance : EPISODIQUE / STRUCTURELLE / NON\_DECLARE ; intensite 0-5 *(sans repères — `[LACUNE]`, NT-G7)* | Injustice épistémique (→ NT-G7). Déclarée par le **documentant** de l'injustice, jamais par qui qualifie le régime affectif. Le canal vers G-AFFECTIF lit le type, la portée et la persistance, jamais l'intensité. `portee` est distinct de `type_asymetrie` (asymétrie de pouvoir, C-POUVOIR) |
| source\_dynamique\_souffrance | Énumération | DOCUMENTATION\_INDEPENDANTE / ISSUE\_DE\_LA\_SOUFFRANCE | Une injustice dont la seule documentation est le signal de souffrance venu de G-AFFECTIF ne passe pas vers G-AFFECTIF (**CONV-19**) |
| hypothese\_injustice\_vers\_affectif | Sortie | type, portée, persistance, DID du documentant ; statut fixe HYPOTHESE | Émise par **R-HYPOTHESE-INJUSTICE** ; reçue en F1 (C-GENRE-METIER). **N'est jamais une qualification** (CONV-20 : F6 n'est pas une source de qualification) |
| précondition\_herméneutique\_satisfaite | Booléen | VRAI / FAUX | **Garde bloquante** : FAUX bloque DÉLIBÉRATION et `REDEFINITION-BUTS` |
| type\_injustice | Énumération | DISTRIBUTIVE / RECONNAISSANCE / REPRESENTATION / EPISTEMIQUE | Fraser, Fricker |
| type\_asymetrie | Énumération | LOCALE / SYSTEMATIQUE / SPATIALE-PLANETAIRE | Traçage des asymétries |
| parite\_participation | Booléen | VRAI / FAUX | FAUX bloque la délibération (Fraser) |
| violence\_symbolique | Booléen + Texte | `mecanisme` (méconnaissance/naturalisation/euphémisation) ; `intensite` 0-5 | C-POUVOIR (W-14, Bourdieu & Passeron 1970) |
| source\_asymetrie\_pouvoir | Énumération | ATTRACTEUR-COGNITIF (→ NT-G1) / POSITIONNELLE-SOCIALE (→ W-14) / INDETERMINEE (défaut) | Discriminant de routage (W-14b) |
| **regime\_du\_dispositif** | Énumération | EXPERIMENTATION / INFRASTRUCTURE / NON\_DECLARE (défaut) | **Régime du dispositif inscrit.** Commande l'applicabilité des critères d'accès aux droits (non-recours, sous-inclusion, exhaustivité réalisée) : ils ne sont applicables qu'au régime INFRASTRUCTURE, où les ayants droit sont définis par une norme opposable extérieure au dispositif. Hors de ce régime, le critère est refusé comme qualification et l'écriture reste inscrite — **E6**, `[CRITÈRE D'ACCÈS HORS INFRASTRUCTURE]` (Annexe §A.15.11). NON\_DECLARE ne vaut pas permission. **Champ de F6 seulement**, non primitive de Couche 0. Appui : PR-17 (`regime_du_dispositif_declare`, `nonDeclare_ne_vaut_pas_permission`). → NT-G7 §3.1bis |

Sous-couche C-DROITS (→ NT-G6)

| **Champ** | **Type** | **Valeurs / Exemples** | **Description** |
| --- | --- | --- | --- |
| droit\_acces / droit\_prélevément / droit\_gestion / droit\_exclusion / droit\_alienation | DID porteur | did:… | Cinq faisceaux Schlager-Ostrom 1992 |
| **droit\_ne\_pas\_etre\_exclu\_usage** | DID porteur + Booléen | did:… | **Contre-écriture R1 du `droit_exclusion`** — versement Fournier §2 (Holder & Flessas 2008). `[CHANGEMENT DE BASE TRACÉ ; source NON VÉRIFIÉE → W-6]` |
| *(aucun score de communalité)* | — | Pas d'agencement linéaire *« 1 (appropriable) à 5 (inaliénable) »* : le rapport source l'examine et l'écarte comme *« réducteur »* ; la communalité se déclare par les cinq champs ci-dessous. | Rochfeld, Cornu & Martin 2021, Section 3 |
| communalite\_interet\_commun | Qualification déclarée | Comment l'intérêt commun est identifié et garanti **en droit** sur cette chose. **Déclaré, jamais calculé.** | Rochfeld, Cornu & Martin 2021, p. 78 |
| communalite\_inclusivite | Qualification déclarée **par instance** : `inclusivite_attributaire`, `inclusivite_deliberative`, `inclusivite_controle` ∈ {FAIBLE, INTERMÉDIAIRE, FORTE, NON DÉCLARÉE} | Dans quelle mesure le pouvoir d'exclure est limité **en droit** — continuum exclusivité / inclusivité —, pour chaque instance tenue. **Déclaré, jamais calculé ; jamais agrégé entre instances.** Second sens de la séparabilité établi sur l'instance de contrôle (NT-G6 §2.1 ; PR-59, `l_inclusivite_du_controle_ne_determine_pas_l_interet_commun`, témoin `controle_temoin`) ; premier sens rapporté à l'instance attributaire (`le_premier_sens_porte_sur_l_attributaire`) ; instance délibérative sans témoin `[MODIFIÉ LE 13/10/2026 — décision n° 55]` | Rochfeld, Cornu & Martin 2021, p. 78 ; p. 332-333, 411 |
| communalite\_instance | Énumération multivalue | ATTRIBUTAIRE / DELIBERATIVE / CONTROLE — les trois instances où la communalité se manifeste | Rochfeld, Cornu & Martin 2021, §2 |
| prescription\_etat | Qualification déclarée | **Le plan vertical** : ce que l'État prescrit sur cette chose, indépendamment du régime de propriété. **Déclaré, jamais calculé.** | Rochfeld, Cornu & Martin 2021, §2 |
| nature\_prerogative | Énumération multivalue | DROIT\_SUBJECTIF / UTILITE\_PUBLIQUE / INTERET\_DIFFUS — **la communalité ne passe pas toujours par un droit**. **Champ pivot du pont F6 ↔ F8 : voir §8.5.6** | Rochfeld, Cornu & Martin 2021, §2.1 |
| **porteur\_instance**  | Couple (instance, porteur nommé) | ATTRIBUTAIRE → … ; DELIBERATIVE → … ; CONTROLE → … | **Qui tient chaque instance déclarée en `communalite_instance`.** §8.5.6.4 rend la déclaration des instances DELIBERATIVE et CONTROLE obligatoire pour toute chose inscrite comme commun **sans dire qui a qualité** ; ce champ le nomme. Formes instituées admises — voir l'encadré ci-dessous |
| **forme\_affectation**  | Énumération | FIDUCIE / ORE / ORIC / AUCUNE | **Forme d'affectation volontaire au titre de laquelle la chose est inscrite comme commun.** AUCUNE : inscription par `E+ ↔ ∅` ou par une propriété collective ordinaire. Conditions d'écriture : §8.5.6.2bis |
| **statut\_juridique\_forme**  | Énumération | DROIT\_POSITIF / **DE\_LEGE\_FERENDA** | **DE\_LEGE\_FERENDA obligatoire pour l'ORIC**, proposition de réforme non adoptée. **Une inscription `DE_LEGE_FERENDA` n'est jamais présentée comme opposable** (§8.5.6.2bis) |
| ecart\_formel\_réel | Mesure déclarée **par droit** : `ecart_acces`, `ecart_prelevement`, `ecart_gestion`, `ecart_exclusion`, `ecart_alienation` | écart droits formels / exercés, droit par droit (Schlager & Ostrom 1992, p. 250-252) | Décalage inscriptible, rapporté à `terme_comparaison_ecart` (document de référence déclaré, Annexe §A.13) ; non instruit ≠ nul (marqueur `[ÉCART NON INSTRUIT]`) ; **aucun écart total** ; commun sans faisceau (`E+ ↔ ∅`) : marqueur `[SANS FAISCEAU]` `[MODIFIÉ LE 13/10/2026 — décision n° 54 ; PR-59 : `non_instruit_n_est_pas_nul`, `meme_ecart_total_droits_differents`, `sans_faisceau_pas_d_alerte`]` |
| seuil\_ecart | **Cinq valeurs** (un seuil par droit) + porteur + durée de cycle | déclaré par le commun, droit par droit ; porteur : l'instance délibérative (`porteur_instance`) | Alerte (phase ENQUÊTE + C-MEMOIRE-PERTES) si l'écart **d'un droit** atteint le seuil **de ce droit** sur deux cycles, l'alerte nommant le droit (PR-59, `un_cycle_ne_suffit_pas`) ; **sans seuil déclaré : marqueur `[SEUIL NON DÉCLARÉ]`, pas d'alerte** (patron PR-50 ; PR-59, `pas_d_alerte_sans_seuil_declare` ; aucun seuil universel, décision du porteur du 13/10/2026) |

> §8.5.6.4 rend obligatoire la déclaration des instances **DELIBERATIVE** et **CONTROLE** pour toute chose inscrite comme commun ; `porteur_instance` nomme qui a qualité. L'instruction de A5 établit que la société à mission institue un porteur pour deux de ces trois instances — **et pour la troisième, aucun.**
>
> | Instance | Forme instituée admise | Nature | Périodicité |
> | :-- | :-- | :-- | :-- |
> | **ATTRIBUTAIRE** | **Bénéficiaires d'une fiducie** (C. civ. art. 2018, 4°) ; **créancier d'une ORE**, si un accès ou un usage est stipulé ; **créancier d'une ORIC** (`DE_LEGE_FERENDA`) — conditions d'écriture en §8.5.6.2bis. **À défaut**, le porteur est le consortium de gouvernance déclaré (Annexe H §H.1), qui n'est pas un statut légal | contractuelle | durée du contrat |
> | **DELIBERATIVE** | **comité de mission** d'une société à mission (C. com. art. L. 210-10, 3°) — distinct des organes sociaux, **comportant au moins un salarié**, rapport joint au rapport de gestion | interne | **annuelle** |
> | **CONTROLE** | **organisme tiers indépendant accrédité COFRAC** (C. com. art. R. 210-21 ; arrêté du 27 mai 2021) — avis **publié**, mission de six ans | externe | **bisannuelle**, trisannuelle sous 50 salariés |
>
> **Ce que ces formes apportent, et qui manque partout ailleurs dans le set : une condition de réfutation instituée.** En cas de non-respect des objectifs, **toute personne intéressée ou le ministère public** peut saisir le tribunal pour faire supprimer la mention de tous les documents de la société, le cas échéant sous astreinte. Ailleurs, la condition de réfutation est **auto-déclarée** — et §9bis reconnaît que les protections internes du registre ne valent que si un ordre juridique les reconnaît. **Ici, l'ordre juridique fournit la procédure et le standing élargi.** `[NUMÉRO D'ARTICLE À CONTRÔLER — L. 210-11 ou L. 210-12 ; texte primaire non lu, 403 Légifrance.]`
>
> **Ce que ces formes n'apportent pas.** Aucune ne tient l'instance **attributaire**, et c'est structurel : **les objectifs statutaires d'une société à mission ne sont dus à personne d'identifié.** En grammaire P-C-E-D-e-d, l'engagement d'une société à mission est un **`E+` dont le miroir est `∅`** — l'asymétrie existentielle de §8.5.2, non un `D+` appariant un `C+`. **La société à mission institue le contrôle d'un engagement dont elle n'institue pas le créancier.** Conséquence versée en §8.6 : **l'OTI n'est pas titulaire admis de `consentement_inscription_NH`.**
>
> `[LISTE NON EXHAUSTIVE, ET DÉCLARÉE TELLE — aucune recherche systématique du droit des sociétés n'a été conduite. Fonds de dotation et SCIC ne sont pas examinés et pourraient offrir d'autres formes instituées.]`
>
> **Fiducie et ORE sont instruites** sur le rapport source (P2, T1, §4, p. 275-315). **La fiducie institue un attributaire** — bénéficiaires, ou règles de désignation (C. civ. art. 2018, 4°) — et un contrôle (art. 2017, 2027). **L'ORE institue un créancier** (C. env. art. L. 132-3), qui tient d'abord le contrôle. **Les deux s'écrivent `D+ ↔ C+`, non `E+ ↔ ∅`** : leurs conditions d'admission, dont le critère de divisibilité sur `D+ ↔ C+`, sont fixées en §8.5.6.2bis. Fonds de dotation et SCIC : **non examinés** (absents du rapport). `[DROIT EN VIGUEUR NON VÉRIFIÉ — rapport d'avril 2021.]`

**F6.3 Signaux et règles** (→ NT-G7 §3.2, NT-G6) : **R-HERMENEUTIQUE** (précondition formelle bloquante ; **garde de `REDEFINITION-BUTS`**) ; **R-CAPABILITES** ; **R-POUVOIR** ; **R-VIOLENCE-SYMBOLIQUE** (contre-écriture obligatoire, W-14) ; **R-PLANETAIRE** (AM-G7-08) ; **R-HYPOTHESE-INJUSTICE** (canal G-JUSTICE → G-AFFECTIF) : une injustice passe vers G-AFFECTIF, comme hypothèse, si son type est TESTIMONIALE ou HERMENEUTIQUE, si elle n'est pas **déclarée** à la fois LOCALE et EPISODIQUE (filtre « ou » : SYSTEMATIQUE ou STRUCTURELLE), si `source_dynamique_souffrance` = DOCUMENTATION\_INDEPENDANTE et si son documentant est désigné ; une portée ou une persistance NON\_DECLARE passe, avec le marqueur `[PORTÉE NON DÉCLARÉE]` (E5) ; une injustice issue de la seule souffrance ne passe pas (E6). Forme : PR-53 (`le_filtre_n_ecarte_que_le_declare_incident`, `local_mais_structurel_passe`, `non_declare_passe_avec_marqueur`, `documentee_par_la_souffrance_ne_passe_pas` ; témoin `filtre_temoin_discriminant`). Règle de frontière : **R-PRIORITE-F6-F10** — **hébergée en NT-G10 §6.2** (frontière F6/F10 : F6 traité en précondition, F10 reprend) ; **F6 y participe sans la porter** (NT-G7 ne la mentionne qu'en renvoi, cf. R-VIOLENCE-SYMBOLIQUE).

**F6.4 Câblage du versement Fournier (NT-G7) — durci.** Note de versement §2 : (1) `droit_ne_pas_etre_exclu_usage` inscrit comme contre-écriture R1 du `droit_exclusion` (lève un `[ENGAGEMENT SANS SYMÉTRIE]`) ; (2) `précondition_herméneutique_satisfaite = FAUX` / `R-HERMENEUTIQUE` confirmée comme **garde générale** de `REDEFINITION-BUTS`.

— Fin de la Fiche F6 —

### Fiche F7 — Mode mimétique / victime / méconnaissance

Localisation : Couche 2 — fiche opérationnelle. *(Champs repris de NT-G8 §3.1-3.2.)*

**F7.1 Objet.** Réinstancie la crise mimétique, le mécanisme victimaire et la méconnaissance fondatrice → NT-G8, **comme grille d'interprétation, non comme cadre causal (AX-13)** : les champs de la fiche qualifient une inscription, ils ne l'expliquent pas.

**F7.2 Champs nommés réintégrés** — Sous-couches C-MIMETISME / C-VICTIME / C-MECONNAISSANCE

| **Champ** | **Type** | **Valeurs / Exemples** | **Description** |
| --- | --- | --- | --- |
| médiation\_type | Énumération | EXTERNE / INTERNE / RIVALITE\_ACTIVE / INDIFFERENCIATION | Type de médiation mimétique (Girard) |
| sujet\_acteur\_DID / modèle\_médiateur\_DID | DID | did:… | Sujet du désir / modèle imité |
| intensite\_rivalite | Score 1-5 | 1 (faible) à 5 (paroxystique) | Intensité de la rivalité |
| distance\_catégorielle | Score 1-5 | 5 = indifférenciés | Distance subsistante sujet/modèle |
| focalisation\_victimaire | Booléen | VRAI / FAUX | Bascule attentionnelle vers un acteur unique |
| victime\_identifiee\_DID | DID | did:… | Acteur désigné bouc émissaire |
| voix\_victime\_inscrite | Booléen | VRAI / FAUX | Contre-récit de la victime inscrit |
| meconnaissance\_fondatrice | Booléen | VRAI / FAUX | Institution fondée sur résolution victimaire |
| narratif\_legitimateur | Texte | récit sacralisant | Masque la violence fondatrice |
| autocritique | Booléen | VRAI / FAUX | G-MIMETIQUE elle-même soumise à R-MECONNAISSANCE |
| principe\_precaution\_asymetrique | Booléen | VRAI / FAUX | Précaution ciblant l'acteur exclu (A5) |

**F7.3 Signaux et règles** (→ NT-G8 §3.2) : **R-CRISE-MIMETIQUE** (infra-Couche-1, canal distinct) ; **R-VICTIME-EMISSAIRE** ; **R-MECONNAISSANCE** ; signaux `focalisation_victimaire`, `meconnaissance_fondatrice`.

**R-CARE-SACRIFICIEL** (couplage G-MIMETIQUE → G-SOIN, médié par G-AFFECTIF ; → NT-G9 §10.3, NT-G3) — *formulation minimale*. **Déclenchement** : sur un même cycle et dans un même collectif, `piegereconnaissancesuspecte` = VRAI (F1, R-PIEGE-RECONNAISSANCE) **et** `focalisation_victimaire` = VRAI (F7), lu selon la grille d'AX-13. **Effets** : signal R-CARE-SACRIFICIEL en C-SIGNAL, niveau ÉLEVÉ ; inscription en C-MEMOIRE-PERTES ; activation de R-VICTIME-EMISSAIRE ; **précondition bloquante** à toute `REDEFINITION_BUTS` en C-DPQT tant que le porteur n'est pas désigné et sa charge redistribuée. **Porteur** : l'acteur, humain ou non, qui concentre soin et désignation victimaire ; **horizon** : au moins deux cycles d'activation conjointe ; **critère** : dissociation entre reconnaissance formelle du porteur et non-inscription de sa charge réelle.

**F7.4 Connexions et réserve.** → F6 (M→J : `R-VICTIME-EMISSAIRE` = forme extrême d'injustice testimoniale) ; ↔ F5 (E↔M : attracteur rituel/sacrificiel). Le routage `source_asymetrie_pouvoir` côté NT-G8 (W-14c item 4) est **`[NON VÉRIFIÉ]` — à NE PAS brancher** avant W-6 + Vague C.

— Fin de la Fiche F7 —

### Fiche F9/F10 — Mode démocratie épistémique / formalisme délibératif

Localisation : Couche 2 — fiche opérationnelle Démocratie épistémique. *(Champs repris de NT-G10 ; renvois « → NT-Gx » appliqués.)*

**F9-F10.1 Objet et fondements théoriques**

La Fiche réinstancie en Couche 2 la **gouvernance procédurale de la délibération** : qualité d'enquête, formes légitimes de parole, détection des concentrations épistémiques, représentation des absents, et **point d'arrêt délibératif**. Fondements : qualité épistémique de l'enquête, formalisme délibératif, épistocratie, représentation descriptive, priorité de traitement → NT-G10 ; frontière justice/procédure (précondition herméneutique, parité de participation) → NT-G7 (F6) ; réflexivité des instruments (règle `R-REFLEXIVITE-INSTRUMENT` **hébergée en NT-G10** ; fondement performatif → NT-G4) ; contrainte jonasienne sur horizon irréversible → NT-G2.

**F9-F10.2 Champs nommés réintégrés**

Sous-couche C-ENQUETE-DEMO (Qualité épistémique du processus)

| **Champ** | **Type** | **Valeurs / Exemples** | **Description** |
| --- | --- | --- | --- |
| methodeexplicite | Booléen | VRAI / FAUX | Critère *méthode* : procédures explicites et réfutables |
| pluralismeactif | Score 1-5 | 1 (mono-source) à 5 (diversité forte) | Critère *pluralisme* : diversité des sources et des cadres |
| reflexiviteregistre | Booléen | VRAI / FAUX | Critère *réflexivité* : les instruments sont eux-mêmes interrogés (→ R-REFLEXIVITE-INSTRUMENT) |
| utilitetransformative | Booléen | VRAI / FAUX | Critère *utilité* : la connaissance transforme la situation |
| typevalidation | Énumération | … / LLM-SEUL | Mode de validation de l'écriture ; `LLM-SEUL` déclenche `llmvalidationseule` |
| qualiteenquete | Énumération | SATISFAISANTE / INSUFFISANTE / BLOQUEE | État synthétique de la qualité d'enquête (→ NT-G10 §4) |
| sujetsepistemiqueslegitimes | Liste DIDs | \[DID…\] | Sujets épistémiques légitimes de la délibération (Annexe H.1) |
| sujetsepistemiquesabsents | Liste DIDs | \[DID…\] | Absents de la production du sens ; tracés, non masqués |
| absencestructurelle | Booléen | VRAI / FAUX (justifié) | VRAI si les absents ne peuvent par nature être rendus présents (générations futures, milieux, défunts). Justifié, non déclaré |
| mecanismesubstitution | Texte | tirage, mandat fiduciaire intergénérationnel, tiers-garant écologique | Dispositif par lequel un collectif présent représente les absents |
| porteurrepresentationabsents | DID acteur | did:… | Porteur habilité des intérêts des absents (→ sujetjugelegitimevalider) |
| contraintejonasienne | Texte / critère | précaution, priorité au pronostic catastrophique | Critère jonasien d'asymétrie en faveur de la non-dégradation irréversible (→ NT-G2) |

Sous-couche C-FORMES-DELIBERATION (Formes légitimes de prise de parole)

| **Champ** | **Type** | **Valeurs / Exemples** | **Description** |
| --- | --- | --- | --- |
| formesdelibacceptees | Liste énumérée | ARGUMENT / RECIT / RHETORIQUE / GESTE / IMAGE | Formes de parole déclarées admises dans la phase DELIBERATION (Young via Ferey) |
| formalismedeliberatif | Booléen (+ signal) | VRAI / FAUX | Un formalisme filtrant les voix est-il actif ? Bloque le passage en CONVENTION (voir F9-F10.3) |

Sous-couche C-EPISTOCRATIE (Concentrations épistémiques)

| **Champ** | **Type** | **Valeurs / Exemples** | **Description** |
| --- | --- | --- | --- |
| pathologieepistemique | Énumération | PARESSE / FERMETURE / ARROGANCE | Type de pathologie épistémique des dominants (Medina via Ferey) |
| risqueepistocratie | Score 1-5 | 1 (faible) à 5 (élevé) | Risque de concentration épistémique |

Sous-couches C-JUSTIFICATION-DEMO et C-REPRESENTATION-DESCRIPTIVE (compactées) : `typejustificationdeclare`, `critererefutation`, `sujetjugelegitimevalider` (positionnement normatif du registre) ; `representationdescriptive`, `avantageepistemiqueactive`, `modeslectionrepresentants` (représentation des groupes affectés — complète `identiteslegitimes`/C-DROITS sans la dupliquer). Détail → NT-G10 §3.1.

**F9-F10.3 Connexions C-SIGNAL et règles activées**

| **Signal C-SIGNAL** | **Condition de déclenchement** | **Niveau / Action** |
| --- | --- | --- |
| enqueteinsatisfaisante | qualiteenquete = INSUFFISANTE ou BLOQUEE | MOYEN — ouvrir ENQUETECOLLECTIVE + inviter les absents |
| risqueepistocratieeleve | risqueepistocratie ≥ 4 | ÉLEVÉ — déclencher R-EPISTOCRATIE (suspension + invitation) |
| llmvalidationseule | typevalidation = LLM-SEUL ET statut ≠ proposition\_non\_validee | ÉLEVÉ — **invalider l'écriture, remise en DELIBERATION** (point d'arrêt vs automatisation) |
| formalismedeliberatif | formalismedeliberatif ET injustice TESTIMONIALE | MOYEN-ÉLEVÉ — ENQUETECOLLECTIVE + ouverture des formes de parole |

Règles activées (→ NT-G10 §3.2, §6.2) : **R-FORMES-DELIBERATION** (si `formalismedeliberatif = VRAI`, **pas de passage DELIBERATION→CONVENTION** sans nouvelle phase ENQUETE incluant les acteurs marginalisés) ; **R-EPISTOCRATIE** ; **R-REFLEXIVITE-INSTRUMENT** (toute modification d'instrument/catégorie de base déclenche RÉVISIONCONCEPTUELLE, interdit le `[CHANGEMENT DE BASE NON TRACÉ]`) ; **R-PRIORITE-F6-F10** (F6 traité en précondition, F10 reprend ensuite — ordre, non veto) ; procédure **DEBLOCAGE-MOTIVE-EXISTENTIEL** (verrou K5, absence structurelle).

Point d'arrêt délibératif (transitions C-ENQUETE-V5) : `ENQUETE→DELIBERATION` si `qualiteenquete ≠ BLOQUEE` ; `DELIBERATION→CONVENTION` **seulement si** `formalismedeliberatif = FAUX`. Aucune conclusion par exécution automatique : une validation `LLM-SEUL` est invalidée et remise en DELIBERATION.

**F9-F10.4 Connexions inter-fiches**

| Vers | Interface |
| --- | --- |
| → F6 (Justice, NT-G7) | `R-PRIORITE-F6-F10` (précondition herméneutique/capabilités avant certification du processus) ; `parité` de participation ; frontière F6/F10 (NT-G10 §6.2) |
| → F4 (Responsabilité, NT-G2) | `contraintejonasienne`, `DEBLOCAGE-MOTIVE-EXISTENTIEL` pour `horizon = IRREVERSIBLE` |
| → F8 (Comptable) | seules les écritures dont `typevalidation ≠ LLM-SEUL` (ou revalidées) sont inscriptibles |

**F9-F10.5 Câblage du versement Fournier (`REDEFINITION-BUTS`) — durci.** L'exigence de gouvernance procédurale de l'acte de redéfinition des buts (versement Fournier — décision du porteur) se branche ici sur des champs nommés : (1) **parité délibérative** → `parité` (F6) + frontière F6/F10 + `sujetsepistemiqueslegitimes` ; (2) **point d'arrêt vs automatisation** → garde `DELIBERATION→CONVENTION` (`formalismedeliberatif = FAUX`) + signal `llmvalidationseule` ; (3) **co-activation F6/F10** → `R-PRIORITE-F6-F10`. Le versement NT-G10 a donc le statut d'**invariant durci**.

— Fin de la Fiche F9/F10 —

— Fin des fiches de Couche 2. —

*Les sources académiques externes du corps des fiches sont remplacées par des renvois « → NT-Gx » (grammaire d'accueil) ou « → Annexe méthodologique ». Les noms de sous-couches (C-DPQT, C-MURRAY…) sont conservés. La bibliographie complète vit dans les notes de grammaire correspondantes.*

## §B.4 Note de vulgarisation - NT-ARCH couche 2 pour le site-vitrine du MRC

### Comment lire la Partie B (Fiches F1–F10)

La Partie A posait la « grammaire de base » du MRC : primitives de Couche 0, régime d’obligation, statut de dette et machine d’états de Couche 1. La Partie B ne rajoute pas des principes, elle montre comment ces invariants se concrètent dans des instruments et des champs utilisables par un collectif.

#### Des « fiches » plutôt que des théories.
Chaque fiche (F1 à F10) décrit un mode d’application : un type d’instrument, une manière d’enquêter, un dispositif comptable, un protocole de délibération… La fiche ne rajoute pas une nouvelle philosophie derrière le MRC, elle décrit : « si un collectif veut faire X (soin, justice, comptabilité, démocratie épistémique…), voilà les champs à remplir, les signaux à surveiller, les verrous à respecter ».

#### Une fiche ne redéfinit jamais les invariants.
Les règles fortes (R1 DÉBIT/CRÉDIT, statut de dette, machine d’états, distinction ACTORIEL / SYSTEMIQUE / HYBRIDE, etc.) vivent en Partie A ; les fiches de Partie B y renvoient explicitement. Si une fiche se mettait à « réinterpréter » R1 ou C-STATUT-DETTE, ce serait un [CHANGEMENT DE BASE NON TRACÉ]. Les fiches ont donc un rôle d’interface : elles organisent l’usage local d’invariants déjà décidés, au lieu de les modifier silencieusement.

Une fiche = un champ d’usage privilégié, pas un silo.
F1 (soin), F4 (responsabilité), F6 (justice/communalité), F8 (comptable), F9–F10 (démocratie épistémique) sont écrites à partir de situations particulières (prendre soin, rendre des comptes, certifier un processus, etc.), mais elles ne sont pas des « modules indépendants ». Elles sont câblées les unes aux autres : par exemple, F8 ne peut pas inscrire une écriture validée « LLM-SEUL » (renvoi à F9–F10), et F6 doit être activée avant la certification finale d’un processus (priorité F6/F10). Cette circulation est explicitement décrite dans les sous-sections « connexions » de chaque fiche.

#### Couplage avec les grammaires (Partie C).
La Partie B ne porte pas la bibliographie académique : dès qu’une fiche engage un argument théorique (justice, responsabilité, évolutivité, etc.), elle renvoie à la note de grammaire correspondante (NT-G1 → NT-G12). Concrètement : si une fiche F6 parle de « capabilités » ou de « parité de participation », les références sont dans NT-G7 ; si F8 manipule l’équation du bilan ou les seize mouvements comptables, les sources sont dans NT-G12. Cela évite que les fiches deviennent des mini-traités et maintient une séparation claire entre outils et théorie.

#### Comment s’en servir concrètement ?
Pour un collectif qui découvre le MRC, la Partie B peut se lire comme une boîte à outils : on ne commence pas forcément par tout, mais par la fiche qui correspond au problème du moment (par exemple F1/F3 pour un conflit de soin, F4/F6 pour une controverse sur la responsabilité, F8 pour rendre visibles certaines dettes, F9–F10 pour sécuriser un processus de décision). Chaque fois, la fiche renvoie vers la Partie A pour les règles structurelles, et vers la Partie C pour les justifications normatives et les conditions de réfutation.

#### Garde-fous contre deux dérives.
La Partie B est écrite pour éviter deux glissements fréquents :
– que des instruments soient pris pour des « vérités » (par exemple, une grille d’enquête ou un score qui s’imposerait sans discussion) ;
– qu’une innovation locale (un nouveau champ, un nouveau signal) modifie en douce un invariant de Couche 1.
C’est pour cela qu’on trouve, dans les fiches, des champs de réflexivité (par exemple R-REFLEXIVITE-INSTRUMENT, DEBLOCAGE-MOTIVE-EXISTENTIEL, signaux comme llmvalidationseule) : ils rappellent que toute évolution d’instrument doit passer par une délibération tracée et, le cas échéant, par une révision formelle dans l’Annexe méthodologique.

#### Articulation avec la gouvernance du set.
Enfin, la Partie B est écrite en cohérence avec les verrous de gouvernance du set (index D.1, règles D.2, traçage D.3). Aucune fiche ne peut, à elle seule, créer une nouvelle grammaire, ajouter un invariant de Couche 1 ou modifier l’architecture des couches. Si un usage répété montre qu’un même type de situation revient et ne rentre dans aucune grammaire existante, cela déclenche un chantier explicite : enquête (F9), passage par l’Annexe méthodologique, puis éventuelle création d’une nouvelle grammaire NT-Gx avec décision tracée du porteur.

En résumé, la Partie A répond à « de quoi est faite la charpente du MRC ? », la Partie B à « quels outils concrets sont disponibles, et comment les brancher sans briser la charpente ? », et la Partie C à « comment ces outils s’inscrivent dans des régimes normatifs et des bibliographies explicites ? ». Lire les trois ensemble permet d’éviter à la fois les raisonnements autoréférentiels et les changements de base non tracés.

### Résumé de chaque fiche

#### F1 – Prendre soin des situations

F1 décrit comment un collectif peut documenter une situation de soin (personnes, milieux, activités) sans la réduire à un simple problème de coûts. Elle propose des champs pour décrire les acteurs concernés, les vulnérabilités, les gestes de soin déjà présents ou manquants, et les conflits possibles avec d’autres obligations (par exemple économiques ou juridiques). Elle sert de porte d’entrée pratique pour la grammaire du soin (NT-G3) et prépare le terrain aux fiches plus spécialisées (travail, mésologie, etc.).

#### F2 – Milieux, territoires, mésologie

F2 organise la description des milieux et des territoires : quelles ressources sont en jeu, quels attachements, quels effets à long terme sur l’habitabilité. Elle permet de rendre visibles des contraintes souvent implicites (par exemple sur une nappe phréatique ou un sol) et de les relier à des décisions concrètes, en renvoyant à la grammaire de mésologie (NT-G5).

#### F3 – Conflits et épreuves

F3 sert à décrire une controverse ou un conflit : qui est en désaccord, sur quoi, et avec quels arguments ou expériences à l’appui. Elle ne tranche pas le conflit mais donne une structure commune pour le décrire, en distinguant les registres (juridique, économique, expérientiel, etc.) et en préparant le passage vers des dispositifs d’enquête ou de délibération plus structurés (F9–F10).

#### F4 – Responsabilité et porteurs d’obligation

F4 applique le régime d’obligation de la Partie A à des cas concrets : à qui, exactement, impute-t-on telle obligation, sur quel horizon, et avec quel degré d’incertitude. Elle aide à distinguer ce qui relève d’un porteur identifié (ACTORIEL) de ce qui reste systémique ou hybride, et à tracer quand une obligation doit remonter vers des acteurs collectifs (institutions, filières, etc.). C’est la fiche qui rend opérationnel le couple « régime d’obligation / C-STATUT-DETTE » en contexte.

#### F5 – Travail sur les instruments et scénarios

F5 porte sur le « travail sur les instruments » : comment un collectif modifie, teste ou combine des instruments (indicateurs, grilles, scénarios) sans faire de ces changements de simples bricolages invisibles. Elle prévoit des champs de réflexivité pour documenter pourquoi un instrument a été ajusté, ce que cela change pour les personnes concernées, et quand une modification doit déclencher une révision plus formelle (Annexe méthodologique, NT-G1).

#### F6 – Justice, communalité, capabilités

F6 est la fiche qui porte les critères de justice et de communalité : qui a réellement accès à quoi, avec quelles capabilités, et selon quels critères de répartition. Elle se branche sur NT-G6 (communalité) et NT-G7 (justice) et introduit notamment la question de la parité de participation : qui est à la table, qui ne l’est pas, et quelles conséquences pour la légitimité des décisions. F6 est explicitement en amont de la certification démocratique en F10 (règle de priorité F6/F10).

#### F7 – Dynamiques mimétiques et sacrifices

F7 décrit comment les dynamiques mimétiques (désir d’imitation, rivalités, boucs émissaires) traversent un collectif. Elle fournit des champs pour repérer les situations où certaines personnes ou groupes supportent systématiquement les coûts pour les autres (risque de « care sacrificiel »), en lien avec la grammaire mimétique (NT-G8) et les alertes sur les injustices répétées.

#### F8 – Comptabilité et valorimètres

F8 est la fiche comptable : elle implémente la règle R1 DÉBIT/CRÉDIT, l’équation du bilan et la typologie des seize mouvements, sans redéfinir ces invariants (qui vivent en Partie A et dans NT-G12). Elle décrit comment typage P-C-E-D-e-d, statut de dette et valorimètres sont combinés pour inscrire des écritures qui restent lisibles par différents régimes comptables (IFRS, PCG, CARE, etc.), via les sous-couches C-MOUVEMENT-TYPE.M et C-MOUVEMENT-TYPE.R. F8 intègre aussi les garde-fous procéduraux : impossibilité d’inscrire une écriture validée uniquement par un LLM, nécessité de respecter la machine d’états de la dette, etc.

#### F9 – Enquête et qualité de l’information

F9 organise la conduite d’une enquête collective : quels matériaux sont mobilisés, qui a été entendu, quelle est la qualité de l’enquête (suffisante, bloquée, biaisée). Elle comporte des signaux comme `enqueteinsatisfaisante` et `risqueepistocratieeleve` qui déclenchent des règles (R-EPISTOCRATIE, ENQUETECOLLECTIVE) lorsque certaines voix sont absentes ou marginalisées. F9 vise à rendre explicites les biais de la production d’information avant de passer à la délibération proprement dite.

#### F10 – Délibération, décision et certification

F10 complète F9 en portant sur les phases de délibération et de certification d’un processus décisionnel. Elle encode la machine d’états autour de la délibération (NONATTRIBUEE, EN_DELIBERATION, ATTRIBUEE, CRITIQUE, CONVENTION) et les champs comme `formalismedeliberatif`, `typejustificationdeclare`, `critererefutation`, `sujetjugelegitimevalider`. F10 contient les points d’arrêt forts : par exemple, aucune décision ne peut être certifiée si la délibération est filtrée par un formalisme qui exclut certaines voix, ou si la validation repose sur un « LLM-SEUL ».

### Comment NT‑ARCH fonctionne en mode descriptif (Couches 0 à 2) et en mode normatif (Couches 0 à 3)

#### Mode descriptif : « dire ce qui se passe » (Couches 0 à 2)

En mode descriptif, NT‑ARCH sert à décrire de manière rigoureuse ce qui se passe déjà dans un collectif, sans dire encore si c’est juste ou souhaitable. Les Couches 0, 1 et 2 sont alors utilisées comme un langage de description :

- La **Couche 0** fournit les primitives : types d’obligations (ACTORIEL / SYSTEMIQUE / HYBRIDE), notion de collectif hybride, etc. On s’en sert pour nommer les choses de manière stable (par exemple : « ici, on a une dette systémique non attribuée »).
- La **Couche 1** fournit les invariants de fonctionnement : R1 DÉBIT/CRÉDIT, statut de dette, machine d’états, conditions de passage par la délibération, etc. Ils permettent de décrire l’état actuel d’une obligation (en délibération, attribuée, critique…) sans encore juger si c’est acceptable.
- La **Couche 2** fournit des fiches d’usage (F1–F10) qui organisent cette description : on y renseigne les champs, on déclenche des signaux, on trace des liens vers d’autres fiches. On obtient ainsi une « coupe » décrite de la situation : qui est concerné, quelles dettes sont inscrites, où l’enquête est bloquée, etc.

En mode descriptif, le MRC se comporte donc d’abord comme un **langage d’inscription** : il oblige à préciser qui fait quoi, qui supporte quoi, ce qui a été vérifié ou pas. On peut déjà repérer des tensions (par exemple une dette systémique qui reste bloquée en NONATTRIBUEE) mais sans conclure encore sur la légitimité des arrangements.

#### Mode normatif : « dire ce qui devrait tenir » (Couches 0 à 3)

Le mode normatif apparaît dès qu’on passe de la simple description à des **engagements sur ce qui devrait être** : ce qui est légitime, ce qui est interdit, ce qui doit être révisé. La différence principale tient à l’activation explicite de la **Couche 3**, celle des grammaires NT‑G1 → NT‑G12 :

- Les grammaires (responsabilité, justice, soin, démocratie épistémique, etc.) disent **quel type d’obligation** est en jeu, avec quels porteurs, sur quel horizon (court terme, intergénérationnel, irréversible) et selon quels critères de vérification.
- Elles portent aussi la **bibliographie académique** et les **conditions de réfutation** : dans chaque NT‑G, une section précise comment contester la grammaire elle‑même ou l’usage qui en est fait, pour éviter les engagements sans symétrie.

En mode normatif, les fiches de Couche 2 ne sont plus seulement des lieux de description :

- **F6**, par exemple, ne se contente pas de décrire qui a accès à quoi ; elle dit aussi à quelles conditions un processus peut être considéré comme « juste », et active des signaux ou des règles si ces conditions sont violées (parité, capabilités).
- **F8** ne fait pas que tracer des écritures ; elle bloque certaines formes de validation (LLM seul, absence de passage par la délibération) et oblige à repasser par F9–F10.
- **F9–F10** transforment une enquête et une délibération en **processus gouverné** : il y a des points d’arrêt, des interdits (par exemple impossibilité de conclure si la délibération est filtrée par un formalisme excluant certaines voix), et des règles de priorité entre fiches (F6 avant F10).

Le mode normatif, c’est donc le même langage que le mode descriptif, mais **branché sur des grammaires qui disent ce qui est acceptable ou non**, avec des conséquences (signaux, verrous, révisions) quand ces critères ne sont pas respectés.

#### Pourquoi garder les deux modes séparés mais articulés ?

Séparer « décrire » et « prescrire » n’est pas un raffinement académique : c’est une manière de limiter les dérives.

- Si on ne garde que le descriptif (Couches 0–2), on peut très bien produire des registres extraordinairement précis… au service de régimes profondément injustes, ou d’automatisations incontrôlées.
- Si on ne garde que le normatif (Couche 3) sans description rigoureuse, on se contente de déclarations de principe impossibles à vérifier (« nous sommes responsables », « nous faisons de la justice climatique ») sans prise sur les inscriptions concrètes.

NT‑ARCH est construit pour que **les deux régimes circulent** :

- ce qui est dit normativement en Couche 3 doit pouvoir redescendre en Couche 2 sous forme de champs, de signaux, de règles de passage (sinon : [DÉCOUPLAGE DE RÉGIMES DÉTECTÉ]) ;
- ce qui est observé et inscrit en Couches 0–2 doit pouvoir remonter vers les grammaires pour ajuster le cadre (via NT‑G1, l’Annexe méthodologique, et les procédures de révision).

Autrement dit : en mode descriptif, NT‑ARCH dit **comment décrire** une situation de manière stable et traçable ; en mode normatif, il dit **quand et comment cette description peut (ou doit) être contestée**, corrigée ou complétée, au nom de grammaires explicites et réfutables.

---

# PARTIE C — Couche 3 : les douze grammaires transversales

## §C.1 Système des grammaires

Une grammaire qualifie normativement une interaction : elle dit *quelle* obligation est en jeu (responsabilité, justice, soin…), désigne porteurs, horizons et critères, et porte la bibliographie académique externe. Chaque note suit la même structure : cadre théorique, justification d'architecture, couplages bidirectionnels, position vis-à-vis des grammaires voisines, conditions de réfutation, inscription dans le régime de vérifiabilité-cohérence, bibliographie, note de vulgarisation.

| Note | Grammaire | Fiche(s) Couche 2 | Sources |
|---|---|---|---|
| NT-G1 | G-EVOLUTIVITE | F5 | → biblio NT-G1 |
| NT-G2 | G-RESPONSABILITE | F4 | → biblio NT-G2 |
| NT-G3 | G-SOIN | F1, F2 | → biblio NT-G3 |
| NT-G4 | G-PERFORMATIVITE | transversal | → biblio NT-G4 |
| NT-G5 | G-MESOLOGIE | F2 | → biblio NT-G5 |
| NT-G6 | G-COMMUNALITE | F6 | → biblio NT-G6 |
| NT-G7 | G-JUSTICE | F6 | → biblio NT-G7 |
| NT-G8 | G-MIMETIQUE | F7 | → biblio NT-G8 |
| NT-G9 | G-AFFECTIF | F1, F5, F7 | → biblio NT-G9 |
| NT-G10 | G-DEMOCRATIE-EPISTEMIQUE | F9, F10 | → biblio NT-G10 |
| NT-G11 | G-TRAVAIL | F1 | → biblio NT-G11 |
| NT-G12 | G-VALUATION | F8 | → biblio NT-G12 |

> Le rapport d'une grammaire à un corpus donné peut être déclaré au moyen de l'**attribut de lecture `statut_grammaire`** — STRUCTURANT / SECONDAIRE / INOPERANT / NON_INSTRUIT (valeur par défaut) — inscrit en **méthode** à l'Annexe méthodologique **§A.17**. C'est un attribut de **lecture**, non un champ de Couche 2 : il qualifie le rapport d'une grammaire à un cas, jamais une écriture. Il **ne modifie ni le compte des douze grammaires (→ §C.2), ni aucun invariant** : déclarer une grammaire `INOPERANT` est un acte de lecture, jamais de dispense.

## §C.2 Statut du « plafond de 12 » — discipline de gouvernance, non invariant d'architecture

Le set compte *actuellement* 12 grammaires, mais rien dans l'architecture des Couches 0–3 ne fixe ce nombre. Le « plafond » est un garde-fou prudentiel **révisable** contre la prolifération, pas une borne structurelle ; le poser comme invariant serait un \[CHANGEMENT DE BASE NON TRACÉ\]. Ce qui régit réellement l'admission d'une grammaire relève de **deux tests de Couche 0**, plus une décision de gouvernance :

1. *Règle de tri* (→ Annexe méthodologique §A) — une source est une grammaire ssi (a) elle pose un engagement normatif *réfutable* propre et (b) transversal à plusieurs interfaces ; sinon c'est une **méthode** (annexe, hors compte — ex. l'analyse formelle de concepts pour F3, → Annexe méthodologique §A.2). Ce sont les méthodes déguisées qui sont plafonnées, pas les grammaires.
2. *Non-réductibilité* — une grammaire n'est admise que si son périmètre n'est pas réductible à une grammaire existante (ex. NT-G11 : la capabilité au travail est une *spécialisation* de NT-G7, non un cas réductible — distinction déclarée pour éviter \[CHANGEMENT DE BASE NON TRACÉ\]).

Une 13e grammaire est donc admissible si elle passe ces deux tests et fait l'objet d'une **décision actée** du porteur. Le nombre courant (12) est un état, pas une contrainte.

## §C.3 Matrice des couplages bidirectionnels — état courant

Tout couplage doit tenir dans les deux sens, sinon \[DÉCOUPLAGE DE RÉGIMES DÉTECTÉ\]. Les chantiers ouverts sont rattachés aux Vagues de travail (→ Annexe méthodologique §D).

| Couplage | Sens | Statut |
|---|---|---|
| G-EVOLUTIVITE ↔ G-MIMETIQUE | E→M, M→E | Formalisé (OK) |
| G-EVOLUTIVITE ↔ G-JUSTICE | E→J, J→E | **LEVÉ SOUS CONDITION DE RÉVISION INSCRITE** — `VJE_carre_ne_commute_pas_sans_revision` + `VJE_ferme_apres_revision_externe` + `sensJE_ne_produit_pas_la_revision`. Le carré **ne se ferme pas de lui-même**. |
| G-EVOLUTIVITE ↔ G-AFFECTIF | E→A ; A→E | Instrumenté (F1 `seuildisposition`, F5 `modificateur_affectif` et `signalversaffectif`) ; **cycle, non commutatif** (PR-9, `les_deux_ordres_different`) ; terminaison exigée et satisfaite par construction (`un_canal_qui_ne_relit_pas_le_seuil_termine`) |
| G-AFFECTIF ↔ G-JUSTICE | A→J ; J→A | A→J : **indice explicatif seul** (CONV-19 ; F6 `source_dynamique_souffrance`) ; J→A : **instrumenté** (F6 R-HYPOTHESE-INJUSTICE → F1 `hypotheseinjusticependante`, règle d'ordre) ; cycle **qui termine** (PR-53, `le_cycle_AJ_termine`) |
| G-SOIN ↔ G-AFFECTIF | S→A, A→S | Formalisé (OK) |
| G-SOIN ↔ G-MIMETIQUE | S→M ok ; M→S | M→S inscrit en F7 (R-CARE-SACRIFICIEL, formulation minimale) ; formalisation complète en Vague C.3 |
| G-SOIN ↔ G-RESPONSABILITE | S→R, R→S | Formalisé (OK) |
| G-MESOLOGIE ↔ COMMUNALITE / RESP / SOIN | bidirectionnel | Formalisé (OK) |
| G-PERFORMATIVITE ↔ MIMETIQUE / JUSTICE | bidirectionnel | OK ; autoréférence résiduelle (Vague C.2) |
| G-MIMETIQUE ↔ G-RESPONSABILITE | R→M, M→R | Documenté NT-G8 ; commutation **réfutée** par PR-5 : le carré M↔R ne commute pas (`le_carre_MR_ne_commute_pas`) ; il se ferme par un acte (`le_carre_ferme_apres_l_acte`) |
| G-JUSTICE ↔ G-DEMOCRATIE-EPISTEMIQUE | F6/F10 | Règle de priorité de co-activation à acter (Vague C.5) |
| G-TRAVAIL ↔ G-SOIN / G-EVOLUTIVITE / G-JUSTICE / G-MIMETIQUE | cf. NT-G11 §4 | Tracés ; sens T→E à instrumenter |
| G-VALUATION ↔ G-PERFORMATIVITE | cf. NT-G12 | Tracé (gouvernance des valorimètres) |

---

# PARTIE D — Le set : index, règles de cohérence, lacunes

## §D.1 Index du set (17 fichiers et le fichier d'état)

| # | Fichier | Rôle |
|---|---|---|
| 1 | `MRC_v5.7_NT-ARCH_Architecture_Couches0-3.md` | **Ce fichier** — architecture complète : Couche 0 (primitives), Couche 1 (régimes et invariants), Couche 2 (fiches F1–F10), Couche 3 (système des grammaires) |
| 2–13 | `MRC_v5.7_NT-G1_Evolutivite.md` → `MRC_v5.7_NT-G12_Valuation.md` | Les douze grammaires de la Couche 3 — tout le cadre théorique et la bibliographie externe |
| 14 | `MRC_v5.7_Annexe_Methodologique.md` | Méthodes formelles non normatives, programme de preuve ProfReg, mécanisme de renvoi des sources, verrous bibliographiques, chantiers ouverts |
| 15 | `MRC_v5.7_ProfReg_Consolide.md` | État formel de référence de ProfReg |
| 16 | `MRC_v5.7_Annexe_H_Dataroom_augmentee.md` | Dataroom augmentée |
| 17 | `MRC_v5.7_Annexe_K_Cas_Chiffres.md` | Cas chiffrés |
| — | `_ETAT_INSCRIPTION_v5.7.md` | Fichier d'état : décisions, obligations ouvertes, registre des inscriptions, renvoi à l'historique |

## §D.2 Règles de cohérence du set

1. Le fichier Architecture ne cite aucune source académique externe : ses ancrages sont portés par les NT-G et reliés par renvoi — sans exception : l'ancrage de l'équation du bilan et de la typologie des seize mouvements vit en NT-G12.
2. Les NT-G1 → G12 portent toute la bibliographie académique externe ; chacune a une note de vulgarisation.
3. Aucune note ne contient d'action de révision : toutes vivent en Annexe méthodologique (§D).
4. Les fiches de Couche 2 ne portent pas de source externe : elles renvoient « → NT-Gx ».
5. Les méthodes formelles vivent dans l'annexe méthodologique, jamais dans une grammaire (règle de tri, Couche 0).
6. Nombre de grammaires : 12 — état courant, gouverné par les deux tests du §C.2.

## §D.3 Traçage des changements de base

L'historique des changements de base et des révisions structurelles du set (dont la numérotation des couches) est tenu dans `MRC_v5.7/_ETAT_INSCRIPTION_v5.7.md` et au suivi de l'Annexe méthodologique (§D). Toute réouverture passe par une décision tracée avec table de correspondance obligatoire.

## §D.4 Lacunes et limites

\[LACUNES ET LIMITES DE CE FICHIER\] (1) Le détail des champs F5–F7 et F9–F10 n'est pas reproduit (§B.3) — leur consolidation reste un chantier. (2) Les renvois « → NT-Gx » sont appliqués dans les fiches F1–F4/F8 reproduites ici ; toute divergence résiduelle avec les notes de grammaire est à contrôler. (3) L'état des verrous bibliographiques et le mapping source → grammaire porteuse sont tenus en Annexe méthodologique (§D.5, §D.9, §D.11) et au fichier d'état — non ici. (4) Tout résidu d'une numérotation de couches provisoire (« 1a », « 1b », grammaires en « Couche 2 ») serait un défaut de correction à signaler.

— MRC v5.7 — NT-ARCH · Architecture des Couches 0 à 3 —
