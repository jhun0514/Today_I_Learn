# Kth Smallest Element in a BST

### 문제설영

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree. (leetcode 230)

Rule 1: The number of nodes in the tree is n
Rule 2: 1 <= k <= n <= 10^4
Rule 3: 0 <= Node.val <= 10^4

ex)
- Input: root = [5,3,6,2,4,null,null,1], k = 3
- Output: 3


### in-order traversal

BST의 작은수는 왼쪽이라는 조건을 이용하여 in-order traversal 검색을 한다.

```python
while crr != None or len(stack) != 0:
    while crr != None:
        stack.append(crr)
        crr = crr.left
    crr = stack.pop(-1)
    temp.append(crr.val)
    crr = crr.right
```


### 전체 코드

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        crr = root
        temp = []
        answer = 0
        while crr != None or len(stack) != 0:
            while crr != None:
                stack.append(crr)
                crr = crr.left
            crr = stack.pop(-1)
            temp.append(crr.val)
            crr = crr.right
            if len(temp) == k:
                answer = temp[-1]
                return answer
        return answer
```
