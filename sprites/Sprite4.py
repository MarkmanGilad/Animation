import pygame
from Graphics import *
from SpaceShip import SpaceShip
from Sun import Sun

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
screen.fill(LIGHTGRAY)

speed_x, speed_y = 0, 0

space_ship_img = pygame.image.load("img/spacecraft.png")
space_ship_img = pygame.transform.scale(space_ship_img, (60, 60))
space_ship_Group = pygame.sprite.Group()

sun = Sun()
sun_Group = pygame.sprite.GroupSingle(sun)

for i in range(5):
    for j in range(3):
        space_ship = SpaceShip(space_ship_img, (100*i,599-j*80)) 
        space_ship_Group.add(space_ship)


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

    screen.fill(LIGHTGRAY)
    sun_Group.update()
    sun_Group.draw(screen)
    
    space_ship_Group.update(speed_x,speed_y)
    space_ship_Group.draw(screen)
    pygame.sprite.groupcollide(sun_Group, space_ship_Group, False, True)
    pygame.display.update()
    clock.tick(FPS)

