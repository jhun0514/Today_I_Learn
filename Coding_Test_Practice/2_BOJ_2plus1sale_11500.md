# 2+1 세일

### 문제설명

KSG 편의점에서는 과일우유, 드링킹요구르트 등의 유제품을 '2+1 세일'하는 행사를 하고 있습니다. KSG 편의점에서 유제품 3개를 한 번에 산다면 그중에서 가장 싼 것은 무료로 지불하고 나머지 두 개의 제품 가격만 지불하면 됩니다. 한 번에 3개의 유제품을 사지 않는다면 할인 없이 정가를 지불해야 합니다.

예를 들어, 7개의 유제품이 있어서 각 제품의 가격이 10, 9, 4, 2, 6, 4, 3이고 재현이가 (10, 3, 2), (4, 6, 4), (9)로 총 3번에 걸쳐서 물건을 산다면 첫 번째 꾸러미에서는 13원을, 두 번째 꾸러미에서는 10원을, 세 번째 꾸러미에서는 9원을 지불해야 합니다.

재현이는 KSG 편의점에서 친구들과 같이 먹을 총 N팩의 유제품을 구입하려고 합니다. 재현이를 도와 최소비용으로 유제품을 구입할 수 있도록 도와주세요! (BaekJoon 11508)

Rule 1: 첫 번째 줄에는 유제품의 수 N (1 ≤ N ≤ 100,000)이 주어집니다.
Rule 2: 두 번째 줄부터 N개의 줄에는 각 유제품의 가격 Ci (1 ≤ Ci ≤ 100,000)가 주어집니다.

ex)
- Input:
        4
        3
        2
        3
        2
- Output:
        8


### 핵심원리 - Greedy approach

- 그리디 접근 방법으로 높은 가격 부터 3개씩 골라 최적해를 구한다.

```python
# 그리디 접근을 위해 내림차순 정렬
C.sort(reverse=True)

# 3개씩 묶어준다
cLen, ind = len(C), 0
while (cLen-ind >= 3):
    ret, ind = ret + C[ind] + C[ind+1], ind + 3

if (cLen-ind) != 0:
    for i in range(ind, cLen):
        ret += C[i]
```


### 전체 코드

- O(NlogN) where N is a number of dairy product. sort의 시간복잡도가 NlogN으로 코드 내에서 가장 크다.

```python
from sys import stdin

# 그리디 접근으로 비싼 가격 순으로 3개씩 꽉채워 사야 최적해가 나온다
N = int(stdin.readline())
C, ret = [], 0
for _ in range(N):
    C.append(int(stdin.readline()))

# 그리디 접근을 위해 내림차순 정렬
C.sort(reverse=True)

# 3개씩 묶어준다
cLen, ind = len(C), 0
while (cLen-ind >= 3):
    ret, ind = ret + C[ind] + C[ind+1], ind + 3

if (cLen-ind) != 0:
    for i in range(ind, cLen):
        ret += C[i]

print(ret)
```


### 다른 풀이 by me

- O(NlogN) 으로 같지만 정렬을 기본 오름차순으로 한 뒤 뒤에서 내려온 방법이 더 빨랐다.

```python
from sys import stdin

# 그리디 접근으로 비싼 가격 순으로 3개씩 꽉채워 사야 최적해가 나온다
N = int(stdin.readline())
C, ret = [], 0
for _ in range(N):
    C.append(int(stdin.readline()))

# 그리디 접근을 위해 내림차순 정렬
C.sort()

# 3개씩 묶어준다
ind = len(C)-1
while (ind >= 1):
    ret, ind = ret + C[ind] + C[ind-1], ind - 3

if ind == 0:
    ret += C[ind]
elif ind == 1:
    ret += C[ind] + C[ind - 1]


print(ret)
```


### 다른 풀이

- O(NlogN) 으로 역시 같지만 2+1에서 할인 받는 1개의 가격만 전체 합에서 빼는 것으로 단계와 시간을 줄였다.

```python
from sys import stdin
input = stdin.readline
c = ([int(input()) for i in range(int(input()))])
c.sort(reverse = True)
res = sum(c)
for i in range(2,len(c),3):
    res-= c[i]
print(res)
```
