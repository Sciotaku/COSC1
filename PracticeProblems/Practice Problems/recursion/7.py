def find_min(glist, i = 0):
    if i == len(glist) - 1:
        return glist[-1]

    m = find_min(glist, i + 1)
    if m < glist[i]:
        return m
    else:
        return glist[i]


print(find_min([1, 4, 7, -1, 0, 45, 10]))
print(find_min([1]))
print(find_min([1, 1, 1]))
