import datetime

class Person(object):
	def __init__(self, name):
		"""create a person called name"""
		self.name = name
		self.birthday = None
		self.lastName = name.split(" ")[-1]
		#name is a string, so split into a list of strings
		#based on spaces, then extract last element

	def getLastName(self):
		"""return self`s last name"""
		return self.lastName

	def __str__(self):
		"""return self`s name"""
		return self.name

	def setBirthday(self, month, day, year):
		"""sets self`s birthday to birthDate"""
		self.birthday = datetime.date(year, month, day)

	def getAge(self):
		"""returns self`s current age in dys"""
		if self.birthday == None:
		    raise ValueError
		return (datetime.date.today() - self.birthday).days

	def __lt__(self, other):
		"""Return True if self`s name is lexicographic less
		than other`s name, and False otherwisw"""
		if self.lastName == other.lastName:
			return self.name < other.name
		return self.lastName < other.lastName

    # other methods

	def __str__(self):
		"""return self`s name"""
		return self.name


#example usage

#p1 = Person("Mark Zuckerberg")
#p1.setBirthday(5,14,84)
#p2 = Person("Drew Houston")
#p2.setBirthday(3,4,83)
#p3 = Person("Bil Gates")
#p3.setBirthday(10, 28,55)
#p4 = Person("Andrew Gates")
#p5 = Person("Steve Wozniak")

#personList = [p1, p2, p3, p4, p5]

#for e in personList:
#	print(e)

#personList.sort()
#for e in personList:
#	print(e)



#MIT CLASS

class MITPerson(Person):
	nextIdNum = 0 # next ID number to assign

	def __init__(self, name):
		Person.__init__(self, name) # initialize Person attributes
		self.idNum = MITPerson.nextIdNum #MITPerson atribute: Unique ID
		MITPerson.nextIdNum += 1

	def getIdNum(self):
		return self.idNum

	#sorting MIT people uses their ID number
	def __lt__(self, other):
		return self.idNum < other.idNum

	def speak(self, utterance):
		return (self.getLastName() + " says: " + utterance)


#example usage

#m3 = MITPerson("Mark Zuckerberg")
#Person.setBirthday(m3,5,14,84)
#m2 = MITPerson("Drew Houston")
#Person.setBirthday(m2,3,4,83)
#m1 = MITPerson("Bil Gates")
#Person.setBirthday(m1,10, 28,55)

#MITPersonList = [m1, m2, m3]

#p1 = MITPerson("Eric")
#p2 = MITPerson("John")
#p3 = MITPerson("John")
#p4 = Person("John")

#for e in MITPersonList:
#	print(e)

#MITPersonList.sort()

#for e in MITPersonList:
#	print(e)

#print(p1<p3)
#print(p1<p4) !!!!!ERROR because p4 has no idNum Attribute == p1.__lt__(p2)
#print(p4<p1) !!!!False -- using the lt Person method

class Student(MITPerson): #Created for Known when a person is an active student
							#and we can use better the isStudent function
    pass

class UG(Student): #Ungraded MIT
    def __init__(self, name, classYear):
    	MITPerson.__init__(self, name)
    	self.year = classYear

    def getClass(self):
    	return self.year

    def speak(self, utterance):
    	return MITPerson.speak(self, " Dude, " +utterance)

class Grad(Student):
	pass

class TransferStudent(Student):
	pass

def isStudent(obj):
	return isinstance(obj, Student)


 
#example usage

s1 = UG("Mat Damon", 2017)
#s2 = UG("Ben Affelck", 2017)
#s3 = UG("Lin Manuel Miranda", 2018)
#s4 = Grad("Leonardo Di Caprio")

#print(s1)
#print(s1.getClass())
#print(s1.speak("Where is the quiz?"))
#print(s2.speak("I have no clue"))
#print(isStudent(s1))



class Professor(MITPerson):
	def __init__(self, name, department):
		MITPerson.__init__(self, name)
		self.department = department

	def speak (self, utterance):
		new = "In course " + self.department + " we say "
		return MITPerson.speak(self, new + utterance) 
		#This will shadow MITPerson speak method

	def lecture(self, topic):
		return self.speak("It is obvious that " + topic)
		#note use of own speak method

#example usage

faculty = Professor("Doctor Arrogant", "six")
print(s1.speak("Hi there"))
print(faculty.speak("hi there"))
print(faculty.lecture("hi there"))






