#!/usr/bin/python

import sys

flag = False
org = sys.argv[2] + "/"
if len(sys.argv[2]) > 0: 
	flag =True

f = sys.stdin
filename = sys.argv[1]
count = -1
for i in f:
	if ">" in i:
		count +=1
		if count != 0:
			fout.close()
		if flag:
			fcat = org +filename+"_output/"+"smallR_files/"+filename+"_"+str(count)+".csv"
		else:
			fcat = filename+"_output/"+"smallR_files/"+filename+"_"+str(count)+".csv"
			
		fout = open(fcat,'w')
		fout.write(i)
	else:
		fout.write(i)	

fout.close()
