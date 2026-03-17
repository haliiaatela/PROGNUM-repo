#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Define the discriminant and solutions of the quadratic equation. 

import math

def value_D(a, b, c):
    return b**2 - 4*a*c

def x1(a, b, value_D):
    return (-b + math.sqrt(value_D)) / (2 * a)

def x2(a, b, value_D): 
    return (-b - math.sqrt(value_D)) / (2 * a)

def x(b, a):
    return  -b / (2 * a)

# User's input values.

a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))

d = value_D(a, b, c)

# State conditions to determine number of solutions.

if d > 0:
    res1 = x1(a, b, d)
    res2 = x2(a, b, d)
    print(f"two solutions: {res1}, {res2}")

elif d == 0:
    res = x(b, a)
    print(f"one solution: {res}")
          
else:
    print (f"no real solution")

