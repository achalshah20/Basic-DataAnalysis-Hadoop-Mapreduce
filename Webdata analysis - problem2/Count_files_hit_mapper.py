#!/usr/bin/python

# Author: Achal Shah
# Date: 03/26/2016
# Task: Find number of hits for each different files
# Module: Mapper

# Sample data line and format
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
# %h %l %u %t \"%r\" %>s %b
# This mapper is used to extract path from each line of data

import sys

for line in sys.stdin:
	data = line.strip().split("GET ")
	if len(data) == 2:
		a,b = data
		path = b.split(" ")
		print "{0}\t{1}".format(path[0],1)
