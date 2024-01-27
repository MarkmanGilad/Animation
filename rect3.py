import pygame
from Graphics import *
import math

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
screen.fill(LIGHTGRAY)

x, y = 200, 200
speed, angle = 0, 0

space_ship = pygame.image.load("img/spacecraft.png")
space_ship = pygame.transform.scale(space_ship, (50, 50))
space_ship = pygame.transform.rotate(space_ship, -90)
space_ship_rect = space_ship.get_rect()
sun = pygame.image.load("img/sun.png")
sun = pygame.transform.scale(sun, (100, 100))
sun_rect = sun.get_rect(center=(700,100))

    
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
                speed += 1
            if event.key == pygame.K_DOWN:
                speed -= 1 
            if event.key == pygame.K_SPACE:
                speed = 0 
                

    screen.fill(LIGHTGRAY)
    screen.blit(sun, sun_rect)

    x += (math.cos(angle/360 * 2 * math.pi) * speed)
    x = x % WIDTH
    y -= (math.sin(math.radians(angle)) * speed)
    y = y % HEIGHT

    space_ship_rotated = pygame.transform.rotate(space_ship, angle=angle)
    space_ship_rect = space_ship.get_rect()
    space_ship_rect.center = x, y
    screen.blit(space_ship_rotated, space_ship_rect)    
    
    if space_ship_rect.colliderect(sun_rect):
        screen.fill('red')

    pygame.display.update()
    clock.tick(FPS)

