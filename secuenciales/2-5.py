#Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, 
#si la fórmula es: pulsaciones = (220 - edad)/10

edad = int(input("¿Cuantos años tienes? "))
pulsaciones = (220 - edad) / 10
print("tu pulso es de " + str(round(pulsaciones,2)) + " pulsaciones por cada 10 segundos de ejercicio")