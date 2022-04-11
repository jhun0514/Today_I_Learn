# DP
import sys

N = int(sys.stdin.readline())
dp = [1 for _ in range(31)]

# 1x2 + 2x1 or 2x2
for i in range(2, 31):
    dp[i] = dp[i-1] + dp[i-2]*2

if N%2 == 1: # 홀수인 경우 = 1x2 1개 뺀 나머지 /2
    answer = int((dp[N] + dp[int((N - 1) / 2)]) / 2)
else: # 짝수인 경우 = 2x1 or 2x2 1개 뺀 나머지 /2 + 깔끔하게 나누기 /2
    answer = int((dp[N] + dp[int(N/2)] + dp[int(N/2 - 1)] * 2) / 2)
print(answer)

# dp[n] = 좌우대칭 + 뒤집었을때 좌우대칭
# 총 경우 = 좌우대칭 + 뒤집었을때 좌우대칭/2 = (dp[n] + 좌우대칭)/2
