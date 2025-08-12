
from flask import Flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Cadena de conexión corregida (asegúrate de que la contraseña sea correcta)
client = MongoClient("mongodb+srv://jtircio2613:Tircio1997@chismografo-cluster.zs0jef5.mongodb.net/?retryWrites=true&w=majority&appName=chismografo-cluster")

db = client["chismografo"]
collection = db["comentarios"]

def create_app():
    app = Flask(__name__)

    from .route import main
    app.register_blueprint(main)

    return app
