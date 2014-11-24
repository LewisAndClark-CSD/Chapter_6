#Challenge_6_1
#11/24/2014
#Dennis Gordick


def ask_number(question, low, high, step):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

ask_number("Give me a number", 1, 100, 1)
