# Math
import sys
import math

N, M = map(int, sys.stdin.readline().split())

# answer(N,M) = answer(N/gcd, M/gcd) * gcd = (M/gcd - 1) * gcd = M - gcd

answer = M - math.gcd(N,M)

print(answer)
