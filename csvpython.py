# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:23:24 2026

@author: M&N
"""

import csv

my_file = open("C:/Users/mn/Desktop/students.csv")

csv_data = csv.reader(my_file)

for row in csv_data:
    print(row)
    
my_file.close()

print("----------------")



with open("C:/Users/mn/Desktop/students.csv", "a", newline="", encoding="utf-8")as my_file:
    writer = csv.writer(my_file)
    writer.writerow(["Reza", 21, 15])
    
    
with open("C:/Users/mn/Desktop/students.csv", "r", encoding="utf-8")as my_file:
    data = csv.DictReader(my_file)
    for row in data:
        print(row)
        
        
name = input("Name: ")
age = input("Age: ")
score = input("Score: ")

with open("students2.csv", "a", newline="", encoding="utf-8") as my_file:

    writer = csv.writer(my_file)

    writer.writerow([name, age, score])

print("Student saved successfully")


with open("C:/Users/mn/Desktop/eju python/students2.csv", "r", encoding="utf-8")as my_file:
    csv_data = csv.reader(my_file)
    for i in csv_data:
        print(i)

