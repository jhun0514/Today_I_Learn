# Brute Force
import sys

N, M = map(int,sys.stdin.readline().split())
lst = [list(int(d) for d in sys.stdin.readline().rstrip()) for _ in range(N)]
K, tmp, lDic = int(sys.stdin.readline()), [], dict()
cnd = K%2

for i in range(N): # 0의 개수와 k의 홀짝이 같으면 저장 / 다르면 켜진행으로 만들수없다.
    if lst[i].count(0)%2 == cnd and lst[i].count(0) <= K:
        tmp.append(lst[i])
for i in range(len(tmp)): # 똑같은 배열이 있으면 +1
    if str(tmp[i]) in lDic:
        lDic[str(tmp[i])] += 1
    else:
        lDic[str(tmp[i])] = 1
if lDic:
    print(max(lDic.values()))
else:
    print(0)
