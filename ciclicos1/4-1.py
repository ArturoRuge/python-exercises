#Calcular el promedio de un alumno que tiene 7 calificaciones en la materia Laboratorio.

print("Ingrese las 7 calificaciones del alumno")
calificaciones = []
acumulador = 0
for i in range(7):
	calificaciones.append(float(input(">>")))
for i in calificaciones:
	acumulador = acumulador + i
promedio = acumulador / 7
print("El promedio es de " + str(round(promedio,2)))

