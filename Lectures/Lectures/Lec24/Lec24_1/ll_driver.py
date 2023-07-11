from Lec24_1.node import Node

n1 = Node(5)
n2 = Node(4)
n3 = Node(1)
n4 = Node(10)
n5 = Node(-2)

head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

new_n = Node(7)
new_n.next = head
head = new_n