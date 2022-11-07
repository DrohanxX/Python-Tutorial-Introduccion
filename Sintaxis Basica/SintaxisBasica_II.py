#Tipos, operadores y variables

    #Tipos

        #Numericos

            #Enteros

            #Flotante

            #Complejos
            
        #Textos

        #Booleanos

        #True

        #False


    #Operadores

        #Aritmeticos

            #Suma (+)

                #   5 + 6

                #   resultado es 11  

            #Resta (-)

                #   10 - 5

                #   resultado es 5

            #Multiplicacion (*)

                #   5 * 5

                #   resultado es 25

            #Division (/)

                #   75 / 2

                #    resultado es 37.5

            #Modulo (%) es el resto de una division

                #   10 % 3

                #   resultado es 1
            
            #Exponente (**)

                #   5 ** 3

                #   resultado es 125

            #Division entera (//)

                #   9 // 2

                #   resultado es 4

        #Comparacion

            #igual que (==)

            #Diferente que (!=)

            #Mayor que (>)

            #Menor que (<)

            #Mayor o igual que (>=)

            #Menor o igual que (<=)

        #Logicos

            #AND

            #OR

            #NOT

        #Asignacion

            #Igual (=)

            #Incremento (+=)

            #Decremento (-=)

            #(+=)

            #(/=)

            #(%/)

            #(**=)

            #(//=)

        #Especiales

            #IS

            #IS NOT

            #IN

            #NOT IN

""" Variable
Espacio en memoria del ordenador donde se almacena un valor que podria cambiar
durante la ejecucion del programa.
Para declarar las variables debe empezar por una letra
"""

#Funciones

"""
    type()
    devuleve el tipo de dato o tipo de variable
"""
nombre = "Johan"

print(type(nombre))

"""
    if
    permite evaluar 2 o mas condiciones
"""
numero1 = 5
numero2 = 7

if numero1 > numero2:
    print("El numero 1 es mayor")
else:
    print("El numero 2 es mayor")
