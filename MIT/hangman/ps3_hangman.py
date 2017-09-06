# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for c in secretWord:
        if c in lettersGuessed:
            win = True
        else:
            win = False
            break
    return win

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    listGuess = []
    for c in secretWord:
        if c in lettersGuessed:
            listGuess.append(c)
        else:
            listGuess.append(" _ ")
    return "".join(listGuess)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letters_copy = letters[:]
    for i in letters:
            if i in lettersGuessed:
                letters_copy.remove(i)
    return "".join(letters_copy)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("The word has " + str(len(secretWord)) + " letters")
    oportunities = 8
    letGuessed = []

    while oportunities >= 1:
        print("You have " + str(oportunities) + " guesses left")
        print("Available letters: " + getAvailableLetters(letGuessed))
        word = input("Please guess a letter: ")
        if word in letGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, letGuessed))
        else:
            letGuessed.append(word)
            if word in secretWord:
                print("Good gues:" + getGuessedWord(secretWord, letGuessed))
            else:
                print("Oop! That letter is not in my word: " + getGuessedWord(secretWord, letGuessed))
                oportunities -= 1                
            if isWordGuessed(secretWord, letGuessed):
                print("Congratulations, you won!")
                break
    if oportunities == 0:
        print(" Sorry, you ran out of guesses. The word was else. ")

        
        

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
