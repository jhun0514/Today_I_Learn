# BFS
import sys
from collections import deque
N, S, E = map(int, sys.stdin.readline().split())
adj, visited, dista, routes = [[] for _ in range(N+1)], [False]*(N+1), [1e9]*(N+1), [0]*(N+1)

for _ in range(N-1):
    x, y, dist = map(int, sys.stdin.readline().split())
    adj[x].append((y, dist))
    adj[y].append((x, dist))

def bfs(s):
    q, dista[s], routes[s] = deque([s]), 0, 0
    while q:
        v = q.popleft()
        if v == E:
            return
        if not (visited[v]):
            visited[v] = True
            for e, cost in adj[v]:
                if not visited[e]:
                    dista[e] = dista[v] + cost
                    routes[e] = v
                    q.append(e)

bfs(S)
ind, maxD = E, 0
while routes[ind] != 0:
    tmp = routes[ind]
    for y, c in adj[ind]:
        if y == tmp:
            ind = y
            if c > maxD:
                maxD = c
print(dista[E]-maxD)
