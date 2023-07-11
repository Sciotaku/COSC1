#Author: Vasanta
#Date: 02/22/2023
#Purpose: Reversing a string

# "abcd"   reverse is "dcba"
#  Reverse from index 1 to the end: "dcb"
#  "dcb" + "a" is "dcba"

def reverse_string(gs, i=0):
    if i == len(gs):
        return ""

    res = reverse_string(gs, i+1)
    res = res + gs[i]

    return res

print(reverse_string("abcd"))
