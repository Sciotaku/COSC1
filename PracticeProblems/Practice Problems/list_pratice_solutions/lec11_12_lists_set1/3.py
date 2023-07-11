# Define a function that takes a list of integers glist that is
# sorted (in increasing order) and an integer n as parameters
# and inserts n into glist in such a way that glist remains sorted.

def insert_n(glist, n):

    for i in range(len(glist)):
        if glist[i] >= n: # come out of loop when you find the position for n
            glist.insert(i, n)
            break

    if i == len(glist) - 1:
        glist.append(n)

mlist = [10, 29, 30, 45, 58]
insert_n(mlist, 84)
print(mlist)