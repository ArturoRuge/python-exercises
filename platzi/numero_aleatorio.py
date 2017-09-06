import random

def run():
	number_found = False
	random_number = random.randint(0, 20)

	while not number_found:
		try:
			print("")
			number = int(input("Digita un número entre 0 y 20: "))

			if number == random_number:
				print("Ganaste!!")
				number_found = True
			elif number < 0 or number > 20:
				print("Recuerda, es un valor entre 0 y 20! intentelo de nuevo: ")
			elif number > random_number:
				print("Es un número menor!")
			else:
				print("Es un número mayor")
		except ValueError:
			print("Has digitado un valor no valido, intentalo de nuevo")


if __name__ == "__main__":
	run()
