#!/usr/bin/env python

# Accept any number of filenames as command-line arguments:: import sys--*.txt-- print sys.argv 
# Each of these files can contain a separate nucleotide sequence on each line
# The script should contain a new function that takes each of these sequences,
# translates them to amino acids, and prints all of them to one output file.

# Made a codon to amino acid dictionary.
	
aminoAcids = {"AAA":"Lys", "AAC":"Asn", "AAG":"Lys", "AAU":"Asn",
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
		    "UAA":"_",   "UAC":"Tyr", "UAG":"_",   "UAU":"Thr",
                    "UCA":"Ser", "UCC":"Ser", "UCG":"Ser", "UCU":"Ser",
                    "UGA":"_",   "UGC":"Cys", "UGG":"Trp", "UGU":"Cys",
                    "UUA":"Leu", "UUC":"Phe", "UUG":"Leu", "UUU":"Phe"}

import sys
l= []
for filename in sys.argv[1:]:	# DB: This line needed [1:] so that it doesn't read in the script itself
#inFile = open (filename, 'r')
#myLine = inFile .readline().strip()
	with open(filename, 'r') as myFile:
		myLine=myFile.read().replace('\n','')
	l.append(myLine)	# DB: This line needed to be indented to be part of the loop
#dna = myLine
dna = ''.join(l)	# DB: Need this line to join all sequences together
dna = dna.upper()
rna = dna.replace("T","U")
print("Your RNA Sequence is: %s," %rna)
protein = ""
for n in range(0,len(rna), 3):
	if rna[n:n+3] in aminoAcids:
		protein += aminoAcids[rna[n:n+3]]
print ("Your protein sequence is: ")
print (protein)
# DB: Need to print AA output to file

# DB: Overall, this is very close! But there were 3 syntax errors that kept it from working
#     properly and it also needs to be able to print the AA sequence to a file.
