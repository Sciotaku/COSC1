def is_substring(s1, s2, i = 0, j = 0):
    if len(s1) < len(s2):
        return False

    if j == len(s2):
        return True

    if i == len(s1):
        return False

    if s1[i] == s2[j]:
        return is_substring(s1, s2, i+1, j+1)
    else:
        return is_substring(s1, s2, i - j + 1, 0)
        #return is_substring(s1, s2, i + 1, 0)


# print(is_substring("testing", "test"))
# print(is_substring("dishwasher", "wash"))
# print(is_substring("test", "testing"))
# print(is_substring("dishwasher", "washer"))
# print(is_substring("dishwasher", "waste"))
print(is_substring("bbbaa", "bbaa"))
