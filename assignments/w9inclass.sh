#!/usr/bin/env python

import sys
for files in sys.argv[1:]:
	Dsf = open(files, 'r')
	for lines in Dsf:
		DNAseq = lines
		RNAseq = DNAseq .replace("T","U")
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

		DNAcodon=""
		for base in range (0, len(RNAseq), 3):
			if RNAseq[base:base+3] in codon:
				DNAcodon += codon[RNAseq[base:base+3]]
		print(DNAcodon)
