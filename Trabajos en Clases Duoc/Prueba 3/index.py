from ipaddress import ip_address
from funciones import registro, menu, buscardor, impresion_certificados, autoDesctruccion,ya_vali_V

nosequeponer =1

while nosequeponer <2:
    try:
        print("Bienvenido, escoje tu opcion:")
        menu()
        opcion = int(input("ingresa una opcion del menu:\n"))
        if opcion ==1:
            registro()
        elif opcion==2:
            buscardor()
        elif opcion==3:
            impresion_certificados()
        elif opcion==4:
            autoDesctruccion()
            nosequeponer=nosequeponer+2
            print("Gracias por preferirnos")
        elif opcion>=5:    
            ya_vali_V()
            nosequeponer=nosequeponer+2
            print("Gracias por preferirnos")
    except:
        print ("Falla en la Matrix!!!!!!!!")
        nosequeponer=nosequeponer+2
