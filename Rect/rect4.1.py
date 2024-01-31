
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


space_ship_rect = space_ship_rect.move(x,y)

space_ship_rect.move_ip(x,y)