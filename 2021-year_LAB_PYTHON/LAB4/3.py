import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
screen = pygame.display.set_mode((360, 520))
screen.fill((185, 211, 238))

# Асфальт
dr.polygon(screen, (96, 123, 139), [(0, 330), (360, 330), (360, 520), (0, 520)])

# Ширина и высота в отдельных координатах
width = 360
height = 520
# Поверхность для прозрачности
surface = pygame.Surface((width, height), pygame.SRCALPHA)


# Функция для переднего голубого фона с домами
def background(x, y, size):
    """
    Рисует передний голубой фон с домами

    :param x: левый верхний угол фона
    :param y: левый верхний угол фона
    :param size: размер фона равен 360size x 330size; домов 70size x 330size, 80size x 320size, 90size x 310 size,
               80size x 310size

    """
    # Фон
    dr.polygon(screen, (145, 171, 198),
               [(x, y), (x + 360 * size, y), (x + 360 * size, y + 330 * size), (x, y + 330 * size)])
    # Дома слева
    dr.polygon(screen, (159, 182, 205),
               [(x + 10 * size, y + 10 * size), (x + 80 * size, y + 10 * size), (x + 80 * size, y + 340 * size),
                (x + 10 * size, y + 340 * size)])
    dr.polygon(screen, (150, 205, 205),
               [(x + 90 * size, y + 30 * size), (x + 170 * size, y + 30 * size), (x + 170 * size, y + 350 * size),
                (x + 90 * size, y + 350 * size)])
    dr.polygon(screen, (198, 226, 255),
               [(x + 60 * size, y + 80 * size), (x + 150 * size, y + 80 * size), (x + 150 * size, y + 390 * size),
                (x + 60 * size, y + 390 * size)])
    # Дома справа
    dr.polygon(screen, (202, 225, 255),
               [(x + 270 * size, y + 10 * size), (x + 350 * size, y + 10 * size), (x + 350 * size, y + 340 * size),
                (x + 270 * size, y + 340 * size)])
    dr.polygon(screen, (122, 197, 205),
               [(x + 240 * size, y + 90 * size), (x + 320 * size, y + 90 * size), (x + 320 * size, y + 400 * size),
                (x + 240 * size, y + 400 * size)])


# Функция для заднего черного фона с домами
def sub_background(x, y, size, colour):
    """
    Рисует черный фон с домами

    :param x: левый верхний угол фона
    :param y: левый верхний угол фона
    :param size: размер фона 360size x 330size, домов
    :param colour: цвет
    """
    # Дома слева
    dr.polygon(surface, colour,
               [(x + 10 * size, y + 10 * size), (x + 80 * size, y + 10 * size), (x + 80 * size, y + 340 * size),
                (x + 10 * size, y + 340 * size)])
    screen.blit(surface, (0, 0))
    dr.polygon(surface, colour,
               [(x + 90 * size, y + 30 * size), (x + 170 * size, y + 30 * size), (x + 170 * size, y + 350 * size),
                (x + 90 * size, y + 350 * size)])
    screen.blit(surface, (0, 0))
    dr.polygon(surface, colour,
               [(x + 60 * size, y + 80 * size), (x + 150 * size, y + 80 * size), (x + 150 * size, y + 390 * size),
                (x + 60 * size, y + 390 * size)])
    screen.blit(surface, (0, 0))
    # Дома справа
    dr.polygon(surface, colour,
               [(x + 270 * size, y + 10 * size), (x + 350 * size, y + 10 * size), (x + 350 * size, y + 340 * size),
                (x + 270 * size, y + 340 * size)])
    screen.blit(surface, (0, 0))
    dr.polygon(surface, colour,
               [(x + 240 * size, y + 90 * size), (x + 320 * size, y + 90 * size), (x + 320 * size, y + 400 * size),
                (x + 240 * size, y + 400 * size)])
    screen.blit(surface, (0, 0))
    # Фон
    dr.polygon(surface, colour, [(x, y), (x + 360 * size, y), (x + 360 * size, y + 330 * size), (x, y + 330 * size)])
    screen.blit(surface, (0, 0))

    pygame.draw.ellipse(surface, colour, (x + 80 * size, y + 130 * size, 400 * size, 80 * size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, colour, (x + 40 * size, y + 30 * size, 210 * size, 70 * size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, colour, (x + 200 * size, y - 10 * size, 210 * size, 50 * size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, colour, (x + 20 * size, y + 410 * size, 110 * size, 25 * size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, colour, (x + 25 * size, y + 445 * size, 110 * size, 25 * size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, colour, (x - 60 * size, y + 380 * size, 110 * size, 25 * size))
    screen.blit(surface, (0, 0))


# Функция для машины
def car(x, y, size):
    """
    Рисует машину

    :param x: левый верхний угол корпуса
    :param y: левый верхний угол корпуса
    :param size: линейные размеры машины (длина корпуса 150size)
    """
    # Выхлоп
    pygame.draw.ellipse(screen, (28, 28, 28), (x - 10 * size, y + 10 * size, 20 * size, 7 * size))
    # Корпус
    dr.polygon(screen, (10, 150, 250),
               [(x, y), (x + (150 * size), y), (x + (150 * size), y + (30 * size)), (x, y + (30 * size))])
    # Крыша
    dr.polygon(screen, (10, 150, 250),
               [(x + (30 * size), y - (25 * size)), (x + (105 * size), y - 25 * size), (x + 105 * size, y),
                (x + 30 * size, y)])
    # Окна
    dr.polygon(screen, (248, 248, 255),
               [(x + 35 * size, y - 20 * size), (x + 60 * size, y - 20 * size), (x + 60 * size, y - 5 * size),
                (x + 35 * size, y - 5 * size)])
    dr.polygon(screen, (248, 248, 255),
               [(x + 75 * size, y - 20 * size), (x + 100 * size, y - 20 * size), (x + 100 * size, y - 5 * size),
                (x + 75 * size, y - 5 * size)])
    # Колеса
    pygame.draw.ellipse(screen, (28, 28, 28), (x + 10 * size, y + 20 * size, 35 * size, 20 * size))
    pygame.draw.ellipse(screen, (28, 28, 28), (x + 105 * size, y + 20 * size, 35 * size, 20 * size))


# Тело кода
sub_background(-10, 0, 0.75, (0, 0, 0, 20))
sub_background(120, 0, 0.75, (0, 0, 0, 20))
background(120, 100, 0.7)
background(-50, 110, 0.7)
car(10, 400, 0.4)
car(20, 450, 0.5)
car(100, 380, 0.35)
car(250, 390, 0.5)
car(180, 450, 0.75)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
