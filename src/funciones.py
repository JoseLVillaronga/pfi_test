import os
import time
def mostrar_menu():
    print("\nIngrese la opción del menu correspondiente:\n")
    print("1- Ejercicio de la clase 02")
    print("2- Ejercicio de la clase 03")
    print("3- Consulta Productos")
    print("4- Alta producto")
    print("5- Suma producto")
    print("6- Resta producto")
    print("7- Baja producto")
    print("8- Salir de la aplicación")

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
        os.system('python3 src/consulta_add.py')
        os.system('clear')
    elif (opcion == '5'):
        os.system('python3 src/consulta_sum.py')
        os.system('clear')
    elif (opcion == '6'):
        os.system('python3 src/consulta_res.py')
        os.system('clear')
    elif (opcion == '7'):
        os.system('python3 src/consulta_baja.py')
        os.system('clear')
    elif (opcion == '8'):
        print("By by ...")
        exit()
    else:
        print("\n\nOpción no válida. Intente de nuevo.")
        time.sleep(2)
        os.system('clear')