# Floyd-Warshall
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
lst = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    lst[a - 1][b - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if lst[i][k] and lst[k][j]:
                lst[i][j] = 1

for i in range(N):
    ans = 0
    for j in range(N):
        if i == j:
            continue
        if not lst[i][j] and not lst[j][i]:
            ans += 1
    print(ans)
