#!/usr/bin/python
import sys
line = sys.stdin.readlines()
for i in range(len(line)):
	if "A C G T Consensus" in line[i]:
		print line[i].strip()
		j = i
		while line[j].strip() != '':
			print line [j].strip()
			j +=1
	if "Transcription factors" in line[i]:
		print line[i]
		k = i
		while line[k].strip() !='':
			print line[k].strip()
			k+=1
		print '','\n','\n','\n'
	k = 0
	j = 0

#print line
