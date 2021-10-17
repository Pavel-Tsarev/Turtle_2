import pygame
import numpy as np
import sys
from pygame.draw import *
from random import randint

pygame.font.init()
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 450))
score = 0
x1 = randint(50, 550)              #здесь я назначаю координаты шариков
x2 = randint(50, 550)
y1 = randint(100, 400)
y2 = randint(100, 400)
r1 = randint(15, 30)               #здесь я назначаю радиусы шариков
r2 = randint(15, 50)
Vx1 = randint(-15, 15)             #здесь я назначаю скорости шариков
Vx2 = randint(-15, 15)
Vy1 = randint(-15, 15)
Vy2 = randint(-15, 15)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball(x, y, r):
    '''
    рисует шарик заданного радиуса в указанной точке
    x - горизонтальная координата центра
    y - вертикальная координата центра
    r - радиус
    '''
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    f = pygame.font.Font(None, 36)
    text = f.render('Score: ' + str(score), 1, (180, 0, 0))
    screen.blit(text, (280, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x0 = event.pos[0]
            y0 = event.pos[1]
            if (np.abs(x0 - x1) <= r1) and (np.abs(y0 - y1) <= r1):
                print('Catched!')
                score = score + 1
                x1 = randint(50, 550)                     #создает новый шар в другом месте
                y1 = randint(100, 400)
                r1 = randint(15, 50)
                Vx1 = randint(-15, 15)
                Vy1 = randint(-15, 15)
            if (np.abs(x0 - x2) <= r2) and (np.abs(y0 - y2) <= r2):
                print('Catched!')
                score = score + 1
                x2 = randint(50, 550)                     #создает новый шар в другом месте
                y2 = randint(100, 400)
                r2 = randint(15, 50)
                Vx2 = randint(-15, 15)
                Vy2 = randint(-15, 15)
    new_ball(x1, y1, r1)
    x1 = x1 + k1*Vx1
    y1 = y1 + l1*Vy1
    if (x1 + r1 >= 600):                                 #первый шар отражается от стенок
        Vx1 = -1*Vx1
        x1 = x1 - 10
    if (x1 - r1 <= 0):
        Vx1 = -1*Vx1
        x1 = x1 +10
    if (y1 + r1 >= 450):
        Vy1 = -1*Vy1
        y1 = y1 - 10
    if (y1 - r1 <= 50):
        l1 = -1*Vy1
        y1 = y1 + 10
    new_ball(x2, y2, r2)
    x2 = x2 + k2 * Vx2
    y2 = y2 + l2 * Vy2
    if (x2 + r2 >= 600):                                 #второй шар отражается от стенок
        Vx2 = -1 * Vx2
        x2 = x2 - 10
    if (x2 - r2 <= 0):
        Vx2 = -1 * Vx2
        x2 = x2 + 10
    if (y2 + r2 >= 450):
        Vy2 = -1 * Vy2
        y2 = y2 - 10
    if (y2 - r2 <= 50):
        Vy2 = -1 * Vy2
        y2 = y2 + 10
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()