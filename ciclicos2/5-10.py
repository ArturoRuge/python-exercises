#10. Encontrar el mayor valor de un conjunto de n números dados.
numeros = []
cant = int(input("Digite la cantidad de números ha ingresa "))
for i in range(1, cant+1):
	numeros.append(int(input(">>Ingrese el valor del número " + str(i) + ": ")))
print("El mayor numero ingresado es " + str(max(numeros)))
