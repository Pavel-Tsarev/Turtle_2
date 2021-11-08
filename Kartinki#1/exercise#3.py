import pygame
from pygame.draw import *

pygame.init()
import numpy as np

FPS = 30
screen = pygame.display.set_mode((600, 800))
polygon(screen, (0, 150, 200), [(0, 0), (600, 0), (600, 400), (0, 400)])
polygon(screen, (70, 230, 150), [(0, 401), (600, 401), (600, 800), (0, 800)])

def zabor(x, y, a, b, n):
    rect(screen, (180, 180, 0), (x, y, a, b))
    h = a / n
    for i in range(n + 1):
        line(screen, (0, 0, 0), (x, y), (x, y + b))
        x = x + h


def psina(x, y, a):
    ellipse(screen, (110, 110, 110),
            (x + 290 * a - (np.abs(a) - a) * 35 / 2, y + 600 * np.abs(a), 35 * np.abs(a), 40 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 317 * a - (np.abs(a) - a) * 9 / 2, y + 625 * np.abs(a), 9 * np.abs(a), 35 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 300 * a - (np.abs(a) - a) * 25 / 2, y + 657 * np.abs(a), 25 * np.abs(a), 12 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 250 * a - (np.abs(a) - a) * 65 / 2, y + 580 * np.abs(a), 65 * np.abs(a), 45 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 243 * a - (np.abs(a) - a) * 30 / 2, y + 580 * np.abs(a), 30 * np.abs(a), 40 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 167 * a - (np.abs(a) - a) * 100 / 2, y + 582 * np.abs(a), 100 * np.abs(a), 70 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 262 * a - (np.abs(a) - a) * 13 / 2, y + 620 * np.abs(a), 13 * np.abs(a), 35 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 252 * a - (np.abs(a) - a) * 22 / 2, y + 650 * np.abs(a), 22 * np.abs(a), 10 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 209 * a - (np.abs(a) - a) * 30 / 2, y + 643 * np.abs(a), 30 * np.abs(a), 60 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 200 * a - (np.abs(a) - a) * 27 / 2, y + 698 * np.abs(a), 27 * np.abs(a), 15 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 150 * a - (np.abs(a) - a) * 30 / 2, y + 605 * np.abs(a), 30 * np.abs(a), 70 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 141 * a - (np.abs(a) - a) * 27 / 2, y + 668 * np.abs(a), 27 * np.abs(a), 15 * np.abs(a)))
    polygon(screen, (0, 0, 0),
            [(x + 160 * a, y + 620 * np.abs(a)), (x + 230 * a, y + 620 * np.abs(a)), (x + 230 * a, y + 550 * np.abs(a)),
             (x + 160 * a, y + 550 * np.abs(a))])
    polygon(screen, (110, 110, 110),
            [(x + 162 * a, y + 618 * np.abs(a)), (x + 228 * a, y + 618 * np.abs(a)), (x + 228 * a, y + 552 * np.abs(a)),
             (x + 162 * a, y + 552 * np.abs(a))])
    ellipse(screen, (0, 0, 0),
            (x + 151 * a - (np.abs(a) - a) * 20 / 2, y + 548 * np.abs(a), 20 * np.abs(a), 30 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 153 * a - (np.abs(a) - a) * 16 / 2, y + 550 * np.abs(a), 16 * np.abs(a), 26 * np.abs(a)))
    ellipse(screen, (0, 0, 0),
            (x + 221 * a - (np.abs(a) - a) * 20 / 2, y + 548 * np.abs(a), 20 * np.abs(a), 30 * np.abs(a)))
    ellipse(screen, (110, 110, 110),
            (x + 223 * a - (np.abs(a) - a) * 16 / 2, y + 550 * np.abs(a), 16 * np.abs(a), 26 * np.abs(a)))
    ellipse(screen, (255, 255, 255),
            (x + 175 * a - (np.abs(a) - a) * 15 / 2, y + 572 * np.abs(a), 15 * np.abs(a), 5 * np.abs(a)))
    ellipse(screen, (255, 255, 255),
            (x + 200 * a - (np.abs(a) - a) * 15 / 2, y + 572 * np.abs(a), 15 * np.abs(a), 5 * np.abs(a)))
    ellipse(screen, (0, 0, 0),
            (x + 205 * a - (np.abs(a) - a) * 6 / 2, y + 572 * np.abs(a), 6 * np.abs(a), 6 * np.abs(a)))
    ellipse(screen, (0, 0, 0),
            (x + 180 * a - (np.abs(a) - a) * 6 / 2, y + 572 * np.abs(a), 6 * np.abs(a), 6 * np.abs(a)))
    polygon(screen, (255, 255, 255), [(x + 180 * a, y + 602 * np.abs(a)), (x + 183 * a, y + 592 * np.abs(a)),
                                      (x + 185 * a, y + 598 * np.abs(a))])
    polygon(screen, (255, 255, 255), [(x + 207 * a, y + 602 * np.abs(a)), (x + 202 * a, y + 598 * np.abs(a)),
                                      (x + 204 * a, y + 592 * np.abs(a))])
    arc(screen, (0, 0, 0),
        (x + 175 * a - (np.abs(a) - a) * 40 / 2, y + 600 * np.abs(a), 40 * np.abs(a), 20 * np.abs(a)), 0, np.pi)


zabor(100, 20, 500, 380, 13)
zabor(-10, 200, 350, 250, 14)
zabor(300, 300, 350, 200, 13)
zabor(-5, 350, 250, 200, 13)

psina(-150, -200, 1.2)
psina(420, 80, -1)
psina(680, 200, -0.5)
polygon(screen, (0, 0, 0), [(380, 555), (380, 455), (440, 395), (480, 375), (520, 455), (520, 535), (485, 615)])
polygon(screen, (200, 200, 0), [(381, 554), (381, 454), (484, 494), (484, 613)])
polygon(screen, (220, 220, 0), [(383, 453), (441, 394), (484, 492)])
polygon(screen, (220, 220, 0), [(480, 376), (443, 394), (486, 492), (518, 454)])
polygon(screen, (200, 200, 0), [(486, 495), (519, 457), (519, 533), (485, 613)])
ellipse(screen, (0, 0, 0), (402, 500, 55, 60))
ellipse(screen, (0, 0, 0), (395, 550, 20, 10), 1)
ellipse(screen, (0, 0, 0), (377, 570, 25, 20), 1)
ellipse(screen, (0, 0, 0), (387, 553, 20, 25), 1)
ellipse(screen, (110, 110, 110), (388, 554, 18, 23))
ellipse(screen, (0, 0, 0), (367, 587, 25, 10), 1)
ellipse(screen, (0, 0, 0), (362, 592, 13, 13), 1)
ellipse(screen, (0, 0, 0), (340, 597, 30, 10), 1)
ellipse(screen, (0, 0, 0), (328, 600, 20, 10), 1)
ellipse(screen, (0, 0, 0), (308, 600, 30, 5), 1)
ellipse(screen, (0, 0, 0), (301, 597, 12, 15), 1)
ellipse(screen, (0, 0, 0), (290, 605, 18, 8), 1)
ellipse(screen, (0, 0, 0), (280, 611, 17, 10), 1)
psina(10, -780, 2.5)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()