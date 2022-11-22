# primero se importa el modulo "io"

#open es para abrir un archivo externo
from io import open

#Se puede abrir en varios modos "lectura", "escritura", "append"
#Crea un archivo con el nombre y lo pone en la ruta raiz del programa
archivo_texto = open("archivo.txt", "a")

"""
#variable con el texto a incluir 
frase = "Estupendo dia para estudiar python \n el lunes"

#Incluir el contenido de la variable en el archivo
archivo_texto.write(frase)

#Por ultimo se debe de cerrar el archivo usando "close"
archivo_texto.close()
"""

#Para  leer informacion de ese archivo previamente creado se usa "r"
#texto = archivo_texto.read()

#Metodo "readlines()" lo que nos hace hacer es leer lo que hay en linea a linea en una lista
#Ahora tenemos lo escrito en un archivo en una lista maniulable
"""
lineas_texto = archivo_texto.readlines()

#Se cierra el archivo
archivo_texto.close()

#print(texto)

print(lineas_texto[0])
"""

#Para añadir texto al archivo se usa "a"

archivo_texto.write("\n no siempre es una buena ocassion para estuidar python")

archivo_texto.close()