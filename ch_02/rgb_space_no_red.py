# Exercise A: Draw the range of colors that mix the green and blue channels
# with no red.
import pygame

pygame.init()
sw = 1000
sh = 800

screen = pygame.display.set_mode((sw, sh))

if __name__ == "__main__":
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
        for x in range(sw):
            for y in range(sh):
                screen.set_at((x, y), pygame.Color(
                    0,
                    int(x/sw * 255),
                    int(y/sh * 255)
                ))
                #screen.set_at((x, y), pygame.Color(int(x / screen_width * 255), int(y / screen_height * 255), 255))
        pygame.display.update()
