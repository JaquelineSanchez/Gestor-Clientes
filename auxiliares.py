#Funciones auxiliares para uso general
import re
import os
import platform

def limpiarPantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def leerTexto(min=0,max=100,mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input(">")
        if min <= len(texto) <=max:
            return texto

def validarDni(dni,lista):
    #validar formato con expresiones regulares
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("El dni no cumple el formato.")
        return False
    #Comprobar que no se repita
    for cliente in lista:
        if cliente.dni == dni:
            print("Ya existe el DNI en otro cliente.")
            return False
    return True
