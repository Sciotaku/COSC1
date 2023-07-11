#Author: Vasanta
#Date: 02/06/2023 and 02/08/2023
#Purpose: List of lists example

# mlist = [[13, 2], [23, -56, 87], [37, 12]]
# print(mlist[1][1])
#
#Define a function that takes a list of lists, glol, as a parameter
#and each inner has integers as elements. Your function should
#return the maximum integer that appears in any of
#the inner lists as an element.

#Solution 1: Make a big list of all numbers and find the max in the big list

#Helper function: Make a list of all numbers that appear in inner lists of
#given list of lists

def make_big_list(glol):
    big_list = []
    i = 0
    while i < len(glol):
        inner_list = glol[i]
        for ele in inner_list:
            big_list.append(ele)

        i = i + 1
    return big_list

big_list = make_big_list([[13, 2], [23, -56, 87], [37, 12]]) #[[13], [2, 23, -56], [87], [37], [12]]
print(big_list)

#Helper function: Find the max integer in the given list
def find_max(glist):
    max = glist[0]

    for ele in glist:
        if max < ele:
            max = ele

    return max

#Main function
def max_in_lol(glol):
    big_list = make_big_list(glol)
    max = find_max(big_list)
    return max

mlol = [[13, 2], [23, -56, 87], [37, 12]]
max = max_in_lol(mlol)
print(max)

#Solution 2: Find local max of each inner list and find the max among those

def find_max_of_allmaxnumbers(glol):
    max = find_max(glol[0])
    max_inner_l_index = 0

    # i = 0
    # while i < len(glol):
    for i in range(len(glol)): #[0, 1, 2]
        inner_list = glol[i]
        local_max = find_max(inner_list)

        if max < local_max:
            max = local_max
            max_inner_l_index = i

    #    i = i + 1

    return max_inner_l_index

max_i = find_max_of_allmaxnumbers([[13, 2], [23, -56, 87], [37, 212]])
print(max_i)
