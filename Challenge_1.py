#! /usr/bin/python3
# Challenge_1.py
# Luke Gosnell
# 11/26/2014

# Design:
# Function can be called with a step value

def ask_number(question,low,high,stepValue=1):
    '''Ask for a numberr within a range.'''
    response = None
    while response not in range(low, high, stepValue):
        response = int(input(question))
    return response
