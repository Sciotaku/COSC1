#Author: Vasanta
#Date: 02/27/2023
#Purpose: Dictionary example, building a dictionary

def make_count_dict(gs):
    count_dict = {}

    for ch in gs:
        if ch in count_dict:
            count_dict[ch] = count_dict[ch] + 1
        else:
            count_dict[ch] = 1

    return count_dict

print(make_count_dict("banana"))


def check_anagrams(gs1, gs2):
    cdict1 = make_count_dict(gs1)
    cdict2 = make_count_dict(gs2)

    check = (cdict1 == cdict2)
    return check

print(check_anagrams("banana", "aanb"))