# DP
import sys
sys.setrecursionlimit(10**6)

lst = list(map(int, sys.stdin.readline().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(100000)]

def step(a, b):
    if a == b:
        return 1
    elif a == 0:
        return 2
    elif abs(b - a) == 2:
        return 4
    else:
        return 3

def dfs(n, l, r):
    if n >= len(lst) - 1: # 마지막
        return 0

    if dp[n][l][r] != -1: # 재귀중 이미 값이 있는 경우
        return dp[n][l][r]

    dp[n][l][r] = min(dfs(n + 1, lst[n], r) + step(l, lst[n]), dfs(n + 1, l, lst[n]) + step(r, lst[n]))
    return dp[n][l][r]

print(dfs(0, 0, 0))
