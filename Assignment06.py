#!/usr/bin/python
import sys

filename = sys.argv[1]

handle   = open(filename, "r")

list     = []

for item in handle:
        linearr = item.split()
        #print linearr

        for item in linearr:
                item = float(item)
                list.append(item)
                #print item
handle.close()

result = sum(list)
print result






#!/usr/bin/python

import sys

filename = sys.argv[1]
handle   = open(filename, "r")


//mylist = sys.argv[1:]

total = 0
for item in handle:
    x = float(item)
    total += x

handle.close()

print total

