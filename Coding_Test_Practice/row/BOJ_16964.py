# DFS
import sys

N = int(sys.stdin.readline().rstrip())
lst, plst = [[] for _ in range(N+1)], [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)

cmp = list(map(int, sys.stdin.readline().split()))

def findP(x, parent):
    for e in lst[x]:
        if e == parent:
            continue
        findP(e,x)
        plst[e] = x

findP(1, -1)
st = [1]
for i in range(1,N):
    while st and st[-1] != plst[cmp[i]]:
        st.pop()
    if not st:
        print(0)
        exit(0)
    st.append(cmp[i])
print(1)
