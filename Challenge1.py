# Challenge1.py
# Author: Sam Coon
# Date: 11/18/14

def ask_number(question, low, high, step = 1):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response

ask_number("Give me an even number between 1 and 10: ",1,10,2)
