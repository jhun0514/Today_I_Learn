# Greedy
import sys

N = int(sys.stdin.readline())
lst, answer = list(map(int, sys.stdin.readline().split())), 0

while len(lst) > 1:
    tmp = max(lst)
    ind = lst.index(tmp)
    if 0 == ind:
        answer += (tmp - lst[ind+1])
    elif ind == len(lst)-1:
        answer += (tmp - lst[ind-1])
    else:
        maxT = max(lst[ind-1], lst[ind+1])
        answer += (tmp - maxT)
    lst.remove(tmp)

print(answer)
