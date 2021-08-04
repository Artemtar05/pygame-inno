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

hero = pygame.Surface((40, 50))
hero.fill(YELLOW)
rect = hero.get_rect()
print(rect.center)
screen.fill(WHITE)
screen.blit(hero, (300, 200))
pygame.display.update()

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(FPS)
