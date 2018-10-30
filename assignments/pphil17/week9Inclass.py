#!/usr/bin/env python


#Amino Acid dictionary:
codon--> AA = {"UUU":"Phe", "UUC":"Phe", "UUA":"Leu",
          "UUG":"Leu", "UCU":"Ser","UCC":"Ser", "UCA":"Ser",
          "UCG":"Ser", "UAA":"Stop", "UAU":"Try","UAC":"Tyr",
          "UAG":"Stop", "UGU":"Cys", "AAA":"Lys", "AAC":"Asn",
          "AAG":"Lys", "AAU":"Asn", "UGA":"Stop",
          "ACA":"Thr", "ACC":"Thr", "ACG":"Thr", "ACU":"Thr",
          "AGA":"Arg", "AGG":"Arg", "AGU":"Ser", "AGC":"Ser",
          "AUA":"Ile", "AUC":"Ile", "AUG":"Met", "AUU":"Ile",
          "CAA":"Gln", "CAG":"Gln", "CAU":"His", "CAC":"His"
          "CCG":"Pro", "CCA":"Pro", "CCC":"Pro", "CCU":"Pro",
          "CGA":"Arg", "CGC":"Arg", "CGG":"Arg", "CGU":"Arg",
          "GAA":"Glu", "GAG":"Glu", "GAC":"Asp", "GAU":"Asp",
          "GCA":"Ala", "GCC":"Ala", "GCG":"Ala", "GCU":"Ala",
          "GGA":"Gly", "GGC":"Gly", "GGG":"Gly", "GGU":"Gly",
          "CUA":"Leu", "CUC":"Leu", "CUG":"Leu", "CUU":"Leu"
          "GUA":"Val", "GUC":"Val", "GUG":"Val", "GUU":"Val"

#List for reading multiple files
import sys
myFile = []
user_args = sys.argv[1:]
for filename in user_args:
    with open(filename, 'r') as myfile:
       myFile = file.read().replace('\n', '')
    myFile.append(sequence)

#Converting DNA sequence --> RNA Sequence by pulling DNA sequence from file
dnaSeq = ''.join(myFile)
dnaSeq = dna.upper()
#T (Thymine) in DNA must be replaced with U (Uracil) in RNA
rnaSeq=dnaSeq.replace("T","U")
print("DNA sequence coonverted to RNA sequence: %S" %rnaSeq)

#Converting RNA sequence to Proteins
proteinSeq = ""
for r in range(0, len(RNAseq), 3):
      if RNAseq[r:r+3] in Codon
         proteinSeq += Codon[rnaSeq[r:r+3]]
print("Your Protein sequence: %s" %proteinSeq)

outFilename = "proteinSeq.txt"
outFile = open(OutFileName, 'w')
outFile.write("%s \n" %proteinSeq)
print("Protein sequence was sent to proteinSeq.txt")
