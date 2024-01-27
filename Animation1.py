# Animation

import pygame
from Graphics import *
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()


spaceShip = pygame.image.load("img/space_ship.png")
spaceShip = pygame.transform.scale(spaceShip, (50,50))
x, y = 200,300
dx, dy = 4,-2

run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill(LIGHTGRAY)
    screen.blit(spaceShip,(x,y))
    x = x + dx
    y = y + dy
    
    if x > 800:
        x = 0

    pygame.display.update()
    clock.tick(FPS)


