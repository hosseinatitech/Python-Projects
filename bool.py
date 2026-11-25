# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 00:32:03 2026

@author: M&N
"""

"""
bool
"""

a1 = "True"

print(type(a1))

a =True

print(type(a))


print(2 > 1)


print("---------------------------")

age = 30

print(age > 25)

print(age == 30) # condeion / shart

print(age == 35)

print("----------------")


age = 20

print(age >= 18)

age = 15

print(age <= 18)

print("----------------")

# bool in str

name = "Ali"

print(name == "Ali")

print("Ali" == "ali")

print(bool(""))

print(bool("Python"))


print("----------------")

# bool in list 

print(bool([]))

print(bool([1, 2, 3]))


print("----------------")

# bool in adadd

print(bool(100))
print(bool(-5))
print(bool(0))

print("----------------")

# bool in dic

print(bool({}))

print(bool({"name": "Ali"}))


print("----------------")


s = "10"

print(s.isdigit())

s2 = "1.12"

print(s2.isdigit())


print("---------------")

mylist = [1, 2, "hosseun"]

print(1 in mylist)

print("---------------")


mydic  = {"car" : 2,
          "mootor" : 1, 
          "bic" : 0
    }
print("Car" in mydic)

print("bic" in mydic)

print("---------------")

# and  
#هر دو شرط باید True باشند تا نتیجه True شود.

age = 20
has_card = True

print(age >= 18 and has_card == True)

print("---------------")

# or

# اگر حداقل یکی از شرط‌ها True باشد، نتیجه True می‌شود.

age = 16
has_permission = True

print(age >= 18 or has_permission == True)

print("---------------")

# not
# not نتیجه Boolean را برعکس می‌کند

print(not True)

is_student = True

print(not is_student)

print("---------------")

age = int(input("Enter your age: "))

print(age >= 18)

print("---------------")

number = int(input("enter"))

print(number % 2 == 0)

print("---------------")

number = 15

print(number >= 10 and number <= 20)


print("---------------")


number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

print(number1 > 0 and number2 > 0)




