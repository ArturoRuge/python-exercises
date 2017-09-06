#9. Encontrar el menor valor de un conjunto de n números dados.

numeros = []
cant = int(input("Digite la cantidad de numeros a analizar "))
for i in range(1, cant+1):
	numeros.append(int(input(">>Digite el número " + str(i) + ": ")))
print("El minimo ingresado es " + str(min(numeros)))