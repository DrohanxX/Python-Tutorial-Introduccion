#POO

#   Transladar a codigo los conceptos de POO


class Coche():

    #Establecer propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    #Establecer comportamiento "metodos"
    #Parametro "self" referencia al objeto perteneciente a la clase
    def arrancar(self):

        self.enMarcha = True

    def estado(self):

        if (self.enMarcha):

            return "El coche esta en marcha"

        else:

            return "El coche esta parado"

#Instanciar una clase
miCoche = Coche()

#Nomenclatura del punto
print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")

#miCoche.arrancar()

print(miCoche.estado())