def oddTuples(aTup):
	"""
	aTup: a tuple
	return: tuple, every other element of aTup
	"""
	otherTuple = ()
	i = 0
	while i < len(aTup):
		otherTuple += (aTup[i],)
		i +=2
	return otherTuple

tup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(tup))