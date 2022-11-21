#Herencia

#   Que es

    #   

#   Para que sirve

#       para reutilizar codigo en caso de crear objetos similares
#       que caracteristicas tienen en comun?
#       que comportamientos en comun tienen todos los objetos?

#   Como hacer que las clases hereden

class Automoviles:

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = True

    def acelerar(self):

        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):

        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena)

#para heredar
class Motocicleta(Automoviles):

    pass

miMoto = Motocicleta("Honda", "CBR")

miMoto.estado()