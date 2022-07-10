#lista es una agrupacion de datos po varios datos dentro de una lista
lista_marvel = ["Iron Man","Thor","Captain America","The Avengers","Guardians of the Galaxy","Ant-Man","Doctor Strange","Spider-Man","Black Panther","Black Widow"]

largo_lista = len(lista_marvel)# obteniendo el largo de la lista 

print ("lista 1:",lista_marvel)
print ("Elementos en la lista:",largo_lista)

ultima = lista_marvel[9]# almacenando el ultimo elemento en la lista en una variable
print ("Ultimo elmento de la lista 1:",ultima)
print ("Ultimo elmento de la lista 1:",lista_marvel[9])# imprimiendo el ultimo elemento de la lista

#POP
# el metodo pop en una lista sirve para eliminar el ultimo elemento de lista
lista_marvel2 = ["Iron Man","Thor","Captain America"]
print ("lista 2:",lista_marvel2)
largo_lista2 = len(lista_marvel2)# obteniendo el largo de la lista 
print ("Elementos de la lista2:",largo_lista2)
lista_marvel2.pop()
largo_lista2 = len(lista_marvel2)# obteniendo el largo de la lista 
print ("Lista 2, luego del POP:",lista_marvel2)
print ("Elementos de la lista 2, luego del POP:",largo_lista2)