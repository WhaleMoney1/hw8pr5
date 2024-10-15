# CSCI 1550: HW 8, Problem 5
# Filename: hw8pr5.py
# Name: Eion
#
# Task: 5-letter word madness ... WORDLE!

import english_words as ew # you don't need to abbreviate the module
wL_var = ew.english_words_set # you can use any variable name you wish

import random


def extractWordleWords(word_list):
    ''' extractWordleWords accepts a list as an argument, and returns a new version of that list, but only filled with words acceptable for wordle
        i.e. words of length 5 and no proper nouns/no special characters
        arguments: 

    '''
    words_as_list = word_list
    newL = []
    for word in words_as_list:
        if len(word) == 5:
            newL += [word]
    
    validletters = 0
    outList = []
    for word in newL:
        for lett in word:
            if ('a' <= lett <= 'z'): # a valid letter 
                validletters += 1 # ( 97 <= x <= 122
            else:
                validletters += 0
        if validletters == 5:
            outList += [word]
        validletters = 0

    return outList 

def exactMatchLocs(word,guess):
    ''' exactMatchLocs takes in two strings, word and guess, and returns a List containing the indecees where word and guess have the same character in at the same index value
    inputs: word, a string
            guess, a string
    returns: a list of indecees (integers)
    '''
    exactMatches = []
    for lett in range(len(word)):
        if word[lett] == guess[lett]:
            exactMatches += [lett]
    return exactMatches

def partialMatchLocs(word,guess):
    ''' partialMatchLocs takes in two strings, word and guess, and returns a List containing the indecees where word and guess have the same letter but at different indecees, additionally, if there is more that one location where the guess has more than one partial match in word, it only returns the index for the first index location
    inputs: word, a string
            guess, a string
    returns: a list of indecees (integers)
    '''
    wordAsList = list(word)
    guessAsList = list(guess)

    partialMatches = []
    for lett in range(len(wordAsList)):
        if (wordAsList[lett] != guessAsList[lett]) and (guessAsList[lett] in wordAsList): #NOT DONE!!!
            partialMatches += [lett]
            for i in range(len(wordAsList)):
                if wordAsList[i] == guess[lett]:
                    wordAsList[i] = '/0' # acts kinda like a NULL
                    break
    return partialMatches

def upperCase(myLetter):
    ''' upperCase accepts a single letter and returns uppercase version, if not given a lowercase letter, will return the given input
    '''
    if 97 <= ord(myLetter) <= 122:
        return chr(ord(myLetter)-32)
    return myLetter

def wordleMatch(word,guess):
    '''
    '''
    list_form_out = ['*','*','*','*','*']
    correctLetts = exactMatchLocs(word,guess)
    partialLetts = partialMatchLocs(word,guess)
    for i in partialLetts:
        list_form_out[i] = guess[i]
    for i in correctLetts:
        list_form_out[i] = upperCase(guess[i])
    
    outWord = ''
    for e in list_form_out:
        outWord += str(e)

    return str(outWord)


def myWordle():
    ''' myWordle simulates a game of wordle, it prompts the user for a five letter word and compares it to a randomly selected word. Each round myWordle will display the letters match exactly and also patially, The player is given 6 guesses to guess the hidden word and the game ends if either the player correctly guesses the word or if the player exausts their guesses

    inputs: no inputs but prompts the user for a word as a guess
    returns: nothing but tells the player if they have won or lost
    '''
    hiddenWord = random.choice(extractWordleWords(wL_var))
    numGuesses = 6

    while numGuesses > 0:
        userGuess = input('please enter a 5 letter guess ')
        while [userGuess] != extractWordleWords([userGuess]):
            userGuess = input('Not a valid input, please enter 5 letter word ')
        Temp = wordleMatch(hiddenWord,userGuess)
        if userGuess == hiddenWord:
            print('You Win!')
            return Temp
        print(Temp)
        numGuesses = numGuesses - 1
        print("number of guesses left ", numGuesses)
    print("out of guesses...\n you lose :(")
    print('The hidden word was',hiddenWord)
    return Temp
