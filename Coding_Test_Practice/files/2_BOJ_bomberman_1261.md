# 봄버맨

### 문제설명

봄버맨은 크기가 R×C인 직사각형 격자판 위에서 살고 있다. 격자의 각 칸은 비어있거나 폭탄이 들어있다.

폭탄이 있는 칸은 3초가 지난 후에 폭발하고, 폭탄이 폭발한 이후에는 폭탄이 있던 칸이 파괴되어 빈 칸이 되며, 인접한 네 칸도 함께 파괴된다. 즉, 폭탄이 있던 칸이 (i, j)인 경우에 (i+1, j), (i-1, j), (i, j+1), (i, j-1)도 함께 파괴된다. 만약, 폭탄이 폭발했을 때, 인접한 칸에 폭탄이 있는 경우에는 인접한 폭탄은 폭발 없이 파괴된다. 따라서, 연쇄 반응은 없다.

봄버맨은 폭탄에 면역력을 가지고 있어서, 격자판의 모든 칸을 자유롭게 이동할 수 있다. 봄버맨은 다음과 같이 행동한다.

가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
다음 1초 동안 봄버맨은 아무것도 하지 않는다.
다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
3과 4를 반복한다.
폭탄을 설치해놓은 초기 상태가 주어졌을 때, N초가 흐른 후의 격자판 상태를 구하려고 한다. (BaekJoon 1261)

Rule 1: 첫째 줄에 R, C, N (1 ≤ R, C, N ≤ 200)이 주어진다. 둘째 줄부터 R개의 줄에 격자판의 초기 상태가 주어진다. 빈 칸은 '.'로, 폭탄은 'O'로 주어진다.

ex)

- Input:

        6 7 3
        .......
        ...O...
        ....O..
        .......
        OO.....
        OO.....

- Output:

        OOO.OOO
        OO...OO
        OOO...O
        ..OO.OO
        ...OOOO
        ...OOOO


### 핵심원리 - Brute Force

- 2초의 시간제한과 200 이하의 반복횟수로 완전 탐색 접근 방법을 이용하였다. 1초 이하, 짝수초에는 계산할 필요가 없고 그 외 나머지만 설치 및 제거를 해준다. 설치시 해당 초를 기록하여 언제 제거해야 하는지 안다.

```python
# 빈자리에 초를 기록한다
def installBomb(time):
    for i in range(R):
        for j in range(C):
            if A[i][j] == '.':
                A[i][j] = time

# N초 에는 N-3초에 심어진 폭탄이 터진다
def removeBomb(time):
    copyA = copy.deepcopy(A)
    if time == 3:
        for i in range(R):
            for j in range(C):
                if copyA[i][j] == 'O':
                    A[i][j] = '.'
                    for z in range(4):
                        rowNext, colNext = i+dx[z], j+dy[z]
                        if (R > rowNext >= 0) and (C > colNext >= 0):
                            A[rowNext][colNext] = '.'
    else:
        for i in range(R):
            for j in range(C):
                if copyA[i][j] == time-3:
                    A[i][j] = '.'
                    for z in range(4):
                        rowNext, colNext = i+dx[z], j+dy[z]
                        if (R > rowNext >= 0) and (C > colNext >= 0):
                            A[rowNext][colNext] = '.'

# 1초 이하는 초기상태와 같다
if N <= 1:
    for i in range(R):
        print(''.join(A[i]))

# 짝수 초의 경우 폭탄으로 가득하기에 계산할 필요가 없다
elif N % 2 == 0:
    temp = [['O' * C] for _ in range(R)]
    for i in range(R):
        print(''.join(temp[i]))
```


### 전체 코드

- O(R*C) where R is a number of row and C is a column

```python
# 시간이 넉넉하기에 단순구현을 합니다.
from sys import stdin
import copy

R,C,N = map(int, stdin.readline().split())
A = [list(stdin.readline().rstrip()) for _ in range(R)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

# 빈자리에 초를 기록한다
def installBomb(time):
    for i in range(R):
        for j in range(C):
            if A[i][j] == '.':
                A[i][j] = time

# N초 에는 N-3초에 심어진 폭탄이 터진다
def removeBomb(time):
    copyA = copy.deepcopy(A)
    if time == 3:
        for i in range(R):
            for j in range(C):
                if copyA[i][j] == 'O':
                    A[i][j] = '.'
                    for z in range(4):
                        rowNext, colNext = i+dx[z], j+dy[z]
                        if (R > rowNext >= 0) and (C > colNext >= 0):
                            A[rowNext][colNext] = '.'
    else:
        for i in range(R):
            for j in range(C):
                if copyA[i][j] == time-3:
                    A[i][j] = '.'
                    for z in range(4):
                        rowNext, colNext = i+dx[z], j+dy[z]
                        if (R > rowNext >= 0) and (C > colNext >= 0):
                            A[rowNext][colNext] = '.'

# 1초 이하는 초기상태와 같다
if N <= 1:
    for i in range(R):
        print(''.join(A[i]))

# 짝수 초의 경우 폭탄으로 가득하기에 계산할 필요가 없다
elif N % 2 == 0:
    temp = [['O' * C] for _ in range(R)]
    for i in range(R):
        print(''.join(temp[i]))

# 홀수 초의 경우
else:
    for i in range(2, N+1):
        if i%2 == 0:
            installBomb(i)
        else:
            removeBomb(i)

    for i in range(R):
        for j in range(C):
            if A[i][j] != '.':
                A[i][j] = 'O'

    for i in range(R):
        print(''.join(A[i]))
```


### 다른 풀이

- O(R*C) where R is a number of row and C is a column

- 나는 규칙을 찾지 못하고 코드를 작성했지만 1초 이하, 짝수 초 이외에 나머지 중 두가지 경우의 수가 반복해서 나온다고 한다.
따라서 제거해야하는 시간대를 기록할 필요가 없기에 더 간결하고 빠른 코드를 작성할 수 있다.

```python
R, C, N = map(int, input().split())

if N == 1:
    for _ in range(R):
        print(input())
elif N % 2 == 0:
    for _ in range(R):
        print("O" * C)
else:
    repeat = 2 if N % 4 == 1 else 1
    B = [input() for _ in range(R)]

    for _ in range(repeat):
        result = [["O" for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if B[i][j] != "O":
                    continue
                for ni, nj in (i, j), (i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1):
                    if 0 <= ni < R and 0 <= nj < C:
                        result[ni][nj] = "."
        B = [row[:] for row in result]

    for row in result:
        print("".join(row))
```
