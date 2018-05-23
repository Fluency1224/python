#/usr/bin/env python
#coding:utf-8
#import numpy as np
import cv2

img = cv2.imread('timg.jpg',cv2.IMREAD_COLOR)

print(img[55,55])
img[55,55] = [255,255,255]
print(img[55,55])

roi = img[100:150,100:150]
print(roi)
img[100:150,100:150] = [255,255,255]

watch_face = img[37:111,133:199]
img[0:74, 0:66] = watch_face
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()