# Name: Chapter 6 Challenge 1
# Date: November 18, 2014
# Author: Brianna Melius

# improve function ask_number() (pg.179) so function can be called w/ step value, make default value of step 1.

def ask_number(question, low, high):
    question = int(input("Enter a number between 1 and 100: "))
    response = none
    while response not in range(low, high):
        response = int(input(question))
    return response

# valid input
ask_number(question, low, high)
ask_number(question, 1, 1)
ask_number(1, 1, question)
ask_number(1, question, 1)
