"""
그리디 or DP / 그리디로 풀었기 때문에, DP로도 풀어봄
이 문제가 그리디가 되는 이유는 weights가 배수관계이기 때문이다.
그걸 꼭 기억하고, 배수가 아니라면 그리디는 접근하지 않는 것이 좋다.
"""

# 1번 문제
# 4578
# 1 4 99 35 50 1000 => ans : 2308

# 1999
# 2 11 20 100 200 600 => ans : 2798

import sys
input = sys.stdin.readline
N = int(input())
costs = list(map(int,input().split()))
weights = [1, 5, 10, 50, 100, 500]
dp = [[0] * (N + 1) for _ in range(6)] # 숫자4578을 만드는데, 동전 6개로 만들 수 있는 최소 가중치 값

for i in range(N + 1):
    dp[0][i] = costs[0] * i # 숫자 1로 만들 수 있는 개수를 초기화 시켜주는 문장

for a in range(1, 6): # 1원은 초기화했기 때문에
    for b in range(1, N + 1):
        dp[a][b] = dp[a-1][b]

        if b - weights[a] >= 0:
            dp[a][b] = min(dp[a][b], dp[a][b-weights[a]] + costs[a])

print(dp[5][N])

