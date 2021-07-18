# 이상한 하노이 탑

### 문제설명

승민이는 기존 하노이 탑 문제를 약간 변형한 이상한 하노이 탑 문제를 만들었다.

이상한 하노이 탑 문제와 기존 하노이 탑 문제와 다른 점이 2가지가 있는데 하나는 "쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.(중간 과정 역시 그래야함)" 라는 조건이 삭제되었다는 점이고 또 다른 하나는 첫 번째 장대에 원판들이 반경 상관없이 무작위로 배치되어 있다는 점이다.

승민이는 이 문제를 진수에게 주었고 원판을 옮긴 횟수가 12345보다 같거나 작으면 피자를 사주기로 하였다. 진수를 도와 피자를 먹게 해주자! (BaekJoon 15500)

Rule 1: 첫 번째 줄에는 원판의 개수 N (1 ≤ N ≤ 123) 이 주어진다.
Rule 2: 두 번째 줄에는 첫 번째 장대에 있는 원판들의 반경 나타내는 정수 ai (1 ≤ ai ≤ N) 들이 공백을 두고 주어진다. (제일 아래에 있는 원판의 반경부터 주어진다.)

ex)
- Input:

        3 1

- Output:

        1


### 핵심원리 - Greedy approach

- 그리디 접근법으로 가장 큰 원판부터 3번째 막대에 넣었다.

```python
for findItem in range(N, 0, -1):
    a, b, ind = (0, 1, lst[0].index(findItem)) if findItem in lst[0] else (1, 0, lst[1].index(findItem))

    for i in range(len(lst[a])-1, ind, -1):
        res.append([a+1, b+1])
        lst[b].append(lst[a].pop())

    lst[a].pop()
    res.append([a+1, 3])
```


### 전체 코드

- O(N^2) where N is a number of disks.

```python
# 스택 with greedy
from sys import stdin

N = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
lst, res = [a,[]], []

# O(N^2) / worst case 에서 N-1, N-2, ... 1 개 반복한다.
for findItem in range(N, 0, -1):
    a, b, ind = (0, 1, lst[0].index(findItem)) if findItem in lst[0] else (1, 0, lst[1].index(findItem))

    for i in range(len(lst[a])-1, ind, -1):
        res.append([a+1, b+1])
        lst[b].append(lst[a].pop())

    lst[a].pop()
    res.append([a+1, 3])

print(len(res))
for a, b in res:
    print('{0} {1}'.format(a, b))
# 반론: 2 4 1 3 일때 7가 최소이지만 이 알고리즘 대로는 8 / 문제가 완벽하지 않다.
```

### 다른 풀이 by asdhugh1

- O(N^2)으로 같은 개념으로 문제를 풀었지만 function으로 나누었다.

```python
count = int(input())
first = list(map(int, input().split()))
second = []

biggest_to_smallest = sorted(first, reverse=True)

popping_first = True
move_count = 0

buf = []


def process(this, this_id, other, other_id):
    popped = this.pop()
    if biggest_to_smallest[0] == popped:
        biggest_to_smallest.pop(0)
        if len(biggest_to_smallest) > 0:
            global popping_first
            popping_first = biggest_to_smallest[0] in first
        buf.append(f"{this_id} 3")
    else:
        other.append(popped)
        buf.append(f"{this_id} {other_id}")


while len(biggest_to_smallest) > 0:
    if popping_first:
        process(first, "1", second, "2")
    else:
        process(second, "2", first, "1")
    move_count += 1

print(move_count)
print("\n".join(buf))
```
