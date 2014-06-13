#!/usr/bin/R
#source("http://bioconductor.org/biocLite.R")
#biocLite("seqLogo")
library("seqLogo")

args <- commandArgs(trailingOnly = TRUE)
p1= paste(args[2],args[1],sep='/')
p = paste(p1,"_output/smallR_files",sep='')

all_files<- list.files(path=p,full.names = TRUE)
filenames <- all_files[grep("jpg",all_files,invert=TRUE)]

print(filenames)

for (i in filenames){
	name = paste(i,".jpg", sep="")
	jpeg(name)
	df <- read.csv(i,comment.char=">",row.names = NULL,header= FALSE)
	df =t(df)
	seqLogo(df)	
	dev.off()

}

