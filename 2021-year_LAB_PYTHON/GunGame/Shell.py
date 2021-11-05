from random import choice

import pygame

from Constants import *
from Target import Target


class Shell:
    shells = []

    def __init__(self, screen: pygame.surface, x=40, y=490):
        """
        Конструктор класса Shell. задает параметры цели и ее движение
        :param screen: поверхность отрисовки в pygame
        :param x: положение шарика вдоль горизонтальной оси (по умолчанию равно координате ствола пушки)
        :param y: положение шарика вдоль веритикальной оси (по умолчанию равно координате ствола пушки)
        """
        self.screen = screen
        self.type = None
        self.velocity_loss = 0.25
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 25
        self.gravity = -9.815 / 10

    def moving(self):
        """
        функция, задающая движение шарика и изменяющая параметры снаряда во времени
        """
        for shell in self.shells:
            if shell.type == GAME_SHELLS["BALL"]:
                shell.vy += shell.gravity
                if shell.x + shell.r >= 800:
                    shell.x = 800 - shell.r
                    shell.vx = -shell.vx * 0.5
                if shell.x - shell.r <= 0:
                    shell.x = shell.r
                    shell.vx = -shell.vx * 0.5
                if shell.y - shell.r <= 0:
                    shell.y = shell.r
                    shell.vy = -shell.vy * 0.5
                if shell.y + shell.r >= 600 - 50:
                    shell.y = 600 - 50 - shell.r
                    shell.vy = -shell.vy * 0.5
                    shell.vx = shell.vx - shell.velocity_loss * shell.vx
                shell.x += int(shell.vx)
                shell.y -= int(shell.vy) - 1
                if shell.y == 536:
                    shell.live -= 1
                    if shell.live <= 0:
                        self.shells.pop(self.shells.index(shell))

            elif shell.type == GAME_SHELLS["SPECIAL_BALL"]:
                shell.vy += -shell.gravity
                if shell.x + shell.r >= 800:
                    shell.x = 800 - shell.r
                    shell.vx = -shell.vx * 1.1
                    shell.r -= 5
                if shell.x - shell.r <= 0:
                    shell.x = shell.r
                    shell.vx = -shell.vx * 1.1
                    shell.r -= 5
                if shell.y - shell.r <= 0:
                    shell.y = shell.r
                    shell.vy = -shell.vy * 1.1
                    shell.r -= 5
                if shell.y + shell.r >= 600 - 50:
                    shell.y = 600 - 50 - shell.r
                    shell.vy = -shell.vy * 1.1
                    shell.r -= 5
                shell.x += int(shell.vx)
                shell.y -= int(shell.vy) - 1
                if shell.r == 0:
                    shell.live = 0
                    if shell.live <= 0:
                        self.shells.pop(self.shells.index(shell))

    def draw(self):
        """
        Функция-отрисовщик снаряда
        """
        for shell in self.shells:
            pygame.draw.circle(
                shell.screen,
                shell.color,
                (shell.x, shell.y),
                shell.r, shell.type)

    def hit_success(self, obj: Target):
        """
        функция-обработчик попадания шарика по мишени
        :param obj: объект класса Target
        :return: bool попал снаряд в цель или нет
        """
        for shell in self.shells:
            if (shell.x - obj.x) ** 2 + (shell.y - obj.y) ** 2 <= (shell.r + obj.r) ** 2:
                return True
        return False
