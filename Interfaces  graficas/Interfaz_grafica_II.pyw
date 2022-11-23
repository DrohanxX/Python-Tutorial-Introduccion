#Interfaz grafica

#   Crear frame y su configuracion

#       El frame deberia ser el contenedor de los widgets

from tkinter import *

raiz = Tk() #Ceacion de ventana

#Titullo de la ventana
raiz.title("Titulo de la ventana")

#Impedir que se redimensione una ventana
raiz.resizable(0,0)

#Cmabiar icono de la ventana extencion .ico
raiz.iconbitmap("icono.ico")

#Cambiar tamaño de la ventana
#raiz.geometry("700x450")

#Metodo config
raiz.config(bg="blue")

#Se crea el frame
miFrame = Frame()

#Se debe de empacar el frame
miFrame.pack()

#Para ver el frame se usara el metodo config para cambiar sus caracteristicas
miFrame.config(bg="red")

#Se dara el tamaño que tenia "raiz"
miFrame.config(width="650", height="350")

#Cambiar las caracteristicas del borde
miFrame.config(bd=35)
miFrame.config(relief="groove")

#Cambiar el incono del cursor al pasar por un frame
miFrame.config(cursor="hand2")

#Bucle infinito para poder salir en la pantalla
raiz.mainloop()