# Challenge 4
# Date: 12/1/2014
# Created by: Zach Golik



def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (1,2,3,4,5,6,7,8)
    print("I choose square number", end=' ')
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
            print(word)
            return word
