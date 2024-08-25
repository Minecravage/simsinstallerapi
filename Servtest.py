from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)
# Chemin du fichier JSON
MODS_FILE = 'public.json'

# Charger les données depuis le fichier JSON
def load_mods():
    if not os.path.exists(MODS_FILE):
        return {"mods": []}
    with open(MODS_FILE, 'r') as file:
        return json.load(file)

@app.route('/mods', methods=['GET'])
def get_mods():
    data = load_mods()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5001)