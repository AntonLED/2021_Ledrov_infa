from random import choice

import pygame

from Constants import *
from Target import Target


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """
        Конструктор класса Ball. Задает параметры шарика и его движение
        :param screen: поверхность отрисовки в pygame
        :param x: положение шарика вдоль горизонтальной оси (по умолчанию равно координате ствола пушки)
        :param y: положение шарика вдоль веритикальной оси (по умолчанию равно координате ствола пушки)
        """
        self.screen = screen
        self.velocity_loss = 0.25
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 25
        self.gravity = -9.815 / 10

    def move(self):
        """
        Функция, задающая движение шарика и изменяющая параметры шарика во времени
        """
        self.vy += self.gravity
        if self.x + self.r >= 800:
            self.x = 800 - self.r
            self.vx = -self.vx * 0.5
        if self.x - self.r <= 0:
            self.x = self.r
            self.vx = -self.vx * 0.5
        if self.y - self.r <= 0:
            self.y = self.r
            self.vy = -self.vy * 0.5
        if self.y + self.r >= 600 - 50:
            self.y = 600 - 50 - self.r
            self.vy = -self.vy * 0.5
            self.vx = self.vx - self.velocity_loss * self.vx

        self.x += int(self.vx)
        self.y -= int(self.vy) - 1

        if self.y == 536:
            self.live -= 1
            if self.live <= 0:
                self.color = WHITE

    def draw(self):
        """
        Функция-отрисовщик шарика.
        """
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hit_test(self, obj: Target):
        """
        Функция-обработчик попадания шарика по мишени
        :param obj: объект класса Target
        :return: bool попал шарик в цель или нет
        """
        if not self.color == WHITE:
            if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
                return True
            return False
