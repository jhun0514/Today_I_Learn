# Group Anagrams

### 문제설영

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
- (leetcode - Group Anagrams)

Rule 1: 1 <= strs.length <= 10^4
Rule 2: 0 <= strs[i].length <= 100
Rule 3: strs[i] consists of lower-case English letters.

ex) strs = ["eat","tea","tan","ate","nat","bat"] -> [["bat"],["nat","tan"],["ate","eat","tea"]]


### Add the anagrams to answer

Sort를 이용하여 같은 알파벳을 소유한 string들을 찾는다.

```python
for i in strs:
    sortways =sorted(i)
    sortway ="".join(sortways)
    if sortway not in subset:
        subset[sortway] = []
        subset[sortway].append(i)
    else:
        subset[sortway].append(i)
```

### 전체 코드

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        if strs == [""]:
            return [[""]]
        answer = []
        subset = {}
        for i in strs:
            sortways =sorted(i)
            sortway ="".join(sortways)
            if sortway not in subset:
                subset[sortway] = []
                subset[sortway].append(i)
            else:
                subset[sortway].append(i)
        for i in subset:

            answer.append(subset[i])
        return answer
```



### 다른 방법

collections.defaultdict를 이용하면 한번에 append 가능하다. tuple이면 dict key로 이용가능.

```python
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
```
