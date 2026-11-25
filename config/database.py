import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database

load_dotenv()


def get_database() -> Database:
    """Crea y devuelve la conexión a la base de datos en MongoDB Atlas."""
    mongo_uri = os.getenv("MONGO_URI")
    db_name = os.getenv("DB_NAME", "BuscadorEmpleos")

    if not mongo_uri:
        raise ValueError("Falta configurar MONGO_URI en las variables de entorno.")

    client = MongoClient(mongo_uri)
    return client[db_name]


def get_collections():
    """Devuelve las colecciones principales del proyecto."""
    db = get_database()
    return {
        "usuarios": db["usuarios"],
        "vacantes": db["vacantes"],
    }
