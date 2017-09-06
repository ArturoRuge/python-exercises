def create_point():
	x = int(input("Define la coordenada X de punto: "))
	y = int(input("Define la coordenada Y del punto: "))
	return Coordinates(x, y)

class Coordinates(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def distance(self, other):
		x_diff_sq = (self.x - other.x)**2
		y_diff_sq = (self.y - other.y)**2
		return (x_diff_sq +  y_diff_sq) **0.5
	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"
	def __sub__(self, other):
		return Coordinates(self.x - other.x, self.y - other.y)
	def __add__(self, other):
		return Coordinates(self.x + other.x, self.y + other.y)





if __name__ == "__main__":
	point1 = create_point()
	point2 = create_point()
	print("")
	print("OPERACIONES CON PUNTOS")
	print("El punto uno es {}".format(point1))
	print("El punto dos es {}".format(point2))
	print("La distancia entre los puntos es de {}".format(Coordinates.distance(point1, point2)))
	print("La resta de los puntos es de {}".format(point1 - point2))
	print("La suma de los puntos es de {}".format(point1 + point2))
	print("")