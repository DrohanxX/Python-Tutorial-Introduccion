#Archivos externos II

#   Como trabajar con ficheros externos de texto con el modulo io

#       Punteros en texto

from io import open

#Se puede abrir el archivo de dos fromas tanto escritura como lectura al mismo tiempo udando "r+"
archivo_texto = open("archivo.txt", "r")
#Al abrir el archivo en puntero se ubica al inicio del texto

print(archivo_texto.read())
#Al leer el archivo el puntero se ubicara al final del archivo por tanto si se vuelve a leer este no tendra nada

#El metodo "seek()" nos permitira ubicr el puntero, solo ubicando el numero de caracteres
archivo_texto.seek(0)
#Esto ubicara el puntero al inicio del texto

print(archivo_texto.read())
#Al volver a leerlo este si tendra un valor ya que se regreso el puntero al inicio 

#Al metodo "read" lee hasta donde se indique
