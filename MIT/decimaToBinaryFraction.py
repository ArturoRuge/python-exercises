x = float(input("Ente a decimal number between 0 an 1: "))
p = 0
while ((2**p)*x)%1 != 0:
	print("Remainder = " + str((2**p)*x - int((2**p)*x)))
	p += 1
numb = int(x*(2**p))
result = ""
if numb == 0:
	result = "0"
while numb > 0:
	result = str(numb%2) + result
	numb = numb//2

for i in range(p - len(result)):
	result = "0" + result

result = result[0:-p] + "." + result[-p:]
print("The binary representation of the decimal " + str(x) + " is " + str(result))
