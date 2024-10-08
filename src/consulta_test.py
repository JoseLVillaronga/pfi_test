import config
config.os.system('clear')

collection = config.db['productos']
documentos = collection.find()

print('Consulta de prueba ...\n\n')

for doc in documentos:
    print(doc)

input("\nPresione Enter para volver al menú principal ...")
exit()