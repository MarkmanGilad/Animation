import pygame
from Graphics import *

class Sun (pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("img/sun.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(center = (100, 100))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.move(1,1)

    def move (self, dx, dy):
        x, y = self.rect.center
        x = (x + dx) % WIDTH
        y = (y + dy) % HEIGHT
        self.rect.center = x, y
    
    

        