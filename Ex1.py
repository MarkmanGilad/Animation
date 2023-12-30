# Animation

import pygame
from Graphics import *
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
screen.fill(LIGHTGRAY)

space_ship = pygame.image.load("img/space_ship.png")
space_ship = pygame.transform.scale(space_ship, (40, 40))

x, y = 50, 50
dx, dy = 2, 2
    
run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(LIGHTGRAY)

    screen.blit(space_ship, (x,y))
    
    x = (x + dx) % WIDTH
    y = (y + dy) % HEIGHT
        
    pygame.display.update()
    clock.tick(FPS)


