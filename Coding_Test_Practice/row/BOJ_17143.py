# Simulation
from sys import stdin
R, C, M = map(int, stdin.readline().split())
dic, count, d = [[0 for _ in range(C)] for __ in range(R)], 0, [(-1,0),(1,0),(0,1),(0,-1)]
if M == 0:
    print(0)
    exit(0)
for _ in range(M):
    r, c, s, d, z = map(int, stdin.readline().split())
    dic[r-1][c-1] = (s, d-1, z)

for i in range(C):
    for ind in range(R):
        if dic[ind][i] != 0:
            s, d, z = dic[ind][i]
            dic[ind][i], count = 0, count + z
            break
    tmp = [[0 for _ in range(C)] for __ in range(R)]
    for x in range(R):
        for y in range(C):
            if dic[x][y] != 0:
                ns, nd, nz = dic[x][y]
                nx, ny = x, y
                if nd < 2:
                    nns = ns % ((R - 1) * 2)
                    for __ in range(nns):
                        if nd == 1:
                            nx += 1
                            if nx >= R:
                                nd = 0
                                nx -= 2
                        else:
                            nx -= 1
                            if nx < 0:
                                nd = 1
                                nx += 2
                else:
                    nns = ns % ((C-1)*2)
                    for __ in range(nns):
                        if nd == 2:
                            ny += 1
                            if ny >= C:
                                nd = 3
                                ny -= 2
                        else:
                            ny -= 1
                            if ny < 0:
                                nd = 2
                                ny += 2
                if tmp[nx][ny] == 0 or nz > tmp[nx][ny][2]:
                    tmp[nx][ny] = (ns, nd, nz)
    dic = tmp
print(count)
