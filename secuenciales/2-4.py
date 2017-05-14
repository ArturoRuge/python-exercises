#Un profesor maestro desea saber que porcentaje de hombres y que por- centaje de 
#mujeres hay en un grupo de estudiantes. Se ingresa como dato el total de mujeres y total de hombres.

numMujeres = int(input("Cantidad de mujeres: "))
numHombres = int(input("Cantidad de hombres: "))
totalEstudiantes = numHombres + numMujeres
porcentajeMujeres = (numMujeres * 100) / totalEstudiantes
porcentajeHombres = (numHombres * 100) / totalEstudiantes
print("El porcentaje de hombres es: " + str(round(porcentajeHombres,2)) + "% y de mujeres es: " + str(round(porcentajeMujeres,2)) + "%")