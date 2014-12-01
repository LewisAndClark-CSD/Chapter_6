# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money
# Edited by: Zach Golik
# Added a limit to the amount of guesses

# guessing loop    
def ask_number(guess, answer):
    guess = int(input("What is my number? "))
    while guess != answer:
        if guess > answer:
            guess = int(input("Lower... "))
        elif guess < answer:
            guess = int(input("Higher... "))
        else:
            print("CORRECT! :D")
            

def main():
    
    import random
    guess = None
    answer = random.randint(1, 100)

    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")


    ask_number(guess, answer)

    print("You answered correctly! :D")
    input("Press enter to exit ")

main()
