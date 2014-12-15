#Chapter6-1.py
#Karl Pearson
#12/9/2014

def ask_number(question, low, high, step=1):
    """Ask for a number within a range."""
    response=None
    while response not in range(low, high, step):
        response=int(input(question))
    return response
