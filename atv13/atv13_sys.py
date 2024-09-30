import sys
import Bio
from Bio.Align import substitution_matrices

BLOSUM62 = substitution_matrices.load('BLOSUM62')

def needleman_wunsch(seq1, seq2, gap):
    H = []
    seq1_aline = ""
    seq2_aline = ""
    for i in range(len(seq2)+1):
        H.append([])
    init = 0
    for i in range(len(seq1)+1):
        H[0].append(init)
        init = init + gap
    init = gap
    for i in range(1, len(seq2)+1):
        H[i].append(init)
        init = init - 5

    for i in range(1, len(seq2)+1):
        for j in range(1, len(seq1)+1):
            val = max(H[i-1][j-1] + (BLOSUM62[seq2[i-1]][seq1[j-1]]), H[i-1][j]+(gap), H[i][j-1]+(gap))
            H[i].append(val)
        print(H[i]) #printa toda matriz

    #Buscar o alinhamento entre seq1 e seq2
    score = int(H[i][j])
    while(i!=0) or (j!=0):
        if H[i][j] == (H[i-1][j-1] + (BLOSUM62[seq2[i-1]][seq1[j-1]]) ):
            seq1_aline += seq1[j-1]
            seq2_aline += seq2[i-1]
            i = i - 1
            j = j - 1
        elif H[i][j] == H[i-1][j]+(gap):
            seq1_aline += "-"
            seq2_aline += seq2[i-1]
            i = i - 1
        elif H[i][j] == H[i][j-1]+(gap):
            seq1_aline += seq1[j-1]
            seq2_aline += "-"
            j = j - 1
    
    #print(j, seq1[j])
    #print(i, seq2[i])
    print(seq1_aline[::-1])
    print(seq2_aline[::-1])
    return score


lines = sys.stdin.readlines()
sequences = []
seq = ""
for i in range(1, len(lines)):
    if ">" not in lines[i]:
        seq += lines[i].strip()
    else:
        sequences.append(seq)
        seq = ""
sequences.append(seq)

if sequences[0] > sequences[1]:
    print(needleman_wunsch(sequences[0], sequences[1], -1))
else:
    print(needleman_wunsch(sequences[1], sequences[0], -1))

