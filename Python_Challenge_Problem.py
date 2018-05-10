#!/usr/bin/python
import sys

#defines the triplets as amino acids
def  translation ( DNA ):
         return {
            "TTT":"F",
            "TTC":"F",
            "TTA":"L",
            "TTG":"L",
            "CTT":"L",
            "CTC":"L",
            "CTA":"L",
            "CTG":"L",
            "ATT":"I",
            "ATC":"I",
            "ATA":"I",
            "ATG":"M",
            "GTT":"V",
            "GTC":"V",
            "GTA":"V",
            "GTG":"V",
            "TCT":"S",
            "TCC":"S",
            "TCA":"S",
            "TCG":"S",
            "CCT":"P",
            "CCC":"P",
            "CCA":"P",
            "CCG":"P",
            "ACT":"T",
            "ACC":"T",
            "ACA":"T",
            "ACG":"T",
            "GCT":"A",
            "GCC":"A",
            "GCA":"A",
            "GCG":"A",
            "TAT":"Y",
            "TAC":"Y",
            "TAA":"*",
            "TAG":"*",
            "CAT":"H",
            " CAC " : " H " ,
            "CAA":"Q",
            "CAG":"Q",
            "AAT":"N",
            "AAC":"N",
            "AAA":"K",
            "AAG":"K",
            "GAT":"D",
            "GAC":"D",
            "GAA":"E",
            "GAG":"E",
            "TGT":"C",
            "TGC":"C",
            "TGA":"*",
            "TGG":"W",
            "CGT":"R",
            "CGC":"R",
            "CGA":"R",
            "CGG":"R",
            "AGT":"S",
            "AGC":"S",
            "AGA":"R",
            "AGG":"R",
            "GGT":"G",
            "GGC":"G",
            "GGA":"G",
            "GGG":"G"
         }[DNA]

def popThree(a):
    temp = str()
    for i in range(0,3):
       temp =  a.pop()


fname = sys.argv[1]
temp = str()
gene = ""
geneDict = {}
ids = []
#organizes data
for line in open(fname, "r"):
    if line[0] == ">": #middle of file reading
        gene = line.replace("\n","")
        gene = gene.replace(">","")
        geneDict[gene] = ""
        ids.append(gene)
    else:
        #saves current values
        geneDict[gene] += line.replace("\n","")

#translates sequences to proteins
for gene in ids:
    print(">"+gene)
    sequence = geneDict[gene]
    output = str()
    for i in range(0,len(sequence), 3):
	protein = str(sequence[i:i+3])
	output += translate(protein)
    print(output)
