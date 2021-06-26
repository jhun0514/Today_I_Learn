# Binary Tree Zigzag Level Order Traversal

### 문제설영

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between). (leetcode 103)

Rule 1: The number of nodes in the tree is in the range [0, 2000].
Rule 2: -100 <= Node.val <= 100

ex)
- Input: root = [3,9,20,null,null,15,7]
- Output: [[3],[20,9],[15,7]]


### 자식 노드 찾기

같은 레벨의 노드들을 묶어 주기위해 노드들의 자식노드를 모두 찾아 리턴해준다.

```python
def findChild(listRoot):
    result = []
    for i in listRoot:
        if i.left is not None:
            result.append(i.left)
        if i.right is not None:
            result.append(i.right)
    return result
```


### 모든 레벨을 search

최상위 레벨부터 마지막 레벨까지 findChild를 진행하여 같은 레벨의 노드를 찾아 list로 묶은 뒤 2차원 list로 넣어준다.

```python
while (len(searchList) != 0):
    temp = []
    for i in searchList:
        temp.append(i.val)
    answer.append(temp)
    searchList = findChild(searchList)
```


### zigzag 구현

왼쪽 오른쪽 번갈아가며 노드를 저장하는 순서를 바꾸어야 하기에 완성된 리스트의 순서를 1레벨씩 건너뛰며 reverse를 진행해준다.
- reverse 를 구현하기위해 [::-1]를 이용했다.

```python
while(level < len(answer)):
    temp = answer[level]
    answer[level] = temp[::-1]
    level = level + 2
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        def findChild(listRoot):
            result = []
            for i in listRoot:
                if i.left is not None:
                    result.append(i.left)
                if i.right is not None:
                    result.append(i.right)
            return result

        searchList = [root]
        answer = []
        level = 1

        while (len(searchList) != 0):
            temp = []
            for i in searchList:
                temp.append(i.val)
            answer.append(temp)
            searchList = findChild(searchList)

        while(level < len(answer)):
            temp = answer[level]
            answer[level] = temp[::-1]
            level = level + 2

        return answer
```


### 다른 풀이

스택을 이용하여 간결하게 풀이하였다. 그 외 아이디어는 비슷하다.

```python
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res,stack=[],[root]
        level=0
        while stack:

            if  level%2:
                res.append([node.val for node in stack[::-1]])
            else:
                res.append([node.val for node in stack])
            temp=[]
            for node in stack:
                temp.extend([node.left,node.right])

            stack=[leaf for leaf in temp if leaf]
            level+=1
        return res
```
