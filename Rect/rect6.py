
import pygame
from Graphics import *
import math
import random

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
space = pygame.image.load("img/space.jpg")
screen.blit(space, (0,0))

x, y = 200, 200
speed, angle = 0, 0

space_ship = pygame.image.load("img/spacecraft.png")
space_ship = pygame.transform.scale(space_ship, (60, 60))
space_ship = pygame.transform.rotate(space_ship, -90)
space_ship_rect = space_ship.get_rect()

enemy = pygame.image.load("Img\starwars_PNG19.png")
enemy = pygame.transform.scale(enemy, (100, 100))
enemy_rect = enemy.get_rect()
enemy_speed = 3
enemy_speed_x, enemy_speed_y = enemy_speed , enemy_speed
enemy_x, enemy_y = 300, 300

font = pygame.font.Font(None, 36)
text = font.render('Collide', True, (255, 255, 255))

run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                angle = angle - 10
            if event.key == pygame.K_LEFT:
                angle = angle + 10
            if event.key == pygame.K_UP:
                speed += 1
            if event.key == pygame.K_DOWN:
                speed -= 1 
            if event.key == pygame.K_SPACE:
                speed = 0 
                

    screen.blit(space, (0,0))
    
    ######## space ship move ###########

    x += (math.cos(math.radians(angle)) * speed)
    x = x % WIDTH
    y -= (math.sin(math.radians(angle)) * speed)
    y = y % HEIGHT

    space_ship_rotated = pygame.transform.rotate(space_ship, angle=angle)
    space_ship_rect = space_ship.get_rect()
    space_ship_rect.center = x, y
    screen.blit(space_ship_rotated, space_ship_rect)    
    
    ######## enemy move ###########
    rnd_x = random.random()
    rnd_y = random.random()
    if rnd_x < 0.01:
        enemy_speed_x = -enemy_speed_x
    if rnd_y < 0.01:
        enemy_speed_y = -enemy_speed_y
        
    enemy_x += enemy_speed_x
    enemy_y += enemy_speed_y
    enemy_rect.center = (enemy_x,enemy_y)

    if enemy_rect.right >= WIDTH:
        enemy_speed_x = -enemy_speed
    elif enemy_rect.left <= 0:
        enemy_speed_x = enemy_speed
    if enemy_rect.bottom >= HEIGHT:
        enemy_speed_y = -enemy_speed
    elif enemy_rect.top <= 0:
        enemy_speed_y = enemy_speed


    screen.blit(enemy, enemy_rect)


    ######## collide ###########

    if space_ship_rect.colliderect(enemy_rect):
        screen.blit(text, (100, 100))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


