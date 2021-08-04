import pygame
pygame.init()

print(pygame.font.get_fonts())
f_sys = pygame.font.SysFont('arial', 12)

SIZE = [600, 400]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Шрифты')
pygame.display.set_icon(pygame.image.load('icon.png.png'))

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (128, 0, 0)
YELLOW = (218, 165, 32)

f = pygame.font.SysFont('arial', 120)
sc_text = f.render('Hello, World',  RED, YELLOW)
pos = sc_text.get_rect(center = (300, 200))

screen.fill(WHITE)
screen.blit(sc_text, pos)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    clock.tick(FPS)
