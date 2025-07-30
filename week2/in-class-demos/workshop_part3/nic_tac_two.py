p1 = "X"
p2 = "O"

board = {"A": {0: "-", 1: "-", 2: "-"}, "B": {0: "-", 1: "-", 2: "-"}, "C": {0: "-", 1: "-", 2: "-"}}

def print_board(board):
    print(f"{board['A'][0]} | {board['A'][1]} | {board['A'][2]}")
    print("---------")
    print(f"{board['B'][0]} | {board['B'][1]} | {board['B'][2]}")
    print("---------")
    print(f"{board['C'][0]} | {board['C'][1]} | {board['C'][2]}")

def check_win(board):
    x_pos = []
    o_pos = []
    for row in board.keys():
        for pos in board[row].keys():
            if board[row][pos] == p1:
                x_pos.append((row, pos))
            elif board[row][pos] == p2:
                o_pos.append((row, pos))

print_board(board)