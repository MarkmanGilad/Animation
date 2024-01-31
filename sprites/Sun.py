import pygame
from Graphics import *

class Sun (pygame.sprite.Sprite):
    def __init__(self, img) -> None:
        super().__init__()
        self.image = img
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(center = (100, 100))
        self.radius = 20
        self.mask = pygame.mask.from_surface(self.image)
                
    def draw (self, surface):
        surface.blit(self.image, self.rect)

    def move (self):
        x, y = self.rect.center
        x = (x + 2) % WIDTH
        y = (y + 1) % HEIGHT
        self.rect.center = x, y
    
    def update(self):
        self.move()
        

        