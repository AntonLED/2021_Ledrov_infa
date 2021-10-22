from random import randint
import pygame
import pygame.draw as dr

width = 1200
height = 600
FPS = 100

pygame.init()
screen = pygame.display.set_mode((width, height))

pygame.font.init()
new_font = pygame.font.SysFont('arial', 30, bold=2)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_figure(fig_type):
    """
    Создает новую фигуру как объект игры с определенными параметрами
    :param fig_type: тип фигуры, крудок или квадратик
    :return: спиок параметров данной фигуры
    """
    if fig_type == "BALL":
        new_color = COLORS[randint(0, 5)]
        new_r = randint(20, 50)
        new_x = randint(new_r, width - new_r)
        new_y = randint(new_r, height - new_r)
        new_vx = randint(-5, 5)
        new_vy = randint(-5, 5)
        return [new_color, new_r, new_x, new_y, new_vx, new_vy]
    elif fig_type == "SQUARE":
        new_color = COLORS[randint(0, 5)]
        size = randint(50, 80)
        new_x = randint(0, width - size)
        new_y = randint(0, height - size)
        new_vx = randint(-20, 20)
        new_vy = randint(-20, 20)
        return [new_color, size, new_x, new_y, new_vx, new_vy]


def draw_figure(fig_type, who_new, is_new=False):
    """
    Отрисовывает фигуру на экране и задает ее механику поведения
    :param fig_type: тип фигуры, кружок или квадратик
    :param who_new: номер фигуры в массиве фигур, задействованных в игровом процессе
    :param is_new: флаг новой фигуры, если опущен, отрисовывает старую
    """
    if fig_type == "BALL":
        if is_new:
            balls[who_new] = new_figure(fig_type)
            dr.circle(screen, balls[who_new][0], (balls[who_new][2], balls[who_new][3]), balls[who_new][1])
        else:
            screen.fill(BLACK)
            for ball in balls:
                if ball[2] <= ball[1] or ball[2] >= width - ball[1]:
                    ball[4] = -ball[4]
                if ball[3] <= ball[1] or ball[3] >= height - ball[1]:
                    ball[5] = -ball[5]
                ball[2] += ball[4]
                ball[3] += ball[5]
                dr.circle(screen, ball[0], (ball[2], ball[3]), ball[1])
    elif fig_type == "SQUARE":
        if is_new:
            squares[who_new] = new_figure(fig_type)
            dr.rect(screen, squares[who_new][0], (squares[who_new][2], squares[who_new][3],
                                               squares[who_new][1],
                                               squares[who_new][1]))
        else:
            for square in squares:
                if square[2] <= 0 or square[2] >= width - square[1]:
                    square[2] = randint(0, width - square[1])
                if square[3] <= 0 or square[3] >= height - square[1]:
                    square[3] = randint(0, height - square[1])
                square[2] += square[4] * randint(-20, 20) / 10
                square[3] += square[5] * randint(-20, 20) / 10
                dr.rect(screen, square[0], (square[2], square[3], square[1], square[1]))


def is_cached(fig_type):
    """
    Функця-обработчик, детектирующая попадание игрока по фигуре
    :param fig_type: тип фигуры, кружок или квадратик
    :return: количество очков за ту или иную фигуру, иначе 0 очков
    """
    if fig_type == "BALL":
        for ball in balls:
            if ((ball[2] - event.pos[0]) ** 2 + (ball[3] - event.pos[1]) ** 2) ** 0.5 <= ball[1]:
                draw_figure(fig_type, balls.index(ball), True)
                return 1
    elif fig_type == "SQUARE":
        for square in squares:
            if ((square[2] - event.pos[0]) ** 2 + (square[3] - event.pos[1]) ** 2) ** 0.5 <= square[1]:
                draw_figure(fig_type, squares.index(square), True)
                return 2
    return 0


def records_sheet_upd():
    """
    Заполняет txt-файл с топом лучших игроков
    """
    with open("records.txt", "r+") as records:
        A = records.readlines()
        names_with_results = []
        for a in A:
            names_with_results.append(a.split())
        for name_and_result in names_with_results:
            name_and_result[3] = int(name_and_result[3])
            name_and_result.pop(0)
        new_player = str(input("Your name is: "))
        new_player = new_player.split()
        names_with_results.append([new_player[0], new_player[1], rat])
        j = -1
        for i in range(len(names_with_results)):
            j += 1
            for o in range(j, len(names_with_results)):
                if names_with_results[i][2] < names_with_results[o][2]:
                    names_with_results[i], names_with_results[o] = names_with_results[o], names_with_results[i]

    with open("records.txt", "w") as records:
        place_number = 1
        for name_and_result in names_with_results:
            if place_number == 11:
                break
            # noinspection PyTypeChecker
            name_and_result.insert(0, place_number)
            name_and_result.append("\n")
            name_and_result = " ".join(map(str, name_and_result))
            records.write(name_and_result)
            place_number += 1


def text_space_upd(score, g_time, limit):
    """
    Обновление текстовых полей на экране
    :param score: текущее количество очков
    :param g_time: время игры
    :param limit: дефолтная продолжительность игры
    """
    lost_time = new_font.render(str(int((limit - g_time) / FPS) // 10 + (
            int((limit - g_time) / FPS) % 10) / 10), False, (255, 255, 255))

    upped_points = new_font.render(str(score), False, (255, 255, 255))

    screen.blit(time_table, (10, 10))
    screen.blit(lost_time, (10, 50))

    screen.blit(score_table, (1040, 10))
    screen.blit(upped_points, (1040, 50))


# Начальная генерация объектов в соответвующие ячейки массивов
num_balls = 10
num_sq = 10
balls = [new_figure("BALL") for _ in range(num_balls)]
squares = [new_figure("SQUARE") for _ in range(num_sq)]

# Счетчики
rat = 0
counter_new_ball = 0
counter_new_square = 0

# Частота появления новых фигур
upd_freq_ball = 50
upd_freq_square = 10

# Настройка текстового поля
score_table = new_font.render("SCORE:", False, (255, 255, 255))
time_table = new_font.render("TIME:", False, (255, 255, 255))

# Дефолтный лимит игрового времени
time_limit = 600 * FPS

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    # Обработка времени игры
    gaming_time = pygame.time.get_ticks()
    if time_limit - gaming_time <= 0:
        finished = True

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rat += is_cached("BALL")
            rat += is_cached("SQUARE")

    # Основная отрисовка фигур
    draw_figure("BALL", None)
    draw_figure("SQUARE", None)

    counter_new_ball += 1
    if counter_new_ball >= upd_freq_ball:
        draw_figure("BALL", randint(0, len(balls) - 1), True)
        counter_new_ball = 0
    counter_new_square += 1
    if counter_new_square >= upd_freq_square:
        draw_figure("SQUARE", randint(0, len(squares) - 1), True)
        counter_new_square = 0

    # Обновление текстовых полей
    text_space_upd(rat, gaming_time, time_limit)

    pygame.display.update()

pygame.quit()

# Запись в таблицу с игроками
records_sheet_upd()
