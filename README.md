# Calculateur de Rareté de Collection de NFTs

Ce programme est conçu pour calculer les pourcentages de rareté des attributs d'une collection de NFTs (Non-Fungible Tokens). Les NFTs sont des actifs numériques uniques basés sur la technologie de la blockchain.

## Comment ça marche

Le programme lit les données des NFTs à partir du fichier JSON contenant les métadonnées des NFTs. Chaque NFT a une liste d'attributs qui décrivent ses caractéristiques. Le programme parcourt chaque NFT et chaque attribut, puis compte le nombre d'occurrences de chaque combinaison trait_type/value.

Ensuite, il calcule les pourcentages de rareté pour chaque combinaison attribut/valeur en divisant le nombre d'occurrences par le nombre total de NFTs et en multipliant par 100.

Enfin, les résultats sont triés par pourcentage de rareté, du plus bas au plus élevé, et affichés à l'écran.

## Comment utiliser le programme

1. Assurez-vous d'avoir Python installé sur votre machine.
2. Clonez ce dépôt sur votre ordinateur.
3. Placez le fichier JSON contenant les métadonnées de votre collection de NFTs dans le répertoire du projet sous le nom `metadata.json`.
4. Exécutez le programme en exécutant la commande suivante dans votre terminal ou invite de commande:
5. Les résultats affichés indiqueront les pourcentages de rareté de chaque attribut de vos NFTs, triés par rareté croissante.

## Exemple de sortie

Voici un exemple de sortie que vous pourriez obtenir en utilisant ce programme :
Type de trait : Couleur, Valeur : Bleu, Pourcentage : 15.20%
Type de trait : Couleur, Valeur : Rouge, Pourcentage : 25.50%
Type de trait : Couleur, Valeur : Vert, Pourcentage : 10.30%
Type de trait : Forme, Valeur : Carré, Pourcentage : 20.10%
Type de trait : Forme, Valeur : Cercle, Pourcentage : 8.90%
Type de trait : Forme, Valeur : Triangle, Pourcentage : 20.20%
## Avertissement

Assurez-vous de sauvegarder vos données de collection de NFTs avant d'exécuter le programme. Bien que le programme ne modifie pas les données, il est préférable de prendre des précautions supplémentaires pour éviter toute perte accidentelle de données.

## Contribuer

Les contributions sont les bienvenues! Si vous avez des suggestions d'amélioration ou des idées pour étendre les fonctionnalités du programme, n'hésitez pas à ouvrir une pull request.