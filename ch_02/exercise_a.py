# Exercise A: Draw the range of colors that mix the green and blue channels
# with no red.
import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for y in range(800):
        for x in range(1000):
            screen.set_at((x, y),
                          pygame.Color(
                              0,
                              int(x / screen_width * 255),
                              int(y / screen_height * 255)
                          ))

    pygame.display.update()
