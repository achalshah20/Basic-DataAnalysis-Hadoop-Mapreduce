#!/usr/bin/python

# Author: Achal Shah
# Date: 03/21/2016
# Task: Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.
# Module: Reducer

import sys

salesTotal = 0
oldKey = None
salesCount = 0

# In this reducer we will get input as store name as key and cost of each prodct as value
# Format key\tvalue

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    salesTotal += float(thisSale)
    salesCount += 1

print "\t SalesTotal: ", salesTotal, "\t SalesCount: ", salesCount

