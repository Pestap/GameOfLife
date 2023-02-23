import sys
import pygame
import time
import pygame.locals
from CellWorld import CellWorld

pygame.init()

x_size = 120
y_size = 60

DISPLAY = pygame.display.set_mode((x_size*10,y_size*10))
shift_x = 5
shift_y = 5
WORLD = CellWorld((x_size, y_size), 'pentadecathlon', (shift_x, shift_y))

FPS = pygame.time.Clock()
FPS.tick(1)
quit = False
is_running = True

# Game loop
while not quit:
    DISPLAY.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
            quit = True

    #draw game
    for row in WORLD.world:
        for cell in row:
            if not cell.is_dead:
                pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(10*cell.position[0], 10*cell.position[1], 10,10))

    if is_running:
        WORLD.advance()
    time.sleep(0.1)
    pygame.display.flip()

