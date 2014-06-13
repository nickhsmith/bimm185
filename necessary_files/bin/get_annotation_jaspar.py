#!/usr/bin/python

import sys

usage = "USAGE: get_annotation_jaspar.py JASPAR_MATRIX_ANNOTATION.txt KEYWORD\n\t\t use this to on input a jaspar annotation file find the keyword (exact -except case) in the file and in combination with other parsers generate matrix and generate uniprot ID list."

if len(sys.argv) != 3:
	print usage
	sys.exit(1)

KEYWORD = sys.argv[2].lower()
f1 = open(sys.argv[1],'r')


for line in f1:
	if KEYWORD in line.strip().lower():
		print line.strip()
