#6. Calcular el factorial de un número ingresado.
factorial = 1
num = int(input("Ingrese un número para calcular su factorial: "))
if num == 0  or num == 1:
	factorial = 1
elif num > 1:
	for i in range(num, 1, -1):
		factorial = factorial * i
else:
	factorial = "No se puede calcular"
print("su factorial es " + str(factorial))


