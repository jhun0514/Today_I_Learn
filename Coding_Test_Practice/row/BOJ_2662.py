# DP
import sys

n, m = map(int, sys.stdin.readline().split())
lst = [0]

for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split()))[1:])

# 각 금액 투자했을 때 얻을 수 있는 최대 이익
dp = [0 for _ in range(n + 1)]
# dp 저장된 값을 얻기 위해서 투자한 비율
companies = [[] for _ in range(n + 1)]

# 첫기업부터 차례로 투자
for i in range(m):
    # n원부터 0원을 투자할 수 있다고 가정할 때를 모두 검사
    for j in range(n, -1, -1):
        cost = 0
        # j원을 투자할 때 얻을 수 있는 최대 금액을 찾은 후 저장
        for k in range(1, j + 1):
            if dp[j-k] + lst[k][i] > dp[j]:
                dp[j] = dp[j-k] + lst[k][i]
                companies[j] = []
                for z in companies[j-k]:
                    companies[j].append(z)
                cost = k
        companies[j].append(cost)
print(dp[-1])
print(*companies[-1])
