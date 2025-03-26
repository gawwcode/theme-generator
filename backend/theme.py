import random

# Base de données pour les éléments de la phrase
data = {
    "adjectives": ["red", "blue", "giant", "tiny", "shiny"],
    "subjects": ["robot", "dragon", "unicorn", "wizard", "alien"],
    "verbs": ["walks", "runs", "flies", "dances", "jumps"],
    "adverbs": ["rapidly", "slowly", "gracefully", "awkwardly", "silently"],
    "locations": ["in a giant forest", "on a distant planet", "through a bustling city", "across a serene lake", "under a starry sky"]
}

def generate_theme():
    # Sélectionner un élément aléatoire de chaque catégorie
    adjective = random.choice(data["adjectives"])
    subject = random.choice(data["subjects"])
    verb = random.choice(data["verbs"])
    adverb = random.choice(data["adverbs"])
    location = random.choice(data["locations"])

    # Construire la phrase
    return f"{adjective} {subject} {verb} {adverb} {location}"

if __name__ == '__main__':
    theme = generate_theme()
    print("Phrase générée :", theme)