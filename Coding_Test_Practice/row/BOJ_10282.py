# Dijkstra
import heapq
from sys import stdin

def dijkstra(s):
    hData, distance[s] = [], 0
    heapq.heappush(hData, (0,s))

    while hData:
        dist, now = heapq.heappop(hData)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            time = dist + i[1]
            if distance[i[0]] > time:
                distance[i[0]] = time
                heapq.heappush(hData, (time, i[0]))

for _ in range(int(stdin.readline())):
    N, D, C = map(int, stdin.readline().split())
    adj, distance = [[] for i in range(N+1)], [1e9] * (N+1)
    for _ in range(D):
        x,y,time = map(int, stdin.readline().split())
        adj[y].append((x,time))
    dijkstra(C)
    count, maxD = 0, 0
    for i in distance:
        if i != 1e9:
            count += 1
            if i > maxD:
                maxD = i
    print(count, maxD)
