#5
def swap_max_min(glist):
    max_i = 0 #remember index of max element
    min_i = 0 #remember index of min element

    i = 0
    while i < len(glist):
        if glist[max_i] < glist[i]:
            max_i = i
        if glist[min_i] > glist[i]:
            min_i = i

        i = i + 1

    #Swap the min and max
    temp = glist[max_i]
    glist[max_i] = glist[min_i]
    glist[min_i] = temp

mlist = [100, 5, -5, 34, 8, 670]
swap_max_min(mlist)
print(mlist)