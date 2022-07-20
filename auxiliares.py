#Funciones auxiliares para uso general
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
