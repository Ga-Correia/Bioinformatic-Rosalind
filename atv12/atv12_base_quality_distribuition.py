# -*- coding: utf-8 -*-
"""atv12_base_quality_distribuition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xvaSwn4kHAN5dQJT2DWSHX9wSBYzboRp
"""

#pip install biopython

import Bio
from Bio import SeqIO

fl = open("rosalind_bphr.txt", "r")
lines = fl.readlines()
limite = int(lines[0])
fl.close()
fasta = open("rosalind_bphr.txt", "w")
for i in range(1, len(lines)):
  fasta.write(lines[i])
fasta.close()

qualidades = []
contador = 0
soma = 0
for record in SeqIO.parse("rosalind_bphr.txt", "fastq"):
  qualidades.append(record.letter_annotations["phred_quality"])

for j in range(len(qualidades[0])):
  for i in range(0, len(qualidades)):
    soma += qualidades[i][j]
  if soma/len(qualidades) < limite:
    contador += 1
  soma = 0
print(contador)