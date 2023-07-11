#Author: Vasanta
#Date: 03/03/2023
#Purpose: Creating vertex graph

from Lectures.Lec26.Lec26_1.vertex import Vertex
vdict = {}

fp = open("data", "r")

for l in fp:
    wlist1 = l.split(":")
    vname = wlist1[0].strip()
    v = Vertex(vname, None, [])
    vdict[vname] = v

fp.close()

fp = open("data", "r")

for l in fp:
    wlist1 = l.split(":")
    vname = wlist1[0].strip()
    adj_name_list = wlist1[1].split(",")

    #Remove white space and "\n"
    for i in range(len(adj_name_list)):
        adj_name_list[i] = adj_name_list[i].strip()

    adj_list = []

    for name in adj_name_list:
        adj_v = vdict[name]
        adj_list.append(adj_v)

    curr_v = vdict[vname]
    curr_v.adj_list = adj_list

fp.close()

