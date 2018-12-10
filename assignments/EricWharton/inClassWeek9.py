#!/usr/bin/env python

#to execute this command, use ./inClassWeek9.py <FILE WITH DNA SEQUENCE>
# amino acid library/dictionary/what have you
codons =	{"AAA":"Lys", "AAC":"Asn", "AAG":"Lys", "AAU":"Asn",
		"ACA":"Thr", "ACC":"Thr", "ACG":"Thr", "ACU":"Thr",
		"AGA":"Arg", "AGC":"Ser", "AGG":"Arg", "AGU":"Ser",
		"AUA":"Ile", "AUC":"Ile", "AUG":"Met", "AUU":"Ile",
		"CAA":"Gln", "CAC":"His", "CAG":"Gln", "CAU":"His",
		"CCA":"Pro", "CCC":"Pro", "CCG":"Pro", "CCU":"Pro",
		"CGA":"Arg", "CGC":"Arg", "CGG":"Arg", "CGU":"Arg",
		"CUA":"Leu", "CUC":"Leu", "CUG":"Leu", "CUU":"Leu",
		"GAA":"Glu", "GAC":"Asp", "GAG":"Glu", "GAU":"Asp",
		"GCA":"Ala", "GCC":"Ala", "GCG":"Ala", "GCU":"Ala",
		"GGA":"Gly", "GGC":"Gly", "GGG":"Gly", "GGU":"Gly",
		"GUA":"Val", "GUC":"Val", "GUG":"Val", "GUU":"Val",
		"UAA":"Stop", "UAC":"Tyr", "UAG":"Stop", "UAU":"Tyr",
		"UCA":"Ser", "UCC":"Ser", "UCG":"Ser", "UCU":"Ser",
		"UGA":"Stop", "UGC":"Cys", "UGG":"Trp", "UGU":"Cys",
		"UUA":"Leu", "UUC":"Phe", "UUG":"Leu", "UUU":"Phe"}

import sys
# list for to-be-entered files
j = []
input = sys.argv[1:]
for fileName in input:
	with open(fileName,'r') as file:
		str = file.read().replace('\n','')
	j.append(str)

# the next sequence of commands will do what was done in the week 8 assignment --> transcribe a DNA sequence to RNA
dnaSeq = ''.join(j)
dnaSeq = dnaSeq.upper()
rnaSeq = dnaSeq.replace("T","U")
print ("RNA sequence: %s" %rnaSeq)

# translation of codons into AA's
amino = ""

for x in range(0, len(rnaSeq), 3):
	if rnaSeq[x:x+3] in codons:
		amino += codons[rnaSeq[x:x+3]]

# send the sequence(s) into one file
print ("Your sequences are in a file called AAsequences.txt")
outFileName = "AAsequences.txt"
outFile = open(outFileName, 'w')
outFile.write("%s \n" %amino)

# DB: Overall, this looks good. I had originally intended that each input sequence would
#     result in a different output AA sequence, but I realize the directions weren't clear
#     about that. My only other comment is that you could add a few more specific comments
#     throughout.
