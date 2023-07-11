# 1. Define a function that takes a list of integers glist as parameter and prints the even numbers in glist.
# def even_num(glist):
#     n_list = []
#     for ele in glist:
#         if ele % 2 == 0:
#             n_list.append(ele)
#     return n_list
#
#
# mlist = [1, 4, 5, 20, 2, 12, 81]
# print(even_num(mlist))


# 2. Define a function that takes a list of integers glist as parameter and prints the numbers at even index.
# def even_num(glist):
#     n_list = []
#     i = 0
#     for ele in glist:
#         if i % 2 == 0:
#             n_list.append(ele)
#         i = i + 1
#     return n_list
#
#
# mlist = [1, 4, 5, 20, 2, 12, 81]
# print(even_num(mlist))


# 3.Define a function that takes a list of integers glist that is sorted (in increasing order) and an integer n as
# parameters and inserts n into glist in such a way that glist remains sorted.

# def sort_list(glist, n):
#     n_list = mlist
#     i = 0
#     for ele in glist:
#         if n < ele:
#             n_list.insert(i, n)
#             break
#         i = i + 1
#
#     return n_list
#
#
# mlist = [1, 2, 3, 4, 6, 8, 10]
# print(sort_list(mlist, 7))


# 4. Define a function that takes a list of integers glist as parameter and returns True if the list is either sorted
# in decreasing or increasing order. Otherwise it returns False. [Extra practice: If you used two loops, think how you
# can solve this problem with only one loop.]

# def check_ordered1(glist):
#
#     # These two variables keep track if the list is sorted in increasing or decreasing order
#
#     is_increasing = True
#     is_decreasing = True
#
#     i = 0
#     while i < len(glist) - 1:
#         if glist[i] < glist[i + 1]:
#             is_decreasing = False
#         elif glist[i] > glist[i + 1]:
#             is_increasing = False
#
#         i = i + 1
#     # If both are False then return False otherwise return True
#     return is_decreasing or is_increasing
#
#
# print(check_ordered1([10, 20, 30, 40, 50]))
# print(check_ordered1([50, 40, 30, 20, 10]))
# print(check_ordered1([4, 4, 4, 4, 4]))
# print(check_ordered1([10, 45, 55, 89, 12]))
# print("------------------")
#
#
# def check_ordered2(glist):
#
#     # These two variables keep track if the list is sorted in increasing or decreasing order
#
#     is_increasing = True
#     is_decreasing = True
#
#     for i in range(len(glist) - 1):
#         if glist[i] < glist[i+1]:
#             is_decreasing = False
#         elif glist[i] > glist[i+1]:
#             is_increasing = False
#     # If both are False then return False otherwise return True
#     return is_decreasing or is_increasing
#
#
# print(check_ordered2([10, 20, 30, 40, 50]))
# print(check_ordered2([50, 40, 30, 20, 10]))
# print(check_ordered2([4, 4, 4, 4, 4]))
# print(check_ordered2([10, 45, 23, 89, 12]))


# 5. Define a function that takes two lists glist1 and glist2 as parameters and returns True if they are the reverse of
# each other, otherwise returns False. For simplicity you can assume that the given lists contain only integers.

# def reverse_list(glist1, glist2):
#
#     if len(glist1) != len(glist2):
#         return False
#
#     n_list = []
#     i = len(glist1) - 1
#     while i >= 0:
#         n_list.append(glist1[i])
#         i = i - 1
#
#     if n_list == glist2:
#         return True
#     else:
#         return False
#
#
# mlist1 = [5, 4, 3, 2, 1]
# mlist2 = [1, 2, 3, 4, 5]
# print(reverse_list(mlist1, mlist2))


# 6. Define a function that takes a list of integers glist as a parameter and returns a list containing all the even
# numbers in glist. Please note that the function should create a new list and not modify the given list glist.

# def even_num(glist):
#     n_list = []
#     for ele in glist:
#         if ele % 2 == 0:
#             n_list.append(ele)
#     return n_list
#
#
# mlist = [1, 4, 5, 20, 2, 12, 81]
# print(even_num(mlist))

# 7. Define a function that takes a list of integers glist as parameter and returns a list containing those numbers in
# glist that are equal to the index at which they appear in glist. Please note that the function should create a new
# list and not modify the given list glist.

# def num_equal_index(glist):
#     i = 0
#     nlist = []
#     for ele in glist:
#         if ele == i:
#             nlist.append(glist[i])
#         i = i + 1
#     return nlist
#
#
# mlist = [0, 13, 2, 33, 5, 67, 36, 7]
# print(num_equal_index(mlist))


# 8. Define a function that takes two lists gl1 and gl2 of integers as parameters. Assume the following:
# a. Each list has unique numbers. (Note: A number can occur in both lists)
# b. Both lists are sorted in increasing order
# Your function should return a list that is sorted in increasing order and contains the numbers in both the lists.
# But if a number appears in both the lists then it should appear only once in the result list.
# Please note that the function should create a new list and not modify the given lists gl1 and gl2.

# Solving this problem with a for loop is very tedious as in for loop you do not have control over changing the indices.

# def merge_lists(gl1, gl2):
#     i = 0  # index into gl1
#     j = 0  # index into gl2
#     rlist = []
#
#     while i < len(gl1) and j < len(gl2):  # As long as there are numbers in both lists
#         if gl1[i] == gl2[j]:
#             # Copy from either of the lists, move forward in both lists
#             rlist.append(gl1[i])
#             i = i + 1
#             j = j + 1
#         elif gl1[i] < gl2[j]:
#             # Copy from gl1 and move forward in gl1
#             rlist.append(gl1[i])
#             i = i + 1
#         else:
#             # Copy from gl2 and move forward in gl2
#             rlist.append(gl2[j])
#             j = j + 1
#
#     # After one of the lists ran out of numbers
#
#     # Copy from gl1 if anything remaining there
#     while i < len(gl1):
#         rlist.append(gl1[i])
#         i = i + 1
#
#     # Copy from gl2 if anything remaining there
#     while j < len(gl2):
#         rlist.append(gl2[j])
#         j = j + 1
#
#     return rlist
#
#
# print(merge_lists([10, 20, 30], [10, 25, 35]))
# print(merge_lists([10, 20, 30], [100, 250, 351]))
# print(merge_lists([], [100, 250, 351]))
# print(merge_lists([10, 20, 30], [10, 20, 30]))


# 9. Define a function that takes two strings gs1 and gs2 as parameters and returns True if the alphabet “a”
# appears an equal number of times in both the strings.

# def count_a1(gs1):
#     i1 = 0
#     for ele in gs1:
#         if ele == "a":
#             i1 = i1 + 1
#     return i1
#
#
# def count_a2(gs2):
#     i2 = 0
#     for ele in gs2:
#         if ele == "a":
#             i2 = i2 + 1
#     return i2
#
#
# def same_a(gs1, gs2):
#     if count_a1(gs1) == count_a2(gs2):
#         return True
#     else:
#         return False
#
#
# print(same_a("Rahul", "Ishan"))


# 10. Define a function that takes a list of integers glist as a parameter and swaps the positions of the minimum and
# the maximum number in the list. Assume that the list has unique integers. Please note that your function should not
# create a new list, instead it should change the given list. Assume there is at least one element in the given list.
# [Note: think if you need to return the changed list or not]
# For example: If glist = [10, 5, -7, 34, 28, 107, -2, 6] then your function should change the given list to
# [10, 5, 107, 34, 28, -7, -2, 6].

# def swap_max_min(glist):
#     max_i = 0  # remember index of max element
#     min_i = 0  # remember index of min element
#
#     i = 0
#     while i < len(glist):
#         if glist[max_i] < glist[i]:
#             max_i = i
#         if glist[min_i] > glist[i]:
#             min_i = i
#
#         i = i + 1
#
#     # Swap the min and max
#     temp = glist[max_i]
#     glist[max_i] = glist[min_i]
#     glist[min_i] = temp
#
#
# mlist = [100, 5, -5, 34, 8, 670]
# swap_max_min(mlist)
# print(mlist)


# 11. Define a function that takes a list of lists glol as parameter.  You may assume that each inner list inside glol is a
# list of integers. For example: [[1, 2], [10, 20], [30, 10], [-4, -5]].
# Your function returns True if at least one list inside glol is sorted in increasing order and at least one list is
# sorted in decreasing order, else it returns False.

# Helper: Checks if given list is in increasing order
# def is_increasing(glist):
#     for i in range(0, len(glist)-1):
#         if glist[i] > glist[i+1]:
#             return False
#     return True
#
#
# # Helper: Checks if the given list is in decreasing order
# def is_decreasing(glist):
#     for i in range(0, len(glist)-1):
#         if glist[i] < glist[i+1]:
#             return False
#     return True
#
#
# # Checks if there is a list in increasing order and there is list in decreasing
# # order
# def one_inc_one_dec(glol):
#     inc = False
#     dec = False
#
#     for l in glol:
#         if is_increasing(l):
#             inc = True  # set to True if there is a list sorted in increasing order
#         if is_decreasing(l):
#             dec = True  # set to True if there is a list sorted in decreasing orderd
#
#     return inc and dec
#
#
# alol = [[10, 20], [10, 40, 30], [1, 8, 5], [100, 20, 3]]
# alol1 = [[20, 10], [10, 40, 30], [1, 8, 5], [100, 20, 3]]
# alol2 = [[10, 20, 1], [10, 40, 30], [1, 18, 50, 0], [100, 200, 3]]
#
# print(one_inc_one_dec(alol))
# print(one_inc_one_dec(alol1))
# print(one_inc_one_dec(alol2))

# 12. Define a function that takes two strings s1 and s2 as parameters and checks if they have the same set of characters
# that occur with the same frequency (you are checking if s1 and s2 are anagrams). For example:
# If s1 = “dirtyroom” and s2 = “dormitory” then it should  return True
# If s1 = “dirty room” and s2 = “dormitory” then it should return False (space is counted as a character)
# If s1 = “too” and s2 = “to” then it should return False.

# def count_freq(gstr, c):  # O(n)
#     count = 0
#     for x in gstr:
#         if c == x:
#             count = count + 1
#
#     return count
#
#
# def check_strings(str1, str2):  # O(n^2)
#
#     if len(str1) != len(str2):
#         return False
#
#     for x in str1:
#         c1 = count_freq(str1, x)  # O(n)
#         c2 = count_freq(str2, x)  # O(n)
#
#         if c1 != c2:
#             return False
#
#     return True
#
#
# print(check_strings("dirtyroom", "dormitory"))
# print(check_strings("washer", "dishwasher"))
# print(check_strings("to", "too"))


# 13. Define a function that takes two strings s1 and s2 as parameters and checks if they have the same set of
# characters but possibly with a different frequency. For example:
# If s1 = “dirtyroom” and s2 = “dormitory” then it should  return True
# If s1 = “dirty room” and s2 = “dormitory” then it should return False (space is counted as a character)
# If s1 = “too” and s2 = “to” then it should return True.

# def contains_char(gstr, c):
#     for x in gstr:
#         if x == c:
#             return True
#
#     return False
#
#
# def check_strings(str1, str2):
#     test1 = False
#     mystory2 = False
#
#     # Check if all characters in str1 are there in str2 and set test1
#     for x in str1:
#         if not contains_char(str2, x):
#             return False
#
#     test1 = True
#
#     # Check if all characters in str2 are
#     # there in str1 and set mystory2
#     for x in str2:
#         if not contains_char(str1, x):
#             return False
#
#     mystory2 = True
#
#     return test1 and mystory2
#
#
# print(check_strings("dirtyroom", "dormitory"))
# print(check_strings("washer", "dishwasher"))
# print(check_strings("to", "too"))
#
# # 14.Define a function that takes a list of lists as a parameter such that each inner list is a list of integers.
# # The function should return a list containing all integers that occur only in one of the inner lists.
#
# # Solution 1
#
#
# # This function puts all integers in inner lists of glol into one big list
# def make_big_list(glol):
#     res = []
#     for gl in glol:
#         for x in gl:
#             res.append(x)
#     return res
#
#
# # Find unique
# def find_unique(glol):
#     big_list = make_big_list(glol)
#     unique_list = []
#
#     for i in range(len(big_list)):
#         unique = True  # Check if number at index i is unique
#         for j in range(len(big_list)):
#             if (i != j) and big_list[i] == big_list[j]:
#                 unique = False
#
#         if unique:  # If number was unique then add to unique_list
#             unique_list.append(big_list[i])
#
#     return unique_list
#
#
# print(find_unique([[10, 20, 30, 12], [10, 40, 30], [40, -10,  60], [20, 40]]))
# print(find_unique([[10, 20, 12, 30], [10, 40, 30, 60], [40, -10, 12, 60], [-10, 20, 40]]))
#
# #-------------------------------#
# # Solution 2
# #-------------------------------#
# #This solution is without breaking it into helper function
# #The broad idea to take every number and check
# def unique(lol):
#     res = []
#     for i in range(len(lol)): #For every inner list
#
#         # For every number in the inner list at index i (by for loop above)
#         for x in lol[i]:
#
#             # Check if it is in any other inner list
#             is_unique = True
#             for j in range(len(lol)):
#                 if i != j:
#                     if x in lol[j]:
#                         is_unique = False
#
#             if is_unique:
#                 res.append(x)
#     return res
#
# lol = [[10, 20, 30, 12], [10, 40, 30], [40, -10, 60], [20, 40]]
# print(unique(lol))
#
# lol = [[10, 20, 12, 30], [10, 40, 30, 60], [40, -10, 12, 60], [-10, 20, 40]]
# print(unique(lol))


