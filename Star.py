import pygame
from Graphics import *

class SpaceShip (pygame.sprite.Sprite):
    def __init__(self, img_Url, pos) -> None:
        super().__init__()
        self.image = pygame.image.load(img_Url)
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(midbottom = pos)
        

    def update(self):
        self.move(2,3)

    def move (self, dx, dy):
        x, y = self.rect.midbottom
        x = (x + dx) % WIDTH
        y = (y + dy) % HEIGHT
        self.rect.midbottom = x, y

        