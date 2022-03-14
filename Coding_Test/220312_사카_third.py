# 2 2 2
# 1 1
# 2 2
# ans :=> 12
# 51 37 1
# 17 19
# 대각선을 항상 한번은 지나쳐야 하고, 최단경로로
# https://www.youtube.com/watch?v=oOSIdBO79

"""
문제의 핵심은 대각선을 결정하게 되었다면, 대각선을 위쪽에서 타든, 아래쪽에서 타든 최단경로는 변함이 없다는 것이다.
"""

import sys
input = sys.stdin.readline

w, h, D = map(int, input().split())
diagonals = [list(map(int, input().split())) for _ in range(D )]
MOD = 10000019
dp = [[0] * (h + 1) for __ in range(w + 1)]
dp[0][0] = 1

# Part1. 먼저 Table에 대각선이 없는, dp를 구한다.
for i in range(w + 1):
    for j in range(h + 1):
        if i == 0 and j == 0:
            continue
        dp[i][j] = 0
        if i > 0: #
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]
        dp[i][j] %= MOD # 파이썬은 사칙연산할 때 그 수가 크면 클수록 더 오래 걸린다. 따라서, 미리미리 이렇게 해주는 것이 좋다.

ans = 0
for diag in diagonals:
    # O -> A -> B -> X
    x, y = diag
    cntAB = (dp[x][y - 1] * dp[w - x + 1][h - y]) % MOD
    # O -> B -> A -> X
    x, y = diag
    cntBA = (dp[x - 1][y] * dp[w - x][h - y + 1]) % MOD
    ans += (cntAB + cntBA) % MOD
    ans %= MOD
print(ans)
