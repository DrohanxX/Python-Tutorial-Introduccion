#Las listas

#Que son
"""
Estructura de datos que nos permite almacenar gran cantidad de valores
(equivalentes a los array en otros LP)

En python las listas pueden guardar diferentes tipos de valores

Se pueden expandir dinamicamente añadiendo nuevos elementos
"""

#Sintaxis

#   nombre_lista = [elemento0, elemento1, elemento2,...]

#los elementos de la lista deben de ser localizables, se recurre a un indice empieza desde 0

miLista = ["Maria","Pepe",5,True]
#Indice       0      1        2        3

print(miLista[2])
#Para mostrar todos los valores de la lista seria asi [:]

#Porcion de lista
print(miLista[0:4])

print(miLista[:4])

print(miLista[2:4])

print(miLista[1:])

#Para agregar elementos a la lista se usa "append"
miLista.append("Sandra")

print(miLista[:])

#Para agregar un elemento en medio de la lista se usa "insert"

miLista.insert(2,"Juan")

print(miLista[:])

#Agregar varios elementos a la lista se usa "extend"

miLista.extend(["Ana","Lucia"])

print(miLista[:])

#Devolver el indice de un elmento dentro de una lista usando "index"
#Si hay mas de un elmento igual, este devuelve solo el primer elemento
print(miLista.index(5))

#Funcion que nos dice si encuentra o no un elmento dentro de una lista usando "in"

print("Pepe" in miLista)

#Para eliminar elementos dentro de una lista usando "remove"

miLista.remove("Ana")

print(miLista[:])

#Eliminar el ultimo elemento agregado a una lista usando "pop"

miLista.pop()

print(miLista[:])

#Sumar una lista a una lista

miLista2 = ["Sandra", "Lucia"]

miLista3 = miLista + miLista2

print(miLista3)