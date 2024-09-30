import sys

lines = sys.stdin.readlines()
seq = lines.pop(0).strip()
rev = seq[::-1]
hash = {"A": "T", "T": "A", "G": "C", "C": "G"}
complement_rev = ""

for i in range(len(rev)):
    complement_rev += hash[rev[i]]
print(complement_rev)
