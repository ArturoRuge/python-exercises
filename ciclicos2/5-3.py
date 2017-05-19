#Determinar cuántos hombres y cuantas mujeres se encuentran en un grupo de n personas, 
#suponiendo que los datos son extraídos alumno por alumno.

cantAlumnos = int(input("Cuantos alumnos hay en la clase? "))
alumnos = []
hombres = 0
mujeres = 0
for i in range (1, cantAlumnos + 1):
	alumnos.append(input("El alumno # " + str(i) + " es hombre(h) o mujer(m) "))
for i in alumnos:
	if i == "h":
		hombres = hombres + 1
	else:
		mujeres = mujeres + 1
print("En el curso hay " + str(hombres) + " hombres y " + str(mujeres) + " mujeres")

