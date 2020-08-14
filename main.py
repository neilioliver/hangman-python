# Hangman
# Neil Pasco
# 2020-08-13


import random


# The intro to the player
def intro():
    print("Hello! Please type in your name!")
    name = input()
    print('Welcome to Hangman, ', name, "!", sep="")
    return name


# Import the dictionary
def importwords():
    wordList = []
    for line in open("wordlist.txt"):
        wordList.append(line.rstrip('\n'))
    return wordList


# Create a random word based on dictionary length
def rand_word(a):
    chosen = random.choice(a)
    return chosen


# Check every letter to see if it matches
# b is word to guess, g is number of guesses
def checker(b, g):
    # Hidden word will be initially asterisks only, and will slowly reveal:
    Hidden = list("*" * len(b))

    # Get list of unique letters from word to guess
    uniques = list(set(b))

    # Boolean variable that governs if word guess is correct or not - stops the while loop
    correctguess = False

    # Initialize empty list of already guessed letters and words
    guesslist = []
    guesslistWrd = []

    while g > 0 or correctguess is False:
        print('Word to guess: ', "".join(Hidden))
        print('Number of guesses = ', g)

        letterguess = input()

        # If the letter you guess is in the word, then replace the asterisks in string with the letter'
        if letterguess in b and len(letterguess) == 1:
            for i in range(len(Hidden)):
                if letterguess == b[i]:
                    Hidden[i] = letterguess

            # If the letter you guess is in the list of already guessed words, notify user and do not penalize
            if letterguess in guesslist:
                print('=> You already guessed the letter', letterguess, 'and it exists.')
            else:
                print('=>', letterguess, 'exists.')

        # If letter you guess is not in word,
        elif len(letterguess) == 1:
            # ...do not deduct a guess if the letter has already been guessed before
            if letterguess in guesslist:
                print('=> You already guessed the letter', letterguess, 'and it does not exist.')
            # ...deduct a guess if the first time guessing it
            else:
                g = g - 1
                print('=>', letterguess, 'does not exist.')

        # If user inputs a word, then check to see if it matches our hidden word
        elif len(letterguess) > 0:
            if list(letterguess) == list(b):
                print('You guessed the word correct!')
                correctguess = True
                break
            else:
                if letterguess in guesslistWrd:
                    print('=> You already guessed the word "', letterguess, '" and it is incorrect.')
                else:
                    g = g - 1
                    print('=> Sorry, wrong word!')
                    if g == 0:
                        break

        if len(letterguess) == 1:
            guesslist.append(letterguess)
            guesslist = list(set(guesslist))
        elif len(letterguess) > 1:
            guesslistWrd.append(letterguess)
            guesslistWrd = list(set(guesslistWrd))
            
        print('Unique letters guessed:', ",".join(guesslist))
        print('Unique words guessed:', ",".join(guesslistWrd))
        print('----------------------------')
        print()

    if g <= 0:
        print('----------------------------')
        print()
        print("Game Over")
        print(">= The word was:", b)
    elif correctguess:
        print('----------------------------')
        print()
        print("Congrats, YOU WON!!")


if __name__ == '__main__':
    # Introduction
    intro()

    # Import our dictionary
    dict = importwords()

    # Our chosen word from the dictionary
    Word2Guess = rand_word(dict)

    # Word length
    W_length = len(Word2Guess)

    # No. of guesses
    guesses = 8
    checker(Word2Guess, guesses)
