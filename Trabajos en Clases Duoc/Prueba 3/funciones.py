from enum import Flag

from datetime import datetime
import random
from datetime import datetime


tipos = []
patentes = []
marcas = []
precios = []
multas_precios = []
multas_fechas = []
duenios = []
registro_autos = []

def menu ():
    print("Automotriz Auto Seguro") 
    print("1.- Grabar")
    print("2.- Buscar")
    print("3.- Imprimir")
    print("4.- Salir")
    
def registro ():
    Flag = False
    while Flag == False:
        tipo = str(input("Ingrese el Tipo de Vehiculo:\n"))
        if tipo == "":
            print("No puede estar vacio")
        else:
            tipos.append(tipo)
            Flag=True
            print("Registro Exitoso")
           # print (tipos)
    Flag = False
###################
    while Flag == False:
        patente = str(input("Ingrese la Patente del Vehiculo:\n"))
        if patente == "" or  len(patente)<2 or len(patente)>15:
            print("Error en la patente")
        else:
            patentes.append(patente)
            Flag=True
            print("Registro Exitoso")
            #print (patentes)
    Flag = False
###################
    while Flag == False:
        marca = str(input("Ingrese la Marca del Vehiculo:\n"))
        if marca == "" or  len(marca)<2 or len(marca)>15:
            print("Error en la Marca")
        else:
            marcas.append(marca)
            Flag=True
            print("Registro Exitoso")
            #print (marcas)        
    Flag = False
###################        

###################
    while Flag == False:
        precio = int(input("Ingrese el Precio del Vehiculo:\n"))
        if precio == None or precio < 5000000:
            print("Error en el precio")
        else:
            precios.append(precio)
            Flag=True
            #print (precios)    
        Flag=False

###################        
        
        while Flag==False:
            duenio = str(input("Ingrese Nombre del Dueño del Vehiculo:\n"))
            if duenio == "":
                print("No puede estar vacio")
            else:
                duenios.append(duenio)
                Flag=True
            print("Registro Exitoso")
            print (duenios)
            multador_costo()
            multador_fecha()
            registradorVehiculos()
        
        
    
def buscardor():
    print("\tBuscador de Vehiculos")
    fpatente = str(input("Ingrese la Patente del Vehiculo a buscar:\n"))    
    for n in patentes:
        if n == fpatente:
            x = patentes.index(n)
            print("para la patente: ",fpatente)
            print("Tipo:\t",tipos[x])
            print("Marca:\t",marcas[x])
            print("Precio:\t",precios[x])
            print("Dueño:\t",duenios[x])
           ## print("Multa:\t",multas_precios[x], "Fecha", multas_fechas[x] )
           ## print("Fecha Registro", registro_autos[x] )
    

def impresion_certificados():
    print("\tImpresion de certificados del vehiculo")
    fpatente = str(input("Ingrese la Patente del Vehiculo a buscar:\n"))    
    for n in patentes:
        if n == fpatente:
            x = patentes.index(n)
            print("para la patente: ",fpatente)
            print("Tipo:\t",tipos[x])
            print("Marca:\t",marcas[x])
            print("Precio:\t",precios[x])
            print("Dueño:\t",duenios[x])
            print("Multa:\t",multas_precios[x], "Fecha", multas_fechas[x] )
            print("Fecha Registro", registro_autos[x] )
            
            
def autoDesctruccion():
    print("\tEliminado Base de Datos")
    print("\t.")
    print("\t..")
    print("\t...")
    tipos.clear
    patentes.clear
    marcas.clear
    precios.clear
    multas_precios.clear
    multas_fechas.clear
    duenios.clear
    registro_autos.clear
    print("\tBase de Datos Eliminada")
    print("\tAdios")

def ya_vali_V():
    print("\t.")
    print("\t..")
    print("\t...")
    print("\tFalla en la Matrix!!!!!!!!.....")
    autoDesctruccion()


def multador_costo ():
        for x in range(1500,3500,1500):
            multas_precios.append(x)
        x=x+1
        
        
def multador_fecha ():        
        inicio = datetime(1999, 1, 30)
        final =  datetime(2022, 5, 28)
        random_date = inicio + (final - inicio) * random.random()
        multas_fechas.append(random_date)
        ##registro_autos.append(random_date)

def registradorVehiculos ():        
        inicio = datetime(1999, 1, 30)
        final =  datetime(2022, 5, 28)
        random_date2 = inicio + (final - inicio) * random.random()
        registro_autos.append(random_date2)