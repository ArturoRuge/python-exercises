#4. Leer un número e imprimir un mensaje que indique si el número es par o no.

num1 = int(input("Digite un numero "))
controlador = num1 % 2
if controlador == 0:
	print(str(num1) + " es un número par")
else:
	print(str(num1) + " es un número impar")
