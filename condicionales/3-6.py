#El gobierno desea reforestar un bosque que mide determinado número de hectáreas. 
#Si la superficie del terreno excede a 1 millón de metros cuadra- dos, entonces decidirá 
#sembrar de la siguiente manera:

hectareas = int(input("Digite las hectareas a sembrar: "))
area = hectareas * 10000
if area > 1000000:
	cantPinos = ((area * 0.7) / 10) * 8
	cantOyamel = ((area * 0.2) / 15) * 15
	cantCedro = ((area * 0.1) / 18) * 10
else:
	cantPinos = ((area * 0.5) / 10) * 8
	cantOyamel = ((area * 0.3) / 15) * 15
	cantCedro = ((area * 0.2) / 18) * 10
def redondear(cantidad):
	cantidadFinal = str(round(cantidad))
	return cantidadFinal

print("El número de pinos es de " + redondear(cantPinos) + " Oyamel " + redondear(cantOyamel) + " y Cedro: " + redondear(cantCedro))