# math
import sys
from math import gcd
from math import sqrt

n = int(sys.stdin.readline().rstrip())
lst = list(int(sys.stdin.readline().rstrip()) for _ in range(n))
lst.sort()
substract, answer = list(), list()

for i in range(1, n):
    substract.append(lst[i] - lst[i - 1])

gcdNum = substract[0]
for i in range(1, len(substract)):
    gcdNum = gcd(gcdNum, substract[i])

for i in range(2, int(sqrt(gcdNum)) + 1):
    if gcdNum % i == 0:
        answer.append(i)
        answer.append(gcdNum//i)
answer.append(gcdNum)
answer = list(set(answer))
answer.sort()
print(*answer)
