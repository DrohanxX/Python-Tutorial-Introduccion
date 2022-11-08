#Conicionales

#Instruccion if
print("Evaluacion de notas")

NotaAlumno = int(input("Escribe la nota del alumno: "))


def evaluacion(nota):

    valoracion = "Aprobado"

    if nota < 5:

        valoracion = "suspenso"

    return valoracion

print(evaluacion(NotaAlumno))