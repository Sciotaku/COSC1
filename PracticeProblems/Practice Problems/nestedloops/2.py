def count_freq(gstr, c):#O(n)
    count = 0
    for x in gstr:
        if c == x:
            count = count + 1

    return count

def check_strings(str1, str2):#O(n^2)

    if len(str1) != len(str2):
        return False

    for x in str1:
        c1 = count_freq(str1, x) #O(n)
        c2 = count_freq(str2, x) #O(n)

        if c1 != c2:
            return False

    return True

print(check_strings("dirtyroom", "dormitory"))
print(check_strings("washer", "dishwasher"))
print(check_strings("to", "too"))
