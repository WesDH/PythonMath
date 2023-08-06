import pygame
from pygame.locals import * # mouse button support

pygame.init()
sw = 1000
sh = 800
sc = pygame.display.set_mode((sw, sh))

white = pygame.Color(255, 255, 255)
first_point = True

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        elif e.type == MOUSEBUTTONDOWN:
            if first_point:
                point1 = pygame.mouse.get_pos()
                print(type(point1))
                first_point = False
            else:
                point2 = pygame.mouse.get_pos()
                pygame.draw.line(sc, white, point1, point2, 1)
                first_point = True
        pygame.display.update()


