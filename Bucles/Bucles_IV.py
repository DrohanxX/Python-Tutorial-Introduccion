import math

#Bucles

#Bucle while

#Sintaxis

#       While condicion:

#           cuerpo del bucle

i = 1

while i <= 2:

    print(f"Ejecucion {i}")

    i = i + 1

print("Termino la condicion")

edad = int(input("Introduce la edad: "))

while edad < 0:

    print("Has introducido una edad incorrectas")

    edad = int(input("Introduce la edad correcra: "))

print("Acceso autorizado, edad: " + str(edad))



print("Calculo de raiz cuadrada")

numero = int(input("Introduce un numero: "))

intentos = 0

while numero < 0:

    print("No se puede hallar la raiz cuadrada de un numero negativo")

    if intentos == 2:

        print("Has consumido demasiados intentos. Finalizara el programa")

        break;  #Salir del bucle

    numero = int(input("Introduce un numero: "))

    if numero < 0:

        intentos = intentos + 1

if intentos < 2:

    solucion = math.sqrt(numero)

    print("La raiz cuadrada de: " + str(numero) + " es " + str(solucion))