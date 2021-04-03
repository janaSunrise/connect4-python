import math
import sys

import pygame

from connect4 import RADIUS, SQUARESIZE, screen, width
from .colors import Colors
from .utils import create_board, draw_board, drop_piece, get_next_open_row, is_valid_location, winning_move

board = create_board()
game_over = False
turn = 0

# Initialize
pygame.init()

# Setup the screens
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

# Main game section
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, Colors.BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, Colors.RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, Colors.YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, Colors.BLACK, (0,0, width, SQUARESIZE))
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, Colors.RED)
                        screen.blit(label, (40,10))
                        game_over = True


            # # Ask for Player 2 Input
            else:				
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!", 1, Colors.YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True

            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)
