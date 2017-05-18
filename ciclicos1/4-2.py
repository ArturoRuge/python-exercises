#Leer 20 números e imprimir cuántos son positivos, cuántos negativos y cuántos son cero.

numeros = []
ceros = 0
positivos = 0
negativos = 0
print("Digite 20 números")
for i in range(20):
	numeros.append(int(input(">>")))
for i in numeros:
	if i == 0: 
		ceros = ceros + 1
	elif i < 0:
		negativos = negativos + 1
	else:
		positivos = positivos + 1
print("los numeros positivos son: " + str(positivos) + " Negativos: " + str(negativos) + " y ceros son: " + str(ceros))
