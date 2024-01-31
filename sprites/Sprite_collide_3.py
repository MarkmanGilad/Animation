import pygame
from Graphics import *
from SpaceShip import SpaceShip
from Sun import Sun

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
screen.fill(LIGHTGRAY)

space_ship_img = pygame.image.load("img/spacecraft.png")
space_ship_img = pygame.transform.scale(space_ship_img, (60, 60))
space_ship = SpaceShip(space_ship_img) 
space_ship.rect.midbottom = (200,599)

sun_img = pygame.image.load("img/sun.png")
sun = Sun(sun_img)

speed_x, speed_y = 0, 0
color = LIGHTGRAY

run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x += -1
            if event.key == pygame.K_RIGHT:
                speed_x += 1
            if event.key == pygame.K_UP:
                speed_y += -1
            if event.key == pygame.K_DOWN:
                speed_y += 1
            if event.key == pygame.K_SPACE:
                speed_x, speed_y = 0, 0

    screen.fill(color)
    
    space_ship.move(speed_x,speed_y)
    space_ship.draw(screen)  

    sun.move()
    sun.draw(screen)  

    if pygame.sprite.collide_mask(space_ship, sun):
        color = pygame.Color('LightBlue')
    else:
        color = LIGHTGRAY

    pygame.display.update()
    clock.tick(FPS)

