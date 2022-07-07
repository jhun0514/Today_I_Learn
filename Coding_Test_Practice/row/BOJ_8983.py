# Binary Search

import sys

M, N, L = map(int, sys.stdin.readline().split())

hunter = sorted(list(map(int, sys.stdin.readline().split())))
animal = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count = 0

for x, y in animal:
    left, right = 0, M-1
    if y <= L:
        while left < right:
            mid = (left + right) // 2
            if hunter[mid] < x:
                left = mid + 1
            else:
                right = mid
        if (abs(x - hunter[right]) + y) <= L:
            count += 1
        elif (abs(x - hunter[right-1]) + y) <= L:
            count += 1
print(count)
