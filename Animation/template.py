# Animation

import pygame
from Graphics import *
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
screen.fill(LIGHTGRAY)

    
run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
    pygame.display.update()
    clock.tick(FPS)


