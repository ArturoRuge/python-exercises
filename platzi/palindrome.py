def palindrome(word):
	reverse_letters = []

	for letter in word:
		reverse_letters.insert(0, letter)

	reverse_word = "".join(reverse_letters)
	print(reverse_word)
	if reverse_word == word:
		return True
	else:
		return False



if __name__ == "__main__":
	word = input("Digita una palabra: ")

	result = palindrome(word)

	if result:
		print("la palabra {} ES un palindromo".format(word))
	else:
		print("la palabra {} NO es un palindromo".format(word))

