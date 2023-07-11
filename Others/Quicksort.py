def partition(the_list, p, r, compare_func):
    pivot = the_list[r]
    i = p - 1

    for j in range(p, r):
        if compare_func(the_list[j], pivot) <= 0:
            i = i + 1
            temp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = temp

    temp = the_list[i+1]
    the_list[i+1] = the_list[r]
    the_list[r] = temp

    return i+1


def quicksort(the_list, p, r, compare_func):
    if p >= r:  # base case
        return

    if p < r:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q-1, compare_func)
        quicksort(the_list, q+1, r, compare_func)


def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list)-1, compare_func)
    return the_list


def compare_func(x, y):
    return x - y


mlist = [5, 8, 12, 71, 72, 78, 231, 324, 403, -6, 7, 18, 36, 47, 78, 123]
print(sort(mlist, compare_func))

