"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if they are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    # Checkin rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '-':
            return f"{row[0]} wins!"

    # Checkin columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return f"{board[0][col]} wins!"

    # Checkin diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return f"{board[0][0]} wins!"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return f"{board[0][2]} wins!"

    # Checkin if the board is unfinished
    for row in board:
        if '-' in row:
            return "unfinished"

    # Otherwise, it's a draw
    return "draw!"


print(tic_tac_toe_checker([['-', '-', 'o'], ['-', 'x', 'o'], ['x', 'o', 'x']]))
print(tic_tac_toe_checker([['-', '-', 'o'], ['-', 'o', 'o'], ['x', 'x', 'x']]))
print(tic_tac_toe_checker([['-', '-', 'o'], ['-', 'o', 'o'], ['o', 'x', 'x']]))
