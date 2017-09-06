#Se desea obtener el promedio de g grupos que están en un mismo año escolar; siendo que cada grupo puede 
#tener n alumnos que cada alumno puede llevar m materias y que en todas las materias se promedian tres 
#calificaciones para obtener el promedio de la materia. Lo que se desea desplegar es el promedio de los grupos, 
#el promedio de cada grupo y el promedio de cada alumno.
proGrupos = []
def promedio(total):
	acumulador = 0
	for i in total:
		acumulador = acumulador + i
	promedio = acumulador / len(total)
	return promedio
cantGrupos = int(input("Digite la cantidad de grupos: "))
for i in range(1, cantGrupos+1):
	proAlumnos = []
	print("GRUPO #" + str(i))
	cantAlumnos = int(input("Digite la cantidad de alumnos: "))
	for j in range(1, cantAlumnos+1):
		proMaterias = []
		print("Alumno #" + str(j))
		cantMaterias = int(input("Digite la cantidad de Materias: "))
		for k in range(1, cantMaterias+1):
			notas = []
			print("Notas materia #" + str(k))
			for l in range(1,4):
				notas.append(int(input("Digite la nota # " + str(l) + ": ")))
			proMaterias.append(promedio(notas))
			print("El promedio de la materia es : " + str(promedio(notas)))
		print("El promedio del alumno es : " + str(promedio(proMaterias)))
		proAlumnos.append(promedio(proMaterias))
	print("El promedio del grupo " + str(i) + " : " + str(promedio(proAlumnos)))
	proGrupos.append(promedio(proAlumnos))
print("El promedio de los grupos es de: " + str(promedio(proGrupos)))
