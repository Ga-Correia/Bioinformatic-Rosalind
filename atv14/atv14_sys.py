import sys
import Bio

profile_matrix = {
    "A": [],
    "C": [],
    "G": [],
    "T": []
}
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

countA = 0
countC = 0
countG = 0
countT = 0
consensus_str = ""

for j in range(len(sequences[0])):
    for i in range(len(sequences)):
        if sequences[i][j] == "A":
            countA +=1
        elif sequences[i][j] == "C":
            countC +=1
        elif sequences[i][j] == "G":
            countG +=1
        elif sequences[i][j] == "T":
            countT +=1
    profile_matrix["A"].append(countA)
    profile_matrix["C"].append(countC)
    profile_matrix["G"].append(countG)
    profile_matrix["T"].append(countT)
    if max(countA, countC, countG, countT) == countA:
        consensus_str += "A"
    elif max(countA, countC, countG, countT) == countC:
        consensus_str += "C"
    elif max(countA, countC, countG, countT) == countG:
        consensus_str += "G"
    elif max(countA, countC, countG, countT) == countT:
        consensus_str += "T"
    countA = 0
    countC = 0
    countG = 0
    countT = 0

print(consensus_str)
print("A: ", end="")
for v in profile_matrix["A"]:
    print(v, end=" ")
print()
print("C: ", end="")
for v in profile_matrix["C"]:
    print(v, end=" ")
print()
print("G: ", end="")
for v in profile_matrix["G"]:
    print(v, end=" ")
print()
print("T: ", end="")
for v in profile_matrix["T"]:
    print(v, end=" ")
print()