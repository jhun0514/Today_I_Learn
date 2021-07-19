# Depth First Search

### 간단 설명

DFS(깊이우선탐색)는 말 그대로 깊이를 우선해서 그래프를 탐색하는 기법

- [참고자료](https://devuna.tistory.com/32?category=890707)

- 시작점인 루트 노드에서 시작하여 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색
- 알고리즘의 핵심은 스택(stack) 자료구조를 사용하는 것 / 물론 스택 없이도 구현 가능하다!
- 경로의 특징을 저장해둬야 하는 문제, 검색 대상 그래프가 정말 큰 문제 등에서는 DFS를 고려한다.


### 파이썬으로 구현

- list를 이용한 stack으로 구현한다.

아래와 같은 유방향 그래프를 DFS로 탐색한다면,

```python
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
```

이렇게 구현한다.

```python
def dfs_step(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited



print(dfs_step(graph_list, root_node))
```

### 전체 코드

```python
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

def dfs_step(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited



print(dfs_step(graph_list, root_node))
```

- output:
        [1, 4, 3, 5, 6, 2]

### 시간 복잡도

- 일반적인 DFS 시간 복잡도
    * 노드 수: V
    * 간선 수: E
        * 위 코드에서 while stack 은 V + E 번 만큼 수행함
    * 시간 복잡도: O(V + E)
