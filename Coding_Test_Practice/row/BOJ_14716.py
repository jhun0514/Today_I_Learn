# BFS
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
lst, answer, dx, dy = [list(map(int, sys.stdin.readline().split())) for _ in range(M)], 0, [0,1,0,-1,1,1,-1,-1],[1,0,-1,0,1,-1,-1,1]
visited = [[False for _ in range(N)] for _ in range(M)]

def bfs(x,y):
    arr = deque()
    arr.append([x, y])
    visited[x][y] = True
    while arr:
        px, py = arr.popleft()
        for z in range(8):
            nx, ny = px+dx[z], py+dy[z]
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if lst[nx][ny]:
                        arr.append([nx,ny])

for i in range(M):
    for j in range(N):
        if not visited[i][j] and lst[i][j]:
            answer += 1
            bfs(i,j)
print(answer)
