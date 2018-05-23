#/usr/bin/env python
#coding:utf-8
import cv2 as cv
import matplotlib.pyplot as plt


#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv.imread("timg.jpg")
#创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
#释放窗口
cv.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100])
plt.show()