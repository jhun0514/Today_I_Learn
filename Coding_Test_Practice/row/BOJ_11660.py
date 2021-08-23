# DP
from sys import stdin
N, M = map(int, stdin.readline().split())
lst, prefixS = [list(map(int, stdin.readline().split())) for _ in range(N)], []

for x in range(N):
    tmp, ind = [], 0
    for y in range(N):
        ind += lst[x][y]
        tmp.append(ind)
    prefixS.append(tmp)

for _ in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    count = 0
    for i in range(x1-1,x2):
        if y1 != 1:
            count -= prefixS[i][y1-2]
        count += prefixS[i][y2-1]
    print(count)
