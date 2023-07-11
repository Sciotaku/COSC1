#There are many ways to solve this problem.
#Here I am giving two solutions.

#Solution 1

#This function puts all integers in inner lists of glol
#into one big list
def make_big_list(glol):
    res = []
    for gl in glol:
        for x in gl:
            res.append(x)
    return res

#Find unique
def find_unique(glol):
    big_list = make_big_list(glol)
    unique_list = []

    for i in range(len(big_list)):
        unique = True #Check if number at index i is unique
        for j in range(len(big_list)):
            if (i != j) and big_list[i] == big_list[j]:
                unique = False

        if unique: #If number was unique then add to unique_list
            unique_list.append(big_list[i])

    return unique_list

print(find_unique([[10, 20, 30, 12], [10, 40, 30], [40, -10,  60], [20, 40]]))
print(find_unique([[10, 20, 12, 30], [10, 40, 30, 60], [40, -10, 12, 60], [-10, 20, 40]]))

#-------------------------------#
# Solution 2
#-------------------------------#
#This solution is without breaking it into helper function
#The broad idea to take every number and check
def unique(lol):
    res = []
    for i in range(len(lol)): #For every inner list

        # For every number in the inner list at index i (by for loop above)
        for x in lol[i]:

            # Check if it is in any other inner list
            is_unique = True
            for j in range(len(lol)):
                if i != j:
                    if x in lol[j]:
                        is_unique = False

            if is_unique:
                res.append(x)
    return res

lol = [[10, 20, 30, 12], [10, 40, 30], [40, -10, 60], [20, 40]]
print(unique(lol))

lol = [[10, 20, 12, 30], [10, 40, 30, 60], [40, -10, 12, 60], [-10, 20, 40]]
print(unique(lol))

