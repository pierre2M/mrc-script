# Annexe H — Dataroom augmentée et dispositifs techniques

*MRC v5.7. Régime : vérifiabilité-cohérence, mode procédural.*

---

## H.0 Statut de cette annexe

### H.0.1 Source fondatrice

L'Annexe H repose sur un document externe unique, identifié et lu intégralement :

> **The Blockchain for Good – France, *Blockchains et développement durable | Finance responsable et Web 3 — De la déclaration d'impact à sa preuve cryptographique*, juin 2026, 149 p.** Partenaires : Institut Louis Bachelier, Bpifrance. Licence CC BY-NC-SA 4.0. Direction de la publication : Jacques-André Fines Schlumberger. Parmi les auteurs et relecteurs : Dr. Louis Bertucci (Blockchain for Good, Institut Louis Bachelier), Dr. Hervé Alexandre (Chaire Fintech, Paris-Dauphine PSL), **Dr. Louis Dumeaux (Chaire comptabilité écologique)**. ✅ VÉRIFIÉ — lecture directe du PDF `MAQ-Finance-responsable-et-web-3-1.pdf`.

> **Point de couplage à noter.** Louis Dumeaux figure parmi les relecteurs de ce rapport et est, par ailleurs, la source du juste prix écologique en **NT-G12 / F8 §8.8** (*Quelle valeur pour l'échange ?*, thèse PSL, 2025). L'Annexe H et la sous-couche `C-CYCLE-PRIX` partagent donc un ancrage.

### H.0.3 Numérotation

La numérotation de cette annexe est celle des renvois du set, conformément à l'instruction du porteur : ce sont les 68 renvois existants qui font foi. NT-ARCH / F8 cite « H.4 (covenants) » et « H.5 (smart contracts) » ; l'Annexe K §K.6 cite « H.6 — smart contracts », « H.9 — interface de délibération » et « H.11 — registre des capitaux numériques ».

| Section | Objet |
| :-: | :-- |
| **H.1** | Identifiants décentralisés (DID) |
| **H.2** | Attestations vérifiables (VC) |
| **H.3** | dMRV et valuemètres de mesure |
| **H.4** | Covenants — l'obligation conditionnelle inscrite |
| **H.5** | Smart contracts — l'exécution, régime HARD |
| **H.6** | Covenant de priorité des créanciers — `R-PRIORITE-CREANCIERS` |
| **H.7** | Stockage à adressage par contenu (IPFS) |
| **H.8** | Architecture technique et phases d'usage |
| **H.9** | Interface de délibération *(appelée par K.6)* |
| **H.10** | Statut juridique et gouvernance du registre |
| **H.11** | Extension comptable — couche technique de F8 *(appelée 17 fois)* |
| **H.12** | Écueils, limites et conditions de réfutation *(section 2.2 du rapport)* |

### H.0.4 Ce que cette annexe fait, et ce qu'elle ne fait pas

**Elle décrit des fonctions et déclare des références. Elle ne spécifie rien.** Aucune méthode DID n'y est enregistrée, aucun schéma de VC n'y est arrêté, aucun schéma d'URI n'y est défini, aucune chaîne ni aucun langage de contrat n'y est choisi. **Ce n'est pas bloquant : voir ci-dessous.**

**L'invariant borné.** L'invariant de Couche 2 (NT-ARCH §B.2) exige une **source déclarée et vérifiable** définie par quatre propriétés — désignation stable, résolution déclarée, vérification d'intégrité, porteur nommé et réfutable — **dont le DID est une forme possible et non la forme obligatoire**. Parmi les six champs concernés (dont `inscription_communalite_uri_ref`), **quatre n'ont aucun besoin d'infrastructure décentralisée** : `mouvement_uri` désigne un ensemble fermé de seize valeurs, `traduction_uri` une clé composite, `valuemetre_uri` se satisfait d'une référence de méthode publiée, et `smart_contract_uri` est sans instance puisque l'Usage 3 est PROJETÉ.

**Ce qui reste non spécifié.** La présente annexe ne spécifie rien, et ce qu'elle ne spécifie pas est **classé par lots** : voir `C3_Specification_Identifiants_et_Bornage_Invariant_2026-09-19.md`, §5. **La révocation des attestations** n'apparaît pas une fois dans le rapport fondateur ; elle relève du standard Bitstring Status List (§H.2.1). **Le mécanisme d'interruption** d'une exécution n'a pas de standard (§H.5.4).

---

## H.1 Identifiants décentralisés (DID) — fondation de l'authenticité

### H.1.1 Le problème

L'acte notarial commence par l'identification des parties. Dans un registre multi-organisationnel — porteurs, financeurs, communes, associations de riverains, agences de bassin, OPCO, capteurs, oracles — cette identification ne peut reposer sur un registre central géré par une seule institution.

Le rapport fondateur établit que ce problème n'est pas théorique : selon l'initiative **ID4D de la Banque mondiale**, une fraction considérable des populations que vise la finance régénérative est sans identité vérifiable, donc invisible pour les marchés de capitaux formels (p. 129). *« Sans capacité à identifier de façon fiable, portable et souveraine les emprunteurs, les porteurs de projets et les intermédiaires locaux, aucun des instruments examinés dans ce rapport ne peut fonctionner à grande échelle »* (p. 128).

### H.1.2 Le standard

Un **identifiant décentralisé (DID)**, standardisé par le **W3C en 2022**, permet à un individu ou à une organisation de créer et contrôler son propre identifiant numérique sans dépendre d'une autorité centrale — banque, État ou plateforme. Le paradigme sépare trois éléments que les systèmes centralisés fusionnent : l'identifiant, les données personnelles, et la base de données ; le registre distribué ne sert que d'infrastructure publique de vérification (p. 129). ✅ VÉRIFIÉ — rapport p. 129.

### H.1.3 Qui reçoit un identifiant dans le MRC

Sous l'invariant borné §B.2, **le DID est une forme possible de source déclarée et vérifiable et non la forme obligatoire**. **Les formes `did:registre:…` ci-dessous sont des libellés de gabarit** — elles montrent la structure de désignation retenue, elles ne préjugent d'aucune méthode DID enregistrée, **et aucune ne l'est à ce jour**. Un identifiant stable existant — LEI, SIREN, DOI, identifiant d'instance de gestion, URL accompagnée d'une empreinte — satisfait la même fonction dès lors que les quatre propriétés de §B.2 sont établies.

| Type d'acteur | Forme d'identifiant (gabarit ; formes équivalentes admises) | Gouvernance de l'identifiant |
| :-- | :-- | :-- |
| Personne physique | `did:registre:person:…` | Auto-souverain, attesté par VC (H.2). **Écriture soumise à `statut_rgpd`** — voir H.7.3 |
| Organisation | `did:registre:org:…` | Gouvernance interne ; à l'échelle des personnes morales, le standard **vLEI** piloté par la **GLEIF** est la référence documentée (p. 130-131) |
| Commun écologique | `did:registre:milieu:…` | **Consortium multi-parties déclaré** : syndicat de bassin, commune, agence de l'eau, associations |
| Commun professionnel | `did:registre:travail:…` | Consortium OPCO + service public de l'emploi + Région + branches |
| Instrument de mesure | `did:registre:capteur:…` | Opérateur scientifique ou technique, certifié par VC de conformité |
| Corpus, concept formel | `did:registre:corpus:…` | Communauté linguistique ou équipe de recherche ; s'articule à `C-RIS` et `C-TCFP` (Fiche 3) |
| Valorimètre | `did:registre:valuemetre:…`, **ou toute autre forme de source déclarée et vérifiable** | `source_valuemetre` est **obligatoire** (NT-ARCH §B.2) ; **le DID en est une forme possible et non la forme obligatoire**  |

**Le DID d'un commun est le porteur que `consentement_inscription_NH` (F8 §8.6) présuppose.** Sans consortium déclaré, ce champ n'a aucun titulaire et ne peut prendre aucune valeur honnête.

**Articulation à la Couche 1.** Le consortium qui gouverne le DID d'un commun est un `legitimiterepresentant` au sens de la phase `REPRESENTATION-PROSPECTIVE` (NT-ARCH §5.2). Quand il vaut `PRATIQUE` ou `planetaireNonDesignee`, le champ `conditionrefutation` est **OBLIGATOIRE** : le DID ne dispense pas de déclarer à quelles conditions la représentation serait invalidée.

### H.1.3bis Le triplet porteur d'une inscription de communalité

*[Décision du porteur. Champ concerné : `inscription_communalite_uri_ref` (NT-ARCH §8.5).]*

**Le problème, en une phrase.** Une organisation à comptabilité tenue a un commissaire aux comptes, ou à défaut un régime comptable déclaré et un normalisateur. **Une entité sans comptabilité n'a ni l'un ni l'autre.** Quand une instance de gestion de l'eau, un consortium de bassin ou un collectif de métier inscrit une écriture dans son registre de communalité, **il faut dire qui écrit en son nom** — l'écriture duale de F8 §8.5.0 place cette inscription en miroir d'une écriture comptable attestée.

**Le patron vient du rapport fondateur, et il est directement transposable.** Le **vLEI de la GLEIF**, que le rapport qualifie d'*« effort de standardisation le plus avancé »*, *« combine cryptographiquement trois sources d'identité — l'identité de l'entité représentée par son code LEI, l'identité personnelle d'un individu, et le rôle officiel que cet individu exerce au sein de l'organisation — permettant une vérification instantanée et automatisée »* (p. 130).

**Toute inscription de communalité déclare donc un triplet.**

| Élément | Ce qu'il désigne | Formes admises | Articulation au set |
| :-- | :-- | :-- | :-- |
| **1. L'entité** | le commun ou le collectif au nom duquel l'écriture est portée | **LEI** (personne morale immatriculée), SIREN, identifiant d'instance de gestion (OLGE / PLE / CLE pour K3), `did:registre:milieu:…` | le consortium déclaré de H.1.3 ; `consentement_inscription_NH` (F8 §8.6) y trouve son titulaire |
| **2. La personne qui inscrit** | l'individu qui porte matériellement l'écriture | identifiant de personne, **soumis à `statut_rgpd`** (H.7.3) | `legitimiterepresentant` (NT-ARCH §5.2) |
| **3. Le rôle qui l'y habilite** | la fonction, au sein du consortium, qui lui donne le droit d'écrire | rôle déclaré dans les statuts de l'institution de gouvernance, attesté par la VC d'habilitation (H.2) | `C-DROITS` ; H.10.4 (règles explicites du consortium).  **Le rôle donne le droit d'écrire, non le pouvoir d'engager** : un `D+` de commun exige en outre `source_engagement_D` (NT-ARCH §8.5, règles §8.5.6.5) |

> **Condition de bonne formation.** Une inscription de communalité dont l'un des trois éléments manque **n'est pas bien formée**. Le deuxième peut être pseudonymisé au titre de `statut_rgpd` — il ne peut pas être absent : **pseudonymiser une personne n'est pas la même chose que n'en désigner aucune.** *Effet du défaut : **E3*** — inscrite, mal formée, phase DÉLIBÉRATION : le triplet dit qui répond de l'écriture (branche 4, attribution ; Annexe §A.15.11).

**Ce que le triplet ajoute au DID, et pourquoi il ne s'y réduit pas.** §H.1.4 restitue la réserve du rapport : *« un DID n'authentifie rien par lui-même »*, il déplace la question vers l'émetteur des attestations. **Le triplet est ce déplacement rendu explicite** : il ne dit pas que l'inscription est vraie, il dit **qui répond de l'avoir faite et à quel titre**. C'est la quatrième propriété de §B.2 — porteur nommé et réfutable — appliquée au cas où aucune institution comptable ne la garantit.

`[CE QUE LE TRIPLET NE RÉSOUT PAS]` **La révocation.** Un rôle se retire, une habilitation s'éteint, un consortium se recompose. Le rapport fondateur **ne mentionne aucun mécanisme de révocation** — le mot n'y apparaît pas une fois. Le mécanisme est pris hors du rapport, dans le standard **Bitstring Status List v1.0** : voir §H.2.1.

*Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* une écriture duale complète où le côté communalité porte ses trois éléments et le côté comptable son régime déclaré.

### H.1.3ter Résolution et vérification

**La voie du résolveur universel est fermée faute de méthode enregistrée, et ce n'est pas le seul obstacle : la spécification de résolution elle-même n'est pas une Recommandation.**

| Spécification | Statut | Date |
| :-- | :-- | :-- |
| **DID Core v1.0** | **Recommandation W3C** | 19 juillet 2022 |
| **Verifiable Credentials Data Model v1.1** | **Recommandation W3C** | 2022 |
| **Bitstring Status List v1.0** | **Recommandation W3C** | 15 mai 2025 |
| **DID Resolution v1** | **Candidate Recommendation Draft** — *« document de travail susceptible d'être modifié, remplacé ou rendu obsolète à tout moment »* | 28 août 2026 |

> **Quatre ans après que l'identifiant est devenu une norme, la manière de le résoudre n'en est toujours pas une.** Le rapport fondateur cite *« les spécifications W3C DID Core 1.0 et DID Resolution »* d'un même mouvement (p. 130), comme deux standards établis ; **ils ne le sont pas au même titre**, et c'est précisément la résolution — la **propriété 2** de l'invariant borné — qui manque. **Le bornage de l'invariant n'est donc pas un repli prudent : rendre le DID obligatoire ferait dépendre un invariant de Couche 2 d'une spécification en projet.**

**Sous le bornage, la résolution est une table à remplir** : l'invariant n'exige pas *une* procédure de résolution, il exige que **chaque forme déclare la sienne**.

| Forme admise (§B.2) | Résolution déclarée | Vérification d'intégrité | Statut |
| :-- | :-- | :-- | :-- |
| URL + empreinte SHA-256 | requête HTTP ; à défaut, recherche par empreinte | recalcul de l'empreinte | **éprouvée** — registre RATP 2025 |
| Identifiant de balise + empreinte du substrat | ouverture du rapport, localisation par identifiant | empreinte du substrat | **éprouvée** — registre RATP 2025 |
| DOI / identifiant d'archive | résolution DOI publique ; HAL | version déposée et horodatée | disponible |
| LEI | registre GLEIF | — | disponible |
| **vLEI** | GLEIF | signature ; triplet entité / personne / rôle | **à instruire** — cohérent avec §H.1.3bis |
| Référence de norme publiée datée | catalogue de l'organisme | numéro et version | disponible |
| **DID** | résolveur universel de la DIF, **méthodes enregistrées uniquement** | document DID signé | **indisponible pour le MRC** — aucune méthode `did:registre:` enregistrée, et la spécification de résolution est un projet |

> **Six formes sur sept sont résolubles aujourd'hui ; la septième est le DID.**

`[CE QUI RESTE OUVERT — la ligne DID, tant que deux conditions ne sont pas réunies : l'enregistrement d'une méthode, et la stabilisation de DID Resolution. **Aucune des deux ne dépend du MRC.**]`

### H.1.4 Condition de bonne formation — la réserve du rapport, restituée

> *« La valeur d'un DID dans un circuit financier dépend entièrement de la confiance que les contreparties accordent à ses émetteurs — ce qui ne fait que déplacer la question de la confiance, sans la supprimer. »* — rapport, p. 130.

**Un DID n'authentifie rien par lui-même.** Il déplace la question vers l'émetteur des attestations (H.2). Tout DID inscrit au registre déclare donc son émetteur d'attestation, et ce que cet émetteur engage.

Le rapport documente en outre un second écueil : *« la prolifération de systèmes d'identité décentralisés incompatibles reproduit, sous une forme technologiquement sophistiquée, la fragmentation des registres centralisés qu'elle prétend corriger »* (p. 130). La **Decentralized Identity Foundation (DIF)** y travaille par des bibliothèques ouvertes et des résolveurs universels d'identité.

`[SIGNAL]` `INSTRUMENT_HOTE_NON_DECLARE` (NT-ARCH §B.2bis) s'applique : un DID logé dans un dispositif non déclaré est une inscription sans hôte tracé.

### H.1.5 Les biens communs comme acteurs — deux exemples

**Le bassin versant : d'un contexte à un créancier.** Dans une dataroom classique, le bassin versant est décrit dans l'étude d'impact comme un contexte. Dans la dataroom augmentée, il a un DID géré par un consortium, un état biophysique continu alimenté par le dMRV, et des porte-parole légitimes qui peuvent inscrire observations, alertes, consentements ou refus. Les prélèvements du projet y sont inscrits comme **débits** vis-à-vis du bassin, les opérations de soin comme **crédits**. *La grammaire transforme le bassin versant en créancier* — ce que la comptabilité CARE dit dans sa propre grammaire (F8 §8.6 : `compte_passif_CARE = DETTE_NATURELLE`).

**Le bassin d'emploi : les compétences comme commun professionnel.** Produites collectivement, dégradées si non renouvelées, elles conditionnent la capacité d'un territoire à absorber un projet. Un projet qui importe ses corps de métier sans former localement prélève sans contribuer. Inscriptions : recrutements locaux qualifiés (VC liés aux DID des personnes), formations financées, sous-traitances, alternances. Articulation : `C-COMMUNALITE-TRAVAIL` et `C-DPQT` (Fiche 1), signal `COMMUN_GOUVERNE_FRAGILE`.

### H.1.6 Déploiements documentés

- **Algorand × DigiLocker (Inde)** — wallet de garde relié au registre national d'identité numérique ; accès de milliers d'emprunteuses rurales à un financement formel via un historique de crédit on-chain (p. 130).
- **Tadamon × Fondation Cardano** — ~5 200 organisations de la société civile dans 57 pays membres de l'OCI ; chaque organisation crée son DID et reçoit une VC présentable au PNUD et à la Banque islamique de développement sans redéposer un dossier (p. 131).
- **vLEI / GLEIF** — premier hackathon mondial en 2025 ; applications documentées à l'accès au crédit agricole en Afrique et en Asie (p. 131).
- **Hypercerts V2** — ATProtocol hors chaîne + **Ethereum Attestation Service (EAS)**, identifiants cross-apps permettant à tout registre d'impact de se brancher sur la même couche de certification (p. 131).

---

## H.2 Attestations vérifiables (VC) — chaînes d'attestation

Les **Verifiable Credentials**, standardisées par le **W3C** (même consortium que les DID), sont des certificats numériques signés cryptographiquement, émis par des tiers de confiance — institution financière, organisation certificatrice, administration locale — et conservés par leur détenteur dans un portefeuille d'identité (rapport, p. 129). Elles sont **portables** : un financeur les vérifie lui-même, sans passer par le porteur ni son auditeur.

| Type de VC | Émetteur | Ce qu'elle renseigne dans le MRC |
| :-- | :-- | :-- |
| Consentement à l'inscription | L'acteur concerné | `consentement_explicitation` ; `statut_rgpd` (F8, arbitrage Q10) |
| Consentement du consortium NH | Consortium de gouvernance du commun | **`consentement_inscription_NH`** (F8 §8.6) |
| Habilitation à inscrire au nom d'un commun | Consortium de gouvernance | Conditionne le droit d'écriture — `C-DROITS` |
| Qualification scientifique d'un instrument | Comité scientifique, agence | `source_valuemetre`, `doctrine_CARE_appliquee`, `doctrine_juste_prix` (F8 §8.6, §8.8) |
| Co-construction d'un valorimètre | Communauté co-constituante | `soin_avec` (Fiche 1), `soin_avec_milieu` (Fiche 2), `C-INSCRIPTION-CORPUS` (Fiche 3) |
| Évaluation tracée | Acteur évaluateur | `R-POUVOIR` — **sans VC, l'évaluation est invalide** (Fiche 6) |
| Représentation d'un acteur non tracé | Consortium ou institution | `legitimiterepresentant` + `conditionrefutation` (NT-ARCH §5.2) |
| Valorimètre sémantique actif | Communauté co-constituante | **`valuemetre_semantique_actif`** (DID du valorimètre — Fiche 3, `C-SEM`) |

`[LACUNE DÉCLARÉE — `R-POUVOIR` porte l'obligation d'évaluation tracée ; aucun signal ne porte son manquement.]`

### H.2.1 Schéma d'attestation et révocation

Le mot « révocation » **n'apparaît pas une fois dans le rapport fondateur**. La lacune est réelle dans le rapport, **non dans le standard** : **Bitstring Status List v1.0 est une Recommandation W3C du 15 mai 2025**, et elle distingue quatre finalités de statut dont deux intéressent le MRC.

| `statusPurpose` | Effet | Ce que cela inscrit dans le MRC |
| :-- | :-- | :-- |
| **revocation** | annulation **définitive** | retrait d'une habilitation à inscrire, fin d'une qualification d'instrument |
| **suspension** | blocage **temporaire et réversible** | suspension d'un rôle pendant une contestation, une vacance ou une enquête |
| refresh | une version à jour existe | renouvellement d'une attestation périodique (OTI, comité de mission) |
| message | statut descriptif | — |

> **La distinction révocation / suspension compte.** Un rôle dans un consortium ne se retire pas seulement : **il se suspend**. Et la suspension est la forme d'attestation qui correspond à **la mise en attente de l'arbitrage A8** *(non l'axiome AX-8)* — une lacune de table met l'écriture en attente, elle ne la refuse pas.

**Ce qu'une attestation du MRC doit porter.** Les champs sont dérivés des versements du set, non inventés.

| Élément | Origine | Obligatoire |
| :-- | :-- | :-- |
| Émetteur nommé et résoluble | NT-ARCH §B.2 borné, propriété 4 | oui |
| Sujet, et **objet attesté** — la proposition attestée, non le seul fait d'attester | — | oui |
| **Triplet porteur** — entité, personne, rôle | §H.1.3bis | oui pour un registre de communalité |
| **`portee_attestation`** — ECRITURE / PROCEDURE / TRAJECTOIRE | NT-ARCH §8.6 | oui |
| **`periodicite_attestation`** | NT-ARCH §8.6 | oui |
| **Niveau d'assurance** — modérée / raisonnable | avis technique CNCC (§H.10.2) | oui |
| Date d'émission et durée de validité | — | oui |
| **Statut** — révocation / suspension, et où il se lit | **Bitstring Status List v1.0** | oui |
| **`publicite_statut`** — `PUBLIC_TRANSITOIRE_DECLARE` / `MUTUALISE` / `NONDECLARE` (refuse)  | décision du porteur | oui |
| **Condition de réfutation** | NT-ARCH §5.2 | oui |

 Le **niveau d'assurance** et la **portée** ne sont pas des champs du modèle W3C : ce sont des exigences propres au MRC, nées d'un cas réel — l'avis d'un OTI est une **assurance modérée de portée PROCEDURE**, ce qui ne se déduit d'aucun champ standard. **Sans elles, une attestation de procédure bisannuelle se lirait comme une attestation d'écriture.**

> ### `[CONTRAINTE SÉRIEUSE — la révocation est, pour les petits collectifs, un mécanisme de divulgation]`
>
> La spécification fixe une **taille minimale de liste de 131 072 bits** (16 Ko non compressés) pour garantir la *herd privacy*, et avertit que le mécanisme est **vulnérable si l'émetteur crée une liste par attestation**.
>
> **Un consortium de gouvernance de douze membres ne peut pas atteindre la herd privacy.** Publier sa liste de statut revient à publier en clair qui a été révoqué et quand. C'est le conflit de §H.7.3 — permanence contre effacement — sous une autre forme.
>
> Deux voies, aucune gratuite : **mutualiser la liste de statut entre consortiums**, ce qui suppose l'accord d'interopérabilité que le rapport pose en condition politique (p. 131) ; ou **assumer la publicité du statut** et la déclarer aux porteurs **avant** leur habilitation.
>
> Un consortium dont la liste n'atteint pas 131 072 entrées **publie son statut en clair et le déclare** : `publicite_statut = PUBLIC_TRANSITOIRE_DECLARE`, avec **(i)** la taille effective de la liste, **(ii)** la date d'information du porteur, **antérieure** à l'émission de l'habilitation, **(iii)** le critère de sortie. **La publicité porte sur le statut, jamais sur le motif** — le motif reste hors liste, sous habilitation (§H.7.3, disposition 3). **La suspension est couverte au même titre que la révocation.**
>
> *Porteur :* l'émetteur de la liste (le consortium, §H.1). *Horizon :* transitoire, sans échéance calendaire. *Critère de sortie :* liste `MUTUALISE`, ou liste propre d'au moins 131 072 entrées. *Critère de révision :* un refus d'habilitation documenté **à cause de** la publicité du statut rouvre la décision — c'est le coût sur le recrutement, déclaré et non mesuré tant qu'aucun refus n'est tracé.
>
> `[ENGAGEMENT À HORIZON IRRÉVERSIBLE — borné, non levé]` La décision porte sur **la liste courante**, qui est mutable. **Ancrer ses versions successives dans un stockage à adressage par contenu rendrait la publicité permanente** : cet ancrage reste **subordonné à §H.7.3**, non résolu. `[PLAUSIBLE, NON VÉRIFIÉ — le statut d'habilitation d'une personne nommée est vraisemblablement une donnée personnelle ; l'information préalable n'établit pas à elle seule une base légale. Pas d'avis juridique.]`

**Preuve sans divulgation.** Le rapport documente une architecture qui intéresse directement le MRC : le **Zero-Knowledge Machine Learning (ZKML)**, par lequel une certification est produite et auditée **sans exposer les données sous-jacentes** — IXO Protocol via son agent WISP pour l'impact climatique, PACT Foundation / ImpactMarket pour l'évaluation d'impact social des micro-crédits (p. 99). C'est la seule voie documentée pour concilier `statut_rgpd` et permanence (H.7.3).

---

## H.3 dMRV et valuemètres de mesure

### H.3.1 Ce que le dMRV change

Le dMRV — *digital Measurement, Reporting and Verification* — substitue à la vérification périodique une vérification continue, automatisée, fondée sur des données collectées indépendamment : imagerie satellitaire, capteurs IoT, modèles d'apprentissage automatique (rapport, p. 85).

Le rapport insiste sur la nature du déplacement : *« la rupture introduite par le dMRV ne se limite pas à une réduction de coûts : elle modifie la nature même de l'information disponible pour les marchés, en substituant à un certificat émis à intervalles fixes un flux de données actualisé en quasi temps-réel »* (p. 85). Et il nomme le prix à payer : *« elle déplace la question de la fiabilité de l'auditeur humain vers la fiabilité des données en entrée du système »* (p. 88).

### H.3.2 Sources par mode, et signaux alimentés

**Tous les signaux cités ci-dessous sont présents dans le set** (recherche menée sur la forme échappée et non échappée des noms).

| Mode | Sources dMRV | Signaux alimentés |
| :-- | :-- | :-- |
| **M-MILIEU** | Capteurs IoT (turbidité, débit, piézomètres) ; imagerie satellitaire et SAR ; **ADN environnemental (aDNe)** ; modèles allométriques calibrés LiDAR | `signal_ecologie_superficielle` · `OBLIGATION_PRESERVATION_VIOLEE` · `signal_amortissement_NH_insuffisant` (F8 §8.9) |
| **M-TRAVAIL** | VC de formation ; contrats signés numériquement ; indicateurs **France Travail**, OPCO, CARIF-OREF | `COMMUN_GOUVERNE_FRAGILE` · `signal_travail_invisible` · `signal_capabilite_alerte` |
| **M-SEMANTIQUE** | Corpus indexés ; treillis FCA pondéré (`C-TCFP`) ; valorimètres co-construits | `CORPUS_NON_CONSENTI` · `carre_non_commutatif` · `PIEGE_ATTRACTEUR` |
| **M-EXISTENTIEL** | Indicateurs systémiques croisés ; horizons temporels indexés (Annexe G.4) | `signal_horizon_incommensurable` · déclencheur possible de `R-INTERDIT-ABSOLU` via `Exist` |

Six autres signaux sont présents et déclenchés dans le set, avec la condition suivante :

| Signal | Fiche | Condition de déclenchement (NT-ARCH) | Mode dMRV qui l'alimente |
| :-- | :-- | :-- | :-- |
| `GENRE_GELE_PERSISTANT` | Fiche 1 | `emotion_dominante_genre` élevée sur 3 interactions consécutives | M-TRAVAIL |
| `MILIEU_DEGRADE_PERSISTANT` | Fiche 2 | `etat_habitabilite_milieu` = FRAGILE / INHABITABLE sur 2 interactions, ou indicateur sous `seuil_alerte_milieu` | M-MILIEU |
| `TOKEN_MARGINAL_NON_ENTENDU` | Fiche 3 | `appel_entendu_semantique` = FAUX ET `asymetrie_DEBIT_CREDIT` < −2 | M-SEMANTIQUE |
| `CONCEPT_INHABITABLE` | Fiche 3 | `etat_habitabilite_semantique` = INHABITABLE | M-SEMANTIQUE |
| `RISQUE_EXISTENTIEL_IMMINENT` | Fiche 4 | `risque_existentiel` = IMMINENT ou IRREVERSIBLE | M-EXISTENTIEL |
| `effondrement_existentiel_calcul` | Fiche 4 | À un horizon h, V_h ne peut plus accueillir les acteurs (Annexe G.5) — **calcul, non déclaration** | M-EXISTENTIEL |

Deux conséquences pour le dMRV, qui ne tiennent que parce que ces signaux existent. `MILIEU_DEGRADE_PERSISTANT` est le seul des six dont la condition passe par un **seuil numérique** (`seuil_alerte_milieu`) : c'est donc le seul directement exposé à l'intervalle de confiance déclaré en H.3.3, et une chaîne dMRV qui l'alimente sans intervalle produit un déclenchement sans convention. `effondrement_existentiel_calcul` déclenche `R-INTERDIT-ABSOLU` : aucune source dMRV ne peut être son unique entrée sans que la limite d'irréversibilité de H.3.3 ne s'applique à plein.

`[LACUNE ET LIMITE — la table « Sources par mode » ci-dessus reste une proposition de cette annexe : aucune fiche du set ne déclare la source dMRV admissible pour un signal donné. L'appariement signal × source est donc **non attesté par le modèle**.]`

### H.3.3 Ce que le dMRV ne peut pas faire — porté par le rapport

Le rapport énonce deux limites (p. 88) :

1. **La qualité des données elles-mêmes.** Couverture nuageuse, limites de résolution selon les écosystèmes, et surtout **les hypothèses des modèles allométriques** utilisés pour convertir des indices de végétation en stocks de carbone : ces marges d'incertitude *« doivent être quantifiées et communiquées »*.
2. **L'irréversibilité de l'erreur.** *« Une fausse donnée une fois validée ne peut être corrigée, et les contrats financiers qui s'y réfèrent s'exécuteront durablement sur des prémisses erronées — rendant les erreurs bien plus coûteuses et difficiles à résorber que dans la finance traditionnelle »* (BRI, cité p. 114).

**Conséquence de Couche 2, versée ici.** Tout valorimètre alimenté par dMRV déclare son **intervalle de confiance** et sa **méthode de conversion**, au titre de `source_valuemetre`. Un indicateur dMRV sans intervalle déclaré est un seuil sans convention — le défaut que R0-bis et `convention_seuil_source` (NT-G12) interdisent.

### H.3.4 Déploiements documentés

**Project Genesis (BRI × Hong Kong Monetary Authority, 2021-2022)** : prototypes d'obligations vertes tokenisées combinant blockchain, smart contracts et IoT pour le suivi en temps réel des sorties environnementales ; **Genesis 2.0** conduit en 2022 avec Goldman Sachs et UN Climate Change (p. 88). — **aDNe** : analyse systématique publiée dans *Communications Earth & Environment* (2024) sur 129 projets carbone forestiers et 396 études, établissant une *« large portée taxonomique, un échantillonnage de terrain simplifié et des gains d'efficience à l'échelle »* (p. 98). — **Inaltérabilité** : revue publiée dans *Discover Environment* (2025) — *« les registres distribués créent des enregistrements immuables sur l'origine, le suivi et la propriété des quotas carbone »* (p. 89). — **Méthodologies de certification** compatibles citées : Verra VCS, Gold Standard, Regen Network (p. 99). — **Chainlink Data Standard** (mai 2025) pour la sécurisation des flux (p. 107).

---

## H.4 Covenants — l'obligation conditionnelle inscrite

**Un covenant est une clause d'un contrat de financement qui impose au porteur des obligations de comportement pendant la durée du prêt, sous peine de remboursement anticipé ou de pénalités.** Les covenants ESG sont aujourd'hui des obligations **déclaratives** : ils n'opèrent pas en temps réel et reposent sur la bonne foi du déclarant.

H.4 porte **l'obligation** ; H.5 porte **son exécution**. La distinction est celle que les renvois de F8 présupposent — `smart_contract_uri` (§8.7) désigne l'exécutant, pas la clause.

Tout covenant inscrit déclare cinq éléments, et cette exigence est la transposition directe de la Couche 2 :

| Élément | Champ ou renvoi |
| :-- | :-- |
| **Le porteur de l'obligation** | acteur identifié par son DID (H.1) — jamais une catégorie générique |
| **Le seuil et sa convention** | `source_valuemetre` **OBLIGATOIRE** — source déclarée et vérifiable, DID non requis (NT-ARCH §B.2 borné) — + intervalle de confiance (H.3.3) |
| **L'horizon** | court terme institutionnel / intergénérationnel / **irréversible** (NT-ARCH §6) |
| **La conséquence et sa réversibilité** | gel de tranche, alerte, blocage — et si l'effet est non annulable, `[ENGAGEMENT À HORIZON IRRÉVERSIBLE]` |
| **Ce que le seuil rend optimisable**  | **`hors_champ_optimisation`** (NT-ARCH §8.8) — l'indicateur que le covenant rend optimisable, **et ce que cette optimisation laisserait hors champ**. Obligatoire pour tout covenant déclenchant un effet financier |

**Trois fonctions documentées.**

*H.4.1 Déblocage conditionnel des fonds.* Les tranches successives sont conditionnées à des états vérifiables du registre : tranche 2 débloquée quand les VC de formation de 15 salariés locaux sont inscrites et que les indicateurs piézométriques sont dans les limites convenues. La promesse devient condition architecturale.

*H.4.2 Alerte automatique aux parties habilitées.* Tout signal `C-SIGNAL` est diffusé aux acteurs habilités selon leur DID et leur VC d'habilitation, avec une granularité gérée cryptographiquement : financeur senior en temps réel, financeur participatif en synthèse, commune pour son territoire, riverains pour leur bassin.

*H.4.3 Cas type.* Un lotissement en zone de recharge d'aquifère obtient son financement avec ce covenant : si les indicateurs piézométriques descendent sous le niveau de référence **deux saisons consécutives**, la tranche finale est gelée jusqu'à un plan de compensation validé par le syndicat de bassin — dont le DID co-signe le contrat.

---

## H.5 Smart contracts — l'exécution, et le régime HARD

H.5 est ce que NT-ARCH §8.7 et §8.11 appellent : `regime_application = HARD` signifie « blocage via smart contract H.5 » ; l'Usage 3 exige « smart contracts d'Annexe H.5 actifs ».

### H.5.1 Exécution automatique des règles de Couche 1

`R-COUPLAGE`, `R-HABITABILITE` et `R-INTERDIT-ABSOLU` deviennent des conditions inscrites. Quand le calcul d'une 2-cellule détecte un défaut de commutativité au-delà du seuil déclaré, le contrat inscrit `carre_non_commutatif`, notifie les acteurs responsables et ouvre une phase **`DELIBERATION`** dans `C-ENQUETE-V5` — sans que cette ouverture dépende d'une décision discrétionnaire. Quand l'effondrement existentiel est détecté dans `Exist`, le contrat déclenche `R-INTERDIT-ABSOLU`.

Phase retenue : `DELIBERATION`. `[À CONFIRMER PAR LE PORTEUR — `AUTOGOUVERNANCE` ou `ENQUETE_COLLECTIVE` conviendraient aussi.]`

`[SEUIL — CONVENTION EXIGÉE]` Le seuil de défaut de commutativité dit qui le pose. Un seuil qui déclenche un blocage est un valorimètre : il déclare son `source_valuemetre` et son poseur, faute de quoi l'inscription est mal formée. *Effet du défaut : **E1*** — le seuil conditionne l'exécution sur d'autres écritures (branche 3) : **il n'est pas inscrit, le blocage automatique ne s'arme pas** ; statut candidat à horizon admissible (Annexe §A.15.11). Même exigence que pour les deux seuils de F8 §8.9 (`taux_couverture_DNH`, `ecart_juste_prix`), donnés comme « typiques » sans source.

### H.5.2 Contrôle de symétrie R1 — et les deux asymétries autorisées

**Un contrat qui refuserait l'enregistrement de toute interaction sans écriture miroir bloquerait les deux asymétries que le modèle autorise expressément** (NT-ARCH §3bis), dont l'une est précisément celle que `R-INTERDIT-ABSOLU` doit protéger.

**Règle.** Le contrat vérifie que le couple (`typage_primitive`, `typage_miroir`) **appartient à la table §8.5.2** — contrôle calculé. Il **n'exige pas** un miroir dans tous les cas. Deux et seulement deux écritures passent sans second livre :

| Asymétrie autorisée | Forme | Traitement par le contrat |
| :-- | :-- | :-- |
| **Engagement existentiel** | `E+ ↔ ∅`, `asymetrie_existentielle = VRAI` | **Acceptée sans miroir.** Le refuser serait empêcher l'inscription d'un engagement envers un acteur non tracé |
| **Dette systémique** | dette sans débiteur attribuable | **Acceptée**, avec `C-STATUT-DETTE` renseigné (NT-ARCH §3) |

Un couple **absent de la table** n'est pas refusé par le contrat comme une fraude : il est **mis en attente** et remonté au porteur, parce qu'une absence de ligne est une lacune de table, pas une violation de R1 — distinction posée en NT-ARCH §8.5.2bis.4.

`[PRÉCÉDENT]` Les lignes `P+ ↔ P−`, `P− ↔ e`, `E−` et `e ↔ E+` de la table §8.5.2 portent des écritures licites — un achat au comptant, une dotation aux amortissements : un contrat qui refuserait tout couple absent de la table refuserait de telles écritures dès que la table est lacunaire.

### H.5.3 Ce que H.5 ne contient pas

`[SPÉCIFICATION ABSENTE — DÉCLARÉE]` Aucune chaîne, aucun langage de contrat, aucun schéma pour `smart_contract_uri`, aucun mécanisme d'arrêt d'urgence. `_ETAT_INSCRIPTION_v5.7.md` inscrit ce point parmi les arbitrages ouverts : « spécification opérationnelle des smart contracts pour le régime HARD ». **Tant qu'elle n'est pas versée, `regime_application` ne peut valoir que `SOFT` et l'Usage 3 n'est pas accessible.**

Le rapport fondateur ajoute une raison de prudence : un contrat qui s'exécute *« de façon automatique et sans possibilité d'interruption manuelle »* sur un oracle compromis exécute une preuve corrompue (p. 113). **Toute spécification future de H.5 déclare son mécanisme d'interruption, ou déclare qu'elle n'en a pas.**

---

### H.5.4 Interruption et substrat

#### Le blocage de l'interruption est interne

Le rapport fondateur fait de l'absence d'interruption son reproche central — *« sans possibilité d'interruption manuelle »* (p. 113) — sans documenter aucun mécanisme. **Le blocage réel est ailleurs, et il est plus profond.**

> *« Le registre sait ouvrir une obligation, la faire délibérer, l'attribuer et la rendre critique ; il ne sait pas la refermer. »* Les termes `ETEINTE`, *extinction de l'obligation*, *clôture de l'épisode* comptent **zéro occurrence** dans le set.

**Interrompre suppose une sortie.** Dans un dispositif qui ne sait rien clore, un mécanisme d'interruption n'est pas une interruption : **c'est une suspension indéfinie sans procédure de reprise ni de fin.**

#### Ce que l'état de l'art fournit, et ce qu'il ne fournit pas

**Il n'existe pas de standard** : seulement des patrons — arrêt d'urgence (`Pausable`), plafonds de fonction, listes d'accès, limiteurs de débit, verrous temporels. **EIP-7625, qui normaliserait l'arrêt sur franchissement de seuil, est encore en discussion.** Les modèles de gouvernance du pouvoir d'arrêt sont eux documentés : équipes communautaires de sécurité, **conseils multisignatures** associant communauté, partenaires et équipe interne, automatisation sur seuils.

**Et la littérature technique nomme le coût dans les termes mêmes que le MRC emploierait** : une pause *« crée une condition de déni de service pour tous les autres utilisateurs »*, et les listes de blocage soulèvent la crainte d'une reprise en main centralisée. **Le pouvoir d'interrompre est un pouvoir, et il est le plus souvent détenu sans être attribué.**

#### Spécification proposée — **l'interruption est une écriture, pas un interrupteur**

Le MRC porte `C-POUVOIR` et `R-POUVOIR` — toute évaluation s'inscrit avec son porteur — et `porteur_instance` (F6.2). **Il ne peut pas accueillir un pouvoir d'arrêt anonyme.**

> Toute interruption d'une exécution déclare, **avant de produire effet** : **qui** interrompt (`porteur_instance`, instance CONTROLE) · **sur quel constat** · **pour quel horizon** · **à quelle condition elle est levée** · **et qui peut contester l'interruption comme la levée**.
>
> **Une interruption sans condition de levée déclarée est une clôture déguisée** — et le registre n'a pas de clôture.

**Cette forme borne les deux défauts à la fois.** Celui que le rapport reproche aux dispositifs existants — aucune interruption possible — et celui que la littérature signale — une interruption détenue sans être attribuée — sont les deux faces du même manque : **l'arrêt n'est pas inscrit.** En faire une écriture le soumet aux règles de tout le reste du registre.

#### Le MRC ne choisit pas de chaîne, il exige qu'elle soit déclarée et remplaçable

Le rapport montre pourquoi le choix est piégé, sur un cas qu'il documente : Regen Network *« affronte une décision d'architecture dont l'enjeu est précisément l'interopérabilité mondiale : rester sur Cosmos SDK ou migrer vers un environnement EVM »* (p. 131). Et il pose que la sortie n'est pas technique mais politique.

**Le set a déjà le champ qui règle la question.** Une chaîne est un **instrument-hôte** au sens de C-TRACABILITE (NT-ARCH §B.2bis), dont le signal `INSTRUMENT_HOTE_NON_DECLARE` pose qu'*« un DID logé dans un dispositif non déclaré est une inscription sans hôte tracé »*.

> **(1)** La chaîne est un **instrument-hôte déclaré**. Une écriture dont l'hôte n'est pas déclaré déclenche `INSTRUMENT_HOTE_NON_DECLARE`.
>
> **(2) Exigence de portabilité — aucune écriture ne tire sa validité de la chaîne qui la porte.** La validité se calcule par l'appartenance du couple à la table §8.5.2 et par les quatre propriétés de §B.2 ; **rien de cela ne dépend d'un substrat**. Une écriture vérifiable sur une seule chaîne serait une écriture **dont la preuve est captive**.
>
> **(3)** Le langage de contrat suit le sort de l'Usage 3 : **PROJETÉ**. Son premier prérequis n'est de toute façon pas le langage mais l'interruption.

**Pourquoi ce n'est pas une esquive.** Choisir une chaîne aujourd'hui trancherait par un acte technique la question politique que le rapport déclare préalable, **au bénéfice des acteurs qui opèrent déjà sur cette chaîne** — c'est exactement la troisième condition du rapport prise à rebours. L'exigence de portabilité **préserve la possibilité de l'accord au lieu de la préempter**.

`[RÉSERVE — la portabilité suppose que la validité d'une écriture soit entièrement calculable hors chaîne. C'est vrai des règles actuelles ; cela cesserait de l'être si une règle venait à dépendre d'un ordonnancement ou d'un horodatage fournis par la chaîne. `[PLAUSIBLE, NON VÉRIFIÉ]`]`

## H.6 Covenant de priorité des créanciers — implémentation de `R-PRIORITE-CREANCIERS`

*F8 §8.7 fait exécuter le régime HARD de `R-PRIORITE-CREANCIERS` par des smart contracts de cette annexe ; H.6 en porte le covenant.*

**La règle** (Couche 1, implémentée en F8 §8.7) : on rembourse d'abord les capabilités plancher (N1), puis les dettes envers les capitaux naturels et humains (N2), puis les dettes financières contractuelles (N3), **avant** toute distribution discrétionnaire (N4).

**Le covenant.**

| Condition | Champ F8 | Effet en régime HARD | Effet en régime SOFT |
| :-- | :-- | :-- | :-- |
| N1 satisfait | `seuil_capabilites_satisfait` | — | — |
| N2 couvert | `dette_NH_couverte_exercice` | — | — |
| N3 honoré | `dette_financiere_honoree` | — | — |
| **Distribution inscrite alors que `distribution_autorisee = FAUX`** | mouvement `j` ou `h` en CARE | **le contrat bloque l'inscription** | `signal_distribuable_avant_NH` levé, inscription passée, `motif_violation` **obligatoire** |
| Effacement d'une dette NH sans consentement du consortium | mouvement `m` | **le contrat bloque** | `signal_remise_NH` levé |
| Couverture durablement insuffisante | `taux_couverture_DNH` | alerte au consortium NH | `signal_amortissement_NH_insuffisant` |

**Garde explicite.** Le rabattement de `S'` sur `E` versé en F8 §8.5.1ter est un fait de **typage** et n'emporte **aucun effet** sur `niveau_prioritaire`. Une distribution aux apporteurs reste N4 même si elle se type `E−`. Toute lecture contraire est un `[DÉCOUPLAGE DE RÉGIMES]`.

**Statut.** `[PROJETÉ, NON DÉPLOYÉ]` Aucun covenant de ce type n'existe dans les cas du set. K1 porte `regime_application = SOFT` et `smart_contract_uri = ∅`. Le présent H.6 spécifie **ce qu'il faudrait écrire**, pas ce qui est écrit.

---

## H.7 Stockage à adressage par contenu — permanence et intégrité

Un registre notarié doit survivre à ses parties. Les plateformes de dataroom ferment ; stocker des documents complets on-chain est prohibitif. Le **stockage à adressage par contenu** résout la tension : chaque document est identifié par son empreinte cryptographique, seul le hash est inscrit on-chain, et toute modification change le hash. Le rapport rattache ce dispositif à **Protocol Labs**, à l'origine du protocole **IPFS** et de la blockchain **Filecoin** (p. 106).

**H.7.1 Ce que cela fonde dans le MRC.** `C-MEMOIRE-PERTES` (Couche 1) et `R-MEMOIRE` : les pertes documentées et la dette héritée qualitative ne peuvent être ni effacées ni falsifiées, et restent accessibles même si l'opérateur initial disparaît. C'est la condition matérielle des engagements à horizon intergénérationnel.

`[LACUNE DÉCLARÉE — `C-MEMOIRE-PERTES` sans table de champs]` Aucun champ du set ne rend l'inscription d'une perte non facultative. `C-MEMOIRE-PERTES` est **invoqué 28 fois dans le set** (NT-ARCH, NT-G2, NT-G3, NT-G6, NT-G9, Annexe K, Annexe méthodologique) **sans qu'aucun document ne porte sa table de champs de Couche 1**. Ce qui est écrit ci-dessus — permanence, non-falsifiabilité, accessibilité après disparition de l'opérateur — est donc, en l'état du set, une **proposition de cette annexe et non une reprise du modèle**. Tant que la table n'est pas versée, l'ancrage par hash décrit en H.7 n'a pas d'objet comptable défini à ancrer. `[À INSTRUIRE — verser la table de champs de `C-MEMOIRE-PERTES` en Couche 1, et y trancher le caractère obligatoire de l'inscription d'une perte (champ `inscription_obligatoire`).]`

**H.7.2 Ce que cela fonde pour F8.** Le hash d'un document est ce qui rend une écriture opposable en Usage 3 : *« identité de l'inscripteur signée, statut explicite, source horodatée, hash, traçabilité »* (§8.11). Le registre RATP 2025 en donne un précédent hors chaîne : il porte le SHA-256 de ses deux substrats, et c'est ce qui le rend ré-auditable par un tiers.

**H.7.3 La contrainte RGPD — déclarée, non résolue.**

`[ENGAGEMENT À HORIZON IRRÉVERSIBLE — délibération nécessaire avant conclusion]`

La permanence entre en conflit direct avec le droit à l'effacement. NT-G9 porte l'obligation : l'inscription de données sensibles dans un registre permanent *« serait irréversible par construction »*. F8 exige `statut_rgpd` pour toute écriture touchant à des personnes (arbitrage Q10).

**Trois dispositions, dont aucune n'est une solution complète :**

1. **Ne jamais inscrire la donnée, seulement son empreinte** — le document reste hors chaîne, révocable ; seul le hash est permanent. Un hash sans le document ne permet plus de vérifier que la destruction.
2. **Preuve sans divulgation (ZKML)** — la certification est auditable sans exposer les données (H.2, rapport p. 99). C'est la seule voie documentée qui préserve les deux exigences.
3. **Cloisonnement par habilitation** — les données personnelles ne quittent pas un périmètre restreint, la permanence ne portant que sur les agrégats.

**Aucune de ces trois dispositions n'est spécifiée dans le set.** L'obligation NT-G9 reste ouverte, et le déploiement de H.7 sur des données personnelles lui est **subordonné**.

---

## H.8 Architecture technique et phases d'usage

### H.8.1 Trois couches techniques

| Couche technique | Composantes | Articulation aux couches du MRC |
| :-- | :-- | :-- |
| **Identité et attestations** | DID (H.1) · VC (H.2) · droits d'accès cryptographiques | Couche 0 (`C-INSCRIPTION`) ; `C-DROITS` ; `C-TRACABILITE` ; `C-CLOTURE-ACCES` (F8 §8.2bis) |
| **Données et mesures** | dMRV biophysique (H.3) · données sociales · oracles validés par la gouvernance du commun | Couche 1 (régime attentionnel pour acteurs non humains) ; Fiches 1, 2, 3 ; valorimètres de F8 |
| **Règles et mémoire** | Smart contracts (H.5, H.6) · horodatage et hachage · stockage adressé par contenu (H.7) | Couche 1 (`R-COUPLAGE`, `R-HABITABILITE`, `R-INTERDIT-ABSOLU`) ; `C-MEMOIRE-PERTES`, `R-MEMOIRE` ; `C-SIGNAL` |

La sous-couche `C-CLOTURE-ACCES` trouve ici son support technique. `cloture_declaree` — qui est exclu, par quel dispositif, qui l'a posé — est exactement ce qu'une VC d'habilitation inscrit ; `enjeu_acces` est ce que le déblocage conditionnel de H.4.1 rend opérant.

### H.8.2 Trois phases temporelles

**Due diligence.** Le financeur n'accède pas à un dossier statique mais à un registre partiellement constitué : inventaire des acteurs identifiés par DID — *inventaire qui est lui-même un engagement*, puisque tout acteur inscrit est une partie dont le consentement et les interactions seront suivis ; état initial des communs attesté par les institutions compétentes plutôt que par le porteur ; légitimité des instruments de mesure, contestations comprises ; covenants lisibles avant signature. *La due diligence cesse d'être un audit de documents pour devenir une lecture de relations.*

**Financement et travaux.** Trois flux : inscriptions du porteur, signées par son DID ; inscriptions automatiques du dMRV, signées par les instruments, **indépendantes de toute décision humaine du porteur** ; inscriptions des tiers — commune, riverains, OPCO, syndicat de bassin.

**Suivi post-financement et transmission.** La dataroom n'a pas de date de fermeture. Les droits d'accès sont transmissibles ; les engagements de préservation survivent au financement initial et sont opposables aux porteurs successifs.

`[RÉSERVE]` **Cette dernière affirmation n'est pas une garantie architecturale des smart contracts** : l'opposabilité aux porteurs successifs est une question juridique (H.10), non une propriété technique.

---

## H.9 Interface de délibération

*Section appelée par l'Annexe K §K.6 (cas K2, où elle est notée « partielle — GitHub Issues/Discussions »).*

Les phases `DELIBERATION`, `ENQUETE_COLLECTIVE`, `ENQUETE_OBSERVATIONNELLE`, `AUTOGOUVERNANCE` et `RECHERCHE-INTERVENTION` de `C-ENQUETE-V5` supposent un lieu où elles se tiennent. H.9 en porte les exigences minimales :

| Exigence | Motif |
| :-- | :-- |
| Participation **ouverte aux représentants des communautés affectées** | `R-POUVOIR` ; `legitimiterepresentant` |
| Traçabilité des positions et des révisions | `C-MEMOIRE-PERTES` ; on ne réécrit pas une délibération |
| **Déclaration de la pondération des voix** | Fiche 9/10 — démocratie épistémique |
| Consentement explicite à l'inscription des échanges | `statut_rgpd` ; `CORPUS_NON_CONSENTI` |

**Avertissement porté par le rapport, section 2.2.3.1 « L'illusion d'une véritable décentralisation » (p. 119).** Le rapport documente, sur le cas **MakerDAO / Sky**, qu'environ **74 % du pouvoir de vote** se concentrait chez quelques détenteurs, *« reproduisant une gouvernance de fait oligarchique »*. **Une interface de délibération n'est pas un dispositif démocratique par construction.** Toute instance déployée au titre de H.9 déclare sa distribution effective du pouvoir de vote, sans quoi elle produit l'inverse de ce qu'elle affiche.

---

## H.10 Statut juridique et gouvernance du registre

### H.10.1 Recevabilité probante

**La loi PACTE de 2019 ne reconnaît pas aux inscriptions dans un dispositif d'enregistrement électronique partagé (DEEP) une valeur probante**, et le rapport fondateur n'établit rien de tel. Ce qu'il porte :

- **Le régime DEEP** est appliqué par le **décret n° 2018-1226 du 24 décembre 2018** (texte d'application de l'ordonnance, voir (1) ci-dessous), *« relatif à l'utilisation d'un dispositif d'enregistrement électronique partagé pour la représentation et la transmission de titres financiers et pour l'émission et la cession de minibons »*. **Son objet est la représentation et la transmission de titres financiers**, non la valeur probante des inscriptions en général. C'est ce cadre qui a rendu possibles les émissions obligataires sur blockchain publique de Société Générale SFH à partir du 18 avril 2019 — *« la France a d'ailleurs été pionnière à l'échelle mondiale »* (p. 48).
- **La loi PACTE du 22 mai 2019**, dans le rapport, est citée pour **la société à mission** : les objectifs sociaux et environnementaux inscrits aux statuts sont *soumis à vérification* (p. 15). **Rien à voir avec le DEEP.**

**Ce que le registre MRC peut donc revendiquer :** un régime juridique existe pour les titres financiers inscrits en DEEP, et une qualité juridique existe pour les objectifs statutaires soumis à vérification. **Aucun des deux ne confère, par lui-même, une valeur probante aux inscriptions du registre.**

> **(1) Le régime DEEP est ouvert par l'ordonnance, le décret l'applique.** Il est ouvert par l'**ordonnance n° 2017-1674 du 8 décembre 2017**, *relative à l'utilisation d'un dispositif d'enregistrement électronique partagé pour la représentation et la transmission de titres financiers*. Le rapport fondateur ne cite que le décret (p. 48). Le décret n° 2018-1226 du 24 décembre 2018 en est le texte d'application, **entré en vigueur le 27 décembre 2018**.
>
> **(2) Ce qui, en droit français, s'approche le plus d'une « valeur probante », et ce que c'est exactement.** L'ordonnance pose une **règle d'équivalence d'effets** : l'inscription d'un titre financier dans un DEEP, et son transfert par inscription dans ce dispositif, **produisent les mêmes effets juridiques qu'une inscription en compte-titres**. Ce n'est pas une valeur probante générale : c'est une équivalence, **strictement bornée aux titres financiers de l'article L. 211-1 du code monétaire et financier émis en droit français et non admis aux opérations d'un dépositaire central** — donc **à l'exclusion des titres cotés**. Titres de capital, titres de créance et parts d'OPC non cotés sont concernés ; **rien d'autre**.
>
> **(3) Ce que le décret exige du dispositif, et qui intéresse directement le MRC.** L'article **R. 211-9-7 du code monétaire et financier**, créé par le décret, impose que le dispositif soit conçu pour **garantir l'enregistrement et l'intégrité des inscriptions**, **permettre d'identifier les propriétaires ainsi que la nature et la quantité des titres**, comporter un **plan de continuité d'activité actualisé incluant un dispositif externe de conservation périodique des données**, et **fournir au propriétaire un relevé de ses opérations**. **Ces quatre exigences sont une spécification de droit positif d'un registre opposable**, et le MRC n'en porte aujourd'hui aucune équivalente — `[À INSTRUIRE : le plan de continuité et la conservation externe périodique n'ont d'équivalent ni dans l'Annexe H §H.7 ni dans F8.]`
>
> `[GABARIT DÉCLARÉ — DÉCISION DU PORTEUR.]` **Les quatre exigences sont versées comme gabarit, non comme obligation.** `[TRANSPOSITION DÉCLARÉE, NON IDENTITÉ — l'article régit les DEEP de titres financiers non cotés ; le registre MRC n'entre pas dans ce champ ; le gabarit est emprunté pour sa forme et ne confère aucune qualité juridique.]`
>
> | # | Exigence | Équivalent versé | Lacune |
> | :-: | :-- | :-- | :-- |
> | G1 | enregistrement et intégrité des inscriptions | §B.2 borné, propriété 3 ; §H.7 | — |
> | G2 | identification des propriétaires, de la nature et de la quantité des titres | triplet porteur (§H.1.3bis) ; typage P-C-E-D-e-d (NT-ARCH §8.5) | transposition de « propriétaire » à un commun |
> | G3 | plan de continuité actualisé avec conservation externe périodique | **aucun** — §H.7 est une forme possible de conservation, non un plan de continuité | **entière** |
> | G4 | relevé de ses opérations remis au propriétaire | **aucun** | **entière** |
>
> **Champ `gabarit_R211_9_7_Gn`, par exigence :** `SATISFAITE` (+ la **forme** qui l'établit, référencée au sens de §B.2 borné) / `PARTIELLE` (+ forme et manque) / `NON_SATISFAITE` / `SANS_OBJET_MOTIVE` (+ **motif écrit**) / `NONDECLARE` (**refuse**, CONV-9). **Un « sans objet » sans motif est un `NONDECLARE` renommé et est refusé.** Le motif est **réfutable par tout tiers** ; sa réfutation requalifie la valeur en `NON_SATISFAITE`.
>
> **G4 n'admet pas le motif « titulaire non humain ».** Pour un commun non humain, le relevé est remis à **l'instance attributaire déclarée** (NT-ARCH §8.5.6.2bis — fiducie, ORE, ORIC ; pour une fiducie, classe de créance par classe de créance). Faute d'instance déclarée : `NON_SATISFAITE`, jamais `SANS_OBJET_MOTIVE`. *Ancrage PR-31 :* `sans_objet_sans_motif_est_un_nondeclare_renomme`, `le_motif_refute_requalifie`, `G4_n_admet_pas_le_titulaire_non_humain`.
>
> `[PROPOSITION, NON DÉCIDÉE]` Un registre qui revendique l'usage 3 (opposable, NT-ARCH §8.11) affiche avec cette revendication toute exigence `NON_SATISFAITE`.
>
> `[SOURCE]` Libellé des exigences sur sources secondaires concordantes ; texte primaire non lu.
>
> **(4) Loi PACTE.** Loi **n° 2019-486 du 22 mai 2019**, **article 169** (raison d'être, article 1835 du code civil) et **article 176** (société à mission, **articles L. 210-10 à L. 210-12 du code de commerce** ; OTI à l'**article R. 210-21**). **Aucun lien avec le DEEP.**
>
> **Statut du contrôle.** Légifrance est inaccessible (erreur 403 sur les pages du décret et de l'ordonnance). Le contrôle repose sur l'intitulé Légifrance des textes, sur deux analyses d'avocats du décret et de l'ordonnance, et sur l'avis technique de la CNCC pour le volet PACTE. **Les textes primaires n'ont pas été lus.** Les trois sources concordent, dans le sens de la prudence. **Une lecture des textes reste requise avant toute production d'un mémoire juridique** — ce qui n'est pas le régime de cette annexe.

### H.10.2 La société à mission

L'exigence de la loi PACTE — *des objectifs statutaires soumis à vérification par un organisme tiers indépendant* — est **le porteur d'attestation dont le MRC manque partout**. Dans le cas RATP, le bloc financier est couvert par des commissaires aux comptes, le bloc durabilité par **personne**, et `consentement_inscription_NH` n'a aucun titulaire. **Le statut de société à mission fournit un porteur d'attestation légalement institué pour des engagements non financiers.**

> L'avis technique de la CNCC sur l'intervention de l'OTI établit ce que la vérification couvre exactement : l'OTI vérifie la **cohérence** entre objectifs statutaires, raison d'être et activité, **et l'exécution** des objectifs au regard des trajectoires définies ; à ce titre il **vérifie la sincérité des indicateurs**, apprécie les procédures de collecte des données, procède par tests de détail et sondages, et peut vérifier sur site.
>
> **Ce qu'il ne fait pas, et c'est la réserve qui subsiste.** L'intervention est une **assurance modérée**, non raisonnable : l'OTI **ne garantit pas l'exactitude** des indicateurs, il apprécie si les procédures sont appropriées et si les données reflètent fidèlement l'exécution. **Il n'atteste donc pas qu'un valorimètre mesure ce qu'il prétend mesurer** — la question de `source_valuemetre` reste entière — mais il n'est pas non plus un vérificateur purement procédural.
>
> **Et la périodicité borne l'usage.** Vérification **au minimum bisannuelle**, **trisannuelle** sur demande pour les sociétés de moins de 50 salariés ; première vérification dans les **18 mois** de la publication au RCS (24 mois pour les petites structures). **Un porteur qui passe tous les deux ou trois ans ne peut pas attester un flux dMRV continu (H.3) ni un covenant à déclenchement (H.4).** Le couplage donne un porteur pour l'engagement statutaire, pas pour l'inscription courante.
>
> Textes : loi n° 2019-486 du 22 mai 2019, art. 169 et 176 ; code de commerce, art. **L. 210-10 à L. 210-12**, **R. 210-21**, A. 210-1 et A. 210-2 ; code civil, art. 1835 ; **décret n° 2020-1 du 3 janvier 2020** ; **arrêté du 27 mai 2021** (diligences de l'OTI).

> **Ce que la loi institue, et que rien d'autre dans le set n'institue.** L'article **L. 210-10** du code de commerce exige, parmi ses cinq conditions, **un comité de mission distinct des organes sociaux comportant au moins un salarié**, qui présente un **rapport annuel** joint au rapport de gestion ; et une **vérification par un organisme tiers indépendant** dont **l'avis est publié**. L'OTI est **accrédité COFRAC** (ou par un organisme signataire de l'accord de reconnaissance), sa mission dure **six ans**, et il intervient dans les **18 mois** de la déclaration au RCS — 24 mois pour les petites structures — puis **tous les deux ans**, **trois ans** sous 50 salariés.
>
> **La déduction qui décide du couplage : il répond à la question de savoir qui a qualité.** NT-ARCH §8.5.6.4 rend obligatoire la déclaration des instances **DELIBERATIVE** et **CONTROLE** avec leurs porteurs nommés, et se clôt sur *« la règle ne dit pas qui a qualité »*. La société à mission fournit un porteur légalement institué pour deux instances, **et pour la troisième : aucun**.
>
> | Instance (Rochfeld, Cornu & Martin 2021) | Organe | Nature | Périodicité |
> | :-- | :-- | :-- | :-- |
> | **ATTRIBUTAIRE** | **aucun** | — | — |
> | **DELIBERATIVE** | **comité de mission** (au moins un salarié) | interne | **annuelle** |
> | **DE CONTRÔLE** | **OTI accrédité COFRAC**, avis publié | externe | **bisannuelle**, trisannuelle sous 50 salariés |
>
> > **La limite, formulée exactement : la société à mission institue le contrôle d'un engagement dont elle n'institue pas le créancier.** Les objectifs statutaires ne sont dus à personne d'identifié ; seul le juge peut retirer la qualité. En grammaire P-C-E-D-e-d, l'engagement d'une société à mission est un **`E+` dont le miroir est `∅`** — l'asymétrie existentielle, non un `D+` appariant un `C+`.
>
> **Garde (NT-ARCH §8.6) : l'OTI ne peut pas être titulaire de `consentement_inscription_NH`.** Consentir au nom d'un non-humain est un acte **attributaire** — parler pour le bénéficiaire — et non un acte de contrôle. Les confondre serait prendre un vérificateur de procédure pour un porte-parole. `[DÉCOUPLAGE DE RÉGIMES évité, déclaré.]`
>
> **Portée d'une attestation dans le registre.** La périodicité bisannuelle est incompatible avec le flux dMRV continu de §H.3 et avec le covenant à déclenchement de §H.4. Toute attestation déclare donc sa **portée** — `ECRITURE`, `PROCEDURE`, `TRAJECTOIRE` — et sa **périodicité**. **Une attestation de portée `PROCEDURE` ne vaut pas attestation des écritures qu'elle couvre** ; elle vaut attestation que le dispositif qui les produit a été examiné.
>
> **Ce que l'avis établit au regard de l'invariant borné §B.2.** Assurance **modérée** : l'OTI vérifie la **sincérité des indicateurs** et apprécie les procédures de collecte, sans garantir l'exactitude. Il établit donc la **quatrième propriété** — porteur nommé et réfutable — et **partiellement la troisième** ; **il n'établit pas qu'un valorimètre mesure ce qu'il prétend mesurer**, et `source_valuemetre` reste entier.
>
> **L'argument le plus fort — une condition de réfutation *instituée*.** En cas de non-respect, **toute personne intéressée ou le ministère public** peut saisir le tribunal pour faire supprimer la mention de tous les documents de la société, le cas échéant sous astreinte. **Partout ailleurs dans le set, la condition de réfutation est auto-déclarée** ; §9bis reconnaît même que les protections internes ne valent que si un ordre juridique les reconnaît. **Ici l'ordre juridique fournit la procédure et le standing élargi.** `[NUMÉRO D'ARTICLE À CONTRÔLER — L. 210-11 ou L. 210-12 selon les sources secondaires ; texte primaire non lu.]`
>
> **Ce que le couplage ne couvre pas : le cas RATP.** L'EPIC n'est pas une société à mission et ne peut pas l'être. **Pour l'établissement public, le bloc durabilité reste sans porteur d'attestation.**
>
> *Porteur :* porteur MRC / architecte. *Horizon :* institutionnel, révisable. *Critère de vérification :* une chose inscrite comme commun dont l'instance CONTROLE est portée par un OTI nommé et dont l'attestation déclare sa portée et sa périodicité.
>
> **Textes.** Loi n° 2019-486 du 22 mai 2019, art. 169 et 176 ; C. com., art. **L. 210-10 à L. 210-12**, **R. 210-21**, A. 210-1 et A. 210-2 ; C. civ., art. 1835 ; décret n° 2020-1 (janvier 2020) ; arrêté du 27 mai 2021. `[VÉRIFIÉ SUR SOURCES SECONDAIRES CONCORDANTES — Légifrance inaccessible, 403.]`

### H.10.3 Le registre ne remplace pas le notaire — il redistribue ses fonctions

L'authentification de l'identité est assurée par les DID et leurs chaînes d'attestation ; la conservation par le hachage et le stockage adressé. Mais **la qualification juridique** des inscriptions — est-ce un consentement opposable ? une reconnaissance de dette ? — reste l'objet d'actes juridiques, qui peuvent être stockés dans le registre mais requièrent une institution de gouvernance reconnue : GIE, SAS à mission, association dont les statuts précisent le rôle de tiers de confiance, ou notaire dont les actes sont liés au registre par leurs empreintes.

### H.10.4 Représentation des communs non humains

Donner un DID à un bassin versant soulève une question de représentation **que les standards actuels ne résolvent pas**. La réponse pratique est un consortium multi-parties aux règles explicites — qui inscrit quoi, sous quelles conditions, avec quels mécanismes de contestation — formalisé dans les statuts de l'institution de gouvernance. Dans le vocabulaire du set : `legitimiterepresentant` et, quand elle vaut `PRATIQUE` ou `planetaireNonDesignee`, `conditionrefutation` obligatoire.

**eIDAS 2 n'est pas cité ici** : aucune occurrence dans le rapport fondateur, et aucune autre source n'est produite. eIDAS 2 existe et pourrait légitimement figurer ici ; une inférence plausible — un règlement européen d'identité numérique *devrait* concerner un registre fondé sur des identifiants — ne tient pas lieu de source. Règle : *une référence dont aucune source du set ne porte la trace est retirée, même vraisemblable, et sa réintroduction passe par le dépôt d'une source.*

---

## H.11 Extension comptable — couche technique de F8 et registre des capitaux

*Section la plus citée du set — **17 renvois**.*

### H.11.1 Ce que le set lui demande

| Renvoi | Demande |
| :-- | :-- |
| F8 §8.10 | « L'extension H.11 dédiée aux dispositifs comptables CARE — **logiciels certifiés, formats d'export, audits étendus** — accueille la couche technique de F8 » |
| Annexe K §K.6 (cas K2) | « Registre des capitaux numériques : **tableau de bord des capitaux** (humain, sémantique, énergétique) avec calcul automatique du **résultat MRC vs résultat classique** » |
| Annexe K (cas K3) | Inscription de budgets publics en régime comptable public |

### H.11.2 Trois fonctions

**a. Format d'export et d'audit.** Un registre comptable MRC doit être lisible par un tiers sans accès au dispositif qui l'a produit. Exigences minimales : un identifiant stable par écriture ; le régime comptable déclaré (`regime_comptable`) ; l'unité, la précision publiée et le signe ; le contexte — entité, période, axes ; l'empreinte du substrat source.

> **Précédent disponible, et il est hors chaîne.** Le registre de données fiabilisées du groupe RATP 2025 (`PPC/RATP/registre_donnees_fiabilisees_RATP_2025.json`) satisfait ces cinq exigences sans aucun dispositif Web3 : il porte le SHA-256 de ses deux substrats, l'identifiant de balise de chacun de ses 538 faits, leur page, leur unité et leur précision déclarée. **Il démontre que la couche technique de F8 est atteignable par le format et la traçabilité documentaire seuls.** Ce que H.1 à H.7 ajouteraient, c'est la vérifiabilité par un tiers sans confiance dans l'émetteur — pas la traçabilité, qui est déjà là.

**b. Différentiel inter-régimes.** H.11 est l'assiette de `signal_translation_manquante` (F8 §8.9) : le décompte des écritures inscrites en CARE sans traduction disponible en IFRS, c'est-à-dire la mesure de ce que la publication financière dominante efface. **Ce signal n'a aujourd'hui aucune assiette** — zéro cellule `∅` dans la table des traductions de F8 §8.4. **C'est H.11 qui doit la tenir.**

**c. Tableau de bord des capitaux.** Présentation conjointe des capitaux financier, naturel et humain (`compte_actif_CARE`, `compte_passif_CARE`), du `resultat_distribuable` après application de `R-PRIORITE-CREANCIERS`, et du `taux_couverture_DNH`. Le cas K2 ajoute un capital **sémantique** et **énergétique** sans équivalent biophysique direct.

### H.11.3 Ce que H.11 n'est pas

`[GARDE]` H.11 est un dispositif d'**inscription et de restitution**. Elle ne calcule aucun indice agrégé de cohérence, ne classe pas les entités, et ne produit aucun valuemètre de synthèse. Présenter un tableau de bord des capitaux comme une mesure de la performance d'un acteur serait un `[DÉCOUPLAGE DE RÉGIMES]` — la même clause qu'en F8 §8.2bis pour l'agrégation des clôtures.

### H.11.4 Statut

Les 17 renvois de F8 à H.11 désignent, en l'état, **une extension dont seules les exigences sont écrites**.

---

## H.12 Écueils, limites et conditions de réfutation

*Cette section restitue la section 2.2 du rapport fondateur (p. 112-121) : les réserves du rapport, et non ses seules promesses.*

### H.12.1 La dépendance aux oracles

*« L'architecture des registres distribués est conçue pour éliminer le recours aux tiers de confiance ; l'intégration d'oracles réintroduit précisément ce type d'intermédiaire au cœur du dispositif »* (p. 113). Un oracle est un **point de défaillance unique** : capteur défaillant, entité compromise, données falsifiées — et le contrat s'exécute *« automatiquement et sans possibilité d'interruption manuelle »*.

Cas documentés : **IXO Protocol** documente explicitement le risque — si les oracles IA sont biaisés ou un capteur manipulé, *« l'ensemble de la chaîne de financement repose sur une preuve corrompue sans mécanisme d'interruption manuelle »* (p. 113) ; **Arbol**, dont la robustesse a été validée lors de l'ouragan Milton en octobre 2024, *« demeure entièrement dépendant de l'intégrité de ses oracles dClimate et Chainlink »*.

**Conséquence pour le MRC.** Le dMRV de H.3 ne supprime pas la dépendance déclarative : il la déplace vers l'opérateur de l'oracle, qui devient un acteur du registre à part entière — donc porteur d'un DID, d'une VC de conformité, et **d'une condition de réfutation déclarée**.

### H.12.2 La loi de Goodhart — le piège de la donnée

Décrite par **Charles Goodhart en 1975** : toute régularité statistique tend à se rompre dès qu'on exerce sur elle une pression à des fins de contrôle. *« Les acteurs sont poussés à maximiser des métriques facilement quantifiables et tokenisables — le nombre d'arbres plantés pour déclencher un crédit carbone — au détriment d'objectifs plus complexes à mesurer et moins directement monétisables : la préservation de la biodiversité endémique, la qualité des sols sur le long terme, le respect des droits des populations riveraines »* (p. 114). **KlimaDAO** en est l'illustration empirique la plus documentée du rapport.

**Conséquence pour le MRC, et elle est structurante.** `C-CYCLE-PRIX` (F8 §8.8) et l'ensemble des valorimètres de F8 sont exposés à cette distorsion **par construction** : dès qu'un indicateur déclenche un effet financier, il cesse d'être un bon indicateur. Le MRC dispose déjà de l'instrument pour le traiter — `signal_ecologie_superficielle` et `PIEGE_ATTRACTEUR` — mais **rien dans F8 ne relie l'automatisation d'un covenant à ce risque**. Le champ **`hors_champ_optimisation`** (NT-ARCH §8.8, `C-CYCLE-PRIX`) porte ce lien : il est le cinquième élément obligatoire du covenant (§H.4). **Obligatoire dès que le seuil déclenche un effet financier.**

**Pourquoi un champ obligatoire alors que rien ne se déclenche.** Le régime `HARD` et l'Usage 3 sont **PROJETÉS** : aucun covenant du MRC n'exécute aujourd'hui d'effet financier automatique, et le piège de Goodhart — qui se referme sur l'automatisme — n'a donc **aucun objet actuel**. C'est la raison de porter le champ dès à présent : **il ne coûte rien tant qu'aucun covenant n'existe, et son absence coûterait une reprise de tous les covenants le jour où l'Usage 3 s'ouvrirait.**

**Ce que le champ ne fait pas.** Il ne corrige pas le biais et ne prétend pas le mesurer. Il oblige à le **nommer avant qu'il opère** — là où `signal_ecologie_superficielle` et `PIEGE_ATTRACTEUR` ne le signalent qu'après coup. `[DIFFICULTÉ DÉCLARÉE — nommer ce qu'un indicateur laisse hors champ suppose de savoir ce qu'on ne mesure pas. La déclaration sera souvent incomplète ; elle n'est pas pour autant facultative, et son incomplétude est elle-même une information.]`

`[MISE EN GARDE DE MÉTHODE]` *« Numériser un système d'évaluation défaillant ou frauduleux sur une blockchain publique ne corrige pas ces défaillances mais les fige »* (p. 114). **L'inaltérabilité n'est une vertu que sur une donnée juste.**

### H.12.3 L'hyper-financiarisation de la nature

Le rapport consacre sa section 2.2.2 à « la transformation du vivant en actif spéculatif » et aux « limites de la quantification écologique » (p. 115-118). **Cette critique vise directement le geste de H.1.5** : faire du bassin versant un créancier, c'est le faire entrer dans une grammaire financière, et c'est réversible en faire un actif.

C'est aussi le point où le MRC diverge du rapport et doit le dire : la comptabilité CARE inscrit les capitaux naturels **au passif comme dettes à rembourser**, non à l'actif comme ressources valorisables, précisément pour rendre cette réversion impossible. **Le typage `P` d'un commun est interdit ; seul `D` ou `E` lui convient.** `[POINT DE DOCTRINE — à confirmer par le porteur ; il n'est inscrit nulle part comme règle.]`

### H.12.4 Les asymétries de pouvoir

Sections 2.2.3.1 et 2.2.3.2 du rapport : « l'illusion d'une véritable décentralisation » et « le risque de crypto-colonialisme et de green grabbing » (p. 119-121). Voir H.9 pour la première. La seconde vise les dispositifs qui, sous couvert de financer la préservation, transfèrent le contrôle de terres ou de ressources hors des communautés qui en vivent — ce que `droit_exclusion` (F6) et `cloture_declaree` (F8 §8.2bis) permettent d'inscrire, à condition qu'on les renseigne.

### H.12.5 Conditions de réfutation de l'Annexe H

L'annexe tombe, en tout ou partie, dans trois cas :

1. **Si les spécifications ne sont jamais versées.** Une annexe qui décrit des fonctions sans jamais fournir de méthode reste un programme. Si aucune spécification n'est produite d'ici la version suivante, H.5 et H.6 doivent être déclarés **projetés** dans le corps du set, et `HARD` retiré de l'énumération `regime_application`.
2. **Si le déploiement reproduit ce qu'il corrige.** Si, sur un cas instruit, la gouvernance des DID de communs se révèle concentrée comme celle de MakerDAO, l'architecture aura déplacé l'asymétrie sans la réduire.
3. **Si la loi de Goodhart l'emporte.** Si, sur un cas instruit, l'automatisation d'un covenant produit une optimisation d'indicateur au détriment de l'objectif, **c'est le covenant qu'il faut retirer, pas l'indicateur qu'il faut raffiner.**

---

## [LACUNES ET LIMITES DE CETTE ANNEXE]

**Domaines hors de portée vérifiable.** Le rapport fondateur a été lu par extraction de texte ; ses figures et encadrés n'ont pas été examinés visuellement. Les deux points de droit de H.10 sont repris du rapport, **non contrôlés sur les textes**. La numérotation est celle des renvois du set, sur instruction du porteur (H.0.3).

**Inférences non ancrées, déclarées.** Le rattachement des VC aux champs du set (H.2) est une proposition de correspondance : seuls les noms de champs ont été vérifiés présents, pas la pertinence du rattachement. Le choix de la phase `DELIBERATION` en H.5.1 est un choix par défaut. Le point de doctrine de H.12.3 — « le typage `P` d'un commun est interdit » — n'est inscrit nulle part dans le set et est proposé, non établi.

**Ce que le régime procédural ne peut pas résoudre.** L'arbitrage entre permanence et droit à l'effacement (H.7.3) engage un horizon irréversible et appelle une délibération. Enfin, savoir si la mise en commun d'un milieu par sa mise en créancier le protège ou le financiarise (H.12.3) est une question de doctrine, pas de contrôle.

**Statut.** Annexe rédigée par un assistant sur instruction du porteur. `R-INCAPACITE-LLM-VALIDER` s'applique : rien ici n'est validé, tout est proposé.
