"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = {'X': 0, 'O': 0, None: 0}
    for i in board:
        for j in i:
            count[j] = count[j] + 1
    
    if count[X] == count[O]:
        return X
    else:
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add(tuple([i,j]))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    boardCopy = deepcopy(board)

    if boardCopy[action[0]][action[1]] == EMPTY:

        getPlayer = player(board)
        boardCopy[action[0]][action[1]] = getPlayer
        return boardCopy
    else:
        raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):

        if board[i][0] != EMPTY and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]

        if board[0][i] != EMPTY and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]

    if board[1][1] != EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[1][1]

    if board[1][1] != EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    getWinner = winner(board)

    if getWinner != None:
        return True
    else:
        isOver = True

        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    isOver = False

        return isOver


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    getWinner = winner(board)

    if getWinner == X:
        return 1
    elif getWinner == O:
        return -1
    else:
        return 0

def min_value(board):
    if terminal(board):
        return utility(board)
    else:
        v = -2
        for action in actions(board):
            v = max(v, max_value(result(board, action)))
        return v


def max_value(board):
    if terminal(board):
        return utility(board)
    else:
        v = 2
        for action in actions(board):
            v = min(v, min_value(result(board, action)))
        return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    else:

        if player(board) == X:
            v = -2
            optimalMove = None
            for action in actions(board):
                max = max_value(result(board, action))
                if max > v:
                    v = max
                    optimalMove = action
            return optimalMove
        
        elif player(board) == O:
            v = 2
            optimalMove = None
            for action in actions(board):
                min = min_value(result(board, action))
                if min < v:
                    v = min
                    optimalMove = action
            return optimalMove