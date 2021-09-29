import pygame
import pygame.draw as drw

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill([150, 150, 150])

drw.circle(screen, (255, 255, 0), (200, 200), 100)
drw.circle(screen, (255, 0, 0), (200 - 50, 200 - 40), 20)
drw.circle(screen, (255, 0, 0), (200 + 50, 200 - 40), 15)
drw.circle(screen, (0, 0, 0), (200 - 50, 200 - 40), 8)
drw.circle(screen, (0, 0, 0), (200 + 50, 200 - 40), 8)
drw.polygon(screen, "black", [(155, 237), (155, 258), (242, 258), (242, 237)])
drw.polygon(screen, "black", [(155, 237), (155, 258), (242, 258), (242, 237)])
drw.polygon(screen, "black", [(171, 154), (175, 145), (103, 100), (97, 109)])
drw.polygon(screen, "black", [(222, 153), (218, 145), (277, 119), (283, 128)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    if pygame.mouse.get_pressed()[0]:
        print(pygame.mouse.get_pos())

pygame.quit()
