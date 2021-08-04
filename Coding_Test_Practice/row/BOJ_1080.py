# Greedy
from sys import stdin
N, M = map(int, stdin.readline().split())
A, B = [list(map(int, stdin.readline().rstrip())) for _ in range(N)], [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
check, point = [[-1 for i in range(M)] for _ in range(N)], 0

if N < 3 or M < 3:
    if A != B:
        print(-1)
    else:
        print(0)
else:
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                check[i][j] = 1
    for i in range(N):
        for j in range(M):
            if check[i][j] == 1:
                if i < N-2 and j < M-2:
                    point += 1
                    for x in range(i, i+3):
                        for y in range(j, j+3):
                            check[x][y] *= -1
                else:
                    print(-1)
                    exit(0)
    print(point)
