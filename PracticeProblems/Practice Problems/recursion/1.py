def is_sorted(glist, i = 0):
    #Base case: Empty list or a list with only
    #one element
    if i == len(glist) or i == len(glist) - 1:
        return True

    if glist[i] <= glist[i+1]:
        return is_sorted(glist, i + 1)
    else:
        return False

print(is_sorted([10, 20, 30, 40, 50, 60]))
print(is_sorted([10, 20, 3, 40, 50, 60]))
print(is_sorted([10, 20, 30, 40, 50, 6]))
print(is_sorted([]))
print(is_sorted([3]))

