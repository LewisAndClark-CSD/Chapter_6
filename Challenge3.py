# Guess My Number(()): Challenge 3
# ENHANCED EDITION of the ENHANCED EDITION
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money(now by using functions)
#
# Last edited: Alton Stillwell
#
######################################################
# Function
def ask_number(guess,answer,tries):
    while guess != answer:
        if guess > answer:
            tries += 1
            guess = int(input("Enter a lower number: "))
        elif guess < answer:
            tries += 1
            guess = int(input("Enter a higher number: "))
        else:
            print("Whhaaaa?")
    tries += 1
    return tries
def main():
    import random  

    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # set the initial values
    answer = random.randint(1, 100)
    guess = int(input("Take a guess: "))
    tries = 0
    end = ''

    # guessing loop
    tries = ask_number(guess, answer, tries)

    # Ending
    if tries < 6:
        print("\nCongrats!")
        print("You guessed the right answer(",answer,")in only",tries,"tries!")
    else:
        print("\nYou have finally guessed the number..")
        print("After",tries,"tries!?!")
        print("I was starting to think you weren't going to be able to do it!")
    input("\n\nPress the enter key to exit.")



    
######################################################
# Main
main()

