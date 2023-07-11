#Author: Vasanta
#Date: 02/22/2023
#Purpose: Multiple recursive calls (Fibonacci)

#1 1 2 3 5 8 13 21 .....
#fib(n) = fib(n-1) + fib(n-2)

def fib(n):
    if n == 1 or n == 2:
        return 1

    n1 = fib(n-1)
    n2 = fib(n-2)

    return n1 + n2

print(fib(4))
