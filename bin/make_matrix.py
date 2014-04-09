#!/usr/bin/python

import sys
import numpy as np

data = open(sys.argv[1],'r')

hlist = []
d = {'A':0, 'C':1, 'G':2, 'T':3}
m = []
temp = []

for i in sys.stdin:
	hlist.append(i.strip())

# generate matrix for specific family. need to get length of motif in order to generate matrix to populate, go through and add a [value,0,0,0] for each line if base = A and then for the next 3 bases go into existing matrix with 3 if statements until it's back to A and reset

for line in data:
	row = line.split()
	count = 0
