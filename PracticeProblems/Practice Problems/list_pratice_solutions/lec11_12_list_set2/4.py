#4
def count_a(gs):
    count = 0
    i = 0
    while i < len(gs):
        if gs[i] == "a":
            count = count + 1
        i = i + 1

    return count

def equal_a(gs1, gs2):
    count1 = count_a(gs1)
    count2 = count_a(gs2)

    return count1 == count2

# print(equal_a("Dartmouth", "apple"))
# print(equal_a("Vasanta", "banana"))
# print(equal_a("", "testing"))
# print(equal_a("abcd","bcdef"))
