#Tupas

#Que son
"""
Son listas inmutables, no se pueden modificar despues de su cracion

No permiten añadir, eliminar, mover elementos
Si permiten extraer porciones, pero el resultado es una tupla nueva
No permiten busquedas (no index)
Si permiten comprobar si un elemento se encuentra en una tupla
"""

#Utilidad o ventajas de las listas
"""
Mas rapidas
Menos espacio (mayor optimizacion)
Formatean strings
Pueden utilizarse como claves de un diccionario
"""

#Sintaxis

#   nombreTupla = (elemento1, elemento2, elemento3,...)
#Indice                0          1          2


miTupla = ("Juan", 13,1,1995,13)

print(miTupla[2])

#Convertir una tupla en una lista con el metodo "list"
#Convertir una lista en tupla con el metodo "tuple"

miLista = list(miTupla)

print(miLista)

#Encontar dentro de una tupla

print("Juan" in miTupla)

#El metodo "count" nos permite aberiguar cuantos elementos se encuentran dentro

print(miTupla.count(13))

#El metodo "len" nos permite aberiguar la longitud de una tupla

print(len(miTupla))

#Tuplas con un unico elemento

miTupla2 = ("Juan",)

print(len(miTupla2))

#Empaquetado de tupla, se pueden hacer las tuplas sin uso de parentesis

miTupla3 = "Juan", 13, 1, 1995

#Desempaquetado ded tupla

miTupla4 = "Juan", 13, 1, 1995

nombre, dia, mes, age = miTupla4

print(nombre)