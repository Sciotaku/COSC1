#Define a function that takes two lists glist1 and glist2
#as parameters and returns True if they are reverse of each
#other, otherwise returns False. For simplicity you can assume
#that the given lists contain only integers.

def is_reverse(glist1, glist2):
    if len(glist1) != len(glist2):
        return False

    i = 0 #i starts at beginning of glist1
    j = len(glist2) - 1 #j starts at end of glist2

    #Idea is similar to checking of palindrome but you need to go till the end
    #and not stop when you cross midpoint.
    
    while i < len(glist1) : # you can j >= 0, as both lists will be equal length
        if glist1[i] != glist2[j]:
            return False

        i = i + 1
        j = j - 1

    return True

mlist1 = [12, 5, 73, 28, 21, 9]
mlist2 = [9, 21, 28, 73, 5, 12]
print(is_reverse(mlist1, mlist2))