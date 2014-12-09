# ask_number
# author: Bo Meers


def ask_number():
    import random
    the_number = random.randint(1, 100)
    guess = int(input("Take a guess: "))
    tries = 1

    # guessing loop
    while guess != the_number:
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")
            
        guess = int(input("Take a guess: "))
        tries += 1
        
ask_numer()
