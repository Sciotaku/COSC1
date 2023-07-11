def find_evens(n, k):
    if k == 0:
        return []

    if (n+1) % 2 == 0:
        l = find_evens(n+1, k-1)
        l.insert(0, n+1)
    else:
        l = find_evens(n+1, k)

    return l

print(find_evens(10, 4))
print(find_evens(11, 4))
print(find_evens(5, 0))
print(find_evens(0, 3))