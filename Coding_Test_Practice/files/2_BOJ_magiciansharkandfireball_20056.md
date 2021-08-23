# 마법사 상어와 파이어볼

### 문제설명

마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다. 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다. i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.

격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.

파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 다음과 같다.

마법사 상어가 모든 파이어볼에게 이동을 명령하면 다음이 일들이 일어난다.

- 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
- 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    - 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    - 파이어볼은 4개의 파이어볼로 나누어진다.
    - 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        - 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
        - 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
        - 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
    - 질량이 0인 파이어볼은 소멸되어 없어진다.

마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자. (BaekJoon 2502)

Rule 1: 첫째 줄에 N, M, K가 주어진다. 둘째 줄부터 M개의 줄에 파이어볼의 정보가 한 줄에 하나씩 주어진다. 파이어볼의 정보는 다섯 정수 ri, ci, mi, si, di로 이루어져 있다.
Rule 2: 서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.

ex)

- Input:

        4 2 1
        1 1 5 2 2
        1 4 7 1 6

- Output:

        8


### 핵심원리 - 이동 수식

- 이동 좌표를 수식으로 표현해야 시간복잡도에 맞출 수 있다.

```python
for elem in lst[x][y]:
    nm, ns, nd = elem
    nx, ny = x+direc[nd][0]*(ns%N), y+direc[nd][1]*(ns%N)
    if nx < 0:
        nx = N + nx
    if ny < 0:
        ny = N + ny
    if nx >= N:
        nx = nx- N
    if ny >=N:
        ny = ny- N
    if tmp[nx][ny]:
        if (nx, ny) not in save:
            save.append((nx,ny))
    tmp[nx][ny].append((nm, ns, nd))
```


### 전체 코드

- O(KMN^2) where K, N, M are numbers of tries, size of matrix, fireballs.

```python
# Simulation
from sys import stdin
N, M, K = map(int, stdin.readline().split())
lst, direc, answer = [[[] for _ in range(N)] for __ in range(N)], [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)], 0

# 주어진 파이어볼의 정보를 저장한다
for _ in range(M):
    r, c, m, s, d = map(int, stdin.readline().split())
    lst[r-1][c-1].append((m, s, d))

for i in range(K):
    tmp, save = [[[] for _ in range(N)] for __ in range(N)], []
    for x in range(N):
        for y in range(N):
            for elem in lst[x][y]:
                nm, ns, nd = elem
                # 파이어볼 이동좌표
                nx, ny = x+direc[nd][0]*(ns%N), y+direc[nd][1]*(ns%N)
                if nx < 0:
                    nx = N + nx
                if ny < 0:
                    ny = N + ny
                if nx >= N:
                    nx = nx- N
                if ny >= N:
                    ny = ny- N
                # 2개 이상 파이어볼 좌표 저장
                if tmp[nx][ny]:
                    if (nx, ny) not in save:
                        save.append((nx,ny))
                tmp[nx][ny].append((nm, ns, nd))

    for ind in save:
        x, y = ind
        nm, ns, nd, check, count = 0, 0, [0,2,4,6], [], 0
        for fire in tmp[x][y]:
            m, s, d = fire
            nm += m
            ns += s
            count += 1
            check.append(d)
        nm, ns, find = int(nm/5), int(ns/count), check[0]%2
        # 질량이 0이면 초기화
        if nm == 0:
            tmp[x][y] = []
            continue
        # 저장한 방향들의 홀수 짝수 통일 여부 확인
        for j in range(1,len(check)):
            if check[j]%2 != find:
                nd = [1,3,5,7]
                break
        tmp[x][y] = [(nm, ns, nd[0]), (nm, ns, nd[1]), (nm, ns, nd[2]), (nm, ns, nd[3])]
    lst = tmp

# 질량 total 계산
for x in range(N):
    for y in range(N):
        for elem in lst[x][y]:
            answer += elem[0]
print(answer)
```

### 다른 풀이 by grasshoppertrainer

- O(KM)으로 처음 파이어볼의 좌표만 탐색하여 시간복잡도를 줄였다.

```python
from sys import stdin
from math import floor


def solution(N, M, K, balls):
    DELTA = (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
    balls = list(map(lambda x: (x[0] - 1, x[1] - 1, *x[2:]), balls))
    for _ in range(K):

        poses = {}
        for x, y, m, s, d in balls:
            dx, dy = DELTA[d]
            nx, ny = (x + s * dx) % N, (y + s * dy) % N
            poses.setdefault((nx, ny), []).append((m, s, d))

        new_balls = []
        for (x, y), vals in poses.items():
            if len(vals) == 1:
                new_balls.append((x, y, *vals[0]))
                continue

            nm, ns, nd = 0, 0, []
            for m, s, d in vals:
                nm += m
                ns += s
                nd.append(d % 2)
            nm = floor(nm / 5)
            ns = floor(ns / len(vals))
            nd = (0, 2, 4, 6) if all(d == nd[0] for d in nd) else (1, 3, 5, 7)
            if nm != 0:
                for d in nd:
                    new_balls.append((x, y, nm, ns, d))

        balls = new_balls

    return sum(map(lambda x: x[2], balls))


lexer = lambda: list(map(int, stdin.readline().strip().split(' ')))
N, M, K = lexer()
balls = [lexer() for _ in range(M)]

print(solution(N, M, K, balls))
```
