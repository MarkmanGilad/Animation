############# Rect #####################
# x,y
# top, left, bottom, right
# topleft, bottomleft, topright, bottomright
# midtop, midleft, midbottom, midright
# center, centerx, centery
# size, width, height
# w,h


import pygame
from Graphics import *
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
screen.fill(LIGHTGRAY)

x, y = 50, 50
dx, dy = 1, -2

space_ship = pygame.image.load("img/spacecraft.png")
space_ship = pygame.transform.scale(space_ship, (40, 50))
space_ship_rect = space_ship.get_rect()
    
run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(LIGHTGRAY)
    
    x = (x + dx) % WIDTH
    y = (y + dy) % HEIGHT
    space_ship_rect.center = x, y
    screen.blit(space_ship, space_ship_rect)    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()