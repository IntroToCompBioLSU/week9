#!/usr/bin/python

# Week 9 in class assignment to get DNA sequences from different files in separate lines.
# Ultimately creating Protein Sequences.

# Setting up Codons to Amino Acid dictionary.
Codon2AA = {"AAA":"Lysine ", "AAC":"Asparagine ", "AAG":"Lysine ", "AAU":"Asparagine ",
"ACA":"Threonine ", "ACC":"Threonine ", "ACG":"Threonine ", "ACU":"Threonine ",
"AGA":"Arginine ", "AGC":"Serine ", "AGG":"Arginine ", "AGU":"Serine ",
"AUA":"Isoleucine ", "AUC":"Isoleucine ", "AUG":"Methionine ", "AUU":"Isoleucine ",
"CAA":"Glutamine ", "CAC":"Histadine ", "CAG":"Glutamine ", "CAU":"Histadine ",
"CCA":"Proline ", "CCC":"Proline ", "CCG":"Proline ", "CCU":"Proline ",
"CGA":"Arginine ", "CGC":"Arginine ", "CGG":"Arginine ", "CGU":"Arginine ",
"CUA":"Leucine ", "CUC":"Leucine ", "CUG":"Leucine ", "CUU":"Leucine ",
"GAA":"Glutamate ", "GAC":"Aspartate ", "GAG":"Glutamate ", "GAU":"Aspartate ",
"GCA":"Alanine ", "GCC":"Alanine ", "GCG":"Alanine ", "GCU":"Alanine ",
"GGA":"Glycine ", "GGC":"Glycine ", "GGG":"Glycine ", "GGU":"Glycine ",
"GUA":"Valine ", "GUC":"Valine ", "GUG":"Valine ", "GUU":"Valine ",
"UAA":"Stop ", "UAC":"Tyrosine ", "UAG":"Stop ", "UAU":"Threonine ",
"UCA":"Serine ", "UCC":"Serine ", "UCG":"Serine ", "UCU":"Serine ",
"UGA":"Stop ", "UGC":"Cysteine ", "UGG":"Tryptophan ", "UGU":"Cysteine ",
"UUA":"Leucine ", "UUC":"Phenylalanine ", "UUG":"Leucine ", "UUU":"Phenylalanine "}

import sys

# Starting list for reading multiple files of DNA sequences.
l = []
user_input = sys.argv[1:]
for filename in user_input:
        with open(filename, 'r') as myfile:
                myLine = myfile.read()
        l.append(myLine)
dnaSeq = ''.join(l)			# DB: Note that the newline characters are still there!
dnaSeq = dnaSeq.upper()
rnaSeq = dnaSeq.replace("T","U")

# Prints RNA sequences.
print("DNA sequences transcribed: %s" %rnaSeq)

# Converts the RNA sequences to amino acids.
proteinSeq = ""
for i in range(0, len(rnaSeq), 3):
	if rnaSeq[i:i+3] in Codon2AA:
		proteinSeq += Codon2AA[rnaSeq[i:i+3]]

# Prints Protein Sequences.
print ("Protein Sequence: "+proteinSeq)

# Tells user where the Protein Sequences are located.
print("The transcribed sequences to amino acids are located in the file named Protein_Sequence.")

# Makes a file and adds the Protein Sequences inside.
outFileName = "Protein_Sequence.txt"
outFile = open(outFileName,'w')
outFile.write("%s \n" %proteinSeq)

# DB: Overall, really good. The only problem is that you've concatenated strings of dna
#     sequence that are interspersed with newline characters. So your script will try to 
#     do the translation with the newlines as well.