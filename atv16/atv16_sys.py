import sys

lines = sys.stdin.readlines()
sequences = []
len_sum = 0
for i in range(len(lines)):
    sequences.append(lines[i].strip())
    len_sum += len(sequences[i])

count_lens = 0
N50 = False
N75 = False
for i in range(len(sequences)):
    max_seq = max(sequences, key=len)
    count_lens += len(max_seq)
    sequences.remove(max_seq)
    if count_lens >= (len_sum*0.5) and N50 == False:
        print(len(max_seq), end=" ")
        N50 = True
    if count_lens >= (len_sum*0.75) and N75 == False:
        print(len(max_seq))
        N75 = True
