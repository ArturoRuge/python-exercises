#1. Leer un precio e imprimir por pantalla el precio final con IVA (21 %).

precio = int(input("Digita el precio del articulo: "))
precioConIVA = precio + (precio * 0.21)
print("El precio final con IVA es de " + str(precioConIVA)) 