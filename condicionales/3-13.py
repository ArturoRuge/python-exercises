#Una institución educativa estableció un programa para estimular a los alumnos con buen 
#rendimiento académico que consiste en lo siguiente:

ciclo = input("El alumno es de primer ciclo (pc) o segundo ciclo (sc)")
promedio = float(input("Cual es el promedio del alumno? "))

if ciclo == "pc":
	matriculaX5 = 180
	if promedio >= 9.5:
		unidades = 55
		descuento = 25 / 100
	elif promedio >= 9 and promedio < 9.5:
		unidades = 50
		descuento = 10 / 100
	elif promedio > 7 and promedio < 9:
		unidades = 50
		descuento = 0
	elif promedio <= 7:
		materiasRepro = int(input("Cuantas materias reprobo? "))
		if materiasRepro <= 3:
			unidades = 45
			descuento = 0
		else:
			unidades = 40
			descuento = 0
else:
	matriculaX5 = 300
	if promedio >= 9.5:
		unidades = 25
		descuento = 20 / 100
	else:
		unidades = 25
		descuento = 0

matriculaNeta = (matriculaX5 * unidades)
descuentoFinal = matriculaNeta * descuento
matriculaFinal = matriculaNeta - descuentoFinal
print("El descuento es de $" + str(descuentoFinal) + " y la matricula con el descuento es de $" + str(matriculaFinal))

		
		