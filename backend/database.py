import random
from flask import Flask, jsonify

app = Flask(__name__)

# Base de données pour les éléments de la phrase
data = {
    "adjectives": ["red", "blue", "giant", "tiny", "shiny"],
    "subjects": ["robot", "dragon", "unicorn", "wizard", "alien"],
    "verbs": ["walks", "runs", "flies", "dances", "jumps"],
    "adverbs": ["rapidly", "slowly", "gracefully", "awkwardly", "silently"],
    "locations": ["in a giant forest", "on a distant planet", "through a bustling city", "across a serene lake", "under a starry sky"]
}

@app.route('/generate-theme', methods=['GET'])
def generate_theme():
    # Sélectionner un élément aléatoire de chaque catégorie
    adjective = random.choice(data["adjectives"])
    subject = random.choice(data["subjects"])
    verb = random.choice(data["verbs"])
    adverb = random.choice(data["adverbs"])
    location = random.choice(data["locations"])

    # Construire la phrase
    theme = f"{adjective} {subject} {verb} {adverb} {location}"
    return jsonify({"theme": theme})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)