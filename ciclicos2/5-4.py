#El Departamento de Seguridad Pública y Tránsito del D.F. desea saber, de los n autos que entran a la ciudad 
#de México, cuántos entran con calcomanía de cada color. Conociendo el último dígito de la placa de cada automóvil s
#e puede determinar el color de la calcomanía utilizando la siguiente relación:

amarilla = 0
rosa = 0
roja = 0
verde = 0
azul = 0
numInvalido = 0
cantAutos = int(input("Digite la cantidad de autos a analizar "))
for i in range(1, cantAutos+1):
	numPlaca = int(input("Cual es el ultimo digito de la placa del carro #" + str(i) + " "))
	if numPlaca == 1 or numPlaca == 2:
		amarilla = amarilla + 1
	elif numPlaca == 3 or numPlaca == 4:
		rosa = rosa +1
	elif numPlaca == 5 or numPlaca == 6:
		roja = roja + 1
	elif numPlaca == 7 or numPlaca == 8:
		verde = verde + 1
	elif numPlaca == 9 or numPlaca == 0:
		azul = azul + 1
	else:
		numInvalido = numInvalido + 1
print("El color de la calcomanía es amarilla:" + str(amarilla) + " rosa:" + str(rosa) + " roja:" + str(roja) + " verde:" + str(verde) + " azul:" + str(azul) + " indeterminado:" + str(numInvalido)) 
