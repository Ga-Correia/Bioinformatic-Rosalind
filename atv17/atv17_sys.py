import sys
#import itertools

"""
def overlap(str1, str2, min=3):
    start = 0
    while True:
        start = str1.find(str2[:min], start)
        if start == -1:
            return 0
        if str2.startswith(str1[start:]):
            return len(str1) - start
        start += 1
"""
        
lines = sys.stdin.readlines()
sequences = []
seq = ""
for i in range(1, len(lines)):
    if lines[i].startswith(">") != True:
        seq += lines[i].strip()
    else:
        sequences.append(seq)
        seq = ""
sequences.append(seq)


genome = sequences[0]
indexes = []
for i in range(1, len(sequences)):
    indexes.append(i)

while len(indexes)>0:
    for i in indexes:
        after = True
        before = True
        for j in reversed(range(int(len(sequences[i])/2 ), len(sequences[i]) ) ):
            if after and genome.endswith(sequences[i][:j]):
                genome = genome + sequences[i][j:]
                after = False
                indexes.remove(i)
            if before and sequences[i].endswith(genome[:j]):
                genome = sequences[i][:-j] + genome
                before = False
                indexes.remove(i)
print(genome)


"""
genome = None
for seq_perm in itertools.permutations(sequences):
    perm_tmp = seq_perm[0]
    for i in range(len(sequences)-1):
        olen = overlap(seq_perm[i], seq_perm[i+1], min=1)
        perm_tmp += sequences[i][olen:]
    if genome is None or len(perm_tmp) < len(genome):
        genome = perm_tmp
print(genome)
"""