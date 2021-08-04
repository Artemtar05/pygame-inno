import pygame

pygame.init()

SIZE = [600, 400]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Заголовок окна')
pygame.display.set_icon(pygame.image.load('icon.png.png'))

clock = pygame.time.Clock()
FPS = 60

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(FPS)
