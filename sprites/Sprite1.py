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
space_ship = SpaceShip(space_ship_img, (200,599)) 
space_ship_Group = pygame.sprite.GroupSingle(space_ship)


run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(LIGHTGRAY)
    
    space_ship_Group.update(1,0)
    space_ship_Group.draw(screen)    
    pygame.display.update()
    clock.tick(FPS)

