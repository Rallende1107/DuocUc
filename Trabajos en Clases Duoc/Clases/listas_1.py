#clear
lista3.clear()#Clear limpia o vacia la lsita
print (lista3)

#copy
lista4 =[1,2,3,4] 
lista5 =lista4.copy()#Crea una copia de la lista en otra varible tipo lista
lista4.append("Rene")#modificando la lista luego de crear una copia de ella
print (lista4, lista5)
#Al modificar la lista 3 con un append la lista 4 quedara sin esa modificacon-.

#count
#Count cuenta los elementos ingresados dentro de la lista.-
lista2 =[1,2,3,4] #si se declara una variable y esta se inicializa y luego se le pasan mas valores. se sobree escribiran
lista4 =[1,2,3,4] 

print (lista2, lista4.count(4), lista4.count(5))


#Acceder a un alemento cuenta desde el indice 0

lista6 =['Rene',2,3,'Allende'] 

print (lista6[0])
