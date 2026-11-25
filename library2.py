# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 06:46:10 2026

@author: M&N
"""
import random

print(round(3.1))

a = random.randint(1, 10)

print(a)



import math

print(math.inf>999999999991)

print(math.log(5,4))


print(math.pow(5, 5))

print(math.degrees(3.14/3))

"""

regx

"""
import re

p = "hossein has a phone. its number +933367"

print(re.search("hossein", p))

r = re.search("hossein", p)

print(r.end())

print(r.start())

"""
\d----digit
\w----word
"""

data= "+933367 1234-5678-9877-1234\ali"

print(re.findall(r"\+\d+", data))

print(re.findall(r"\d{4}-\d{4}-\d{4}-\d{4}", data))


print("---------------")


import requests

import bs4

r = requests.get("https://www.varzesh3.com/livescore")

print(r)

data1 = r.text

soup = bs4.BeautifulStoneSoup(data1)

print(soup)

m = soup.select("title")

print(m[0])

print(type(m))


mytitle = m[0]



print(mytitle.get_text())

m = soup.select("li")

print(m)



















