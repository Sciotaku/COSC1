# Define a function that takes a list of integers glist as
# parameter and returns True if the list is either sorted in
# decreasing or increasing order. Otherwise, it returns False.

def check_ordered1(glist):
    # These two variables keep track if the list is sorted in increasing or
    # decreasing order

    is_increasing = True
    is_decreasing = True

    i = 0
    while i < len(glist) - 1:
        if glist[i] < glist[i + 1]:
            is_decreasing = False
        elif glist[i] > glist[i + 1]:
            is_increasing = False

        i = i + 1

    # If both are False then return False otherwise return True
    return (is_decreasing or is_increasing)

print(check_ordered1([10, 20, 30, 40, 50]))
print(check_ordered1([50, 40, 30, 20, 10]))
print(check_ordered1([4, 4, 4, 4, 4]))
print(check_ordered1([10, 45, 55, 89, 12]))
print("------------------")

def check_ordered2(glist):

    #These two variables keep track if the list is sorted in increasing or
    #decreasing order

    is_increasing = True
    is_decreasing = True

    for i in range(len(glist) - 1):
        if glist[i] < glist[i+1]:
            is_decreasing = False
        elif glist[i] > glist[i+1]:
            is_increasing = False

    # If both are False then return False otherwise return True
    return (is_decreasing or is_increasing)

print(check_ordered2([10, 20, 30, 40, 50]))
print(check_ordered2([50, 40, 30, 20, 10]))
print(check_ordered2([4, 4, 4, 4, 4]))
print(check_ordered2([10, 45, 23, 89, 12]))