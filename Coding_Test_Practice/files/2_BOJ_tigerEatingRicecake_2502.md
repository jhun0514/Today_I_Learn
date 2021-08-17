# 후보 추천하기

### 문제설명

월드초등학교 학생회장 후보는 일정 기간 동안 전체 학생의 추천에 의하여 정해진 수만큼 선정된다. 그래서 학교 홈페이지에 추천받은 학생의 사진을 게시할 수 있는 사진틀을 후보의 수만큼 만들었다. 추천받은 학생의 사진을 사진틀에 게시하고 추천받은 횟수를 표시하는 규칙은 다음과 같다.

- 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
- 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
- 비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 그 자리에 새롭게 추천받은 학생의 사진을 게시한다. 이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.
- 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
- 사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.

후보의 수 즉, 사진틀의 개수와 전체 학생의 추천 결과가 추천받은 순서대로 주어졌을 때, 최종 후보가 누구인지 결정하는 프로그램을 작성하시오. (BaekJoon 1713)

Rule 1: 첫째 줄에는 사진틀의 개수 N이 주어진다. (1 ≤ N ≤ 20) 둘째 줄에는 전체 학생의 총 추천 횟수가 주어지고, 셋째 줄에는 추천받은 학생을 나타내는 번호가 빈 칸을 사이에 두고 추천받은 순서대로 주어진다.
Rule 2: 총 추천 횟수는 1,000번 이하이며 학생을 나타내는 번호는 1부터 100까지의 자연수이다.

ex)

- Input:

        3
        9
        2 1 4 3 5 6 2 7 2

- Output:

        2 6 7


### 핵심원리 - DP

- 동적계산으로 해당 날에 누적된 첫째날과 둘째날의 떡의 계수를 구한다.

```python
for i in range(2, D):
    dp[i] = dp[i-2] + dp[i-1]

xCount, yCount = dp[D-1].count('x'), dp[D-1].count('y')
```


### 전체 코드

- O(K/2) where K is a number of given rice cake.

```python
# DP
from sys import stdin
D, K = map(int, stdin.readline().split())
dp, xCount, yCount = [[] for _ in range(30)], 0, 0
dp[0], dp[1] = ['x'], ['y']

for i in range(2, D):
    dp[i] = dp[i-2] + dp[i-1]

xCount, yCount = dp[D-1].count('x'), dp[D-1].count('y')

for i in range(int(K/2)):
    if (K - xCount * i) % yCount == 0:
        print(i)
        print((K - xCount * i) // yCount)
        break
```

### 다른 풀이 by bumipunzel

- O(K/2)으로 최대 시간은 같지만 count 대신 누적 수를 리스트에 직접 저장 함으로써 시간을 줄였다.

```python
day=[1,1]
d,k=map(int,input().split())
while True:
  if len(day)==d-1:
    break
  day.append(day[-1]+day[-2])
ap=day[-2]
bp=day[-1]
i=1
while True:
  t=(k-ap*i)
  if t%bp==0:
    a=i
    b=t//bp
    break
  i+=1
print(a)
print(b)
```
