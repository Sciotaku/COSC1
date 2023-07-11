# Problem 1

# def num_square(n):
#     if n == 0:
#         return
#
#     res = n ** 2
#     print(res)
#     num_square(n-1)
#
#
# num_square(5)


# Problem 2

# def num_square(n):
#     if n == 0:
#         return
#
#     num_square(n - 1)
#     res = n ** 2
#     print(res)
#
#
# num_square(5)


# Problem 3

# def square_even(n):
#     if n == 0:
#         return
#
#     square_even(n - 1)
#
#     if n % 2 == 0:
#         res = n ** 2
#         print(res)
#
#
# square_even(10)


# Problem 4

# res = 1
#
#
# def prod_odd(n):
#     global res
#     if n == 0:
#         return
#
#     if n % 2 != 0:
#         res = res * n
#     prod_odd(n-1)
#     return res
#
#
# print(prod_odd(5))


# Problem 5

# mult_list = []
#
#
# def mult_num(n, p):
#     if n == 0:
#         return
#
#     if n % p == 0:
#         mult_list.append(n)
#
#     mult_num(n-1, p)
#     return mult_list
#
#
# print(mult_num(10, 3))


# Problem 6
# i = 0
# res = 0
#
#
# def mult_sum(glist, p):
#     global res, i
#     if i == len(glist):
#         return
#
#     if glist[i] % p == 0:
#         res = res + glist[i]
#
#     i = i + 1
#     mult_sum(glist, p)
#     return res
#
#
# print(mult_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))


# Problem 7


# def count_evens(glist, n=0):
#     if n >= 2:
#         return True
#
#     if len(glist) == 0:
#         return False
#
#     if glist[0] % 2 == 0:
#         n = n + 1
#
#     glist.pop(0)
#     return count_evens(glist, n)
#
#
# mlist = [1, 2, 3, 4, 5, 7, 9]
# print(count_evens(mlist))









