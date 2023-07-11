#Author: Vasanta
#Date: 03/06/2023
#Purpose: Example of runtime analysis

def func1(n): #a*n + b, (a+1)*n, O(n)
    i = 0
    while i < n:
        print(i)
        i = i + 1

def func2(n): #(a+a)*n + (b+b), O(n)
    i = 0
    while i < n:
        print(i)
        i = i + 1

    i = 0
    while i < n:
        print(i)
        i = i + 1

def func3(n):
    i = 0
    while i < n: #a*n + b, O(n)
        if i % 2 == n:
            print(i)
        i = i + 1

def func4(n):#b , O(1)
    i = 0
    while i < 5:
        print(i)
        i = i + 1

def func5(n):#a*n^2 + b*n + c, O(n^2)
    i = 0
    while i < n:
        j = 0
        while j < n:
            print(i, j)
            j  = j + 1
        i = i + 1

def func6(n): #a*n + b, O(n)
    i = 0
    while i < n:
        j = 0
        while j < 3:
            print(i, j)
            j = j + 1
        i = i + 1

def func7(n): #a*n+b, O(n)
    i = 0
    while i < 2:
        j = 0
        while j < n:
            print(i, j)
            j = j + 1
        i = i + 1