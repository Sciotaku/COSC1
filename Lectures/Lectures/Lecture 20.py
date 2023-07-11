# Author: Rahul Gupta
# Date: 02/15/2023
# Purpose: Recursion examples: non-lists

# Define a recursive function that prints all the even numbers between 1 and n.


# def print_evens(n):
#     if n == 1:
#         return
#
#     print_evens(n-1)
#     if n % 2 == 0:
#         print(n)
#
#
# print(print_evens(10))


# def sum_evens(n):
#     if n == 1:
#         return 0
#
#     res = sum_evens(n-1)
#
#     if n % 2 == 0:
#         res = res + n
#
#     return res
#

# print(sum_evens(10))


# Define a recursive function that takes a positive integer n andn non-negative integer k as a parameter and returns the
# largest k even numbers between 1 and n.

# def sum_evens_k(n, k):
#     if k == 0:
#         return 0
#
#     if n == 1:
#         return 0
#
#     if n % 2 == 0:
#         res = sum_evens_k(n-1, k-1)
#         res = res + n
#     else:
#         res = sum_evens_k(n-1, k)
#
#     return res
#
#
# print(sum_evens_k(9, 4))


# Define a recursive function that takes a list of positive integers and prints all even numbers in the list.

# def print_evens_list(glist, i=0):
#     if i == len(glist):
#         return
#
#     print_evens_list(glist, i + 1)
#
#     if glist[i] % 2 == 0:
#         print(glist[i])
#
#
# mlist = [10, 5, 7, 9, 4, 3, 6]
# print(print_evens_list(mlist))


# def sum_evens_list(glist, i=0):
#     if i == len(glist):
#         return 0
#
#     res = sum_evens_list(glist, i + 1)
#
#     if glist[i] % 2 == 0:
#         res = res + glist[i]
#
#     return res
#
#
# mlist = [10, 5, 7, 9, 4, 3, 6]
# print(sum_evens_list(mlist))


# Define a recursive function that takes a string as a parameter and checks if the string is a palindrome.

# def rec_is_palindrome(gs, i=0, j=None):
#     if j == None:
#         j = len(gs) - 1
#
#     if i >=j:
#         return True
#
#     if gs[i] != gs[j]:
#         return False
#
#     res = rec_is_palindrome(gs, i + 1, j - 1)
#
#     return res
#
#
# print(rec_is_palindrome("LOL"))

