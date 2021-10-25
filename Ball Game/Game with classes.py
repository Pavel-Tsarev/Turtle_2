import pygame
import numpy as np
from pygame.draw import *
from random import randint

pygame.font.init()
pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 700))
score = 0
time_live = 347
GREY = (127, 127, 127)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [GREY, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


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
        circle(screen, (100, 100, 255), (self.x, self.y), 5*self.r/7)
        circle(screen, (255, 0, 0), (self.x, self.y), 3*self.r/7)

    def collision_wall(self):
        if self.x + self.r >= 900:
            self.Vx = -1 * self.Vx
            self.x = self.x - 10
        if self.x - self.r <= 0:
            self.Vx = -1 * self.Vx
            self.x = self.x + 10
        if self.y + self.r >= 700:
            self.Vy = -1 * self.Vy
            self.y = self.y - 10
        if self.y - self.r <= 50:
            self.Vy = -1 * self.Vy
            self.y = self.y + 10

    def ball_click(self, mouse_x, mouse_y):
        global score
        if (np.abs(mouse_x - self.x) <= self.r) and (np.abs(mouse_y - self.y) <= self.r):
            score = score + 1
            if (np.abs(mouse_x - self.x) <= self.r) and (np.abs(mouse_y - self.y) <= 5*self.r/7):
                score = score + 1
                if (np.abs(mouse_x - self.x) <= self.r) and (np.abs(mouse_y - self.y) <= 3*self.r/7):
                    score = score + 1
            self.x = randint(50, 900)
            self.y = randint(100, 650)
            self.r = randint(20, 50)
            self.Vx = randint(-15, 15)
            self.Vy = randint(-15, 15)
            self.color = COLORS[randint(0, 5)]
            print('Попався!')


ball_one = Ball(randint(50, 850), randint(100, 650), randint(-15, 15), randint(-15, 15), randint(20, 50), COLORS[0])
ball_two = Ball(randint(50, 850), randint(100, 650), randint(-15, 15), randint(-15, 15), randint(20, 50), COLORS[1])
ball_three = Ball(randint(50, 850), randint(100, 650), randint(-15, 15), randint(-15, 15), randint(20, 50), COLORS[2])
ball_four = Ball(randint(50, 850), randint(100, 650), randint(-15, 15), randint(-15, 15), randint(20, 50), COLORS[3])
ball_five = Ball(randint(50, 850), randint(100, 650), randint(-15, 15), randint(-15, 15), randint(20, 50), COLORS[4])
ball_six = Ball(randint(50, 850), randint(100, 650), randint(-15, 15), randint(-15, 15), randint(20, 50), COLORS[5])
LIST_BALLS = [ball_one, ball_two, ball_three, ball_four, ball_five, ball_six]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    f = pygame.font.Font(None, 36)
    text = f.render('Score: ' + str(score) + '  Time: ', True, (180, 0, 0))
    screen.blit(text, (220, 20))
    polygon(screen, (180, 0, 0), [(500, 20), (850, 20), (850, 40), (500, 40)])
    polygon(screen, (0, 0, 0), [(502, 22), (847, 22), (847, 38), (502, 38)])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            for i in range(6):
                LIST_BALLS[i].ball_click(mouse_x, mouse_y)
    for i in range(6):
        LIST_BALLS[i].move()
        LIST_BALLS[i].collision_wall()
    time_live = time_live - 1
    polygon(screen, (180, 0, 0), [(502, 22), (502 + time_live, 22), (502 + time_live, 38), (500, 38)])
    if time_live <= 0:
        finished = True
        print('Игра закончена. Ваш результат: ', score)
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
