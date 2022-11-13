#Generadores

#   Instruccion "yield from"

#   Utilidad

#       Simplicar el codigo de los generadores en el caso de utilzar bucles anidados


#Cuando se coloca "*" delante del argumento de funcion, se indica que recibira un numero indetermiando de elementos de una tupla

def devuelve_ciudades(*ciudades):

    for elemento in ciudades:

        #for subElemento in elemento:

            yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))