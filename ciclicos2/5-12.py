#Cinco miembros de un club contra la obesidad desean saber cuánto han bajado o subido de peso desde la 
#última vez que se reunieron. Para esto se debe realizar un ritual de pesaje en donde cada uno se pesa en 
#diez básculas distintas para así tener el promedio más exacto de su peso. Si existe diferencia positiva 
#entre este promedio de peso y el peso de la última vez que se reunieron, significa que subieron de peso. 
#Pero si la diferencia es negativa, significa que bajaron. Lo que el problema requiere es que por cada persona 
#se imprima un letrero que diga: “Subió” o “Bajó” y la cantidad de kilos que subió o bajó de peso.


for i in range(1, 6):
	peso = []
	pesoTotal = 0
	print("DATOS PERSONA #" + str(i))
	promedioAnterior = int(input("Digite el promedio de peso anterior: "))
	print("Digite los datos de las básculas")
	for i in range(1, 11):
		peso.append(int(input("Peso de la bácula " + str(i) + (": ") )))
	for i in peso:
		pesoTotal = pesoTotal + i
	promedioActual = pesoTotal / 10 
	comparacionPesos = promedioActual - promedioAnterior
	if comparacionPesos > 0:
		print("Subio" + str(comparacionPesos) + "Kilos")
	else:
		print("Bajo" + str(comparacionPesos) + "Kilos")
