# 해킹

### 문제설명

최흉최악의 해커 yum3이 네트워크 시설의 한 컴퓨터를 해킹했다! 이제 서로에 의존하는 컴퓨터들은 점차 하나둘 전염되기 시작한다. 어떤 컴퓨터 a가 다른 컴퓨터 b에 의존한다면, b가 감염되면 그로부터 일정 시간 뒤 a도 감염되고 만다. 이때 b가 a를 의존하지 않는다면, a가 감염되더라도 b는 안전하다.

최흉최악의 해커 yum3이 해킹한 컴퓨터 번호와 각 의존성이 주어질 때, 해킹당한 컴퓨터까지 포함하여 총 몇 대의 컴퓨터가 감염되며 그에 걸리는 시간이 얼마인지 구하는 프로그램을 작성하시오. (BaekJoon 10282)

Rule 1: 각 테스트 케이스에서 같은 의존성 (a, b)가 두 번 이상 존재하지 않는다.

ex)

- Input:

        2
        3 2 2
        2 1 5
        3 2 5
        3 3 1
        2 1 2
        3 1 8
        3 2 4

- Output:

        2 5
        3 6


### 핵심원리 - Sorting

- 정렬로 가장 투표가 적은 순, 다음으로 오래된 순 으로 복합정렬을 통해 후보의 수가 꽉차면 가장 적고 오래된 후보를 지우고 새로 추가한다.

```python
for i in res:
    if num == i[2]:
        i[0] += 1
        check = True
        break
if not check:
    if len(res) >= N:
        res = sorted(res, key=lambda x: (x[0], x[1]))
        del res[0]
        res.append([0, ind, num])
    else:
        res.append([0, ind, num])
```


### 전체 코드

- O(TN) where T, N are a number of test case and adjacent number.

```python
# Dijkstra
import heapq
from sys import stdin

def dijkstra(s):
    hData, distance[s] = [], 0
    heapq.heappush(hData, (0,s))

    while hData:
        dist, now = heapq.heappop(hData)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            time = dist + i[1]
            if distance[i[0]] > time:
                distance[i[0]] = time
                heapq.heappush(hData, (time, i[0]))

for _ in range(int(stdin.readline())):
    N, D, C = map(int, stdin.readline().split())
    adj, distance = [[] for i in range(N+1)], [1e9] * (N+1)
    for _ in range(D):
        x,y,time = map(int, stdin.readline().split())
        adj[y].append((x,time))
    dijkstra(C)
    count, maxD = 0, 0
    for i in distance:
        if i != 1e9:
            count += 1
            if i > maxD:
                maxD = i
    print(count, maxD)
```

### 다른 풀이 by fjdksl546

- O(TN)으로 같지만 다익스트라에서 카운트와 맥스값을 계산하여 실행시간을 줄였다.

```python
import sys, heapq

def dijkstra(num):
    inf = 9876543210
    d = [inf] * (n + 1)
    d[num] = 0
    q = []
    heapq.heappush(q, (0, num))
    while q:
        cur_dist, cur = heapq.heappop(q)
        if d[cur] < cur_dist:
            continue
        for i in adj[cur]:
            next, next_dist = i
            if d[next] > next_dist + cur_dist:
                d[next] = next_dist + cur_dist
                heapq.heappush(q, (next_dist + cur_dist, next))
    cnt = 0
    times = 0
    for i in range(1, n + 1):
        if d[i] != 9876543210:
            cnt += 1
            times = max(times, d[i])
    return cnt, times

tc = int(sys.stdin.readline())
for _ in range(tc):
    n, d, c = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        adj[b].append((a,s))
    print(' '.join(map(str, dijkstra(c))))
```
