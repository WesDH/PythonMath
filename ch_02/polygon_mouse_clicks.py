import pygame
from pygame.locals import * # mouse button support
import random

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
white = pygame.Color(255, 255, 255)
click_counter = 0
click_coords = []

def get_random_col() -> pygame.Color:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return pygame.Color(r, g, b)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == MOUSEBUTTONDOWN:
            click_coords.append(pygame.mouse.get_pos())
            if len(click_coords) == 3:
                color = get_random_col()
                pygame.draw.polygon(screen, color,
                                    ((click_coords[0]),
                                     (click_coords[1]),
                                     (click_coords[2])))
                click_coords = []
                break

    pygame.display.update()

