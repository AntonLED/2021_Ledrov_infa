import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
screen = pygame.display.set_mode((360, 520))
screen.fill((185, 211, 238))
dr.polygon(screen, (96, 123, 139), [(0, 330), (360, 330), (360, 520), (0, 520)])

# ширина и высота в отдельных координатах
width = 360
height = 520
# поверхность для прозрачности
surface = pygame.Surface((width, height), pygame.SRCALPHA)


# функция для фона
def background(x, y, size):
    dr.polygon(screen, (145, 171, 198),
               [(x, y), (x + 360 * size, y), (x + 360 * size, y + 330 * size), (x, y + 330 * size)])
    # дома слева
    dr.polygon(screen, (159, 182, 205),
               [(x + 10 * size, y + 10 * size), (x + 80 * size, y + 10 * size), (x + 80 * size, y + 340 * size),
                (x + 10 * size, y + 340 * size)])
    dr.polygon(screen, (150, 205, 205),
               [(x + 90 * size, y + 30 * size), (x + 170 * size, y + 30 * size), (x + 170 * size, y + 350 * size),
                (x + 90 * size, y + 350 * size)])
    dr.polygon(screen, (198, 226, 255),
               [(x + 60 * size, y + 80 * size), (x + 150 * size, y + 80 * size), (x + 150 * size, y + 390 * size),
                (x + 60 * size, y + 390 * size)])
    # дома справа
    dr.polygon(screen, (202, 225, 255),
               [(x + 270 * size, y + 10 * size), (x + 350 * size, y + 10 * size), (x + 350 * size, y + 340 * size),
                (x + 270 * size, y + 340 * size)])
    dr.polygon(screen, (122, 197, 205),
               [(x + 240 * size, y + 90 * size), (x + 320 * size, y + 90 * size), (x + 320 * size, y + 400 * size),
                (x + 240 * size, y + 400 * size)])


# Функция для домов одного цвета
def sub_background(x, y, size, COLOUR):
    # дома слева
    dr.polygon(surface, COLOUR,
               [(x + 10 * size, y + 10 * size), (x + 80 * size, y + 10 * size), (x + 80 * size, y + 340 * size),
                (x + 10 * size, y + 340 * size)])
    screen.blit(surface, (0, 0))
    dr.polygon(surface, COLOUR,
               [(x + 90 * size, y + 30 * size), (x + 170 * size, y + 30 * size), (x + 170 * size, y + 350 * size),
                (x + 90 * size, y + 350 * size)])
    screen.blit(surface, (0, 0))
    dr.polygon(surface, COLOUR,
               [(x + 60 * size, y + 80 * size), (x + 150 * size, y + 80 * size), (x + 150 * size, y + 390 * size),
                (x + 60 * size, y + 390 * size)])
    screen.blit(surface, (0, 0))
    # дома справа
    dr.polygon(surface, COLOUR,
               [(x + 270 * size, y + 10 * size), (x + 350 * size, y + 10 * size), (x + 350 * size, y + 340 * size),
                (x + 270 * size, y + 340 * size)])
    screen.blit(surface, (0, 0))
    dr.polygon(surface, COLOUR,
               [(x + 240 * size, y + 90 * size), (x + 320 * size, y + 90 * size), (x + 320 * size, y + 400 * size),
                (x + 240 * size, y + 400 * size)])
    screen.blit(surface, (0, 0))

    dr.polygon(surface, COLOUR, [(x, y), (x + 360 * size, y), (x + 360 * size, y + 330 * size), (x, y + 330 * size)])
    screen.blit(surface, (0, 0))

    pygame.draw.ellipse(surface, COLOUR, (x + 80 * size, y + 130 * size, 400 * size, 80 * size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, COLOUR, (x + 40 * size, y + 30 * size, 210 * size, 70 * size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, COLOUR, (x + 200 * size, y - 10 * size, 210 * size, 50 * size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, COLOUR, (x + 20 * size, y + 410 * size, 110 * size, 25 * size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, COLOUR, (x + 25 * size, y + 445 * size, 110 * size, 25 * size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, COLOUR, (x - 60 * size, y + 380 * size, 110 * size, 25 * size))
    screen.blit(surface, (0, 0))


# функция для машины
def car(x, y, size):
    # выхлоп
    pygame.draw.ellipse(screen, (28, 28, 28), (x - 10 * size, y + 10 * size, 20 * size, 7 * size))
    # корпус
    dr.polygon(screen, (10, 150, 250),
               [(x, y), (x + (150 * size), y), (x + (150 * size), y + (30 * size)), (x, y + (30 * size))])
    # крыша
    dr.polygon(screen, (10, 150, 250),
               [(x + (30 * size), y - (25 * size)), (x + (105 * size), y - 25 * size), (x + 105 * size, y),
                (x + 30 * size, y)])
    # окна
    dr.polygon(screen, (248, 248, 255),
               [(x + 35 * size, y - 20 * size), (x + 60 * size, y - 20 * size), (x + 60 * size, y - 5 * size),
                (x + 35 * size, y - 5 * size)])
    dr.polygon(screen, (248, 248, 255),
               [(x + 75 * size, y - 20 * size), (x + 100 * size, y - 20 * size), (x + 100 * size, y - 5 * size),
                (x + 75 * size, y - 5 * size)])
    # колеса
    pygame.draw.ellipse(screen, (28, 28, 28), (x + 10 * size, y + 20 * size, 35 * size, 20 * size))
    pygame.draw.ellipse(screen, (28, 28, 28), (x + 105 * size, y + 20 * size, 35 * size, 20 * size))


# тело кода
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
