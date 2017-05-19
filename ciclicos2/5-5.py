#5. Obtener el promedio de calificaciones de un grupo de n alumnos.
cantAlumnos = int(input("Digite la cantidad de alumnos: "))
calificacion=[]
contador = 0
for i in range(1, cantAlumnos +1):
	calificacion.append(int(input("calificacion estudiante " + str(i) + " ")))
for i in calificacion:
	contador = contador + i
promedio = contador / len(calificacion)
print("El promedio de calificaciones del grupo es de: " + str(promedio))