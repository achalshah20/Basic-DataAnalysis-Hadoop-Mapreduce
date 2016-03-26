#!/usr/bin/python

# Author: Achal Shah
# Date: 03/26/2016
# Task: Find number of hits on each different IP
# Module: Reducer

import sys

# In this reducer we will get input as IP as key and 1 as value
# Format key\tvalue
# This reducer will process each lines and count the number of times each IP got hit.

oldKey = None
totalHit = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, iCount = data_mapped
    iCount = int(iCount)

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", totalHit
        oldKey = thisKey
	totalHit = 0

    oldKey = thisKey
    totalHit += iCount


if oldKey != None:
    print oldKey, "\t", totalHit

