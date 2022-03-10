# DP
import sys

n, m = map(int, input().split())
lst, answer = [], 0
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().rstrip())))

for i in range(1, n):
    for j in range(1, m):
        if lst[i][j] != 0:
            lst[i][j] += min(lst[i-1][j], lst[i][j-1], lst[i-1][j-1])
for i in lst:
    maxV = max(i)
    answer = max(answer,maxV)
print(answer ** 2)
