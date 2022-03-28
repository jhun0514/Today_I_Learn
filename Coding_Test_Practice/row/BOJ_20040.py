# Union & Find
import sys

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

flag = True

for i in range(m):
    x, y = map(int, input().split())

    if find_parent(parent, x) == find_parent(parent, y):
        print(i+1)
        flag = False
        break
    else:
        union_parent(parent, x, y)

if flag:
    print(0)
