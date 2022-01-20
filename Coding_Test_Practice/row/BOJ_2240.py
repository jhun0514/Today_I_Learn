# dp
import sys

T, W = map(int, sys.stdin.readline().split())
lst, dp = list(int(sys.stdin.readline().rstrip()) for _ in range(T)), [[0]*(W+1) for _ in range(T+1)]
lst.insert(0,0)

for i in range(1,T+1):
    if lst[i] == 1:
        dp[i][0] = dp[i-1][0]+1
    else:
        dp[i][0] = dp[i-1][0]
    for j in range(1,W+1):
        if j > i:
            break
        if (j%2 == 0 and lst[i] == 1) or (j%2 == 1 and lst[i] == 2):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[-1]))
