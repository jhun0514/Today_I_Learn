# Bfs
import sys
from collections import deque

def bfsPassenger(taxi): # 최단 경로 검색
    q = deque()
    q.append(taxi)
    visited, minDistance = [[0] * N for _ in range(N)], 1e9
    candidate = [] # 후보 저장
    while q:
        x, y = q.popleft()
        if visited[x][y] > minDistance:
            break
        if [x, y] in passenger: # 최단 경로 손님 찾기
            minDistance = visited[x][y]
            candidate.append([x, y])
        else:
            for d in range(4):
                nx, ny = x + dxdy[d][0], y + dxdy[d][1]
                if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] != 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
    if candidate:
       candidate.sort()
       return visited[candidate[0][0]][candidate[0][1]], candidate[0][0], candidate[0][1]
    else: # 갈 수 없는 경우
       return -1, -1, -1


def bfsDestination(start, end): # 목적지 최단경로
    q = deque()
    q.append(start)
    visited, x, y = [[0] * N for _ in range(N)], 0, 0
    while q:
        x, y = q.popleft()
        if [x, y] == end:
            break
        for d in range(4):
            nx, ny = x + dxdy[d][0], y + dxdy[d][1]
            if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] != 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    return visited[x][y], x, y

N, M, fuel = map(int, sys.stdin.readline().split())
lst = [list(map(int, input().split())) for _ in range(N)]
taxiY, taxiX = map(int, input().split())
taxi, passenger, destinations, dxdy = [taxiY - 1, taxiX - 1], [], [], [[1, 0], [0, 1], [-1, 0], [0, -1]]

for _ in range(M):
    px, py, dx, dy = map(int, input().split())
    passenger.append([px - 1, py - 1])
    destinations.append([dx - 1, dy - 1])

for _ in range(M):
    distance, px, py = bfsPassenger(taxi) # 최단 경로 검색
    if distance == -1 or fuel - distance < 0: # 손님에게 못가거나 연료가 부족하면 종료
        fuel = -1
        break
    fuel,idx = fuel-distance, passenger.index([px, py])  # 남은기름, 손님위치
    passenger[idx] = [-1, -1] # 손님을 태웠기에 bfsPassenger에서 제외되기 위해 [-1, -1]로 설정하기
    distance2, px2, py2 = bfsDestination([px, py], destinations[idx])
    if [px2, py2] != destinations[idx] or fuel - distance2 < 0: # 도착지에 도달하지 못하거나 연료가 부족하면 종료
        fuel = -1
        break
    fuel += distance2 # fuel - dis + dis + dis
    taxi = [px2, py2] # 갱신

print(fuel)
