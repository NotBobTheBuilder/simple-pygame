import sys
import math
import pygame
from pygame.locals import FULLSCREEN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE


def main():
    screen      = pygame.display.set_mode((1024, 768), FULLSCREEN)
    image       = pygame.image.load('wow.png')
    clock       = pygame.time.Clock()

    black       = (0,0,0)
    play_game   = True
    x_position  = 50
    y_position  = 50

    while play_game:
        clock.tick(60)
        screen.fill(black)

        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_ESCAPE]:
            play_game = False
        if key_pressed[K_RIGHT]:
            x_position += 5
        
        screen.blit(image, (x_position, y_position))
        pygame.display.flip()
        pygame.event.pump()

    pygame.quit()

main()
