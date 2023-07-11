# Rahul Gupta
# Date: 01/30/2023
# Purpose: Intro to lists

# mlist = [10, 20, 30, 40, -40, -30, -20, -10]
# print(mlist)

# Adding to a list
# mlist.append(45)
# print(mlist)

# Indexing into the list
# print(mlist[2])
# mlist[1] = 0
# print(mlist)
# mlist.insert(2, 1)
# print(mlist)

# Length of the list
# print(len(mlist))
# print(mlist[len(mlist) - 1])
# print(mlist[-1])

# Delete from the list
# mlist.remove(-10)
# print(mlist)
# del mlist[2]
# print(mlist)

# Going through all elements in a list

# mlist = [10, 20, 30, 40, -40, -30, -20, -10]

# Basics
# i = 0
# while i <= len(mlist) - 1:
#     print(mlist[i])
#     i = i + 1

# Define a function that takes a list of positive integers in a list

# prod = 1
#
#
# def prod_list(glist):
#     global prod
#     i = 1
#     while i <= len(glist) - 1:
#         if glist[i] > 0:
#             prod = prod * glist[i]
#         i = i + 1
#     return prod
#
#
# mlist = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# prod_list(mlist)
# print("The product of all positive integers in the given list is", prod)


# Find the max element in the given list

# def find_max(glist):
#     max = glist[0]
#     i = 0
#     while i <= len(glist):
#         if max < glist[i]:
#             max = glist[i]
#         i = i + 1
#     return max