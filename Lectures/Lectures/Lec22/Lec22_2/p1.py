#Author: Vasanta
#Date: 02/22/2023
#Purpose: Building lists recursively

#Define a recursive function that takes a list of
#positive integers and returns the sum of all even numbers in
#the list.

# def sum_evens_list(glist, i=0):
#     if i == len(glist):
#         return 0
#
#     res = sum_evens_list(glist, i+1)
#
#     if glist[i] % 2 == 0:
#         res = res + glist[i]
#
#     return res
#
# print(sum_evens_list([10, 6, 7, 3, 2]))

def create_evens_list(glist, i=0):
    if i == len(glist):
        return []

    res_list = create_evens_list(glist, i+1)

    if glist[i] % 2 == 0:
        res_list.append(glist[i])

    return res_list

print(create_evens_list([10, 6, 7, 3, 2]))
