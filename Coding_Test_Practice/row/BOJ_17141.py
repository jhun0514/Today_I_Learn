#BFS
import sys
from collections import deque
import itertools

N, M = map(int,sys.stdin.readline().split())
lst, dx, dy = list(list(map(int,sys.stdin.readline().split())) for _ in range(N)), [-1,0,1,0],[0,1,0,-1]
queue, virus, empty, answer = deque(), [], 0, 1e9

def bfs(cLst):
    global answer
    count, times = 0, 0
    while queue:
        x, y = queue.popleft()
        times = cLst[x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if N > nx >= 0 and N > ny >= 0:
                if lst[nx][ny] != 1 and cLst[nx][ny] == -1:
                    cLst[nx][ny] = cLst[x][y]+1
                    queue.append((nx, ny))
                    count += 1
    if count == empty:
        answer = min(answer, times)

for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            virus.append((i, j))
        if lst[i][j] == 0:
            empty += 1
empty = empty + len(virus) - M
comb = itertools.combinations(virus, M)
for i in comb:
    nLst = list([-1]*N for _ in range(N))
    for j in range(M):
        x, y = i[j]
        queue.append((x, y))
        nLst[x][y] = 0
    bfs(nLst)
print(answer if answer != 1e9 else -1)
