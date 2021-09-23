# BFS
import sys
from collections import deque
T = int(sys.stdin.readline())
dx, dy, aList = [0, 1, 0, -1], [1, 0, -1, 0], []
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
maxH, minH = max(map(max, lst)), min(map(min, lst))

for i in range(minH, maxH+1):
    visited, count = [[0 for _ in range(T)] for __ in range(T)], 0
    for a in range(T):
        for b in range(T):
            if not visited[a][b] and lst[a][b] >= i:
                q = deque([(a,b)])
                visited[a][b] = 1
                while q:
                    x, y = q.popleft()
                    for j in range(4):
                        nx, ny = x+dx[j], y+dy[j]
                        if 0 <= nx < T and 0 <= ny < T:
                            if not visited[nx][ny] and lst[nx][ny] >= i:
                                visited[nx][ny] = 1
                                q.append((nx, ny))
                count += 1
    aList.append(count)

print(max(aList))
