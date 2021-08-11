# Greedy
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    lst, save = [list(map(int, stdin.readline().split())) for __ in range(N)], 1
    lst.sort()
    tmp = lst[0][1]

    for i in range(1, N):
        if lst[i][1] < tmp:
            save+=1
            tmp = lst[i][1]
    print(save)
