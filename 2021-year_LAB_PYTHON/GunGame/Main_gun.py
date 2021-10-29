import pygame
from Constants import *
from Gun import Gun
from Target import Target

# инициализация и настройка pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

# массив объектов класса Ball
balls = []

# инициализация объектов
gun = Gun(screen)
target1 = Target(screen, RED)
target2 = Target(screen, GREEN)

# счетчики и флаги
score = 0
num_shoots = 0
wait_counter = 0
finished = False

# основной цикл программы
while not finished:
    screen.fill(WHITE)
    clock.tick(FPS)

    # обработка шариков
    for b in balls:
        b.draw()
        b.move()
        if b.hit_test(target1) and target1.live:
            score += 0.5
            target1.live = False
            target1.new_target_params()
        if b.hit_test(target2) and target2.live:
            score += 0.5
            target2.live = False
            target2.new_target_params()

    # обработка событий, пушки, мишени и текстового поля
    if target1.live or target2.live or wait_counter >= 100:
        gun.draw()
        target1.draw(is_live=target1.live)
        target2.draw(is_live=target2.live)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.start_shooting()
            elif event.type == pygame.MOUSEBUTTONUP:
                balls.append(gun.make_shell(event))
                num_shoots += 1
            elif event.type == pygame.MOUSEMOTION:
                gun.targeting(event)
        gun.power_up()
        if wait_counter >= 100:
            target1.live = True
            target2.live = True
            num_shoots = 0
        wait_counter = 0
    else:
        text_surface = my_font.render("Вы уничтожили цель за " + str(num_shoots) + " выстрелов.", 0, (0, 0, 0))
        screen.blit(text_surface, (150, 250))
        wait_counter += 1

    # отображение очков игрока
    score_surface = my_font.render(str(score), 1, (0, 0, 0))
    screen.blit(score_surface, (10, 10))

    pygame.display.update()

pygame.quit()
