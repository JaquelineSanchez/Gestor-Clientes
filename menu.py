#Interactuar con la base de datos
import os

def iniciar():
    while True:
        os.system('cls')

        print("================================")
        print("Bienvenid@ al Gestor de clientes")
        print("================================")
        print("[1] Listar los clientes")
        print("[2] Agregar un cliente")
        print("[3] Buscar un cliente")    
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente")
        print("[6] Cerrar el Gestor")
        print("================================")
        op = int(input("Elige un número: "))

        os.system('cls')

        if op == 1:
            print("Listando clientes...\n")
            #
        elif op == 2:
            print("Agregando...\n")            
            #
        elif op == 3:
            print("Buscando...\n")
            #
        elif op == 4:
            print("Modificando...\n")
            #
        elif op == 5:
            print("Borrando...\n")
            #
        elif op == 6:
            print("Saliendo...\n")
            break
        else:
            print("Esa opción no existe")
        input("Presiona ENTER para continuar")



        

        