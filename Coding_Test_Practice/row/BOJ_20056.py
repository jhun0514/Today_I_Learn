# Simulation
from sys import stdin
N, M, K = map(int, stdin.readline().split())
lst, direc, answer = [[[] for _ in range(N)] for __ in range(N)], [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)], 0

for _ in range(M):
    r, c, m, s, d = map(int, stdin.readline().split())
    lst[r-1][c-1].append((m, s, d))
for i in range(K):
    tmp, save = [[[] for _ in range(N)] for __ in range(N)], []
    for x in range(N):
        for y in range(N):
            for elem in lst[x][y]:
                nm, ns, nd = elem
                nx, ny = x+direc[nd][0]*(ns%N), y+direc[nd][1]*(ns%N)
                if nx < 0:
                    nx = N + nx
                if ny < 0:
                    ny = N + ny
                if nx >= N:
                    nx = nx- N
                if ny >=N:
                    ny = ny- N
                if tmp[nx][ny]:
                    if (nx, ny) not in save:
                        save.append((nx,ny))
                tmp[nx][ny].append((nm, ns, nd))

    for ind in save:
        x, y = ind
        nm, ns, nd, check, count = 0, 0, [0,2,4,6], [], 0
        for fire in tmp[x][y]:
            m, s, d = fire
            nm += m
            ns += s
            count += 1
            check.append(d)
        nm, ns, find = int(nm/5), int(ns/count), check[0]%2
        if nm == 0:
            tmp[x][y] = []
            continue
        for j in range(1,len(check)):
            if check[j]%2 != find:
                nd = [1,3,5,7]
                break
        tmp[x][y] = [(nm, ns, nd[0]), (nm, ns, nd[1]), (nm, ns, nd[2]), (nm, ns, nd[3])]
    lst = tmp

for x in range(N):
    for y in range(N):
        for elem in lst[x][y]:
            answer += elem[0]
print(answer)
