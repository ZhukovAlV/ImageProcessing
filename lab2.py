# подключение стандартной библиотеки:
from random import random, randint
# подключение кода из библиотеки Pillow:
from PIL import Image, ImageDraw, ImageFont
# подключение кода из расширения библиотеки Pillow:
from PIL.JpegImagePlugin import JpegImageFile
from pylab import *
import cv2
import numpy as np

mode = int(input('mode:'))  # Считываем номер преобразования.
image = Image.open("example.jpg")  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pixels = image.load()  # Выгружаем значения пикселей.

if (mode == 0): # Оттенки серого
    for i in range(width):
        for j in range(height):
            a = pixels[i, j][0]
            b = pixels[i, j][1]
            c = pixels[i, j][2]
            S = (a + b + c) // 3
            draw.point((i, j), (S, S, S))
if (mode == 1): # Сепия
    depth = int(input('depth:'))
    for i in range(width):
        for j in range(height):
            a = pixels[i, j][0]
            b = pixels[i, j][1]
            c = pixels[i, j][2]
            S = (a + b + c) // 3
            a = S + depth * 2
            b = S + depth
            c = S
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
if (mode == 2): # Негатив
    for i in range(width):
        for j in range(height):
            a = pixels[i, j][0]
            b = pixels[i, j][1]
            c = pixels[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))
if (mode == 3): # Добавление шумов
    factor = int(input('factor:'))
    for i in range(width):
        for j in range(height):
            rand = randint(-factor, factor)
            a = pixels[i, j][0] + rand
            b = pixels[i, j][1] + rand
            c = pixels[i, j][2] + rand
            if a < 0:
                a = 0
            if b < 0:
                b = 0
            if c < 0:
                c = 0
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))
if (mode == 4):
     factor = int(input('factor:'))
     for i in range(width):
         for j in range(height):
             a = pixels[i, j][0] + factor
             b = pixels[i, j][1] + factor
             c = pixels[i, j][2] + factor
             if a < 0:
                 a = 0
             if b < 0:
                 b = 0
             if c < 0:
                 c = 0
             if a > 255:
                 a = 255
             if b > 255:
                 b = 255
             if c > 255:
                 c = 255
             draw.point((i, j), (a, b, c))
if (mode == 5):
    factor = int(input('factor:'))
    for i in range(width):
        for j in range(height):
            a = pixels[i, j][0]
            b = pixels[i, j][1]
            c = pixels[i, j][2]
            S = a + b + c
            if S > (((255 + factor) // 2) * 3):
                            a, b, c = 255, 255, 255
            else:
                            a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
if (mode == 6):
    image = cv2.imread('example.jpg')
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv2.filter2D(image, -1, kernel)
    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image.show()
