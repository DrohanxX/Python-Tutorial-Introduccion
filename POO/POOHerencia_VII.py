#Herencia

#   Sobre escritura de metodos

#   Herencia simole y multiple

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

class Furgoneta(Automoviles):

    def carga(self,cargar):

        self.cargado = cargar

        if (self.cargado):

            return "La furgoneta esta cargada"

        else:

            return "La furgoneta NO esta cargada"

#para heredar
class Motocicleta(Automoviles):

    hcaballito = ""

    def caballito(self):

        self.hcaballito = "Voy a hacer el caballito"

    #Sobre escritura de metodo
    def estado(self):

        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena, "\n", self.hcaballito)

class VElectricos(Automoviles):

    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        
        self.autonomia = 100

    def cargarEnergia(self):

        self.cargando = True


#Herencia multiple
#Preferencia a la que se indique primero
class BicicletaElectrica(VElectricos, Automoviles):

    pass

miBici = BicicletaElectrica("Orbea", "HC100")




miMoto = Motocicleta("Honda", "CBR")

miMoto.caballito()

miMoto.estado()


miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))