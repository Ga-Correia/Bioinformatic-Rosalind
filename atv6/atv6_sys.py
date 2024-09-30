import sys
lines =  sys.stdin.readlines()
palavras = lines.pop(0).strip().split()
hash = {}

for i in palavras:
    if i not in hash:
        hash[i] = 0
    hash[i] += 1

for k, v in hash.items():
    print(k, v)