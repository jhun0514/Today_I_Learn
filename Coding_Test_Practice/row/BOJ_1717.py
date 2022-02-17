# Union Find
import sys
sys.setrecursionlimit(1000000) # union and find

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N + 1)]

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

for i in range(M):
    sign, a, b = map(int, sys.stdin.readline().split())
    if sign == 0:
        union(a, b)
    elif sign == 1:
        if find(a) == find(b):
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
