#!/usr/bin/python
import sys
usage = "USAGE: parse_jaspar.py JASPAR_FILE ID_INFO \n\n\t use this script in order to find the ID_INFO within the header line"

if len(sys.argv) != 3:
	print usage
	sys.exit(1)


ID = False
f1 = open(sys.argv[1],'r')
FAMILY = sys.argv[2].lower()

for line in f1:
	if FAMILY in line.lower():
		ID = True

	if (ID):
		print line.strip()

	if line.strip() == '':
		ID= False
