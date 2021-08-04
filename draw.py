import pygame

pygame.init()

SIZE = [600, 400]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Заголовок окна')
pygame.display.set_icon(pygame.image.load('icon.png.png'))

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.draw.rect(screen, RED, (10 ,10, 50, 100), 2) # прямоугольник
pygame.draw.line(screen, GREEN, (200, 20), (250, 80), 6)
pygame.draw.circle(screen, WHITE, (300, 250), 40)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    clock.tick(FPS)
