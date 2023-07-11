# Author: Rahul Gupta
# Date: 03/06/2023
# Purpose: Runtime analysis examples

def func1(n):  # a*n + b, O(n)
    i = n
    while i >= 1:
        print(n)
        i = i - 1


def func2(n):  # a*n^2 + b*n + c, O(n^2)
    i = n
    while i >= 1:
        print(n)
        i = i - 1
        j = 0
        while j < n:
            j = j + 1
        i = i - 1


def func3(n):  # O(log(n))
    i = 1
    while i < n:
        print(i)
        i = i * 2


def func4(n):  # O(log(n))
    i = n
    while i > 1:
        print(i)
        i = i // 2


def func5(glist):  # n is len(glist), O(n)
    for x in glist:
        print(x)


def func6(n):  # O(n^2)
    i = 1
    rlist = []
    while i <= n:
        rlist.insert(0, i)
        i = i + 1


def func7(n):
    i = n
    rlist = []
    while i >= 1:
        rlist.append(i)
        i = i + 1

