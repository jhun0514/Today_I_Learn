# Simulation
from sys import stdin
from collections import defaultdict
import heapq
R, C, M = map(int, stdin.readline().split())
# A = [list(map(int, stdin.readline().split())) for _ in range(M)]
dic, count = defaultdict(list), 0
if M == 0:
    print(0)
    exit(0)
for _ in range(M):
    r, c, s, d, z = map(int, stdin.readline().split())
    heapq.heappush(dic[c], [r,z,s,d])

for i in range(1, C+1):
    print(dic)
    if dic[i]:
        r, z, s, d = heapq.heappop(dic[i])
        print(i,r,z,s,d)
        count += z
    temp = defaultdict(list)
    for key, value in dic.items():
        for k in value:
            nr, nz, ns, nd = k
            nc = key
            # if nd == 1:
            #     ind = abs(nr - (ns + abs(R - ns)))
            #     if ind > R:
            #         nr = ind % R
            #         nd = 1 if (ind // R) % 2 == 0 else 2
            #     else:
            #         nr, nd = ind, 1 if (ind // R) % 2 == 0 else 2
            # elif nd == 2:
            #     ind = abs(nr + (ns + abs(R - ns)))
            #     if ind > R:
            #         nr = ind % R
            #         nd = 2 if (ind // R) % 2 == 0 else 1
            #     else:
            #         nr, nd = ind, 2 if (ind // R) % 2 == 0 else 1
            # elif nd == 3:
            #     ind = abs(nc + (ns + abs(C - ns)))
            #     if ind > R:
            #         nc = ind % R
            #         nd = 3 if (ind // R) % 2 == 0 else 4
            #     else:
            #         nc, nd = ind, 3 if (ind // R) % 2 == 0 else 4
            #     if nr == 2 and nz == 5:
            #         print(nc)
            # elif nd == 4:
            #     ind = abs(nc - (ns + abs(C - ns)))
            #     if ind > R:
            #         nc = ind % R
            #         nd = 4 if (ind // R) % 2 == 0 else 3
            #     else:
            #         nc, nd = ind, 4 if (ind // R) % 2 == 0 else 3
            if nd < 3:
                nns = ns % ((R - 1) * 2)
                while nns > 0:
                    if nd == 2:
                        nr += 1
                        if nr > R:
                            nd = 4
                            nr -= 2
                    else:
                        nr -= 1
                        if nr < 1:
                            nd = 3
                            nr += 2
                    nns -= 1
            else:
                nns = ns%((C-1)*2)
                while nns > 0:
                    if nd == 3:
                        nc += 1
                        if nc > C:
                            nd = 4
                            nc -= 2
                    else:
                        nc -= 1
                        if nc < 1:
                            nd = 3
                            nc += 2
                    nns -= 1
                heapq.heappush(temp[nc], [nr,nz,ns,nd])
    dic = temp

    for l in dic:
        for i in range(len(dic[l])):
            if i+1 < len(dic[l]):
                if dic[l][i][0] == dic[l][i+1][0]:
                    dic[l].pop(i)

print(count)
