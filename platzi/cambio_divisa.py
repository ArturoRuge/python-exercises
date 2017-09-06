def change(ammount):
	"""
	input: cantidad de pesos argentinos
	output: conversion de los pesos argentinos a dolares
	"""
	arg_to_dollar_rate = 17.2
	return ammount / arg_to_dollar_rate 

def run():
	print("CARCULADORA CAMBIO MONEDA")
	print("Convierte peso Argentino a dolares")
	print("")

	ammount = float(input("Digita la cantidad de pesos Argentinos"))

	result = change(ammount)

	print("${} pesos Argentinos son ${} dolares ".format(ammount, result))
	print("")

if __name__ == "__main__":
	run()

