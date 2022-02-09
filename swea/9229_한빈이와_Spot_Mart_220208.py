"""
2 <= N <= 1000
2봉지를 고르는 방식 Brute-force : O(n^2) = 1,000,000 < 1억

따라서, Brute-force로 풀어도 Solution 나옴
물론 greedy나 이분탐색 하면 더 시간이 빨리 나올 것 같긴 하지만 파이썬을 지원안해줘서 pass
"""

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    _max = -int(1e9)

    for i in range(len(data)):
        left = data[i]
        for j in range(i + 1, len(data)):
            right = data[j]

            if _max <= left + right <= m:
                _max = max(_max, left + right)
    if _max == -int(1e9): _max = -1
    print("#{} {}".format(tc, _max))