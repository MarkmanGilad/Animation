# Animation

import pygame
from Graphics import *
pygame.init()
import math


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
screen.fill(LIGHTGRAY)

space_ship = pygame.image.load("img/spacecraft.png")
space_ship = pygame.transform.scale(space_ship, (60, 60))
space_ship = pygame.transform.rotate(space_ship,-90)

x, y = 400, 300
v, angle = 0, 0

run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                angle = angle - 5
            if event.key == pygame.K_LEFT:
                angle = angle + 5
            if event.key == pygame.K_UP:
                v += 1
            if event.key == pygame.K_DOWN:
                v -= 1
    dx = v * math.cos(math.pi*angle/180)
    dy = v * math.sin(math.pi*angle/180) 
    x = (x + dx) % WIDTH
    y = (y - dy) % HEIGHT
    rotated_spaceship = pygame.transform.rotate(space_ship,angle)

    screen.fill(LIGHTGRAY)
    screen.blit(rotated_spaceship, (x,y))

    pygame.display.update()
    clock.tick(FPS)


