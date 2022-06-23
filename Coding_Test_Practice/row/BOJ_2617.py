# DFS

import sys

N, M = list(map(int, sys.stdin.readline().split()))
bigger = [[0] * (N + 1) for _ in range(N + 1)]
smaller = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    num1, num2 = list(map(int, sys.stdin.readline().split()))
    bigger[num1][num2] = 1
    smaller[num2][num1] = 1

def countNode(N, lst):
    def dfs(curr):
        visited[curr], count = True, 0

        for next in range(1, N+1):
            if lst[curr][next] and not visited[next]:
                count += (dfs(next) + 1) # child + 자기 자신
        return count

    results = [0] * (N+1)

    for i in range(1, N+1):
        visited = [False] * (N+1)
        results[i] = dfs(i)
    return results

biggerCount = countNode(N, bigger)
smallerCount = countNode(N, smaller)

answer = 0
middle = (N+1) // 2
for i in range(1, N+1):
    # 중간갯수 이상 혹은 이하
    if smallerCount[i] >= middle or biggerCount[i] >= middle:
        answer += 1

print(answer)
