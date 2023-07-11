#Author: Vasanta
#Date: 02/25/2023
#Purpose: Mergesort

#Merge:
#Input: Two sorted lists
#Output: A big sorted list containing elements from given lists

#glist = [5, 8, 12, 71, 72, 78, 231, 324, 403, -6, 7, 18, 36, 47, 78, 123]
#from index p to q is sorted and from index q+1 to r is sorted
#In this example p = 0, q = 8, r = 15

def merge(glist, p, q, r):
    list1 = glist[p:q+1]
    list2 = glist[q+1:r+1]

    i = 0 #index into list1
    j = 0 #index into list2
    k = p

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            glist[k] = list1[i]
            i = i + 1
        else: #list2[j] < list1[i]
            glist[k] = list2[j]
            j = j + 1

        k = k + 1

    while j < len(list2): #Case where list1 has no more elements
        glist[k] = list2[j]
        j = j + 1
        k = k + 1

    while i < len(list1): #Case where list2 has no more element
        glist[k] = list1[i]
        i = i + 1
        k = k + 1


# mlist = [5, 8, 12, 71, 72, 78, 231, 324, 403, -6, 7, 18, 36, 47, 78, 123]
# merge(mlist, 0, 8, 15)
# print(mlist)


def mergesort(glist, p=0, r=None):
    if r == None:
        r = len(glist) - 1

    if p >= r: #basecase
        return

    mid = (p+r)//2
    mergesort(glist, p, mid) #sorts the first half
    mergesort(glist, mid+1, r) #sorts the second half

    merge(glist, p, mid, r)

mlist = [89, 23, -7, 45, 8, 4, 123, 3]
mergesort(mlist)
print(mlist)