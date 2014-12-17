def ask_number(question, low=1, high=100, stepValue=1):
    """Ask for a number within a range."""
    response=None
    while response not in range(low, high, stepValue):
        response=int(input(question))
    return response
 
