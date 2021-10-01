from math import pi
from math import sin

import pygame

pygame.init()
FPS = 30
screen = pygame.display.set_mode((500, 650), pygame.SRCALPHA)


def draw_landscape():
    sun = pygame.Surface((600, 350))  # поверхность солнца
    sun.set_alpha(150)
    sun.set_colorkey('BLACK')

    pygame.draw.rect(screen, (155, 252, 248), (0, 0, 650, 500), 0)  # небо
    pygame.draw.rect(screen, (255, 255, 255), (0, 390, 650, 500), 0)  # лед

    pygame.draw.ellipse(sun, (253, 255, 219), (0 + 140, 0, 360, 330), 30)  # отрисовка круга солнца
    pygame.draw.line(sun, (253, 255, 219), (140, 165), (360 + 140, 165), 25)  # отрисовка креста солнца
    pygame.draw.line(sun, (253, 255, 219), (180 + 140, 0), (180 + 140, 330), 25)  # отрисовка креста солнца
    # отрисовка кружков в центре и пересечениях креста с кругом
    pygame.draw.circle(sun, (255, 255, 100), (180 + 140, 10), 15)
    pygame.draw.circle(sun, (255, 255, 100), (180 + 140, 310), 15)
    pygame.draw.circle(sun, (255, 255, 100), (20 + 140, 160), 15)
    pygame.draw.circle(sun, (255, 255, 100), (350 + 140, 160), 15)
    pygame.draw.circle(sun, (255, 255, 100), (180 + 140, 170), 25, 0)
    screen.blit(sun, (0, 0))


def draw_bear(size, x, y):
    # body
    pygame.draw.ellipse(screen, (255, 255, 255), (x, y + size / 8, size * 3 / 8, size * 0.75), 0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x, y + size / 8, size * 3 / 8, size * 0.75), 1)
    # head
    pygame.draw.ellipse(screen, (255, 255, 255), (x + size / 8, y, size * 3 / 8, 3 * size / 16), 0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x + size / 8, y, size * 3 / 8, 3 * size / 16), 1)
    # leg
    pygame.draw.ellipse(screen, (255, 255, 255), (x + size / 8, y + size * (1 - 5 / 16), 5 * size / 16, 5 * size / 16),
                        0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x + size / 8, y + size * (1 - 5 / 16), 5 * size / 16, 5 * size / 16), 1)
    # feet
    pygame.draw.ellipse(screen, (255, 255, 255),
                        (x + size * (1 / 4 + 1 / 16), y + size * (1 - 3 / 32), 7 * size / 32, 3 * size / 32), 0)
    pygame.draw.ellipse(screen, (0, 0, 0),
                        (x + size * (1 / 4 + 1 / 16), y + size * (1 - 3 / 32), 7 * size / 32, 3 * size / 32), 1)
    # fishing rod
    pygame.draw.line(screen, (0, 0, 0), (x + size * 3 / 8, y + 9 * size / 20), (x + size * 3 / 4, y), 5 * size // 500)
    pygame.draw.line(screen, (0, 0, 0), (x + size * 7 / 20, y + 11 * size / 20), (x + size * 3 / 8, y + 9 * size / 20), 5 * size // 500)
    # arm
    pygame.draw.ellipse(screen, (255, 255, 255),
                        (x + size * (1 / 4 + 1 / 16), y + size * 0.4, 7 * size / 32, 3 * size / 32), 0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x + size * (1 / 4 + 1 / 16), y + size * 0.4, 7 * size / 32, 3 * size / 32),
                        1)
    # hole
    pygame.draw.ellipse(screen, (169, 169, 169), (x + size / 2, y + size * (1 - 4 / 16), size / 2, 4 * size / 16), 0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x + size / 2, y + size * (1 - 4 / 16), size / 2, 4 * size / 16), 1)
    # water in the hole
    pygame.draw.ellipse(screen, (0, 100, 102),
                        (x + size * (17 / 32), y + size * (13 / 16), 7 * size / 16, 3 * size / 16), 0)
    pygame.draw.ellipse(screen, (0, 0, 0), (x + size * (17 / 32), y + size * (13 / 16), 7 * size / 16, 3 * size / 16),
                        1)
    # spinning
    pygame.draw.aaline(screen, (0, 0, 0), (x + size * 3 / 4, y), (x + size * 3 / 4, y + size * (1 - 1 / 8)), 1)
    # mouth
    pygame.draw.line(screen, (0, 0, 0), (x + size * 5 / 16, y + 9 / 64 * size),
                       (x + size * 15 / 32, y + 9 / 64 * size), 2)
    # nose
    pygame.draw.circle(screen, (0, 0, 0), (x + size * 16 / 32, y + 5 / 64 * size), 7 * size / 600, 0)
    # eye
    pygame.draw.circle(screen, (0, 0, 0), (x + size * 10 / 32, y + 4 / 64 * size), 9 * size / 600, 0)
    # ear
    pygame.draw.circle(screen, (255, 255, 255), (x + size * 5 / 32, y + 2 / 64 * size), 18 * size / 600, 0)
    pygame.draw.circle(screen, (0, 0, 0), (x + size * 5 / 32, y + 2 / 64 * size), 18 * size / 600, 1)
    # fish
    draw_fish(x + 250, y + size, size / 3)


def draw_fish(x, y, size):
    # тело рыбы
    cords = [(x + 41 / 166 * size, y + 68 / 166 * size), (x + 76 / 166 * size, y + 41 / 166 * size),
             (x + 110 / 166 * size, y + 23 / 166 * size), (x + 149 / 166 * size, y + 18 / 166 * size),
             (x + 189 / 166 * size, y + 30 / 166 * size), (x + 164 / 166 * size, y + 54 / 166 * size),
             (x + 136 / 166 * size, y + 67 / 166 * size), (x + 81 / 166 * size, y + 72 / 166 * size)]
    pygame.draw.polygon(screen, 'GREY', cords)
    pygame.draw.aalines(screen, 'BLACK', True, cords, 1)
    # хвост рыбы
    cords = [(x + 42 / 166 * size, y + 67 / 166 * size), (x, y + 116 / 166 * size),
             (x + 1 / 166 * size, y + 75 / 166 * size)]
    pygame.draw.polygon(screen, 'GRAY', cords)
    pygame.draw.aalines(screen, 'BLACK', True, cords, 1)
    # верхний плавник
    cords = [(x + 141 / 166 * size, y + 19 / 166 * size), (x + 130 / 166 * size, y),
             (x + 59 / 166 * size, y + 13 / 166 * size), (x + 104 / 166 * size, y + 26 / 166 * size)]
    pygame.draw.polygon(screen, 'RED', cords)
    pygame.draw.aalines(screen, 'BLACK', False, cords, 1)
    # нижние плавники
    cords = [(x + 141 / 166 * size, y + 65 / 166 * size), (x + 157 / 166 * size, y + 93 / 166 * size),
             (x + 179 / 166 * size, y + 65 / 166 * size), (x + 147 / 166 * size, y + 61 / 166 * size)]
    pygame.draw.polygon(screen, 'RED', cords)
    pygame.draw.aalines(screen, 'BLACK', False, cords, 1)
    cords = [(x + 77 / 166 * size, y + 73 / 166 * size), (x + 69 / 166 * size, y + 95 / 166 * size),
             (x + 101 / 166 * size, y + 91 / 166 * size), (x + 94 / 166 * size, y + 71 / 166 * size)]
    pygame.draw.polygon(screen, 'RED', cords)
    pygame.draw.aalines(screen, 'BLACK', False, cords, 1)

    pygame.draw.circle(screen, 'BLUE', (x + 150 / 166 * size, y + 35 / 166 * size), 10 / 166 * size)
    pygame.draw.circle(screen, 'BLACK', (x + 145 / 166 * size, y + 35 / 166 * size), 5 / 166 * size)
    pygame.draw.circle(screen, 'WHITE', (x + 145 / 166 * size, y + 38 / 166 * size), 1 / 166 * size)


pygame.display.update()
clock = pygame.time.Clock()
clock.tick(FPS)
finished = False

while not finished:
    clock.tick(FPS)
    draw_landscape()

    draw_bear(280, 50, 280)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
            pygame.quit()
    pygame.display.update()

pygame.quit()