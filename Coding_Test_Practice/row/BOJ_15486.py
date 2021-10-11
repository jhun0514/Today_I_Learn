# DP
import sys

N, T, P = int(sys.stdin.readline()), [], []
DP, maxP = [0] * (N+1), 0
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    T.append(x)
    P.append(y)
for i in range(N):
    maxP = max(maxP,DP[i])
    if i+T[i] > N:
        continue
    DP[i+T[i]] = max(maxP+P[i],DP[i+T[i]])
print(max(DP))

# N:7
# D : 1     2   3   4   5   6   7
# T : 3 	5	1	1	2	4	2
# P : 10	20	10	20	15	40	200
#maxp:0     0   0   10  30  30  45
#dp:  0     0   0   10  30  20  45
