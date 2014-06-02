#!/usr/bin/python
import sys

seq = ''
for i in sys.stdin:
	print len(i)
	if len(i) == 1:
		break
	line = i.split()
	for i in range(len(line)):
		line[i] = float(line[i])
	print line
	maxB = max(line)
	if line[0] == maxB:
		seq+='A'
	if line[1] == maxB:
		seq+='C'
	if line[2] == maxB:
		seq+='G'
	if line[3] == maxB:
		seq+='T'

print seq
	
