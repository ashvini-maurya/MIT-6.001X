# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    
    print len(wordlist), "words loaded."



   
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
    
    for char in secretWord:
	if (char in lettersGuessed):
		return True
	
    return False
    		


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    leftWord = ""
    for char in secretWord:
    	addedChar = ""
	if char in lettersGuessed:
		addedChar = char
	else:
		addedChar = "_ "
	leftWord += addedChar
    return leftWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    
    import string
    available = ""
    for char in string.ascii_lowercase:
	if not (char in lettersGuessed):
		available += char
    return available


def newGuess(guessesLeft, availableLetters):
    print "-----------------"
    print "You have " + str(guessesLeft) + "guesses left."
    print "Available letters: " + availableLetters
    guess = raw_input("Please guess a letter: ")
    return guess

	
    
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


    print "Welcome to hangman!"
    print "I am thinking of a word " + str(len(secretWord)) + " letters long."

   
    letters_guessed = [] 
    letters_available = getAvailableLetters(letters_guessed)

    num_guesses = "" 


    while (num_guesses > 0 and not isWordGuessed(secretWord, letters_guessed)):
   	 g = newGuess(num_guesses, letters_available).lower()

	 guessed = getGuessedWord(secretWord, letters_guessed)
	
	 if g in letters_guessed:
		 print "Ooops! You have already guessed that letter: " + guessed
	 else:
		 letters_guessed.append(g)
		 letters_available = getAvailableLetters(letters_guessed)
		 guessed = getGuessedWord(secretWord, letters_guessed)

		
		 if g in secretWord: 
		       	 print "Good Guess: " + guessed
		 else:
			 num_guesses = float(num_guesses) - 1
			 print "Ooops! That letter is not in my word: " + guessed

    print "------------"

    if (isWordGuessed(secretWord, letters_guessed)):
	print "Congrats, u won!"	
    else:
	print "Sorry, u ran out of guesses. Tha word was " + secretWord







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
