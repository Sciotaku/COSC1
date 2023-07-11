#Define a function that takes a list of integers glist as parameter and prints
#the even numbers in glist.

def print_even1(glist):
    for x in glist:
        if x % 2 == 0:
            print(x)


def print_even2(glist):
    i = 0
    while i < len(glist):
        if glist[i] % 2 == 0:
            print(glist[i])

        i = i + 1

glist = [1, 4, 5, 20, 2, 12, 87]
print("Solution 1:")
print_even1(glist)

print("Solution 2:")
print_even2(glist)