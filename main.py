import sys
import pygame
import pygame.locals
pygame.init()


DISPLAY = pygame.display.set_mode((1200,600))

FPS = pygame.time.Clock()
FPS.tick(2)
quit = False

# Game loop
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
            quit = True

    pygame.display.update()

