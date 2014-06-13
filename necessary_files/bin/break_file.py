#!/usr/bin/python

import sys

flag = False
org = sys.argv[2] + "/"
if len(sys.argv[2]) > 0: 
	flag =True

f = sys.stdin
filename = sys.argv[1]
count = -1
pos_weight = ''
for i in f:
	if len(i.strip()) <1:
		continue
	if ">" in i:
		count +=1
		header = i.split()
		header = '_'.join(header)
		if count != 0:
			fout.close()
		if flag:
			fcat = org +filename+"_output/"+"smallR_files/"+header[1:].strip()+".txt"
		else:
			fcat = filename+"_output/"+"smallR_files/"+header[1:].strip()+".txt"
			
		fout = open(fcat,'w')
		fout.write(i)

	elif 'A' in i:
		continue
	else:
		line = i.split(',')
		for j in range(len(line)):
			line[j] = float(line[j].strip())
		
		
		tot = sum(line)
		line[0] = line[0]/tot
		line[1] = line[1]/tot
		line[2] = line[2]/tot
		line[3] = line[3]/tot

		for k in line:
			pos_weight += str(k) +',' 
		fout.write(pos_weight[:-1]+'\n')
		pos_weight = ''

fout.close()
