

import numpy as np
import pygame
from color import BLACK, RED, BLUE, YELLOW

pygame.init()

colors = [BLACK, RED, YELLOW]

ROW_COUNT = 6
COLUMN_COUNT = 7

# Display variables
DIST = 80
RADIUS = DIST // 2
WIDTH = COLUMN_COUNT * DIST
HEIGHT = (ROW_COUNT + 1) * DIST

window = pygame.display.set_mode((WIDTH, HEIGHT))

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, col, player):
    if not is_valid(board, col):
        return
    global turn
    turn = (turn+1) % 2
    row = ROW_COUNT-1
    while row > 0 and board[row-1][col] == 0:
        row -= 1
    board[row][col] = player
    check_win(board, row, col, player)

def print_win(board, player):
    print_board(board)
    print('Player {} won.'.format(player))

def check_win(board, row, col, player):
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
        truth = [lst[i]!=0, lst[i+1]!=0, lst[i+2]!=0,lst [i+3]!=0]
        if False not in truth:
            if lst[i] == lst[i+1] and lst[i+1] == lst[i+2] and lst[i+2] == lst[i+3]:
                print_win(board, player)
                game_over = True

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
        truth = [lst[i]!=0, lst[i+1]!=0, lst[i+2]!=0, lst[i+3]!=0]
        if False not in truth:
            if lst[i] == lst[i+1] and lst[i+1] == lst[i+2] and lst[i+2] == lst[i+3]:
                print_win(board, player)
                game_over = True

    # Check the column at index colcol
    lst = []
    for i in range(ROW_COUNT):
        lst.append(board[i][col])
    for i in range(len(lst)-3):
        truth = [lst[i]!=0, lst[i+1]!=0, lst[i+2]!=0, lst[i+3]!=0]
        if False not in truth:
            if lst[i] == lst[i+1] and lst[i+1] == lst[i+2] and lst[i+2] == lst[i+3]:
                print_win(board, player)
                game_over = True

    # Check the row at index row
    lst = []
    for i in range(COLUMN_COUNT):
        lst.append(board[row][i])
    for i in range(len(lst)-3):
        truth = [lst[i]!=0, lst[i+1]!=0, lst[i+2]!=0, lst[i+3]!=0]
        if False not in truth:
            if lst[i] == lst[i+1] and lst[i+1] == lst[i+2] and lst[i+2] == lst[i+3]:
                print_win(board, player)
                game_over = True

def print_board(board):
    print(np.flip(board, axis=0))

def is_valid(board, col):
    if board[ROW_COUNT-1][col] != 0:
        print('Full column.')
        return False
    return True

def draw_board(surface, board, player):
    surface.fill(BLACK) # Clear the display
    pygame.draw.rect(surface, BLUE, (0, DIST, WIDTH, HEIGHT-DIST)) # Draw the playing board
    
    # Draw the piece to be dropped
    pos = (pygame.mouse.get_pos()[0], RADIUS)
    pygame.draw.circle(surface, colors[player], pos, RADIUS-4)

    # Draw circles according to the values inside the board variable
    for j in range(COLUMN_COUNT):
        for i in range(ROW_COUNT):
            pos = (DIST*j+RADIUS, HEIGHT - (DIST*i+RADIUS))
            c = int(board[i][j])
            pygame.draw.circle(surface, colors[c], pos, RADIUS-4)
    pygame.display.update()

def get_input(board, player):
    if pygame.mouse.get_pressed()[0] == True:
        mouse_pos_x = pygame.mouse.get_pos()[0]
        col = mouse_pos_x//DIST
        drop_piece(board, col, player)

def main():
    global board
    global game_over
    global turn

    board = create_board()
    game_over = False
    turn = 0
    print_board(board)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                get_input(board, turn+1)
        draw_board(window, board, turn+1)

if __name__ == '__main__':
    main()