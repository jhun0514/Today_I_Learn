# Dijkstra

### 간단 설명

최단 경로 문제란 두 노드를 잇는 가장 짧은 경로를 찾는 문제이고 가중치 그래프 (Weighted Graph) 에서 간선 (Edge)의 가중치 합이 최소가 되도록 하는 경로를 찾는 것이 목적이다.

다익스트 알고리즘은 최단 경로 알고리즘 중 하나의 정점에서 다른 모든 정점 간의 각각 가장 짧은 거리를 구하는 알고리즘이다.

- 첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 갱신하는 기법
- 다익스트라 알고리즘은 너비우선탐색(BFS)와 유사
    * 첫 정점부터 각 노드간의 거리를 저장하는 배열을 만든 후, 첫 정점의 인접 노드 간의 거리부터 먼저 계산하면서, 첫 정점부터 해당 노드간의 가장 짧은 거리를 해당 배열에 업데이트
- 우선순위 큐를 활용한 다익스트라 알고리즘
    * 첫 정점을 기준으로 배열을 선언하여 첫 정점에서 각 정점까지의 거리를 저장
        * 초기에는 첫 정점의 거리는 0, 나머지는 무한대로 저장함 (inf 라고 표현함)
        * 우선순위 큐에 (첫 정점, 거리 0) 만 먼저 넣음
    * 우선순위 큐에서 노드를 꺼냄
        * 처음에는 첫 정점만 저장되어 있으므로, 첫 정점이 꺼내짐
        * 첫 정점에 인접한 노드들 각각에 대해, 첫 정점에서 각 노드로 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지의 거리를 비교한다.
        * 배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우, 배열에 해당 노드의 거리를 업데이트한다.
        * 배열에 해당 노드의 거리가 업데이트된 경우, 우선순위 큐에 넣는다.
            * 결과적으로 너비 우선 탐색 방식과 유사하게, 첫 정점에 인접한 노드들을 순차적으로 방문하게 됨
            * 만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다, 더 긴 거리(루트)를 가진 (노드, 거리)의 경우에는 해당 노드와 인접한 노드간의 거리 계산을 하지 않음
    * 2번의 과정을 우선순위 큐에 꺼낼 노드가 없을 때까지 반복한다.


### 파이썬으로 구현

- heapq 라이브러리 활용을 통해 우선순위 큐를 사용한다.

아래와 같은 유방향 그래프를 Dijkstra로 탐색한다면,

```python
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
```

이렇게 구현한다.

```python
def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances
```

### 전체 코드

```python
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances
```

- output:
        {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}

### 시간 복잡도

- 다익스트라 알고리즘은 크게 다음 두 가지 과정을 거침
    * 간선 수: E
    * 과정1: 각 노드마다 인접한 간선들을 모두 검사하는 과정
        * O(E)
    * 과정2: 우선순위 큐에 노드/거리 정보를 넣고 삭제(pop)하는 과정
        * 𝑂(𝐸𝑙𝑜𝑔𝐸)
    * 시간 복잡도: 𝑂(𝐸𝑙𝑜𝑔𝐸)
- 참고 - 힙큐 시간복잡도
    * depth (트리의 높이) 를 h라고 표기한다면,
    * n개의 노드를 가지는 heap 에 데이터 삽입 또는 삭제시, 최악의 경우 root 노드에서 leaf 노드까지 비교해야 하므로 h=log2n 에 가까우므로, 시간 복잡도는 O(logn)

* 참고자료 - fastcampus: 알고리즘
