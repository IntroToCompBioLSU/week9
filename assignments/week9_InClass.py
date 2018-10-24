#!/usr/bin/python
#will use sys for command-line arguments
#setting up dictionary
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
#Starting list for reading multiple files
l = []
user_input = sys.argv[1:]
for filename in user_input:
        with open(filename, 'r') as myfile:
                myLine = myfile.read()
        l.append(myLine)
dnaSeq = ''.join(l)
dnaSeq = dnaSeq.upper()
rnaSeq = dnaSeq.replace("T","U")
count = 0
rnaList = []
for i in range(len(rnaSeq)):
	if rnaSeq[count] != '\n':
		rnaList.append(rnaSeq[count])
count = count + 1
print (rnaList[0])
print("DNA sequences transcribed: %s" %rnaSeq)
#Converts the RNA sequence to amino acids.
proteinSeq = ""
for i in range(0, len(rnaSeq), 3):
	if rnaSeq[i:i+3] in Codon2AA:
		proteinSeq += Codon2AA[rnaSeq[i:i+3]]
print ("Protein Sequence: "+proteinSeq)
print("The transcribed sequences to amino acids are located in the file named Protein_Sequence.")
outFileName = "Protein_Sequence.txt"
outFile = open(outFileName,'w')
outFile.write("%s \n" %proteinSeq)


