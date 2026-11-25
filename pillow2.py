# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:48:24 2026

@author: M&N
"""

from PIL import Image

img = Image.open("C:/Users/mn/Desktop/img/atitech.png")
print(img.size)

#img.show()

print(img.info)

print(img.format)
print(img.filename)

print(img.mode)

fix = img.rotate(-90)

#fix.show()

fix1 = img.convert("L").convert("1")

fix1.show()

from PIL import Image

img = Image.open("C:/Users/mn/Desktop/img/atitech.png")

colors = img.getcolors(maxcolors=1000000)

if colors:
    print("تعداد رنگ‌های متفاوت:", len(colors))
else:
    print("تعداد رنگ‌ها بیشتر از حد تعیین‌شده است")