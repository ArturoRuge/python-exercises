numb = int(input("Digite un numero entero: "))
if numb < 0:
	isNeg = True
	numb = abs(num)
else:
	isNeg = False
result = ""
if numb == 0:
	result = "0"
while numb > 0:
	result = str(numb%2) + result
	numb = numb//2
if isNeg:
	result= "-" + result
print("El número en binario es : " + str(result))