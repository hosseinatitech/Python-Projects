# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:10:40 2026

@author: M&N
"""
import json 

student = {
    "name": "Hossein",
    "age": 28
}

# تبدیل دیکشنری به رشته JSON
data = json.dumps(student)

print(data)
# تبدیل رشته JSON به دیکشنری
new_data = json.loads(data)
print(new_data)

print(type(data))
print(type(new_data))






import json

d = {"name":"hossein", "sen":28, "fun":"footbal", "sco":30}

print(type(d))


mj = json.dumps(d)

print(mj)
print(type(mj))



import json

product = {
    "title": "Laptop",
    "price": 500,
    "available": True
}

data = json.dumps(product)

print(data)


d1 = json.loads(data)

print(d1["title"])






