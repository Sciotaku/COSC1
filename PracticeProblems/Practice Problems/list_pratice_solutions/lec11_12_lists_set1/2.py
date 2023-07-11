# Define a function that takes a list of integers
# glist as parameter and prints the numbers at even index.

def print_even_indx1(glist):
    for i in range(len(glist)):
        if i % 2 == 0:
            print(glist[i])


def print_even_indx2(glist):
    i = 0
    while i < len(glist):
        if i % 2 == 0:
            print(glist[i])

        i = i + 1

glist = [1, 4, 5, 20, 2, 12, 87]
print("Solution 1:")
print_even_indx1(glist)

print("Solution 2:")
print_even_indx2(glist)