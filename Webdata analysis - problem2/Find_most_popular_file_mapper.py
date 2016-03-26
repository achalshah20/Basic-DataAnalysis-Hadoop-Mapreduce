#!/usr/bin/python

# Author: Achal Shah
# Date: 03/26/2016
# Task: Find most popular file on the website
# Module: Mapper

# Sample data line and format
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
# %h %l %u %t \"%r\" %>s %b
# This mapper is used to extract file name from each line

import sys

for line in sys.stdin:
	data = line.strip().split("GET ")
	if len(data) == 2:
		a,b = data
		path = b.split(" ")
		final_path = path[0]
		if "http://www.the-associates.co.uk" in final_path:
			final_path = final_path[len("http://www.the-associates.co.uk"):len(final_path)]

		print "{0}\t{1}".format(final_path,1)
