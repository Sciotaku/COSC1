#Given a list of numbers find the longest sequence
#of consecutive numbers that you can form using
#the numbers in the list. You cannot sort the given
#list.

#Find the maximum number in the give list
def find_max(glist):
    max = glist[0]
    for x in glist:
        if x > max:
            max = x

    return max


def max_num_seqs(glist):
    max = find_max(glist)
    res = []

    max_count = 1

    for i in range(len(glist)):
        x = glist[i]
        #make the longest possible sequence
        #starting from x going in forward direction
        #and keep the count
        curr_count = 1
        curr_seq = [x]

        #Try expanding the sequence for x
        #starting from x+1 till max element in
        #the list
        for y in range(x+1, max+1):
            if y in glist:
                curr_count = curr_count + 1
                curr_seq.append(y)
            else:
                break

        #check if curr_count is bigger than
        #max_count then update max_count and
        #max_seq
        if curr_count > max_count:
            max_count = curr_count
            res = [] #remove all old sequences
            #add the curr_seq to result
            res.append(list(curr_seq))
        elif curr_count == max_count:
            #if it was equal to max_count
            #thenadd to result list
            res.append(list(curr_seq))

    return res



#alist = [4, 8, 9, 13, 1, 2, 5, 7, 10, 100, 3, 11]
alist = [29, 26, 2, 1, 6, 7, 27, 100, 4, 8, 28, 5, 25, 99, 98, 97, 96, 101]
rlist = max_num_seqs(alist)
print(rlist)



