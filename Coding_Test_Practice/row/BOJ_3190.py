# Simulation
import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
lst, move, dx, dy, count, r, c, d, ind = list([0]*N for _ in range(N)), list(), [0,1,0,-1], [1,0,-1,0], 0, 0, 0, 0, 0
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    lst[x-1][y-1] = 1
L = int(sys.stdin.readline())
for i in range(L):
    x, y = sys.stdin.readline().split()
    move.append([int(x), y])

lst[r][c], save = -1, [(r,c)]
while(True):
    if (ind < L and move[ind][0] == count):
        if (move[ind][1] == "L"):
            d = (d-1)%4
        else:
            d = (d+1)%4
        ind+=1
    nr, nc = r+dx[d], c+dy[d]
    if (0<=nr<N and 0<=nc<N and lst[nr][nc] != -1):
        if lst[nr][nc] == 1:
            lst[nr][nc] = -1
            save.append((nr,nc))
        else:
            lst[nr][nc] = -1
            save.append((nr, nc))
            a, b = save.pop(0)
            lst[a][b] = 0
        r, c, count = nr, nc, count + 1
    else:
        count +=1
        break
print(count)
