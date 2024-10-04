#!/usr/bin/env python3
import os

def mostrar_menu():
    print("\nIngrese la opción del menu correspondiente:\n")
    print("1- Ejercicio de la clase 02")
    print("2- Ejercicio de la clase 03")
    print("3- Salir de la aplicación")

def ejecutar_opcion(opcion):
    if opcion == '1':
        os.system('python3 src/ejercicio_clase02.py')
    elif opcion == '2':
        os.system('python3 src/ejercicio_clase03.py')
    elif opcion == '3':
        print("By by ...")
        exit()
    else:
        print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        ejecutar_opcion(opcion)
