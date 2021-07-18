# 로봇 청소기

### 문제설명

로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 각 칸은 (r, c)로 나타낼 수 있고, r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수이다.

로봇 청소기는 다음과 같이 작동한다.

1. 현재 위치를 청소한다.
2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
    a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다. (BaekJoon 14503)

Rule 1: 첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50). 둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
Rule 2: 셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다. 로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.

ex)
- Input:

        3 3
        1 1 0
        1 1 1
        1 0 1
        1 1 1

- Output:

        1


### 핵심원리 - DFS approach

- DFS 탐색 접근법으로 주어진 지점부터 움직일수 없을때 까지 청소한다.

```python
# 최악의 경우 모든 점을 청소하므로 O(NM)
def dfs(x, y, direc):
    global res
    if not visited[x][y]:
        res += 1
    visited[x][y] = True

    for index, dxy in enumerate(direction[direc]):
        nx, ny = x+dxy[0], y+dxy[1]
        if 0 <= nx < N and 0 <= ny < M:
            if not lst[nx][ny] and not visited[nx][ny]:
                nd = compass[direc][index]
                dfs(nx,ny,nd)
            elif index == 3:
                nnx, nny = x + direction[direc][1][0], y + direction[direc][1][1]
                if 0 <= nnx < N and 0 <= nny < M and not lst[nnx][nny]:
                    dfs(nnx, nny, direc)
                else:
                    print(res)
                    sys.exit(0)
```


### 전체 코드

- O(NM) where N, M is a number of row and column of the matrix.

```python
# dfs
import sys
from sys import stdin

N, M = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
lst, res = list(list(map(int, stdin.readline().split())) for _ in range(N)), 0
visited = [[False] * M for _ in range(N)]
direction = [[(0, -1), (1, 0), (0, 1), (-1, 0)], [(-1, 0), (0, -1), (1, 0), (0, 1)],
             [(0, 1), (-1, 0), (0, -1), (1, 0)], [(1, 0), (0, 1), (-1, 0), (0, -1)]]
compass = [(3,2,1,0), (0,3,2,1), (1,0,3,2), (2,1,0,3)]

# 최악의 경우 모든 점을 청소하므로 O(NM)
def dfs(x, y, direc):
    global res
    if not visited[x][y]:
        res += 1
    visited[x][y] = True

    for index, dxy in enumerate(direction[direc]):
        nx, ny = x+dxy[0], y+dxy[1]
        if 0 <= nx < N and 0 <= ny < M:
            if not lst[nx][ny] and not visited[nx][ny]:
                nd = compass[direc][index]
                dfs(nx,ny,nd)
            elif index == 3:
                nnx, nny = x + direction[direc][1][0], y + direction[direc][1][1]
                if 0 <= nnx < N and 0 <= nny < M and not lst[nnx][nny]:
                    dfs(nnx, nny, direc)
                else:
                    print(res)
                    sys.exit(0)

dfs(r,c,d)
```

### 다른 풀이 by ells2124

- O(NM)으로 같은 개념으로 문제를 풀었지만 while 문을 이용했고 이동 방향을 수식으로 간소화 했다.

```python
import sys
q = lambda: list(map(int,sys.stdin.readline().split()))
m,n = q()
r,c,h = q()
mat = []
for _ in range(m):
	mat.append(q())

r_move = [0,-1,0,1]
c_move = [-1,0,1,0]

b = 1
cnt = 1
mat[r][c] = -1

while b :
	for i in range(4):
		nr = r + r_move[h]
		nc = c + c_move[h]
		h = (h+3) % 4

		if mat[nr][nc] == 0:
			mat[nr][nc] = -1
			r = nr
			c = nc
			cnt += 1
			check = 1
			break;
		else:
			check = 0

	if i == 3 and check == 0:
		nr = r + r_move[(h+3) % 4]
		nc = c + c_move[(h+3) % 4]
		if mat[nr][nc] == 1:
			b = 0
		else:
			r = nr
			c = nc
print(cnt)
```
