def contains_char(gstr, c):
    for x in gstr:
        if x == c:
            return True

    return False

def check_strings(str1, str2):
    test1 = False
    test2 = False

    #Check if all characters in str1 are
    #there in str2 and set test1
    for x in str1:
        if not contains_char(str2, x):
            return False

    test1 = True

    # Check if all characters in str2 are
    # there in str1 and set mystory2
    for x in str2:
        if not contains_char(str1, x):
            return False

    test2 = True

    return (test1 and test2)

print(check_strings("dirtyroom", "dormitory"))
print(check_strings("washer", "dishwasher"))
print(check_strings("to", "too"))