# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 00:54:19 2026

@author: M&N
"""

"""

funcion

"""

def hello():
    print("hello world")
    
hello()
hello()
hello()
hello()

print("----------------------")

def hello1(name):
    '''
    

    Parameters
    ----------
    name : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    for i in range(3):
        print(f"hello wellcom:{name}")
        
hello1("hossein")

'''
funcion : snake - case

avrag _ of _ sum

'''


def sey_hello_n_time(name, n):
    for i in range(n):
        print(f"hello wellcom : {name}")
        
sey_hello_n_time("hossein", 2)
sey_hello_n_time("ali", 1)


print("------------------------")


def sum_of_number(a, b):
    res = a+b
    print(res)

sum_of_number(4, 6)


print("--------------------")


def sum_of_number1(a, b):
    ret = a+b
    return ret

ans = sum_of_number1(4, 5)

print(ans)

print("---------------------")

def chandta_toosh_hast(s, c):
    counter = 0
    for this_chacter in s:
        if this_chacter == c:
            counter+=1
    return (counter)

name = "hossein"

show = chandta_toosh_hast(name, "s")

print(show)

print("--------------------")

def rectangle_area(length, width):
    return length * width

masahat = rectangle_area(10, 5)
print(masahat)


print("--------------------")

def takhfif_price(ghimat,takhfif):
    mohasebetkhfif = ghimat * takhfif / 100
    gimatnahaei = ghimat - mohasebetkhfif
    return gimatnahaei

mahsool = takhfif_price(10000, 20)

print(mahsool)





print("------------------")

def number_even(number):
    
    if number %2 == 0:
        return "enan"
    else:
        return "odd"
    
resalt = number_even(int(input("num")))

print(resalt)

print("----------------")


def avrag_sum(number1, number2, number3):
    res1 = number1+number2+number3/3
    return res1

num1 = int(input("adad1"))
num2 = int(input("adad2"))
num3 = int(input("adad3"))
avr = avrag_sum(num1, num2, num3)

print(avr)


print("-------------------")
    

def calculator(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        return a / b

    else:
        return "عملگر نامعتبر است"


num1 = float(input("عدد اول: "))
operator = input("عملگر را وارد کنید: ")
num2 = float(input("عدد دوم: "))

result = calculator(num1, num2, operator)

print("نتیجه:", result)


print("------------")

def average(numbers):

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


scores = [15, 18, 20, 17]

print(average(scores))


print("------------------")



""""
sisen2

"""

def print_n_time(name, n=1):
    for i in range(n):
        print(name)

print_n_time("hossein")        


print("---------")


def tavan(n, t=2):
    javab = 1
    for i in range(t):
        javab *=n
        return javab
    
print(tavan(2, 2))


print("-----------------")

def sum_of_tow(n1, n2=10):
    return n1+n2

print(sum_of_tow(10))

print("-------------")


def is_even(n):
    return n%2 == 0

def number_of_evans(nambers):
    count = 0
    for n in nambers:
        if is_even(n):
            count+=1
    return count

count = number_of_evans([1, 2, 3, 5, 6, 7, 4])

print(count)


print("--------------")

def any_even_in_list(numbrs1):
    for a in numbrs1:
        if is_even(a):
            return True
    return False


numbers = [1, 3]

print(any_even_in_list(numbers))


print("--------------")

def get_odd(nums):
    odd = []
    count = 0
    for num in nums:
        if not is_even(num):
            odd.append(num)
            count+=1
            
    return count, odd

my_num = [1, 2, 3, 4, 5, 6, 7]

count_odd,get_nums = get_odd(my_num)

print(count_odd,get_nums)

print("----------------")

def add(a, b):
    return a + b


def show_result():
    result = add(10, 20)
    print(result)


show_result()


print("-----------------")


def jam_zarb(n1, n2):
    jam = n1 + n2
    zarb = n1 * n2
    return jam, zarb

x, y = jam_zarb(4, 3)

print(x)

print(y)


print("--------------")

def total(numbers):

    result = 0

    for number in numbers:
        result += number

    return result


def average1(numbers):
    result = total(numbers)
    
    return result / len(numbers)

my_list = [1, 5, 14, 5, 6]

print(average(my_list))


print("-----------------")

def sum1(a, b):
    return a + b


def multiply(a, b):
    return a * b

def taghsim(a, b):
    return a / b


def calculate(a, b):

    sum_result = sum1(a, b)
    multiply_result = multiply(a, b)
    taghsim_result = taghsim(a, b)

    return sum_result, multiply_result, taghsim_result


print(calculate(5, 3))

print("------------------")


"""
sisen 3
**args
**kwargs
map
lambda
filter


"""

# args // kwargs

""" 
args return : tuple
va har che argomans bekhahim be def midim.
"""
def add1(*args):
    print(f"args is {args}")
    total = 0

    for number in args:
        total += number

    return total


print(add1(10, 20))
print(add1(10, 20, 30))
print(add1(10, 20, 30, 40))



print("----------------")


def zarb(*args):
    print(f"args is :{args}")
    result = 1
    for i in args:
        result*=i
    return result

b = zarb(2, 3, 4, 5)

print(b)

print("--------------------")

"""
kwargs return " dict
va baray in ke func ro ba har paramtri mitavan seda bazenim

"""

def person(**kwargs):

    for key, value in kwargs.items():
        print(key, value)


person(
    name="Hossein",
    age=25,
    city="Baku"
)

print("-------------")



def calculeter_masahat(**kwargs):
    print(f"kwargs is :{kwargs}")
    if "tool" in kwargs:
        return kwargs["tool"] * kwargs["ertfa"]
    if "shoa" in kwargs:
        return kwargs["shoa"] * 3.14 * kwargs["shoa"]
    return 404

print(calculeter_masahat(tool = 5 , ertfa = 4))

print(calculeter_masahat(shoa = 4))

print("-------------")

def test(*args, **kwargs):
    print(args)
    print(kwargs)
    
test(10, 20, 30, name="hossein", age = 28, city = "ker")
    

print("-------------")

# lambda
# nashanas
""" 
lambda : funcion nashanas hast bdon in ke asmi baray func bzari az
 func astefade mikonum
 lambda parameter: expression
"""

tavan2 = lambda x : x**2
print(tavan2(5))

print("------------")

jam = lambda a, b :a + b
print(jam(2,3))

print("-----------")

even = lambda x: x % 2 == 0

print(even(10))

print("------------")



# map
"""
map  : kardan bara in hast ke ye funcion ro roya ya list anjam daha
map(function, iterable)

"""
#یک تابع را روی تک‌تک اعضای iterable اجرا کن.
def tavan2(x):
    return x ** 2
my_lista = [2, 4, 8]

tavana = map(tavan2 , my_lista)

print(list(tavana))

print("---------------")

mylist2 = [2, 4, 5, 3, 1]

res = map(lambda x : x * 2, mylist2)

print(list(res))

print("--------------------")


a = [2, 4, 8]

tavana1 = map(lambda x : x ** 2, a)

print(list(tavana1))


print("---------------")

numbers = ["10", "20", "30", "40"]

result = map(int, numbers)

print(list(result))

print("----------------")

def add2(*args):
    total = 0

    for number in args:
        total += number

    return total


numbers = list(map(int, input("num: ").split()))

z = add2(*numbers)

print(z)

print("--------------")
#filter

"""
filter : bary in ke ya chizi ro filter konim

"""

mylist = [1, 2.2, 4, 5, 3.2, 8 , 9.1]
print(list(filter(lambda x : x  !=  int(x), mylist)))

print("------------")

list_number = [1, 2, 5, 4, 3, 7, 8]

res_even = filter(lambda x : x %2 == 0, list_number)

print(list(res_even))


print("----------------")

names = ["ali", "hossein", "hasan", "sara"]

short_name = filter(lambda s : len(s)<=4, names)

for name1 in short_name:
    print(name1)
    
print("----------------")

scores = [8, 12, 15, 7, 19, 20]

passed = filter(lambda x: x >= 10, scores)

print(list(passed))
    
"""
map : roy hame anasor tagheer ejad mikonad

filter : bar asas shart roy ansor tagheer  ejad mokonad

"""

print("-------------")

def add2(*args):
    total = 0

    for number in args:
        total += number

    return total


numbers = list(map(int, input("num: ").split()))

z = add2(*numbers)

print(z)

print("----------------")

def person(**kwargs):

    print(kwargs["name"])
    
person(name = "hossein", age = 28)

print("-------------")


def student(*scor1, **info):
    total1 = 0
    for scor in scor1:
        total1+=scor
    avg = total1/len(scor1)
    
    print("name:", info.get("name"))
    print("age:", info.get("age"))
    print("avg:", avg)


student(18, 15, 16, name= "ali" , age = 28 , )

print("---------------")

#Unpacking
namubers = [20, 30, 10, 40]

print(*namubers)


print("------------")

person = {
    "name": "Ali",
    "age": 20
}
def show(name , age):
    print(name)
    print(age)
    
show(**person)

print("----------")

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)

sqr = map(lambda x : x**2, even_numbers)

print(list(sqr))



