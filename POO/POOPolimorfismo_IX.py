#Polimorfismo

#   Objeto

#       Puede cambiar de forma depeniendo el contexto (cambia su comportamiento)


class Coche():

    def desplazamiento(self):

        print("Me desplazo utilizando 4 ruedas")


class Moto():

    def desplazamiento(self):

        print("Me desplazo utilizando 2 ruedas")


class Camion():

    def desplazamiento(self):

        print("Me desplazo utilizando 6 ruedas")


#Polimorfismo

def desplazamientoVehiculo(vehiculo):

    vehiculo.desplazamiento()

miVehiculo = Camion()

desplazamientoVehiculo(miVehiculo)