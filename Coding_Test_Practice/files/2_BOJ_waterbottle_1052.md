# 물병

### 문제설명

지민이는 N개의 물병을 가지고 있다. 각 물병에는 물을 무한대로 부을 수 있다. 처음에 모든 물병에는 물이 1리터씩 들어있다. 지민이는 이 물병을 또 다른 장소로 옮기려고 한다. 지민이는 한 번에 K개의 물병을 옮길 수 있다. 하지만, 지민이는 물을 낭비하기는 싫고, 이동을 한 번보다 많이 하기는 싫다. 따라서, 지민이는 물병의 물을 적절히 재분배해서, K개를 넘지 않는 비어있지 않은 물병을 만들려고 한다.

물은 다음과 같이 재분배 한다:
- 먼저 같은 양의 물이 들어있는 물병 두 개를 고른다. 그 다음에 한 개의 물병에 다른 한 쪽에 있는 물을 모두 붓는다. 이 방법을 필요한 만큼 계속 한다.

이런 제약 때문에, N개로 K개를 넘지않는 비어있지 않은 물병을 만드는 것이 불가능할 수도 있다. 다행히도, 새로운 물병을 살 수 있다. 상점에서 사는 물병은 물이 1리터 들어있다.

예를 들어, N=3이고, K=1일 때를 보면, 물병 3개로 1개를 만드는 것이 불가능하다. 한 병을 또다른 병에 부으면, 2리터가 들어있는 물병 하나와, 1리터가 들어있는 물병 하나가 남는다. 만약 상점에서 한 개의 물병을 산다면, 2리터가 들어있는 물병 두 개를 만들 수 있고, 마지막으로 4리터가 들어있는 물병 한 개를 만들 수 있다. (BaekJoon 1052)

Rule 1: 첫째 줄에 N과 K가 주어진다. N은 107보다 작거나 같은 자연수이고, K는 1,000보다 작거나 같은 자연수이다.

ex)
- Input:
        3 1
- Output:
        1


### 핵심원리 - Binary Number approach

- 주어진 숫자를 이진수로 변환하여 물병의 개수를 구한다.

```python
def dec_to_bin(x):
    return int(bin(x)[2:])
```


### 전체 코드

- O(N) where N is a number of water bottle.

```python
# 시뮬레이션
from sys import stdin

N,K = map(int, stdin.readline().split())

# 현재 물병의 최소 개수를 구하기위해 이진수를 구한다 / O(logN)
def dec_to_bin(x):
    return int(bin(x)[2:])

binNum = dec_to_bin(N)  # 2진수를 리스트로 변환한다 / O(N)
lst = list(map(int, str(binNum)))
lenLst = lst.count(1)
revLst = lst[::-1]

# 뒤부터 탐색하며 최대 K개수로 맞춘다 / 최대 O(N)
if lenLst <= K:
    print(0)
else:
    requireK = lenLst - K  # K개수로 맞추기 위해 물을 채워야 할 물병의 위치
    arr = []
    temp = 0

    # 각각 물병의 크기를 구하기 위해 index를 구한다.
    for index, num in enumerate(revLst):
        if num == 1:
            arr.append(index)
    requireN = 2**arr[requireK]  # 필요한 물병의 크기
    for i in range(requireK):
        temp += 2**arr[i]  # 필요한 물병의 위치 미만의 물병들에 이미 들어있는 물의 양
    print(requireN - temp)  # K개수로 맞추기 위해 필요한 물의 양
```

### 다른 풀이

- O(N)으로 같지만 인풋 N 그자체에 추가된 물의 양을 더하며 각 반복 마다 이진수를 구함으로 단계와 시간을 줄였다.

```python
n,k=map(int,input().split())
c=0
while bin(n).count('1')>k:
 a=2**(bin(n)[::-1].index('1'))
 c+=a
 n+=a
print(c)i]
print(res)
```
