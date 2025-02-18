from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Requête reçue avec succès !"})
    
if __name__ == '__main__':
    app.run(debug=True)