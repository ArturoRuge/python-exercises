string = "abcdefghijklmnopqrstuvwxyz"
carac = "m"

def buscar_carac(carac, string2):
	tam_string = len(string2) - 1
	mitad_string = int(tam_string / 2)
	if carac < string2[0] or carac > string2[-1]:
		return "Caracter o se encuentra en la lista" 
	if carac == string2[mitad_string]:
		return True
	else:
		if carac < string2[tam_string]:
			return buscar_carac(carac, string2[:tam_string])
		else:
			return buscar_carac(carac,string2[tam_string:])

print(buscar_carac(carac, string))