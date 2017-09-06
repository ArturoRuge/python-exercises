#7. Una persona desea invertir su dinero en un banco, el cual le otorga un 2 % de interés. 
#¿Cuál será la cantidad de dinero que esta persona tendrá al cabo de un año si la ganancia de cada mes es reinvertida?
inversion = int(input("Ingrese la cantidad a invertir: "))
for i in range (12):
	intereses= inversion * 0.02
	inversion = inversion + intereses
print("El dinero que tedrá a un año será de " + str(inversion))