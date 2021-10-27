# week 1 pythong 1 class
'''
Name:
Date:
Description:  Examples, etc

Week 1 Python Notes
Name:
Date:
Description: Examples of functions in Python
'''


########## Functions and return ##########

# f(x) = x^2 + 3x +2

def myfun(x):
    'Calculates the function f(x) = x^2 + 3x +2'
    solution = x**2 + 3*x + 2
    return solution             ## Use return when you expect the function to give a value back in return

help(myfun)

print(myfun(5))

print(10+6)

"""
def urfun(x):
    'Calculates the function f(x) = x^2 - 3x +2'
    solution = x**2 -3*x + 2    ## Forgot to return

def theirfun(x):
    'Calculates the function f(x) = x^2 + 3x - 2 and prints f(x)'
    solution = x**2 + 3*x - 2
    print(solution)

print(myfun(5))
print(urfun(5))                 ## We'll get None because the function did not return anything
print(theirfun(5))

var1 = myfun(5)

print("The function value is", var1)


help(myfun)

"""

"""
def rectPrismVol(height, length, width):
    volume = height * length * width
    return volume


prism1vol = rectPrismVol(4, 6, 10)
prism2vol = rectPrismVol(5.5, 10, 1)

print("Prism 1:", prism1vol, "cu. ft.")
print("Prism 2:", prism2vol, "cu. ft.")

print(type(prism1vol))
print(type(prism2vol))

print("Prism 1 smaller?", prism1vol < prism2vol)
"""

"""
def myfun(x):
    'Calculates the function f(x) = x^2 + 3x +2'
    solution = x**2 + 3*x + 2
    return solution         ## ends the function
    solution = 2 * solution ## this line is ignored
    return solution         ## this line is ignored

print(myfun(5))
"""

"""
def myfun(x):
    'Calculates the function f(x) = x^2 + 3x +2'
    solution = x**2 + 3*x + 2
    solution = 2 * solution
    return solution

print(myfun(5))
"""


########## import ##########

"""
import math

a = math.sqrt(25)
b = math.ceil(4.3)      ## number rounded up

print(a, b)

help(math)

print(math.pi)
"""

"""
import math as m
a = m.sqrt(34)
b = m.ceil(5.1444)      ## number rounded up

print(a, b)

print(m.pi)
"""

"""
import fractions
import math

num1 = fractions.Fraction(3, 4)

print(num1)
print(num1 == 0.75)
print(num1 > 1)
print(type(num1))

print(math.floor(num1))     ## number rounded down
print(3 // 4)               ## division rounded down
"""


"""
## changing or checking working directory
import os                   ## please don't change directory in your programming assignments
os.chdir(_____________)
os.getcwd()
"""

"""
## Task: Calculate the circumference and area of a circle
import math

def circumference(radius):
    ' Calculate the circumference of a circle given radius '
    return 2 * math.pi * radius

def area(radius):
    ' Calculate the area of a circle given radius '
    return math.pi * radius ** 2


# Creating and calculating variables
r = 10
c = circumference(r)
a = area(r)

# Print summary
print("Radius:", r)
print("Circumference:", c)
print("Area:", a)
"""


"""
## Task: Calculate the circumference and area of a circle
import math

def circumference(radius):
    ' Calculate the circumference of a circle given radius '
    return 2 * math.pi * radius

def area(radius):
    ' Calculate the area of a circle given radius '
    return math.pi * radius ** 2

def printdetails(radius):
    'Prints a summary of the radius, circumference, and area'
    c = circumference(radius)
    a = area(radius)

    # Print summary
    print("----------")
    print("Radius:", radius)
    print("Circumference:", c)
    print("Area:", a)

printdetails(10)
printdetails(12)
printdetails(2.5)


## Task: Calculate the circumference and area of a circle with rounding to two decimals
import math

def circumference(radius):
    ' Calculate the circumference of a circle given radius '
    return 2 * math.pi * radius

def area(radius):
    ' Calculate the area of a circle given radius '
    return math.pi * radius ** 2

def printdetails(radius):
    'Prints a summary of the radius, circumference, and area'
    c = circumference(radius)
    a = area(radius)

    # Print summary
    print("----------")
    print("Radius:", round(radius,ndigits = 2))
    print("Circumference:", round(c, ndigits = 2))
    print("Area:", round(a, ndigits = 2))

printdetails(10)
printdetails(12)
printdetails(2.5)
"""