#Un proveedor de estéreos ofrece un descuento del 10 % sobre el precio sin I.V.A. de algún 
#aparato si este cuesta $2.000 o más. Además, indepen- dientemente de esto, ofrece un 5 % de descuento 
#si la marca es “YNOS”. Determinar cuánto pagará, con I.V.A. incluido, un cliente cualquiera por la compra de su aparato.

precioInicial = int(input("Precio del aparato: "))
iva = int(input("porcentaje del IVA "))
marca = input("Marca del estéreo ")
valorIVA = (iva / 100) * precioInicial
descuento2 = 0

if precioInicial >= 2000:
	descuento = precioInicial * 0.1
else:
	descuento = 0
if marca == "ynos":
	descuento2 = precioInicial * 0.05

precioFinal = precioInicial + valorIVA - descuento - descuento2   
print("El valor final a pagar es de: $" + str(round(precioFinal)))