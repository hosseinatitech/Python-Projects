# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:22:45 2026

@author: M&N
"""

nomre = {"riazi":18,
         "adabiat":20, 
         "progeram":20}

print(nomre["riazi"],nomre["adabiat"])

print(nomre)

print(type(nomre))

print("==============================")

nomre2 = {"hossein":
          {"riazi":18,
           "adabiat":20, 
           "progeram":20},
          "ali":
              {"riazi":15,
               "adabiat":20, 
               "progeram":18}
              }

print(nomre2["hossein"]["riazi"])

print(nomre2.keys())
print(nomre2.values())

print("==============================")

my_dic = {1 : "hossein", 2 : "ali"}

print(my_dic[1])


my_dic1 ={"hossein":1, "ali": 2}

print(my_dic1["hossein"],my_dic1["ali"])

print(my_dic1.values())

print(my_dic1.keys())

print(my_dic1.items())

print("==============================")


adad = {"list":[1, 2, 3, 4], "list2":[5, 6, 7, 8]}

print(adad["list"][2])

print("==============================")


my_list = {1 : ["hossein", "ali"], 2 : ["hasan","sara"]}

print(my_list[1][1].upper())


print("==============================")


student = {
    "name":"Ali",
    "age":20
}

print(student["name"])

print(student["age"])

#change motagir

student["age"] = 25

print(student["age"])

print("==============================")

#add kardan

student["city"] = "kerman"

print(student["city"])

student.pop("age")

print(student)

print("==============================")



del student["city"]
print(student)


print("==============================")

#student.clear()
#print(student)

print("==============================")

print(len(student))

print(str(student))

print("==============================")


a = {"ali":1, "hossein":2}

b = str(a)

print(b)

print(type(b))


print("==============================")

name = input("نام: ")
age = int(input("سن: "))
city = input("شهر: ")

student = {
    "name": name,
    "age": age,
    "city": city
}

print(student)

print("==============================")


my_dic = {"hossein":2, 
          "ali": 3,
          "hasan":4
    }

my_dic1 = my_dic.copy()

print(my_dic1)

print("hi")


