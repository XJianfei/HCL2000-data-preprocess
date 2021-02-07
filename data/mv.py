#!/bin/python

import os
import sys
import shutil

listHcl = []
listHw = []
#list = []
listHcl.append("E")
for line in open("2.txt"): 
    listHw.append(line.replace("\n", "").strip())
for line in open("1.txt"): 
    listHcl.append(line.replace("\n", "").strip())
#print(list)

for file in os.listdir("images/"):
    print(file)
    for i in range(1, len(listHw) + 1):
        if not os.path.exists:
            os.mkdir("hw/{:0>5d}".format(i))
        print("cp images/" + file + "/" + str(listHcl.index(listHw[i - 1])) + ".jpg -> " + "hw/{:0>5d}".format(i))
    #shutil.copyfile("images/" + file + "/" listHcl[listHw[i]], "hw/{:0>5d}".format(i))
