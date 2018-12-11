#!/usr/bin/env python
#using sys for command-line arguments

CodonAA = {"AAA":"Lysine ", "AAC":"Asparagine ", "AAG":"Lysine ", "AAU":"Asparagine ", 
"ACA":"Threonine ", "ACC":"Threonine ", "ACG":"Threonine ", "ACU":"Threonine ",
"AGA":"Arginine ", "AGC":"Serine ", "AGG":"Arginine ", "AGU":"Serine ", 
"AUA":"Isoleucine ", "AUC":"Isoleucine ", "AUG":"Methionine ", "AUU":"Isoleucine ", 
"CAA":"Glutamine ", "CAC":"Hisdadine ", "CAG":"Glutamine ", "CAU":"Hisdadine ",
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

#beginning list for reading more than one files
l = []
file_input = sys.argv[1:]
for filename in file_input:
	with open(filename, 'r') as myfile:
		myLine = myfile.read()
	l.append(myLine)
dnaSequence = ''.join(l)			# DB: Note that newline characters will still be present!
dnaSequence = dnaSequence.upper()
rnaSequence = dnaSequence.replace("T","U")
print("DNA sequences transcribed: %s" %rnaSequence)

#Convert RNA sequences to their respective amino acids
proteinSequence = ""
for i in range(0,len(rnaSequence), 3):
	if rnaSequence[i:i+3] in CodonAA:
		proteinSequence += CodonAA[rnaSequence[i:i+3]]
proteinSequence = proteinSequence.upper()
proteinSequence = proteinSequence.replace(' ','\n')

print ("Protein Sequence: "+proteinSequence)
print("The transcribed  sequences to amino acids are located in the file name Prot_Seq.")
outFileName = "Prot_Seq.txt"
outFile = open(outFileName,'w')
outFile.write("%s \n" %proteinSequence)

# DB: Really good, but newline characters will still be present in the concatenate DNA sequence
#     and your script will then try to include them in translation. This will result in fewer
#     amino acids than you expect. Maybe try stripping whitespace from strings before you concatenate.