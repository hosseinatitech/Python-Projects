# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:10:30 2026

@author: M&N
"""


import json

d = {"name":"hossein", "sen":28, "fun":"footbal", "sco":30}

print(type(d))


mj = json.dumps(d)

print(mj)

new_data = json.loads(mj)
print(new_data)

print(new_data["sen"])

import requests

url = "https://dummyjson.com/users"

respons = requests.get(url)
print(respons)

print(respons.text)

print("----------------")

data = respons.json()
print(data)

print("---------------------")

user = data["users"]



for user in data["users"]:
    print(user["firstName"])









