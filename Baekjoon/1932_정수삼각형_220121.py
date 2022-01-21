"""
보자마자 DP이겠구나 생각했음. 하나하나 써보면서 규칙성을 찾아보자

dp[0][0] = 7 => dp[0][0]
dp[1][0] = 7 + 3 => dp[0][0] + data[1][0]
dp[1][1] = 7 + 8 => dp[0][0] + data[1][1]
dp[2][0] = 7 + 3 + 8 => dp[1][0] + data[2][0]
dp[2][1] = 7 + 3 + 1 or 7 + 8 + 1 => dp
dp[2][2] = 7 + 8 + 0
"""
import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N):
    for j in range(len(data[i])):
        if j == 0:
            data[i][j] = data[i-1][j] + data[i][j]
        elif j == len(data[i]) -1:
            data[i][j] = data[i-1][j-1] + data[i][j]
        else:
            data[i][j] = max(data[i-1][j-1] + data[i][j], data[i-1][j] + data[i][j])

print(max(map(max,data)))

"""
max(map(max,array))) 알아두면 유용하다.
"""
