# 캐슬 디펜스

### 문제설명

캐슬 디펜스는 성을 향해 몰려오는 적을 잡는 턴 방식의 게임이다. 게임이 진행되는 곳은 크기가 N×M인 격자판으로 나타낼 수 있다. 격자판은 1×1 크기의 칸으로 나누어져 있고, 각 칸에 포함된 적의 수는 최대 하나이다. 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다.

성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다. 궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다. 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다. 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다.

게임 설명에서 보다시피 궁수를 배치한 이후의 게임 진행은 정해져있다. 따라서, 이 게임은 궁수의 위치가 중요하다. 격자판의 상태가 주어졌을 때, 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.

격자판의 두 위치 (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|이다. (BaekJoon 17135)

Rule 1: 첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D가 주어진다.
Rule 2: 둘째 줄부터 N개의 줄에는 격자판의 상태가 주어진다. 0은 빈 칸, 1은 적이 있는 칸이다.

ex)
- Input:

        5 5 1
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        1 1 1 1 1

- Output:

        3


### 핵심원리 - BFS approach

- 브루트포스 구현 후 BFS 접근법으로 사정거리 안을 왼쪽부터 탐색하며 적을 제거했다.

```python
def search(bow):
    cplst = copy.deepcopy(lst)
    saveA = set()
    for i in range(N-1, -1, -1)
        for j in bow:
            visi = [[False] * M for _ in range(N)]
            arr = deque()
            arr.append((i, j))
            while arr:
                x, y = arr.popleft()
                if not visi[x][y]:
                    visi[x][y] = True
                    if cplst[x][y] == 1:
                        saveA.add((x,y))
                        break
                    for d in range(3):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M and not visi[nx][ny]:
                            if (abs(i-nx) + abs(j-ny)) < D:
                                arr.append((nx, ny))
        for b,n in saveA:
            cplst[b][n] = 0
    return len(saveA)
```


### 전체 코드

- O(NM^4) where N, M is a number of rows and columns.

```python
# Brute Force + BFS
from sys import stdin
import copy
from collections import deque

N,M,D = map(int, stdin.readline().split())
lst, maxNum = [], 0
dx, dy = [0, -1, 0], [-1, 0, 1]
for _ in range(N):
    lst.append(list(map(int, stdin.readline().split())))

# O(MN)
def search(bow):
    cplst = copy.deepcopy(lst)
    saveA = set()
    for i in range(N-1, -1, -1)
        for j in bow:
            visi = [[False] * M for _ in range(N)]
            arr = deque()
            arr.append((i, j))
            while arr:
                x, y = arr.popleft()
                if not visi[x][y]:
                    visi[x][y] = True
                    if cplst[x][y] == 1:
                        saveA.add((x,y))
                        break
                    for d in range(3):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M and not visi[nx][ny]:
                            if (abs(i-nx) + abs(j-ny)) < D:
                                arr.append((nx, ny))
        for b,n in saveA:
            cplst[b][n] = 0
    return len(saveA)

# O(NM^4) ?
for i in range(M-2):
    for j in range(i+1,M-1):
        for z in range(j+1, M):
            tmp = [i, j, z]
            maxNum = max(maxNum, search(tmp))
print(maxNum)
```

### 다른 풀이 by hellodongsik

- 같은 개념으로 문제를 풀었지만 기능을 세분화 하였다.

```python
# 궁수자리 3개 뽑는거
def location(idx=-1,num=3,position=[]):
    global M,ans

    if num==0:
        cnt = defence(position)
        ans= max(ans,cnt)
        return

    for i in range(idx+1,M-num+1):
        position.append(i)
        location(i,num-1,position)
        position.pop()

# 궁수 전진
def defence(position):
    global N,M
    # 복제
    enemy_copy = [0] * N
    for i in range(N):
        enemy_copy[i] = enemy[i][:]

    cnt_attack=0
    arc1 ,arc2, arc3 = position
    for i in range(N-1,-1,-1):
        a = shoot(i, arc1 , enemy_copy)
        b = shoot(i, arc2 , enemy_copy)
        c = shoot(i, arc3 , enemy_copy)
        attack = set()
        if a: attack.add((a[0],a[1]))
        if b: attack.add((b[0], b[1]))
        if c: attack.add((c[0], c[1]))
        cnt_attack+=len(attack)
        for j,k in attack:
            enemy_copy[j][k]=0
    return cnt_attack

# 발사
# 같은 거리일 때 가장 왼쪽에 있는 적 공격
# 화살 발사하고 삼각형을 그린다고 생각하면 된다.
def shoot(a, b, enemy_copy):
    global N,M,D
    if enemy_copy[a][b]==1:
        return (a,b)

    arrow=[(a,b,1)]
    st=0
    while arrow:
        r,c,d=arrow[st]
        st+=1
        if d>D:
            return False
        for nr,nc in (r,c-1),(r-1,c),(r,c+1):
            if not(0<=nr<N and 0<=nc<M): continue
            if (nr,nc,d+1) in arrow: continue
            if enemy_copy[nr][nc]==1:
                if d+1>D:
                    continue
                return (nr,nc)
            else:
                arrow.append((nr,nc,d+1))
        if st==len(arrow):      # st가 인덱스 초과한것
            return False
    # return False


N,M,D=map(int,input().split())
enemy=[list(map(int, input().split())) for _ in range(N)]

ans=0
location()
print(ans)
```
