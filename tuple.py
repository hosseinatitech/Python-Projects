# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 00:30:08 2026

@author: M&N
"""

"""
tuple

"""
name = ("ali", "hossein", "reza", 1, 2)

print(name)

print(type(name))

my_list = list(name)

print(my_list)

city = ("kerman",
        "tehran",
        "esf",
        "kermanshah"
        )

print(city)
print(city[0])
print(city[3])
print(len(city))
print("tehran" in city)
my_list1 = list(city)
print(my_list1)

print(len(city))


print("-----------------")

numbers = [10, 20, 30]

my_tuple = tuple(numbers)

print(my_tuple)


print("------------------")

my_tuple = (10, 20, 30)

my_list = list(my_tuple)

print(my_list)

print("--------------")


my_tuple = (10)

print(type(my_tuple))

my_tuple1 = (10,)

print(type(my_tuple1))




person = ("Hossein", 28, "Kerman")

name, age, city = person

print(name)
print(age)
print(city)



scores = (18, 16, 20, 14, 17)

total = sum(scores)
average = total / len(scores)

print("Total:", total)
print("Average:", average)






numbers = (15, 8, 25, 12, 30, 5)

maximum = max(numbers)
minimum = min(numbers)

print("Maximum:", maximum)
print("Minimum:", minimum)

# chang vulues


new_tuple = ("ali", "mohammad", "hossein")


new_list = list(new_tuple)


print(new_list) 

new_list.append("sara")

new_tuple2 = tuple(new_list)

print(new_tuple2)

print("-----------")


nlist = [1, 2, 5, 6]

nlist[0] = 7

print(nlist)



ntuple = (1, 2, 5, 6)

ntuple[0] = 7
print(ntuple)








