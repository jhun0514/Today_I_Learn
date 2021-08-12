# 신입 사원

### 문제설명

언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.

그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오. (BaekJoon 1946)

Rule 1: 첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.

ex)

- Input:

        2
        5
        3 2
        1 4
        4 1
        2 3
        5 5
        7
        3 6
        7 3
        4 2
        1 4
        5 7
        2 5
        6 1

- Output:

        4
        3


### 핵심원리 - Greedy

- 정렬 후 맨앞의 순위를 저장하여 이보다 크면 제외 아니면 카운트를 올리고 새로저장하여 다음을 비교한다.

```python
lst.sort()
tmp = lst[0][1]

for i in range(1, N):
    if lst[i][1] < tmp:
        save+=1
        tmp = lst[i][1]
```


### 전체 코드

- O(TNlogN) where T, N are a number of cases and a number of candidates.

```python
# Greedy
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    lst, save = [list(map(int, stdin.readline().split())) for __ in range(N)], 1
    lst.sort()
    tmp = lst[0][1]

    for i in range(1, N):
        if lst[i][1] < tmp:
            save+=1
            tmp = lst[i][1]
    print(save)
```

### 다른 풀이 by wkddkdud99

- O(TN)으로 sorting 대신 인덱스 자체로 정렬을 대체하여 시간복잡도를 줄였다.

```python
import sys
input = sys.stdin.readline
def solution():
    case = int(input())
    answers = []
    for _ in range(case):
        n = int(input())
        scores = [0]*(n+1)
        for _ in range(n):
            s1, s2 = map(int, input().split())
            scores[s1] = s2
        answer = 1
        min = scores[1]
        for score in scores[2:]:
            if(score<min):
                answer += 1
                min = score
        answers.append(str(answer))
    print('\n'.join(answers))
solution()
```
