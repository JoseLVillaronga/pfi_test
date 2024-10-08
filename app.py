#!/usr/bin/env python3
from src import config
config.os.system('clear')

def mostrar_menu():
    print("\nIngrese la opción del menu correspondiente:\n")
    print("1- Ejercicio de la clase 02")
    print("2- Ejercicio de la clase 03")
    print("3- Consulta de prueba")
    print("4- Salir de la aplicación")

def ejecutar_opcion(opcion):
    if opcion == '1':
        config.os.system('python3 src/ejercicio_clase02.py')
        config.os.system('clear')
    elif opcion == '2':
        config.os.system('python3 src/ejercicio_clase03.py')
        config.os.system('clear')
    elif opcion == '3':
        config.os.system('python3 src/consulta_test.py')
        config.os.system('clear')
    elif opcion == '4':
        print("By by ...")
        exit()
    else:
        print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        ejecutar_opcion(opcion)
