import config
config.os.system('clear')

collection = config.db['productos']
documentos = collection.find()

print('Consulta de prueba ...\n\n')

for doc in documentos:
    print("--------------------------------------------------------------")
    print("Nombre: ",doc["nombre"])
    print("Precio: ",doc["precio"])
    print("IVA: ",doc["iva"])
    print("Ganancia: ",doc["ganancia"])
    print("Cantidad: ",doc["cantidad"])
    print("Código: ",doc["codigo"])
    print("ID: ",doc["_id"])

input("\nPresione Enter para volver al menú principal ...")
exit()