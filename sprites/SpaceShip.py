import pygame
from Graphics import *

class SpaceShip (pygame.sprite.Sprite):
    def __init__(self, image, pos) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(midbottom = pos)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dx, dy):
        self.move(dx,dy)

    def move (self, dx, dy):
        x, y = self.rect.midbottom
        x = (x + dx) % WIDTH
        y = (y + dy) % HEIGHT
        self.rect.midbottom = x, y

    