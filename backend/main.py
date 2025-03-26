from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from database import init_db, get_random_item
import os

app = Flask(__name__, static_folder=os.path.abspath('../frontend'))
CORS(app)

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/generate', methods=['GET'])
def get_theme():
    theme = generate_theme()
    return jsonify({"theme": theme})

def generate_theme():
    erso_data = get_random_item("personnages")  # (nom, nombre)
    perso, nombre = perso_data
    adj_sujet = get_random_item("adjectifs_sujet")
    action = get_random_item("actions")
    adv = get_random_item("adverbes")
    lieu = get_random_item("lieux")
    adj_lieu = get_random_item("adjectifs_lieu")

    article = "a" if nombre == "singulier" else "the"
    phrase = f"{article} {adj_sujet} {perso} {action} {adv} in a {adj_lieu} {lieu}"
    return f"{phrase}"

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=8080)