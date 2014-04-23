#!/usr/bin/python

import sys
import numpy as np

def print_matrix(matrix):
	print "A,C,G,T"
	for i in matrix:
		print i[0],',',i[1],',',i[2],',',i[3]

def make_freq(matrix):
	for i in matrix:
		tot = sum(i)
		for j in range(len(i)):
			i[j] /=tot
	return matrix

usage = "USAGE: ./make_matrix.py MATRIX_SORTED_DATA ID_LIST > OUTPUT_FILE \n\t\t use matrix data and a header list to generate a frequency matrix for each ID"

if len(sys.argv) !=3:
	print usage
	sys.exit(1)


data = open(sys.argv[1],'r')
idf = open(sys.argv[2], 'r')

hlist = []
for line in idf:
	hlist.append(line.split()[0])	


d = {'A':0, 'C':1, 'G':2, 'T':3}
end = False
temp = []
val  = []
freq = []
old = ''
alist= []
count = 1

# generate matrix for specific family. need to get length of motif in order to generate matrix to populate, go through and add a [value,0,0,0] for each line if base = A and then for the next 3 bases go into existing matrix with 3 if statements until it's back to A and reset

for line in data:
	row = line.split()
	if row[0] in hlist:
		ID = row[0]
		count = 0
		if row[1] == 'A':
			alist.append(row)
			temp.append([.0,.0,.0,.0])
			continue

		else:
			if len(alist) > 0:
				tlen =len(alist)
				for i in range(len(alist)):
					aval = float(alist[i][3])
					aind = int(alist[i][2]) -1
					temp[aind] = np.add(temp[i], (aval,.0,.0,.0))
			#	print_matrix(temp)
				alist = []
			val = [.0,.0,.0,.0]
			loc = d[row[1]]
			index = int(row[2]) -1 


			val[loc] = float(row[3])
			temp[index]= (np.add(temp[index] ,val))
		
		#print row, tlen
		if tlen >9:
			tlen =9
		if row[1] == 'T' and int(row[2]) == (tlen): 
			if count == 0:
				print '>'+ID
				temp = make_freq(temp)
				print_matrix(temp)
				print ''
			temp = []
			count = 1

	old = row[0]
