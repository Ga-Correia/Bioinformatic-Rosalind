import sys

lines = sys.stdin.readlines()
string =  lines.pop(0).strip()
numbers = list(map(int, lines[0].split()))
print(string)

a = numbers[0]
b = numbers[1]
c = numbers[2]
d = numbers[3]

print(string[a:b+1], string[c:d+1])