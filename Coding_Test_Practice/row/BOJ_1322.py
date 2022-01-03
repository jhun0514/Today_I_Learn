# bit
import sys

X, K = map(int,(sys.stdin.readline().split()))
bx, bk = [0] * 64, [0] * 64
bx.extend(list(map(int,bin(X)[2:])))
bk.extend(list(map(int,bin(K)[2:])))
bx.reverse()
bk.reverse()
bitLen = max(len(bin(X)[2:]), len(bin(K)[2:]))

bInd, kInd, answer = 0, 0, 0
while (kInd < bitLen):
    if (bx[bInd] == 0):
        answer += (1 << bInd) * bk[kInd]
        kInd += 1
    bInd += 1

print(answer)
