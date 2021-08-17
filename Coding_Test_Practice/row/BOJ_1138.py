# Simulation
from sys import stdin
N = int(stdin.readline())
lst, answer = list(map(int, stdin.readline().split())), []
answer.append(N)
for i in range(N-2,-1,-1):
    if lst[i] == 0:
        answer[:0] = [i+1]
        continue
    count = 0
    for j in range(len(answer)):
        if answer[j] > i:
            count += 1
        if count == lst[i]:
            answer = answer[:j+1] + [i+1] + answer[j+1:]
            break
print(*answer)
