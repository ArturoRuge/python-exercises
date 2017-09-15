import csv
CANTIDAD_DE_CAMPOS = 5

class LongitudCamposIncorrectoError(Exception):
	pass

nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
	with open(nombre_archivo) as archivo:
		print("El archivo se abrio correctamente")
		archivo_csv = csv.reader(archivo)
		for linea in archivo_csv:
			if len(linea) != CANTIDAD_DE_CAMPOS:
				raise LongitudCamposIncorrectoError()


except FileNotFoundError:
	print("El archivo no existe")

except LongitudCamposIncorrectoError:
	mensaje = "{} no tiene los campos correctos".format(linea)
	print(mensaje)
	with open("error.log", "w") as error_file:
		error_file.write(mensaje)