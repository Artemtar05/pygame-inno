import pygame

pygame.init()

SIZE = [600, 400]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Заголовок окна')
pygame.display.set_icon(pygame.image.load('icon.png.png'))

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (128, 0, 0)
YELLOW = (218, 165, 32)

x = 300
y = 200
speed = 10

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x -= speed
            elif event.key == pygame.K_d:
                x += speed
            elif event.key == pygame.K_w:
                y -= speed
            elif event.key == pygame.K_s:
                y += speed

    pygame.draw.circle(screen, YELLOW, (x, y), 40)
    pygame.display.update()
    clock.tick(FPS)
