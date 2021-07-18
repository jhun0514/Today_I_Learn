# 도서관

### 문제설명

세준이는 도서관에서 일한다. 도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다. 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다. 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다. (BaekJoon 1461)

Rule 1: 첫째 줄에 책의 개수 N과, 세준이가 한 번에 들 수 있는 책의 개수 M이 주어진다.
Rule 2: 둘째 줄에는 책의 위치가 주어진다. N은 10,000보다 작거나 같은 자연수이고, M은 10,000보다 작거나 같다. 책의 위치는 0이 아니며, 그 절댓값이 10,000보다 작거나 같다.

ex)
- Input:

        7 2
        -37 2 -6 -39 -29 11 -28

- Output:

        131


### 핵심원리 - Greedy approach

- 그리디 접근법으로 거리 순으로 정렬 후 거리가 먼 순서대로 그룹을 지정했다.

```python
# heapq에서 M개 만큼 가지고 이동하는 경우의 거리를 더한다. / O(NlogN)
while pos:
    res += heapq.heappop(pos)
    for i in range(M-1):
        if pos:
            heapq.heappop(pos)
while neg:
    res += heapq.heappop(neg)
    for i in range(M-1):
        if neg:
            heapq.heappop(neg)
```


### 전체 코드

- O(NlogN) where N is a number of books.

```python
# Greedy
from sys import stdin
import heapq

N, M = map(int, stdin.readline().split())
lst, largest = list(map(int, stdin.readline().split())), 0
pos, neg, res = [], [], 0

# save largest and sort pos, neg by heapq / O(NlogN)
for i in lst:
    if abs(i) > largest:
        largest = abs(i)
    if i > 0:
        heapq.heappush(pos, -i)
    else:
        heapq.heappush(neg, i)

# heapq에서 M개 만큼 가지고 이동하는 경우의 거리를 더한다. / O(NlogN)
while pos:
    res += heapq.heappop(pos)
    for i in range(M-1):
        if pos:
            heapq.heappop(pos)
while neg:
    res += heapq.heappop(neg)
    for i in range(M-1):
        if neg:
            heapq.heappop(neg)

print((-res)*2 - largest)
```

### 다른 풀이 by goodlucky00

- O(NlogN)으로 같은 개념으로 문제를 풀었지만 heapq 대신 list 자체를 정렬했다.

```python
N,M=map(int,input().split())
a=list(map(int,input().split()))
mi=[]
pl=[]
result=0
for i in a:
    if i<0:
        mi.append(-i)
    else:
        pl.append(i)

mi.sort(reverse=True)
pl.sort(reverse=True)

if len(mi) ==0:
    mi.append(0)
if len(pl) ==0:
    pl.append(0)

i=0
while(i<len(mi)):
    result += mi[i]*2
    i += M

i=0
while(i<len(pl)):
    result += pl[i]*2
    i += M

result -=max(mi[0],pl[0])
print(result)
```
