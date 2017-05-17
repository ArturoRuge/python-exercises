#10. Una frutería ofrece las manzanas con descuento según la siguiente tabla:

pesoManzanas = int(input("Digite la cantidad de manzanas en Kg: "))
valorKg = int(input("Cual es el valor por Kg de manzana? "))

while pesoManzanas <= 0 or valorKg <= 0:
	print("No se admiten valores iguales o menores a 0")
	pesoManzanas = int(input("Digite la cantidad de manzanas en Kg: "))
	valorKg = int(input("Cual es el valor por Kg de manzana? "))

if pesoManzanas <= 2:
	descuento = 0
elif pesoManzanas > 2 and pesoManzanas <= 5:
	descuento = 10
elif pesoManzanas > 5 and pesoManzanas <=10:
	descuento = 15
else:
	descuento = 20

valorNeto =  pesoManzanas * valorKg
descuentoFinal = (descuento /100) * valorNeto
valorFinal = valorNeto - descuentoFinal
print("Valor a pagar: $" + str(valorFinal)) 