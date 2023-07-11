# Dictionary
# 1. Define a function that takes a list glist that contains unique integers as parameter. The function returns a
# dictionary that has the integers in glist as keys and associates each key with its square. For example:
# If glist =[1, 5, 2, 4, -2] then function returns the dictionary {1: 1, 2: 4, 4: 16, 5: 25, -2: 4}
# [Note: that order can be different as you cannot predict the order in which key-value pairs are stored in dictionary]


# def create_dict(glist):
#     dict = {}
#     for ele in glist:
#         dict[ele] = ele ** 2
#
#     return dict
#
#
# mlist = [1, 5, 2, 4, -2]
# print(create_dict(mlist))


# 2. Let us now generalize problem 1 (given above): Define a function that takes a list glist that contains unique
# integers, and a function func as parameter (Hint: you used this idea in Lab3 for passing compare functions).
# The function func takes an integer as a parameter and returns some value. The function you define should return a
# dictionary that has the integers in glist as keys and associates each key k with func(k), i.e. the value returned
# by func when k is passed as parameter. For example:
# If glist =[1, 5, 2, 4, -2] and func = func2 (defined below) then your function returns the dictionary
# {1: 10, 2: 20, 4: 40, 5: 50, -2: -20} [Note: that order can be different as you cannot predict the order in which
# key-value pairs are stored in dictionary]


# def func(x):
#    return x*10
#
#
# def create_dict(glist):
#     dict = {}
#     for ele in glist:
#         dict[ele] = func(ele)
#
#     return dict
#
#
# mlist = [1, 5, 2, 4, -2]
# print(create_dict(mlist))


# 3. Define a function that takes two dictionaries d1 and d2 as parameters and returns a list of keys that
# appear in only one of the two dictionaries. For example:
#  If d1  = {“a”:1, “b”:3, “c”:4} and d2 = {“b”:6, “c”:4, “d”:5} then your function returns [“a”, “d”]
#  [note: order of elements in the returned list doesn’t matter]


# def func(d1, d2):
#     res = []
#     for k in d1:
#         if not k in d2:
#             res.append(k)
#
#     for k in d2:
#         if not k in d1:
#             res.append(k)
#
#     return res
#
#
# d1 = {"a": 1, "b": 3, "c": 4}
# d2 = {"b": 6, "c": 4, "d": 5}
# print(func(d1, d2))


# 4. Define a function that takes two dictionaries d1 and d2 as parameters and returns a list of keys that appear
# in both the dictionaries.
#  For example: If d1  = {“a”:1, “b”:3, “c”:4} and d2 = {“b”:6, “c”:4, “d”:5} then your function returns [“c”, “b”]
#  [note: order of elements in the returned list doesn’t matter]


# def func(d1, d2):
#     res = []
#     for k in d1:
#         if k in d2:
#             res.append(k)
#
#     return res
#
#
# d1 = {"a": 1, "b": 3, "c": 4}
# d2 = {"b": 6, "c": 4, "d": 5}
# print(func(d1, d2))


# 5. Define a function that takes a dictionary d1 as a parameter and returns a list of lists such that each inner
# list contains keys that have the same associated value in d1.
#  For example:
#  If d1  = {“a”:1, “b”:3, “c”:4, “d”:3, “e”:1, “f”: 3} then your function returns [[“a”, “e”], [“b”, “d”, “f”], [“c”]].
#  [note: order of elements in the returned list and inner lists doesn’t matter]


# def func(gdict):
#     res = []
#     for k in gdict:
#         check = False
#         for ilist in res:
#             if gdict[ilist[0]] == gdict[k]:
#                 ilist.append(k)
#                 check = True
#
#         if not check:
#             res.append([k])
#
#     return res
#
#
# d1 = {"a": 1, "b": 3, "c": 4, "d": 3, "e": 1, "f": 3}
# print(func(d1))



# Linked Lists

# 1. Define a function that takes the head of a linked list hnode and integers val1 and val2 as parameters.
# Your function should replace every occurrence of val1 as data in a given linked list by val2.
# Assume that the data stored in each node is an integer.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def build_ll(glist):
#     head = None
#     i = 0
#     n = 0
#     while i < len(glist):
#         new_node = Node(glist[i])
#         if head == None:
#             head = new_node
#             n = new_node
#         else:
#             n.next = new_node
#             n = n.next
#         i = i + 1
#
#     return head
#
#
# def print_ll(head):
#     n = head
#     while n is not None:
#         print(n.data, end="-->")
#         n = n.next
#
#     print("\n")
#
#
# def replace_val(hnode, val1, val2):
#     n = hnode
#
#     while n is not None:
#         if n.data == val1:
#             n.data = val2
#         n = n.next
#
#
# h1 = build_ll([10, 4, 6, 23, -5, 4])
# replace_val(h1, 4, 7)
# print_ll(h1)


# 2. Define a function that takes the head of a linked list as a parameter.
# Assume that the data stored in each node is an integer.
# Your function returns the maximum data in the linked list. For example:
# 	The given linked list is:  10 → 15 → 2→ 30 → -10 → 5 then it should return 30.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def build_ll(glist):
#     head = None
#     i = 0
#     n = 0
#     while i < len(glist):
#         new_node = Node(glist[i])
#         if head is None:
#             head = new_node
#             n = new_node
#         else:
#             n.next = new_node
#             n = n.next
#         i = i + 1
#
#     return head
#
#
# def print_ll(head):
#     n = head
#     while n is not None:
#         print(n.data, end="-->")
#         n = n.next
#
#     print("\n")
#
#
# def find_max_ll(head):
#     if head is not None:
#         max = head.data
#     else:
#         return None
#
#     n = head.next
#     while n is not None:
#         if max < n.data:
#             max = n.data
#         n = n.next
#
#     return max
#
#
# head = build_ll([10, 4, 70, 8])
# print_ll(head)
# print(find_max_ll(head))


# 3. Define a function that takes the head of a linked list as a parameter. Assume that the data stored in each node
# is an integer. Your function should return the sum of all the integers stored as data in the nodes of the linked list.
# For example: The given linked list is:  10 → 15 → 2→ 30 → -10 → 5 then it should return  52

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def build_ll(glist):
#     head = None
#     i = 0
#     n = 0
#     while i < len(glist):
#         new_node = Node(glist[i])
#         if head is None:
#             head = new_node
#             n = new_node
#         else:
#             n.next = new_node
#             n = n.next
#         i = i + 1
#
#     return head
#
#
# def print_ll(head):
#     n = head
#     while n is not None:
#         print(n.data, end="-->")
#         n = n.next
#
#     print("\n")
#
#
# def find_sum_ll(head):
#     sum = 0
#     n = head
#
#     while n is not None:
#         sum = sum + n.data
#         n = n.next
#
#     return sum
#
#
# head = build_ll([10, 4, 5, 6])
# print_ll(head)
# print(find_sum_ll(head))


# 4. Define a function insert_before that takes the head of a linked list, and two integers val_before and val as
# parameters. Assume that the data stored in each node is an integer. Your function should insert a new node with
# data as val such that the next node of the new node is the first node in the given  linked list with data as
# val_before. You may assume that a node with data val_before will always exist in the given linked list. For example:
# If the given head is reference to head node the linked list: 10 → 15 → 2→ 30 → 10 → 5, val_before is 10 and val is 20,
# then after adding the node the linked list should be 20 → 10 → 15 → 11→ 2→ 30 → 10 → 5.
# If the given head is reference to head node the linked list:
# 10 → 15 → 2→ 30 → -10 → 5, val_before is 2 and val is 11, then after adding the node the linked list should
# be 10 → 15 → 11→ 2→ 30 → -10 → 5.


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def build_ll(glist):
#     head = None
#     i = 0
#     n = 0
#     while i < len(glist):
#         new_node = Node(glist[i])
#         if head is None:
#             head = new_node
#             n = new_node
#         else:
#             n.next = new_node
#             n = n.next
#         i = i + 1
#
#     return head
#
#
# def print_ll(head):
#     n = head
#     while n is not None:
#         print(n.data, end="-->")
#         n = n.next
#
#     print("\n")
#
#
# def insert_before(head, val_before, val):
#     prev = None
#     n = head
#     while n is not None:
#         if n.data == val_before:
#             new_node = Node(val)
#             if prev is None:
#                 new_node.next = n
#                 head = new_node
#             else:
#                 new_node.next = prev.next
#                 prev.next = new_node
#             break
#
#         prev = n
#         n = n.next
#
#     return head
#
#
# h1 = build_ll([10, 5, 7, 10, 28, 6])
# print_ll(h1)
# h1 = insert_before(h1, 28, 20)
# print_ll(h1)


# 1. Define a function that takes a list of integers glist as parameter and deletes some elements from glist such
# that only one copy of each number in the given list is retained when your function returns. Your function modifies
# the given list and hence does not return the modified list. It does not matter which copies of an integer are deleted
# from the given list. You can assume len(glist) > 0. For example:
# If glist = [0, 5, 2, 5, 2, 7, 8, 1], then your function should change glist to [0, 5, 2, 7, 8, 1].
# If glist = [1, 5], then your function should not change the given list.
# NOTE: Your function should modify the given list like quicksort/mergesort sort the given list and do not return
# anything.
# Runtime of your function should be O(n) where n is the len(glist).

# def func(glist):
#     d = {}
#
#     # Add all values to dictionary and keep the count as value
#     for k in glist:
#         if k in d:
#             d[k] = d[k] + 1
#         else:
#             d[k] = 1
#
#     # Remove all elements from glist one at a time from the end
#     # pop is O(1) so loop below will be O(n) removing from the front will make it O(n^2)
#     for i in range(len(glist)):
#         glist.pop()
#
#     # Add them back only once
#     for k in d:
#         if d[k] > 0:
#             glist.append(k)
#             d[k] = d[k] - 1


