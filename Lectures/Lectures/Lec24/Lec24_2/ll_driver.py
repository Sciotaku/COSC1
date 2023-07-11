from Lec24_2.node import Node

n1 = Node(10)
n2 = Node(4)
n3 = Node(7)
n4 = Node(-5)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1

new_node = Node(11)
new_node.next = head
head = new_node