#There are many ways to solve this problem.
#Here I am giving two solutions.
#-----------------#
# Solution 1
#-----------------#
#This function finds the length of number with
#max digits from the given list.

#Helper function to find number with max digits
def find_longest_number_length(glist):
    longest = glist[0]

    for x in glist:

        #To find a length of a number convert it into string using
        #Python built-in str function and then get the length
        if len(str(x)) > len(str(longest)):
            longest = x

    return len(str(longest))

#Main function that splits by problem definition
def categorize(glist):
    if len(glist) == 0:
        return []

    longlen = find_longest_number_length(glist)
    print(longlen)
    res = []
    #res is a list of lists
    #create one inner list for each length from 1 to
    #length of the longest length
    for i in range(longlen):
        res.append([])

    for x in glist:
        k = len(str(x))
        # k-1 because number with 1 digit will be in list a index 0
        # 2 digits numbers will be in list at index 1 and so on
        res[k-1].append(x)

    #Delete empty lists
    i = 0
    while i < len(res):
        if len(res[i]) == 0:
            del res[i]
        else:
            i = i + 1

    return res

my_l = [1000, 1, 2, 2, 9, 2300, 10000, 3, 12000]
print(categorize(my_l))
print(categorize([]))

#-----------------#
# Solution 2
#-----------------#
#In this solution we only create an innerlist
#when required.

#Find the inner list to which x can be inserted.
#If such a list doesn't exist then there can be
#two scenarios:
#a. A new inner-list [x] has to be added at the end
#of result list and in this case find_postion returns None.
#b. A new inner-list [x] has to be inserted at
#specific location in result list. Then return the
#index at which [x] has to be inserted.

def find_position(res, x):
    for i in range(len(res)):
        if len(str(x)) == len(str(res[i][0])): #You want to insert in this list
            return i
        elif len(str(x)) < len(str(res[i][0])): #You have gone past the correct list
            return i

    return None

def categorize2(l):
    res = []

    for x in l:
           p = find_position(res, x)
           if p == None:
               #res is empty. So append a list containing x
               res.append([x])
           elif len(str(x)) == len(str(res[p][0])):
               #there is a list in res with numbers of same
               #length as x
               res[p].append(x)
           else:
               #res is not empty, but there is no other
               #number of same length as x so far

               res.insert(p, [x])
    return res

my_l = [100, 10, 20, 23, 9, 230, 10000, 3, 12000, 303]

print(categorize2(my_l))
print(categorize2([]))