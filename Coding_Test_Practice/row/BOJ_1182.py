# Brute Force
from sys import stdin
import itertools
N, S = map(int, stdin.readline().split())
lst, count = list(map(int, stdin.readline().split())), 0

for i in range(1, N+1):
    nLst = itertools.combinations(lst, i)
    for li in nLst:
        if sum(li) == S:
            count += 1
print(count)
