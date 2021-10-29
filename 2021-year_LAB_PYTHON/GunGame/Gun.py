import math

import pygame

from Ball import Ball
from Constants import *


class Gun:
    # длина пушки по умолчанию
    DEFAULT_GUN_LENGTH = 10

    def __init__(self, screen):
        """
        Конструктор класса Gun. Задает параметры пушки по умолчанию
        :param screen: поверхность отрисовки в pygame
        """
        self.screen = screen
        self.fire_power = 10
        self.is_on = 0
        self.angle = 1
        self.color = GREY
        self.length = Gun.DEFAULT_GUN_LENGTH

    def start_shooting(self):
        """
        Поднятие флажка о начале стрельбы
        """
        self.is_on = 1

    def make_shell(self, event):
        """
        Функция-генератор снаряда в виде шарика. Задает параметры снаряда как объекта класса Ball, вылетевшего из пушки
        :param event: событие pygame для детектирование положения компьютерной мыши
        :return: объект класса Ball
        """
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.angle = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.fire_power * math.cos(self.angle)
        new_ball.vy = - self.fire_power * math.sin(self.angle)
        self.is_on = 0
        self.fire_power = 10

        return new_ball

    def targeting(self, event):
        """
        Функция для прицеливания. Задает наклон пушки к горизонту и ее цвет.
        :param event: событие pygame для детектирования положения компьютерной мыши
        """
        if event:
            self.angle = math.atan((event.pos[1] - 450) / (event.pos[0] - 20))

        if self.is_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """
        Функция-отрисовщик ствола пушки
        """
        x_0 = 40
        y_0 = 450
        x_1 = x_0 + self.length * abs(math.cos(self.angle))
        y_1 = y_0 + self.length * math.sin(self.angle)
        pygame.draw.polygon(self.screen, self.color, (
            [x_0, y_0], [x_1, y_1],
            [x_1 - Gun.DEFAULT_GUN_LENGTH * math.sin(self.angle), y_1 + Gun.DEFAULT_GUN_LENGTH * math.cos(self.angle)],
            [x_0 - Gun.DEFAULT_GUN_LENGTH * math.sin(self.angle), y_0 + Gun.DEFAULT_GUN_LENGTH * math.cos(self.angle)]))

    def power_up(self):
        """
        Функция, задающая мощность пушечного выстрела
        """
        if self.is_on:
            if self.fire_power < 100:
                self.length += 1
                self.fire_power += 1
            self.color = RED
        else:
            self.length = Gun.DEFAULT_GUN_LENGTH
            self.color = GREY
