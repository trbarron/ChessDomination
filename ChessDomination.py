import random
import numpy as np
import matplotlib.pyplot as plt

piece = "king"
low_score = [64]
iterations_for_low_score = [0]
iterations = 1000000000

def format_board(board):
    for board_row in board:
        print('\t' + str(board_row))
    
def find_empty_square(piece_board):
    space_available = not (min(min(piece_board)))
    found_empty_square = False
    while space_available and not found_empty_square:
        x = random.randint(0,7)
        y = random.randint(0,7)
        found_empty_square = not piece_board[y][x]
    return [x,y]

def update_attack_board(piece, piece_board, attack_board):
    for x in range(0,8):
        for y in range(0,8):
            if piece_board[y][x] == 0:
                attack_board = attack_from_square(piece,x,y,attack_board)
    return piece_board

def attack_from_square(piece,x,y,attack_board):
    if piece == "horsie" or piece == "knight":
        attack_board[y][x] = 1
        if x > 1:
            if y > 0:
                attack_board[y-1][x-2] = 1
            if y < 7:
                attack_board[y+1][x-2] = 1
        if x > 0:
            if y > 1:
                attack_board[y-2][x-1] = 1
            if y < 6:
                attack_board[y+2][x-1] = 1
        if x < 7:
            if y > 1:
                attack_board[y-2][x+1] = 1
            if y < 6:
                attack_board[y+2][x+1] = 1
        if x < 6:
            if y > 0:
                attack_board[y-1][x+2] = 1
            if y < 7:
                attack_board[y+1][x+2] = 1
    if piece == "bishop" or piece == "diag-man":
        movement = 0
        while max(x+movement,y+movement) < 8:
            attack_board[y+movement][x+movement] = 1
            movement = movement + 1
        movement = 0
        while x-movement >= 0 and y+movement <= 7:
            attack_board[y+movement][x-movement] = 1
            movement = movement + 1
        movement = 0
        while x-movement >= 0 and y-movement >= 0:
            attack_board[y-movement][x-movement] = 1
            movement = movement + 1
        movement = 0
        while x+movement <= 7 and y-movement >= 0:
            attack_board[y-movement][x+movement] = 1
            movement = movement + 1
    if piece == "queen" or piece == "bae":
        movement = 0
        while max(x+movement,y+movement) < 8:
            attack_board[y+movement][x+movement] = 1
            movement = movement + 1
        movement = 0
        while x-movement >= 0 and y+movement <= 7:
            attack_board[y+movement][x-movement] = 1
            movement = movement + 1
        movement = 0
        while x-movement >= 0 and y-movement >= 0:
            attack_board[y-movement][x-movement] = 1
            movement = movement + 1
        movement = 0
        while x+movement <= 7 and y-movement >= 0:
            attack_board[y-movement][x+movement] = 1
            movement = movement + 1
        movement = 0
        while x+movement <= 7:
            attack_board[y][x+movement] = 1
            movement = movement + 1
        movement = 0
        while x-movement >= 0:
            attack_board[y][x-movement] = 1
            movement = movement + 1
        movement = 0
        while y+movement <= 7:
            attack_board[y+movement][x] = 1
            movement = movement + 1
        movement = 0
        while y-movement >= 0:
            attack_board[y-movement][x] = 1
            movement = movement + 1
    if piece == "rook" or piece == "castle":
        movement = 0
        while x+movement <= 7:
            attack_board[y][x+movement] = 1
            movement = movement + 1
        movement = 0
        while x-movement >= 0:
            attack_board[y][x-movement] = 1
            movement = movement + 1
        movement = 0
        while y+movement <= 7:
            attack_board[y+movement][x] = 1
            movement = movement + 1
        movement = 0
        while y-movement >= 0:
            attack_board[y-movement][x] = 1
            movement = movement + 1
    if piece == "king" or piece == "kingEdwardTheThird":
        for x_movement in range(-1,2):
            for y_movement in range(-1,2):
                if (x+x_movement)>= 0 and (x+x_movement) <= 7 and (y+y_movement)>= 0 and (y+y_movement) <= 7:
                    attack_board[y+y_movement][x+x_movement] = 1
    return attack_board

for i in range(0,iterations):
    piece_board = [[0 for i in range(0,8)] for _ in range(0,8)]
    attack_board = [[0 for i in range(0,8)] for _ in range(0,8)]
    pieces_placed = 0
    while min(min(attack_board)) is 0 and pieces_placed < min(low_score):
        [x,y] = find_empty_square(piece_board)
        piece_board[y][x] = 1
        attack_board = attack_from_square(piece,x,y,attack_board)
        pieces_placed = pieces_placed + 1
    if pieces_placed < min(low_score):
        print("piece_board:")
        format_board(piece_board)
        print("attack_board:")
        format_board(attack_board)
        print("Pieces placed: " + str(pieces_placed))
        low_score.append(pieces_placed)
        iterations_for_low_score.append(i)
        print(pieces_placed)
        print(i)
        fig, ax = plt.subplots()
        ax.imshow(piece_board, cmap='Greys', interpolation='nearest')
        ax.set_xticks(np.arange(-0.5, 7.5))
        ax.set_yticks(np.arange(-0.5, 7.5))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xlim(-0.5, 7.5)
        ax.set_ylim(-0.5, 7.5)
        ax.set_title(piece + " domination in " + str(pieces_placed) + " pieces in " + str(i+1) + " iterations")
        ax.grid(color='green',linestyle='-', linewidth=0.5)
        plt.savefig(str(min(low_score))+".png")
