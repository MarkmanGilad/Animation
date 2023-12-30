# Animation

import pygame
from Graphics import *
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
screen.fill(LIGHTGRAY)

space_ship = pygame.image.load("img/spacecraft.png")
space_ship = pygame.transform.scale(space_ship, (60, 60))

x, y = WIDTH//2, HEIGHT//2
dx, dy = 0, 0
angle = 0

run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = dx + 2
            if event.key == pygame.K_LEFT:
                dx = dx - 2
            if event.key == pygame.K_UP:
                dy = dy - 2
            if event.key == pygame.K_DOWN:
                dy = dy + 2
            if event.key == pygame.K_1:
                angle += 45
            if event.key == pygame.K_2:
                angle -= 45

    screen.fill(LIGHTGRAY)
    rotated_spaceship = pygame.transform.rotate(space_ship,angle)
    screen.blit(rotated_spaceship, (x,y))
    
    x = (x + dx) % WIDTH
    y = (y + dy) % HEIGHT


    pygame.display.update()
    clock.tick(FPS)


