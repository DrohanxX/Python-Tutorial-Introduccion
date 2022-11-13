#Generadores

#   Que son
"""
Estructuras que extraen valores de una funcion y se almacenan en objetos iterables
(que se pueden reorrer)
Se almacenan de uno en uno
Cada vez que un generador almacena un valor, este permanece en un estado pausado hasta que
se solicita la siguiente, "suspension de estado"
"""

#   Funcionaminento

#La funcion "yield" construye un objeto iterable

#       Funcion tradicional
#       def generarnumeros():
#           return numeros

#       Generador
#       def generarnumeros():
#           yield numeros

#   Que utilidad tienen

#       Son mas eficientes que las funciones tradicionales

#       Muy utiles con listas de valores infinitos

#       Bajo determinados escenarios, sera muy util que un generador  devuelva los valores de uno en uno

#   Cual es su sintaxis

#       Generador
#       def generarnumeros():
#           yield numeros

def generarPares(limite):

    num = 1

    while num < limite:

        yield num * 2

        num = num + 1

devuelvePares = generarPares(10)

print(next(devuelvePares))

print(next(devuelvePares))

print(next(devuelvePares))