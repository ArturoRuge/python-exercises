#Calcular e imprimir la tabla de multiplicar de un número cualquiera. Im- primir el multiplicando, 
#el multiplicador y el producto.

numero = int(input("Digite el número del cual desea sabr la tabla de multiplicar: "))
for i in range (1,11):
	print(str(numero) + (" * ") + str(i) + " = " + str(numero*i) )