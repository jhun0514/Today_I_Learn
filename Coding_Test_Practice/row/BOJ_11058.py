# dp
import sys

n = int(sys.stdin.readline())
dp = [i for i in range(0, 101)]

for i in range(7, n+1):
    dp[i] = max(dp[i-3]*2, max(dp[i-4]*3, dp[i-5]*4))
print(dp[n])
