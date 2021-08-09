# 신기한 키보드

### 문제설명

동혁이의 키보드에는 버튼 세 개와 LCD창 한 개가 달려 있다. LCD창에는 문자열 S가 쓰여 있다. 그리고 커서는 문자열의 가장 왼쪽 글자에 위치해 있다. 버튼 세 개는 왼쪽, 오른쪽, 엔터키이다.

왼쪽 키는 만약 현재 커서에서 왼쪽으로 더 갈 수 있으면, 왼쪽으로 커서를 한 칸 이동시키는 역할을 하고, 오른쪽 키도 현재 커서에서 오른쪽으로 갈 수 있으면 오른쪽으로 커서를 한 칸 이동시키는 역할을 한다. LCD창의 크기는 정확하게 문자열 S의 크기와 같다. 그리고 커서는 절대로 LCD창을 벗어나지 않는다. 엔터키는 문자열을 컴퓨터에 전송해서 컴퓨터 화면에 출력하는 역할을 한다. 문자열이 화면에 출력되면, 그 문자는 빈 칸으로 변한다.

동혁이는 LCD창에 쓰여 있는 문자열을 컴퓨터 화면에 알파벳 순서대로 쓰려고 한다. 동혁이는 완벽주의자이기 때문에, 문자열 S에 있는 모든 문자를 하나도 빠짐없이 출력하려고 한다. 만약 a가 LCD창에 3개가 있으면 컴퓨터 화면에는 a가 3번 나와야 한다.

LCD창에 쓰여 있는 문자열이 주어질 때, 그 문자열을 알파벳 순서대로 출력할 때, 키의 입력을 최소화하는 프로그램을 작성하시오. (BaekJoon 1796)

Rule 1: 첫째 줄에 LCD창에 쓰여 있는 문자열 S가 주어진다. 문자열 S는 길이가 1,000보다 작다. 문자열 S는 알파벳 소문자로만 이루어져 있다.

ex)

- Input:

        abba

- Output:

        9


### 핵심원리 - Dynamic Programming

- 동적 프로그래밍으로 점화식을 찾아 계산하였다.
- Base case
    - DP[i][x] = 0에서 출발해서 x로 도착하는 과정에서 i 알파벳을 찾는 거리

- 나머지 알파벳
    - DP[i][j] = (DP[이전에 마지막으로 찾은 알파벳][z] + z에서 출발해서 j로 도착하는 과정에서 i 알파벳을 찾는 거리) 중에서 min 값
        - z = 이전에 마지막 도착 지점, 이번에 출발지점
        - j = 이번에 도착지점

```python
# DP calculate
for i in range(26):
    if index[i][0] != -1:
        if find: # DP base
            for x in range(len(N)):
                dp[i][x] = dist(0, x, index[i][0], index[i][1])
            find, count = False, i
            continue
        for j in range(len(N)):
            minTemp = []
            for z in range(len(N)):
                distances = min(dist(z,j,index[i][0],index[i][1]), dist(z,j,index[i][1],index[i][0]))
                minTemp.append(dp[count][z] + distances)
            if len(minTemp) > 0:
                dp[i][j] = min(minTemp)
        count = i
```


### 전체 코드

- O(N^2) where N is a length of the string.

```python
# Dynamic Programming
from sys import stdin

N = stdin.readline().rstrip()
dp, index, count, find = [[0 for _ in range(len(N))] for _ in range(26)], [[-1,-1] for _ in range(26)], -1, True

if not N:
    print(0)
    exit(0)

for i in range(26):
    tmp = chr(i + 97)
    index[i][0], index[i][1] = N.find(tmp), N.rfind(tmp)

def dist(a,b,c,d):
    distance = abs(a-c) + abs(c-d) + abs(b-d)
    return distance

# DP calculate
for i in range(26):
    if index[i][0] != -1:
        if find: # DP base
            for x in range(len(N)):
                dp[i][x] = dist(0, x, index[i][0], index[i][1])
            find, count = False, i
            continue
        for j in range(len(N)):
            minTemp = []
            for z in range(len(N)):
                distances = min(dist(z,j,index[i][0],index[i][1]), dist(z,j,index[i][1],index[i][0]))
                minTemp.append(dp[count][z] + distances)
            if len(minTemp) > 0:
                dp[i][j] = min(minTemp)
        count = i
print(min(dp[count]) + len(N))
```

### 다른 풀이 by ssw3095

- O(N^2)으로 전체적인 흐름은 비슷하지만 재귀를 이용하여 시간을 단축하였다.

```python
import sys

def cost(now_i, next_i, m):
    return abs(now_i-m) + abs(m-next_i)

def dp(alpha, now_i):
    if alpha == 26:
        return 0
    if not list_memo[alpha][now_i] == -1:
        return list_memo[alpha][now_i]
    if list_lr[alpha][0] == list_lr[alpha][0] == -1:
        list_memo[alpha][now_i] = dp(alpha+1, now_i)
    else:
        l, r = list_lr[alpha]

        list_memo[alpha][now_i] = min(dp(alpha+1, l) + cost(now_i, l, r), dp(alpha+1, r) + cost(now_i, r, l))
    return list_memo[alpha][now_i]


dict_alpha = {chr(97+i):i for i in range(26)}
s = sys.stdin.readline().strip()
list_memo = [[-1]*(len(s)) for _ in range(26)]
list_lr = [[-1, -1] for _ in range(26)]
for i in range(len(s)):
    if list_lr[dict_alpha[s[i]]][0] == -1:
        list_lr[dict_alpha[s[i]]][0] = i
    list_lr[dict_alpha[s[i]]][1] = i

print(dp(0, 0)+len(s))
```
