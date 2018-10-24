#!/usr/bin/env python


######## Jacob Searight : Jacobssearight : Biol4800 : Week 9 In Class Assignment : 10.18.18

######## The files that are to be read should be listed after the script during execution.
######## For loop to open the files supplied
import sys
for files in sys.argv[1:]:
	DNAseqfile = open(files, 'r')
	DNAseq = DNAseqfile.read()
######## The codon dictionary was copied and pasted from an internet source (https://www.biostars.org/p/2903/).
######## For the codon translation table, all thymine nucelic acids must be replaced with uracil.
	RNAseq = DNAseq.replace("T","U")
	codon = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
	"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
	"UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
	"UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
	"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
	"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
	"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
	"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
	"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
	"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
	"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
	"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
	"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
	"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
	"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
	"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
######## the sequence stored in variable DNAseq is now RNAseq, we now need to read every three RNA bases and match them to a codon, contained in the variable DNAcodon. A for loop is used. 
	DNAcodon = ""
	for base in range(0, len(RNAseq), 3):
		if RNAseq[base:base+3] in codon:
			DNAcodon += codon[RNAseq[base:base+3]]
######## The outfile is named as AAOutput.txt, and the 'a' command allows it to be appended to it after each run of the for loop. 
	oFName = "AAOutput.txt"
	oF = open(oFName,'a')
	oF.write("%s \n" %DNAcodon)

