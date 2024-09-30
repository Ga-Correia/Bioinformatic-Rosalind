import sys
import Bio
from Bio import SeqUtils
from Bio import Seq

def GC_count(seq):
    return (seq.count("G")+seq.count("C"))/len(seq)

lines = sys.stdin.readlines()
sequences = []
seq = ""
hash = {}
hash[lines[0]] = seq

for i in range(1, len(lines)):
    if ">" not in lines[i]:
        seq += lines[i].strip()
    else:
        sequences.append(seq)
        hash[lines[i]] = 0
        seq = ""
sequences.append(seq)

i = 0
maximo = 0
chave = None
for k in hash:
    #hash[k] = round(100*SeqUtils.gc_fraction(sequences[i]), 6)
    hash[k] = round(100*GC_count(str(sequences[i])), 6)
    #if hash[k] > maximo:
     #   maximo = hash[k]
      #  chave = k
    i+1

max_funct = max(hash)
#chave = chave.replace(">", "")
#print(chave, end="")
print(max_funct, end="")
print(hash[max_funct])