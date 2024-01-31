import pygame
from Graphics import *

class SpaceShip (pygame.sprite.Sprite):
    def __init__(self, image) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.radius = 30
        self.mask = pygame.mask.from_surface(self.image) 

    def move (self, dx, dy):
        x, y = self.rect.midbottom
        x = (x + dx) % WIDTH
        y = (y + dy) % HEIGHT
        self.rect.midbottom = x, y

    def draw (self, surface):
        surface.blit(self.image, self.rect)

    def update(self, dx, dy): # for sprite Group
        self.move(dx,dy)
