# Brute Force
import sys

N, M = map(int, sys.stdin.readline().split())
lst = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    lst[x-1][y-1] = 1
for i in range(N):
    for x in range(N):
        for y in range(N):
            if lst[x][i] and lst[i][y]:
                lst[x][y] = 1

count = [0 for i in range(N)]
for i in range(N):
    for j in range(N):
        if lst[i][j]:
            count[i] += 1
            count[j] += 1

print(count.count(N-1))
