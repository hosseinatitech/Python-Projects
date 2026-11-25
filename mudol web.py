# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 09:35:52 2026

@author: M&N
"""
"""
mudol web
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
print("---------------------")

data = respons.json()
print(data)


print("-----------")



user = data["users"]

for user in data["users"]:
    print(user["firstName"])
    
    
    
import requests

url = "https://dummyjson.com/users"

response = requests.get(url)

data = response.json()

for user in data["users"]:
    print("نام:", user["firstName"])
    print("نام خانوادگی:", user["lastName"])
    print("سن:", user["age"])
    print("ایمیل:", user["email"])
    print("--------------------")


print("---------------------")

import requests

import json

url = "http://api.open-notify.org/astros.json"

respon = requests.get(url)

print(respon)



json_data = respon.json()

print(json_data)


print(json_data["number"])

print(json_data["people"])

for this_prson in json_data["people"]:
    print(this_prson["name"], this_prson["craft"])























