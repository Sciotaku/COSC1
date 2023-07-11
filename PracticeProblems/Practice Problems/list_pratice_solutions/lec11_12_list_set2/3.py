# Solving this problem with a for loop is very tedious as in a
# for loop you do not have control over changing the indices.

def merge_lists(gl1, gl2):
    i = 0  # index into gl1
    j = 0  # index into gl2
    rlist = []

    while i < len(gl1) and j < len(gl2):  # As long as there are numbers in both lists
        if gl1[i] == gl2[j]:
            # Copy from either of the lists, move forward in both lists
            rlist.append(gl1[i])
            i = i + 1
            j = j + 1
        elif gl1[i] < gl2[j]:
            # Copy from gl1 and move forward in gl1
            rlist.append(gl1[i])
            i = i + 1
        else:
            # Copy from gl2 and move forward in gl2
            rlist.append(gl2[j])
            j = j + 1

    # After one of the lists ran out of numbers

    # Copy from gl1 if anything remaining there
    while i < len(gl1):
        rlist.append(gl1[i])
        i = i + 1

    # Copy from gl2 if anything remaining there
    while j < len(gl2):
        rlist.append(gl2[j])
        j = j + 1

    return rlist

# print(merge_lists([10, 20, 30], [10, 25, 35]))
# print(merge_lists([10, 20, 30], [100, 250, 351]))
# print(merge_lists([], [100, 250, 351]))
# print(merge_lists([10, 20, 30], [10, 20, 30]))
