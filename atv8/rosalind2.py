import sys
import Bio
from Bio.Seq import MutableSeq

seq = ""
sequencias = []
linhas = sys.stdin.readlines()
#print(linhas)

for i in range(1, len(linhas)):
    if ">" not in linhas[i]:
        seq += linhas[i].strip()
    else:
        sequencias.append(Bio.Seq.MutableSeq(seq))
        seq = ""
sequencias.append(seq)

#for i in range(len(sequencias)):
#    sequencias[i] = Bio.Seq.MutableSeq(sequencias[i])

dna = sequencias.pop(0)
sequencias.sort(reverse = True, key = len)
for i in range(0, len(sequencias)):
  dna = dna.replace(sequencias[i], "")

proteina = dna.translate()
print(proteina[:len(proteina)-1])
