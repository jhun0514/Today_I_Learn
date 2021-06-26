# Letter Combinations of a Phone Number

### 문제설영

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order. A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters. (leetcode 17)

Rule 1: 0 <= digits.length <= 4
Rule 2: digits[i] is a digit in the range ['2', '9'].

ex)
- Input: digits = "23"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


### DFS with recursion

recursion로 모든 combinations를 구해준다

```python
def dfs(point: int, digit:str):
    if point == lend:
        answer.append(digit)
    else:
        letter = keypad[digits[point]]
        for lett in letter:
            dfs(point+1, digit+lett)
```


### 전체 코드

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {'2': "abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        answer = []
        lend = len(digits)
        if digits == "":
            return answer
        def dfs(point: int, digit:str):
            if point == lend:
                answer.append(digit)
            else:
                letter = keypad[digits[point]]
                for lett in letter:
                    dfs(point+1, digit+lett)

        dfs(0,"")   

        return answer

```
