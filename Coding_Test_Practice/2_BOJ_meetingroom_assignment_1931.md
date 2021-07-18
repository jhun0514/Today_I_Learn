# 회의실 배정

### 문제설명

한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다. (BaekJoon 1931)

Rule: 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100000)

ex)
- Input:
        2
        12
        34
        14
- Output:
        2


### 핵심원리 - Greedy with sorting by end time (with sub start time)

- 회의 끝나는 시간 기준으로 정렬을 하면서 동일 시간 존재시 시작시간 순으로 정렬을 한다.

```python
sortedTime = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
```


### 전체 코드

- O(N) 끝나는 시간 순으로 정렬된 리스트를 가지고 겹치지 않는 시작~끝 집합의  개수를 구한다.

```python
n = int(input())
sortedTime = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
answer, endTime = 0,0
for sTime, eTime in sortedTime:
    if sTime >= endTime:
        answer += 1
        endTime = eTime
print(answer)
```


### 다른 풀이

- O(N) 정렬이라는 기본 방향은 같지만 해시테이블을 이용하여 각 시작 시간 별 끝나는 시간들을 모아 정렬해준다. 그 후 시작시간 키값 만을 정렬 하여 for 문으로 하나씩 탐색하며 겹치지 않는 집합을 카운트한다. 이때 시작시간은 늦더라도 끝나는 시간이 더 빠르면 끝나는 시간을 업데이트 해준다.

```python
N = int(input())
dic = {}
for _ in range(N):
    start, end = map(int, input().split())
    if dic.get(start):
        dic[start].append(end)  # min(dic.get(start, float('inf')), end)
    else:
        dic[start] = [end]

for k in dic.keys():
    dic[k].sort()

keys = sorted(dic.keys())
print(dic)
end = 0
count = 0
for key in keys:
    for e in dic[key]:
        if e < end:
            print(e)
            end = e
        elif key >= end:
            count += 1
            end = e
            print(key, e)

print(count)
```
