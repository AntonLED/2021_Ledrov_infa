import math
from random import choice

import pygame

from Constants import *
from Shell import Shell


class Gun:
    # длина и скорость пушки по умолчанию
    DEFAULT_GUN_LENGTH = 10
    SPEED = 2

    def __init__(self, screen, x=40, y=490):
        """
        Конструктор класса Gun, задающий параметры пушки
        :param screen: повержность отрисовки pygame
        :param x: начальная координата пушки по горизонтальной оси
        :param y: наччальная координата пушки по вертикальной оси
        """
        self.screen = screen
        self.x = x
        self.vx = 10
        self.y = y
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
        Функция-генератор снаряда как объекта класса Shell
        :param event: событие pygame
        :return: булева 1 если не произошло ошибок
        """
        new_shell = Shell(self.screen, self.x)
        new_shell.type = choice(list(GAME_SHELLS.values()))
        new_shell.r += 5
        self.angle = math.atan2((event.pos[1] - new_shell.y), (event.pos[0] - new_shell.x))
        new_shell.vx = self.fire_power * math.cos(self.angle)
        new_shell.vy = - self.fire_power * math.sin(self.angle)
        self.is_on = 0
        self.fire_power = 10
        Shell.shells.append(new_shell)
        return True

    def targeting(self, event):
        """
        Функция для прицеливания. Задает наклон пушки к горизонту и ее цвет.
        :param event: событие pygame для детектирования положения компьютерной мыши
        """
        if event:
            if not event.pos[0] == self.x:
                self.angle = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))

        if self.is_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """
        Функция-отрисовщик ствола пушки
        """
        if self.angle >= 0:
            self.angle = self.angle + math.pi

        x_1 = self.x + self.length * math.cos(self.angle)
        y_1 = self.y + self.length * math.sin(self.angle)
        pygame.draw.polygon(self.screen, self.color, (
            [self.x, self.y], [x_1, y_1],
            [x_1 - Gun.DEFAULT_GUN_LENGTH * math.sin(self.angle),
             y_1 + Gun.DEFAULT_GUN_LENGTH * math.cos(self.angle)],
            [self.x - Gun.DEFAULT_GUN_LENGTH * math.sin(self.angle),
             self.y + Gun.DEFAULT_GUN_LENGTH * math.cos(self.angle)]))
        self.gun_body()

    def gun_body(self):
        """
        Функция-отрисовщик корпуса танка
        """
        r = 3.8
        pygame.draw.circle(self.screen, GREY, [self.x + 3, self.y + 3], 10)
        pygame.draw.circle(self.screen, BLACK, [self.x - 13 * r, self.y + 13 * r], 10)
        pygame.draw.circle(self.screen, BLACK, [self.x - 13 * r + 20, self.y + 13 * r], 10)
        pygame.draw.circle(self.screen, BLACK, [self.x - 13 * r + 40, self.y + 13 * r], 10)
        pygame.draw.circle(self.screen, BLACK, [self.x - 13 * r + 60, self.y + 13 * r], 10)
        pygame.draw.circle(self.screen, BLACK, [self.x - 13 * r + 80, self.y + 13 * r], 10)
        pygame.draw.polygon(self.screen, GREY, (
            [self.x, self.y],
            [self.x + 5 * r, self.y + 5 * r],
            [self.x + 15 * r, self.y + 5 * r],
            [self.x + 10 * r, self.y + 12 * r],
            [self.x - 15 * r, self.y + 12 * r],
            [self.x - 20 * r, self.y + 5 * r],
            [self.x - 13 * r, self.y + 5 * r],
            [self.x - 8 * r, self.y - 1 * r],
            [self.x - 2 * r, self.y - 1 * r]))

    def shoot_boosting(self):
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

    def move(self):
        """
        Функция, определяющее движение такнка влево и вправо по нажатиям на клавищи "A" и "F" соответственно
        """
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a]) and (self.x > 40):
            self.x -= Gun.SPEED
        elif (keys[pygame.K_d]) and (self.x < WIDTH - 40):
            self.x += Gun.SPEED
