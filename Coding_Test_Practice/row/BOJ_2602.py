# DP
import sys

letters = sys.stdin.readline()
up = sys.stdin.readline()
down = sys.stdin.readline()

dp, answer = [[[0] * 2 for _ in range(len(letters))] for _ in range(len(up))], 0

# Base case: 처음 갈 수 있는 부분
for i in range(len(up)):
    if up[i] == letters[0]:
        dp[i][0][0] = 1
    if down[i] == letters[0]:
        dp[i][0][1] = 1

for i in range(len(up)):
    for j in range(1, len(letters)):
        if up[i] == letters[j]:
            for k in range(i):
                dp[i][j][0] += dp[k][j - 1][1]

        if down[i] == letters[j]:
            for k in range(i):
                dp[i][j][1] += dp[k][j - 1][0]

for i in range(len(up)):
    answer += (dp[i][len(letters) - 1][0] + dp[i][len(letters) - 1][1])

print(answer)
