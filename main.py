

import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, col, player):
    row = ROW_COUNT-1
    while row > 0 and board[row-1][col] == 0:
        row -= 1
    board[row][col] = player
    check_win(board, row, col)

def check_win(board, row, col):
    global game_over

    # Check the primary diagonal from the indexes (row,col)
    lst = []
    r = row - 1
    c = col - 1
    while r >= 0 and c >= 0:
        lst.append(board[r][c])
        r -= 1
        c -= 1
    lst.reverse()
    lst.append(board[row][col])
    r = row + 1
    c = col + 1
    while r < ROW_COUNT and c < COLUMN_COUNT:
        lst.append(board[r][c])
        r += 1
        c += 1
    for i in range(len(lst)-3):
        truth = [lst[i] != 0, lst[i+1]!=0,lst[i+2]!=0,lst[i+3]!=0]
        if False not in truth:
            if lst[i] == lst[i+1] and lst[i+1] == lst[i+2] and lst[i+2] == lst[i+3]:
                game_over = True
                return True

    # Check the secondary diagonal from the indexes (row,col)
    lst = []
    r = row - 1
    c = col + 1
    while r >= 0 and c < COLUMN_COUNT:
        lst.append(board[r][c])
        r -= 1
        c += 1
    lst.reverse()
    lst.append(board[row][col])
    r = row + 1
    c = col - 1
    while r < ROW_COUNT and c >= 0:
        lst.append(board[r][c])
        r += 1
        c -= 1
    for i in range(len(lst)-3):
        truth = [lst[i] != 0, lst[i+1]!=0,lst[i+2]!=0,lst[i+3]!=0]
        if False not in truth:
            if lst[i] == lst[i+1] and lst[i+1] == lst[i+2] and lst[i+2] == lst[i+3]:
                game_over = True
                return True


    # Check the column from the indexes (row, col)
    lst = []
    for i in range(ROW_COUNT):
        lst.append(board[i][col])
    for i in range(len(lst)-3):
        truth = [lst[i] != 0, lst[i+1]!=0,lst[i+2]!=0,lst[i+3]!=0]
        if False not in truth:
            if lst[i] == lst[i+1] and lst[i+1] == lst[i+2] and lst[i+2] == lst[i+3]:
                game_over = True
                return True

    # Check the row from the indexes (row, col)
    lst = []
    for i in range(COLUMN_COUNT):
        lst.append(board[row][i])
    for i in range(len(lst)-3):
        truth = [lst[i] != 0, lst[i+1]!=0,lst[i+2]!=0,lst[i+3]!=0]
        if False not in truth:
            if lst[i] == lst[i+1] and lst[i+1] == lst[i+2] and lst[i+2] == lst[i+3]:
                game_over = True
                return True

def print_board(board):
    print(np.flip(board, axis=0))

def is_valid(board, col):
    if col < 0 or col > COLUMN_COUNT - 1:
        print('Position out of bounds')
        return False
    if board[ROW_COUNT-1][col] != 0:
        print('Full column.')
        return False
    return True

board = create_board()
game_over = False
turn = 0

while not game_over:
    print_board(board)
    while True:
        col = int(input('Player {} make a selectoin (0-6): '.format(turn+1)))
        if is_valid(board, col) == True:
            break
    drop_piece(board, col, turn+1)
    turn = (turn + 1) % 2

print_board(board)
if turn == 0:
    turn = 2
print('Player {} won.'.format(turn))