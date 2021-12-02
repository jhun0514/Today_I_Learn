# simulation
import sys

N = sys.stdin.readline().rstrip().split(":")
for i in range(len(N)):
    if N[i] == ' ':
        N[i] = "0000"
    if len(N[i]) < 4:
        N[i] = "0"*(4-len(N[i]))+N[i]
if len(N) < 8:
    for i in range(8-len(N)):
        N.insert(N.index("0000"), "0000")
if len(N) > 8:
    del N[N.index("0000")]
print(":".join(N))
