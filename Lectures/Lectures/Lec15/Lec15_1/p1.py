#Author: Vasanta
#Date: 02/06/2023 and 02/08/2023
#Purpose: List of lists example

# mlist = [[13, 2], [23, -56, 87], [37]]
# print(mlist[1][1])
#
#Define a function that takes a list of lists, glol, as a parameter
#and each inner has integers as elements. Your function should
#return the maximum integer that appears in any of
#the inner lists as an element.

#Solution1: Treat as if all numbers are in one list

#Helper function: Makes one big list of all number in given list of lists (glol)

def make_big_list(glol):
    big_list = []
    i = 0
    while i < len(glol):
        inner_list = glol[i]

        for ele in inner_list:
            big_list.append(ele)

        i = i + 1

    return big_list

res = make_big_list([[13, 2], [23, -56, 87], [37]])
print(res)

#Helper function: Given a list of integers returns the maximum number
def find_max(glist):
    max = glist[0]

    for ele in glist:
        if ele > max:
            max = ele

    return max

#Main function: Find the max among all numbers that appear in inner lists

def max_of_lol(glol):
    big_list = make_big_list(glol)
    max = find_max(big_list)
    return max

mlol = [[13, 2], [23, -56, 87], [37, 27]] #[[13], [2, 23, -56], [87], [37, 27]]
print(max_of_lol(mlol))

#Solution 2

#Main function: find the max among the max numbers from each of the inner lists
def max_of_all_maxnumbers(glol):
    max = find_max(glol[0])
    max_inner_list_index = 0

    i = 1
    while i < len(glol):
        local_max = find_max(glol[i])
        if max < local_max:
            max = local_max
            max_inner_list_index = i

        i = i + 1

    return max_inner_list_index

mlol = [[13, 2], [23, -56, 87], [37, 27, -45], [34, 12, 8]]
print(max_of_all_maxnumbers(mlol))