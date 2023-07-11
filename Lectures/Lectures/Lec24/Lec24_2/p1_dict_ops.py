#Author: Vasanta
#Date: 02/27/2023
#Purpose: Dictionary operations

mdict = {}

mdict["cs1"] = 260
mdict["cs10"] = 135
mdict["cs50"] = 60

print(mdict)
print(len(mdict))
print(mdict["cs10"])
mdict["cs1"] = 259
print(mdict)

new_dict = {}
new_dict["cs50"] = 60
new_dict["cs1"] = 259
new_dict["cs10"] = 135

print(new_dict == mdict)

x = "cs57"
if x in mdict:
  print(mdict[x])

for k in mdict:
    print(k, mdict[k])