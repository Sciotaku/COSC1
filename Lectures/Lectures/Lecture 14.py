# Rahul Gupta
# Date: 02/06/2023
# Purpose: List of strings

# Define a function that takes a non-empty list of non-empty strings as a parameter and returns the string that has max
# number of a's in it.

# Helper function: Counts the number of a's in a given string
# def count_a(gs):
#     count = 0
#
#     for ch in gs:
#         if ch == "a":
#             count = count + 1
#
#     return count
#
#
# # main function: Find the string with max a's
# def max_a_in_list(glist):
#     max_a_str = glist[0]
#     i = 0
#     while i < len(glist):
#         a1 = count_a(max_a_str)
#         a2 = count_a(glist[i])
#         if a1 < a2:
#             max_a_str = glist[i]
#
#         i = i + 1
#
#     return max_a_str
#
#
# mlist = ["test", "snow", "Dartmouth", "Snowboard", "banana", "mango"]
# print(max_a_in_list(mlist))


# Selection Sort
# Algorithm
# The smallest number between index 0 and end of the list is: -5
# Swap -5 with 45
# [-5, 5, 23, 45, 13, 108, 34]

# Smallest number between index 1 and end of the list is: 5
# Swap 5 with 5
# [-5, 5, 23, 45, 13, 108, 34]

# Smallest number between index 2 and end of the list is: 13
# Swap 13 with 23
# [-5, 5, 13, 45, 23, 108, 34]

# Smallest number between index 3 and end of the list is: 23
# Swap 23 with 45
# [-5, 5, 13, 23, 45, 108, 34]

# Smallest number between index 4 and end of the list is: 34
# Swap 34 with 45
# [-5, 5, 13, 23, 34, 108, 45]

# Smallest number between index 5 and end of the list is: 45
# Swap 45 with 108
# [-5, 5, 13, 23, 34, 45, 108]


# Helper function: Find the index of min values between teh parameter k and end of the given list.

# def find_min_i(k, glist):
#     min_i = k
#     i = k
#     while i < len(glist):
#         if glist[min_i] > glist[i]:
#             min_i = i
#
#         i = i + 1
#
#     return min_i
#
#
# def selection_sort(glist):
#     start = 0
#     while start < len(glist):
#         min_index = find_min_i(start, glist)
#
#         temp = glist[min_index]
#         glist[min_index] = glist[start]
#         glist[start] = temp
#         start = start + 1
#
#
# mlist = [45, 5, 23, -5,  13, 108, 34]
# selection_sort(mlist)
# print(mlist)


# List of lists example

# Define a function that takes a list of lists as a parameter. Assume that inner lists have integers.
# The function should find the maximum element stored in any of the inner list.

# def max_in_lists(glist):
#     max_ele = glist[0][0]
#     for inner in glist:
#         for ele in inner:
#             if ele > max_ele:
#                 max_ele = ele
#
#     return max_ele
#
#
# mlist = [[-40, 5, 20], [50, 89], [120]]
# print(max_in_lists(mlist))
