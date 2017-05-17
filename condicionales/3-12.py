#Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico determina 
#si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo. 
#Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se determina su resultado 
#como positivo y en caso contrario como negativo. La tabla en la que el médico se basa para obtener el resultado es la 
#siguiente:

nivelHem = int(input("Cual es el nivel de hemogoblina del paciente? "))
unidad = input("El paciente tiene más de un año? (si) (no)")

if unidad == "no":
	edad = int(input("Cuantos meses tiene? "))
	if edad > 0 and edad <= 1:
		rangoMin = 13
	elif edad > 1 and edad <= 6:
		rangoMin = 10
	elif edad > 6 and edad <= 12:
		rangoMin = 11
else:
	edad = int(input("Cuantos años tiene? "))
	if edad > 1 and edad <= 5:
		rangoMin = 11.5
	elif edad > 5 and edad <= 10:
		rangoMin = 12.6
	elif edad > 10 and edad <= 15:
		rangoMin = 13
	else:
		genero = input("Es hombre (h) o mujer (m)? ")
		if genero == "mujer":
			rangoMin = 12
		else:
			rangoMin = 14

if nivelHem < rangoMin:
	print("El paciente sufre de anemia")
else:
	print("El paciente está sano")
