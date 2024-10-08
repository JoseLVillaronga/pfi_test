#!/usr/bin/env python3
from src import config
config.os.system('clear')

user=str(input("Ingresar usuario: "))
contra=input("Ingresar contraseña: ")

collection = config.db['usuarios']
usuario = collection.find_one({"nombre": user})

if (usuario is not None):
    if (usuario["nombre"] == user):
        if ((usuario["password"] == config.hashlib.md5(contra.encode()).hexdigest())):
            print("Logueo correcto ...")
            config.time.sleep(1)
            config.os.system('clear')
        else:
            config.os.system('clear')
            print("Logueo incorrecto ...")
            config.time.sleep(2)
            #exit()
            print(type(usuario))
    else:
        config.os.system('clear')
        print("Logueo incorrecto ...")
        config.time.sleep(2)
        exit()
else:
    config.os.system('clear')
    print("Usuario no encontrado ...")
    config.time.sleep(2)
    exit()

def mostrar_menu():
    print("\nIngrese la opción del menu correspondiente:\n")
    print("1- Ejercicio de la clase 02")
    print("2- Ejercicio de la clase 03")
    print("3- Consulta de prueba")
    print("4- Salir de la aplicación")

def ejecutar_opcion(opcion):
    if (opcion == '1'):
        config.os.system('python3 src/ejercicio_clase02.py')
        config.os.system('clear')
    elif (opcion == '2'):
        config.os.system('python3 src/ejercicio_clase03.py')
        config.os.system('clear')
    elif (opcion == '3'):
        config.os.system('python3 src/consulta_test.py')
        config.os.system('clear')
    elif (opcion == '4'):
        print("By by ...")
        exit()
    else:
        print("\n\nOpción no válida. Intente de nuevo.")
        config.time.sleep(2)
        config.os.system('clear')

if (__name__ == "__main__"):
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        ejecutar_opcion(opcion)
