def factorial(num):
	"""input: int >= 0
	return: n factorial
	"""
	if type(num) != type(1):
		print("El factorial solo está definido para enteros")
		return -1
	elif num < 0:
		print("El factorial solo está definido para positivos")
		return -1
	elif num == 0:
		return 1
	else:
		return num * factorial(num -1)



if __name__ == "__main__":
	num = int(input("Digite un número para hayar su factorial: "))
	result = factorial(num)
	print("El factorial de {} es {}".format(num, result))