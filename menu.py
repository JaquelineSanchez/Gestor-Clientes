#Interactuar con la base de datos
import os
import auxiliares
import database as db

def iniciar():
    while True:
        auxiliares.limpiarPantalla()

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

        auxiliares.limpiarPantalla()

        if op == 1:
            print("Listando clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)
            
        elif op == 2:                                
            dni = None
            while True:
                dni = auxiliares.leerTexto(3,3,"DNI (2 int y 1 char):").upper()
                if auxiliares.validarDni(dni,db.Clientes.lista):
                    break                
           
            nombre = auxiliares.leerTexto(2,30,"Nombre:").capitalize()
            apellido = auxiliares.leerTexto(2,30,"Apellido:").capitalize()
            print("Agregando...")    
            db.Clientes.crear(dni,nombre, apellido)
            print("Cliente añadido correctamente...\n")  

        elif op == 3:            
            dni = auxiliares.leerTexto(3,3,"DNI (2 int y 1 char):").upper()
            print("Buscando...\n")
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("No se encontró el cliente.")

        elif op == 4:
            dni = auxiliares.leerTexto(3,3,"DNI (2 int y 1 char):").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:            
                print("Se encontro al cliente:")
                print(cliente)
                print("\nIngresa los datos modificados:")
                nombre = auxiliares.leerTexto(2,30,"Nombre:").capitalize()
                apellido = auxiliares.leerTexto(2,30,"Apellido:").capitalize()
                print("Modificando...\n")    
                db.Clientes.modificar(dni, nombre, apellido)
                print("Cliente modificado correctamente...\n")  
            else:
                print("No se encontró ningun cliente con ese DNI")
        
        elif op == 5:
            dni = auxiliares.leerTexto(3,3,"DNI (2 int y 1 char):").upper()
            print("Buscando...\n")            
            print("Cliente borrado correctamente") if db.Clientes.borrar(dni) else print("No se encontró el cliente.")                        
        
        elif op == 6:
            print("Saliendo...\n")
            break
        else:
            print("Esa opción no existe")
        input("Presiona ENTER para continuar")



        

        