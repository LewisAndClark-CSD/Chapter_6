# Challenge 4
# Author: Alton Stillwell
# Date: 11/19/14
#########################
# Design
#  
########################################################################
def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("I shall take square number",end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
    
