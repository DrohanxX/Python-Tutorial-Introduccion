#Condicionales

#Switch

#En python no existe, pero nos ofrece diferentes formas de hacer algo similar

#Concatenacion de operadores de comparacion

print("Ingresos")

salario_P = int(input("Introduce el salario del presidente: "))

salario_D = int(input("Introduce el salario del director: "))

salario_JA = int(input("Introduce el salario del jefe de area: "))

salario_A = int(input("Introduce el salario del administrativo: "))

print("Salario del presidente: " +  str(salario_P))

print("Salario del director: " +  str(salario_D))

print("Salario del jefe de area: " +  str(salario_JA))

print("Salario del administrativo: " +  str(salario_A))

if salario_A < salario_JA < salario_D < salario_P:

    print("Todo esta bien")

else:

    print("Algo esta fallando")

#Operadores logicos "and" y "or"

print("Becas")

DA = int(input("Introduce la distancia de tu casa a la escuela: "))

NH = int(input("Introduce el numero de hermanos: "))

SF = int(input("Introduce tu salario anual: "))

if DA > 40 and NH > 2 or SF <= 20000:

    print("Tienes derecho a beca")

else:

    print("No tienes derecho a beca")

#Operador "in"

#Para solucionar las mayusculas y minusculas se utiliza "lower()" "upper()"

print("Asignaturas")

print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

opcion = input("Escribe la asignatura escogida:")

asignatura = opcion.lower() #Transforma el texto a minusculas

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):

    print("Asigantura elegida: " + asignatura)

else:

    print("La asignatura: " + asignatura + "No esta contemplada")
