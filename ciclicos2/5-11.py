#11. En un supermercado un cajero captura los precios de los artículos que los 
#clientes compran e indica a cada cliente cuál es el monto de lo que deben pagar. 
#Al final del día le indica a su supervisor cuánto fue lo que cobró en total a todos 
#los clientes que pasaron por su caja.

montoTotal = 0
nuevoCliente = "si"
while nuevoCliente == "si":
	facturaCliente = 0
	costoArticulos = 0
	cantArticulos = int(input("Digite la cantidad de articulos del cliente"))
	for i in range(1, cantArticulos+1):
		costoArticulo = int(input("precio " + str(i) + ":"))
		costoArticulos = costoArticulos + costoArticulo
	montoTotal = montoTotal + costoArticulos
	print("La factura del cliente es de: " +str(costoArticulos))
	nuevoCliente = input("Desea calcular la factura de un nuevo cliente? (si) (no) ")
print("El monto total del día es de " + str(montoTotal))

