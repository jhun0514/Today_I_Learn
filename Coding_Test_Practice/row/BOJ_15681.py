# DFS with DP
import sys
sys.setrecursionlimit(10**6)
N, R, Q = map(int, sys.stdin.readline().split())
connected, child, size = list([] for _ in range(N+1)), list([] for _ in range(N+1)), list(0 for _ in range(N+1))
for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    connected[x].append(y)
    connected[y].append(x)

def makeTree(current, parent):
    for nod in connected[current]:
        if nod != parent:
            child[current].append(nod)
            makeTree(nod, current)

def countSubTreeNode(currentNode):
    size[currentNode] = 1
    for nod in child[currentNode]:
        countSubTreeNode(nod)
        size[currentNode] += size[nod]

makeTree(R, -1)
countSubTreeNode(R)
for _ in range(Q):
    print(size[int(sys.stdin.readline().rstrip())])
