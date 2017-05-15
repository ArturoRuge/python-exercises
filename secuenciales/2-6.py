#6. Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. 
#Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.
inversion1 = int(input("Cantidad de primera inversión: "))
inversion2 = int(input("Cantidad de segunda inversión: "))
inversion3 = int(input("Cantidad de tercera inversión: "))
inversionTotal = inversion1 + inversion2 + inversion3
def porcentajeInv(inversion):
	porcentaje = (inversion * 100) / inversionTotal
	return porcentaje
print("El procentaje de inversión del primer, segundo y tercer inversionista es: " + str(round(porcentajeInv(inversion1),2)) + "% " + str(round(porcentajeInv(inversion2),2)) + "% " + str(round(porcentajeInv(inversion3),2)) + "%" )

