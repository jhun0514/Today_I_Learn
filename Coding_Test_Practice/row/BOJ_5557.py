# DP
import sys
N = int(sys.stdin.readline())
lst, dp = list(map(int, sys.stdin.readline().split())), [[0] * 21 for i in range(N)]
dp[0][lst[0]] = 1
for i in range(1, N-1):
    for j in range(21):
        if dp[i - 1][j]:
            if 0 <= j + lst[i] <= 20:
                dp[i][j + lst[i]] += dp[i - 1][j]
            if 0 <= j - lst[i] <= 20:
                dp[i][j - lst[i]] += dp[i - 1][j]
print(dp[N-2][lst[-1]])

# 8 3 2 4 8 7 2 4 0 8 8
# DP[0][num] = 현재 식에 0번째(8)를 더할때 num으로 갈 수 있는 경우의 수
