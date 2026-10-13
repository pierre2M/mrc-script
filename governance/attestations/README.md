# Attestations de vérificateurs tiers (phase 4.2)

Une attestation dit qu'une personne **distincte du porteur et du rédacteur** a rejoué, sur sa machine et à partir des
dépôts publiés, le build et l'audit de ProfReg et tous les contrôles de `mrc-script`. Elle porte sur la
reproductibilité technique ; elle ne valide aucune écriture, ne rend rien opposable et ne canonise rien.

1. Le vérificateur clone les dépôts publiés (`pierre2M/mrc-script`, et `pierre2M/ProfReg` dans `mrc-script/profreg`),
   puis lance `tools/attester.sh --verificateur "Prénom Nom"` (avec `--prive <clone>` s'il a accès au dépôt privé du banc).
2. Il signe l'attestation avec **sa** clé : `ssh-keygen -Y sign -f ~/.ssh/<sa_cle> -n mrc-attestation <attestation>.md`.
3. Il transmet au porteur l'attestation, sa signature, les journaux et sa clé publique.
4. Le porteur ajoute la clé à `governance/signataires_autorises` (principal `verificateur-<nom>`, espace de noms
   `mrc-attestation`), verse l'attestation et sa signature ici, et lance `tools/check_attestations.py`
   (signature, clé distincte de celles de l'agent et du validateur, arbre de ProfReg = manifeste, conclusion réussie).

`[RAISONNEMENT AUTORÉFÉRENTIEL évité]` : le rédacteur des dépôts (y compris un assistant IA) ne peut pas attester.
