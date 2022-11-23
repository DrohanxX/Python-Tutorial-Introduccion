#Interfaz grafica

#   Estrucutura de la ventana en tkinter

#       Raiz (tk)
#           Frame
#               Widgets

#Las extenciones que contengan ventanas deben de terner "pyw"


#importar la libreria tkinter

from tkinter import *

raiz = Tk() #Ceacion de ventana

#Titullo de la ventana
raiz.title("Titulo de la ventana")

#Impedir que se redimensione una ventana
raiz.resizable(0,0)

#Cmabiar icono de la ventana extencion .ico
raiz.iconbitmap("icono.ico")

#Cambiar tamaño de la ventana
raiz.geometry("700x450")

#Metodo config
raiz.config(bg="blue")

#Bucle infinito para poder salir en la pantalla
raiz.mainloop()