import math

def sumarea_peri(n, s):
	"""
	input: n-number of sides and s- side length
	output: suma de n y s
	"""
	area = (0.25 * n * (s**2)) / (tan(math.pi) / n)
	perimetro = n * s
	suma = area + perimetro 
	return round(suma, 2)

print(sumarea_peri(3, 10))