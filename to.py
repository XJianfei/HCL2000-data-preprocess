#!/bin/python

import os

list = []
for line in open("2.txt"): 
    list.append(line.replace("\n", "").strip())
print(list)

print(list.index("中"))
