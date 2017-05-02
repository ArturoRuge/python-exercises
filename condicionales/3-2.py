genero = input("masculino(M) o femenino(F)??")
edad = int(input("Edad?"))
if genero == "M":
	pulsaciones = (210 - edad) / 10
else:
	pulsaciones = (220 - edad) / 10
print("tus pulsaciones son  " + str(pulsaciones) + " cada 10 segundos")