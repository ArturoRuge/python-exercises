def gcdRecur(a, b):
	if b == 0:
		return a
	else:
		return gcdRecur(b, a%b)

valor1 = int(input("Digite el primer valor "))
valor2 = int(input("Digite el segundo valor "))

print("El maximo comun divisor de " + str(valor1) + \
	" y " + str(valor2) + " es " + str(gcdRecur(valor1, valor2)))