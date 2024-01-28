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

x, y = 250, 350
speed_x, speed_y = 1, 1

rectangle = pygame.Surface((100,80))
rectangle.fill('red')
rect = rectangle.get_rect(center = (x,y))

    
run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(LIGHTGRAY)
    
    if rect.bottom >= HEIGHT:
        speed_y = -2
    elif rect.top <= 0:
        speed_y = 2
    if rect.right >= WIDTH:
        speed_x = -2
    elif rect.left <= 0:
        speed_x = 2
    
    # rect.move_ip(speed_x, speed_y) 
    rect = rect.move(speed_x, speed_y) 
    screen.blit(rectangle, rect)    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()