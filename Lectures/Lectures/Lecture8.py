# Author: Rahul Gupta
# Date: 1/23/2023
# Purpose: Demo return statement


# Functions that return parameter
# from math import sqrt
#
#
# def func(n):
#     print(n**(1/2))
#
#
# func(4)
#
# print(sqrt(4))

# def func(n):
#     return n * n
#
#
# x = func(4)
# y = func(9)
# print(x + y)


# Functions being passed as parameters
# def func(n):
#     print("In function func")
#     print("Address of function n is", n)
#     n()
#
#
# def x():
#     print("In function x")
#     print("Address of function n is", x)
#
#
# func(x)


# def func(n):
#     print("In function func")
#     print("Address of function n is", n)
#     n()
#
#
# def x():
#     print("In function x")
#     print("Address of function n is", x)
#
#
# func(x())


# def func(n):
#     print("In function func")
#     print("Address of function n is", n)
#     n(10)
#
#
# def x(p):
#     print("In function x")
#     print("Address of function n is", x, p)
#
#
# func(x)


# Functions with optional parameters

# def func(x, y, z):
#     print(x, y, z)


# func(10, 20, 30)  # There are positional parameters/arguments

# func(10, 20)  # What happens?


# def func(x, y, z=300):
#     print(x, y, z)


# func(10, 20)  # z is a optional parameter
# func(10, 20, 30)  # It overrides the value of z


# def func(x, y=200, z=300):
#     print(x, y, z)


# func(10)  # y and z are optional parameters
# func(10, 20) # It overrides the value of y


# Keywords arguments
# def func(x, y=200, z=300):
#     print(x, y, z)


# func(10, z=30)
# func(10, z=30, y=20)  # Position doesn't matter when using keywords


