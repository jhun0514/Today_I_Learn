# Breadth First Search

### 간단 설명

BFS(너비우선탐색)는 말 그대로 너비를 우선해서 그래프를 탐색하는 기법

<img src="../source/algorithm/Breadth-First-Search-Algorithm.gif" alt="image-BFS" style="zoom:50%;" />

- 시작점인 루트 노드와 같은 거리에 있는 노드를 우선으로 방문
- 알고리즘의 핵심은 큐(queue) 자료구조를 사용하는 것 / 물론 큐없이도 구현 가능하다!
- 노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드의 정보만 큐에 넣어 먼저 큐에 들어있던 노드부터 방문하면 되는 것


### 파이썬으로 구현

- list로 구현시 append와 pop을 이용해야 하는데, pop의 경우 O(N)의 시간복잡도라 이렇게 구현하면 시간적으로 매우 비효율적인 코드가 된다.
- 따라서 collections 라이브러리의 deque를 사용한다.
- 또한 인접 노드 중 방문하지 않았던 노드를 큐에 넣을 때는 파이썬 데이터 타입 중 set 을 사용하면 아주 쉽게 구현할 수 있다.

아래와 같은 유방향 그래프를 BFS로 탐색한다면,

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
from collections import deque

def bfs_step(graph, root):
    visited = []
    queue = deque([root])

    while(queue):
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited



print(bfs_step(graph_list, root_node))
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

from collections import deque

def bfs_step(graph, root):
    visited = []
    queue = deque([root])

    while(queue):
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited



print(bfs_step(graph_list, root_node))
```

- output: [1, 3, 4, 5, 2, 6]
