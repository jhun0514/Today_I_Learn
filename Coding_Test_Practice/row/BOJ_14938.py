# Floyd
import sys

N, m, r = map(int, sys.stdin.readline().split())
item = [0] + list(map(int, sys.stdin.readline().split()))
lst, answer = [[100 for _ in range(N+1)] for _ in range(N+1)], 0

for i in range(N+1):
    lst[i][i] = 0

for _ in range(r):
    a, b, dist = map(int, sys.stdin.readline().split())
    lst[a][b] = dist
    lst[b][a] = dist

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if lst[i][j] > lst[i][k] + lst[k][j]:
                lst[i][j] = lst[i][k] + lst[k][j]

for i in range(1, N+1):
    tmp = [item[x] for x in range(1, N+1) if lst[i][x] <= m]
    answer = max(answer, sum(tmp))
print(answer)
