# 센서

### 문제설명

한국도로공사는 고속도로의 유비쿼터스화를 위해 고속도로 위에 N개의 센서를 설치하였다. 문제는 이 센서들이 수집한 자료들을 모으고 분석할 몇 개의 집중국을 세우는 일인데, 예산상의 문제로, 고속도로 위에 최대 K개의 집중국을 세울 수 있다고 한다.

각 집중국은 센서의 수신 가능 영역을 조절할 수 있다. 집중국의 수신 가능 영역은 고속도로 상에서 연결된 구간으로 나타나게 된다. N개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 하며, 집중국의 유지비 문제로 인해 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야 한다.

편의를 위해 고속도로는 평면상의 직선이라고 가정하고, 센서들은 이 직선 위의 한 기점인 원점으로부터의 정수 거리의 위치에 놓여 있다고 하자. 따라서, 각 센서의 좌표는 정수 하나로 표현된다. 이 상황에서 각 집중국의 수신 가능영역의 거리의 합의 최솟값을 구하는 프로그램을 작성하시오. 단, 집중국의 수신 가능영역의 길이는 0 이상이며 모든 센서의 좌표가 다를 필요는 없다. (BaekJoon 2212)

Rule 1: 첫째 줄에 센서의 개수 N(1 ≤ N ≤ 10,000), 둘째 줄에 집중국의 개수 K(1 ≤ K ≤ 1000)가 주어진다.
Rule 2: 셋째 줄에는 N개의 센서의 좌표가 한 개의 정수로 N개 주어진다. 각 좌표 사이에는 빈 칸이 하나 있으며, 좌표의 절댓값은 1,000,000 이하이다.

ex)

- Input:

        6
        2
        1 6 9 3 6 7

- Output:

        5


### 핵심원리 - Greedy approach

- 그리디 접근법으로 가장 거리가 떨어진 센서사이를 끊어서 그룹을 나누었다.

```python
lst.sort()
# 센서 사이 거리를 구해서 정렬한다.
for i in range(N-1):
    tmp = lst[i+1] - lst[i]
    res.append(tmp)
res.sort()
print(sum(res[:N-K])) # K개 그룹으로 만들기 위해 거리 순으로 자른다
```


### 전체 코드

- O(NlogN) where N is a number of sensors.

```python
## Greedy
from sys import stdin

N, K = int(stdin.readline()), int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
res = []

if N <= K:
    print(0)
else:
    # 거리 순으로 그룹을 지정하는게 효율적이기에 정렬을 우선한다 / O(NlogN)
    lst.sort()
    # 센서 사이 거리를 구해서 정렬한다.
    for i in range(N-1):
        tmp = lst[i+1] - lst[i]
        res.append(tmp)
    res.sort()
    print(sum(res[:N-K])) # K개 그룹으로 만들기 위해 거리 순으로 자른다
```

### 다른 풀이 by asdhugh1

- O(NlogN)으로 같은 개념으로 문제를 풀었지만 pop으로 먼 거리들을 잘라준 후 더하여 시간을 줄였다.

```python
import sys
n = int(input())
m = int(input())
l1 = list(map(int, input().split()))
l1.sort()
#l1 = [1, 3, 6, 6, 7, 9, 12 ,14]
if n==1 and m==1:
    print(1)

elif (n ==1):
    print(0)

elif m ==1 :
    print(l1[-1]-l1[0])
# if n <=m :
#     print(0)
#     sys.exit(0)

else :
    diff_list = [l1[i+1] - l1[i] for i in range(len(l1)-1)]

    diff_list.sort()

    for _ in range(m-1):

        diff_list.pop()
    print(sum(diff_list))
```
