# Chapter 6, Challenge 1
# Pg. 179
# Author: Alton Stillwell
# Date: 11/18/14
#########################
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
