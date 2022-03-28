# BFS
import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
move = dict()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    move[x] = y

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    move[x] = y

Q, visited, answer = [], [0] * 101, 0
heapq.heappush(Q, [0,1])
visited[1] = 1

while Q:
    count, now = heapq.heappop(Q)
    # 100 도달
    if now == 100:
        answer = count
        break
    # 주사위 1~6
    for i in range(1,7):
        if now + i < 101:
            if visited[now+i] == 0:
                if now+i in move.keys():
                    heapq.heappush(Q, [count + 1, move[now + i]])
                    visited[move[now+i]] = 1
                else:
                    heapq.heappush(Q, [count + 1, now + i])
                    visited[now+i] = 1
print(answer)
