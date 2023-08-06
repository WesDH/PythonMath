import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
white = pygame.Color(255, 255, 255)


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.polygon(screen, white, ((10, 10), (10, 400), (195, 195)))
    pygame.display.update()

