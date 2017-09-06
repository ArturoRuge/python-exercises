class NumList(object):
	"""NumList is a set of integers"""

	def __init__(self):
		self.vals=[]

	def insert(self, e):
		if not e in self.vals:
			self.vals.append(e)
		else:
			print("Ese valor ya existe!")
	def member(self, e):
		if e in self.vals:
			print("El valor existe")
		else:
			print("El valor NO existe")
	def remove(self, e):
		try:
			self.vals.remove(e)
		except:
			raise ValueError(str(e) + "not found")

	def __str__(self):
		self.vals.sort()
		result = ""
		for e in self.vals:
			result = result + str(e) + ","
		return "{" + result[:-1] + "}"


def create_list():
	l = NumList()
	option = True

	while option:
		print("")
		print("QUE QUIERES HACER CON LA LISTA:?")
		print("Añadir elemento(A)---Eliminar elemento(R)")
		print("Consultar si un elemento y esta cargado(C)")
		print("Ver la lista(V)-------Salir(S)")
		rst = input()
		if rst == "A":
			l.insert(input("Digita el numero a añadir: "))
		elif rst == "C":
			l.member(input("Digita el valor a consultar: "))
		elif rst == "R":
			l.remove(input("Digita el valor a eliminar: "))
		elif rst == "V":
			print(l)
		else:
			option = False
			print("has creado esta lista {} Chaooo!".format(l))




if __name__ == "__main__":

	create_list()