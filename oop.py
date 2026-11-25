# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:21:01 2026

@author: M&N
"""

class classname():
    def __init__(self, param1):
        self.param1 = param1     #atteribvte
        print("obtect certaed")
    def say_hello(self):         #method
        print("hello")
        
a = classname(1)                 #self = a

a.say_hello()


print("-----------------")

class Book():
    def __init__(self , page):
        self.pages = page
        
mybook = Book(540)

print(mybook.pages)

print(type(mybook))

yourbook = Book(14)
print(yourbook.pages)



print("-------------")

class prson():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def moerfi(self):
        print("my name is ", self.name)
        print("i am is" , self.age , "old years")
        
person1 = prson("hossein", 28)

person2 = prson("ali", 30)

person1.moerfi()

person2.moerfi()



print("-----------------")

class car():
    def __init__(self , berand, coler):
        self.berand = berand
        self.coler = coler
car1 = car("bmw", "red")

car2 = car("benz", "belck")

print(car1.berand)
print(car2.berand)

print(car1.coler)

print("---------------")




class clculater():
    def __init__(self, number1 , number2):
        self.number1 = number1
        self.number2 = number2
    def add(self):
        print(self.number1 + self.number2)
        
    def zarb(self):
        print(self.number1 * self.number2)
a = int(input("num1"))
b = int(input("num2"))
clc = clculater(a, b)

clc.add()
clc.zarb()

print("----------------")

class circel():
    pi = 3.14
    def __init__(self, r):
        self.r = r
    def masahat(self):
        m = self.r * self.r * self.pi
        
        return m
c1 = circel(10)

print(c1.masahat())


print("-----------------")

# ارث بری


class newbook():
    def __init__(self , name, page):
        self.name = name
        self.page = page
        
    def open(self):
        
        print(f"opened  the {self.name} watch has {self.page} pages")
        
b1 = newbook("c progeram", 452)

b1.open()


class Darsi(newbook):
    def __init__(self, reashte, paye, name , page):
        newbook.__init__(self, name, page)
        self.reashte = reashte
        self.paye = paye
        print("a neew darsi book")
    def open(self):
        print( f"opened {self.name} to {self.reashte} paye{self.paye}")
d = Darsi("riazi", 12, "phisics", "50")

print(d.page)

d.open()



print("---------------")

#چند شکلی


class Runer():
    def __init__(self, name):
        self.name = name
        
    def action(self):
        print(f"{self.name} is runing")
        
class football():
    def __init__(self, name):
        self.name = name
        
    def action(self):
        print(f"{self.name} is football")
        
p1 = football("hossein")  
p1.action()

print(type(p1))

p2 = Runer("ALI")

p2.action()
print(type(p2))



for person3 in [p1 , p2]:
    person3.action()


               
        
        



    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        










        
        
        




























