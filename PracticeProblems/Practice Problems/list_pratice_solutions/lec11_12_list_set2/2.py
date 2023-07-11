#Define a function that takes a list of integers glist as input
#and returns a list containing those numbers in
#glist that are equal to the index at which they appear
#in glist.

def match_num_index1(glist):
    rlist = []
    i = 0
    while i < len(glist):
        if i == glist[i]:
            rlist.append(i)
        i = i + 1
        
    return rlist

print(match_num_index1([0, 13, 2, 33, 5, 57, 36, 7]))
print(match_num_index1([10, 30, 20]))

def match_num_index2(glist):
    rlist = []
    for i in range(len(glist)):
        if i == glist[i]:
            rlist.append(i)

    return rlist

print(match_num_index2([0, 13, 2, 33, 5, 57, 36, 7]))
print(match_num_index2([10, 30, 20]))