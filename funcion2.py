# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 01:35:55 2026

@author: M&N
"""

def student(*scor1, **info):
    total1 = 0
    for scor in scor1:
        total1+=scor
    avg = total1/len(scor1)
    
    print("name:", info.get("name"))
    print("age:", info.get("age"))
    print("avg:", avg)


student(18, 15, 16, name= "ali" , age = 28 , )

print("---------------")

#Unpacking
namubers = [20, 30, 10, 40]

print(*namubers)


print("------------")

person = {
    "name": "Ali",
    "age": 20
}
def show(name , age):
    print(name)
    print(age)
    
show(**person)

print("----------")

# map
"""
map  : kardan bara in hast ke ye funcion ro roya ya list anjam daha
map(function, iterable)

"""
#یک تابع را روی تک‌تک اعضای iterable اجرا کن.
def tavan2(x):
    return x ** 2
my_lista = [2, 4, 8]

tavana = map(tavan2 , my_lista)

print(list(tavana))

print("---------------")

mylist2 = [2, 4, 5, 3, 1]

res = map(lambda x : x * 2, mylist2)

print(list(res))

print("--------------------")


a = [2, 4, 8]

tavana1 = map(lambda x : x ** 2, a)

print(list(tavana1))


print("---------------")

numbers = ["10", "20", "30", "40"]

result = map(int, numbers)

print(list(result))

print("----------------")

def add2(*args):
    total = 0

    for number in args:
        total += number

    return total


numbers = list(map(int, input("num: ").split()))

z = add2(*numbers)

print(z)

print("--------------")
#filter

"""
filter : bary in ke ya chizi ro filter konim

"""

mylist = [1, 2.2, 4, 5, 3.2, 8 , 9.1]
print(list(filter(lambda x : x  !=  int(x), mylist)))

print("------------")

list_number = [1, 2, 5, 4, 3, 7, 8]

res_even = filter(lambda x : x %2 == 0, list_number)

print(list(res_even))


print("----------------")

names = ["ali", "hossein", "hasan", "sara"]

short_name = filter(lambda s : len(s)<=4, names)

for name1 in short_name:
    print(name1)
    
print("----------------")

scores = [8, 12, 15, 7, 19, 20]

passed = filter(lambda x: x >= 10, scores)

print(list(passed))
    
"""
map : roy hame anasor tagheer ejad mikonad

filter : bar asas shart roy ansor tagheer  ejad mokonad

"""

print("-------------")


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)

sqr = map(lambda x : x**2, even_numbers)

print(list(sqr))

























