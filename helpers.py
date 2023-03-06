import re 
import os
import plataform

def liampiar_pantalla():
    os.system('cls') if plataform.system() =="Windows" else os.system('clear')

def leer_texto(longitud_min=0, longitud_max=50,mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(mensaje)>= longitud_min and len(mensaje)<=longitud_max
        return texto

def bastidor_valido(bastidor,vehiculo):
    if not re.match('[0-9]{2}[A-Z]$',bastidor):
        pritn("Bastidor incorrecto, debe cumplir el formato.")
        return false
    for vehiculos in vehiculo:
        if vehiculos.bastidor==bastidor:
            print("Bastidor utilizado por otro unsuario")
            return false

    return True
