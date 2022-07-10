from operator import index
from os import system
import time
ruts = []
nombres = []
direcciones = []
comunas = []
correos = []
edades = []
celulares = []
flag = True
while flag == True:
    time.sleep(2)
    print("BIENVENIDOS A SISTEMA DE COMPRA")
    print("1. REGISTRAR CLIENTE")
    print("2. CONSULTAR DATOS CLIENTE")
    print("3. REGISTRO DE PEDIDO")
    print("4. CHEQUEAR PEDIDO")
    print("5. SALIR")
        
    try:
            op = int(input("Seleccion una opción\n"))
            if op == 1:
                print("REGISTRAR CLIENTE")
                rut = input("Ingrese rut sin puntos ni guión\n")
                ruts.append(rut)
                nombre = input("Ingrese nombre\n")
                nombres.append(nombre) 
                direccion = input("Ingrese dirección\n")
                direcciones.append(direccion)
                comuna  = input("Ingrese comuna\n")
                comunas.append(comuna) 
                correo = input("Ingrese correo\n")
                correos.append(correo)
                edad = int(input("Ingrese edad\n"))
                edades.append(edad)
                celular = int(input("Ingrese celular 9 digitos sin el +56"))
                celulares.append(celular)
            if op == 2:
                print("CONSULTAR DATOS CLIENTE")
                busca_rut = input("Ingresa rut a consultar")
                for n in ruts:
                    if n == busca_rut:
                        x = ruts.index(n)
                        print(f"rut: {ruts[x]}")
                        print(f"nombre: {nombres[x]}")
                        print(f"direccion: {direcciones[x]}")
                        print(f"comuna: {comunas[x]}")
                        print(f"correo: {correos[x]}")
                        print(f"edad: {edades[x]}")
                        print(f"celular: {celulares[x]}")
 
            if op == 3:
                print("REGISTRO DE PEDIDO")
            if op == 4:
                print("CHEQUEAR PEDIDO")
            if op == 5:
                continuar = int(input("DESEA SALIR?\n1. Si?\t2. No\n"))
                if continuar == 1:
                    print("Muchas gracias por visitarnos")
                    flag = False
      

    except :
            system("cls")#--->para sistema windows #system("clear")--->para linux(ubuntu, mac, etc)
            print("Oops!  Este sistema acepta solo numeros...")