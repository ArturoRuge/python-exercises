animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals["d"].append("Hola")
animals["d"].append("burro")
animals["b"].append("babbon2")

def biggest(aDict):
	cantMax = 0
	posMax = None
	for key in aDict.keys():
		if len(aDict[key]) >= cantMax:
			posMax = key
			cantMax = len(aDict[key])
	return posMax

def how_many(aDict):
	cantidad = 0
	for keys in aDict.keys():
		cantidad += len(aDict[keys])
	return cantidad

print(how_many(animals))
print(biggest(animals), animals)
