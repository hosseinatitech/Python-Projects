# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 00:45:40 2026

@author: M&N
"""

"""

error handling

"""

try:
    prnt("hello")
    
except:
    print("error dashi")
    
    
print("--------------")



def divis(a, b):
    try:
        
        return a/b
    except:
        print("error in return")
        return None
print(divis(2, 5))

print(divis(3, 0))

print("-----------------")


def divis(a, b):
    try:
        
        return a/b
    except Exception as e:
        print(f"error in return , e = {e}")
        return None
print(divis(2, 5))

print(divis(3, 0))

print("----------------")



def divis(a, b):
    try:
        
        return a/b
    except ZeroDivisionError:
        print("can not zero/0")
        return None
    except Exception as e :
        print(f"error is : {e}")
        return None
        
print(divis(2, 5))

print(divis(3, 0))

print(divis("a", True))





print("----------------------")


while True:
    try:
        num1 = float(input("عدد اول را وارد کنید: "))
        num2 = float(input("عدد دوم را وارد کنید: "))

        result = num1 / num2

    except ValueError:
        print("خطا: لطفاً عدد معتبر وارد کنید.")

    except ZeroDivisionError:
        print("خطا: تقسیم بر صفر امکان‌پذیر نیست.")

    else:
        print("نتیجه تقسیم:", result)
        break

print("-------------------")


try:
    password = input("رمز عبور را وارد کنید: ")

    if len(password) < 8:
        raise ValueError("رمز عبور باید حداقل ۸ کاراکتر باشد")

except ValueError as error:
    print("خطا:", error)

















      
