# Simulation
import sys

N = int(sys.stdin.readline())
lst, answer,count = list((map(int, sys.stdin.readline().split()))), [], 1

while len(answer) != N:
    temp,subanswer = [],[]
    for i in range(len(lst)):
        if lst[i]%2 == 1:
            subanswer.append(lst[i]*(2**(count-1)))
        else:
            temp.append(lst[i])
    lst = temp
    for i in range(len(lst)):
        lst[i] = lst[i]//2
    count += 1
    subanswer.sort(reverse=True)
    for i in subanswer:
        answer.append(i)
print(*answer)

# 4 8 6 3 12 9
#
# count = 3
# sub = 3 9
# temp = 4 8 6 12
#
# lst =
#
# answer = 9 3 6 12 4 8
