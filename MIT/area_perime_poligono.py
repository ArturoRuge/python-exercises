import math

def polysum(n, s):
	"""
	input: n-number of sides and s- side length
	output: sum of the perimeter square and area
	"""
	area = (0.25 * n * (s**2)) / (math.tan(math.pi / n))
	perimeter = n * s
	sumarea_peri = area + (perimeter**2) 
	return round(sumarea_peri, 4)

num_sides = int(input("type the number of sides: "))
len_sides = int(input("type the sides`s lenght? "))
print(polysum(num_sides, len_sides))