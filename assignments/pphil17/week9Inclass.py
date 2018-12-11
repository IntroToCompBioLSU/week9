#!/usr/bin/env python


#Amino Acid dictionary:
codon_AA = {"UUU":"Phe", "UUC":"Phe", "UUA":"Leu",			# DB: Can't use --> in a variable name
          "UUG":"Leu", "UCU":"Ser","UCC":"Ser", "UCA":"Ser",
          "UCG":"Ser", "UAA":"Stop", "UAU":"Try","UAC":"Tyr",
          "UAG":"Stop", "UGU":"Cys", "AAA":"Lys", "AAC":"Asn",
          "AAG":"Lys", "AAU":"Asn", "UGA":"Stop",
          "ACA":"Thr", "ACC":"Thr", "ACG":"Thr", "ACU":"Thr",
          "AGA":"Arg", "AGG":"Arg", "AGU":"Ser", "AGC":"Ser",
          "AUA":"Ile", "AUC":"Ile", "AUG":"Met", "AUU":"Ile",
          "CAA":"Gln", "CAG":"Gln", "CAU":"His", "CAC":"His",	# DB: Added missing comma
          "CCG":"Pro", "CCA":"Pro", "CCC":"Pro", "CCU":"Pro",
          "CGA":"Arg", "CGC":"Arg", "CGG":"Arg", "CGU":"Arg",
          "GAA":"Glu", "GAG":"Glu", "GAC":"Asp", "GAU":"Asp",
          "GCA":"Ala", "GCC":"Ala", "GCG":"Ala", "GCU":"Ala",
          "GGA":"Gly", "GGC":"Gly", "GGG":"Gly", "GGU":"Gly",
          "CUA":"Leu", "CUC":"Leu", "CUG":"Leu", "CUU":"Leu",	# DB: Added missing comma
          "GUA":"Val", "GUC":"Val", "GUG":"Val", "GUU":"Val"}	# DB: Added missing brace

#List for reading multiple files
import sys
myFile = []
user_args = sys.argv[1:]
for filename in user_args:
    with open(filename, 'r') as myfile:
       sequence = myfile.read().replace('\n', '')	# DB: Fixed variable name
    myFile.append(sequence)

#Converting DNA sequence --> RNA Sequence by pulling DNA sequence from file
dnaSeq = ''.join(myFile)
dnaSeq = dnaSeq.upper()		# DB: Fixed variable name
#T (Thymine) in DNA must be replaced with U (Uracil) in RNA
rnaSeq=dnaSeq.replace("T","U")
print("DNA sequence coonverted to RNA sequence: %s" %rnaSeq) # DB: Adjusted to lowercase s

#Converting RNA sequence to Proteins
proteinSeq = ""
for r in range(0, len(rnaSeq), 3):	# DB: Adjusted variable name on these two lines (rnaSeq)
      if rnaSeq[r:r+3] in codon_AA:		# DB: Adjusted name of dictionary and added colon
         proteinSeq += codon_AA[rnaSeq[r:r+3]]
print("Your Protein sequence: %s" %proteinSeq)

outFilename = "proteinSeq.txt"
outFile = open(outFilename, 'w')	# DB: Adjusted variable name to outFilename
outFile.write("%s \n" %proteinSeq)
print("Protein sequence was sent to proteinSeq.txt")

# DB: Good ideas here, but several syntax errors (see above). The script worked well once
#     these were fixed, though.