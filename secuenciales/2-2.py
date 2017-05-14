#2. Un vendedor recibe un sueldo base más un 10 % extra por comisión de sus ventas, 
#el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las 
#tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
venta1 = int(input("Digita el valor de tu primera venta "))
venta2 = int(input("Digita el valor de tu segunda venta "))
venta3 = int(input("Digita el valor de tu tercera venta "))
sueldoBase = int(input("digite su sueldo base "))
comision = (venta1 + venta2 + venta3) * 0.1
sueldo = sueldoBase + comision
print("Su comisión de este mes es " + str(comision) + " pesos y su sueldo es de " + str(sueldo) + (" pesos"))