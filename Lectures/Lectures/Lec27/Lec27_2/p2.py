#Author: Vasanta
#Date: 03/06/2023
#Purpose: Linked list example

from Lec27_2.node import Node

def build_ll(glist):
    head = None
    i = 0
    while i < len(glist):
        new_node = Node(glist[i])
        if head == None:
             head = new_node
             n = new_node
        else:
            n.next = new_node
            n = n.next
        i = i + 1

    return head

def print_ll(head):
    n = head

    while n != None:
        print(n.data, end="-->")
        n = n.next

    print("\n")

def insert_after(head, val_after, val):
    new_node = Node(val)
    n = head
    while n != None:
        if n.data == val_after:
            new_node.next = n.next
            n.next  = new_node

        n = n.next

h1 = build_ll([5, 7, 8, 4, 3, 5, 11, 5])
print_ll(h1)
insert_after(h1, 5, 12)
print_ll(h1)