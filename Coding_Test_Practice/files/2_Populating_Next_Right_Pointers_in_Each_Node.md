# Populating Next Right Pointers in Each Node

### 문제설영

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. (leetcode 116)

Rule 1: Initially, all next pointers are set to NULL.
Rule 2: The number of nodes in the given tree is less than 4096.

ex)
- Input: root = [1,2,3,4,5,6,7]
- Output: [1,#,2,3,#,4,5,6,7,#]


### BFS with queue

queue를 이용하여 BFS 검색을 한다.

```python
queue = [root]
while queue:
    node = queue.pop(0)
    if node.left and node.right:
        node.left.next = node.right
        if node.next:
            node.right.next = node.next.left
        queue.append(node.left)
        queue.append(node.right)
```


### 전체 코드

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                queue.append(node.left)
                queue.append(node.right)
        return root
```


### 다른 풀이

recursion으로 간결하게 풀이하였다. 그 외 아이디어는 비슷하다.

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        def connect1(self, root):
            if root and root.left and root.right:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                self.connect1(root.left)
                self.connect1(root.right)
        return root
```
