#POO

#Transladar a codigo los conceptos de POO 

class Coche():

    #Cear un constructor
    # init es el metodo inicial 
    def __init__(self):

        #Establecer propiedades
        self.largoChasis = 250
        self.anchoChasis = 120
        #Encapsular usando "__" al iniciar una variable para que no pueda ser modificada desde fuera de la clase
        self.__ruedas = 4
        self.enMarcha = False
        
    #Establecer comportamiento "metodos"
    #Parametro "self" referencia al objeto perteneciente a la clase
    def arrancar(self,arrancamos):

        self.enMarcha = arrancamos

        if (self.enMarcha):

            return "El coche esta en marcha"

        else:

            return "El coche esta parado"

    def estado(self):

        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)

#Instanciar una clase
miCoche = Coche()

#Nomenclatura del punto

print(miCoche.arrancar(True))

print(miCoche.estado())

print("------------Se crea el segundo objeto------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))

#Cambiar propiedades de una clase de un objeto
miCoche2.__ruedas = 2

print(miCoche2.estado())