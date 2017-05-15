#Una compañía de seguros esta abriendo un departamento de finanzas y estableció un programa 
#para captar clientes, que consiste en lo siguiente: Si el monto por el que se efectúa el seguro 
#es menor que $50.000 la cuota a pagar será por el 3% del monto, y si el monto es mayor que $50.000 
#la cuota a pagar será el 2 % del monto. La aseguradora desea determinar cuál será la cuota que debe pagar un cliente.

montoSeguro = int(input("Valor del monto del seguro: "))
if montoSeguro < 50000:
	cuota = montoSeguro * 0.03
else:
	cuota = montoSeguro * 0.02

print("la cuota a pagar es de: $" + str(round(cuota)))