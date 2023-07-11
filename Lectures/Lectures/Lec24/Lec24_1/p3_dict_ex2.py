#Author: Vasanta
#Date: 02/27/2023
#Purpose: Dictionary example, building a dictionary


def count_chars(gs):
#returns a dictionary with keys as charracters and associated value as the count
#of how many times it appears in gs
    count_dict = {}

    for ch in gs:
        if ch in count_dict:
            count_dict[ch] = count_dict[ch] + 1
        else:
            count_dict[ch] = 1

    return count_dict

print(count_chars("banana"))

def check_anagrams(gs1, gs2):
    cdict1 = count_chars(gs1)
    cdict2 = count_chars(gs2)

    check = (cdict1 == cdict2)
    return check

print(check_anagrams("banana", "apple"))