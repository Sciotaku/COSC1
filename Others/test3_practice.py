# 1. Define a recursive function that takes a list of integers as a parameter and returns True if the list is sorted
# in increasing order; otherwise it returns False.

# def is_sorted(glist, k=0):
#     if k == len(glist) - 1 or k == len(glist):
#         return True
#
#     if glist[k] <= glist[k+1]:
#         return is_sorted(glist, k+1)
#     else:
#         return False
#
#
# mlist = [0, 1, 2, 3, 4, 5]
# print(is_sorted(mlist))


# 2. Define a recursive function that takes two strings s1 and s2 as parameters and checks if s2 is a prefix of s1.
# For example: s2 = “test” and s = “testing” then s1 is a prefix of s2.

# def check_prefix(s1, s2, k=0):
#     if k == len(s1):
#         return True
#
#     if s1[k] == s2[k]:
#         return check_prefix(s1, s2, k+1)
#     else:
#         return False
#
#
# a1 = "fast"
# a2 = "fasting"
# print(check_prefix(a1, a2))


# 3. Define a recursive function that takes two strings s1 and s2 as parameters and checks if s2 is a substring of s1.

# def is_substring(s1, s2, i=0, j=0):
#     if len(s2) > len(s1):
#         return False
#
#     if j == len(s2):
#         return True
#
#     if i == len(s1):
#         return False
#
#     if s2[j] == s1[i]:
#         return is_substring(s1, s2, i+1, j+1)
#     else:
#         return is_substring(s1, s2, i-j+1, 0)
#
#
# a1 = "dishwasher"
# a2 = "wash"
# print(is_substring(a1, a2))


# 4. Write a recursive function that takes two non-negative integers n and k as parameters and prints the first k
# even numbers greater than n.

# def great_num(n, k):
#     if k == 0:
#         return
#
#     if (n+1) % 2 == 0:
#         print(n+1)
#         great_num(n+1, k-1)
#     else:
#         great_num(n+1, k)
#
#
# print(great_num(7, 3))


# 5. Write a recursive function that takes two non-negative integers n and k as parameters and returns a list
# containing first k even numbers greater than n.

# def great_num_list(n, k):
#     if k == 0:
#         return []
#
#     if (n + 1) % 2 == 0:
#         l = great_num_list(n + 1, k - 1)
#         l.insert(0, n + 1)
#     else:
#         l = great_num_list(n + 1, k)
#
#     return l
#
#
# print(great_num_list(5, 4))


# 6. Write a recursive function that takes a list of integers glist that is sorted in increasing order and an integer
# key as a parameter. The function should insert the key into glist such that glist remains sorted.


# def keep_sorted(glist, key, i=0):
#     if i >= len(glist):
#         glist.append(key)
#         return
#
#     if key < glist[i]:
#         glist.insert(i, key)
#     else:
#         keep_sorted(glist, key, i+1)
#
#     return glist
#
#
# mlist = [1, 2, 3, 4, 5]
# print(keep_sorted(mlist, 0))


# 7. Write a recursive function find_min that takes a list of integers as a parameter and returns the minimum element
# in the list.


# def find_min(glist, i=0):
#     if i == len(glist) - 1:
#         return glist[-1]
#
#     m = find_min(glist, i + 1)
#
#     if m < glist[i]:
#         return m
#     else:
#         return glist[i]
#
#
# mlist = [1, 2, 3, 4, 5, 4, 3, 2, 0]
# print(find_min(mlist))


# 8. Write a recursive function find_min_index that takes a list of integers as a parameter and returns that index
# of the minimum element in the list.

# def find_min_index(glist, i=0):
#     if i == len(glist) - 1:
#         return i
#
#     m = find_min_index(glist, i + 1)
#
#     if glist[m] < glist[i]:
#         return m
#     else:
#         return i
#
#
# mlist = [10, 5, 9, 0, 6, 8, 7, 3, 4, 2]
# print(find_min_index(mlist))


# Define a recursive function that takes two positive integers n and k as parameters and does the following:
# prints first k even numbers between 1 and n if there are at least k even numbers between 1 and n
# otherwise it prints all the even numbers between 1 and n.


# def func(n, k):
#     if n == 1:
#         return 0
#
#     # The recursive call returns how many even numbers it has already included in the sum
#     x = func(n - 1, k)
#
#     # If x == k it means I have added first k even numbers
#     if x == k:
#         return x
#     else:  # If x != k (it means it is x < k as k is a positive number, then print more even numbers)
#         if n % 2 == 0:
#             print(n)
#             return x + 1
#         else:
#             return x
#
#
# func(10, 10)


# Identify the base case: The base case is the simplest possible input for which the answer is already known.
# This is the point at which the recursion "bottoms out" and the function stops calling itself.
# Identify the base case first, as it is usually the easiest case to solve.
# Define the recursive case: The recursive case is when the function calls itself with a smaller input.
# This is where the real work happens. Think about how the problem can be broken down into smaller sub problems,
# and how those sub problems can be solved recursively.
# Trust the recursion: When writing a recursive function, it can be difficult to see how the function will work
# for larger inputs. Trust that the recursion will work for smaller inputs, and focus on solving the problem for
# those inputs. The recursive function will then be able to solve the problem for larger inputs by breaking them down
# into smaller sub problems.
# Use helper functions: Sometimes it can be helpful to define a helper function to handle some of the recursion.
# This can make the code more readable and easier to understand.
# Visualize the recursion: Drawing a diagram or a flowchart can help you visualize how the recursion works.
# This can make it easier to understand and debug the code.
# Test the function: Make sure to test the function with different inputs, including edge cases and corner cases.
# This will help you identify any issues with the recursion and ensure that the function is working correctly.














