"""
Tic Tac Toe Player
"""

import math
import copy

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

    if any(None in row for row in board):
        Xmove = sum(row.count("X")for row in board)
        Omove = sum(row.count("O") for row in board)

        if Xmove == Omove:
            return "X"
        else:
            return "O"
    else:
        return



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_moves.add((i,j))
    return available_moves




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i < 3 and j < 3 and board[i][j] is EMPTY:
        nplayer = player(board)
        resultboard = copy.deepcopy(board)
        resultboard[i][j] = nplayer
        return resultboard
    else:
        raise Exception("Move not valid")



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
            return "X"
        elif board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
            return "O"

    for i in range(3):
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            return "X"
        elif board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            return "O"

    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "O"
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "X"
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return "O"
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return "X"

    return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif any(None in row for row in board):
        return False
    else:
        return True




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    cplayer = player(board)

    if terminal(board):
        return None

    if cplayer == "X":
        bestv = -1
        bestm = (-1, -1)
        check = sum(row.count(EMPTY) for row in board)

        if check == 9:
            return bestm

        for action in actions(board):
            move = min_value(result(board, action))
            if move == 1:
                bestm = action
                break
            elif move > bestv:
                bestm = action

        return bestm

    elif player(board) == "O":
        bestv = 1
        bestm = (-1,-1)

        for action in actions(board):
            move = max_value(result(board, action))
            if move == -1:
                bestm = action
                break
            elif move < bestv:
                bestm = action

        return bestm



def max_value(board):
    """
    Function to attempt to get the maximum value possible for the board.
    """
    if terminal(board):
        return utility(board)

    t = -1
    for action in actions(board):
        t = max(t, min_value(result(board, action)))
        if t == 1:
            break

    return t

def min_value(board):
    """
    Function to attempt to get the minimum value possible for the board.
    """
    if terminal(board):
        return utility(board)

    t = 1
    for action in actions(board):
        t = min(t, max_value(result(board, action)))
        if t == -1:
            break

    return t