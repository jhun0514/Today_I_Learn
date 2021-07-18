# Count and Say

### 문제설명

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

- countAndSay(1) = "1"
- countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying. (Leetcode 38)

Rule: 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

ex)

- Input:
        3322251
- Output:
        23321511


### 핵심원리 - Brute Force

- 완전 탐색 접근 방법으로 각 단계별 숫자를 분석하여 연속된 같은 숫자를 카운트하여 새로운 str를 만든다.

```python
while(tp < len(temp)):
    if tp+1 < len(temp) and temp[tp] == temp[tp+1]:
        pointer += 1
    else:
        answer=answer + str(pointer) + temp[tp]
        pointer = 1
    tp += 1
```


### 전체 코드

- O(n*a) where a is a count and say str for each step

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        pointer = 1
        answer = "1"
        for i in range(n-1):
            temp = answer
            answer = ""
            tp = 0
            while(tp < len(temp)):
                if tp+1 < len(temp) and temp[tp] == temp[tp+1]:
                    pointer += 1
                else:
                    answer=answer + str(pointer) + temp[tp]
                    pointer = 1
                tp += 1

        return answer
```


### 다른 풀이

- O(n*a) 각 단계별로 regex 정규 표현식을 이용하여 각 중복 숫자의 부분 집합과 중복 숫자를 구한다. (.) 는 처음 나오는 숫자를 고른다. 그뒤에 따라오는 \ 2*는 (.)과 같은 숫자를 모두 고른다(바로 따라오는 숫자만) group은 이렇게 픽한 부분집합을 저장하고 digit은 (.)를 저장한다. 이렇게 모든 부분집합을 구한다.

```python
def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(group)) + digit
                    for group, digit in re.findall(r'((.)\2*)', s))
    return s
```
