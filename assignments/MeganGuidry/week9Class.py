#!/usr/bin/env python

# translate a nucleotide sequence from files in command line to amino acid sequence
# setting dictionary for codon to amino acid
codon2aa = {"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N", 
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
            "UAA":"stop", "UAC":"Y", "UAG":"stop", "UAU":"T", 
            "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S", 
            "UGA":"stop", "UGC":"C", "UGG":"W", "UGU":"C", 
                "UUA":"L", "UUC":"F", "UUG":"L", "UUU":"F"}

# creating contents list for files entered
import sys
files = []
user_args = sys.argv[1:]
for filename in user_args:
    with open(filename, 'r') as file:
        str = file.read().replace('\n', '')
    files.append(str)

#pulling DNA sequence from file & transcribing to RNA sequence
dnaSeq = ''.join(files)
dnaSeq = dnaSeq.upper()
print("DNA sequence: %s" %dnaSeq)
rnaSeq = dnaSeq.replace("T","U")
print("Transcribed sequence: %s" %rnaSeq)

# translating rna codons to amino acids
aaSeq = ""
for n in range(0, len(rnaSeq), 3):
    if rnaSeq[n:n+3] in codon2aa:
        aaSeq += codon2aa[rnaSeq[n:n+3]]
print("Amino Acid sequence: %s" %aaSeq)

# sending amino acid sequence to file
outFileName = "aminoAcidSeq.txt"
outFile = open(outFileName, 'w')
outFile.write("%s \n" %aaSeq)
print("Amino acid sequence send to aminoAcidSeq.txt")
