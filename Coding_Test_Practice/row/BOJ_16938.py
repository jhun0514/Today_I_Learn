# Brute Force
import sys
from itertools import combinations

N, L, R, X = map(int, sys.stdin.readline().split())
lst, count = list(map(int, sys.stdin.readline().split())), 0

for i in range(2, N+1):
    temp = list(combinations(lst, i))
    for j in temp:
        if L <= sum(j) <= R and (max(j) - min(j)) >= X:
            count += 1
print(count)
