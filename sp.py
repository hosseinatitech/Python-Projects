# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:00:06 2026

@author: M&N
"""

s = set()

s = {1, 2, 3}

print(s)

s2 = s
print(s2)


s.add(10)
print(s)
print(s2)

s2 = s.copy()
print(s2)
s.add(100)
print(s)
print(s2)

s.remove(10)
print(s)



print("--------------")


a = {1, 2, 3}

a2 = {3, 4, 5}

a.difference_update(a2)
print(a)

print(a.isdisjoint(a2))
















