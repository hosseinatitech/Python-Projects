# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 10:37:20 2026

@author: M&N
"""

import csv
"""
my_file = open("C:/Users/mn/Downloads/testcsv.csv")
csv_data = csv.reader(my_file)
for line in csv_data:
    print(line)
    
my_file.close()

my_file = open("C:/Users/mn/Downloads/testcsv.csv")

csv_data = csv.reader(my_file)

line =list(csv_data)
print(line[1])


for this_line in line :
    print(this_line[1])

my_file = open("C:/Users/mn/Downloads/testcsv.csv")

csv_data = csv.DictReader(my_file)

line = list(csv_data)

print(line) 

print(line[1]) 



out_file = open("my_csv.csv", mode="w", newline="")
csv_writer = csv.writer(out_file, delimiter= "\t")
csv_writer.writerow([1, 2, 3])
csv_writer.writerow(["hossein", "ali", "sara"])
out_file.close()

"""

import openpyxl

wb = openpyxl.load_workbook("C:/Users/mn/Desktop/tes1.xlsx")

print(type(wb))

ws = wb.active

print(ws)


print(ws["B4"].value)

this_cell = ws["B4"]
print(this_cell.value)

print(this_cell.fill)


new_wb = openpyxl.Workbook()
ws = new_wb.active
ws["A1"] = "HOSSEIN"

print(ws["A1"].value)

import datetime

ws["A2"] = datetime.datetime.now()


new_wb.save("C:/Users/mn/Desktop/t2.xlsx")

new_wb.close()









