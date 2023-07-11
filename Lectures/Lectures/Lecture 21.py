# Author: Rahul Gupta
# Date: 02/15/2023
# Purpose: Recursion examples: lists

# def sum_evens_list(glist, i=0):
#     if i == len(glist):
#         return []
#
#     res_list = sum_evens_list(glist, i + 1)
#
#     if glist[i] % 2 == 0:
#         res_list.append(glist[i])
#
#     return res_list
#
#
# mlist = [10, 6, 7, 3, 2]
# print(sum_evens_list(mlist))


# Reverse a string

# def reverse_string(gs, i=0):
#     if i == len(gs):
#         return ""
#
#     res = reverse_string(gs, i+1)
#
#     res = res + gs[i]
#
#     return res
#
#
# print(reverse_string("abcd"))


# return the nth number in Fibonacci sequence

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#
#     n1 = fib(n-1)
#     n2 = fib(n-2)
#
#     return n1 + n2
#
#
# print(fib(4))

# Towers of Hanoi


