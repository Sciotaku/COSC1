# 1
def even_list1(glist):
    rlist = []
    i = 0
    while i < len(glist):
        if glist[i] % 2 == 0:
            rlist.append(glist[i])

        i = i + 1

    return rlist


print(even_list1([10, 4, 5, 3, 8]))
print(even_list1([11, 43, 5, 3]))


def even_list2(glist):
    rlist = []

    for ele in glist:
        if ele % 2 == 0:
            rlist.append(ele)

    return rlist


print(even_list2([10, 4, 5, 3, 8]))
print(even_list2([11, 43, 5, 3]))
