#Que lea tres números diferentes y determine cuál es el número medio del conjunto de los tres números.

num1 = int(input("Digite el primer número "))
num2 = int(input("Digite el segundo número "))
num3 = int(input("Digite el tercer número "))

if num1 > num2 and num1 < num3:
	print("El número del medio es el " + str(num1))
elif num2 > num1 and num2 < num3:
	print("El número del medio es el " + str(num2))
elif num3 > num1 and num3 < num2:
	print("El número del medio es el " + str(num3))


