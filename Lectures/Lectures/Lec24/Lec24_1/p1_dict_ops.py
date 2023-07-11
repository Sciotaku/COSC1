#Author: Vasanta
#Date: 02/27/2023
#Purpose: Dictionary operations

mdict = {}
#Adding to dictionary
mdict["cs1"] = 260
mdict["cs10"] = 135
mdict["cs50"] = 60

print(mdict)
print(len(mdict))

mdict["cs1"] = 259
print(mdict)
print(mdict["cs10"])

new_dict1 = {}
new_dict1["cs50"] = 60
new_dict1["cs10"] = 135
new_dict1["cs1"] = 259

print(new_dict1)
print(mdict == new_dict1)

# del mdict["cs1"]
# print(mdict)

x = "cs57"
if x in mdict:
    print(mdict["cs57"])

for k in mdict:
    print(k, mdict[k])

