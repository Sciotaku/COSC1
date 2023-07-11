# Author: Rahul Gupta
# Date: 03/06/2023
# Purpose: Linked list examples

from Lectures.Lec25_1.node import Node


# def build_ll(glist):
#     head = None
#     i = 0
#     while i < len(glist):
#         new_node = Node(glist[i])
#         if head == None:
#              head = new_node
#              n = new_node
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
#
#     while n != None:
#         print(n.data, end="-->")
#         n = n.next
#
#     print("\n")
#
#
# def delete_node(head, val):
#     n = head
#     prev = None
#     while n!= None:
#         if n.data == val:
#             if prev != None:
#                 prev.next = n.next  # bypass the node n
#             else:
#                 head = n.next
#
#         prev = n
#         n = n.next
#
#     return head
#
#
# h1 = build_ll([5, 7, 4, 5, 14, 3])
# print_ll(h1)
# h1 = delete_node(h1, 5)
# print_ll(h1)


# def build_ll(glist):
#     head = None
#     i = 0
#     while i < len(glist):
#         new_node = Node(glist[i])
#         if head == None:
#              head = new_node
#              n = new_node
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
#
#     while n != None:
#         print(n.data, end="-->")
#         n = n.next
#
#     print("\n")
#
#
# def insert_after(head, val_after, val):
#     new_node = Node(val)
#     n = head
#
#     while n != None:
#         if n.data == val_after:
#             new_node.next = n.next
#             n.next = new_node
#
#         n = n.next
#
#
# h1 = build_ll([5, 7, 4, 8, 12, 5])
# print_ll(h1)
# insert_after(h1, 4, 11)
# print_ll(h1)


# Example of runtime analysis
# def func1(n):
#     i = 0
#     while i < n:
#         print(i)
#         i += 1
#
#
# def func2(n):  # (a+a)*n + (b + b), O(n)
#     i = 0
#     while i < n:
#         print(i)
#         i = i + 1
#
#     i = 0
#     while i < n:
#         print(i)
#         i += 1
#
#
# def func3(n):  # a*n + b, O(n)
#     i = 0
#     while i < n:
#         if i % 2 == 0:
#             print(i)
#         i = i + 1
#
#
# def func4(n):  # b, O(1)
#     i = 0
#     while i < n:
#         i = i + 1
#
#
# def func5(n):  # O(n^2)
#     i = 0
#     while i < n:
#         j = 0
#         while j < n:
#             print(i, j)
#             j = j + 1
#
#         i = i + 1

