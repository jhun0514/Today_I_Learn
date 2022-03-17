# Two Pointer
import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
closeZero, val = [], float('inf')

for i in range(n-2):
    leftPivot, rightPivot = i+1, n-1
    while leftPivot < rightPivot:
        tmp = lst[i] + lst[leftPivot] + lst[rightPivot]
        if abs(tmp) < abs(val):
            val = tmp
            closeZero = [lst[i], lst[leftPivot], lst[rightPivot]]

        if tmp > 0:
            rightPivot -= 1
        elif tmp < 0:
            leftPivot += 1
        else:
            break

for i in closeZero:
    print(i, end=" ")
