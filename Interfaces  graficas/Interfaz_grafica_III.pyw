#Interfaz grafica

#   Creacion de interfaz grafica

#       Widgets label

#Label

#   Nos permiten mostrar texto o imagenes

#   Tienen como unica finalidad mostrar texto, no se interactua con el

from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)
miFrame.pack()

#Creacion de label con texto
miLabel = Label(miFrame, text="Hola a todos",fg="red", font=(18))
#El metodo "place nos permite ubicar por cordenadas x y"
miLabel.place(x=100, y=200)

#Imagen en un label
miImagen = PhotoImage(file="8RDg.gif")
Imagen = Label(miFrame, image=miImagen).place(x=50,y=100)

root.mainloop()