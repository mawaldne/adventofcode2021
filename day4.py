import fileinput
import pprint
import numpy as np
pp = pprint.PrettyPrinter(indent=4)

boards = []
board = []
draws = []

for line in fileinput.input():
    if fileinput.isfirstline():
        draws = list(map(int, line.strip().split(",")))
        continue

    if line.strip() == "":
        continue

    board.append(list(map(int, line.strip().split())))
    if len(board) == 5:
        boards.append(board)
        board = []


def transpose(board):
    boardT = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            boardT[j].append(board[i][j])
    return boardT


def bingo(sequence, boards):
    drawn = set()

    for n in sequence:
        drawn.add(n)

        for board in boards:
            for row in (board + transpose(board)):
                if len(set(drawn) & set(row)) == 5:
                    return (n, drawn, board)

last_picked, drawn, board = bingo(draws, boards)
total_unpicked_numbers = sum([sum(set(row) - drawn) for row in board])

print(last_picked * total_unpicked_numbers)
