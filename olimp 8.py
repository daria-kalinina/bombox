import os
import sys
import pygame
import random
import time, datetime


def fon1():
    timer_stop = datetime.datetime.utcnow() + datetime.timedelta(seconds=15)
    sizef = width, height = 600, 600
    screen = pygame.display.set_mode(sizef)
    namef = 'mol1.png'
    fullname = os.path.join('data', namef)
    imagef = pygame.image.load(fullname)
    xf = 0
    yf = 0
    imagef = pygame.transform.scale(imagef, (600, 600))
    run1 = True
    while run1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
            screen.blit(imagef, (xf, yf))
        pygame.display.flip()
        if datetime.datetime.utcnow() > timer_stop:
            break
    pygame.quit()
fon1()

pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.draw.line(screen, 'white', (0, 28), (600, 28), width=1)


def fon():
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    name = 'mol.png'
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    x = 0
    y = 0
    image = pygame.transform.scale(image, (600, 600))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            screen.blit(image, (x, y))
        pygame.display.flip()
    pygame.quit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (30, 30))
    return image

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(str(text), True, 'black')
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    text += 10
    text_surface = font.render(str(text), True, 'white')
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def load_level(filename):
    y1 = 0
    c = []
    c1 = []
    c2 = []
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        for y in mapFile:
            if '\n' in y:
                y = y[:-1]
            y1 += 1
            for x in range(20):
                if y[x] == '#':
                    c.append([x*30, y1*30])
                    c1.append(x*30)
                    c2.append(y*30)
    return [c, c1, c2]

image = load_image("bomb.png")
x=10
y=40
image = pygame.transform.scale(image, (30, 30))
screen.blit(image, (x, y))
running = True
v = 40
x_clock = pygame.time.Clock()
y_clock = pygame.time.Clock()
xdir = 1
ydir = 0


image_ap = load_image("apple.png")
image_ap = pygame.transform.scale(image_ap, (30, 30))
x_ap=10
y_ap=40
screen.blit(image_ap, (x_ap, y_ap))
scht = -10
nx = []
ny = []
running = True
while running:
    pygame.draw.rect(screen, (0, 0, 0), ((x, y), (30, 30)))
    x += xdir * v * x_clock.tick() / 1000
    y += ydir * v * y_clock.tick() / 1000
    screen.blit(image, (x, y))
    screen.blit(image_ap, (x_ap, y_ap))
    pygame.display.flip()
    c_ap = abs(abs(x) - abs(x_ap))                                ### ЗДЕСЬ У НАС ЯБЛОЧКО
    d_ap = abs(abs(y) - abs(y_ap))
    if c_ap < 15 and d_ap < 15:
        v += 10
        draw_text(screen, scht, 18, width / 2, 10)
        pygame.draw.rect(screen, (0, 0, 0), ((x_ap, y_ap), (30, 30)))
        scht += 10
        nx.append(x_ap)
        ny.append(y_ap)
        while x_ap in nx or y_ap in ny:
            x_ap = random.randint(30, 570)
            y_ap = random.randint(70, 570)
    na = str(int(scht // 10))
    if scht < 100:
        c = load_level(f'{na}.txt')
    else:
        running = False
        fon()
        break
    coors = c[0]
    nx = c[1]
    ny = c[2]
    image_b = load_image("box.png")
    image_b = pygame.transform.scale(image_b, (25, 25))
    for i in coors:
        x_b = i[0]
        y_b = i[1]
        screen.blit(image_b, (x_b, y_b))
        c_b = abs(abs(x) - abs(x_b))  ### А ЗДЕСЬ НАЧИНАЕТСЯ УРОВЕНЬ
        d_b = abs(abs(y) - abs(y_b))
        if c_b < 30 and d_b < 30:
            pygame.draw.rect(screen, (0, 0, 0), ((x, y), (30, 30)))
            x=10
            y=40
        c_ba = abs(abs(x_ap) - abs(x_b))
        d_ba = abs(abs(y_ap) - abs(y_b))
        if c_ba < 30 and d_ba < 30:
            pygame.draw.rect(screen, (0, 0, 0), ((x_ap, y_ap), (30, 30)))
            x_ap = random.randint(30, 570)
            y_ap = random.randint(70, 570)
    if y < 32:
        xdir = 0
        ydir = 1
    if y > 570:
        xdir = 0
        ydir = -1
    if x < 0:
        xdir = 1
        ydir = 0
    if x > 570:
        xdir = -1
        ydir = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                xdir = -1
                ydir = 0
            if event.key == pygame.K_RIGHT:
                xdir = 1
                ydir = 0
            if event.key == pygame.K_UP:
                xdir = 0
                ydir = -1
            if event.key == pygame.K_DOWN:
                xdir = 0
                ydir = 1
pygame.quit()