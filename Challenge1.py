def ask_number(question, low=1, high=100, stepValue=1):
    """Ask a yes or no question"""
    response=None
    while response not in range(low, high, stepValue=1):
        reponse=int(input(question))
    return response
