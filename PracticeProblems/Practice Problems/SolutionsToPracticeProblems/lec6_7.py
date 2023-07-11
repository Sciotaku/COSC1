#1
# Define a function print_evens that takes a positive
# integer n as parameter and prints all the even
# numbers between 0 and n, excluding n irrespective
# of if it is even or odd.

def print_evens(n):
    i = 0
    while i < n:
        if i % 2 == 0:
            print(i)
        i = i + 1

#print_evens(7)
#print_evens(10)

#2
#Define a function print_evens that takes a
#positive integer n as parameter and prints all
#the even numbers between 0 and n, including n if it
#is an even number.

def print_evens1(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            print(i)
        i = i + 1

# print_evens1(7)
# print_evens1(10)

#3
#Define a function print_odds that takes a
#positive integer n as parameter and prints all the
#odd numbers between 0 and n, including n if it is
#an odd number.

def print_odds(n):
    i = 0 #You can also start at 1
    while i <= n:
        if i % 2 == 1:
            print(i)
        i = i + 1

# print_odds(7)
# print_odds(10)

#4
#Define a function product_even that takes a positive
#integer n as parameter and prints the product of all
#even numbers between 1 and n (including n).

def product_even(n):
    i = 1
    prod = 1
    while i <= n:
        if i % 2 == 0:
            prod = prod * i
        i = i + 1

    print(prod)

# product_even(5)
# product_even(8)

#5

#Define a function product_odd that takes two positive
#integers m and n as parameters and prints the product
#of all odd numbers between m and n. You may assume m < n
#and m is odd.

def product_odd(m, n):
    i = m
    prod = 1

    while i <= n:
        prod = prod * i
        i = i + 2
        #i will remain odd as starting value m is odd

    print(prod)

#product_odd(3, 8)

#6
#Define a function product_odd that takes two positive
# integers m and n as parameters and prints the product
# of all odd numbers between m and n. You may assume m < n.
# Parameters m and n can be even or odd.

def product_odd1(m, n):
    #This if statement will make sure m will always
    #start as odd
    if m % 2 == 1:
        i = m
    else:
        i = m + 1
    prod = 1

    while i <= n:
        prod = prod * i
        i = i + 2
        #varibale i will remain odd as starting value
        #m is odd

    print(prod)

# product_odd1(2, 8)
# product_odd1(3, 8)

#7
#Define a function last_k_evens1 that takes two positive
#integers n and k as parameters. It should print the
# last k even numbers between 1 and n. You can make the
# following assumptions:
#1. There are at least k even numbers between 1 and n
#2. n is an even number

def last_k_even1(n, k):
    i = n
    count = 0 #tracks the number of even numbers printed
    while count < k:
        if i % 2 == 0:
            print(i)
            count = count + 1
        i = i - 1

#last_k_even1(10, 4)

#8
#8. Define a function last_n_evens2 that takes two
# positive integers n and k as parameters. It should
# print the last k even numbers between 1 and n. You
# can make the following assumptions:
#1.There are at least k even numbers between 1 and n

def last_k_even2(n, k):
    i = n
    count = 0 #tracks the number of even numbers printed
    while count < k:
        if i % 2 == 0:
            print(i)
            count = count + 1
        i = i - 1

#last_k_even2(10, 4)

#9
#Define a function last_k_evens3 that takes two
#positive integers n and k as parameters. Your function
#should do the following:
#1. print the last k even numbers between 1 and n if
# there are k or more even numbers between 1 and n.
#2. Otherwise it should print all the even numbers
# between 1 and n.

def last_k_even3(n, k):
    i = n
    count = 0 #tracks the number of even numbers printed
    while count < k and i > 1:
        if i % 2 == 0:
            print(i)
            count = count + 1
        i = i - 1

# last_k_even3(10, 4)
# last_k_even3(10, 7)
# last_k_even3(11, 5)

#10
#Define a function factorial_limit1 that takes a positive
#integer limit as parameter and prints the largest
#number whose factorial is strictly less than the value
#limit. For example:
#If limit is 121, then your function should print 5.
#If limit is 115, then your function should print 4.
#If limit is 120, then your function should print 4 (strictly smaller than the limit).

def factorial_limit1(limit):
    i = 1
    prod = 1
    while prod < limit:
        prod = prod * i
        i = i + 1

    print(i-2)
    #We need to subract 2 from i as the last i included
    #in the prodcut should not be counted and
    #i is one more that what was included in the product.

#factorial_limit1(120)

#11
#Define a function factorial_limit2 that takes a
# positive integer limit as parameter and prints the
# largest number whose factorial is less than or equal
# to limit. For example:
#1. If limit is 121, then your function should print 5.
#2. If limit is 115, then your function should print 4.
#3. If limit is 120, then your function should print 5.

def factorial_limit2(limit):
    i = 1
    prod = 1
    while prod < limit:
        prod = prod * i
        i = i + 1

    if prod == limit:
        print(i - 1)
    else:
        print(i - 2)

#factorial_limit2(115)

#12
#Define a function lcm that takes two positive integer
# parameters m and n, and prints the smallest number
# that is divisible by both m and n. For example:
#If m = 2 and n = 3 then it should print 6.
#If m = 8 and n = 4 it should print 8.

def lcm(m, n):
    if m < n: #select the bigger number as starting point
        i = n
    else:
        i = m

    while i % m != 0 or i % n != 0:
        #keep increasing i till we find a number
        #divisible by both m and n.
        i = i + 1

    print(i)

#lcm(12, 30)

#13
#Define a function is_factorial, that takes a positive
#integer n as parameter and prints True if it is a
#factorial of another positive integer. Otherwise it
#prints False. For example:
#1. If n = 24 then it should print True as 24 is
# factorial of 4.
#2. If n = 25 then it should print False as 25 is
# not equal to the factorial of any other positive
# integer.

def is_factorial(n):
    i = 1
    prod = 1

    while prod < n:
    # Keep computing the product till it is either equal
    # or greater than n.
        prod = prod * i
        i = i + 1

    #If prod is exactly equal to n then
    #n is a factorial of a number
    if prod == n:
        print(True)
    else:
        print(False)


#is_factorial(121)
#is_factorial(120)

#14
#Define a function gcd that prints the greatest common
#divisor of two positive integers m and n that are
#passed as parameters to the function.

def gcd(m, n):
    if m < n: #Start looking for factor at the smaller number
        start = m
    else:
        start = n

    i = start
    #We will start with the smaller number and
    #go in decreasing order looking for a
    #number that is factor of both m and n

    while m % i != 0 or n % i != 0:
        i = i - 1

    print(i)

#gcd(4, 15)
#gcd(15, 5)
#gcd(11, 7)




