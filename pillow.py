# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:08:56 2026

@author: M&N
"""

from PIL import Image

img = Image.open("C:/Users/mn/Desktop/testi/shakhsi.jpg")
print(img.size)
#img.show()


print(img.info)

print(type(img))

print(img.filename)

print(img.format)

print(img.mode)

fixe = img.rotate(-90)

fixe.show()

print(fixe.size)

fixe.crop((500,0 , 1000, 200)).show()

fixe.save("C:/Users/mn/Desktop/testi/shakhsi2.png")


