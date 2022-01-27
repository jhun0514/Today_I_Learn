#dp
import sys

N = int(sys.stdin.readline().rstrip())
lst, answer = list(list(map(int,sys.stdin.readline().split())) for _ in range(N)), float('inf')

for i in range(3):
    dp = [[0]*N for _ in range(3)]
    for j in range(3):
        if i == j:
            dp[j][0] = lst[0][j]
            continue
        dp[j][0] = float('inf')
    for j in range(1,N):
        dp[0][j], dp[1][j], dp[2][j] = lst[j][0]+min(dp[1][j-1],dp[2][j-1]), lst[j][1]+min(dp[0][j-1],dp[2][j-1]), lst[j][2]+min(dp[1][j-1],dp[0][j-1])
    for j in range(3):
        if i == j:
            continue
        answer = min(answer, dp[j][-1])
print(answer)
