import pygame
from Tile import Tile


class Grid:
    BORDER_WIDTH = 5

    def __init__(self, w):
        self.w = w
        self.board = [[Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()]]
        self.active_tile = None
        width = w.get_width() // 9

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                t = self.board[i][j]
                t.set_rect(5 + j*width, 5 + i*width, width)

    def draw_grid(self):
        grid = pygame.Rect(5, 5, self.w.get_width() - 10, self.w.get_height() - 10)
        pygame.draw.rect(self.w, (0, 0, 0), grid, self.BORDER_WIDTH)

        for i in range(3):
            pygame.draw.line(self.w, (0, 0, 0), (5 + i*(self.w.get_width() - 10) // 3, 5), (5 + i*(self.w.get_width() - 10) // 3, self.w.get_height() - 5), Grid.BORDER_WIDTH)
        for i in range(3):
            pygame.draw.line(self.w, (0, 0, 0), (5, 5 + i*(self.w.get_height() - 10) // 3), (self.w.get_width() - 5, 5 + i*(self.w.get_height() - 10) // 3), Grid.BORDER_WIDTH)
        for i in range(9):
            pygame.draw.line(self.w, (0, 0, 0), (5 + i*(self.w.get_width() - 10)//9, 5), (5 + i*(self.w.get_width() - 10)//9, self.w.get_height() - 5))
        for j in range(9):
            pygame.draw.line(self.w, (0, 0, 0), (5, 5 + j*(self.w.get_height() - 10)//9), (self.w.get_width() - 5, 5 + j*(self.w.get_height() - 10)//9))

        font = pygame.font.SysFont("Arial", 20, True)

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                tile = self.board[i][j]
                input_box = pygame.Rect(5 + j * (self.w.get_width() - 10) // 9, 5 + i * (self.w.get_width() - 10) // 9, tile.size, tile.size)
                input_font = font.render(str(tile.number), True, (0, 0, 0))
                empty_font = font.render("", True, (0, 0, 0))
                pygame.draw.rect(self.w, tile.color, input_box, 1)
                if tile.number != 0:
                    self.w.blit(input_font, (input_box.x + tile.size//2 - 5, input_box.y + tile.size//2 - 10))
                if tile.number == 0:
                    self.w.blit(empty_font, (input_box.x + tile.size//2 - 5, input_box.y + tile.size//2 - 10))
        pygame.display.update()

    def tile_clicked(self, mpos):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j].rect.collidepoint(mpos):
                    tile = self.board[i][j]
                    input_box = pygame.Rect(5 + j * (self.w.get_width() - 10) // 9, 5 + i * (self.w.get_width() - 10) // 9, tile.size, tile.size)
                    if self.active_tile is None:
                        self.active_tile = tile
                        tile.is_active = not tile.is_active
                    elif self.active_tile is tile:
                        tile.is_active = not tile.is_active
                        self.active_tile = None
                    elif self.active_tile is not tile:
                        self.active_tile.color = tile.INACTIVE_COLOR
                        pygame.draw.rect(self.w, tile.color, input_box, Grid.BORDER_WIDTH // 4)
                        self.active_tile = tile
                        tile.is_active = not tile.is_active

                    if tile.is_active:
                        tile.color = tile.ACTIVE_COLOR
                        pygame.draw.rect(self.w, tile.color, input_box, Grid.BORDER_WIDTH//4)
                    else:
                        tile.color = tile.INACTIVE_COLOR
                        pygame.draw.rect(self.w, tile.color, input_box, Grid.BORDER_WIDTH//4)

                    pygame.display.update()
                    return tile

    def get_board(self):
        result = [[],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  []]
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                tile = self.board[i][j]
                result[i].append(tile.number)

        return result

    def has_active_tile(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j].is_active:
                    return True

        return False
