#Author: Vasanta
#Date: 02/27/2023
#Purpose: Dictionary example1, going over a dictionary

#Compare two given dictionaries and return True is they have
#same set of keys and value associated withe each key is same.

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

mdict["cs1"] = 260
mdict["cs10"] = 135
mdict["cs50"] = 60

new_dict = {}
new_dict["cs50"] = 60
new_dict["cs1"] = 260
new_dict["cs10"] = 135

print(compare_dict(mdict, new_dict))