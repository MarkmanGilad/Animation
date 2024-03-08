# Animation

import pygame
from Graphics import *
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
screen.fill(LIGHTGRAY)

for row in range(3):
    for col in range(4):
       pygame.draw.circle(screen, RED, center=(col*50, row* 100), radius=20) 
    
run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
    pygame.display.update()
    clock.tick(FPS)


