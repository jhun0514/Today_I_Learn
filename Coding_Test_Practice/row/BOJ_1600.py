# Bfs
import sys
import collections

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())
table, dx, dy = [list(map(int, sys.stdin.readline().split())) for _ in range(H)], [0, 0, 1, -1], [1, -1, 0, 0]
hx, hy, visited = [-1, -2, -1, -2, 1, 2, 1, 2], [-2, -1, 2, 1, -2, -1, 2, 1], [[[0] * (K+1) for _ in range (W)]for _ in range(H)]

def bfs(a, b):
    q = collections.deque()
    q.append((a, b, 0, 0))
    visited[a][b][0] = 1
    while q:
        x, y, horseMove, count = q.popleft()

        if x == H - 1 and y == W - 1:
            return count

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if visited[nx][ny][horseMove] == 0:
                    if table[nx][ny] == 0:
                        visited[nx][ny][horseMove] = 1
                        q.append((nx, ny, horseMove, count + 1))

        if horseMove < K:
            for i in range(8):
                nx, ny = x + hx[i], y + hy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if visited[nx][ny][horseMove + 1] == 0:
                        if table[nx][ny] == 0:
                            visited[nx][ny][horseMove + 1] = 1
                            q.append((nx, ny, horseMove + 1, count + 1))
    return -1

print(bfs(0, 0))
