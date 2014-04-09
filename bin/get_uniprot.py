#!/usr/bin/python

import sys

usage = "USAGE: bin/get_uniprot.py JASPAR_PROTEIN < JASPAR_ID > OUTPUT_FILE \n\t\t Use to generate a motif matrix for each of the files in the JASPAR_ID input"

if len(sys.argv) != 2:
	print usage
	sys.exit(1)

fp = open(sys.argv[1],'r')

header_list =[]

for i in sys.stdin:
	header_list.append(i.strip())
	
for line in fp:
	if line.split()[0] in header_list:
		print line.split()[1]

