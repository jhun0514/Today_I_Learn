# Brute Force
import sys

N, lst, dic, number, answer = int(sys.stdin.readline().rstrip()), [], {}, 9, 0

for i in range(N):
    tmp = sys.stdin.readline().rstrip()
    lst.append(tmp)
    for j in range(len(tmp)):
        alphb = lst[i][j]
        if alphb not in dic:
            dic[alphb] = 0
        dic[alphb] += 10 ** (len(tmp) - j - 1)

sortedDic = sorted(dic.items(), reverse=True, key=lambda x: x[1])
for i in range(len(sortedDic)):
    answer += dic[sortedDic[i][0]]*number
    number -= 1
print(answer)
