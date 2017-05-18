#Suponga que se tiene un conjunto de calificaciones de un grupo de 40 alumnos. Realizar un 
#algoritmo para calcular la calificación media y la calificación más baja de todo el grupo.
print("Digite las 40 calificaciones")
calificaciones = []
acumulador = 0
for i in range(40):
	calificaciones.append(int(input(">>")))
for i in calificaciones:
	acumulador = acumulador + i
media = acumulador / len(calificaciones)
calificacionBaja = min(calificaciones)
print("La calificación media es de: " + str(media) + " y la calificación más baja es de " + str(calificacionBaja))