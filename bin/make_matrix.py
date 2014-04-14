#!/usr/bin/python

import sys
import numpy as np

def print_matrix(matrix):
	for i in matrix:
		print i

def make_freq(matrix):
	for i in matrix:
		tot = sum(i)
		for j in range(len(i)):
			i[j] /=tot

usage = "USAGE: ./make_matrix.py MATRIX_DATA ID_LIST > OUTPUT_FILE \n\t\t use matrix data and a header list to generate a frequency matrix for each ID"

if len(sys.argv) !=3:
	print usage
	sys.exit(1)


data = open(sys.argv[1],'r')
idf = open(sys.argv[2], 'r')

hlist = []
for line in idf:
	hlist.append(line.split()[0])	


d = {'A':0, 'C':1, 'G':2, 'T':3}
print hlist
end = False
temp = []
val  = []
freq = []

# generate matrix for specific family. need to get length of motif in order to generate matrix to populate, go through and add a [value,0,0,0] for each line if base = A and then for the next 3 bases go into existing matrix with 3 if statements until it's back to A and reset

for line in data:
	row = line.split()
	if row[0] in hlist:
		if row[1] == 'A':
			aval = float(row[3])
			temp.append([aval,.0,.0,.0])
			end = False

		else:
			val = [.0,.0,.0,.0]
			loc = d[row[1]]
			index = int(row[2]) -1 


			val[loc] = float(row[3])
			#print val
			temp[index]= (np.add(temp[index] ,val))
			end = True
	
		if end == True and row[1] == 'A':
			print "OUT OUT OUT"
			temp = []


print_matrix(temp)
#make_freq(temp)
#print_matrix(temp)

