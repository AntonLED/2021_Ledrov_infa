import pygame

from Constants import *
from Gun import Gun
from Shell import Shell
from Target import Target

# инициализация и настройка pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

# инициализация объектов
gun = Gun(screen)
target1 = Target(screen, RED)
target2 = Target(screen, GREEN)
game_shells = Shell(screen)

# счетчики и флаги
score = 0
num_shoots = 0
wait_counter = 0
finished = False
t1_is_live = True
t2_is_live = True

# основной цикл программы
while not finished:
    clock.tick(FPS)
    screen.fill(WHITE)

    if t1_is_live:
        t1_is_live = target1.is_draw(is_live=not game_shells.hit_success(target1))

    if t2_is_live:
        t2_is_live = target2.is_draw(is_live=not game_shells.hit_success(target2))

    if t1_is_live or t2_is_live:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.start_shooting()
            elif event.type == pygame.MOUSEBUTTONUP:
                num_shoots += gun.make_shell(event)
            elif event.type == pygame.MOUSEMOTION:
                gun.targeting(event)
        gun.move()
        gun.draw()
        gun.shoot_boosting()
    else:
        target1.setting()
        target2.setting()
        text_surface = my_font.render("Вы уничтожили цели за " + str(num_shoots) + " выстрелов.", 0, (0, 0, 0))
        screen.blit(text_surface, (150, 250))
        wait_counter += 1
        if wait_counter >= 100:
            score += 1
            num_shoots = 0
            wait_counter = 0
            t1_is_live = True
            t2_is_live = True

    game_shells.moving()
    game_shells.draw()

    # отображение очков игрока
    score_surface = my_font.render(str(score), 1, (0, 0, 0))
    screen.blit(score_surface, (10, 10))

    # отрисовка поверхности земли
    pygame.draw.rect(screen, GREY, (0, 551, 1000, 200))

    pygame.display.update()

pygame.quit()
