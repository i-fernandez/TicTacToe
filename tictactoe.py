# MODULES
import sys
import pygame
import numpy as np

from constants import *


# PYGAME SETUP
pygame.init()
screen =  pygame.display.set_mode( (WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill(BG_COLOR)


class Board:

    def __init__(self) -> None:
        self.squares = np.zeros( (ROWS, COLS) )
        self.empty_sqrs = self.squares  # list of empty squares
        self.marked_sqrs = 0
        

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0


# 45:44

class Game:

    def __init__(self) -> None:
        self.board = Board()
        self.player = 1   # player 1: cross, player 2: circle
        self.show_lines()

    def show_lines(self):
        # vertical lines
        pygame.draw.line(screen, LINE_COLR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)
        
        # horizontal lines
        pygame.draw.line(screen, LINE_COLR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    def draw_fig(self, row, col):
        if self.player == 1:
            # draw cross
            # desc line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE  + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            # asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)


        elif self.player == 2:
            # draw circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRCLE_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1 

def main():

    game = Game()
    board = game.board
    
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // SQSIZE
                col = event.pos[0] // SQSIZE
                if board.empty_sqr(row, col):
                    game.board.mark_sqr(row, col, game.player)
                    game.draw_fig(row, col)
                    game.next_turn()
                    



        pygame.display.update()


main()