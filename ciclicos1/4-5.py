#En un centro de verificación de automóviles se desea saber el promedio de puntos contaminantes de 
#los primeros 25 automóviles que lleguen. Asimis- mo se desea saber los puntos contaminantes del carro 
#que menos contamino y del que más contamino.
print("Digite el valor contaminante de los 25 automóviles")
carrosContaminantes=[]
contador = 0
for i in range(10):
	carrosContaminantes.append(int(input(">>")))
for i in carrosContaminantes:
	contador = contador + i
promedio = contador / len(carrosContaminantes)
print("El promedio de carros contaminantes es de " + str(promedio) + " los valores minimo y máximo son: " + str(min(carrosContaminantes)) + str(max(carrosContaminantes)))