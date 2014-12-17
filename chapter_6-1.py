#Chapter_6-1
#Joe Carty
#12/15/14

def ask_number(question, low, high, step = 1):
    """Ask a number within a range."""
    response=None
    while response not in range(low, high, step):
        response = int(input(question))
    return responce
