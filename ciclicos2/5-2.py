#En una empresa se requiere calcular el salario semanal de cada uno de los n obreros que trabajan en ella. 
#El salario se obtiene de la siguiente forma:
#Si el obrero trabaja 40 horas o menos se le paga $20 por hora.
#Si trabaja más de 40 horas se le paga $20 por cada una de las primeras 40 horas y $25 por cada hora extra.

cantObreros = int(input("De cuantos obreros necesita calcular el salario? "))
for i in range(1, cantObreros+1):
	htrabajo = int(input("Cuantas horas trabajo el obrero #" + str(i) + " "))
	if htrabajo <= 40:
		salario = htrabajo * 20
		print("El salario semanal del obrero #" + str(i) + " es de " + str(salario))
	else:
		salario = (20*40) + ((htrabajo - 40) * 25)
		print("El salario semanal del obrero es de #" + str(i) + " es de " + str(salario))
