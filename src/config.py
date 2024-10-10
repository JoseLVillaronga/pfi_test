import os
import time
import json
import hashlib
######################
# Conexion MongoDB
######################
from pymongo import MongoClient
# Define las credenciales
usuario = 'pfi'
password = 'pfi123'
# Define la URL de conexión 
client = MongoClient(f'mongodb://{usuario}:{password}@localhost:27017/')
# Seleccionar la base de datos
db = client['PFI']
###########
# Login
###########
def loguinMain(user,contra):
    collection = db['usuarios']
    usuario = collection.find_one({"nombre": user})
    if (usuario is not None):
        if (usuario["nombre"] == user):
            if ((usuario["password"] == hashlib.md5(contra.encode()).hexdigest())):
                print("Logueo correcto ...")
                time.sleep(1)
                os.system('clear')
            else:
                os.system('clear')
                print("Logueo incorrecto ...")
                time.sleep(2)
                exit()
        else:
            os.system('clear')
            print("Logueo incorrecto ...")
            time.sleep(2)
            exit()
    else:
        os.system('clear')
        print("Usuario no encontrado ...")
        time.sleep(2)
        exit()