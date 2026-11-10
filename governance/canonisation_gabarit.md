# Gabarit — décision de canonisation limitée (phase 4.3)

*Gabarit, non adopté. La décision est **inscrite au registre pilote** (journal et `_ETAT_INSCRIPTION`), pas seulement
dans ce dépôt : un dépôt ne se déclare pas canonique lui-même. Le texte de la formule de canonisation (la note du
02/10/2026, clauses 1 à 9) est à reprendre ici à l'adoption.*

## 1. Instance qui adopte
- Instance (D13, 09/10/2026) : **P. M. (porteur du registre pilote) et J.-S. M. (vérificateur tiers), conjointement** ; adoption à deux voix concordantes ; date : `[…]`.
- Préalable : attestation de J.-S. M. versée dans `governance/attestations/` et contrôlée par `tools/check_attestations.py` sur l'arbre canonisé.

## 2. Objet canonisé (version immuable)
| Objet | Empreinte |
| --- | --- |
| Set MRC v5.7 (empreinte globale du manifeste) | `53cf46738edf1db3375e8091b5f9d327be9bb12ed493ed40b0634a627e29b9d2` |
| NT-ARCH v5.7 | `1f365c94c83f5bc70d8eac8c1aa7c7bd77efcf564c26d55c1cbac383d54f839f` |
| ProfReg (arbre git publié) | `48ab6c29f011048c12c1558f9413a3a064345a22` |
| mrc-script (arbre git publié ; D11 : pas de tag) | `[arbre attesté, relevé à l'adoption]` |
| Attestation du vérificateur tiers (D12 : J.-S. M.) | `[nom du fichier]`, signée `verificateur-jsm` |

## 3. Portée
- Limitée au **pilote C** (écriture duale entre teneurs) et au **registre pilote**. Ne vaut pour aucun autre registre.
- Ce qui est canonisé : la référence de contrôle (règles, vérificateur déterministe, état de ProfReg). **Aucune écriture
  n'est rendue opposable** par la canonisation ; l'opposabilité relève de la gouvernance de chaque registre.

## 4. Durée
- Date d'effet : `[…]`. **Date d'expiration : `[…]`** (au plus tard : `[…]`). Réexamen avant expiration.

## 5. Conditions de suspension (réfutation)
La canonisation est suspendue de plein droit, et la suspension inscrite au registre, si :
1. une attestation de vérificateur tiers ultérieure, signée, conclut à un échec sur le même objet ;
2. l'une des empreintes du §2 ne correspond plus à l'état publié ;
3. une contestation est jugée fondée selon la voie du §3 de `registre_pilote.md` ;
4. une règle du pilote est modifiée (nouvelle décision de porteur) sans nouvelle canonisation.

## 6. Voie de contestation
- Celle de `governance/registre_pilote.md` §3. Limite déclarée : sans tiers de contestation, la voie n'est pas indépendante.

## 7. Inscription
- Registre pilote : `[référence de l'inscription]` ; journal `_ETAT_INSCRIPTION_v5.7.md` : `[date]`.
