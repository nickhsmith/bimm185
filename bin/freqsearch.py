#!/usr/bin/python
import sys
import math
import MOODS
import numpy as np


usage = "USAGE: freqfind.py SEARCH_FILE MOTIF_FREQ_FILE \n \tSEARCH_FILE is the file of all upstream regions from the genes (generated by GO.getSearch) \n\t MOTIF_FREQ_FILE is the file containing the frequency information for JASPAR Transctription factors" 

if len(sys.argv)<2:
	print usage
	sys.exit(1)

searchregion = open(sys.argv[1],'r')
freqfile = open(sys.argv[2],'r')
search_region = searchregion.readlines()

def consensus(freq_matrix):
	for i in range(len(freq_matrix)-1):
		for j in range(len(freq_matrix[i])):
			freq_matrix[i][j] = float(freq_matrix[i][j].strip())
	consensus =''
	freq_matrix.pop()
	for line in freq_matrix:
		if max(line) == line[0]:
			consensus += 'A'
		if max(line) == line[1]:
			consensus += 'C'
		if max(line) == line[2]:
			consensus += 'G'
		if max(line) == line[3]:
			consensus += 'T'

	return consensus

def search(consensus_list,TF,master,search_region,p=0.0001):
	count = 0
	count1 = 0
	
	interaction_only = False
	try:
		if sys.argv[3] == "True":
			interaction_only = True
		else:
			interaction_only = False
	except IndexError:
		pass
	duplicate = []
	
	threshold = []
	header = ''
	for i in master:
		count +=1
		threshold += [p]
		print >> sys.stderr, count

	#print threshold
	
	for region in search_region:
		if 'strand' in region:
			continue
		if '>' in region:
			header = region
		else:
			for i in range(len(master)):
	
				tf = TF[i]
				tf_length = len(consensus_list[i])
				#result = MOODS.search(region,master,threshold,absolute_threshold=threshold)
				result = MOODS.search(region,master,p)
				for j in result:
					for (position,score) in j:
						if interaction_only:
							if [tf,header] not in duplicate:
								duplicate += [[tf,header]]
								print tf.strip(),header.strip()[1:]
								print ''
						else:
							if [tf,header,position] not in duplicate:
								duplicate+= [[tf,header,position]]
								print tf.strip(),header.strip()[1:]
								print 'position:',position
								print consensus_list[i],'Matched the motif in the upstream region:',region[position:position+tf_length]
								print ''


'''

	print '@TF ID',TF
	for i in search_region:
		if 'strand' in i:
			continue
		if i[0] =='>':
			header = i
			#print header

		result =MOODS.search(i,[matrix],t,absolute_threshold=t)
		if len(result)>0:
			for i in result:
				for (position, score) in i:
					#print header
					print("Position: " + str(position) + " Score: "+ str(score))

		else:
			for j in range(len(i)-motif_len+1):
				dist +=1
				score = 0
				seq = i[j:j+motif_len].strip()	
				for nt in range (len(seq)):
					if seq[nt] == 'A':	
						score += a[nt]
					if seq[nt] == 'C':	
						score += c[nt]
					if seq[nt] == 'G':	
						score += g[nt]
					if seq[nt] == 'T':	
						score += t[nt]
				if score > 0:
					
					print header,seq
					print score
					print ''
'''
				

consensusList = []
master = []
A_list = []
C_list = []
G_list = []
T_list = []

#process freqfile
for i in freqfile:
	if '>' in i:
		header = i.strip()
		fmatrix =[]
		continue
	if 'A' == i[0]:
		continue
	line = i.strip().split(',')
	fmatrix += [line]

	'''
	if len(line) >1:
		try:
			A_list.append(math.log(float(line[0])/.25))
		except ValueError:
			A_list.append(-100000000000)
		try:
			C_list.append(math.log(float(line[1])/.25))
		except ValueError:
			C_list.append(-100000000000)
		try:
			G_list.append(math.log(float(line[2])/.25))
		except ValueError:
			G_list.append(-100000000000)
		try:
			T_list.append(math.log(float(line[3])/.25))
		except ValueError:
			T_list.append(-100000000000)

	'''
	if len(line)>1:

		A_list.append(float(line[0]))
		C_list.append(float(line[1]))
		G_list.append(float(line[2]))
		T_list.append(float(line[3]))

	elif len(A_list) > 0:
		cseq= consensus(fmatrix)
		consensusList.append(cseq)
		master.append([[A_list,C_list,G_list,T_list],header])
		A_list = []
		C_list = []
		G_list = []
		T_list = []

all_matrix = []
tf_list = []

try:
	p = float(sys.argv[4])
except IndexError:
	try:
		p=float(sys.argv[3])
	except ValueError:
		pass

for i in range(len(master)):
	if len(all_matrix) == 0:
		tf_list = [master[i][1]]
		all_matrix = [master[i][0]]

	else:
		tf_list += [master[i][1]]
		all_matrix += [master[i][0]]
#print len(tf_list)
#print len(all_matrix)
search(consensusList,tf_list,all_matrix, search_region,p)
			

