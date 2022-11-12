#Bucles

#Notaciones especiales con print 

#La funcion de tipo "f" nos perfmiten notar con formatos diferentes con el tipo range

for i in range(5):

    print(f"Valor de la avriable {i}")

for i in range(5,50,3):

    print(f"Valor de la avriable {i}")


valido = False

email = input("Introduce tu email: ")

for i in range(len(email)):

    if email[i] == "@":

        valido = True

if valido:

    print("Email correcto")

else:

    print("Email incorrecto")