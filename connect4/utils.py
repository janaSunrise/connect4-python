import numpy as np
import pygame

from connect4 import COLUMN_COUNT, RADIUS, ROW_COUNT, SQUARESIZE, height, screen
from .colors import Colors


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def winning_move(board, piece):
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, Colors.BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(
                screen,
                Colors.BLACK,
                (int(c * SQUARESIZE + SQUARESIZE / 2),
                int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)),
                RADIUS
            )

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):		
            if board[r][c] == 1:
                pygame.draw.circle(
                    screen,
                    Colors.RED,
                    (int(c * SQUARESIZE + SQUARESIZE / 2),
                    height - int(r * SQUARESIZE + SQUARESIZE / 2)),
                    RADIUS
                )
            elif board[r][c] == 2: 
                pygame.draw.circle(
                    screen,
                    Colors.YELLOW,
                    (int(c * SQUARESIZE + SQUARESIZE / 2),
                    height - int(r * SQUARESIZE + SQUARESIZE / 2)),
                    RADIUS
                )

    pygame.display.update()
