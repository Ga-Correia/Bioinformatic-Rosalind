# -*- coding: utf-8 -*-
"""atv10_ready_quality_distribuition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OwBHvap4F21rs2xSEG-6O2CW2XfhtbRU
"""

#pip install biopython

import Bio
from Bio import SeqIO

fl = open("rosalind_phre.fastq", "r")
lines = fl.readlines()
limite = int(lines[0])
fl.close()

fasta = open("rosalind_phre.fastq", "w")
for i in range(1, len(lines)):
  fasta.write(lines[i])
fasta.close()

contador = 0
for record in SeqIO.parse("rosalind_phre.fastq", "fastq"):
  soma = sum(record.letter_annotations["phred_quality"])
  media = soma/len(record.letter_annotations["phred_quality"])
  if media < limite:
    contador = contador+1
print(contador)