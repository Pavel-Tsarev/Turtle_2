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
x1 = randint(50, 550)
x2 = randint(50, 550)
y1 = randint(100, 400)
y2 = randint(100, 400)
r1 = randint(15, 30)
r2 = randint(15, 50)
Vx1 = randint(-15, 15)
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


class Ball:
    def __init__(self, x, y, Vx, Vy, r, color):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.r = r
        self.color = color

    def move(self):
        circle(screen, BLACK, (self.x, self.y), self.r)
        self.x = self.x + self.Vx
        self.y = self.y + self.Vy
        circle(screen, self.color, (self.x, self.y), self.r)

    def collision_wall(self):
        if self.x + self.r >= 600:
            self.Vx = -1 * self.Vx
            self.x = self.x - 10
        if self.x - self.r <= 0:
            self.Vx = -1 * self.Vx
            self.x = self.x + 10
        if self.y + self.r >= 450:
            self.Vy = -1 * self.Vy
            self.y = self.y - 10
        if self.y - self.r <= 50:
            self.Vy = -1 * self.Vy
            self.y = self.y + 10

    def ball_click(self, x0, y0):
        global score
        if (np.abs(x0 - self.x) <= self.r) and (np.abs(y0 - self.y) <= self.r):
            self.x = randint(50, 550)
            self.y = randint(100, 400)
            self.r = randint(15, 50)
            self.Vx = randint(-15, 15)
            self.Vy = randint(-15, 15)
            self.color = COLORS[randint(0, 5)]
            print('Попався!')
            score = score + 1

ball_one = Ball(x1, y1, Vx1, Vy1, r1, COLORS[0])

def draw_ball(x, y, r):
    circle(screen, COLORS[3], (x, y), r)

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
            ball_one.ball_click(x0, y0)
            if (np.abs(x0 - x2) <= r2) and (np.abs(y0 - y2) <= r2):
                print('Попався!')
                score = score + 1
                x2 = randint(50, 550)
                y2 = randint(100, 400)
                r2 = randint(15, 50)
                Vx2 = randint(-15, 15)
                Vy2 = randint(-15, 15)
    ball_one.move()
    ball_one.collision_wall()
    draw_ball(x2, y2, r2)
    x2 = x2 + Vx2
    y2 = y2 + Vy2
    if (x2 + r2 >= 600):
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