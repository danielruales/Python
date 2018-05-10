#!/usr/bin/python

import sys
import os

filename = sys.argv[1] 
#print filename
matrix = "matrix"
#proteinfile = open(filename, "r")

cmd = "rpsblast+ -db /home/bryan/data/cdd/cdd -query %s -outfmt 7 -evalue 0.05 > %s" %(filename,matrix) 
os.system(cmd)
matrixFile = open(matrix, "r")
tmpOut = ""
flag = 0
for line in matrixFile:
    if line[0] == '#':
        lineArray = line.split(' ')
	    if lineArray[1] == "Query:":
                if flag == 0:
                    flag = 1
                else:
                    print tmpOut
                tmpOut = lineArray[2].replace("\n", "")
    else:
        lineArray = line.split('\t')
        tmpOut += (' ' + lineArray[1] + ' ' + lineArray[6] + ' ' + lineArray[7])
print tmpOut







#!/usr/bin/python

import sys
import os

filename = sys.argv[1] #prints the filename
matrix = "matrix"

cmd = "rpsblast+ -db /home/bryan/data/cdd/cdd -query %s -outfmt 7 -evalue 0.05 > %s" %(filename,matrix) 
os.system(cmd)
matrixFile = open(matrix, "r")
tmpOut = ""
flag = 0
####
for line in matrixFile:
    if line[0] == '#':
        lineArray = line.split(' ')
        if lineArray[1] == "Query:":
                if flag == 0:
                    flag = 1
                else:
                    print tmpOut
                tmpOut = lineArray[2].replace("\n", "")
    else:
        lineArray = line.split('\t')
        tmpOut += (' ' + lineArray[1] + ' ' + lineArray[6] + ' ' + lineArray[7])
####
print tmpOut