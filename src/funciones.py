import os
import time
def mostrar_menu():
    print("\nIngrese la opción del menu correspondiente:\n")
    print("1- Ejercicio de la clase 02")
    print("2- Ejercicio de la clase 03")
    print("3- Consulta de prueba")
    print("4- Salir de la aplicación")

def ejecutar_opcion(opcion):
    if (opcion == '1'):
        os.system('python3 src/ejercicio_clase02.py')
        os.system('clear')
    elif (opcion == '2'):
        os.system('python3 src/ejercicio_clase03.py')
        os.system('clear')
    elif (opcion == '3'):
        os.system('python3 src/consulta_test.py')
        os.system('clear')
    elif (opcion == '4'):
        print("By by ...")
        exit()
    else:
        print("\n\nOpción no válida. Intente de nuevo.")
        time.sleep(2)
        os.system('clear')