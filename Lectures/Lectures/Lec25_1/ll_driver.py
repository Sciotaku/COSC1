from Lectures.Lec25_1.node import Node


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

h1 = build_ll([5, 8, 23, 7, -4])
print_ll(h1)

def ll_is_increasing(head):
    n = head

    while n.next != None:
        if n.data > n.next.data:
            return False

        n = n.next

    return True

h2 = build_ll([3, 6, 8, 9])
print(ll_is_increasing(h2))