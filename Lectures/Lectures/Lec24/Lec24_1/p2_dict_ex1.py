#Author: Vasanta
#Date: 02/27/2023
#Purpose: Dictionary example1, going over a dictionary

#Comparing two dictionaries

def compare_dict(gd1, gd2):
    if len(gd1) != len(gd2):
        return False

    for k1 in gd1:
        if k1 in gd2:
            if gd1[k1] != gd2[k1]:
                return False
        else:
           return False

    return True

mdict = {}
#Adding to dictionary
mdict["cs1"] = 260
mdict["cs10"] = 135
mdict["cs50"] = 60

new_dict1 = {}
new_dict1["cs50"] = 60
new_dict1["cs10"] = 135
new_dict1["cs1"] = 260

print(compare_dict(mdict, new_dict1))




