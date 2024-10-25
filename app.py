#!/usr/bin/env python3
from src import config
from src import funciones
config.os.system('clear')

user=str(input("Ingresar usuario: "))
contra=config.getpass.getpass("Ingresar contraseña: ")

config.loguinMain(user,contra)

while True:
    funciones.mostrar_menu()
    opcion = input("\nSeleccione una opción: ")
    funciones.ejecutar_opcion(opcion)
