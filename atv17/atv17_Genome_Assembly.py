# -*- coding: utf-8 -*-
"""atv17_bioavanc.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uCaEGbdqxb1cFyvWOQ4prHBGnLJWzurP
"""

#pip install biopython

from Bio import SeqIO

sequences = []
indexes = []
for record in SeqIO.parse("rosalind_long.txt", "fasta"):
  sequences.append(record.seq)

genome = sequences[0]
for i in range(1, len(sequences)):
  indexes.append(i)

while len(indexes)>0:
  for i in indexes:
    before = True
    after = True
    for j in reversed(range(int(len(sequences[i])/2), len(sequences[i]))):
      if after and genome.endswith(sequences[i][:j]):
        genome = genome + sequences[i][j:]
        indexes.remove(i)
        after = False
      if before and sequences[i].endswith(genome[:j]):
        genome = sequences[i][:-j] + genome
        indexes.remove(i)
        before = False

print(genome)