#El gobierno ha establecido el programa SAR (Sistema de Ahorro para el Retiro) que consiste en que 
#los dueños de la empresa deben obligatoria- mente depositar en una cuenta bancaria un porcentaje del 
#salario de los trabajadores. Adicionalmente los trabajadores pueden solicitar a la empre- sa que deposite 
#directamente una cuota fija o un porcentaje de su salario en la cuenta del SAR, la cual le será descontada 
#de su pago. Un trabajador que ha decidido aportar a su cuenta del SAR desea saber la cantidad total de dinero 
#que estará depositado en esa cuenta cada mes, y el pago mensual que recibirá.

salario = int(input("Cual es su salario? "))
sar = int(input("Cual es el % del SAR? "))
formaAporte = input("Desea realizar su aporte en porcentaje(%) o cuota fija(ct) ? ")

if formaAporte == "ct":
	aporte = int(input("Digite la cantidad a aportar: "))
	aporteNeto = aporte
else:
	aporte = int(input("Digite el % de aporte voluntario? "))
	aporteNeto = (aporte / 100) * salario

sarNeto = (sar / 100) * salario
sarTotal = sarNeto + aporteNeto
salarioFinal = salario - sarTotal

print("El aporte mensual al programa SAR es de: $" + str(round(sarTotal)) + " Y el salario total es de: $" + str(round(salarioFinal)))