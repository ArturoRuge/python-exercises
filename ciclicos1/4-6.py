#Un entrenador le ha propuesto a un atleta recorrer una ruta de cinco kilómetros durante 10 días, 
#para determinar si es apto #para la prueba de 5 Kilómetros o debe buscar otra especialidad. 
#Para considerarlo apto debe cumplir por lo menos una de las #siguientes condiciones:

#Que en ninguna de las pruebas haga un tiempo mayor a 16 minutos.
#Que al menos en una de las pruebas realice un tiempo menor a 13 minutos.
#Que su promedio de tiempos sea menor o igual a 15 minutos.


tiempoPruebas = []
contador = 0
print("Digite el tiempo de las 10 pruebas")
for i in range(1,11):
	tiempoPruebas.append(int(input("prueba " + str(i) + " : ")))


if max(tiempoPruebas) < 16:
	print("Puede correr la prueba")
elif min(tiempoPruebas) < 13:
	print("Puede correr la prueba")
else:
	for i in tiempoPruebas:
		contador = contador + i
	promedio = contador / len(tiempoPruebas)
	if promedio <= 15:
		print("Puede correr la prueba")
	else:
		print("NO Puede correr la prueba")


