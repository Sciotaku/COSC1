# Author: Rahul Gupta
# Date: 2/24/2023
# Purpose: Quicksort Algorithm


def partition(the_list, p, r, compare_func):

    # We chose the last element as the pivot in the quicksort algorithm.
    pivot = the_list[r]

    # Then set the index of the smaller element to i
    i = p - 1

    # We loop through all the elements from p to r-1.
    for j in range(p, r):

        # If the current element is less than or equal to the pivot,
        # swap it with the element at index i and increment i.
        if compare_func(the_list[j], pivot):
            i = i + 1
            temp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = temp

    # Swap the pivot element with the element at index i+1.
    swap = the_list[i + 1]
    the_list[i + 1] = the_list[r]
    the_list[r] = swap

    # Return the index of the pivot element.
    return i + 1


def quicksort(the_list, p, r, compare_func):
    # Base case
    if p >= r:
        return

    # Partition the list and sort the two sub-lists recursively.
    if p < r:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q - 1, compare_func)
        quicksort(the_list, q + 1, r, compare_func)


# Function to sort the_list using quicksort and return the sorted list.
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)
    return the_list
