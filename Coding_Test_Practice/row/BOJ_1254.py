# Brute Force
from sys import stdin

A, B = list(stdin.readline().rstrip()), []

if len(A) == 1:
    print(1)
else:
    for i in range(len(A)):
        midLen, answer = ((len(A)-i) // 2), True
        if midLen == 0:
            print(len(A) * 2 -1)
            break
        for j in range(midLen):
            if A[i + j] != A[len(A)-1-j]:
                answer = False
                break
        if answer:
            print(len(A)+i)
            break
