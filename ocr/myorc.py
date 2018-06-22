#########################################################################
# File Name: myorc.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: Fri 22 Jun 2018 04:54:54 PM CST
#########################################################################
#!/usr/bin/python
#!Coding:utf-8
import pytesseract
from PIL import Image

# open image
image1 = Image.open('7364.png')
code1 = pytesseract.image_to_string(image1,lang="chi_sim")
image2 = Image.open('test.png')
code2 = pytesseract.image_to_string(image2,lang="chi_sim")
print(code1,code2)
