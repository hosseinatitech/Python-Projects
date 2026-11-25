# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 02:25:08 2026

@author: M&N
"""

file = open("test.text", "w")

file.write("hello hossein")
file.write("\n hi ali")

file.close()
print("--------------------")
file = open("test.text", "r")

file1 = file.read()
print(file1)
file.close()
print("--------------------")

file = open("test.text" , "a")
file.write("\nhi python\nhello world")
file.close()

print("--------------------")

file= open("test.text", "r")
file2 = file.read()
print(file2)
file.close()

print("--------------------")

file = open("test1.tex" , "w")
file.write("hi ahmad")
file.close()

file = open("test1.tex", "r")

a = file.read()
print(a)
file.close()

print("--------------------")


with open("test9.text", "w") as file9:
    file9.write("hello hasan")
    
with open("test9.text", "r") as file9:
    data = file9.read()
    print(data)


with open("test.text", "r") as file:
    line = file.readlines()
    print(line)
    
    
print("--------------------")
  

#ذخیره چند اطلاعات
name = input("Enter your name: ")
last = input("enter your last")
with open("users.txt", "w") as file:
    file.write(name)
    file.write(last)
    
print("--------------------")

#ذخیره چند اطلاعات
name = input("Enter your name: ")
age = input("Enter your age: ")

with open("user.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age)
    
print("--------------------")

#اضافه کردن چند کاربر
name = input("Enter your name: ")

with open("users.txt", "a") as file:
    file.write(name + "\n")
    








