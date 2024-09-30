import sys
import Bio
from Bio import pairwise2
from Bio.Align import substitution_matrices

BLOSUM62 = substitution_matrices.load('BLOSUM62')
"""
def needleman_wunsch(seq1, seq2):
    H = []
    gap = -5
    for i in range(len(seq2)+1):
        H.append([])
    
    init = 0
    for i in range(len(seq1)+1):
        H[0].append(init)
        init = init - 5
    init = -5
    for i in range(1, len(seq2)+1):
        H[i].append(init)
        init = init - 5

    for i in range(1, len(seq2)+1):
        for j in range(1, len(seq1)+1):
            val = max(H[i-1][j-1] + (BLOSUM62[seq2[i-1]][seq1[j-1]]), H[i-1][j]+(gap), H[i][j-1]+(gap))
            H[i].append(val)
        #print(H[i]) #printa toda matriz
    return int(H[i][j])
"""
lines = sys.stdin.readlines()
sequences = []
seq = ""
distances_matrix = {}
distances_matrix[lines[0]] = {}
seq_ids_indexes = [0]

for i in range(1, len(lines)):
    if lines[i].startswith(">") != True:
        seq += lines[i].strip()
    else:
        distances_matrix[lines[i]] = {}
        seq_ids_indexes.append(i)
        sequences.append(seq)
        seq = ""
sequences.append(seq)

control_flag = 0
for i in range(0, len(sequences)):
    for j in range(control_flag, len(sequences)):
        #if sequences[i] > sequences[j]:
        #   a = needleman_wunsch(sequences[i], sequences[j])
        #else:
        #    a = needleman_wunsch(sequences[j], sequences[i])
        a = pairwise2.align.globalds(sequences[i], sequences[j], BLOSUM62, -5, -5, score_only=True)
        distances_matrix[lines[seq_ids_indexes[i]]][lines[seq_ids_indexes[j]]] = a
    if i == 0:
        minimo = min(distances_matrix[lines[seq_ids_indexes[i]]], key=distances_matrix[lines[seq_ids_indexes[i]]].get)
    control_flag += 1

print(minimo, end="")