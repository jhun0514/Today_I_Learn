# Simulation
from sys import stdin

L, R = stdin.readline().split()
count = 0
if len(L) != len(R) or '8' not in L or '8' not in R:
    print(0)
else:
    for i in range(len(L)):
        if L[i] != '8' or R[i] != '8':
            if L[i] == R[i]:
                continue
            else:
                print(count)
                exit(0)
        else:
            count += 1
    print(count)
