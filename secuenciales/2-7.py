#7. Un alumno desea saber cual será su promedio general en las tres materias mas difíciles 
#que cursa y cual será el promedio que obtendrá en cada una de ellas. Estas materias se evalúan como 
#se muestra a continuación:
#La calificación de Análisis se obtiene de la siguiente manera: 
	#• Examen 90%
	#• Promedio de Trabajos Prácticos 10 %
	#• En esta materia se pidió un total de tres TP.
#La calificación de Álgebra se obtiene de la siguiente manera:    
	#• Examen80%
	#• Promedio de Trabajos Prácticos 20 %
	#• En esta materia se pidió un total de dos TP.
#La calificación de Programación se obtiene de la siguiente manera: 
	#• Examen 85%
	#• Promedio de Trabajos Prácticos 15 %
	#• En esta materia se pidió un total de tres TP.

analisisExamen = int(input("Calificación examen Analisis: "))
analisisTP1 = int(input("Calificacion TP1: "))
analisisTP2 = int(input("Calificacion TP2: "))
analisisTP3 = int(input("Calificacion TP3: "))

algebraExamen = int(input("Calificación examen Álgebra: "))
algebraTP1 = int(input("Calificacion TP1: "))
algebraTP2 = int(input("Calificacion TP2: "))

prograExamen = int(input("Calificación examen programación: "))
prograTP1 = int(input("Calificacion TP1: "))
prograTP2 = int(input("Calificacion TP2: "))
prograTP3 = int(input("Calificacion TP3: "))

notaAnalisis = (analisisExamen * 0.9) + (((analisisTP1 + analisisTP2 + analisisTP3) / 3) * 0.1 )
notaAlgebra = (algebraExamen * 0.8) + (((algebraTP1 + algebraTP2) / 2) * 0.2)
notaProgra= (prograExamen * 0.85) + (((prograTP1 + prograTP2 + prograTP3) / 3) * 0.15)
promedioGeneral = (notaAnalisis + notaAlgebra + notaProgra) / 3

print("Su promedio general es de: " + str(round(promedioGeneral,2)) + " Sus notas en Análisis, Álgebra y Programación son: " + str(round(notaAnalisis,2)) + " " + str(round(notaAlgebra,2)) + " y " + str(round(notaProgra,2)))
