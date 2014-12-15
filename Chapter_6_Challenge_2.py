# Name: Chapter 6 Challenge 2
# Date: November 18, 2014
# Author: Brianna Melius

# Design: modify "guess my number" from ch. 3 by reusing the function ask_number().

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# use function in place of loop
def ask_number(question, low, high):
    question = int(input("Enter a number between 1 and 100: "))
    response = none
    while response not in range(low, high):
        response = int(input(question))
    tries += 1
    return response

ask_number(question, low, high)

print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
