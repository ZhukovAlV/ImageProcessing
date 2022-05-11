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

if (mode == 0): # Выбираем 3 точки
    im = array(Image.open("example.jpg"))
    imshow(im)
    print('Click 3 times')
    x = ginput(3)
    print('You choosed:', x)
    show()
if (mode == 1): # Выбор объекта из фона
    img = cv2.imread('camera.jpg')
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    rect = (50, 50, 650, 550)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 10, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]
    # while True:
    cv2.imshow('Test', img)
    cv2.waitKey(0)
if (mode == 2): # Выбор объекта по цвету
    img = cv2.imread('camera.jpg')
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_pt = hsv_img[223, 143]
    hsv_min = (hsv_pt * 0.95).astype('uint8')
    hsv_max = (hsv_pt * 1.05).astype('uint8')
    result = cv2.inRange(hsv_img, hsv_min, hsv_max)
    # while True:
    cv2.imshow('Test', result)
    cv2.waitKey(0)
if (mode == 3): # Обнаружение глаз и рта
    img = cv2.imread("camera.jpg")
    cv2.imshow('img', img)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        smile = smile_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in smile:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('Test', img)
    cv2.waitKey(0)
    cv2.imwrite('output.jpg', img)
if (mode == 4): # Оттенки цвета, выбранного пользователем на изображении
    im = array(Image.open('camera.jpg'))
    imshow(im)
    print('Click 1 times')
    coords = ginput(1)[0]

    img = cv2.imread('camera.jpg')
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_pt = hsv_img[int(coords[1]), int(coords[0])]
    hsv_min = (hsv_pt * 0.9).astype('uint8')
    hsv_max = (hsv_pt * 1.1).astype('uint8')
    result = cv2.inRange(hsv_img, hsv_min, hsv_max)
    cv2.imshow('Test', result)
    cv2.waitKey(0)


