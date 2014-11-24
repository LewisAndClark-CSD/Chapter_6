#Challenge_6_2
#11/24/2014
#Dennis Gordick

# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

def ask_number(question, low, high, step):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
    tries += step
    

#Opening Remarks
print("Welcome to 'Guess My Number'!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

# set the initial values
the_number = random.randint(1, 100)
# Create the priming read here
tries = 0
guess= 0
while int(guess) != int(the_number):

    guess = ask_number("Enter your guess:", 1, 100, 1)

    if int(guess) == int(the_number):
        print("Your right on the money!")
    elif int(guess) > int(the_number):
        print("To high!")
    elif int(guess) < int(the_number):
        print("To low!")

    tries += 1
#Didnt know how to make it reloop to the start...
print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!")

#Program Closing  
input("Press the enter key to exit.")

