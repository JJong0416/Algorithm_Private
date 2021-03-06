"""
풀기 전:
일단 Brute-force는 n의 범위가 1부터 2000이고, 1과 2로만 구성된걸로 해도 2천만이 나오므로 TLE가 나올 것이다.
그리고 1234567을 나눈 값이라고 하니, 큰 값일 가능성이 매우 높다.
또한, 이전의 데이터를 통해 계산할 수 있기  때문에 DP일 가능성이 매우 높다.
"""
def solution(n):
    if n == 1:
        return 1

    dp = [0 for _ in range(n + 1)]

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n] % 1234567
"""
초기 풀이 :
dp = [0 for _ in range(n+1)]

dp[1] = 1 # 1을 만드는 경우의 수는 1가지
dp[2] = 2 # 2를 만드는 경우의 수는 2가지
dp[3] = dp[1] + dp[2] # 3을 만드는 경우의 수는
dp[4] = dp[2] + dp[3] # 5가지
dp[5] = dp[3] + dp[4] # 8가지

이 풀이가 맞다. 맨 처음 dp[6] 13이 아닌 11로 계산한 상태라 생각보다 오래 걸림.
"""