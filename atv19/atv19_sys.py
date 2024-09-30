import sys
from math import sqrt

def euclidean_distance(p1, p2):
    sum = 0
    for i in range(len(p1)):
        sum += (p1[i] - p2[i])**2
    square = sqrt(sum)
    return square

lines = sys.stdin.readlines()
lin1 = lines[0].split()
K = int(lin1[0]) #numero de Ks q terei no centro
M = int(lin1[1]) #numero de Ms que terei no centro
pts = []
for i in range(1, len(lines)):
    pts.append(list(map(float, lines[i].split())))
centers = []
for i in range(0, K):
    centers.append(pts[i])

while True:
    attrs = {}
    for p in pts:
        dist = []
        for center in centers:
            dist.append(euclidean_distance(p, center))
        index_center = dist.index(min(dist))
        if index_center not in attrs:
            attrs[index_center] = []
        attrs[index_center].append(p)

    new_centers = []
    for index in range(0, K):
        point = []
        for i in range(0, M):
            sum = 0
            for p in attrs[index]:
                sum += p[i]
            mean = sum/len(attrs[index])
            point.append(mean)
        new_centers.append(point)
    if centers != new_centers:
        centers =  new_centers
    else:
        break

for center in centers:
    for c in center:
        print(f"{c:.3f}", end = " ")
    print()



