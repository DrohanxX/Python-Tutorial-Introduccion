#POO

#Transladar a codigo los conceptos de POO 

class Coche():

    #Cear un constructor
    # init es el metodo inicial 
    def __init__(self):

        #Establecer propiedades
        #Encapsular usando "__" al iniciar una variable para que no pueda ser modificada desde fuera de la clase
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False
        
    #Establecer comportamiento "metodos"
    #Parametro "self" referencia al objeto perteneciente a la clase
    def arrancar(self,arrancamos):

        self.__enMarcha = arrancamos

        if (self.__enMarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enMarcha and chequeo):

            return "El coche esta en marcha"

        elif ( self.__enMarcha and chequeo == False):

            return "Algo salio mal en el chequeo interno"

        else:

            return "El coche esta parado"

    def estado(self):

        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    #Encapsular un metodo para usar solo desde dentro de la clase
    def __chequeo_interno(self):

        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):

            return True

        else:

            return False

#Instanciar una clase
miCoche = Coche()

#Nomenclatura del punto

print(miCoche.arrancar(True))

print(miCoche.estado())

print("------------Se crea el segundo objeto------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))

print(miCoche2.estado())