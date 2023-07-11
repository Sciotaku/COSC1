from time import time

def find_min_i(k, glist):
    min_i = k
    for i in range(k, len(glist)):
        if glist[min_i] > glist[i]:
            min_i = i

    return min_i


def selection_sort(glist):
    start = 0
    while start < len(glist):
        min_index = find_min_i(start, glist)

        temp = glist[min_index]
        glist[min_index] = glist[start]
        glist[start] = temp

        start = start + 1

def merge(glist, p, q, r):
    list1 = glist[p:q+1]
    list2 = glist[q+1:r+1]

    i = 0
    j = 0
    k = p

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            glist[k] = list1[i]
            i = i + 1
        else: #list1[i] > list2[j]
            glist[k] = list2[j]
            j = j + 1

        k = k + 1

    while j < len(list2): #More elements remaining in list2
        glist[k] = list2[j]
        j = j + 1
        k =  k + 1

    while i < len(list1): #Elements remaining in list1
        glist[k] = list1[i]
        i = i + 1
        k = k + 1


# mlist = [-6, 4, 9, 14, 27, 78, 89, 105, 7, 8, 15, 38, 67, 69, 105, 143, 150]
# merge(mlist, 0, 7, 16)
# print(mlist)

def mergesort(glist, p=0, r=None):
    if r == None:
        r = len(glist) - 1

    if p >= r:
        return

    mid = (p+r) // 2
    mergesort(glist, p, mid)
    mergesort(glist, mid+1, r)

    merge(glist, p, mid, r)

#Generate a reverse list
mlist = []
i = 100000
while i >= 1:
    mlist.append(i)
    i = i - 1

t1 = time()
selection_sort(mlist)
#mergesort(mlist)
t2 = time()

print(t2 - t1)
