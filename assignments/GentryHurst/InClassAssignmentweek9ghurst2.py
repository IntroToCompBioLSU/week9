#!/usr/bin/env python

#Will use sys for command-line arguments
import sys

#defining the function
def translate(sequence):
	"""This function will translate rna to amino acid sequence"""
	rna_codon = {"UUU" : "Phe", "CUU" : "Leu", "AUU" : "Ile", "GUU" : "Val",
           "UUC" : "Phe", "CUC" : "Leu", "AUC" : "Ile", "GUC" : "Val",
           "UUA" : "Leu", "CUA" : "Leu", "AUA" : "Ile", "GUA" : "Val",
           "UUG" : "Leu", "CUG" : "Leu", "AUG" : "Met", "GUG" : "Val",
           "UCU" : "Ser", "CCU" : "Pro", "ACU" : "Thr", "GCU" : "Ala",
           "UCC" : "Ser", "CCC" : "Pro", "ACC" : "Thr", "GCC" : "Ala",
           "UCA" : "Ser", "CCA" : "Pro", "ACA" : "Thr", "GCA" : "Ala",
           "UCG" : "Ser", "CCG" : "Pro", "ACG" : "Thr", "GCG" : "Ala",
           "UAU" : "Tyr", "CAU" : "His", "AAU" : "Asn", "GAU" : "Asp",
           "UAC" : "Tyr", "CAC" : "His", "AAC" : "Asn", "GAC" : "Asp",
           "UAA" : "STOP", "CAA" : "Gln", "AAA" : "Lys", "GAA" : "Glu",
           "UAG" : "STOP", "CAG" : "Gln", "AAG" : "Lys", "GAG" : "Glu",
           "UGU" : "Cys", "CGU" : "Arg", "AGU" : "Ser", "GGU" : "Gly",
           "UGC" : "Cys", "CGC" : "Arg", "AGC" : "Ser", "GGC" : "Gly",
           "UGA" : "STOP", "CGA" : "Arg", "AGA" : "Arg", "GGA" : "Gly",
           "UGG" : "Trp", "CGG" : "Arg", "AGG" : "Arg", "GGG" : "Gly"
           }
	protein_string = ""
#Determine if sequence is divisible by 3
	for i in range(0, len(firstline)-(3+len(firstline)%3), 3):
		if rna_codon[firstline[i:i+3]] == "STOP":
			break
		protein_string += rna_codon[firstline[i:i+3]]
	return protein_string

#sys for command line arguments
FilesToRead = sys.argv

#reads the sequences in the files
for seq in sys.argv[1:]:
	print("The following amino acid sequences are from the file:")
	print(seq)
	infile = open(seq,'r')
#translates the sequences in the files using new function
	with open(seq) as f:
		for firstline in f.readlines():
			if firstline[0] == '>':
				translate(firstline)
				seq += (firstline.strip('>') + '	')
			else:
				print(translate(firstline))
				seq += (translate(firstline))
#sends the amino acid seq to a new file
			amino = translate(firstline)
			OutFileName = "AminoAcidSeq.txt"
			outFile = open(OutFileName,'a')
			outFile.write("%s \n" %amino)

print("The above amino acid sequences have been saved to the following file:")
print("AminoAcidSeq.txt")
