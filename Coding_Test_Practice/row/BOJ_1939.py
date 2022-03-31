# Binary Search
import sys
from collections import deque, defaultdict

N, M = map(int, sys.stdin.readline().split())
bridge, left, right, answer = defaultdict(list), 1, 1e9, 1
for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    bridge[A].append((B, C))
    bridge[B].append((A, C))
    right = max(right, C)
first, last = map(int, sys.stdin.readline().split())

def bfs(mid):
    visited = [0 for _ in range(N+1)]
    visited[first] = 1
    q = deque([first])
    while q:
        island = q.popleft()
        if island == last:
            return True
        for b, c in bridge[island]:
            if not visited[b] and c >= mid:
                q.append(b)
                visited[b] = 1
    return False

while left <= right:
    mid = int((left+right)/2)
    if bfs(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
