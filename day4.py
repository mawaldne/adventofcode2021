import fileinput

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


def bingo(sequence, boards, last):
    wins = set()
    drawn = set()

    for last_picked in sequence:
        drawn.add(last_picked)

        for i, board in enumerate(boards):
            for row in (board + transpose(board)):
                if len(set(drawn) & set(row)) == len(row):
                    wins.add(i)
                    if not last or len(wins) == len(boards):
                        return (last_picked, drawn, board)

last_picked, drawn, board = bingo(draws, boards, False)
total_unpicked_numbers = sum([sum(set(row) - drawn) for row in board])

print(last_picked * total_unpicked_numbers)

last_picked, drawn, last_board = bingo(draws, boards, True)
total_unpicked_numbers = sum([sum(set(row) - drawn) for row in last_board])

print(last_picked * total_unpicked_numbers)



