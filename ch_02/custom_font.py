import pygame

pygame.init()
screen_width = 800
screen_height = 200
screen = pygame.display.set_mode((screen_width,
                                  screen_height))
done = False
white = pygame.Color(255, 255, 255)
pygame.font.init()
#font = pygame.font.SysFont('Comic Sans MS', 120, False, True)
font = pygame.font.Font('fonts/Request Coffee.ttf', 80)

text = font.render('Wesley Dean', True, white)
text2 = font.render('Havens', True, white)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        screen.blit(text, (10, 10))
        screen.blit(text2, (150, 110))
        pygame.display.update()
pygame.quit()
