# Author: Rahul Gupta
# Date: 03/01/2023
# Purpose: Randomized Quicksort Algorithm

from random import randint


def partition(the_list, p, r, compare_func):

    # choose a random index in the range from p to r, inclusive, and swap the item at this index with the item in
    # the_list[r]
    pivot_index = randint(p, r)
    the_list[pivot_index], the_list[r] = the_list[r], the_list[pivot_index]

    pivot = the_list[r]
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


# define the comparison function
def compare_func(a, b):
    if a < b:
        return True
    else:
        return False


# create a list of integers to sort
my_list = [9, 3, 6, 2, 8, 5, 1, 4, 7]

# sort the list using randomized quicksort
sorted_list = sort(my_list, compare_func)

# print the sorted list
print(sorted_list)
