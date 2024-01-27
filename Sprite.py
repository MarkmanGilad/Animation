import pygame
from Graphics import *
from SpaceShip import SpaceShip


pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
screen.fill(LIGHTGRAY)


space_ship = SpaceShip("img/space_ship.png", (100,100)) 
space_ship_Group = pygame.sprite.GroupSingle(space_ship)


run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(LIGHTGRAY)

    # screen.blit(space_ship, (x,y))
    space_ship_Group.update()
    space_ship_Group.draw(screen)    
    pygame.display.update()
    clock.tick(FPS)

