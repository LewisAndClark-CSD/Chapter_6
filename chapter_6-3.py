#Chapter_6-3
#Joe Carty
#12/15/14

def of main():
    
    import random  

    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # set the initial values
    the_number=random.randint(1,100)
    guess = int(input("Take a guess: "))
    tries = 1
    def ask_number(question, low, high, step = 1):
        """Ask a number within a range."""
        response=None
        while response not in range(low, high, step):
            response = int(input(question))
        return responce

    # guessing loop
    while guess != the_number:
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")
                
        guess = int(input("Take a guess: "))
        tries += 1

    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")
      
    input("\n\nPress the enter key to exit.")

