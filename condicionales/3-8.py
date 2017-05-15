#En un juego de preguntas a las que se responde “Si” o “No” gana quien responda correctamente las tres preguntas. 
#Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego. 
print("Responda Sí(s) o No(n) a las siguientes preguntas")
pregunta1 = input("Colón descubrió América? ")
if pregunta1 == "s":
	pregunta2 = input("La independencia de México fue en el año 1810 ")
	if pregunta2 == "n":
		pregunta3 = input("The Doors fue un grupo de rock Americano ")
		if pregunta3 == "s":
			print("Eres un genio, ganaste!!")
		else:
			print("Casi ganas, sigue intentando!!")
	else:
		print("Casi llegas a la última pregunta, chao!!")

else:
	print("perdiste!!! gracias por jugar")