# Kruskal
import sys
import math

n = int(sys.stdin.readline())
location = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
parent, lst, answer = [i for i in range(n+1)], [], 0

for i in range(n-1):
    for j in range(i+1,n):
        ijDis = round(math.sqrt((location[i][0] - location[j][0]) ** 2 + (location[i][1] - location[j][1]) ** 2),2)
        lst.append((ijDis,i,j))
lst.sort(key=lambda x: x[0])

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if px < py:
        parent[py] = px
    elif px > py:
        parent[px] = py
    else:
        return

for l, x, y in lst:
    if find(x) != find(y):
        union(x,y)
        answer += l
print(answer)
