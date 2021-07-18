# 외계인의 기타 연주

### 문제설명

상근이의 상상의 친구 외계인은 손가락을 수십억개 가지고 있다. 어느 날 외계인은 기타가 치고 싶었고, 인터넷에서 간단한 멜로디를 검색했다. 이제 이 기타를 치려고 한다.

보통 기타는 1번 줄부터 6번 줄까지 총 6개의 줄이 있고, 각 줄은 P개의 프렛으로 나누어져 있다. 프렛의 번호도 1번부터 P번까지 나누어져 있다.

멜로디는 음의 연속이고, 각 음은 줄에서 해당하는 프렛을 누르고 줄을 튕기면 연주할 수 있다. 예를 들면, 4번 줄의 8번 프렛을 누르고 튕길 수 있다. 만약, 어떤 줄의 프렛을 여러 개 누르고 있다면, 가장 높은 프렛의 음이 발생한다.

예를 들어, 3번 줄의 5번 프렛을 이미 누르고 있다고 하자. 이때, 7번 프렛을 누른 음을 연주하려면, 5번 프렛을 누르는 손을 떼지 않고 다른 손가락으로 7번 프렛을 누르고 줄을 튕기면 된다. 여기서 2번 프렛의 음을 연주하려고 한다면, 5번과 7번을 누르던 손가락을 뗀 다음에 2번 프렛을 누르고 연주해야 한다.

이렇게 손가락으로 프렛을 한 번 누르거나 떼는 것을 손가락을 한 번 움직였다고 한다. 어떤 멜로디가 주어졌을 때, 손가락의 가장 적게 움직이는 회수를 구하는 프로그램을 작성하시오. (BaekJoon 2841)

Rule 1: 첫째 줄에 멜로디에 포함되어 있는 음의 수 N과 한 줄에 있는 프렛의 수 P가 주어진다. (N ≤ 500,000, 2 ≤ P ≤ 300,000)
Rule 2: 다음 N개 줄에는 멜로디의 한 음을 나타내는 두 정수가 주어진다. 첫 번째 정수는 줄의 번호이고 두 번째 정수는 그 줄에서 눌러야 하는 프렛의 번호이다. 입력으로 주어진 음의 순서대로 기타를 연주해야 한다.

ex)
- Input:
        5 15
        2 8
        2 10
        2 12
        2 10
        2 5
- Output:
        7


### 핵심원리 - Stack

- 스택을 이용하여 단순 데이터 저장 방법으로 문제를 접근한다.

```python
for i in range(N):
    sNum, pNum = map(int, input().split())
    if sNum not in pStack:
        pStack[sNum] = [pNum]
        ret += 1
    else:
        # 맨위인 경우
        if pNum == pStack[sNum][-1]:
            continue
        # 누르기만 하면 되는 경우
        if pNum > pStack[sNum][-1]:
            pStack[sNum].append(pNum)
            ret += 1
        # 누르고 있는걸 때야하는 경우
        if pNum < pStack[sNum][-1]:
            # 때기만 하는 경우
            if pNum in pStack[sNum]:
                tmp = pStack[sNum].index(pNum) + 1
                ret = ret + len(pStack[sNum]) - tmp
                pStack[sNum] = pStack[sNum][:tmp]
            # 때고 누르는 경우
            else:
                while(len(pStack[sNum]) != 0 and pNum < pStack[sNum][-1]):
                    pStack[sNum].pop()
                    ret += 1
                pStack[sNum].append(pNum)
                ret += 1
```


### 전체 코드

- O(N+B) where N is a number of melody and B is a while statement (최적화 실패로 pypy3로만 통과되었다.)

```python
N, P = map(int, input().split())

pStack = {}
ret = 0

for i in range(N):
    sNum, pNum = map(int, input().split())
    if sNum not in pStack:
        pStack[sNum] = [pNum]
        ret += 1
    else:
        # 맨위인 경우
        if pNum == pStack[sNum][-1]:
            continue
        # 누르기만 하면 되는 경우
        if pNum > pStack[sNum][-1]:
            pStack[sNum].append(pNum)
            ret += 1
        # 누르고 있는걸 때야하는 경우
        if pNum < pStack[sNum][-1]:
            # 때기만 하는 경우
            if pNum in pStack[sNum]:
                tmp = pStack[sNum].index(pNum) + 1
                ret = ret + len(pStack[sNum]) - tmp
                pStack[sNum] = pStack[sNum][:tmp]
            # 때고 누르는 경우
            else:
                while(len(pStack[sNum]) != 0 and pNum < pStack[sNum][-1]):
                    pStack[sNum].pop()
                    ret += 1
                pStack[sNum].append(pNum)
                ret += 1

print(ret)
```


### 다른 풀이 by me

- O(N+B) where N is a number of melody and B is a while statement

- 최적화를 위해 dictionary에 key를 미리 지정했다. 또한 작동 경우의 수를 3가지로 줄여 시간을 줄였다.

```python
#시간을 줄이기 위해 stdin 사용
from sys import stdin

N, P = map(int, stdin.readline().split())

#시간을 줄이기 위해 미리 dic key 지정
pStack, ret = {
    "1" : [], "2" : [], "3" : [], "4" : [], "5" : [], "6" : []
}, 0

for _ in range(N):
    sNum, pNum = stdin.readline().split()
    pNum = int(pNum)

    #1. 더 높은 프렛을 제거
    while(pStack[sNum] and pNum < pStack[sNum][-1]):
        pStack[sNum].pop()
        ret += 1

    #2-1. 이미 들어있는 경우
    if pStack[sNum] and pStack[sNum][-1] == pNum:
        continue

    #2-2. 새로 추가하는 경우
    pStack[sNum].append(pNum)
    ret += 1

print(ret)
```
