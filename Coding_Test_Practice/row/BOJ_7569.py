# BFS
from sys import stdin
from collections import deque
M, N, H = map(int, stdin.readline().split())
A, q, tmp, count = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(H)], deque(), [], 0
dx, dy, dz = [0, 1, 0, -1], [1, 0, -1, 0], [1, -1]
for i in range(H):
    for j in range(N):
        for z in range(M):
            if A[i][j][z] == 1:
                tmp.append((i,j,z))
q.append(tmp)
def bfs():
    global count
    while q:
        t = q.popleft()
        ind = []
        for z, x, y in t:
            for i in range(2):
                nz = z+dz[i]
                if 0 <= nz < H and A[nz][x][y] == 0:
                    A[nz][x][y] = 1
                    ind.append((nz,x,y))
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and A[z][nx][ny] == 0:
                    A[z][nx][ny] = 1
                    ind.append((z, nx, ny))
        if len(ind) > 0:
            q.append(ind)
        count += 1
bfs()
for i in range(H):
    for j in range(N):
        if A[i][j].count(0) > 0:
            print(-1)
            exit(0)
print(count-1)
