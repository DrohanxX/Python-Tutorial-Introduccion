#Bucles 

#Bucle for

#Recorriendo strings

#Tipo range

#Notaciones especiales con print

#El argumento "end" determinara como terminara la impresion 

for i in ["Pildoras","Informaticas",3]:

    print("Hola", end=" ") #Pone todo sobre la misma linea

#Recorrer caracter por paracter de un string

for i in "johancacerez":

    print("Hola", end=" ")

#Comprobacion de correo electronico

contador = 0

miemail = input("\n Introduce tu direccion de email: ")

for i in miemail:

    if (i == "@" or i == "."):

        contador = contador + 1

#Para simplicicar una variable boolena y comrpobarla
#if email:

if contador == 2:

    print("\n email correcto")

else:

    print("\n email incorrecto")

