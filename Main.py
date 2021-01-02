import pygame
from Grid import Grid
from SudokuBoard import SudokuBoard
import time


# Constants
TOTAL_SCREENWIDTH = 1000
SCREENWIDTH = 600
SCREENHEIGHT = 600
BORDER_WIDTH = 4

# Pygame Initialization
pygame.init()
w = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
w.fill((255, 255, 255))
pygame.display.update()

g = Grid(w)

# Font Setup
font = pygame.font.SysFont("Arial", 22, True)

user_input = ''
run = True
g.draw_grid()
counter = 0

while run:
    g.draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            tile = g.tile_clicked(mouse_pos)
        elif event.type == pygame.KEYDOWN:
            w.fill((255, 255, 255))
            if tile.is_active:
                if event.key == pygame.K_BACKSPACE:
                    tile.set_number(0)
                    g.tile_clicked(mouse_pos)
                    user_input = ''
                else:
                    user_input += event.unicode
                    try:
                        tile.set_number(int(user_input))
                    except ValueError:
                        pass
                    g.tile_clicked(mouse_pos)
                    user_input = ''

            if event.key == pygame.K_RETURN:
                board = SudokuBoard()
                board.set_board(g.get_board())
                board.solve()
                for i in range(len(board.board)):
                    for j in range(len(board.board)):
                        tile = g.board[i][j]
                        tile.number = board.solutions[counter].board[i][j]

            elif event.key == pygame.K_SPACE:
                counter += 1
                if counter < len(board.solutions):
                    for i in range(len(board.board)):
                        for j in range(len(board.board)):
                            tile = g.board[i][j]
                            tile.number = board.solutions[counter].board[i][j]
                else:
                    w.fill((255, 255, 255))
                    game_over = font.render("No more solutions", True, (0, 0, 0))
                    text_game_over = game_over.get_rect()
                    text_game_over.center = (SCREENWIDTH//2, SCREENHEIGHT//2)
                    w.blit(game_over, text_game_over)
                    pygame.display.update()
                    time.sleep(2)
                    run = False
