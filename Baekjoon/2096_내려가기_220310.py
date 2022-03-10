"""
어떻게 풀어야 할까?
1 <= N <= 100,000
여기서, bfs로 풀게 되면 시간초과가 날 것이다.
dp로 풀 수 있는가 ? 한번 dp로 풀어보자
이런 제엔장!!!!!!
N줄에 3개
즉 전체 크기는 N * 3이라는 것이다.

"""
# 풀이1. bfs => 시간초과X, 메모리 초과
"""
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, 1, 1]
dy = [-1, 0, 1]

def bfs(sx, sy):
    global _min, _max

    dq = deque()
    dq.append((sx, sy, data[sx][sy]))

    while dq:
        x, y, tot = dq.popleft()

        if x == N-1:
            _min = min(_min, tot)
            _max = max(_max, tot)

        for d in range(3):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                dq.append((nx, ny, tot + data[nx][ny]))


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
_min, _max = int(1e9), -int(1e9)

for i in range(N):
    bfs(0, i)

print(_max, _min)
"""
import sys

input = sys.stdin.readline

N = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(N):
    a, b, c = map(int, input().split())

    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_dp[j], max_dp[j + 1])
            min_tmp[j] = a + min(min_dp[j], min_dp[j + 1])

        elif j == 1:
            max_tmp[j] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            min_tmp[j] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])

        else:
            max_tmp[j] = c + max(max_dp[j], max_dp[j - 1])
            min_tmp[j] = c + min(min_dp[j], min_dp[j - 1])

    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]

print(max(max_dp), min(min_dp))