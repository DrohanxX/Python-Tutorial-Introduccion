#Diccionarios

#Que son
"""
Estructura de datos que nos permite almacenar valores de diferente tipo (enteros, cadena de
texto, decimales) e incluso listas, tuplas y otros diccionarios

La principal caracteristica de los diccionarios es que los datos se almacenan asociados a una
clave de tal forma que se crea una asociasion de tipo "clave:valor" para cada elemento almacenado

Los elementos almacenados no estan ordenados, el orden es indiferente a la hora de almacenar 
informacion en un diccionario
"""

miDiccionario = {"Alemania":"Berlin","Francia":"Paris","Reino unido":"Londres","España":"Madrid"}

print(miDiccionario["Alemania"])

#Agregar elementos a un diccionario

miDiccionario["Italia"] = "Lisboa"

print(miDiccionario)

#Modidicar una clave de dun diccionario

miDiccionario["Italia"] = "Roma"

print(miDiccionario)

#Eliminar elementos de un diccionario con el metodo "del"

del miDiccionario["Reino unido"]

print(miDiccionario)

#Añadir una tupla a un diccionario


miTupla = ["España", "Francia", "Reino unido", "Alemania"]

miDiccionario2 = {miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlin"}

print(miDiccionario2)

#Almacenar una tupla entera

miDiccionario3 = {23:"Jordan", "nombre":"Michael", "equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}

print(miDiccionario3["anillos"])

#Almacenar un diccionario dentro de otro diccionario

miDiccionario4 = {23:"Jordan", "nombre":"Michael", "equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}

print(miDiccionario4["anillos"])

#El metodo "keys" nos devuelve las claves de un diccionario

print(miDiccionario4.keys())

#El metodo "values" obtenemos los valores de un diccionario

print(miDiccionario4.values())

#Longitud de dicciknario usando "len"

print(len(miDiccionario4))