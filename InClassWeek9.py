#!/usr/bin/env python

import sys
line = []
usrinputs = sys.argv[1:]
for Filename in usrinputs:
	with open (Filename, 'r') as carpeta:
		TheLine = carpeta.read()
	line.append(TheLine)
DNA= ''.join(line)
DNA= DNA.upper()
RNA= DNA.replace("T", "U")
CodonTrans = {"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N",
                "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T",
                "AGA":"R", "AGC":"S", "AGG":"R", "AGU":"S",
                "AUA":"I", "AUC":"I", "AUG":"M", "AUU":"I",
                "CAA":"Q", "CAC":"H", "CAG":"Q", "CAU":"H",
                "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P",
                "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R",
                "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L",
                "GAA":"E", "GAC":"D", "GAG":"E", "GAU":"D",
                "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
                "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G",
                "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V",
                "UAA":"_", "UAC":"Y", "UAG":"_", "UAU":"T",
                "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S",
                "UGA":"_", "UGC":"C", "UGG":"W", "UGU":"C",
                "UUA":"L", "UUC":"F", "UUG":"L", "UUU":"F"}
AASeq= ""
for n in range(0, len(RNA), 3):
	if RNA[n:n+3] in CodonTrans:
		AASeq += CodonTrans[RNA[n:n+3]]
print("AASeq is: %s and is saved to: AASeq_Archivo" %AASeq)
AASeq_Archivo= "Nuevo Amino Acid Sequence Archivo."
outFile = open(AASeq_Archivo, 'w')
outFile.write("%s" %AASeq)
