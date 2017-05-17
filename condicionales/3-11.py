#El dueño de una empresa desea planificar las decisiones financieras que tomará en el siguiente año. 
#La manera de planificarlas depende de lo si- guiente: 
#Si actualmente su capital se encuentra con saldo negativo, 
#pedirá un préstamo bancario para que su nuevo saldo sea de $10.000. Si su capi- tal tiene actualmente un saldo 
#positivo pedirá un préstamo bancario para tener un nuevo saldo de $20.000, pero si su capital tiene actualmente 
#un saldo superior a los $20.000 no pedirá ningún préstamo. 

#Posteriormente repartirá su presupuesto de la siguiente 
#manera: $5.000 para computado- ras,$2.000 para mobiliario y el resto, la mitad será para la compra de insumos y la 
#otra para otorgar incentivos al personal. Desplegar qué can- tidades se destinarán para la compra de insumos e 
#incentivos al personal y, en caso de que fuera necesario, a cuánto ascendería la cantidad que se pediría al banco.

capital = int(input("Cual es el capital de su empresa? "))

if capital < 0:
	prestamo = abs(capital) + 10000
	capitaFinal = 10000
elif capital > 0 and capital < 20000:
	prestamo = 20000 - capital
	capitaFinal = 20000
else:
	prestamo = 0
	capitaFinal = capital

capitalSobrante = capitaFinal - 7000
compraInsumos = capitalSobrante / 2

if prestamo > 0:
	print("la cantidad para compra de insumos e incentivos es cada una de $" + str(round(compraInsumos)) + "  La cantidad del prestamo al banco fue de $" + str(prestamo))
else:
	print("la cantidad para compra de insumos e incentivos es cada una de $" + str(round(compraInsumos)))



