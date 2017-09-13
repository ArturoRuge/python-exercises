class Animals(object):
	def __init__(self, age):
	    self.age = age
	    self.name = None
	def get_age(self):
		return self.age
	def get_name(self):
		return self.name
	def set_age(self, newage):
	    self.age = newage
	def set_name(self, newname=""):
	    self.name = newname
	def __str__(self):
		return "animal" + str(self.name) + ":" + str(self.age)


class Cat(Animals):
	def speak(self):
		print("meawwwwww")
	def __str__(self):
		return "Cat" + str(self.name) + ":" + str(self.age)

class Rabbit(Animals):
	def speak(self):
		print("Beeeep")
	def __str__(self):
		return "Rabbit" + str(self.name) + ":" + str(self.age)

class Person(Animals):
	def __init__(self, name, age):
		Animals.__init__(self, age)
		Animals.set_name(self, name)
		self.friends = []
	def get_friends(self):
		return self.friends
	def add_friends(self, fname):
		if fname not in self.friends:
			self.friends.append(fname)
	def speak(self):
		print("Hello")
	def age_diff(self, other):
		#Alternative: diff = self.age - other.age
		diff = self.get_age() - other.get_age()
		if self.age > other.age:
			print(self.name, "is", diff, "years older than" , other.name)
		else:
			print(other.name, "is", -diff, "years oldes then", self.name)
	def __str__(self):
		return "Person:" + str(self.name) + ":" * str(self.age)


if __name__ == "__main__":
	desconocido = Animals(100)
	desconocido.set_name("Desconocido")
	print(desconocido)

	bunny = Rabbit(40)
	bunny.set_name("Bunny")
	bunny.speak()

	pelusa = Cat(2)
	pelusa.set_name("Pelusa")
	pelusa.speak()
	print(pelusa)




