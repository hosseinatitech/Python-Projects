# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:50:53 2026

@author: M&N
"""
# string to list
name = "hossein, ali, sara"

name2 = name.split(",")
print(name2) 

text = "Ali,Reza,Sara"

names = text.split(",")

print(names)

print('/n==========================')


text = "hossein, aziz, ali"

text2 = list(text.split(","))

print(text2)

print('/n==========================')


a = [1, 2, 3, 4]

print(a)


my_list = ["hossein", 2, 3, 4]

result = str(my_list)

print(result)


print('/n==========================')

# list to string

my_list3 = ["Ali", "Sara", "Reza"]

result = ",".join(my_list3)

print(result)


print('/n==========================')

# string to list
my_list = (input("enter your list"))

my_list2 = list(my_list.split(","))

print(my_list2)

print(len(my_list2))

print('/n==========================')


my_list = (input("enter"))

print(len(my_list))

my_list2 = list(my_list.split(","))

print(len(my_list2))


print('/n==========================')

"""
my_list =list((input("enter")))

print(len(my_list))

my_list2 = list(my_list.split(","))

print(len(my_list2))


"""


names = ["Ali","Sara"]

names.append("Reza")

print(names)

names.insert(1,"Hossein")

print(names)


print('/n==========================')


list1 = [1,2,3]

list2 = [3,4]

list1.extend(list2)

print(list1)

print('/n==========================')

numbers=[2,5,9]

print(max(numbers))


print(min(numbers))

print(sum(numbers))


print('/n==========================')


numbers1=[1,2,2,2,5]

print(numbers1.count(2))


print('/n==========================')


names=["Ali","Sara","Reza"]

print(names.index("Sara"))

print('/n==========================')


words=["I","Love","Python"]

print(" ".join(words))


print('/n==========================')

a3 = [1,2,3]

a3.remove(1)
print(a3)
a3.clear()
print(a3)

print('/n==========================')

a4 = ["hossein", "ali", "hasan","ali"]

print(a4.count("ali"))

print(a4.index("ali"))

first = a4.index("ali")
second = a4.index("ali", first + 1)

print(second)
print('/n==========================')


numbers = [10, 20, 30, 40]

numbers.pop(2)      # حذف عنصر با اندیس 2 (عدد 30)

numbers.remove(20)  # حذف مقدار 20

print(numbers)

print('/n==========================')

my_list = [1, 2, 3]
my_list2 = my_list.copy()
print(my_list2)





"""
| تابع      | کاربرد                 |
| --------- | ---------------------- |
| append()  | اضافه کردن انتهای لیست |
| insert()  | درج در محل دلخواه      |
| extend()  | ترکیب دو لیست          |
| remove()  | حذف بر اساس مقدار      |
| pop()     | حذف بر اساس اندیس      |
| clear()   | حذف همه اعضا           |
| copy()    | کپی لیست               |
| sort()    | مرتب‌سازی              |
| reverse() | برعکس کردن             |
| count()   | شمارش                  |
| index()   | پیدا کردن اندیس        |
"""

