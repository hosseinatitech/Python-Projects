# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 09:40:18 2026

@author: M&N
"""

'''set'''

f = {'apple' , 'orange' , 'banana'}
print(type(f))
print(len(f))
print(f)
for i in f:
    print(i)

f1 = set(('apple' , 'orange' , 'banana'))
print(f1==f)
print('cherry 'in f)
f.add('cherry')
print(f)

f.update(['mango','grapes'])
print(f)

f.remove('apple')
print(f)

print('\n===================')

vowels = {'a', 'e', 'o', 'i', 'u'}
print(vowels)
#vowels.remove('k')
vowels.discard('h')
x = vowels.pop()
print(x)                     # u
print(vowels)                # {'i', 'o', 'e', 'a'}

c = vowels.copy()
print(c)
vowels.clear()
print(vowels)
print(len(vowels))
del c


print('\n===================')
a = {1, 2 , 3 , 4 , 5}
b = {2, 4 ,7}
print(a-b)
print(b-a)
r = a.difference(b)
print(r)                    #{1, 3, 5}
print(a)                    #{1, 2, 3, 4, 5}
print(b)                    #{2, 4, 7}


r = a.difference_update(b)
print(r)                    #None
print(a)                    #{1, 3, 5}
print(b)                    #{2, 4, 7}


print('\n===================')

x = {1, 2 , 3 }
y = {2, 3 , 4 }
print(x.symmetric_difference(y))          #{1, 4}
print(x ^ y)                              #{1, 4}


x = {1, 2 , 3 }
y = {2, 3 , 4 }
print(x.intersection(y))                  #{2, 3}
print(x & y)                              #{2, 3}



x = {1, 2 , 3 }
y = {2, 3 , 4 }
print(x.union(y))                      #{1, 2, 3, 4}
print(x | y)                           #{1, 2, 3, 4}


print('\n===================')

x = {56, 98 }
s = 'ali'
a = [13, 25 ]
t = (7, 8 )
d = {'one':1 , 'two':2}
x.update(s,a,t,d)         #{98, 7, 8, 'one', 13, 'l', 'a', 'two', 56, 25, 'i'}
print(x)



print('\n===================')

x = {1, 2, 3 }
y = {2, 3 }
print(x.isdisjoint(y))                #False

x = {1, 2 }
y = {3, 7, 8 }
print(x.isdisjoint(y))               #True


print('\n===================')

x = {1, 2 }
y = {1, 2, 3 }
print(x.issubset(y))                #True
print(y.issubset(x))                #False


print('\n===================')

w = 'ailreza'
x = {'a' , 'r'}
s = set(w)
print(x.intersection(s))           #{'r', 'a'}

print('\n===================')

d1 = {'a': 1, 'b':3, 'c':2}
d2 = {'a': 2, 'b':3, 'c':1}
s1 = set(d1.items())
s2 = set(d2.items())
s = s1 & s2
for k,v in s :
  print(k)                         #b








