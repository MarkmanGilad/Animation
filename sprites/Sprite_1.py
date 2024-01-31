import pygame
from Graphics import *
from SpaceShip import SpaceShip

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
screen.fill(LIGHTGRAY)

space_ship_img = pygame.image.load("img/spacecraft.png")
space_ship_img = pygame.transform.scale(space_ship_img, (60, 60))
space_ship = SpaceShip(space_ship_img) 
space_ship.rect.midbottom = (400,599)

run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(LIGHTGRAY)
    
    space_ship.move(-2, -3)
    space_ship.draw(screen)    
    
    pygame.display.flip()
    clock.tick(FPS)

