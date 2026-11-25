# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 01:09:42 2026

@author: M&N
"""

age = 30

if age < 18:
    print("salam bache")
if age >= 30:
    print("salam moosen")
    
print("-------------------")

sen = 160
if sen < 18:
    print("salam bache")
elif sen < 40:
    print("salam miansal")
elif sen < 90:
    print("salm mossen")
elif sen < 150:
    print("wow")
else:
    print("bikhial")
    
    
print("-------------------")

action = "gool"

socer = 0

if action == "shoot":
    print("oh shoot kard")
elif action == "pass":
    print("pass dad be dostesh")
elif action == "gool":
    print("goooooool")
    socer+=1
else:
    print("chekardi")
    
if socer > 0:
    print(f"win {socer}")
    
else:
    print("bazi badi bood")
    
print("----------")
"""
number = int(input("enter your number"))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


print("----------")

age = int(input("Enter your age: "))

if age >= 18:
    print("You can enter")
else:
    print("You cannot enter")
"""
print("------------")

score = 17

if score >= 18:
    print("Excellent")

elif score >= 15:
    print("Very Good")

elif score >= 10:
    print("Passed")

else:
    print("Failed")
    
print("----------")

# python az bala be paeein mikhanad
score = 19

if score >= 10:
    print("Passed")

elif score >= 18:
    print("Excellent")
    
    
print("---------------")

age = 25

if age < 5:
    print("Child")

elif age < 13:
    print("Kid")

elif age < 18:
    print("Teenager")

elif age < 30:
    print("Young")

else:
    print("Adult")

print("-------------------")

"""
for

"""
for i in range(5):
    print("Hello")
print("---------------")
    
for i in range(1, 11):
    print(i)
print("---------------")

for i in range(0, 10, 2):
    print(i)
    
print("---------------")

for i in range(1, 10, 2):
    print(i)
print("---------------")


for i in range(2, 10, 2):
    print(i)
print("-----------------")

for i in range(10, 0, -1):
    print(i)

print("-------------")
name = "Hossein"

for i in name:
    print(i)
    
print("------------")

text = "banana"

count = 0

for char in text:
    if char == "a":
        count += 1

print(count)

print("-------------")

cont = 0
names = ["Ali", "Sara", "Reza", "Ali"]

for name in names:
    if name == "Ali":
        
        cont = cont+1
    print(name)
print(cont)

print("--------------")
count = 0
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
for a in my_list:
    if a %2 == 0:
        print(a)
        count = count+1
    else:
        print(f"{a} is odd")
print(f" we had  {count} even numbers")

print("----------------")


"""
unpackig
"""


person = ("Ali", 20, "Tehran")

name, age, city = person

print(name)
print(age)
print(city)

print("-----------")
numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)

print("------------")

my_tupel = (1, 2, 8, "hossein")
for i in my_tupel:
    print(i)
    
print("-----------")



people = (("hosssein", 28) , ("ali",30), ("sara",18))
for name,sen in people:
    print(f"{name} is {sen} old")

print("-----------")

peole1 = {"hossein" : (28, 185),
          "ali": (30, 189),
          "sara" : (45, 17500)
    
    }

for person in peole1:
    print(person ,peole1[person][0])
    
print("-----------")
  
perso2 = {
    "name": "Ali",
    "age": 20,
    "city": "Tehran"
}

for key, value in perso2.items():
    print(key, value)
    
print("----------")

"""
while True:
    print("hello world")
"""
a = 0
while a <= 5:
    print(f"a is {a}")
    a+=1
    
print("----------")

f = 12
while f <= 100:
    f+=1

print(f"fuell is {f}")

print("--------------")

#for a in [1, 2, 3, 4, 5, 6]:
#    pass


for a in [1, 2, 3, 4, 5, 6]:
    if a == 3:
        break
    print(a)
    
print("-------------")
    
names = ["Ali", "Sara", "Reza", "Hossein", "Maryam"]

for name in names:

    if name == "Hossein":
        print("Hossein found")
        break
    
print("---------------")

for b in [1, 2, 3, 4, 5, 6]:
    if b == 3:
        continue
    print(b)
    
print("----------")

l = [2, 4, 6, 8]

nl = []

for a in l:
    nl.append(a*2)
print(nl)

print("----------")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = []

for number in numbers:

    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

print("-----------")

#List Comprehension
my_list1 = [1, 3, 5, 7]

n_list = [x *2 for x in my_list1]

print(n_list)


print("---------")

ml = [2, 3, 4, 5, 6, 8]

ml2 = [n for n in ml if n%2 == 0]
ml3 = ["zoj" if m %2 == 0 else "fard"  for m in ml]
print(ml2) 
print(ml3)   

print("-------------")

"""

operetor useing

"""

for i in range(6):
    for j in range(6):
        print(i, j, i*j)
        
print("----------")

for a in range(6):
    for b in range(6):
        print(a*b, end="\t")
    print()

print("----------")

for i in range(2, 16, 2):
    print(i, end=" ")
    
    
print("----------")

for x in range(10, 1, -1):
    print(x, end=" ")


print("-----------------")

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)



print("---------------")


s = "hossein"

for i in range(len(s)):
    print(i, s[i])
    
    
    
print("----------------")


l = ["hossein", 5, "ali"]

for i in range(len(l)):
    print(i, l[i])
    
print("------------")

names = ["Ali", "Sara", "Reza"]

for index, name in enumerate(names):
    print(index, name)
    
print("-------------")
    

students = ["Ali", "Sara", "Reza", "Hossein"]

for number, student in enumerate(students, start=1):
    print(number, "-", student)
    

print("--------------------")

m = ["ali", 5, "hosein"]

for c , k in enumerate(m):
    print(c , k)

print("-------------")

name1 = ["hossein", "ali", "hasan"]

famili = ["aiz", "haydari", "par"]

age = [28, 15, 18]

for d in zip(name1, famili, age):
    print(d)
    
    
print("----------------")


names = ["Ali", "Sara", "Reza"]

scores = [18, 20]
for names, scores in zip(names, scores):
    print(names, scores)
    
print("------------")

name2 = ["ali", "hossein", "hasan"]

age2 = [35, 28, 18]

student1 = dict(zip(name2, age2))

print(student1)


print("---------------")

g  = "abcd"

if "j" in g:
    print("bood")
else:
    print("nabood")

print("------------")

print(max(1, 2, 3, 4, 5, 6, 7, 8, 9))

print(min(1, 2, 3, 4, 5, 6, 7, 8, 9))

print("--------------")

from random import randint

print(randint(1, 10))


print("-----------")



for i in range(5):
    number = randint(1, 100)
    print(number)



print("-----------------")

import random

names = ["Ali", "Sara", "Reza", "Hossein"]

name = random.choice(names)

print(name)

print("----------------")

javab = randint(1, 6)

i = input("chee bood")

i = int(i)

if i == javab:
    print("woow")
    
else:
    print(f"javab in bood{javab}")



print("-------------")

ans = randint(1, 100)

while True:
    
    gusse = int(input("adad ro hads bezan"))

    if gusse == ans:
        print("wooooooow")
        break
    elif gusse < ans:
        print("balatar")
    
    else:
        print("peaintar")

    










    