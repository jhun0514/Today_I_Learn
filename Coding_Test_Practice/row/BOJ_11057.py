# Dynamic programming
import sys
N = int(sys.stdin.readline())
dp = [[0 for i in range(10)] for _ in range(N)]
dp[0] = [1 for _ in range(10)]
for i in range(1, N):
    for j in range(10):
        for z in range(j, 10):
            dp[i][j] += dp[i-1][z]
print(sum(dp[N-1])%10007)
