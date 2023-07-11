def is_prefix(s1, s2, i = 0):
    if len(s1) < len(s2):
        return False

    if i == len(s2):
        return True

    if s1[i] == s2[i]:
        return is_prefix(s1, s2, i+1)
    else:
        return False

print(is_prefix("testing", "test"))
print(is_prefix("dishwasher", "wash"))
print(is_prefix("test", "testing"))
print(is_prefix("test", "test"))
print(is_prefix("test",""))
