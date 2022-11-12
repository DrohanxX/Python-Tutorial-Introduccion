#Bucles

#Instrucciones "continue", "pass", "else"


#Continue
"""
Si un bucle lee esta condicion se saltara todo el procedimiento del bucle hasta el siguiente
"""

for letra in "Python":

    if letra == "h":

        continue #Salto de bucle

    print("Viendo la letra " + letra)


nombre = "Pildoras informaticas"

contador = 0

for i in nombre:

    if i == " ":

        continue

    contador += 1

print(contador)

