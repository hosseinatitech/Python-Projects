# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:58:42 2026

@author: M&N
"""

fruit_prices = {
                "appel":1500,
                "banana":1000,
                "orang":1200
    }

fruit_prices["banana"]= 1100
del fruit_prices["appel"]

fruit_prices["anar"] = 1600

print(fruit_prices)
print(fruit_prices.keys())

print(fruit_prices.values())

print(fruit_prices.get("banana"))



print("============================")
"""
name = input("نام: ")
age = int(input("سن: "))
city = input("شهر: ")

student = {
    "name": name,
    "age": age,
    "city": city
}

print(student)
"""
print("============================")

car = {
    "brand": "BMW",
    "model": "X5",
    "color": "Black"
}


print(car["color"])

print("============================")

student = {
    "name": "Sara",
    "age": 18
}

student["age"] = 20
print(student)



print("============================")

person = {
    "name": "Hossein",
    "age": 22
}
person["phone"] = "09123456789"

print(person)


print("============================")

person1 = {
    "name": "Ali",
    "age": 20,
    "city": "Tabriz"
}

del person1["city"]

print(person1)  

print("============================")


book = {
    "title": "Python",
    "author": "Ali",
    "pages": 350
}
print(len(book))

print("============================")

student2 = {
    "name": "Ali",
    "age": 20
}
print("age" in student2)


print("============================")

student4 = {
    "name": "Ali",
    "age": 20,
    "city": "Tehran"
}
print(student4.keys())

print(student4.values())

print("============================")


student5 = {
    "name": "Ali",
    "age": 20
}
print(student5)







