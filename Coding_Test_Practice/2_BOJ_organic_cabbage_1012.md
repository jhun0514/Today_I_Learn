# 유기농 배추

### 문제설명

차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. (BaekJoon 1012)

Rule: 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

ex)
- Input: 1
        5 3 6
        0 2
        1 2
        2 2
        3 2
        4 2
        4 0
- Output:
        2


### DFS with recursion

- leetcode 의 number of island와 같은 맥락의 문제로 dfs recursion 을 이용하면 간단하게 풀 수 있다.
인접 지역을 조사하며 퍼져 나가면 된다.

```python
def dfs(grid, a, b):
    if (a < 0 or b < 0 or a >= len(grid) or b >= len(grid[0]) or grid[a][b] != 1):
        return
    grid[a][b] = '#'
    dfs(grid, a+1, b)
    dfs(grid, a-1, b)
    dfs(grid, a, b+1)
    dfs(grid, a, b-1)
```


### 전체 코드

- O(TMN)

```python
import sys
sys.setrecursionlimit(10**6)

def dfs(grid, a, b):
    if (a < 0 or b < 0 or a >= len(grid) or b >= len(grid[0]) or grid[a][b] != 1):
        return
    grid[a][b] = '#'
    dfs(grid, a+1, b)
    dfs(grid, a-1, b)
    dfs(grid, a, b+1)
    dfs(grid, a, b-1)

testCase = int(sys.stdin.readline())
# O(TMN) 최악의 경우 모든 지점을 탐색해야 한다.
for t in range(testCase):
    m,n,k = map(int, sys.stdin.readline().split())
    grid, count = [[0]*m for _ in range(n)], 0
    for k2 in range(k):
        x,y = map(int, sys.stdin.readline().split())
        grid[y][x] = 1

    for b in range(m):
        for a in range(n):
            if grid[a][b] == 1:
                dfs(grid,a,b)
                count += 1

    print(count)
```


### 다른 풀이

기본적인 흐름은 동일하지만 디테일한 recursion을 통해 실행시간을 단축 시켰다.

```python
import sys;p=sys.stdin.readline;
sys.setrecursionlimit(1000000)
q=int(p())
def T(t, o, s):
    t[s][o]=0
    if o+1 < x and t[s][o+1]==1:
        T(t,o+1,s)
    if o-1>= 0 and t[s][o-1]==1:
        T(t, o-1,s)
    if s -1 >= 0 and t[s-1][o]==1:
        T(t, o,s-1)
    if s +1 < y and t[s+1][o]==1:
        T(t,o,s+1)

for _ in range(q):
    x, y, c = map(int, p().split())
    t = [[0] * x for _ in range(y)]
    for i in range(0,c):
        m,n=map(int,p().split());t[n][m] = 1
    v = 0
    for i in range(0,x):
        for j in range(0, y):
            if t[j][i] == 1:
                T(t, i, j);v+=1
    print(v)
```
