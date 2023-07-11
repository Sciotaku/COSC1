# Author: Rahul Gupta
# Date: 02/15/2023
# Purpose: Function call stack


def funcA(n):
    if n < 10:
        x = funcB(n+5)
        return x
    else:
        return n


def funcB(n):
    if n < 10:
        y = funcA(n+7)
        return y
    else:
        return n


print(funcA(2))
