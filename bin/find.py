#!/usr/bin/python
import sys
# usage = ./find.py LARGE_FILE option=jaspar < search_term_file >OUTPUT
# use instead of grep -f for 1 word per line in search term file
# if using for jaspar data have second param="jaspar"

jaspar = False

if sys.argv[2] == "jaspar":
	jaspar = True
f1 = sys.stdin.readlines()
f2 = open(sys.argv[1],'r')

for line in f2:
	for j in f1:
		if jaspar == True:
			if j.strip() in line.split()[0]:
				print line.strip()
		else:
			if j.strip() in line:
				print line.strip()

