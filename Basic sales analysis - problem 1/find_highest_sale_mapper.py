#!/usr/bin/python

# Author: Achal Shah
# Date: 03/21/2016
# Task: Find the monetary value for the highest individual sale for each separate store.
# Module: Mapper

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
# This mapper is used to separate product Store and cost

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)

