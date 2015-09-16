
import random
import string

WORDLIST_FILENAME = "words.txt"

#loading words from file
def loadWords():
    """Returns: list of valid words, strings of lowercase letters."""
    
    print "Loading word list...."

    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print len(wordlist), "words loaded."
    return wordlist


#choosing a random word
def chooseWord(wordlist):
    """wordlist : list of words (strings)
       Returns a random word from wordlist"""
    
    return random.choice(wordlist)

#check if work is guessed
def isWordGuessed(secretWord, lettersGuessed):
    '''secretWord: string, the word to be guessed
       lettersGuessed: list, what letters have been guessed so far
       returns: boolean, True if all the letters of secretWord are in lettersGuessed;
                False otherwise'''
    total=[]
    for i in secretWord:
        if i in lettersGuessed:
            total+= [1]
        else:
            total+= [0]
        
    
    if 0 in total:
        return False
    else:
        return True

# get the word guessed so far
def getGuessedWord(secretWord, lettersGuessed):
    '''secretWord: string, the word the user is guessing
       lettersGuessed: list, what letters have been guessed so far
       returns: string, comprised of letters that have been guessed so far and underscores where the letters still have to be guessed'''
    
    ans=''
    for i in secretWord:
        if i in lettersGuessed:
            ans+=i
        else:
            ans+='_'
    return ans

#get alphabets still available to guess
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not yet been guessed.'''
    
    all='abcdefghijklmnopqrstuvwxyz'
    avail=''
    used=''
    for i in all:
        if i in lettersGuessed:
            used+=i
            
        else:
            avail+=i
            
    return avail
    
#starts game
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    * let the user know how many letters the secretWord contains.
    * Ask the user to supply one guess per round.
    * The user receives feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, display to the user the partially guessed word so far, and letters available to be guessed.'''
    
    print 'Welcome to the game, Hangman!'
    
    print'I am thinking of a word that is '+ str(len(secretWord)) +' letters long.'
    
    print '-----------'
    
    lettersGuessed=[]

    chances=8
    guessedWord=[]
    while chances>0:
        
        
        if '_' in getGuessedWord(secretWord,lettersGuessed):
              print 'You have '+ str(chances) +' guesses left.'
              print 'Available letters:'+ getAvailableLetters(lettersGuessed)
              guess=raw_input('Please guess a letter:')
              guessInLowerCase = guess.lower()
        
              if guessInLowerCase in lettersGuessed:
                    print "Oops! You've already guessed that letter:"+ getGuessedWord(secretWord, lettersGuessed)
                    print '-----------'
              else:
            
                            if guessInLowerCase in secretWord:
                            
                               guessedWord+=guessInLowerCase
                               lettersGuessed+=guessInLowerCase
                               print 'Good guess:'+ getGuessedWord(secretWord, lettersGuessed)
                               print '-----------'
                            else:
                               
                               chances-=1
                               lettersGuessed+=guessInLowerCase
                               print 'Oops! That letter is not in my word:'+ getGuessedWord(secretWord, lettersGuessed)
                               print '-----------'
        else:
             break
        
    if '_' in getGuessedWord(secretWord,lettersGuessed):
        print 'Sorry, you ran out of guesses. The word was '+ secretWord + '.'
    else:
        print 'Congratulations, you won!'

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
