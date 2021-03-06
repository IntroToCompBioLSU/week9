#!/usr/bin/env python

#import sys library
import sys

#define a new function to translate the sequence to aminoacids
def translation(DNAseq):
		
		#Table of codons and their respective amino acids
        codontable = {
                'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
                'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
                'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
                'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
                'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
                'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
                'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
                'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
                'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
                'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
                'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
                'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
                'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
                'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
                'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
                'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
                }
		
		#variable to store the aminoacids
        proteinsequence=''
		
		#define a codon and convert that an aminoacid using the table above
        for n in range(0,len(Sequencelist),3):	# DB: It's best not to use global variable names (like Sequencelist) inside a function
                        proteinsequence += codontable[Sequencelist[n:n+3]]
		
		#return the output
        return(proteinsequence)

#define filelist variable to capture all input  files
Filelist=sys.argv[1:]

#name and define  output file
Outfilename='Aminoacidseq.txt'
Outfile=open(Outfilename,'w')

#use a counter to count file numbers that have been  modified by the code below
Filenum=0

#a for loop to open the files and  write the filename in the output file
for filename in Filelist:
        Infile=open(filename,'r')
        Outfile.write(filename +'\n')
		
		#a for loop to modify line of sequence from the files and translate them
        for line in Infile:
                Sequencelist=line.strip('\n')
                Sequencelist=Sequencelist.upper()
                Aminoacidseq=translation(Sequencelist)
				
				#write the aminoacid sequence to the output file
                Outfile.write(Aminoacidseq +'\n')
		
		#close the files
        Infile.close()
		
		#counter  to identify how many files were manipulated and print out the total
        Filenum +=1     

print('number of files processed',Filenum)
#close the output file
Outfile.close()


# DB: Looks really good. Two minor things: (1) I find it easiest to keep comments indented
#     to the same level as the code they are referring to. Also, adding some spaces between
#     lines can really improve readability. (2) I really like that you define a novel function
#     but it's best not to refer to global variables (those defined in the main body of the
#     script) from inside a function.





