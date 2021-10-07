# Dijkstra
import sys
import heapq
L, R, C, sX, sY, sZ, eX, eY, eZ = 0, 0, 0, 0, 0, 0, 0, 0, 0
dx, dy, dz = [1,-1,0,0,0,0], [0,0,1,-1,0,0], [0,0,0,0,1,-1]

def dijkstra(lst, distance):
    heap_data = []
    heapq.heappush(heap_data, (0, [sZ,sY,sX]))
    distance[sZ][sY][sX] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        nz, ny, nx = now[0], now[1], now[2]
        if distance[nz][ny][nx] < dist:
            continue
        for i in range(6):
            nnz, nny, nnx = nz + dz[i], ny + dy[i], nx + dx[i]
            if L > nnz >= 0 and R > nny >= 0 and C > nnx >= 0 and lst[nz][ny][nx] != '#':
                cost = dist + 1
                if distance[nnz][nny][nnx] > cost:
                    distance[nnz][nny][nnx] = cost
                    heapq.heappush(heap_data, (cost, [nnz,nny,nnx]))
    return distance[eZ][eY][eX]

while True:
    L, R, C = map(int, sys.stdin.readline().split())
    lst, distance = [], [[[1e9 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    if L == 0 and R == 0 and C == 0:
        break
    sX, eX = 31, 31
    for i in range(L):
        tmp = [list(str(sys.stdin.readline().rstrip())) for _ in range(R)]
        if sX >= 31 or eX >= 31:
            for j in range(0, R):
                for k in range(0, C):
                    if tmp[j][k] == 'S':
                        sZ, sY, sX = i, j, k
                    elif tmp[j][k] == 'E':
                        eZ, eY, eX = i, j, k
        sys.stdin.readline()
        lst.append(tmp)
    answer = dijkstra(lst, distance)
    if answer == 1e9:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)." %answer)
