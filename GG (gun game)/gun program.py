import pygame
import numpy as np
from pygame.draw import *
from random import randint

pygame.font.init()
pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 700))
score = 0
snaryad_time = 70
ready = 2
h = 10*2**0.5
l = 25
v = 5
a = 0
fly = -1
bomb_number = 0
x_pushka = 450
dviz_pushka = 0
time_live = 347
GREY = (127, 127, 127)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [GREY, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
inp = open('Table of records(gun)', 'r')
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
out = open('Table of records(gun)', 'w')


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

    def smert_move(self):
        '''
        метод хаотично перемещает череп
        '''
        circle(screen, (0, 0, 0), (self.x, self.y), 25)
        circle(screen, (0, 0, 0), (self.x, self.y + 12.5), 12.5)
        if np.abs(self.x - 450) <= 450 and np.abs(self.y - 350) <= 300:
            self.x = self.x + randint(-20, 20)
            self.y = self.y + randint(-20, 20)
        else:
            self.x = self.x + 20*np.abs(450 - self.x)/(450 - self.x)
            self.y = self.y + 20*np.abs(350 - self.y)/(350 - self.y)
        circle(screen, (255, 255, 255), (self.x, self.y), 25)
        circle(screen, (255, 255, 255), (self.x, self.y + 12.5), 12.5)
        circle(screen, (0, 0, 0), (self.x - 5, self.y - 5), 5)
        circle(screen, (0, 0, 0), (self.x + 5, self.y - 5), 5)
        polygon(screen, (0, 0, 0), [(self.x - 10, self.y + 5), (self.x - 10, self.y + 20),
                                    (self.x + 10, self.y + 20), (self.x + 10, self.y + 5)], 2)
        polygon(screen, (0, 0, 0), [(self.x - 20/6, self.y + 5), (self.x - 20/6, self.y + 20),
                                    (self.x + 20/6, self.y + 20), (self.x + 20/6, self.y + 5)], 2)

    def collision_wall(self):
        '''
        метод оценивает расстояние от центра шарика до стен и отвечает за отражение шарика от стены в случае касания
        '''
        if self.x + self.r >= 900:
            self.Vx = -1 * self.Vx
            self.x = self.x - 10
        if self.x - self.r <= 100:
            self.Vx = -1 * self.Vx
            self.x = self.x + 10
        if self.y + self.r >= 670:
            self.Vy = -1 * self.Vy
            self.y = self.y - 10
        if self.y - self.r <= 50:
            self.Vy = -1 * self.Vy
            self.y = self.y + 10

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

    def collision_snaryad(self, ball):
        '''
        метод оценивает расстояние от шарика до снаряда и в случае
        столкновения убирает сняряд и создает новый шар
        '''
        global score, time_live
        t = (self.x - ball.x) ** 2 + (self.y - ball.y) ** 2 - (self.r + ball.r) ** 2
        if t < 0 and ball.color != (0, 0, 0):
            time_live = time_live + 15 - self.r/5                               # добавочное время и количество очков
            score = score + 55 - self.r*2                                       # зависят от радиуса подбитого шара
            self.Vx = randint(-15, 15)
            self.Vy = randint(-15, 15)
            self.x = randint(200, 850)
            self.y = randint(100, 650)
            self.color = COLORS[randint(0, 5)]
            self.r = randint(10, 20)
            ball.Vx = 0
            Ball.Vy = 0
            ball.color = (0, 0, 0)
            print('Есть пробитие!')

    def snaryad_move(self):
        '''
        метод перемещает снаряд согласно его скорости
        '''
        if snaryad_time > 0:
            circle(screen, BLACK, (self.x, self.y), self.r)
            self.x = self.x + self.Vx
            self.y = self.y + self.Vy
            circle(screen, self.color, (self.x, self.y), self.r)
            self.Vy = self.Vy + 2
        else:
            self.Vx = 0
            self.Vy = 0

    def create_bomb(self, ball):
        self.x = ball.x
        self.y = ball.y - 37.5 - 8
        self.Vy = 0

    def bomb_fall(self):
        global bomb_number
        ellipse(screen, (0, 0, 0), (self.x - 2, self.y + 4, 4, 8))
        if self.y >= 700:
            self.x = 0
            self.y = 0
            self.Vy = 0
            bomb_number = 0
        else:
            self.Vy = self.Vy - 0.5
            self.y = self.y - self.Vy
            ellipse(screen, (124, 124, 124), (self.x - 2, self.y + 4, 8, 16))

class Gun:
    def __init__(self, a, l, x):
        self.a = a
        self.l = l
        self.x = x

    def draw_gun(self):
        '''
        Рисует пушку, направленную на курсор мыши
        '''
        polygon(screen, GREEN, [(self.x - 50, 680), (self.x + 50, 680), (self.x + 50, 660), (self.x - 50, 660)])
        cosa = self.a/np.abs(self.a)*1/(self.a**2 + 1)**0.5
        sina = np.abs(self.a)/(self.a**2 + 1)**0.5
        if ready == 1:
            colour = (200, 0, 0)
        if ready == 0 or ready == 2:
            colour = GREEN
        polygon(screen, colour, [(self.x + h*(cosa + sina)/2**0.5, 680 - h*(sina - cosa)/2**0.5),
                                 (self.x + h*(cosa + sina)/2**0.5 + self.l*cosa, 680 - h*(sina - cosa)/2**0.5 - self.l*sina),
                                 (self.x + h*(cosa - sina)/2**0.5 + self.l*cosa, 680 - h*(sina + cosa)/2**0.5 - self.l*sina),
                                 (self.x + h*(cosa - sina)/2**0.5, 680 - h*(sina + cosa)/2**0.5)])

    def bomb_explosion(self, ball):
        global time_live
        if self.x - 50 <= ball.x and self.x + 50 >= ball.x and ball.y >= 668:
            print('Вы взорваны. Окончательно и безповоротно')
            time_live = 0


ball_one = Ball(randint(200, 850), randint(100, 650), randint(-15, 15), randint(-15, 15), randint(10, 20), COLORS[randint(0, 5)])
ball_two = Ball(randint(200, 850), randint(100, 650), randint(-15, 15), randint(-15, 15), randint(10, 20), COLORS[randint(0, 5)])
bomb = Ball(0, 0, 0, 0, 1, (0, 0, 0))
Smert_one = Ball(randint(200, 850), randint(100, 650), randint(-15, 15), randint(-15, 15), 30, (255, 255, 255))
Smert_two = Ball(randint(200, 850), randint(100, 650), randint(-15, 15), randint(-15, 15), 30, (255, 255, 255))
snaryad = Ball(300, 300, 0, 0, 1, (0, 0, 0))
LIST_BALLS = [ball_one, ball_two]
LIST_SMERTS = [Smert_one, Smert_two]
Pushka = Gun(0, 20, 450)

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            dviz_pushka = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            dviz_pushka = -1
        if event.type == pygame.KEYUP:
            dviz_pushka = 0
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ready = 1
        elif event.type == pygame.MOUSEBUTTONUP and fly == 0:
            ready = 0
        elif event.type == pygame.MOUSEBUTTONUP and fly == 1:
            ready = 2
        elif event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0]
            if mouse_x == 450:
                mouse_x = 450.0001
            mouse_y = event.pos[1]
            a = (mouse_y - 780) / (450 - mouse_x)
            x = x_pushka
            Pushka = Gun(a, l, x)
    Pushka.draw_gun()
    if ready == 1:
        l = l + 2
        if l >= 100:
            l = 99
        v = v + 2
        fly = 0
    if x_pushka >= 50 and x_pushka <= 850:
        x_pushka = x_pushka + dviz_pushka*2
    else:
        x_pushka = x_pushka + (450 - x_pushka)/np.abs(450 - x_pushka)
    if ready == 0:
        rad = randint(15, 30)
        snaryad = Ball(x_pushka + (10 + l + rad)*a/np.abs(a)/(a**2 + 1)**0.5, 680 - (10 + l + rad)*np.abs(a)/(a**2 + 1)**0.5,
                       v*(a/np.abs(a))/(a**2 + 1)**0.5, v*(-1)*np.abs(a)/(a**2 + 1)**0.5, rad, (255, 0, 0))
        l = 25
        v = 5
        snaryad_time = 50
        fly = 1
        ready = 2
    if fly > 0:
        snaryad.snaryad_move()
        snaryad.collision_wall()
        snaryad_time = snaryad_time - 1
    if snaryad_time <= 0.9:
        fly = 0
    for i in range(2):
        LIST_BALLS[i].move()
        LIST_BALLS[i].collision_snaryad(snaryad)
        for j in range(2):
            if i == j:
                pass
            else:
                LIST_BALLS[i].collision_ball(LIST_BALLS[j])
        LIST_BALLS[i].collision_wall()
    for i in range(2):
        LIST_SMERTS[i].smert_move()
        LIST_SMERTS[i].collision_snaryad(snaryad)
        for j in range(2):
            if i == j:
                LIST_SMERTS[i].collision_ball(LIST_BALLS[j])
            else:
                LIST_SMERTS[i].collision_ball(LIST_BALLS[j])
                LIST_SMERTS[i].collision_ball(LIST_SMERTS[j])
    if bomb_number == 0:
        i = randint(0, 1)
        p = randint(-10, 10)
        if p == 0:
            bomb.create_bomb(LIST_SMERTS[i])
            bomb_number = 1
    if bomb_number == 1:
        bomb.bomb_fall()
        Pushka.bomb_explosion(bomb)
    time_live = time_live - 0.5
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
