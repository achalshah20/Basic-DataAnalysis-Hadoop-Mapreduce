#!/usr/bin/python

# Author: Achal Shah
# Date: 03/21/2016
# Task: Find the monetary value for the highest individual sale for each separate store.
# Module: Reducer

import sys

highestSale = 0
oldKey = None


# In this reducer we will get input as store name as key and cost of each prodct as value
# Format key\tvalue

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    if highestSale < float(thisSale):
        highestSale = float(thisSale)

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", highestSale
        oldKey = thisKey;
        highestSale = float(thisSale) #If store name changes then store latest sale price as highest sale

    oldKey = thisKey


if oldKey != None:
    print oldKey, "\t", highestSale

