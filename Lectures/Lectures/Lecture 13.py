# Rahul Gupta
# Date: 02/03/2023
# Purpose: for loop examples

# def find_max_i(glist):
#     max_i = 0
#
#     for i in range(0, len(glist)):
#         if glist[max_i] < glist[i]:
#             max_i = i
#
#     return max_i
#
#
# mlist = [5, -34, -3, 30, -3, 4, 1, 7]
# print(find_max_i(mlist))


# Check if a list is sorted in ascending order

# def is_sorted(glist):
#
#     for i in range(0, len(glist) - 1):
#         if glist[i] > glist[i+1]:
#             return False
#
#     return True
#
#
# mlist = [1, 2, 3, 4, 5, 6]
# print(is_sorted(mlist))


# Nested loops

# i = 0
# while i < 5:
#     print(i)
#     i = i + 1
#
#     j = 0
#     while j < 5:
#         print(j)
#         j = j + 1


# def primes_in_the_list(glist):
#
#     for ele in glist:
#         if ele == 1:
#             continue
#
#         f = 2
#         while f < ele:
#             if ele % f == 0:
#                 break
#
#             f = f + 1
#
#         if f == ele:
#             print(ele)
#
#
# mlist = [2, 3, 5, 7, 9, 11, 13, 15]
# print(primes_in_the_list(mlist))

