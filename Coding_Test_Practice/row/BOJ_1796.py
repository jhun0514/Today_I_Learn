# Dynamic Programming
from sys import stdin

N = stdin.readline().rstrip()
dp, index, count, find = [[0 for _ in range(len(N))] for _ in range(26)], [[-1,-1] for _ in range(26)], -1, True

if not N:
    print(0)
    exit(0)

for i in range(26):
    tmp = chr(i + 97)
    index[i][0], index[i][1] = N.find(tmp), N.rfind(tmp)

def dist(a,b,c,d):
    distance = abs(a-c) + abs(c-d) + abs(b-d)
    return distance

# DP calculate
for i in range(26):
    if index[i][0] != -1:
        if find: # DP base
            for x in range(len(N)):
                dp[i][x] = dist(0, x, index[i][0], index[i][1])
            find, count = False, i
            continue
        for j in range(len(N)):
            minTemp = []
            for z in range(len(N)):
                distances = min(dist(z,j,index[i][0],index[i][1]), dist(z,j,index[i][1],index[i][0]))
                minTemp.append(dp[count][z] + distances)
            if len(minTemp) > 0:
                dp[i][j] = min(minTemp)
        count = i
print(min(dp[count]) + len(N))
