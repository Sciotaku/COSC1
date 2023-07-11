# Author: Rahul Gupta
# Date: 02/21/2023
# Purpose: Perform binary search on a sorted list of random numbers.

from random import randint

# Perform binary search for key on the sublist of the_list
# starting at index left and going up to and including index right.
# If key appears in the_list, return the index where it appears.
# Otherwise, return None.
# Requires the_list to be sorted.


def binary_search(the_list, key, left=None, right=None):
    # If using the default parameters, then search the entire list.
    if left == None and right == None:
        left = 0
        right = len(the_list) - 1

    # First, we check if the sublist is empty.
    if left > right:
        return None

    # We then compute the midpoint of the sublist.
    mid_point = (left + right) // 2  # returns an integer and ignores the decimal part

    # If the key is found, return its index.
    if the_list[mid_point] == key:
        return mid_point

    # If the key is less than the midpoint, search the left half of the sublist.
    elif key < the_list[mid_point]:
        right = mid_point - 1
        return binary_search(the_list, key, left, right)

    # If the key is greater than the midpoint, search the right half of the sublist.
    elif key > the_list[mid_point]:
        left = mid_point + 1
        return binary_search(the_list, key, left, right)


# Driver code for binary search.
n = int(input("How many items in the list? "))

# Make a list of n random ints.
i = 0
the_list = []
while i < n:
    the_list.append(randint(0, 1000))
    i += 1

# Binary search wants a sorted list.
the_list = sorted(the_list)
print("The list: " + str(the_list))

while True:
    key = input("What value to search for? ('?' to see the list, 'q' to quit): ")

    if key == "?":
        print("The list: " + str(the_list))
    elif key == "q":
        break
    else:
        key = int(key)
        index = binary_search(the_list, key)
        if index == None:
            print(str(key) + " not found")
        else:
            print(str(key) + " found at index " + str(index))
