#En una fábrica de computadoras se planea ofrecer a los clientes un des- cuento que dependerá del 
#número de computadoras que compre. Si las computadoras son menos de cinco se les dará un 10 % de 
#descuento sobre el total de la compra; si el número de computadoras es mayor o igual a cinco pero 
#menos de diez se le otorga un 20 % de descuento; y si son 10 o más se les da un 40 % de descuento. 
#El precio de cada computadora es de $1.600.

numCompu = int(input("Digite el número de computadoras: "))
valorNeto = numCompu * 1600
if numCompu < 5:
	descuento = valorNeto * 0.1
	valorFinal = valorNeto - descuento
elif numCompu >= 5 and numCompu <10:
	descuento = valorNeto * 0.2
	valorFinal = valorNeto - descuento
else:
	descuento = valorNeto * 0.4
	valorFinal = valorNeto - descuento
print("su descueno sobre su compra es de $" + str(descuento) + " y el precio final a pagar es de $" + str(valorFinal))



