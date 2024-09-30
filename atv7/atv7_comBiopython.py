import Bio
from Bio import Seq
from Bio import SeqUtils

fl = open("rosalind_gc.txt", "r")
linhas =  fl.readlines()
sequencias = []
seq = ""
hash = dict()
hash[linhas[0]] = seq

for i in range(1, len(linhas)):
  if ">" not in linhas[i]:
    seq += linhas[i]
  else:
    hash[linhas[i]] = ""
    sequencias.append(seq)
    seq = ""
sequencias.append(seq)

for i in range(0, len(sequencias)):
  sequencias[i] = Bio.Seq.Seq(sequencias[i].replace("\n", ""))

i = 0
maximo = 0
chave = ""

for k in hash:
  hash[k] = round(100*Bio.SeqUtils.gc_fraction(sequencias[i]), 6)
  if hash[k] > maximo:
    maximo = hash[k]
    chave = k
  i = i+1

print(chave.replace(">", ""), end="")
print(maximo)
