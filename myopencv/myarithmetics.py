#/usr/bin/env python
#coding:utf-8
import cv2
import numpy as np

img1 = cv2.imread('3d-image.png')
img2 = cv2.imread('line.png')

print(img1.__sizeof__())
print(img2.__sizeof__())
add = img1 + img2

#add = cv2.add(img1, img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()