# Challenge 1
# Date: 11/18/2014
# Created by: Zach Golik
def answer():
    import random
    answer = random.randint(1, 100)
    
def ask_number(guess, answer):
    
    while guess != answer:
        guess = int(input("What is my number? "))
        if guess > answer:
            guess = int(input("Lower... "))
            tries += 1
        elif guess < answer:
            guess = int(input("Higher... "))
            tries += 1
        else:
            print("CORRECT! :D")
            tries += 1




           
