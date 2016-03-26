#!/usr/bin/python

# Author: Achal Shah
# Date: 03/21/2016
# Task: Find sales breakdown by product category across all of our stores.
# Module: Reducer

import sys

salesTotal = 0
oldKey = None

# In this reducer we will get input as product category as key and cost of each prodct as value
# Format key\tvalue

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesTotal

