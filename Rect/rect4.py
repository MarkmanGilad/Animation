
# In Pygame, the `Rect` object is a fundamental tool for handling rectangular areas, crucial for collision detection, drawing, and positioning elements in a game window. Here's a list of common methods associated with the `Rect` object in Pygame:
# 1. **init**: Initializes a new rectangle. It can be called with the rectangle's top-left corner coordinates and its width and height `(left, top, width, height)` or with two points `(top-left and bottom-right)`.
# 2. **copy**: Returns a new copy of the rectangle.
# 3. **move**: Moves the rectangle by a given offset.
# 4. **move_ip**: Moves the rectangle in place by a given offset.
# 5. **inflate**: Returns a new rectangle that is larger or smaller than the original, centered around the original rectangle.
# 6. **inflate_ip**: Inflates the rectangle in place, making it larger or smaller while keeping it centered.
# 7. **clamp**: Returns a new rectangle that is moved to be completely inside another rectangle.
# 8. **clamp_ip**: Moves the rectangle to be completely inside another rectangle, in place.
# 9. **clip**: Returns a new rectangle that is cropped to be completely inside another rectangle.
# 10. **union**: Returns the smallest rectangle that contains both the original rectangle and another one.
# 11. **union_ip**: Updates the rectangle to be the smallest rectangle that can contain both itself and another rectangle.
# 12. **unionall**: Returns the smallest rectangle that can contain the original rectangle and a sequence of other rectangles.
# 13. **fit**: Returns a new rectangle that is moved and resized to fit another rectangle.
# 14. **contains**: Tests if the rectangle completely contains another rectangle.
# 15. **collidepoint**: Tests if a point is inside the rectangle.
# 16. **colliderect**: Tests if two rectangles overlap.
# 17. **collidelist**: Tests if the rectangle collides with any in a sequence of rectangles.
# 18. **collidelistall**: Returns a list of all the rectangles in a sequence that collide with it.
# 19. **collidedict**: Tests if the rectangle collides with any in a dictionary of rectangles.
# 20. **collidedictall**: Returns a list of all the pairs from a dictionary of rectangles that collide with the rectangle.
# 21. **normalize**: Corrects negative dimensions of the rectangle.


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
sun1 = pygame.image.load("img/sun.png")
sun1 = pygame.transform.scale(sun1, (100, 100))
sun2 = pygame.image.load("img/sun_1.png")
sun2 = pygame.transform.scale(sun2, (100, 100))

sun = sun1
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
        sun = sun2
    else:
        sun = sun1
        

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
