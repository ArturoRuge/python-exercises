class Fraction(object):
	def __init__(self, num, dem):
		self.num = num
		self.dem = dem
	def __str__(self):
		return str(self.num) + "/" + str(self.dem) 
	def getNum(self):
		return self.num
	def getDem(self):
		return self.dem
	def __add__(self, other):
		new_num = self.getNum() * other.getDem() + \
				self.getDem() * other.getNum()
		new_dem = self.getDem() * other.getDem()
		return str(new_num) + "/" + str(new_dem) 
	def __sub__(self, other):
		new_num = self.getNum() * other.getDem() - \
				self.getDem() * other.getNum()
		new_dem = self.getDem() * other.getDem()
		return str(new_num) + "/" + str(new_dem)
	def convert(self):
		return self.getNum() / self.getDem()


def create_fraction():
	num = int(input("Digita el numerador: "))
	dem = int(input("Digita el denominadador: "))
	return Fraction(num, dem)



if __name__ == "__main__":
	print("")
	print("PRIMER FRACCIONARIO")
	fract1 = create_fraction()
	print("SEGUNDO FRACCIONARIO")
	fract2 = create_fraction()
	print("Los fraccionarios ingresados son {} y {}".format(fract1, fract2))
	print("La suma de los dos fraccionarios es {}".format(fract1 + fract2))
	print("La resta de los dos fraccionarios es {}".format(fract1 - fract2))
	print("Los fraccionarios en numero flotante equivalen a {} y {}".format(fract1.convert(), fract2.convert()))
	print("")