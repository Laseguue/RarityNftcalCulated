import json
from collections import defaultdict

# Load the JSON file
with open("build/json/_metadata.json", 'r') as f:
    donnees = json.load(f)

# Initialiser un dictionnaire pour stocker les comptages
comptages = defaultdict(int)

# Compter le nombre total de NFTs
total_nfts = len(donnees)

# Parcourir chaque NFT
for nft in donnees:
    # Parcourir chaque attribut
    for attribut in nft['attributes']:
        # Incrémenter le comptage pour cette combinaison trait_type/value
        comptages[(attribut['trait_type'], attribut['value'])] += 1

# Calculer les pourcentages
pourcentages = {(trait_type, value): (comptage / total_nfts) * 100
               for (trait_type, value), comptage in comptages.items()}

# Trier les résultats par pourcentage
pourcentages_tries = sorted(pourcentages.items(), key=lambda item: item[1])

# Afficher les résultats
for (trait_type, value), pourcentage in pourcentages_tries:
    print(f'Type de trait : {trait_type}, Valeur : {value}, Pourcentage : {pourcentage:.2f}%')
