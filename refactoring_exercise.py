import pygame
import numpy as np
from pygame.draw import *
import random
pygame.init()

def tree(x, y, w, colour):
    '''
    Function draws tree from the top of the screen.
    x - coordinate of the left edge
    y - coordinate of the low edge
    w - width of tree trunk
    colour - colour of tree, written in a suitable form
    '''
    polygon(screen, colour, ((x, 0), (x + w, 0), (x + w, y), (x, y)))

def koluchka(x, y, s):
    '''
    Function draws hedgehog's spike.
    x, y - coordinates of the low left vertex of the spike
    s - coefficient of compression/stretching
    s > 0
    '''
    w = 5*s
    l = 50*s
    a = random.randint(-30, 30)
    a = a/180*np.pi
    polygon(screen, (0, 0, 0), ((x, y), (x + w*np.cos(a), y + w*np.sin(a)),
                                (x + w/2*np.cos(a) + l*np.sin(a), y + w/2*np.sin(a) - l*np.cos(a))))

def iozh(x, y, s, k, colour, colour1, colour2):
    '''
    Function draws hedgehog.
    x, y - coordinates of the left hedgehog's edge
    s - coefficient of compression/stretching
    s > 0
    k = 1,  if hedgehog must look to the right
    k = -1, if hedgehog must look to the left
    colour - colour of the hedgehog's body and head
    colour1 - colour of hedgehog's apple
    colour2 - colour of the hedgehog's mushroom
    '''
    ellipse(screen, colour, (x + (k - 1)*s*50, y, 100*s, 70*s))                      # body
    ellipse(screen, colour, (x + 80*s*k + (k - 1)*s*10, y + 55*s, 20*s, 10*s))       # head
    ellipse(screen, colour, (x + (k - 1)*s*10, y + 55*s, 20*s, 10*s))                # legs
    ellipse(screen, colour, (x - 10*s*k + (k - 1)*s*10, y + 40*s, 20*s, 10*s))
    ellipse(screen, colour, (x + 92*s*k + (k - 1)*s*5, y + 45*s, 10*s, 10*s))
    ellipse(screen, colour, (x + 80*s*k + (k - 1)*s*20, y + 25*s, 40*s, 20*s))
    circle(screen, (0, 0, 0), (x + 120*s*k, y + 35*s), 2*s)                          # nose
    circle(screen, (0, 0, 0), (x + 110*s*k, y + 30*s), 3*s)                          # eyes
    circle(screen, (0, 0, 0), (x + 105*s*k, y + 35*s), 3*s)
    for i in range(10*s, 95*s, 10*s):
        for j in range(30*s, 65*s, 10*s):
            if not ((i > 70*s) and (j > 55*s)):
                koluchka(x + k*i, y + j, s)
    apple(x + (k - 1)*s*15, y, s, colour1)
    apple(x + 10*s*k + (k - 1)*s*15, y, s, colour1)
    grib (x + 50*s*k, y, s, k, colour2)
    for i in range(10*s, 95*s, 10*s):
        for j in range(30*s, 65*s, 10*s):
            if not ((i > 79*s) and (j > 55*s)):
                koluchka(x + k*i, y + j, s)

def grib(x, y, s, k, colour):
    '''
    Function draws mushroom.
    x, y - coordinates of the left border of the mushroom's leg
    s - coefficient of compression/stretching
    s > 0
    k = 1,  if hedgehog must look to the right
    k = -1, if hedgehog must look to the left
    colour - colour of the mushroom's hat
    '''
    ellipse(screen, (255, 255, 255), (x + (k - 1)*s*15, y , 30*s , 50*s))            # mushroom's leg
    ellipse(screen, colour, (x - 20*s*k + (k - 1)*s*35, y, 70*s, 20*s))              # mushroom's hat
    ellipse(screen, (255, 255, 255), (x - 5*s*k + (k - 1)*s*5, y + 5*s, 10*s, 3*s))  # mushroom's dots
    ellipse(screen, (255, 255, 255), (x + 10*s*k + (k - 1)*s*2, y + 5*s, 4*s, 3* s))
    ellipse(screen, (255, 255, 255), (x + 25*s*k + (k - 1)*s*5, y + 5*s, 10*s, 3*s))
    ellipse(screen, (255, 255, 255), (x + 25*s*k + (k - 1)*s*3.5, y + 10*s, 7*s, 3*s))
    ellipse(screen, (255, 255, 255), (x + 10*s*k + (k - 1)*s*3.5, y + 10*s, 7*s, 3*s))

def apple(x, y, s, colour):
    '''
    Function draws apple.
    x, y - coordinates of the left edge of apple
    s - coefficient of compression/stretching
    s > 0
    colour - colour of apple, written in a suitable form
    '''
    ellipse(screen, colour, (x, y , 30*s , 30*s))

FPS = 30
screen = pygame.display.set_mode((800, 1000))
screen.fill((0, 255, 0))                                                             # colour of the wall
polygon(screen, (100, 100, 100), ((0, 600), (0, 1000), (800, 1000), (800, 600)))     # colour of the floor
tree(0, 650, 50, (190, 190, 0))
iozh(400, 600, 1, -1, (0, 0, 150), (0, 255, 0), (255, 0, 0))
tree(100, 980, 150, (190, 190, 0))
tree(600, 650, 70,  (190, 190, 0))
tree(700, 800, 50,  (190, 190, 0))
iozh(400, 800, 2, -1, (60, 60, 60), (255, 255, 0), (255, 0, 0))
iozh(-50, 700, 1, 1, (60, 60, 60), (150 ,150, 150), (0, 255, 0))
iozh(650, 600, 1, 1, (60, 60, 60), (255, 255, 0), (255, 0, 0))
grib(500, 930, 1, 1, (255, 0, 0))
grib(500, 930, 1.1, 1, (255, 0, 255))
grib(600, 930, 1, 1, (255, 0, 0))
grib(650, 930, 0.8, 1, (255, 255, 0))
grib(701, 930, 1.3, 1, (255, 0, 0))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()




