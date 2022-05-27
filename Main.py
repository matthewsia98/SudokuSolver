import pygame
from Grid import Grid
from SudokuBoard import SudokuBoard
import time


# Constants
TOTAL_SCREENWIDTH = 1000
SCREENWIDTH = 800
SCREENHEIGHT = 800
BORDER_WIDTH = 4

# Pygame Initialization
pygame.init()
w = pygame.display.set_mode((TOTAL_SCREENWIDTH, SCREENHEIGHT))
w.fill((255, 255, 255))
pygame.display.update()

# Grid Initialization
g = Grid(w, SCREENWIDTH)

# Font Setup
font = pygame.font.SysFont("Arial", 30, True)

# Menu Setup
set_board = font.render("Set Board", True, (0, 0, 0))
set_board_rect = set_board.get_rect()
set_board_rect.center = ((SCREENWIDTH + TOTAL_SCREENWIDTH) // 2, SCREENHEIGHT // 6)
clear_board = font.render("Clear Board", True, (0, 0, 0))
clear_board_rect = clear_board.get_rect()
clear_board_rect.center = ((SCREENWIDTH + TOTAL_SCREENWIDTH) // 2, 2 * SCREENHEIGHT // 6)
reset_board = font.render("Reset Board", True, (0, 0, 0))
reset_board_rect = reset_board.get_rect()
reset_board_rect.center = ((SCREENWIDTH + TOTAL_SCREENWIDTH) // 2, 3 * SCREENHEIGHT // 6)
solve = font.render("Solve", True, (0, 0, 0))
solve_rect = solve.get_rect()
solve_rect.center = ((SCREENWIDTH + TOTAL_SCREENWIDTH) // 2, 4 * SCREENHEIGHT // 6)
next_solution = font.render("Next Solution", True, (0, 0, 0))
next_solution_rect = next_solution.get_rect()
next_solution_rect.center = ((SCREENWIDTH + TOTAL_SCREENWIDTH) // 2, 5 * SCREENHEIGHT // 6)

# Main Loop Variables Initialization
user_input = ''
run = True
board = SudokuBoard()
solutions = None

def draw_menu():
    w.blit(set_board, set_board_rect)
    w.blit(clear_board, clear_board_rect)
    w.blit(reset_board, reset_board_rect)
    w.blit(solve, solve_rect)
    w.blit(next_solution, next_solution_rect)
    

while run:
    w.fill((255, 255, 255))
    draw_menu()
    g.draw_grid(SCREENWIDTH, SCREENHEIGHT)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            tile = g.tile_clicked(mouse_pos, SCREENWIDTH)

            if set_board_rect.collidepoint(mouse_pos):
                copy = g.copy_grid()
                board.set_board(g.get_board())
                if not board.is_valid_board():
                    not_valid = font.render("Invalid Board", True, (255, 0, 0))
                    not_valid_rect = not_valid.get_rect()
                    not_valid_rect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 2)
                    w.blit(not_valid, not_valid_rect)
                    pygame.display.update()
                    time.sleep(2)
                    w.fill((255, 255, 255))
            elif clear_board_rect.collidepoint(mouse_pos):
                g.clear_grid()
                w.fill((255, 255, 255))
                g.draw_grid(SCREENWIDTH, SCREENHEIGHT)
                pygame.display.update()
                board.set_board(g.get_board())
                copy.print_grid()
                print('\n', '-' * 100, '\n')
            elif reset_board_rect.collidepoint(mouse_pos):
                g = copy.copy_grid()
                w.fill((255, 255, 255))
                g.draw_grid(SCREENWIDTH, SCREENHEIGHT)
                pygame.display.update()
                board.set_board(g.get_board())
                copy.print_grid()
                print('\n', '-' * 100, '\n')
            elif solve_rect.collidepoint(mouse_pos):
                solutions = board.solve_all()
                solution = next(solutions)
                for i in range(len(board.board)):
                    for j in range(len(board.board)):
                        tile = g.board[i][j]
                        tile.number = solution.board[i][j]
                g.draw_grid(SCREENWIDTH, SCREENHEIGHT)
                time.sleep(2)
            elif next_solution_rect.collidepoint(mouse_pos):
                w.fill((255, 255, 255))
                pygame.display.update()
                try:
                    solution = next(solutions)
                    for i in range(len(board.board)):
                        for j in range(len(board.board)):
                            tile = g.board[i][j]
                            tile.number = solution.board[i][j]

                    g.draw_grid(SCREENWIDTH, SCREENHEIGHT)
                except StopIteration:
                    no_solution = font.render("No more solutions", True, (255, 0, 0))
                    no_solution_rect = no_solution.get_rect()
                    no_solution_rect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 2)
                    w.blit(no_solution, no_solution_rect)
                    pygame.display.update()
                    time.sleep(2)
                    w.fill((255, 255, 255))
        elif event.type == pygame.KEYDOWN:
            w.fill((255, 255, 255))
            if tile.is_active:
                if event.key == pygame.K_BACKSPACE:
                    tile.set_number(0)
                    g.tile_clicked(mouse_pos, SCREENWIDTH)
                    user_input = ''
                else:
                    user_input += event.unicode
                    try:
                        tile.set_number(int(user_input))
                    except ValueError:
                        pass
                    g.tile_clicked(mouse_pos, SCREENWIDTH)
                    user_input = ''
