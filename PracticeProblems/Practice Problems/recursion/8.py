def find_min_i(glist, i = 0):
    if i == len(glist) - 1:
        return i

    m_i = find_min_i(glist, i + 1)
    if glist[m_i] < glist[i]:
        return m_i
    else:
        return i


print(find_min_i([1, 4, 7, -1, 0, 45, -10]))
print(find_min_i([1]))
print(find_min_i([1, 1, 1]))