import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

'''
    Draws a white star as a rectangle on the screen
    :arg x (int): location of the x coordinate to draw
    :arg y (int):  location of the  coordinate to draw
    :arg size (int): size of the the star
'''
def draw_star(x: int, y: int, size: int) -> None:
    white = pygame.Color(255, 255, 255)
    pygame.draw.rect(screen, white, (x, y, size, size))


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # rear and tail
    draw_star(int(screen_width*.1), int(screen_height*.6), 15)
    draw_star(int(screen_width * .35), int(screen_height * .65), 18)
    draw_star(int(screen_width * .42), int(screen_height * .4), 10)

    # front and front leg
    draw_star(int(screen_width * .7), int(screen_height * .37), 10)
    draw_star(int(screen_width * .65), int(screen_height * .52), 30)
    draw_star(int(screen_width * .73), int(screen_height * .65), 7)
    draw_star(int(screen_width * .73), int(screen_height * .8), 16)

    # hea)
    draw_star(int(screen_width * .85), int(screen_height * .25), 10)
    draw_star(int(screen_width * .92), int(screen_height * .3), 10)

    pygame.display.update()
