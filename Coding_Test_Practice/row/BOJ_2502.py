# DP
from sys import stdin
D, K = map(int, stdin.readline().split())
dp, xCount, yCount = [[] for _ in range(30)], 0, 0
dp[0], dp[1] = ['x'], ['y']

for i in range(2, D):
    dp[i] = dp[i-2] + dp[i-1]

xCount, yCount = dp[D-1].count('x'), dp[D-1].count('y')

for i in range(int(K/2)):
    if (K - xCount * i) % yCount == 0:
        print(i)
        print((K - xCount * i) // yCount)
        break
