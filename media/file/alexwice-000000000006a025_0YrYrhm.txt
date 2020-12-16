from collections import defaultdict as ddic
from itertools import combinations, permutations, product
import bisect
import heapq
import sys
stdout = sys.stdout
rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split()))

MOD = 10**9 + 7
def guess(x):
    print(x)
    stdout.flush()
    return rr()

def solve(N, picks, A):
    A.sort()
    P = [0]
    for x in A:
        P.append(P[-1] + x)

    ans = float('inf')
    for i in range(N - picks + 1):
        bns = (A[i+picks-1]) * picks
        bns -= P[i + picks] - P[i]
        ans = min(ans, bns)
    return ans

T = rri()
for tc in range(1, T+1):
    N,P = rrm()
    A = rrm()
    ans = solve(N, P, A)
    print("Case #{}: {}".format(tc, ans))
