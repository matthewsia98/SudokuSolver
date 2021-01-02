import pygame


class Tile:
    ACTIVE_COLOR = (0, 255, 0)
    INACTIVE_COLOR = (0, 0, 0)

    def __init__(self):
        self.number = 0
        self.is_active = False
        self.color = self.INACTIVE_COLOR

    def set_number(self, n):
        self.number = n

    def set_rect(self, x, y, size):
        self.size = size
        self.rect = pygame.Rect(x, y, size, size)

    def draw_number(self):
        pass
