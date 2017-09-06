
#8. Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos.
cantAlumnos = int(input("Ingrese la cantidad de alumnos que hay en el salón "))
mujeres = 0
hombres = 0
edadMujeres = 0
edadHombres = 0
for i in range (1,cantAlumnos+1):
	genero = input("Género (m) o (f) del alumno " + str(i) + " ")
	if genero == "m":
		hombres = hombres + 1
		edad = int(input("Digite la edad "))
		edadHombres = edadHombres + edad
	else:
		mujeres = mujeres + 1
		edad = int(input("Digite la edad "))
		edadMujeres = edadMujeres + edad

promedioM = edadMujeres / mujeres 
promedioH = edadHombres / hombres
promedio = (promedioM + promedioH) / 2
print("El promedio de edad de los hombres es de: " + str(promedioH) + " años, el de mujeres es de: " + str(promedioM) + " años y el promedio general del grupo es de: " + str(promedio) + " años")

