from random import randint, choice

import pygame

from Constants import *


class Target:
    def __init__(self, screen, color):
        """
        Конструктор класса Target. Задает параметры по умолчанию для движущейся мишени в виде шарика.
        :param screen: поверхность для рисования pygame
        :param color: цвет мишени
        """
        self.live = 1
        self.screen = screen
        self.points = 0
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.vx = randint(-15, 15)
        self.vy = randint(-15, 15)
        self.r = randint(2, 50)
        self.color = color
        self.type = choice(GAME_TARGETS)

    def setting(self):
        """
        Функция обновления параметров мишени
        """
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.vx = randint(-15, 15)
        self.vy = randint(-15, 15)
        self.r = randint(2, 50)
        self.type = choice(GAME_TARGETS)

    def is_draw(self, is_live):
        """
        Функция-отрисовщик мишеней
        :param is_live: флажок жизни мишени
        :return: булово значение: полчилось нарисовать мишень или нет
        """
        if is_live:
            if self.type == "TARGET":
                if self.x + self.r >= 800:
                    self.x = 800 - self.r
                    self.vx = -self.vx
                if self.x - self.r <= 0:
                    self.x = self.r
                    self.vx = -self.vx
                if self.y - self.r <= 0:
                    self.y = self.r
                    self.vy = -self.vy
                if self.y + self.r >= 600 - 50:
                    self.y = 600 - 50 - self.r
                    self.vy = -self.vy

                self.x += int(self.vx)
                self.y -= int(self.vy) - 1

                pygame.draw.circle(
                    self.screen,
                    self.color,
                    (self.x, self.y),
                    self.r
                )

            elif self.type == "SPECIAL_TARGET":
                self.color = choice(GAME_COLORS)
                if self.x + self.r >= 800:
                    self.x = randint(self.r + 50, 800 - self.r - 50)
                    self.vx = -self.vx
                if self.x - self.r <= 0:
                    self.x = randint(self.r + 50, 800 - self.r - 50)
                    self.vx = -self.vx
                if self.y - self.r <= 0:
                    self.y = randint(self.r + 50, 600 - self.r - 50)
                    self.vy = -self.vy
                if self.y + self.r >= 600 - 50:
                    self.y = randint(self.r + 50, 600 - self.r - 50)
                    self.vy = -self.vy

                self.x += int(self.vx)
                self.y -= int(self.vy) - 1

                if self.r <= 3:
                    self.vx = self.vy = 0

                pygame.draw.circle(
                    self.screen,
                    self.color,
                    (self.x, self.y),
                    self.r
                )
            return True
        else:
            return False
