#Author: Vasanta
#Date: 02/25/2023
#Purpose: Mergesort

#glist = [-6, 4, 9, 14, 27, 78, 89, 105, 7, 8, 15, 38, 67, 69, 105, 143, 150]
#Between index p and q is the first sorted part, and between index q+1 and r
#we have second sorted part.
#In this example: p = 0, q = 7, r = 16

#list1 = glist[p:q+1]
#list2 = glist[q+1:r+1]

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



mlist = [45, 8, 10, 34, -7, -11, 25, 99]
mergesort(mlist)
print(mlist)