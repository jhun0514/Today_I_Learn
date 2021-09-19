# DP
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    total = int(sys.stdin.readline())
    d = [0]*(total+1)
    d[0] = 1
    for i in range(N):
        for j in range(coins[i], total+1):
            d[j] += d[j - coins[i]]
    print(d[total])
