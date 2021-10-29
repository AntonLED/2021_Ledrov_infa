from random import randint
import pygame


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
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.r = randint(2, 50)
        self.color = color

    def new_target_params(self):
        """
        Функция обновления параметров мишени
        """
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.r = randint(2, 50)

    def draw(self, is_live):
        """
        Функция-отрисовщик движения мишени
        :param is_live: флажок жизни мишени
        """
        if is_live:
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
