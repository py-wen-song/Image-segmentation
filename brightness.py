import cv2 as cv
import numpy as np
import copy
import random
from PIL import ImageStat
#仅供测试，代码有误
#For testing only, code is wrong

img = cv.imread('1.png')
cv.imshow('img', img)
rows, cols, channel = img.shapedst
a = 1.3
b = 3
for i in range(rows):
    for j in range(cols):
        for c in range(3):
            color =float.img[i, j][c] * a + b
            if color > 255:
                img[i, j][c] = 255
            elif color < 0:
                img[i, j][c] = 0
cv.imshow('dst', img)
