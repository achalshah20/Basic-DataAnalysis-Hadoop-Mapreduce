#!/usr/bin/python

# Author: Achal Shah
# Date: 03/21/2016
# Task: Find sales breakdown by product category across all of our stores.
# Module: Mapper

#This mapper is used to separate product category and cost
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(item, cost)

