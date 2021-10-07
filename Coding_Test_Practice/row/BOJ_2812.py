# Greedy
import sys
N, K = map(int, sys.stdin.readline().split())
lst, num, tmp = list(sys.stdin.readline()), K, []

for i in range(N):
    while tmp and num > 0 and tmp[-1] < lst[i]:
        tmp.pop()
        num -= 1
    tmp.append(lst[i])

print(''.join(tmp[:N-K]))

# 그리디 하게 제일 큰 수 가 앞으로 오면 된다.
# 1924
# 94
