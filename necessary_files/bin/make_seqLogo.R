#!/usr/bin/R
#source("http://bioconductor.org/biocLite.R")
#biocLite("seqLogo")
library("seqLogo")

args <- commandArgs(trailingOnly = TRUE)
p1= paste(args[2],args[1],sep='/')
p = paste(p1,"_output/smallR_files",sep='')

p
filenames <- list.files(path=p, pattern="*.csv",full.names = TRUE)
filenames

for (i in filenames){
	name = paste(i,".jpg", sep="")
	jpeg(name)
	df <- read.csv(i,comment.char=">")
	df =t(df)
	seqLogo(df)	
	dev.off()

}

