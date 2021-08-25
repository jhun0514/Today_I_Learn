# DP
from sys import stdin

A, B = list(stdin.readline().rstrip()), list(stdin.readline().rstrip())
lst = [list(0 for _ in range(len(A)+1)) for _ in range(len(B)+1)]

for i in range(1, len(B)+1):
    for j in range(1, len(A)+1):
        if A[j-1] == B[i-1]:
            lst[i][j] = lst[i-1][j-1] + 1
        else:
            lst[i][j] = max(lst[i-1][j], lst[i][j-1])

print(lst[len(B)][len(A)])
