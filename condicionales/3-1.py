import random
cuenta = int(input("total de la compra: "))
numero = random.randint(0,100)
if numero <74:
	descuento = cuenta * 0.15
else:
	descuento = cuenta * 0.2
print("Su numero es " + str(numero) + " Su descuento es de " + str(descuento) + " pesos")