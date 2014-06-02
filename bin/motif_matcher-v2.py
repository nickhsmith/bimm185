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

def resultPrint(result,strand):
	
	if strand == '+' or strand == '1':
		f.write( "positive strand upstream (5')\n"+result[0]+'\n')
	if strand == '-' or strand == '-1':
		f.write( "reverse strand upstream (5')\n"+result[1]+'\n')

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

	upstream = end + range_dist
	if upstream > len(seq):
		upstream = len(seq)

	tf_rev_upstream = gene_region_rev[-1*(range_dist):]
	
	return [tf_plus_upstream.tostring(),tf_rev_upstream.tostring()]


def search_region(name,chromosome,bed_line,ftype,range_dist=10000):
	#get chromosome into seq
	strand = '+'


	rev = False
	l = bed_line.split()

	if ftype == "UCSC":
		start = int(l[1])-1
		end = int(l[2])
		if l[5] == "-":
			strand = '-'
			rev = True

	if ftype == "ensemble":
		start = int(l[2]) -1
		end = int(l[3])
		if l[4] == "-1":
			strand = l[4]
			rev = True

	TFsite = map_coordinates(start,end,chromosome,range_dist,rev =rev)
	if ftype == 'UCSC':
		f.write('>'+line[0]+' '+line[3]+' '+line[5])

	elif ftype == 'ensemble':
		if line[4] == '-1':
			strand = '-'
		else:
			strand = '+'
		try:
			if len(line[8]) > 0:
				f.write( '>chr'+line[1]+" "+ line[0]+" "+ line[7]+" "+line[8]+" "+ strand+"\n")
		except IndexError:
			try:
				if len(line[7]) >0:
					f.write('>chr'+line[1]+" "+ line[0]+" "+ line[7]+" "+strand+"\n")
			except IndexError:
					f.write('>chr'+line[1]+" "+ line[0]+" "+strand+"\n")
	resultPrint(TFsite,strand)


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



chromosome = ''
length = 0
count =0
for l in bed_file:
	old = thisone
	if count == 0 and ensemble:
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
			chromlist.remove(i)
			filename = "search_regions/"+sys.argv[2].split('/')[1]+"_"+chrm[:-1]+'_'+sys.argv[3]+"_search_region.txt"
			f = open(filename,'w')

			for seq in SeqIO.parse(thisone, "fasta"):
				chromosome = seq.seq
			break	

	search_region(chrm[:-1],chromosome,l,ftype,range_dist=range_dist)

