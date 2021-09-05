# 줄어들지 않아

### 문제설명

어떤 숫자가 줄어들지 않는다는 것은 그 숫자의 각 자리 수보다 그 왼쪽 자리 수가 작거나 같을 때 이다.

예를 들어, 1234는 줄어들지 않는다.

줄어들지 않는 4자리 수를 예를 들어 보면 0011, 1111, 1112, 1122, 2223이 있다. 줄어들지 않는 4자리수는 총 715개가 있다.

이 문제에서는 숫자의 앞에 0(leading zero)이 있어도 된다. 0000, 0001, 0002는 올바른 줄어들지 않는 4자리수이다.

n이 주어졌을 때, 줄어들지 않는 n자리 수의 개수를 구하는 프로그램을 작성하시오. (BaekJoon 2688)

Rule 1: 첫째 줄에 테스트 케이스의 개수 T(1 <= T <= 1,000)이 주어진다. 각 테스트 케이스는 숫자 하나 n으로 이루어져 있다. (1 <= n <= 64)

ex)

- Input:

        3
        2
        3
        4

- Output:

        55
        220
        715


### 핵심원리 - Dynamic programming

- 동적 프로그래밍 알고리즘으로 가장 작은 수 부터 계산 하여 점점 커지며 큰 수를 계산할 때 사용한다.

```python
lst = [0] + [1] * 10
for _ in range(N):
    for j in range(1, 11):
        lst[j] += lst[j - 1]
```


### 전체 코드

- O(TN) where T, N are the numbers of test case and num size.

```python
# Dynamic programming
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(input())
    lst = [0] + [1] * 10
    for _ in range(N):
        for j in range(1, 11):
            lst[j] += lst[j - 1]
    print(lst[10])
```

### 다른 풀이 by ssw3095

- O(T)로 먼저 모든 경우를 계산하고 테스트 케이스를 돌린다. 범위가 작기에 가능.

```python
import sys

list_memo= [[0]*10 for _ in range(65)]
list_memo[1] =[1]*10
for i in range(2,65):
    for j in range(10):
        for k in range(j,10):
            list_memo[i][k] += list_memo[i-1][j]

T = int(sys.stdin.readline())
for _ in range(T):
    print(sum(list_memo[int(sys.stdin.readline())]))
```
