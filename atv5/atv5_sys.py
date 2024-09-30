import sys

lines = sys.stdin.readlines()

for i in range(1, len(lines), 2):
    sys.stdout.writelines(lines[i])
