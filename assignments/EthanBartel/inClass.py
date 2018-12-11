#!/usr/bin/python

#will use sys for command-line arguments
#setting up dictionary
aminoAcids = {"AAA":"Lysine ", "AAC":"Asparagine ", "AAG":"Lysine ", "AAU":"Asparagine ", 
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
#Starting list for reading multiple files
l = []
user_args = sys.argv[1:]
for filename in user_args:
	with open(filename, 'r') as myfile:
		myLine = myfile.read().replace('\n', '')
	l.append(myLine)
dna = ''.join(l)
dna = dna.upper()  
rna = dna.replace("T","U")
print("Your RNA sequence is: %s." %rna)
protein = ""
for n in range(0, len(rna), 3):
	if rna[n:n+3] in aminoAcids:
		protein += aminoAcids[rna[n:n+3]]
print("Your Protein sequence is located in the file Protein.txt.")
outFileName = "Protein.txt"
outFile = open(outFileName,'w')
outFile.write("%s \n" %protein)
