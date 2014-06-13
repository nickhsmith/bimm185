#!/usr/bin/python

import sys
import os
from Bio import Seq
from Bio import SeqIO

usage = 'USAGE: motif_matcher.py BED_FILE GENOME_DIR FILE_TYPE DISTANCE > OUTPUT_FILE \n\n \t BED_FILE is a gene bed file\n\t GENOME_DIR is the location of the chromosome fasta files\n\t FILE_type is UCSC or ensemble\n\t distance an integer'

if len(sys.argv) != 5:
	print usage
	sys.exit(1)

def chromname(directory):
	chromlist = []
	#print directory
	for dirname, dirnames, filenames in os.walk(directory):
		# print path to all filenames.
		for filename in filenames:
			chromlist.append(os.path.join(dirname, filename))

	return chromlist

def resultPrint(result):
	
	print "positive strand upstream (5')\n",result[0]
#	print "positive strand downstream (3')\n",result[1]
	print "reverse strand upstream (5')\n",result[1]
#	print "reverse strand downstream (3')\n",result[3]

def get_gene (start,end,seq,rev = False):
	for seq in SeqIO.parse(filename,'fasta'):
		s = seq.seq
		
		real_seq = s[start:end]

		if rev == True:
			real_seq = real_seq.reverse_complement()

		return real_seq
	
def map_coordinates(start,end,seq, range_dist,rev = False):

	gene_region = seq[start-range_dist:end+range_dist]
	gene_region_rev = gene_region.reverse_complement()


	upstream = start - range_dist
	if upstream < 0 :
		upstream = 0
	tf_plus_upstream = gene_region[:range_dist]

#	downstream = end + range_dist
#	if downstream > len(seq):
#		downstream = len(seq)
#
#	tf_plus_downstream = gene_region[-1*(range_dist):]
#
#	downstream = start - range_dist
#	if downstream < 0 :
#		downstream = 0
#	tf_rev_downstream= gene_region_rev[:range_dist]
#
	upstream = end + range_dist
	if upstream > len(seq):
		upstream = len(seq)

	tf_rev_upstream = gene_region_rev[-1*(range_dist):]
	
	return [tf_plus_upstream.tostring(),tf_rev_upstream.tostring()]
#	return [tf_plus_upstream.tostring(),tf_plus_downstream.tostring(),tf_rev_upstream.tostring(),tf_rev_downstream.tostring()]


def search_region(fasta,bed_line,ftype,range_dist=10000):
	#get chromosome into seq
	for seq in SeqIO.parse(fasta, "fasta"):
		chromosome = seq.seq


	rev = False
	l = bed_line.split()

	if ftype == "UCSC":
		start = int(l[1])-1
		end = int(l[2])
		if l[5] == "-":
			rev = True

	if ftype == "ensemble":
		start = int(l[2]) -1
		end = int(l[3])
		if l[4] == "-1":
			rev = True


	TFsite = map_coordinates(start,end,chromosome,range_dist,rev =rev)
	if ftype == 'UCSC':
		print '>'+line[0],line[3],line[5]

	elif ftype == 'ensemble':
		if line[4] == '-1':
			strand = '-'
		else:
			strand = '+'
		try:
			if len(line[8]) > 0:
				print '>chr'+line[1], line[0], line[7],line[8], strand
		except IndexError:
			try:
				if len(line[7]) >0:
					print  '>chr'+line[1], line[0], line[7],strand
			except IndexError:
					print  '>chr'+line[1], line[0],strand
	resultPrint(TFsite)


#MAIN METHOD
bed_file = open(sys.argv[1],'r')

ftype = sys.argv[3]

UCSC = ensemble = False
range_dist = int(sys.argv[4])

if ftype == "ensemble":
	ensemble = True
if ftype == "UCSC":
	UCSC = True

chromlist = chromname(sys.argv[2])
#print chromlist
thisone = ''



count =0
for l in bed_file:
	if count == 0:
		count = 1
		continue
	line = l.split()
	if UCSC:
		chrm = line[0] + '.'

	if ensemble:
		chrm = "chr"+line[1]+"."

	for i in chromlist:
		if chrm in i:
			thisone= i
			break	

	search_region(thisone,l,ftype,range_dist=range_dist)


