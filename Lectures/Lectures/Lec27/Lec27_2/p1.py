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

def delete_val(head, val):
    n = head
    prev = None

    while n != None:
        if n.data == val:
            if prev != None:
                prev.next = n.next #bypasses the node n
            else:
                head = n.next

        prev = n
        n = n.next

    return head

h1 = build_ll([5, 7, 8, 4, 3, 5, 11, 5])
print_ll(h1)
h1 = delete_val(h1, 5)
print_ll(h1)