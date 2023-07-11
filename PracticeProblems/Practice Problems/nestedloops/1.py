# Define a function that takes a list of lists glol as parameter.
# You may assume that each inner list inside glol is a list of
# integers. For example: [[1, 2], [10, 20], [30, 10], [-4, -5]].
# Your function returns True if at least one list inside glol is
# sorted in increasing order and at least one list is sorted in decreasing order, else it returns False.

#Helper: Checks if given list is in increasing order
def is_increasing(glist):
    for i in range(0, len(glist)-1):
        if glist[i] > glist[i+1]:
            return False
    return True
#Helper: Checks if the given list is in decreasing order
def is_decreasing(glist):
    for i in range(0, len(glist)-1):
        if glist[i] < glist[i+1]:
            return False
    return True

#Checks if there is a list in increasing order and there is list in decreasing
#order
def one_inc_one_dec(glol):
    inc = False
    dec = False

    for l in glol:
        if is_increasing(l):
            inc = True #set to True if there is a list sorted in increasing order
        if is_decreasing(l):
            dec = True #set to True if there is a list sorted in decreasing orderd

    return (inc and dec)

alol = [[10, 20], [10, 40, 30], [1, 8, 5], [100, 20, 3]]
alol1 = [[20, 10], [10, 40, 30], [1, 8, 5], [100, 20, 3]]
alol2 = [[10, 20, 1], [10, 40, 30], [1, 18, 50, 0], [100, 200, 3]]

print(one_inc_one_dec(alol))
print(one_inc_one_dec(alol1))
print(one_inc_one_dec(alol2))