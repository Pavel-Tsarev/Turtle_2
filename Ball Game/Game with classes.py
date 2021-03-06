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
inp = open('Table of Records', 'r')

Stroka = []
Results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(14):                         # это я считываю строки из таблицы рекордов
    Stroka.append(inp.readline())
for i in range(0, 10, 1):                   # это я вынимаю численные значения рекордов
    j = 33
    dlina = 0
    record = 0
    while Stroka[i + 4][j] != '\n':
        dlina = dlina + 1
        j = j + 1
    for f in range(33, j, 1):
        dlina = dlina - 1
        record = record + int(Stroka[i + 4][f])*10**dlina
    Results[i] = record
print(Results)
out = open('Table of Records', 'w')


class Ball:
    def __init__(self, x, y, Vx, Vy, r, color):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.r = r
        self.color = color

    def move(self):
        '''
        метод перемещает шар согласно его скорости
        '''
        circle(screen, BLACK, (self.x, self.y), self.r)
        self.x = self.x + self.Vx
        self.y = self.y + self.Vy
        circle(screen, self.color, (self.x, self.y), self.r)
        circle(screen, (100, 100, 255), (self.x, self.y), 5*self.r/7)
        circle(screen, (255, 0, 0), (self.x, self.y), 3*self.r/7)

    def bonus_action(self):
        '''
        метод хаотично перемещает бонусный объект
        '''
        ellipse(screen, (0, 0, 0), (self.x, self.y, 10, 5))
        circle(screen, (0, 0, 0), (self.x, self.y), self.r)
        self.x = self.x + randint(-20, 20)
        self.y = self.y + randint(-20, 20)
        circle(screen, (0, 110, 0), (self.x, self.y), self.r)
        circle(screen, (0, 0, 0), (self.x, self.y), self.r - 2)
        ellipse(screen, (0, 110, 0), (self.x - self.r - 10, self.y + self.r - 5, 20 + 2*self.r, 10 + self.r/2))
        ellipse(screen, (0, 0, 0), (self.x - self.r - 8, self.y + self.r - 3, 16 + 2*self.r, 6 + self.r/2))

    def collision_wall(self):
        '''
        метод оценивает расстоние от центра шарика до стен и отвечает за отражение шарика от стены в случае касания
        '''
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
        '''
        метод оценивает расстояние от координаты курсора до центра шарика и при попадании курсором по шарику прибавляет
        игровые очки и создает новый шар
        param mouse_x: горизонтальная координата курсора
        param mouse_y: вертикальная координата курсора
        '''
        global score
        global time_live
        if (np.abs(mouse_x - self.x) <= self.r) and (np.abs(mouse_y - self.y) <= self.r):
            score = score + 1
            time_live = time_live + 5
            if (np.abs(mouse_x - self.x) <= self.r) and (np.abs(mouse_y - self.y) <= 5*self.r/7):
                score = score + 1
                time_live = time_live + 5
                if (np.abs(mouse_x - self.x) <= self.r) and (np.abs(mouse_y - self.y) <= 3*self.r/7):
                    score = score + 1
                    time_live = time_live + 5
            if time_live >= 438:                  # проверка того, что линия жизни не вышла за пределы шкалы
                time_live = 437
            self.x = randint(50, 900)
            self.y = randint(100, 650)
            self.r = randint(20, 50)
            self.Vx = randint(-15, 15)
            self.Vy = randint(-15, 15)
            self.color = COLORS[randint(0, 5)]
            print('Попався!')

    def bonus_click(self, mouse_x, mouse_y):
        '''
        метод оценивает расстояние от координаты курсора до бонусного объекта и при попадании курсором
        по бонусному объекту прибавляет игровые очки и создает объект в другом  месте
        param mouse_x: горизонтальная координата курсора
        param mouse_y: вертикальная координата курсора
        '''
        global score
        global time_live
        if (np.abs(mouse_x - self.x) <= self.r) and (np.abs(mouse_y - self.y) <= self.r):
            score = score + 5
            time_live = time_live + 25
            if time_live >= 438:
                time_live = 437
            self.x = randint(50, 900)
            self.y = randint(100, 650)
            self.r = randint(10, 15)
            self.color = COLORS[randint(0, 5)]
            print('Бонус попався!')

    def collision_ball(self, ball):
        '''
        метод оценивает расстояние между 2 шарами и в зависимости от этого меняет скорости так,
        чтобы шары не пересекались
        param ball: объект класса Ball, с которым проверяется столкновение
        '''
        t = (self.x - ball.x)**2 + (self.y - ball.y)**2 - (self.r + ball.r)**2
        if t < 0 and self.x != ball.x and self.y != ball.y:
            self.Vx = -self.Vx
            self.Vy = -self.Vy
            self.x = self.x + (self.x - ball.x)/np.abs(self.x - ball.x)*10       # небольшое изменение координат шарика,
            self.y = self.y + (self.y - ball.y)/np.abs(self.y - ball.y)*10       # чтобы избежать пересечения с другим


BONUS = Ball(randint(50, 850), randint(100, 650), randint(-15, 15), randint(-15, 15), 30, COLORS[0])
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
    polygon(screen, (180, 0, 0), [(500, 20), (850, 20), (850, 40), (500, 40)])      # создание шкалы времени
    polygon(screen, (0, 0, 0), [(502, 22), (847, 22), (847, 38), (502, 38)])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            BONUS.bonus_click(mouse_x, mouse_y)
            for i in range(6):
                LIST_BALLS[i].ball_click(mouse_x, mouse_y)
    BONUS.bonus_action()
    BONUS.collision_wall()
    for i in range(6):
        LIST_BALLS[i].move()
        for j in range(6):
            if i == j:
                pass
            else:
                LIST_BALLS[i].collision_ball(LIST_BALLS[j])
        LIST_BALLS[i].collision_wall()
    time_live = time_live - 1
    polygon(screen, (180, 0, 0), [(502, 22), (502 + time_live, 22), (502 + time_live, 38), (500, 38)])
    if time_live <= 0:
        finished = True
        print('Игра закончена. Ваш результат: ', score)
        if score >= Results[9] and score < Results[0]:
            for i in range(4):
                Stroka[i] = Stroka[i].rstrip()
                print(Stroka[i], file=out)
            for i in range(9):
                if (Results[i] > score) and (score >= Results[i + 1]):
                    Stroka[i + 4] = Stroka[i + 4].rstrip()
                    print(Stroka[i + 4], file=out)
                    print('You                        |    ', score, file=out)
                else:
                    if Results[i] > score:
                        Stroka[i + 4] = Stroka[i + 4].rstrip()
                        print(Stroka[i + 4], file=out)
                    if Results[i] < score:
                        Stroka[i + 4] = Stroka[i + 4].rstrip()
                        print(Stroka[i + 4], file=out)
        else:
            if score < Results[9]:
                for i in range(14):
                    Stroka[i] = Stroka[i].rstrip()
                    print(Stroka[i], file=out)
            if score >= Results[0]:
                for i in range(4):
                    Stroka[i] = Stroka[i].rstrip()
                    print(Stroka[i], file=out)
                print('You                        |    ', score, file=out)
                for i in range(9):
                    Stroka[i + 4] = Stroka[i + 4].rstrip()
                    print(Stroka[i + 4], file=out)
        out.close()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
