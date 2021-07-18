# 치즈

### 문제설명

아래 <그림 1>과 같이 정사각형 칸들로 이루어진 사각형 모양의 판이 있고, 그 위에 얇은 치즈(회색으로 표시된 부분)가 놓여 있다. 판의 가장자리(<그림 1>에서 네모 칸에 X친 부분)에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.

이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다. 치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다.
입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때, 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오. (BaekJoon 2636)

Rule 1: 첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다. 세로와 가로의 길이는 최대 100이다.
Rule 2: 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.

ex)
- Input:

        13 12
        0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 1 1 0 0 0
        0 1 1 1 0 0 0 1 1 0 0 0
        0 1 1 1 1 1 1 0 0 0 0 0
        0 1 1 1 1 1 0 1 1 0 0 0
        0 1 1 1 1 0 0 1 1 0 0 0
        0 0 1 1 0 0 0 1 1 0 0 0
        0 0 1 1 1 1 1 1 1 0 0 0
        0 0 1 1 1 1 1 1 1 0 0 0
        0 0 1 1 1 1 1 1 1 0 0 0
        0 0 1 1 1 1 1 1 1 0 0 0
        0 0 0 0 0 0 0 0 0 0 0 0

- Output:

        3
        5


### 핵심원리 - BFS approach

- BFS 접근법으로 공기와 맞닿아있는 부분 부터 탐색하였다. 1차 탐색 후 부터는 이전 탐색 장소만 BFS로 탐색한다.

```python
def bfs():
    global lst
    tmp, copyLst = set(), copy.deepcopy(lst)
    while que:
        x, y = que.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if lst[nx][ny] == 0:
                        que.append((nx,ny))
                    else:
                        copyLst[nx][ny] = 0
                        tmp.add((nx,ny))
    lst = copyLst
    return tmp
```


### 전체 코드

- O(NM) where N, M is a number of rows and columns.

```python
# Queue
from sys import stdin
from collections import deque
import copy

N, M = map(int, stdin.readline().split())
lst, que, res, resLen, count = [], deque(), -1, 0, 0
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
visited = [[False] * M for _ in range(N)]
que.append((0, 0))

for _ in range(N):
    lst.append(list(map(int, stdin.readline().split())))

def bfs():
    global lst
    tmp, copyLst = set(), copy.deepcopy(lst)
    while que:
        x, y = que.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if lst[nx][ny] == 0:
                        que.append((nx,ny))
                    else:
                        copyLst[nx][ny] = 0
                        tmp.add((nx,ny))
    lst = copyLst
    return tmp

# O(NM)
while que:
    resLen = count
    tmp = bfs()
    res += 1
    que.extend(tmp)
    count = len(tmp)

print(res)
print(resLen)
```

### 다른 풀이 by guno98

- O(NM)으로 같은 개념으로 문제를 풀었지만 스택을 이용하였다.

```python
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
MAP=[]
time=0
visited=[[False]*M for _ in range(N)]
for _ in range(N):
    temp=list(map(int,input().split()))
    MAP.append(temp)

d=[(0,1),(0,-1),(1,0),(-1,0)]
stack,air,hole=[(0,0)],[],[]
visited[0][0]=True
while stack:
    c=stack.pop()
    air.append(c)
    for i in range(4):
        nx=c[0]+d[i][0];ny=c[1]+d[i][1];
        if not(0<=nx<N and 0<=ny<M) or visited[nx][ny]:
            continue
        if MAP[nx][ny]:
            continue
        visited[nx][ny]=True
        stack.append((nx,ny))
cnt=0;


while True:
    next_air=[]

    while air:
        c=air.pop()
        for i in range(4):
            nx=c[0]+d[i][0];ny=c[1]+d[i][1];
            if not(0<=nx<N and 0<=ny<M) or visited[nx][ny]:
                continue
            visited[nx][ny]=True
            if MAP[nx][ny]:
                next_air.append((nx,ny))
            else: # 구멍
                air.append((nx,ny))
    if not next_air:
        break
    cnt=len(next_air)
    air=next_air
    time+=1

print(time)
print(cnt)
```
