#!/usr/bin/env python

import os
import tempfile
import re

g = open("asrs.txt", "w")

def slice_reading(filepath,y,z,x=0):
    # x : number of lines to skip before the periodical treatment
    # y : number of lines to periodically skip
    # z : number of lines to periodically print
    with open('1031.txt') as f:
        lines = f.readlines()
        lgth = len(lines)

    if lgth > x+y:
        for a in xrange(x+y,lgth,y+z):
            g.writelines(lines[a:a+z])
    else:
        print 'Not enough lines before lines to print'


slice_reading('1031.txt',10,52)
g.close()

# open the input file
inputFile = r"asrs.txt"

# open the output file
outputFile = r"final.txt"     

text = open(inputFile).read()
mergedText = open(outputFile, "w")  
count = 0  

for line in text.splitlines():
    # Make sure line numbers are even
    if count%2 == 0:
        lineTrunc = line
    else:
        # merge the lines in the output file
        mergedText.writelines(lineTrunc + " " + line + "\n")
    count += 1
    
    

inputFile.close()
outputFile.close()

print "finished"
print "number of lines in input file: " + str(count)

