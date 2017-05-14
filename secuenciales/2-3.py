#Un alumno desea saber cuál será su calificación final en la materia de Laboratorio. 
#Dicha calificación se compone de los siguientes porcentajes:
#55 % del promedio de sus tres calificaciones parciales. 
#30 % de la calificación del examen final.
#15 % de la calificación de un trabajo final.

parcial1 = int(input("Calificación del primer parcial: "))
parcial2 = int(input("Calificación del segundo parcial: "))
parcial3 = int(input("Calificación del tercer parcial: "))
examenFinal = int(input("Calificación examen final: "))
trabajoFinal = int(input("Calificación trabajo final: "))

notaParciales = ((parcial1 + parcial2 + parcial3)/3) * 0.55
notaExamen = examenFinal * 0.3
notaTrabajo = trabajoFinal * 0.15

print("Su nota final es " + str(notaParciales + notaExamen + notaTrabajo))