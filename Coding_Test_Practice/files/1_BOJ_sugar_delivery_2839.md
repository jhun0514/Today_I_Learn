# 설탕배달

### 문제설명

상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오. (BaekJoon 2839)

Rule: 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

ex)
- Input:
        18
- Output:
        4


### 핵심원리 - Greedy approach

- 그리디한 접근으로 풀기 위해 최대한 5로 나눈 몫을 가져가게 만들기 위해 3,6,9,12 순으로 체크를 진행한다. (3과 5의 최소 공배수는 3,6,9,12,5의 조합으로 이루어져 있다.)

```python
if (n%3 == 0 and n < 10):
    print(n//3)
elif ((n-3)%5 == 0 and n >= 3):
    print((n-3)//5 + 1)
elif ((n-6)%5 == 0 and n >= 6):
    print((n-6)//5 + 2)
elif ((n-9)%5 == 0 and n >= 9):
    print((n-9)//5 + 3)
elif ((n - 12) % 5 == 0 and n >= 12):
    print((n - 12) // 5 + 4)
else:
    print(-1)
```


### 전체 코드

- O(1) / 68ms

```python
n = int(input())

if (n%5 == 0):
    print(n//5)
else:
    if (n%3 == 0 and n < 10):
        print(n//3)
    elif ((n-3)%5 == 0 and n >= 3):
        print((n-3)//5 + 1)
    elif ((n-6)%5 == 0 and n >= 6):
        print((n-6)//5 + 2)
    elif ((n-9)%5 == 0 and n >= 9):
        print((n-9)//5 + 3)
    elif ((n - 12) % 5 == 0 and n >= 12):
        print((n - 12) // 5 + 4)
    else:
        print(-1)

```


### 다른 풀이

- O(1) 기본적인 흐름은 동일하지만 while 문으로 5로 나눈 나머지가 3으로 나누어 지지 않는다면 몫에서 5를 빼서 나머지에 더한 후 다시 나누어 주는 것을 반복한다. 실행시간 자체는 이 풀이가 58ms 로 더 빠르다.

```python
n = int(input())

a = n//5
b = n%5
c = 0

while a>=0:
    if b%3 == 0:
        c = b//3

        break
    a -= 1
    b += 5

if b%3 == 0:
    print(a+c)
else:
    print(-1)
```