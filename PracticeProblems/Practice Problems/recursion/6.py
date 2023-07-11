def insert_key(glist, key, i = 0):
    if i == len(glist):
        glist.append(key)
        return

    if glist[i] >= key:
        glist.insert(i, key)
    else:
        insert_key(glist, key, i+1)

my_list = [10, 20, 30, 40, 50]
insert_key(my_list, 60)
print(my_list)
insert_key(my_list, 33)
print(my_list)
insert_key(my_list, 2)
print(my_list)