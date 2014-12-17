#ask_number.py
#Joe Carty
#12/11/14

def ask_number(question, low, high, step = 1):
    """Ask a number within a range."""
    response=None
    while response not in range(low, high, step):
        response = int(input(question))
    return responce
