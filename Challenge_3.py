#! /usr/bin/python3
# DD36.py
# Luke Gosnell
# 11/28/2014

# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")
def ask_number(question,low,high,stepValue=1):
    '''Ask for a numberr within a range.'''
    response = None
    while response not in range(low, high, stepValue):
        response = int(input(question))
    return response

# set the initial values
the_number = random.randint(1, 100)
guess = ask_number("Guess: ",1,100)
tries = 1

def main(the_number,guess,tries):
    while guess != the_number:
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")
        guess = ask_number("Guess: ",1,100)
        tries += 1

    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")
  
    input("\n\nPress the enter key to exit.")
main(the_number,guess,tries)
