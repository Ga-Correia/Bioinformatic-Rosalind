import sys
import Bio
from Bio.Seq import Seq

lines = sys.stdin.readlines()
sequences = []
seq = ""
frame123 = []
frame456 = []

for i in range(1, len(lines)):
    if ">" not in lines[i]:
        seq += lines[i].strip()
    else:
        sequences.append(seq)
        seq = ""
sequences.append(seq)
seq1 = Bio.Seq.Seq(sequences.pop(0))
seq2 = seq1.reverse_complement()

for i in range(0, 3):
    if len(seq1[i:]) % 3 == 0:
        frame123.append(seq1[i:].translate())
        frame456.append(seq2[i:].translate())
    elif len(seq1[i:]) % 3 == 1:
        frame123.append((seq1[i:]+Seq("NN")).translate())
        frame456.append((seq2[i:]+Seq("NN")).translate())
    elif len(seq1[i:]) % 3 == 2:
        frame123.append((seq1[i:]+Seq("N")).translate())
        frame456.append((seq2[i:]+Seq("N")).translate())    
frames = frame123+frame456

potences_proteins = []
for i in range(len(frames)):
    for j in range(len(frames[i])):
        if frames[i][j] == "M" and frames[i].find("*", j) != -1:
            potences_proteins.append(frames[i][j:frames[i].find("*", j)])
potences_proteins = list(set(potences_proteins))

for i in potences_proteins:
    print(i)
