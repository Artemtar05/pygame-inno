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
speed = 5

flag = True
fl_left = fl_right = fl_up = fl_down = False
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                fl_right = True
            elif event.key == pygame.K_a:
                fl_left = True
            elif event.key == pygame.K_w:
                fl_up = True
            elif event.key == pygame.K_s:
                fl_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                fl_right = fl_left = False
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                fl_up = fl_down = False

    if fl_left:
        x -= speed
    elif fl_right:
        x += speed
    elif fl_up:
        y -= speed
    elif fl_down:
        y += speed
    pygame.draw.rect(screen, YELLOW, (x, y, 10, 20))
    pygame.display.update()
    clock.tick(FPS)
