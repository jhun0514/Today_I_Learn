# 알고스팟

### 문제설명

알고스팟 운영진이 모두 미로에 갇혔다. 미로는 NxM 크기이며, 총 1x1크기의 방으로 이루어져 있다. 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.

만약 이 문제가 알고스팟에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를 사용할 수 없다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오. (BaekJoon 1261)

Rule 1: 첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다. 0은 빈 방을 의미하고, 1은 벽을 의미한다.
Rule 2: (1, 1)과 (N, M)은 항상 뚫려있다.

ex)
- Input:
        3 3
        011
        111
        110
- Output:
        3


### 핵심원리 - Dijkstra

- 다익스트라 탐색 접근 방법으로 각 방까지 걸리는 최단 경로를 구한다.

```python
def dijkstra(row, col):
    heapData = []
    heapq.heappush(heapData,(0,row,col))
    distance[col][row] = 0
    while heapData:
        dist, rowNow, colNow = heapq.heappop(heapData)
        if distance[colNow][rowNow] < dist:
            continue
        for i in range(4):
            colNext, rowNext = colNow + dx[i], rowNow + dy[i]
            if (N > colNext >= 0) and (M > rowNext >= 0):
                cost = dist + int(A[colNext][rowNext])
                if distance[colNext][rowNext] > cost:
                    distance[colNext][rowNext] = cost
                    heapq.heappush(heapData, (cost, rowNext, colNext))
```


### 전체 코드

- O(NlogN) where N is a number of rooms

```python
# 최소횟수를 구하는 문제기에 최단거리 다익스트라를 이용했습니다.
import heapq
from sys import stdin

def dijkstra(row, col):
    heapData = []
    heapq.heappush(heapData,(0,row,col))
    distance[col][row] = 0
    while heapData:
        dist, rowNow, colNow = heapq.heappop(heapData)
        if distance[colNow][rowNow] < dist:
            continue
        for i in range(4):
            colNext, rowNext = colNow + dx[i], rowNow + dy[i]
            if (N > colNext >= 0) and (M > rowNext >= 0):
                cost = dist + int(A[colNext][rowNext])
                if distance[colNext][rowNext] > cost:
                    distance[colNext][rowNext] = cost
                    heapq.heappush(heapData, (cost, rowNext, colNext))



M, N = map(int, stdin.readline().split())
A = [list(stdin.readline().rstrip()) for _ in range(N)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
distance = [[1e9 for _ in range(M)] for i in range(N)]

dijkstra(0,0)
print(distance[N-1][M-1])
```


### 다른 풀이

- O(NlogN) 으로 똑같지만 deque로 힙큐 기능의 부분을 구성했다. 필요부분의 기능만 구성함으로써 실행시간이 더 빠르다.

```python
from sys import stdin

m, n = map(int, input().split())
status = stdin.read().split()

def dijkstra():
    COST = [[1e4]*m for _ in range(n)]
    COST[0][0] = 0
    deque = [(0, 0)]

    while True:
        x, y = deque.pop(0)
        if x == m-1 and y == n-1:
            return COST[n-1][m-1]

        cost = COST[y][x]
        for x, y in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
            if not (0 <= x < m and 0 <= y < n):
                continue

            is_wall = status[y][x] == '1'
            new_cost = cost + (1 if is_wall else 0)

            if COST[y][x] <= new_cost:
                continue

            COST[y][x] = new_cost
            if is_wall:
                deque.append((x, y))
            else:
                deque.insert(0, (x, y))
print(dijkstra())
```
