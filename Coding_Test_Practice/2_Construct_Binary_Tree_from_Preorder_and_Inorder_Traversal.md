# Construct Binary Tree from Preorder and Inorder Traversal

### 문제설영

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. (leetcode 105)

Rule 1: preorder and inorder consist of unique values.
Rule 2: Each value of inorder also appears in preorder.

ex)
- Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
- Output: [3,9,20,null,null,15,7]


### Hash Map for inorder index

특정 value 를 받으면 해당 value의 index를 반환하여 준다.

- enumerate를 사용하여 간결하게 구현해주었다.

```python
preorder_index = 0
inorder_index_map = {}
for index, value in enumerate(inorder):
    inorder_index_map[value] = index
```


### Recursion을 이용하여 자식노드를 계속 연결해준다.

핵심 아이디어: inorder는 left,root,right 순으로 이동한다는 것을 이용하여 서브 트리들을 계속만들어 준다.
preorder의 첫 노드는 root노드이고 다음노드는 left인것을 이용하여 preorder의 노드를 inorder 노드에서 찾아 left, right tree로 나누어준다.

- nonlocal로 preorder index를 계속 유지 해준다.

```python
def treeRecursion(left, right):
    nonlocal preorder_index

    if left > right:
        return None

    root = preorder[preorder_index]
    inorder_index = inorder_index_map[root]
    answer = TreeNode(root)

    preorder_index += 1

    answer.left = treeRecursion(left,inorder_index-1)
    answer.right = treeRecursion(inorder_index+1,right)


    return answer
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def treeRecursion(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root = preorder[preorder_index]
            inorder_index = inorder_index_map[root]
            answer = TreeNode(root)

            preorder_index += 1

            answer.left = treeRecursion(left,inorder_index-1)
            answer.right = treeRecursion(inorder_index+1,right)


            return answer




        preorder_index = 0
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return treeRecursion(0,len(preorder)-1)
```
