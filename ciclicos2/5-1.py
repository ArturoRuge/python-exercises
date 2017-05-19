#Una compañía de seguros tiene contratados a n vendedores. Cada uno hace tres ventas a la semana. 
#Su política de pagos es que #un vendedor recibe un sueldo base, y un 10% extra por comisiones de sus ventas. 
#El gerente de su compañía desea saber cuanto #dinero obtendrá en la semana cada vendedor por concepto de 
#comisiones por las tres ventas realizadas, y cuanto tomando en #cuenta su sueldo base y sus comisiones.

ventas = []
contador = 0
numEmpleados = int(input("Digite el numero de empleados ")) + 1
for i in range(1, numEmpleados):
	sueldo = int(input("Digite el sueldo semanal base del empleado " + str(i) + " : "))
	for i in range(1,4):
		ventas.append(int(input("Venta " + str(i) + " : ")))
	for i in ventas:
		contador = contador + i
	comision = contador * 0.1
	print("La comisión del vendedor es de $" + str(comision) + " y su sueldo base más comisión es de $" + str(sueldo + comision) )
