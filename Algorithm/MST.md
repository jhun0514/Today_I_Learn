# Minimum Spanning Tree

### 간단 설명

최소 신장 트리란 가능한 Spanning Tree(원래의 그래프의 모든 노드가 연결되어 있으면서 트리의 속성을 만족하는 그래프 / no cycle) 중에서, 간선의 가중치 합이 최소인 Spanning Tree를 지칭함

대표적인 최소 신장 트리 알고리즘
- Kruskal’s algorithm (크루스칼 알고리즘), Prim's algorithm (프림 알고리즘)


### 크루스칼 알고리즘 (Kruskal's algorithm)

- 모든 정점을 독립적인 집합으로 만든다.
- 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.
- 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다. (최소 신장 트리는 사이클이 없으므로, 사이클이 생기지 않도록 하는 것임)
    * 탐욕 알고리즘을 기초로 하고 있음 (당장 눈 앞의 최소 비용을 선택해서, 결과적으로 최적의 솔루션을 찾음)
- Union-Find 알고리즘
    * Disjoint Set을 표현할 때 사용하는 알고리즘으로 트리 구조를 활용하는 알고리즘
    * 간단하게, 노드들 중에 연결된 노드를 찾거나, 노드들을 서로 연결할 때 (합칠 때) 사용
    * Disjoint Set이란
        * 서로 중복되지 않는 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
        * 공통 원소가 없는 (서로소) 상호 배타적인 부분 집합들로 나눠진 원소들에 대한 자료구조를 의미함
        * Disjoint Set = 서로소 집합 자료구조
    * 순서
        1. 초기화
            * n 개의 원소가 개별 집합으로 이뤄지도록 초기화
        2. Union
            * 두 개별 집합을 하나의 집합으로 합침, 두 트리를 하나의 트리로 만듬
        3. Find
            * 여러 노드가 존재할 때, 두 개의 노드를 선택해서, 현재 두 노드가 서로 같은 그래프에 속하는지 판별하기 위해, 각 그룹의 최상단 원소 (즉, 루트 노드)를 확인
    * 주의점
        * Find/Union 시 계산량이 O(N) 이 될 수 있으므로, 해당 문제를 해결하기 위해, union-by-rank, path compression 기법을 사용함
    * union-by-rank 기법
        * 각 트리에 대해 높이(rank)를 기억해 두고
        * Union시 두 트리의 높이(rank)가 다르면, 높이가 작은 트리를 높이가 큰 트리에 붙임 (즉, 높이가 큰 트리의 루트 노드가 합친 집합의 루트 노드가 되게 함)
        * 높이가 h - 1 인 두 개의 트리를 합칠 때는 한 쪽의 트리 높이를 1 증가시켜주고, 다른 쪽의 트리를 해당 트리에 붙여줌
        * 초기화시, 모든 원소는 높이(rank) 가 0 인 개별 집합인 상태에서, 하나씩 원소를 합칠 때, union-by-rank 기법을 사용한다면,
        * 높이가 h 인 트리가 만들어지려면, 높이가 h - 1 인 두 개의 트리가 합쳐져야 함
        * 높이가 h - 1 인 트리를 만들기 위해 최소 n개의 원소가 필요하다면, 높이가 h 인 트리가 만들어지기 위해서는 최소 2n개의 원소가 필요함
        * 따라서 union-by-rank 기법을 사용하면, union/find 연산의 시간복잡도는 O(N) 이 아닌,  𝑂(𝑙𝑜𝑔𝑁)로 낮출 수 있음
    * path compression
        * Find를 실행한 노드에서 거쳐간 노드를 루트에 다이렉트로 연결하는 기법
        * Find를 실행한 노드는 이후부터는 루트 노드를 한번에 알 수 있음
    * union-by-rank 와 path compression 기법 사용시 시간 복잡도는 다음 계산식을 만족함이 증명되었음
        * 𝑂(𝑀𝑙𝑜𝑔∗𝑁)
        * 𝑙𝑜𝑔∗𝑁은 다음 값을 가짐이 증명되었음
        * N이 2^265536 값을 가지더라도, 𝑙𝑜𝑔∗𝑁의 값이 5의 값을 가지므로, 거의 O(1), 즉 상수값에 가깝다고 볼 수 있음


### 파이썬으로 구현

- 아래와 같은 유방향 그래프를 kruskal로 탐색한다면,

```python
mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}
```

이렇게 구현한다.

```python
def kruskal(graph):
    mst = list()

    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결 (사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst
```

### 전체 코드

```python
mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()


def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()

    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결 (사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst
```

- output:
        [(5, 'A', 'D'),
         (5, 'C', 'E'),
         (6, 'D', 'F'),
         (7, 'A', 'B'),
         (7, 'B', 'E'),
         (9, 'E', 'G')]

### 시간 복잡도

- 크루스컬 알고리즘의 시간 복잡도는 O(E log E)
    * 간선 수: E
    * 노드 수: V
    * 간선을 비용 기준으로 정렬하는 시간에 좌우됨 (즉 간선을 비용 기준으로 정렬하는 시간이 가장 큼)
    * 과정1: 모든 정점을 독립적인 집합으로 만든다.
        * O(V)
    * 과정2: 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.
        * 𝑂(𝐸𝑙𝑜𝑔𝐸)
    * 과정3: 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다. (최소 신장 트리는 사이클이 없으므로, 사이클이 생기지 않도록 하는 것임)
        * union-by-rank 와 path compression 기법 사용시 시간 복잡도가 결국 상수값에 가까움, O(1)
        * 𝑂(𝐸)
- 참고 - 힙큐 시간복잡도
    * depth (트리의 높이) 를 h라고 표기한다면,
    * n개의 노드를 가지는 heap 에 데이터 삽입 또는 삭제시, 최악의 경우 root 노드에서 leaf 노드까지 비교해야 하므로 h=log2n 에 가까우므로, 시간 복잡도는 O(logn)


### 프림 알고리즘 (Prim's algorithm)

- 시작 정점을 선택한 후, 정점에 인접한 간선중 최소 간선으로 연결된 정점을 선택하고, 해당 정점에서 다시 최소 간선으로 연결된 정점을 선택하는 방식으로 최소 신장 트리를 확장해가는 방식
- Kruskal's algorithm 과 Prim's algorithm 비교
    * 둘다, 탐욕 알고리즘을 기초로 하고 있음 (당장 눈 앞의 최소 비용을 선택해서, 결과적으로 최적의 솔루션을 찾음)
    * Kruskal's algorithm은 가장 가중치가 작은 간선부터 선택하면서 MST를 구함
    * Prim's algorithm은 특정 정점에서 시작, 해당 정점에 연결된 가장 가중치가 작은 간선을 선택, 간선으로 연결된 정점들에 연결된 간선 중에서 가장 가중치가 작은 간선을 택하는 방식으로 MST를 구함
- 순서
    * 임의의 정점을 선택, '연결된 노드 집합'에 삽입
    * 선택된 정점에 연결된 간선들을 간선 리스트에 삽입
    * 간선 리스트에서 최소 가중치를 가지는 간선부터 추출해서,
        * 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 이미 들어 있다면, 스킵함(cycle 발생을 막기 위함)
        * 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 들어 있지 않으면, 해당 간선을 선택하고, 해당 간선 정보를 '최소 신장 트리'에 삽입
            * 해당 간선에 연결된 인접 정점의 간선들 중, '연결된 노드 집합(connected_nodes)' 에 없는 노드와 연결된 간선들만 간선 리스트(candidate_edge_list) 에 삽입
    * 추출한 간선은 간선 리스트에서 제거
    * 간선 리스트에 더 이상의 간선이 없을 때까지 3-4번을 반복


### 파이썬으로 구현

- heapq 라이브러리 활용을 통해 우선순위 큐를 사용한다.

아래와 같은 유방향 그래프를 prim으로 탐색한다면,

```python
myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]
```

이렇게 구현한다.

```python
def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst
```

### 전체 코드

```python
myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

from collections import defaultdict
from heapq import *

def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst
```

- output:
        [(5, 'A', 'D'),
        (6, 'D', 'F'),
        (7, 'A', 'B'),
        (7, 'B', 'E'),
        (5, 'E', 'C'),
        (9, 'E', 'G')]

### 시간 복잡도

- 최악의 경우, while 구문에서 모든 간선에 대해 반복하고, 최소 힙 구조를 사용하므로 O(𝐸𝑙𝑜𝑔𝐸) 시간 복잡도를 가짐
    * 간선 수: E
    * 노드 수: V
- 참고 - 개선된 프림 알고리즘
    * 간선이 아닌 노드를 중심으로 우선순위 큐를 적용하는 방식
        * 초기화 - 정점:key 구조를 만들어놓고, 특정 정점의 key값은 0, 이외의 정점들의 key값은 무한대로 놓음. 모든 정점:key 값은 우선순위 큐에 넣음
        * 가장 key값이 적은 정점:key를 추출한 후(pop 하므로 해당 정점:key 정보는 우선순위 큐에서 삭제됨), (extract min 로직이라고 부름)
        * 해당 정점의 인접한 정점들에 대해 key 값과 연결된 가중치 값을 비교하여 key값이 작으면 해당 정점:key 값을 갱신
            * 정점:key 값 갱신시, 우선순위 큐는 최소 key값을 가지는 정점:key 를 루트노드로 올려놓도록 재구성함 (decrease key 로직이라고 부름)
    * 개선된 프림 알고리즘 구현시 고려 사항
        * 우선순위 큐(최소힙) 구조에서, 이미 들어가 있는 데이터의 값 변경시, 최소값을 가지는 데이터를 루트노드로 올려놓도록 재구성하는 기능이 필요함
        * 구현 복잡도를 줄이기 위해, heapdict 라이브러리를 통해, 해당 기능을 간단히 구현

    ```python
    from heapdict import heapdict

    def prim(graph, start):
        mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
        for node in graph.keys():
            keys[node] = float('inf')
            pi[node] = None
        keys[start], pi[start] = 0, start

        while keys:
            current_node, current_key = keys.popitem()
            mst.append([pi[current_node], current_node, current_key])
            total_weight += current_key
            for adjacent, weight in mygraph[current_node].items():
                if adjacent in keys and weight < keys[adjacent]:
                    keys[adjacent] = weight
                    pi[adjacent] = current_node
        return mst, total_weight

    mygraph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}    
    }
    mst, total_weight = prim(mygraph, 'A')
    print ('MST:', mst)
    print ('Total Weight:', total_weight)
    ```

    * 개선된 프림 시간복잡도 𝑂(𝐸𝑙𝑜𝑔𝑉)
        * 최초 key 생성 시간 복잡도: 𝑂(𝑉)
        * while 구문과 keys.popitem() 의 시간 복잡도는 𝑂(𝑉𝑙𝑜𝑔𝑉)
            * while 구문은 V(노드 갯수) 번 실행됨
            * heap 에서 최소 key 값을 가지는 노드 정보 추출 시(pop)의 시간 복잡도:  𝑂(𝑙𝑜𝑔𝑉)
        * for 구문의 총 시간 복잡도는 𝑂(𝐸𝑙𝑜𝑔𝑉)
            * for 구문은 while 구문 반복시에 결과적으로 총 최대 간선의 수 E만큼 실행 가능 𝑂(𝐸)
            * for 구문 안에서 key값 변경시마다 heap 구조를 변경해야 하며, heap 에는 최대 V 개의 정보가 있으므로 𝑂(𝑙𝑜𝑔𝑉)
            
    > 일반적인 heap 자료 구조 자체에는 본래 heap 내부의 데이터 우선순위 변경시, 최소 우선순위 데이터를 루트노드로 만들어주는 로직은 없음. 이를 decrease key 로직이라고 부름, 해당 로직은 heapdict 라이브러리를 활용해서 간단히 적용가능

* 참고자료 - fastcampus: 알고리즘    
