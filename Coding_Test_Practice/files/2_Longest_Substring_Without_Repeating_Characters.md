# Decimal to Binary to Zero with Python

### 문제설영

Given a string s, find the length of the longest substring without repeating characters.
- (leetcode - Longest Substring Without Repeating Characters)

Rule 1: 0 <= s.length <= 5 * 10^4
Rule 2: s consists of English letters, digits, symbols and spaces.

ex) s = "abcabcbb" -> 3  / input: "abcabcbb", output: 3


### Find max range with two pointers

포인터 2개를 이용하여 가장 긴 거리를 찾는다

- Function 대신 while loop를 사용하였다.
- nolastpoint = 마지막 index 감지

```python
while (nolastpoint):
        if rightpoint >= len(s) - 1:
            nolastpoint = False
        newstr = s[rightpoint]
        if newstr not in numset:
            numset[newstr] = [rightpoint]
            rightpoint += 1
            temp += 1
        else:
            numset[newstr].append(rightpoint)
            leftpoint = numset[newstr].pop(0)
            for i in list(numset):
                if numset[i][0] < leftpoint:
                    numset.pop(i)
            temp = rightpoint - leftpoint
            rightpoint += 1
        answer=max(answer,temp)
```

### 전체 코드

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        answer = 0
        temp = 0
        leftpoint = 0
        rightpoint = 0
        numset = {}
        nolastpoint = True
        while (nolastpoint):
            if rightpoint >= len(s) - 1:
                nolastpoint = False
            newstr = s[rightpoint]
            if newstr not in numset:
                numset[newstr] = [rightpoint]
                rightpoint += 1
                temp += 1
            else:
                numset[newstr].append(rightpoint)
                leftpoint = numset[newstr].pop(0)
                for i in list(numset):
                    if numset[i][0] < leftpoint:
                        numset.pop(i)
                temp = rightpoint - leftpoint
                rightpoint += 1
            answer=max(answer,temp)
        return answer
```



### 다른 방법

포인터 대신 맵, max 를 이용하여 거리를 잰다.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
```

### 다른 방법2

enumerate를 이용하여 한번에 index와 알파벳을 구한다. 방법 1과 마찬가지로 dict를 update 해주는 것이 아닌
왼쪽 pointer를 업데이트해준다. 훨씬 시간, 공간으로 효율적

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength
```
