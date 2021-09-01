# Dynamic programming
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(input())
    lst = [0] + [1] * 10
    for _ in range(N):
        for j in range(1, 11):
            lst[j] += lst[j - 1]
    print(lst[10])
