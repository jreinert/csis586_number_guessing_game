# Author: Jeremy Reinert
# Date: 1/17/2020
# Version: 1.0

# hw1-reinert.py

"""Generates a random number between 1 and 1000, asks a player to guess the number, and prompt the user to play again when they guess the correct number"""

#Import Modules
import random

# Initialize Variables
num = random.randrange(1, 1000)
run = True
guess = 0
minGuess = 0
numGuess = 0
timesPlayed = 0

# While loop to play
while run == True:
    timesPlayed += 1
    # While loop to check that guess does not equal num
    while guess != num:
        
        # Prompt user for input and cast str input to int
        guess = input('Guess my number between 1 and 1000 with the fewest guesses ')
        numGuess += 1
        isNum = False

        # Check if input is a number or prompt user to enter a number if not
        while isNum == False:
            if guess.isdigit():
                guess = int(guess)
                isNum = True
            else:
                guess = input('You did not enter a number. Please guess my number between 1 and 1000 with the fewest guesses ')        
        
        # Check if guess is greater than num
        if guess > num:
            print('Too high. Try again.')
            print('Guesses: ' + str(numGuess))

        # Check if guess is less than num
        elif guess < num:
            print('Too low. Try again.')
            print('Guesses: ' + str(numGuess))

        # Check if guess equals num
        elif guess == num:
            print('Congratulations. You guessed the number!')
            print('Guesses: ' + str(numGuess))

            if timesPlayed == 1:
                minGuess = numGuess
                print('Minimum Number of Guesses: ' + str(minGuess))
            elif timesPlayed > 1:
                if minGuess > numGuess:
                    minGuess = numGuess
                    print('Minimum Number of Guesses: ' + str(minGuess))

    # Prompt user to play again
    playAgain = input("Do you want to play again? 'Y' for Yes and 'N' for No ")
    playAgain = playAgain.upper()
    
    # Check if input equals Y
    if playAgain == 'Y':
        guess = 0
        num = random.randrange(1,1000)
        numGuess = 0
    
    # Check if input equals N
    elif playAgain == 'N':
        print('Thanks for playing Guess the Number with me')
        break
