#En una escuela privada la matrícula de los alumnos se determina según el número de materias que cursan. 
#El costo de todas las materias es el mismo. Se ha establecido un programa para estimular a los alumnos, 
#el cual consiste en lo siguiente: si el promedio obtenido por un alumno en el último período es mayor o igual que 9, 
#se le hará un descuento del 30% sobre la matrícula y no se le cobrará I.V.A.; si el promedio obtenido es menor que 9 
#deberá pagar la matrícula completa, la cual incluye el 10% de IVA. Obtener cuánto debe pagar un alumno.

costoMateria = int(input("Digite el costo por materia: "))
numMaterias = int(input("Cuantas materias cursará el alumno: "))
promedioAnterior = int(input("Promedio del alumno en el último periodo: "))
matricula = costoMateria * numMaterias

if promedioAnterior >= 9:
	matriculaFinal = matricula - (matricula * 0.3)
	iva = "0%"
else:
	matriculaFinal = matricula + (matricula * 0.1)
	iva = "10%"

print("El costo de la matricula es de: $" + str(round(matriculaFinal)) + " con un IVA del " + iva)


