import os
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