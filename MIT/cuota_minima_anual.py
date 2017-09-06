#write a program that calculates the minimum fixed monthly 
#payment needed in order pay off a credit card balance within 
#12 months. By a fixed monthly payment, we mean a single number
# which does not change each month, but instead is a constant 
#amount that will be paid each month.

balance = int(input("Digite la deuda "))
interes = int(input("Digite el interés anual "))
interesMensual = (interes / 100) / 12
def calcularCuota(balance, interes, meses, cuota):
	"""
	input: 
	balance: valor de la deuda calculada mensualmente
	interes: interes anual de la deusa
	meses: 12 meses para pagar la deuda
	cuota: minima cuota a pagar mensualmente
	output
	El valor de balnace(deuda) despues de pagar 12 meses
	la cuota
	"""
	balance -= cuota
	if meses == 1:
		return balance
	else:
		nuevoBalance = balance + (balance * interesMensual)
		return calcularCuota(nuevoBalance, interes, meses-1, cuota)

i = True
cuota = 10
while i: 
	if calcularCuota(balance, interes, 12, cuota) <= 0:
		i = False
		break
	cuota += 10
print("El valor minimo a pagar mensualmente para que la deuda \
	sea pagada en 12 meses es de : $" + str(cuota))

