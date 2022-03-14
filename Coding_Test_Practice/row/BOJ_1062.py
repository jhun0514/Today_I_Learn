# Bitmask
import sys
import itertools

n, k = map(int, sys.stdin.readline().split())

if k < 5:
    print(0)
elif k > 25:
    print(n)
else:
    k -= 5
    must, lst, count = {'a', 'n', 't', 'i', 'c'}, [], 0
    alpha = {ky: v for v, ky in enumerate((set(map(chr, range(ord('a'), ord('z') + 1))) - must))}
    for _ in range(n):
        tmp = 0
        for c in set(input()) - must:
            tmp |= (1 << alpha[c])
        lst.append(tmp)
    power_by_2 = (2 ** i for i in range(21))
    for comb in itertools.combinations(power_by_2, k):
        test, tmp = sum(comb), 0
        for cb in lst:
            if test & cb == cb:
                tmp += 1
        count = max(count, tmp)
    print(count)
