# Challenge2.py
# Author: Sam Coon
# Date: 11/19/14

import random

def main(question, low, high):
    """Guess number in a range"""
    print("\t\tWelcome to guess my number WITH FUNCTIONS!")
    print("\nThe game is simple I think of a number between a certain range and you try to guess it.")
    print("\nYou only have 10 tries though so guess wisely!")
    number = random.randint(low,high)
    tries = 1
    guess = int(input(question))
    while guess in range(low, high) and guess != number:
        if guess > number:
            print("Lower...")
            guess = int(input(question))
            tries += 1
        elif guess < number:
            print("Higher...")
            guess = int(input(question))
            tries += 1
        if guess == number:
            print("\nYou guessed it and it took you",tries,"tries!")
            print("Thanks for playing!")
        if tries == 10:
            print("\nSorry You have no more tries. The number was",number)
            print("Thanks for playing!")
            guess = 1000
    return guess

game = main("\nGuess a number between 1 and 100: ", 1, 100)
