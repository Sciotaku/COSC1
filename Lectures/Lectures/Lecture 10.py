# Rahul Gupta
# Date: 01/27/2023
# Purpose: Demo break and continue statements

# def func(n):
#     i = 1
#     while i <= n:
#         print(i)
#         i = i + 1
#         if i == 4:
#             break
#         print(i)
#
#
# func(5)


# def func(n):
#     i = 1
#     while i <= n:
#         print(i)
#         i = i + 1
#         if i == 4:
#             continue  # Skips to the header of the loop
#         print(i)
#
#
# func(5)


# Is prime with print


# count = 0
# loop = 1
#
#
# def prime(n):
#     global count, loop
#     while loop <= n:
#         if n % loop == 0:
#             count = count + 1
#         loop = loop + 1
#     if count == 2:
#         print("The given number is Prime")
#     else:
#         print("The given number is Composite")
#
#
# prime(int(input("Enter any positive integer: ")))


# def is_prime_print(n):
#     if n == 1:
#         print(False)
#     else:
#         f = 2
#         while f < n:
#             if n % f == 0:
#                 break
#             f = f + 1
#
#         if f == n:
#             print(True)
#         else:
#             print(False)
#
#
# is_prime_print(237)


# def is_prime_return(n):
#     if n == 1:
#         return False
#     f = 2
#     while f < n:
#         if n % f == 0:
#             break
#         f = f + 1
#
#     if f == n:
#         return True
#     else:
#         return False
#
#
# i = 1
# while i <= 1000:
#
#     test = is_prime_return(i)
#
#     if test:
#         print(i)
#
#     i = i + 1



