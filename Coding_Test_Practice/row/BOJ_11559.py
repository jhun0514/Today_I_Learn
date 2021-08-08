# BFS
from sys import stdin
from collections import deque

N = [list(stdin.readline().rstrip()) for _ in range(12)]
count, change, visited, dx, dy = 0, True, [], [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(i, j):
    global visited
    check, q, index, save = False, deque([(i,j)]), 0, []
    while q:
        x, y = q.popleft()
        if (x,y) not in visited:
            visited.append((x,y))
            save.append((x,y))
            index += 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 12 and 0 <= ny < 6 and N[x][y] == N[nx][ny]:
                    if (nx, ny) not in visited:
                        q.append((nx,ny))
    if index >= 4:
        check = True
        for x, y in save:
            N[x][y] = '.'
    return check

def reform():
    for i in range(6):
        for j in range(11, -1, -1):
            if N[j][i] == '.':
                tmp = j-1
                while tmp > -1:
                    if N[tmp][i] != '.':
                        N[j][i] = N[tmp][i]
                        N[tmp][i] = '.'
                        break
                    tmp -= 1

while change:
    change, visited = False, []
    for i in range(12):
        for j in range(6):
            if N[i][j] == '.' or (i,j) in visited:
                continue
            else:
                x = bfs(i,j)
                if not change:
                    change = x
    if change:
        count += 1
        reform()

print(count)
