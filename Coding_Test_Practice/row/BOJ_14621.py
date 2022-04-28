# Kruskal
import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = ['0'] + list(sys.stdin.readline().rstrip().split())
parents, q, total, count = [i for i in range(n+1)], [], 0, 0

for _ in range(m):
    u, v, d = map(int, sys.stdin.readline().rstrip().split())
    if lst[u] == lst[v]:
        continue
    heapq.heappush(q, [d, u, v])

def find(node):
    if parents[node] == node:
        return node
    else:
        parents[node] = find(parents[node])
        return parents[node]

def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2:
        return False
    else:
        parents[root2] = root1
        return True

while q:
    c, node1, node2 = heapq.heappop(q)
    if union(node1, node2):
        total += c
        count += 1
        if count == n-1:
            break

if count == n-1:
    print(total)
else:
    print(-1)
