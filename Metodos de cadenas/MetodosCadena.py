#Metodos de cadenas

#   Uso de metodos de cadenas

#       Se usan en los formularios


#   String

#       upper()
#           Comvierte en mayusculas todas las letras de un string

#       find()
#           representar la posicion de un caracter o un grupo de caracteres

#       split()
#           separa por palabras utilizando espacios

#       lower()
#           pasa a minusculas un string

#       isdigit()
#           devuelve true o false si el valor es un digito o no lo es

#       strip()
#           borrar los epacios sobrantes al principio y al final

#       capitalize()
#           en un string poner la primer letra en mayuscula

#       isalum()
#           comprobar si son alfanumericos

#       replace()
#           cambia una palabra o una letra por otra

#       count()
#           Contar cuantas veces aparece una letra o cadena de caracteres dentro de un string

#       isalpha()
#           comprobar si  hay solo letras

#       rfind()
#           representar el indice de un caracter empezando desde atras

#EJEMPLOS

nombreUsuario = input("Introduce tu nombre: ")

print("El nombre es: ", nombreUsuario.upper())
#                                    .lower()
#                                    .capitalize()

edad = input("Introduce tu edad: ")

print("Edad: ", edad.isdigit())

while(edad.isdigit() == False):

    print("Por favor introduce un valor numerico")

    edad = input("Introduce tu edad: ")

if (int(edad)<18):

    print("No puedes pasar")

else:

    print("Si puedes pasar")