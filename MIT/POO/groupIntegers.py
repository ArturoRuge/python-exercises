class IntSet(object):
	"""An intSet is a set of integers
	The value is represented by a set of ints, self.vals.
	Each int in the set occurs in self.vals exactly once."""

	def __init__(self):
		"""Create an empty set of integers"""
		self.vals = []

	def insert(self, e):
		"""Assumes e is an integer and inserts e into self"""
		if not e in self.vals:
			self.vals.append(e)
			return "Elemento agregado correctamente"
		else:
			return "El elemento ya existe en la lista"

	def member(self, e):
		return e in self.vals

	def remove(self, e):
		try:
			self.vals.remove(e)
			return "El elemento a sido eliminado"
		except:
			raise ValueError(str(e) + "not found")
			return "Ese elemento no existe"

	def __str__(self):
		"""Return a string representation of self"""
		self.vals.sort()
		return "{" + ",".join([str(e) for e in self.vals]) + "}"

	def intersect(self, other):
		newInset = IntSet()
		cont = 0
		for number in self.vals:
			for number2 in other:
				if number == number2:
					newInset.insert(number)
					cont +=1
		if cont == 0:
			return "No hay coincidencias entre las listas"
		else:
			return newInset
	def __len__(self):
		cont = 0
		for items in self.vals:
			cont +=1
		return cont


if __name__ == "__main__":
	keepAdd = True
	s1 = IntSet()
	s2 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

	while keepAdd:
		print("")
		print("Insertar(I) Consultal(C) Remover(R) Imprimir(Im) \
			   Comparar(Co)  Cantidad Elemento(Ca)     Salir(S)  ")
		select = input("Que quiere hacer con la lista?: ")
		if select == "I":
			e = int(input("Digite el valor a agregar en la lista:  "))
			print(s1.insert(e))
		elif select == "C":
			e = int(input("Digite el valor a consultar en la lista:  "))
			if s1.member(e):
				print("El valor existe en la lista")
			else:
				print("El valor NO existe en la lista")
		elif select == "R":
			e = int(input("Digite el valor a eliminar:  "))
			print(s1.remove(e))
		elif select == "Im":
			print(s1)
		elif select == "Co":
			print("Los elementos que están en la lista que has creado \
			y en nuestra lista son {}".format(s1.intersect(s2)))
		elif select == "Ca":
			print("la lista tiene {} elementos".format(len(s1)))

		else:
			print("Byeeeeee!")
			keepAdd = False 