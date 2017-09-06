def average_temps(list_temp):
	sum_of_temps = 0

	for temp in list_temp:
		sum_of_temps += temp

	return sum_of_temps / len(list_temp)



if __name__ == "__main__":
	list_temp = [22, 21, 24, 24, 22, 21, 24]

	average = average_temps(list_temp)

	print("La temperatura promedio es de {}".format(average))
