# Greedy
import sys

N, answer = int(sys.stdin.readline().rstrip()), 0
px, py = map(int, sys.stdin.readline().split())

for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    if x < py:
        if y > py:
            py = y
        else:
            continue
    else:
        answer += (py - px)
        px, py = x, y

answer += (py - px)
print(answer)
