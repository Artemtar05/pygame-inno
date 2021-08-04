import pygame
import random

# РАЗМЕР ОКНА
SIZE = [500, 600]
# Кадров в секунду (FPS)
FPS = 30

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LAGUNA = (7, 235, 250)

pygame.init()  # включаем библиотеку
pygame.mixer.init()  # подключаем звук
screen = pygame.display.set_mode(SIZE)  # установили размер в окно Screen
pygame.display.set_caption("Bad Korp")  # дали название окну
clock = pygame.time.Clock()  # подключили FPS


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(LAGUNA)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -8

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


# Класс игрока, наследуется от класса Sprite внутри PyGame
# Создаем в классе игрока : поверхность для изображение (self.image) ,
class Player(pygame.sprite.Sprite):
    # __init__    -> срабатываем при создании класса в коде
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))  # создаем поверхность // аналог метода blit()
        self.image.fill(GREEN)  # заливаем поверхность цветов
        self.rect = self.image.get_rect()  # создаем Rect (предназначен для заливки прямоугольных областей)
        self.rect.centerx = SIZE[
                                0] / 2  # вернет прямоугольник, координата x центра которого будет иметь значение SIZE[0] / 2
        self.rect.bottom = SIZE[1] - 10  # хранит координату от низа нашего rect (прямоугольной области)
        self.speedx = 0  # скорость

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def update(self):  # обновление координаты x в rect
        self.rect.x += self.speedx  # обновление скорости
        self.speedx = 0  # чтоб персонаж останавливался

        key = pygame.key.get_pressed()  # получить нажатую клавишу
        if key[pygame.K_LEFT]:  # стрелка влево
            self.speedx = -5
        if key[pygame.K_RIGHT]:  # стрелка вправо
            self.speedx = 5

        if self.rect.right > SIZE[0]:  # право
            self.rect.right = SIZE[0]
        if self.rect.left < 0:  # лево
            self.rect.left = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))  # создаем поверхность // аналог метода blit()
        self.image.fill(RED)  # заливаем красным цветом
        self.rect = self.image.get_rect()  # создаем Rect из поверхности
        self.rect.x = random.randrange(SIZE[0] - self.rect.width)  # координата центра нашего Rect
        self.rect.y = random.randrange(-80, -40)  # Координата по Y<0 -> за пределами екрана
        self.speedy = random.randrange(1, 8)  # скорость по Y рандомно от 1 до 8
        self.speedx = random.randrange(-2, 3)  # скорость по x

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > SIZE[1] + 10 or self.rect.right < 0 or self.rect.left > SIZE[
            0]:  # если верхняя часть RECT ушла за нижнюю часть окна
            self.rect.x = random.randrange(SIZE[0] - self.rect.width)
            self.rect.y = random.randrange(-80, -40)
            self.speedy = random.randrange(1, 8)


# создаем группу спрайтов
all_sprites = pygame.sprite.Group()
enems = pygame.sprite.Group()
bullets = pygame.sprite.Group()
# создаем екзмепляр класса Player
player = Player()
# добавляем спрайт Player в группу
all_sprites.add(player)
# добавляем спрайты Enemy
for i in range(7):
    m = Enemy()
    all_sprites.add(m)
    enems.add(m)

running = True
while running:
    # Включаем FPS
    clock.tick(FPS)
    # отлавливаем все события
    for event in pygame.event.get():
        # проверка на закрытие окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Обновление
    all_sprites.update()

    screen.fill(BLACK)  # залили поверхность черным
    all_sprites.draw(screen)  # отрисовываем спрайты на екране Screen
    pygame.display.flip()  # аналог display.update()

pygame.quit()
